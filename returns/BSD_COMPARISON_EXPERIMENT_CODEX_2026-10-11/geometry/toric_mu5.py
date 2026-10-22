"""Exact nodal-fiber mu_5 controls, independent of a CM trace or torsion transport."""
import json
from pathlib import Path

class F:
    q=0
    def __init__(self,a=0):
        if isinstance(a,F):self.a=a.a
        elif isinstance(a,int):self.a=(a%self.q,0,0,0)
        else:self.a=tuple(x%self.q for x in a)
    def __add__(x,y):
        y=F(y);return F([a+b for a,b in zip(x.a,y.a)])
    __radd__=__add__
    def __neg__(x):return F([-a for a in x.a])
    def __sub__(x,y):return x+-F(y)
    def __rsub__(x,y):return F(y)+-x
    def __mul__(x,y):
        y=F(y);c=[0]*7
        for i,a in enumerate(x.a):
            for j,b in enumerate(y.a):c[i+j]+=a*b
        for i in range(6,3,-1):
            for j in range(1,5):c[i-j]-=c[i]
        return F(c[:4])
    __rmul__=__mul__
    def __pow__(x,n):
        if n<0:return (x**(x.q**4-2))**(-n)
        z=F(1)
        while n:
            if n&1:z=z*x
            x=x*x;n//=2
        return z
    def __truediv__(x,y):
        y=F(y);assert y!=0
        return x*y**(-1)
    def __rtruediv__(x,y):return F(y)/x
    def __eq__(x,y):return x.a==F(y).a
    def out(x):return list(x.a)


def curve_on(a,P):
    if P is None:return True
    x,y=P;a1,a2,a3,a4,a6=map(F,a)
    return y*y+a1*x*y+a3*y==x**3+a2*x*x+a4*x+a6


def add(a,P,Q):
    if P is None:return Q
    if Q is None:return P
    x,y=P;X,Y=Q;a1,a2,a3,a4,a6=map(F,a)
    if x==X:
        if Y==-y-a1*x-a3:return None
        lam=(3*x*x+2*a2*x+a4-a1*y)/(2*y+a1*x+a3)
    else:lam=(Y-y)/(X-x)
    nu=y-lam*x
    xx=lam*lam+a1*lam-a2-x-X
    return (xx,-(lam+a1)*xx-nu-a3)


def point_out(P):return None if P is None else [c.out() for c in P]

models=[('287133c1',113,[1,1,1,-1669982047,-25795561267816]),('424347b1',167,[1,1,1,1878418,-485198548])]
out=[]
for label,q,a in models:
    F.q=q;a1,a2,a3,a4,a6=a
    b2=(a1*a1+4*a2)%q;b4=(a1*a3+2*a4)%q;b6=(a3*a3+4*a6)%q
    i4=pow(4,-1,q)
    noders=[r for r in range(q) if (4*r**3+b2*r*r+2*b4*r+b6)%q==0 and (12*r*r+2*b2*r+2*b4)%q==0]
    assert len(noders)==1
    r=noders[0];d=(3*r+b2*i4)%q
    roots=[v for v in range(q) if v*v%q==d]
    assert len(roots)==2;v=roots[0]
    z=F([0,1,0,0]);assert z**5==1 and z!=1
    # irreducible Phi_5 because q has order 4 modulo 5.
    assert pow(q,4,5)==1 and pow(q,2,5)!=1
    pts=[None]
    for k in range(1,5):
        zz=z**k;xx=4*d*zz/(1-zz)**2;uu=v*(1+zz)/(1-zz)
        x=F(r)+xx;y=uu*xx-(a1*x+a3)/2
        P=(x,y);assert curve_on(a,P);assert x!=r
        pts.append(P)
    for i in range(5):
        for j in range(5):assert add(a,pts[i],pts[j])==pts[(i+j)%5]
    for i in range(1,5):assert tuple(c**q for c in pts[i])==pts[(i*q)%5]
    out.append({'label':label,'ell':q,'nodal_x':r,'square_root_orientation':v,'d':d,'minimal_equation_used':a,'field':'F_ell[zeta]/(zeta^4+zeta^3+zeta^2+zeta+1)','points_indexed_by_zeta_power':[point_out(P) for P in pts],'curve_equations':4,'group_law_checks':25,'frobenius_checks':4,'frob_exponent':q%5})
result={'status':'EXACT_NONSINGULAR_TORIC_MU5_REALIZED','controls':out,'total_group_law_checks':50,'scope':'Nodal special-fiber arithmetic only. No CM trace, Shimura component-index or globally transported pairing computed.'}
p=Path(__file__).with_name('TORIC_MU5.json');p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':result['status'],'ell_values':[r['ell'] for r in out],'group_law_checks':50}))
