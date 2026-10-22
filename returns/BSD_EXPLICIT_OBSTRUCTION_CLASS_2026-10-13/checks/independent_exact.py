"""Independent rational and polynomial checks; no Sha or L-value inputs.

Run: python3 checks/independent_exact.py (requires sympy).
Local solubility at all places uses Miller--Stoll, not this finite checker.
"""
from fractions import Fraction as Q
from math import isqrt
from pathlib import Path
import json
import sympy as s

d = 43737
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def mul(a,b): return (a[0]*b[0]+d*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def power(a,n):
    z=(Q(1),Q(0))
    for _ in range(n): z=mul(z,a)
    return z
def norm(a): return a[0]**2-d*a[1]**2
def div(a,b): return tuple(z/norm(b) for z in mul(a,(b[0],-b[1])))
def kcoord(c0,c1): return (Q(c0)+Q(c1)/2,Q(c1)/2)
eps=(Q(23423),Q(112))
assert norm(eps)==1
small=[]
for b in range(1,225):
    aa=d*b*b+4; a=isqrt(aa)
    if a*a==aa and (a-b)%2==0: small.append([a,b])
assert small==[[46846,224]]
assert (-4)%3==2 and all((a*a)%3!=2 for a in range(3))
assert div((Q(1464),Q(7)),(Q(1464),Q(-7)))==eps
P=[(Q(1778638,9),Q(1169009812,27)),
   (Q(6466626346478,36517849),Q(2366996613841078836,220677361507))]
def descent(X,y):
    assert y*y+y==X**3-19766893413*X-1937478573143510
    return ((X-Q(11*d,3))*(y+Q(1,2)),
            -4*X*X+Q(161*d,6)*X-Q(785*d*d,18))
f1,f2=map(lambda p:descent(*p),P)
assert f1==kcoord(Q(393863215501942,243),Q(-1249565229839,81))
rho=kcoord(Q(-54179073,352403588),Q(-527625,352403588))
assert div(f2,power(f1,2))==power(rho,5)
gamma=kcoord(-5829,-56)
alpha=div(gamma,(gamma[0],-gamma[1]))
assert norm(gamma)==11**4
assert alpha==kcoord(Q(68266265,14641),Q(655984,14641)) and norm(alpha)==1

X,D=s.symbols('X D')
cubic=X**3-s.Rational(31,3)*D**2*X-s.Rational(2501,108)*D**3
qq=-4*X**2+s.Rational(161,6)*D*X-s.Rational(785,18)*D**2
assert s.expand((X-s.Rational(11,3)*D)**2*cubic-D*qq**2-(X-s.Rational(14,3)*D)**5)==0
u,v=s.symbols('u v'); h=u*u-d*v*v
pp=u**5+10*d*u**3*v*v+5*d*d*u*v**4
qp=5*u**4*v+10*d*u*u*v**3+d*d*v**5
rr=23423*pp+112*d*qp; ss=112*pp+23423*qp
assert s.expand(rr**2-d*ss**2-h**5)==0
xt=h+s.Rational(14*d,3)
qt=qq.subs({X:xt,D:d})
eq=2*ss+8*h*h+21*d*h+11*d*d
assert s.expand(eq-2*(ss-qt))==0
diff=s.expand(rr**2-(h+d)**2*cubic.subs({X:xt,D:d}))
assert s.expand(diff-eq*s.Rational(d,2)*(ss+qt))==0

base=Path(__file__).resolve().parents[1]
model=json.loads((base/'implementation/FISHER_MODEL.json').read_text())
xs=s.symbols('x0:5'); env={str(x):x for x in xs}
mat=s.Matrix([[s.sympify(z.replace('^','**'),locals=env) for z in row] for row in model['matrix']])
quadrics=[s.sympify(z.replace('^','**'),locals=env) for z in model['signed_pfaffians']]
assert mat+mat.T==s.zeros(5)
assert all(s.expand(z)==0 for z in s.Matrix([quadrics])*mat)
for i in range(5):
    ii=[j for j in range(5) if j!=i]; mm=mat.extract(ii,ii)
    pf=(-1)**i*(mm[0,1]*mm[2,3]-mm[0,2]*mm[1,3]+mm[0,3]*mm[1,2])
    assert s.expand(pf-quadrics[i])==0
jac=s.Matrix(quadrics).jacobian(xs); witnesses=[]
for row in json.loads((base/'implementation/LOCAL_WITNESSES.json').read_text()):
    w=row['nonsingular_witness']
    if w is None: continue
    ell=row['prime']; at=dict(zip(xs,w['point']))
    assert all(int(q.subs(at))%ell==0 for q in quadrics)
    minor=int(jac.extract(w['minor_rows'],w['minor_columns']).subs(at).det())%ell
    assert minor==w['minor_value'] and minor!=0
    ij=w['omitted_equations']; pivot=int(mat[ij[0],ij[1]].subs(at))%ell
    assert pivot==w['pfaffian_syzygy_unit_pivot'] and pivot!=0
    witnesses.append(ell)

result={"norm_epsilon":1,"fundamental_unit_scan":{"b_range":[1,224],"solutions":small,
 "norm_minus_one_excluded_mod_3":True},"points_on_A":2,"point_fifth_power_relation":True,
 "generic_descent_norm_identity":True,"fisher_theta_equals_epsilon":True,
 "split11_class_norm":1,"affine_cover_map_identity":True,
 "pfaffians_and_syzygy":True,"independently_verified_Hensel_witness_primes":witnesses,
 "scope":"Exact arithmetic and symbolic identities; local Selmer membership and global nontriviality are in written proof."}
out=Path(__file__).resolve().parents[1]/'outputs/INDEPENDENT_EXACT.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
