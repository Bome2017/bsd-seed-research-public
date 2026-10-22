#!/usr/bin/env python3
"""Exact local detector for the submitted 43737 isogeny control.

Standard library only. The rank, 5-saturation, and all-place descent theorem
application are retained inputs. No L-value, regulator, class-group computation,
or fundamental-unit assertion enters these checks. This is not a seed verifier.
"""
from __future__ import annotations
import ast
import itertools
import json
from dataclasses import dataclass
from fractions import Fraction as Q
from typing import Optional

D = 43737


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


@dataclass(frozen=True)
class Quad:
    a: Q
    b: Q = Q(0)

    def __post_init__(self):
        object.__setattr__(self, 'a', Q(self.a))
        object.__setattr__(self, 'b', Q(self.b))

    def __add__(self, other):
        other = other if isinstance(other, Quad) else Quad(other)
        return Quad(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Quad(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-other if isinstance(other, Quad) else -Q(other))

    def __mul__(self, other):
        other = other if isinstance(other, Quad) else Quad(other)
        return Quad(self.a*other.a + D*self.b*other.b,
                    self.a*other.b + self.b*other.a)

    __rmul__ = __mul__

    def conj(self):
        return Quad(self.a, -self.b)

    def norm(self):
        return self.a*self.a - D*self.b*self.b

    def inv(self):
        n = self.norm()
        if n == 0:
            raise ZeroDivisionError('zero quadratic-field element')
        return Quad(self.a/n, -self.b/n)

    def __truediv__(self, other):
        other = other if isinstance(other, Quad) else Quad(other)
        return self*other.inv()

    def __pow__(self, n: int):
        if type(n) is not int:
            raise TypeError('integer exponent required')
        if n < 0:
            return self.inv()**(-n)
        result = Quad(1)
        base = self
        while n:
            if n & 1:
                result = result*base
            n //= 2
            base = base*base
        return result


def vp_int(n: int, p: int) -> int:
    if n == 0:
        raise ValueError('valuation of zero is not a finite integer')
    n = abs(n)
    ans = 0
    while n % p == 0:
        n //= p
        ans += 1
    return ans


def vp_q(a: Q, p: int) -> int:
    if not a:
        raise ValueError('valuation of zero')
    return vp_int(a.numerator, p)-vp_int(a.denominator, p)


def residue(a: Q, p: int) -> int:
    if a.denominator % p == 0:
        raise ValueError('nonintegral residue')
    return a.numerator*pow(a.denominator, -1, p) % p


def hensel_x11(precision: int) -> int:
    """Root of x^2-x-10934 equal to 1 modulo 11."""
    if type(precision) is not int or precision < 1:
        raise ValueError('positive precision required')
    root, modulus = 1, 11
    require((root*root-root-10934) % modulus == 0, 'initial root')
    for _ in range(1, precision):
        correction = (-((root*root-root-10934)//modulus)
                      *pow(2*root-1, -1, 11)) % 11
        root += correction*modulus
        modulus *= 11
        require((root*root-root-10934) % modulus == 0, 'Hensel root')
    return root


def local_data(z: Quad, precision: int = 12) -> dict:
    """Return certified leading local data; reject a zero/insufficient jet.

    sqrt(D)=2*x-1 modulo 11^precision. The error in z has valuation
    >= precision+v_11(b); a leading residue is used only strictly below it.
    """
    root = hensel_x11(precision)
    a = z.a + z.b*(2*root-1)
    if a == 0:
        raise ValueError('zero approximation is not a leading digit')
    v = vp_q(a, 11)
    if z.b and v >= precision + vp_q(z.b, 11):
        raise ValueError('insufficient p-adic precision')
    leading = a/(Q(11)**v)
    unit = residue(leading, 11)
    logs = {pow(2, j, 11): j % 5 for j in range(10)}
    require(len(logs) == 10, '2 must generate F_11^*')
    return {'v_11': v, 'unit_residue_mod_11': unit,
            'signature_mod_5': [v % 5, logs[unit]]}


def on_A(point) -> bool:
    x,y = map(Q, point)
    return y*y+y == x**3-19766893413*x-1937478573143510


def descent(point) -> Quad:
    x,y = map(Q, point)
    return Quad((x-Q(11*D, 3))*(y+Q(1, 2)),
                -4*x*x+Q(161*D, 6)*x-Q(785*D*D, 18))


# Small exact polynomial arithmetic, represented by exponent-tuple dictionaries.
Poly = dict[tuple[int, ...], Q]


def pc(a, n=5) -> Poly:
    a = Q(a)
    return {} if not a else {(0,)*n: a}


def px(j, n=5) -> Poly:
    exponents = [0]*n
    exponents[j] = 1
    return {tuple(exponents): Q(1)}


def pa(a: Poly,b: Poly) -> Poly:
    out = dict(a)
    for k,v in b.items():
        out[k] = out.get(k,Q(0))+v
        if out[k] == 0:
            del out[k]
    return out


def ps(a: Poly,c) -> Poly:
    c = Q(c)
    return {k:v*c for k,v in a.items() if v*c}


def pm(a: Poly,b: Poly) -> Poly:
    out: Poly = {}
    for k,u in a.items():
        for l,v in b.items():
            e = tuple(x+y for x,y in zip(k,l))
            out[e] = out.get(e,Q(0))+u*v
    return {k:v for k,v in out.items() if v}


def pp(a: Poly,n: int, dim=5) -> Poly:
    if type(n) is not int or n < 0:
        raise ValueError('nonnegative integer polynomial exponent required')
    out = pc(1,dim)
    for _ in range(n):
        out = pm(out,a)
    return out


def parse_poly(text: str) -> Poly:
    """Parse the supplied quadrics with an arithmetic-only AST whitelist."""
    def visit(node):
        if isinstance(node,ast.Constant) and type(node.value) is int:
            return pc(node.value)
        if isinstance(node,ast.Name) and node.id in [f'x{i}' for i in range(5)]:
            return px(int(node.id[1:]))
        if isinstance(node,ast.UnaryOp) and isinstance(node.op,ast.USub):
            return ps(visit(node.operand),-1)
        if isinstance(node,ast.BinOp):
            if isinstance(node.op,ast.Add): return pa(visit(node.left),visit(node.right))
            if isinstance(node.op,ast.Sub): return pa(visit(node.left),ps(visit(node.right),-1))
            if isinstance(node.op,ast.Mult): return pm(visit(node.left),visit(node.right))
            if isinstance(node.op,ast.Pow) and isinstance(node.right,ast.Constant):
                if node.right.value not in (0,1,2): raise ValueError('unexpected exponent')
                return pp(visit(node.left),node.right.value)
        raise ValueError('non-polynomial expression')
    return visit(ast.parse(text.replace('^','**'),mode='eval').body)


def peval(poly: Poly,point,p: Optional[int]=None):
    out=Q(0)
    for exponents,c in poly.items():
        t=c
        for x,e in zip(point,exponents): t*=Q(x)**e
        out+=t
    return out if p is None else residue(out,p)


def pd(poly: Poly,j: int) -> Poly:
    out={}
    for es,c in poly.items():
        if es[j]:
            ee=list(es);ee[j]-=1
            out[tuple(ee)]=c*es[j]
    return out


def det3(a,p):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])) % p


def fisher_check():
    x=[px(i) for i in range(5)]
    matrix=[[{} for _ in range(5)] for _ in range(5)]
    upper={(0,1):ps(x[0],11),(0,2):ps(pa(x[2],ps(x[4],-1)),D),
           (0,3):pa(ps(x[1],-1),x[3]),(0,4):ps(x[3],-1),
           (1,2):ps(pa(x[1],x[3]),-1),(1,3):pa(x[2],x[4]),(1,4):x[4],
           (2,3):ps(x[0],183),(2,4):pa(ps(x[1],1464),ps(x[2],306159)),
           (3,4):pa(ps(x[1],7),ps(x[2],1464))}
    for (i,j),v in upper.items(): matrix[i][j]=v;matrix[j][i]=ps(v,-1)
    pf=[]
    for deleted in range(5):
        a,b,c,d=[i for i in range(5) if i!=deleted]
        p=pa(pa(pm(matrix[a][b],matrix[c][d]),ps(pm(matrix[a][c],matrix[b][d]),-1)),
             pm(matrix[a][d],matrix[b][c]))
        pf.append(ps(p,(-1)**deleted))
    expected=[
      '-7*x1^2 - 2928*x1*x2 - 306159*x2^2 - 7*x1*x3 - 1464*x2*x3 + 183*x0*x4 - 1464*x1*x4 - 306159*x2*x4',
      '-1464*x1^2 - 612318*x1*x2 - 64030968*x2^2 + 183*x0*x3 + 1464*x1*x3 + 306159*x2*x3 + 306159*x1*x4 + 64030968*x2*x4',
      '77*x0*x1 + 16104*x0*x2 - x2*x3 + x1*x4 - 2*x3*x4',
      '-16104*x0*x1 - 3367749*x0*x2 - x1*x3 - x3^2 + 43737*x2*x4 - 43737*x4^2',
      '2013*x0^2 + x1^2 - 43737*x2^2 - x3^2 + 43737*x4^2']
    for actual,text in zip(pf,expected): require(actual==parse_poly(text),'Pfaffian mismatch')
    for row in matrix:
        total={}
        for entry,q in zip(row,pf): total=pa(total,pm(entry,q))
        require(not total,'Pfaffian syzygy')
    local=[]
    for p,point in [(5,[1,0,1,2,3]),(11,[1,0,6,0,6])]:
        require(all(peval(q,point,p)==0 for q in pf),'witness not on reduction')
        found=None
        for rows in itertools.combinations(range(5),3):
            other=[i for i in range(5) if i not in rows]
            pivot=peval(matrix[other[0]][other[1]],point,p)
            if not pivot: continue
            for cols in itertools.combinations(range(1,5),3):
                m=[[peval(pd(pf[i],j),point,p) for j in cols] for i in rows]
                v=det3(m,p)
                if v:
                    found={'p':p,'point':point,'equations_zero_based':list(rows),
                           'variables_zero_based':list(cols),'Jacobian_minor_mod_p':v,
                           'complementary_matrix_entry_mod_p':pivot}
                    break
            if found:break
        require(found is not None,'no suitable Hensel minor')
        local.append(found)
    return {'all_five_Pfaffians_match':True,'all_five_syzygies':True,
            'fresh_local_Hensel_receipts':local,
            'geometric_singularity_Groebner_computation_replayed':False,
            'all_place_solubility':'retained Miller-Stoll application, not these two witnesses'}


# Finite-field polynomial arithmetic for a degree-five irreducibility certificate.
def trim(a,p):
    a=[x%p for x in a]
    while a and a[-1]==0: a.pop()
    return a


def rem(a,b,p):
    a=trim(a,p); b=trim(b,p)
    if not b:raise ZeroDivisionError('zero polynomial')
    while len(a)>=len(b):
        t=a[-1]*pow(b[-1],-1,p)%p;k=len(a)-len(b)
        old_len = len(a)
        for j in range(len(b)): a[k+j]=(a[k+j]-t*b[j])%p
        a=trim(a,p)
        require(len(a) < old_len, 'polynomial remainder did not lower degree')
    return a


def mulmod(a,b,f,p):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return rem(c,f,p)


def powmod(a,n,f,p):
    r=[1]
    while n:
        if n&1:r=mulmod(r,a,f,p)
        n//=2;a=mulmod(a,a,f,p)
    return r


def gcdmod(a,b,p):
    while b:a,b=b,rem(a,b,p)
    return [(x*pow(a[-1],-1,p))%p for x in a]


def main():
    require(D==3*61*239 and D%4==1,'discriminant inputs')
    epsilon=Quad(23423,112)
    gamma=Quad(-5857,-28)
    alpha=gamma/gamma.conj()
    require(epsilon.norm()==1,'unit norm')
    require(gamma.norm()==11**4,'gamma norm')
    require(alpha==Quad(Q(68594257,14641),Q(327992,14641)),'alpha display')
    require(alpha.norm()==1,'alpha norm')
    require(Quad(1464,7).norm()==183,'Fisher norm')
    require(Quad(1464,7)/Quad(1464,-7)==epsilon,'Fisher theta')
    P1=(Q(1778638,9),Q(1169009812,27))
    P2=(Q(6466626346478,36517849),Q(2366996613841078836,220677361507))
    require(on_A(P1) and on_A(P2),'point membership')
    beta1,beta2=descent(P1),descent(P2)
    displayed=Quad(Q(393863215501942,243)-Q(1249565229839,162),-Q(1249565229839,162))
    require(beta1==displayed,'displayed descent value')
    rho=Quad((-Q(54179073)-Q(527625,2))/352403588,-Q(527625,2*352403588))
    require(beta2==beta1**2*rho**5,'exact point relation')
    # Verify the global polynomial norm identity with rational coefficients.
    X=px(0,1)
    linear=pa(X,pc(-Q(11*D,3),1))
    quad=pa(pa(ps(pp(X,2,1),-4),ps(X,Q(161*D,6))),pc(-Q(785*D*D,18),1))
    curve=pa(pa(pp(X,3,1),ps(X,-19766893413)),pc(-Q(1937478573143510)+Q(1,4),1))
    norm=pa(pm(pp(linear,2,1),curve),ps(pp(quad,2,1),-D))
    require(norm==pp(pa(X,pc(-Q(14*D,3),1)),5,1),'descent polynomial norm')
    rows=[]
    for name,z in [('epsilon',epsilon),('alpha11',alpha),('f(P1)',beta1),('f(P2)',beta2)]:
        datum=local_data(z)
        datum['class']=name;rows.append(datum)
    require([r['signature_mod_5'] for r in rows]==[[0,4],[4,0],[0,0],[0,0]],'local detector matrix')
    determinant=(0*0-4*4)%5
    require(determinant==4,'detector determinant')
    cases=0
    for a,b,c in itertools.product(range(5),repeat=3):
        # This is actual local evaluation of epsilon^a alpha^b beta1^(-c),
        # not just multiplication of the displayed two-by-two matrix.
        z=epsilon**a*alpha**b*beta1**(-c)
        sig=local_data(z,40)['signature_mod_5']
        require(sig==[(4*b)%5,(4*a)%5],'signature homomorphism')
        require((sig==[0,0])==(a==0 and b==0),'relation separation')
        cases+=1
    try:local_data(alpha,4)
    except ValueError: pass
    else:raise AssertionError('insufficient precision was accepted')
    # Chebyshev identity and irreducible quintic splitting field.
    t=px(0,1)
    T5=pa(pa(pp(t,5,1),ps(pp(t,3,1),-5)),ps(t,5))
    DD=pa(pa(pp(t,4,1),ps(pp(t,2,1),-3)),pc(1,1))
    require(pa(pp(T5,2,1),pc(-4,1))==pm(pa(pp(t,2,1),pc(-4,1)),pp(DD,2,1)),
            'Chebyshev difference identity')
    require(46846**2-4==224**2*D,'Chebyshev quadratic discriminant')
    f=[-46846,5,0,-5,0,1];xx=[0,1]
    r5=powmod(xx,11**5,f,11)
    r1=powmod(xx,11,f,11)
    r1 += [0]*max(0,2-len(r1));r1[1]-=1
    require(r5==xx and gcdmod(trim(f,11),trim(r1,11),11)==[1], 'quintic irreducibility')
    # Seed comparison only: this one auxiliary place cannot give a 17-detector.
    count=1+sum((y*y-x**3+x*x+66020924*x+65074271436)%11==0
                for x in range(11) for y in range(11))
    require(count==14 and count%17!=0,'seed local group')
    return {'status':'PASS_EXACT_LOCAL_DETECTOR_UNDER_RETAINED_GLOBAL_INPUTS',
            'local_place':'(11, x_K-1); sqrt(d)=1 mod 11',
            'uniformizer':11,'residue_generator':2,'Hensel_root_mod_11_5':hensel_x11(5),
            'local_signatures':rows,'independent_obstruction_matrix_columns':[[0,4],[4,0]],
            'determinant_mod_5':determinant,'all_exponent_relation_cases':cases,
            'descent_polynomial_norm_identity':True,'exact_fP2_fP1_relation':True,
            'fifth_power_precision_countercontrol':'PASS',
            'class_number_or_fundamental_unit_used_in_lower_bound':False,
            'Fisher_model':fisher_check(),
            'splitting_field':{'polynomial':'t^5-5*t^3+5*t-46846','degree':5,
                'irreducible_mod_11':True,'Chebyshev_identity':True,
                'root_formula':'z=(t+224*sqrt(d)/(t^4-3*t^2+1))/2, z^5=epsilon',
                'projective_point_coordinates_computed':False},
            'seed_comparison':{'p':17,'auxiliary_place':11,'number_of_points_mod_11':count,
                'local_full_17_Kummer_group':'zero','new_seed_conclusion':None},
            'retained_not_recomputed':['rank upper bound two and 5-saturation of P1,P2',
               'isogeny/Tamagawa/differential inputs for Miller-Stoll 11',
               'all-place Selmer membership from that theorem',
               'class/unit dimension count if claiming the detector is an isomorphism',
               'global five-chart Groebner smoothness calculation'],
            'new_seed_prime_results':0,'FIN':'UNCHANGED','ORDER9':'UNCHANGED','Q36':'UNCHANGED'}

if __name__=='__main__':
    print(json.dumps(main(),indent=2,sort_keys=True))
