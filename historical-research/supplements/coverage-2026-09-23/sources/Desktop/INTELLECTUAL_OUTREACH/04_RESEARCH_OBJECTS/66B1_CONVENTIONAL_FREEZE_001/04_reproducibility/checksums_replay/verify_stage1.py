#!/usr/bin/env python3
"""Independent Stage-I corroboration for 66b1, not a proof of uniform descent.
No packet computation or data are imported. Requires Python 3 and sympy.
"""
import json
from pathlib import Path
import sympy as s

x,y,X,Y,U,V,q,a,b=s.symbols('x y X Y U V q a b')
f0=y*y+x*y+y-x**3-x*x+2*x+1
f=Y**2-X**3-17*X**2-64*X
assert s.expand(f.subs({X:4*(x-1),Y:8*y+4*x+4})-64*f0)==0
assert s.expand(f0.subs({x:X/4+1,y:(Y-X-8)/8})-f/64)==0
fq=Y**2-X**3-17*q*X**2-64*q*q*X
minq=y*y+x*y-x**3-(17*q-1)*x*x/4-4*q*q*x
assert s.expand(fq.subs({X:4*x,Y:8*y+4*x})-64*minq)==0
fpq=V**2-U*(U-q)*(U-33*q)
minpq=y*y+x*y-x**3+(31*q+1)*x*x/4+2*q*q*x
assert s.expand(fpq.subs({U:q+4*x,V:8*y+4*x})-64*minpq)==0

# Isogeny identity and composition x-coordinate.
fx=X*(X*X+a*X+b)
u=X+a+b/X
v=Y*(1-b/X**2)
D=a*a-4*b
assert s.factor((v*v-u*(u*u-2*a*u+D)).subs(Y*Y,fx))==0
xh=(u-2*a+D/u)/4
xdouble=(X*X-b)**2/(4*fx)
assert s.factor(xh-xdouble)==0
# y composition agrees with tangent-and-chord duplication.
lam=(3*X**2+2*a*X+b)/(2*Y)
ydouble=-Y+lam*(X-xdouble)
yh=v*(1-D/u**2)/8
num=s.together(yh-ydouble).as_numer_denom()[0]
assert s.rem(num,s.Poly(Y**2-fx,Y),Y)==0
assert s.expand((X*X-64)**2+32*X*(X*X+17*X+64)-((X+8)**4+32*X*X))==0


def invs(ai):
    a1,a2,a3,a4,a6=ai
    b2=a1*a1+4*a2; b4=a1*a3+2*a4; b6=a3*a3+4*a6
    b8=a1*a1*a6-a1*a3*a4+4*a2*a6+a2*a3*a3-a4*a4
    return tuple(s.factor(z) for z in (b2*b2-24*b4,-b2**3+36*b2*b4-216*b6,-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6))
assert invs([1,1,1,-2,-1])==(97,-17,528)
assert invs([1,(17*q-1)/4,0,4*q*q,0])==(97*q*q,-17*q**3,528*q**6)
assert invs([1,-(31*q+1)/4,0,-2*q*q,0])==(1057*q*q,34255*q**3,4356*q**6)
assert invs([0,17*q,0,64*q*q,0])[2]==2162688*q**6
assert invs([0,-34*q,0,33*q*q,0])[2]==17842176*q**6


def legendre(n,p):
    t=pow(int(n)%p,(p-1)//2,p)
    return -1 if t==p-1 else t

def v2(n):
    if n<=0: raise ValueError('positive input required')
    return (n&-n).bit_length()-1

def count_curve(p):
    # Count from y^2=x(x^2+17x+64) using a quadratic-residue table,
    # independent of any halving test or character prediction.
    char=[-1]*p
    char[0]=0
    for t in range(1,(p+1)//2): char[(t*t)%p]=1
    return p+1+sum(char[(z*(z*z+17*z+64))%p] for z in range(p))

rows=[]; exceptions=[]; family=[]
for p0 in s.primerange(5,10000):
    p=int(p0)
    if p==11: continue
    n=count_curve(p); val=v2(n)
    criterion=legendre(33,p)==-1 and legendre(-2,p)==-1
    if (val==2)!=criterion: exceptions.append([p,n,val])
    rows.append([p,n,p+1-n,val,legendre(33,p),legendre(-2,p)])
    if p%8==5 and legendre(p,3)==-1 and legendre(p,11)==1:
        assert val==2 and (p+1-n)%8==2 and p+1-n!=0
        family.append([p,n,p+1-n,val])
assert not exceptions
res={
 'purpose':'finite corroboration only; uniform proof is in the reconstruction',
 'bound_exclusive':10000,
 'symbolic_checks':'all passed',
 'all_good_primes_checked':len(rows),
 'exact_character_criterion_exceptions':exceptions,
 'family_primes_checked':len(family),
 'family_first_12_rows_q_N_a_v2':family[:12],
 'family_all_rows_q_N_a_v2':family,
 'all_rows_p_N_a_v2_chi33_chiminus2':rows,
}
out=Path(__file__).with_name('independent_checks.json')
out.write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps({k:v for k,v in res.items() if not k.startswith(('family_all','all_rows'))},indent=2))
