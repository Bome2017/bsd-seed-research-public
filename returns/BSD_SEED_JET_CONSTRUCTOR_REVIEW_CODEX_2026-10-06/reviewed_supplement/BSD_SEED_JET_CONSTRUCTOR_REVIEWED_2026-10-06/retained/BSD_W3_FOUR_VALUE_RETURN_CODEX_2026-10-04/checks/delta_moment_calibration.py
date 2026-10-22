"""Independent exact calibration on Delta, NOT on the BSD seed.

Construct Delta's even period polynomial using Manin relations and T_2=-24.
Compare the one-layer polynomial moment formula with a deeper Riemann sum.
Only sympy is used for the small rational nullspace; arithmetic is exact.
"""
from fractions import Fraction
from math import comb, gcd, lcm
import json
import sympy as sp

DEGREE = 10

def transform(poly, A, B, C, D, upto=None, modulus=None):
    """P(AX+BY,CX+DY), coefficients of X^(d-h)Y^h."""
    d=len(poly)-1; cap=d if upto is None else upto
    out=[0]*(cap+1)
    for j,c in enumerate(poly):
        if not c: continue
        for u in range(min(d-j,cap)+1):
            for v in range(min(j,cap-u)+1):
                out[u+v]+=c*comb(d-j,u)*comb(j,v)*A**(d-j-u)*B**u*C**(j-v)*D**v
    return [x%modulus for x in out] if modulus else out

def period_polynomial():
    d=DEGREE; cols=[]
    for j in range(d+1):
        q=[int(i==j) for i in range(d+1)]
        S=transform(q,0,1,-1,0)
        R=transform(q,-1,1,-1,0)
        RR=transform(q,0,-1,1,-1)
        t=[sum(xs) for xs in zip(transform(q,2,0,0,1),transform(q,1,0,0,2),transform(q,1,1,0,2))]
        neg=transform(q,1,1,-2,0)
        cols.append([q[i]+S[i] for i in range(d+1)]
                    +[q[i]+R[i]+RR[i] for i in range(d+1)]
                    +[t[i]-neg[i]+24*q[i] for i in range(d+1)]
                    +[q[i] if i%2 else 0 for i in range(d+1)])
    mat=sp.Matrix(cols).T; ns=mat.nullspace()
    assert len(ns)==1
    scale=lcm(*(int(x.q) for x in ns[0])); r=[int(x*scale) for x in ns[0]]
    common=gcd(*r); r=[x//common for x in r]
    if r[0]<0:r=[-x for x in r]
    assert mat*sp.Matrix(r)==sp.zeros(mat.rows,1)
    return r

def convergents(a,b):
    pp,p=0,1; qq,q=1,0
    out=[(1,0)]
    while b:
        c,a,b=a//b,b,a%b
        pp,p=p,c*p+pp; qq,q=q,c*q+qq
        out.append((p,q))
    return out

def cusp_symbol(r,a,b,upto=3,modulus=None):
    """Integral symbol of {infinity}-{a/b} from unimodular paths."""
    out=[0]*(upto+1); conv=convergents(a,b)
    for (a0,b0),(a1,b1) in zip(conv,conv[1:]):
        # Edge {a0/b0}-{a1/b1}; first column maps infinity, second maps zero.
        det=a0*b1-a1*b0
        assert det in (-1,1)
        # Negating either column leaves its cusp unchanged and makes det=1.
        if det==-1:a1,b1=-a1,-b1
        term=transform(r,b1,-a1,-b0,a0,upto,modulus)
        out=[x+y for x,y in zip(out,term)]
    return [x%modulus for x in out] if modulus else out

def tau(n):
    # q product_(m>=1)(1-q^m)^24, sufficient for the selected n.
    a=[1]+[0]*(n-1)
    for m in range(1,n):
        b=[0]*n
        for j in range(min(24,(n-1)//m)+1):
            v=(-1)**j*comb(24,j)
            for i in range(n-j*m): b[i+j*m]+=v*a[i]
        a=b
    return a[n-1]

def unit_root(p,ap,precision):
    m=p**precision; a=ap%m
    assert a%p
    for _ in range(precision+2):a=(ap-p**11*pow(a,-1,m))%m
    assert (a*a-ap*a+p**11)%m==0
    return a

def run():
    r=period_polynomial(); p=11; precision=4; m=p**precision
    hecke=[]
    for ell in (3,5):
        v=transform(r,ell,0,0,1)
        for a in range(ell):
            term=transform(cusp_symbol(r,a,ell,upto=DEGREE),1,a,0,ell)
            v=[x+y for x,y in zip(v,term)]
        assert v==[tau(ell)*x for x in r]
        hecke.append({'ell':ell,'eigenvalue':tau(ell)})
    ap=tau(p); alpha=unit_root(p,ap,precision)
    direct=[]; fine=[]
    for s in (2,3,4):
        total=0
        for a in range(1,p):
            c=cusp_symbol(r,a,p,upto=s,modulus=m)
            moment=sum(comb(s,h)*pow(comb(DEGREE,h),-1,m)*a**(s-h)*p**h*c[h] for h in range(s+1))%m
            omega=pow(a,p**precision,m)
            total+=pow(omega,-s,m)*moment
        direct.append(total*pow(alpha,-1,m)%m)
    sums=[0]*3
    for a in range(1,p**precision):
        if a%p==0:continue
        c=cusp_symbol(r,a,p**precision,upto=0,modulus=m)[0]
        omega=pow(a,p**precision,m)
        principal=a*pow(omega,-1,m)%m
        for j,s in enumerate((2,3,4)):sums[j]=(sums[j]+pow(principal,s,m)*c)%m
    fine=[x*pow(alpha,-precision,m)%m for x in sums]
    assert direct==fine, (direct,fine)
    # The p-stabilization correction is alpha^-1 phi(pD)(pX,Y):
    # its h-coordinate has p^(10-h), invisible here for h<=4.
    return {'status':'PASS','curve':'NOT THE SEED: classical cuspform Delta, level 1 weight 12',
            'period_polynomial':r,'p':p,'tau_p':ap,'alpha_mod_p4':alpha,
            'exponents':[2,3,4],'one_layer_values':direct,'level_p4_riemann_values':fine,
            'riemann_terms':(p-1)*p**3,'primitive_polynomial':gcd(*r)==1,
            'additional_hecke_checks':hecke,
            'seed_values_computed':False,'scope':'Exact modular-symbol calibration of moment formula, not seed normalization or uniform nonvanishing'}

if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
