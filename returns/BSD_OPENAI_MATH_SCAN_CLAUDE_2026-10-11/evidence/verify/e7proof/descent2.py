# 2-isogeny descent (Silverman AEC X.4.9 form) in pure Python, exact integer arithmetic.
# Curve y^2 = x^3 + a x^2 + b x,  phi: E -> E' with kernel (0,0),  E': Y^2 = X^3 - 2a X^2 + (a^2-4b) X.
# Sel^phi(E)  = { d | a^2-4b (signed squarefree) : d w^2 = d^2 - 2a d z^2 + (a^2-4b) z^4 soluble everywhere }  (receives E'(Q)/phi E(Q))
# Sel^phihat(E') = { d | b : d w^2 = d^2 + a d z^2 + b z^4 soluble everywhere }                        (receives E(Q)/phihat E'(Q))
# dim Sel_2(E) <= dim Sel^phi(E) + dim Sel^phihat(E') - dim( E'(Q)[phihat] / phi(E(Q)[2]) ),
#   the last term = 1 if E(Q)[2] = Z/2 (a^2-4b not a square), 0 if E(Q)[2] = (Z/2)^2.
import sys
from itertools import combinations
from math import isqrt

def vp(n,p):
    if n==0: return 10**9
    v=0
    while n%p==0: n//=p; v+=1
    return v
def polyval(c,x):  # c[i] coefficient of x^i
    r=0
    for ci in reversed(c): r=r*x+ci
    return r
def shift_scale(c,z0,s):  # H(t) = h(z0 + s t) as integer coefficient list
    n=len(c); out=[0]*n
    # expand sum c_i (z0 + s t)^i
    from math import comb
    for i,ci in enumerate(c):
        for j in range(i+1):
            out[j]+= ci*comb(i,j)*(z0**(i-j))*(s**j)
    return out
def is_sq_unit_mod(u,p):
    if p==2: return u%8==1
    return pow(u%p,(p-1)//2,p)==1
def has_sq_value(h,p,k,z0,depth=0):
    """exists t in Z_p with h(z0 + p^k t) in (Q_p^*)^2 ∪ {0}?"""
    if depth>300: raise RuntimeError("depth")
    H=shift_scale(h,z0,p**k)
    v=min(vp(c,p) for c in H)
    if v>=10**9: return True   # h identically zero (never happens)
    H1=[c//p**v for c in H]
    rec=set()
    if p==2:
        for t0 in range(8):
            val=polyval(H1,t0)
            if val%2==1:
                if v%2==0 and val%8==1: return True
            else:
                rec.add(t0%2)
    else:
        for t0 in range(p):
            val=polyval(H1,t0)%p
            if val!=0:
                if v%2==0 and is_sq_unit_mod(val,p): return True
            else:
                rec.add(t0)
    # only after every class at this level failed the unit-square test do we descend into the zero classes
    for t0 in sorted(rec):
        if has_sq_value(h,p,k+1,z0+(p**k)*t0,depth+1): return True
    return False
def locally_soluble(d,a,b,p):
    # d*g(z) square for some z in Q_p ∪ {inf}, g(z) = d^2 + a d z^2 + b z^4
    h=[d*d*d,0,d*d*a,0,d*b]          # d*g(z)
    hrev=[d*b,0,d*d*a,0,d*d*d]       # d*z^4 g(1/z)
    return has_sq_value(h,p,0,0) or has_sq_value(hrev,p,1,0)
def real_soluble(d,a,b):
    if d>0: return True           # z=0 gives d^3>0
    if d*b>0: return True
    # d<0, b>0: need g(Z)<=0 for some Z>=0, g=bZ^2 + a d Z + d^2
    # vertex Z=-ad/(2b) >=0 iff a d <=0 ; discriminant a^2 d^2 - 4 b d^2 >=0 iff a^2>=4b
    return (a*d<=0) and (a*a>=4*b)
def primes_of(n):
    n=abs(n); ps=[]; p=2
    while p*p<=n:
        if n%p==0:
            ps.append(p)
            while n%p==0: n//=p
        p+=1
    if n>1: ps.append(n)
    return ps
def selmer(a,b,badprimes):
    """Sel group for the image of points of y^2=x^3+ax^2+bx (d | b)."""
    ps=primes_of(b); sel=[]
    for r in range(len(ps)+1):
        for sub in combinations(ps,r):
            m=1
            for q in sub: m*=q
            for d in (m,-m):
                ok=real_soluble(d,a,b) and all(locally_soluble(d,a,b,p) for p in badprimes)
                if ok: sel.append(d)
    return sel
def log2(n):
    k=0
    while (1<<k)<n: k+=1
    assert (1<<k)==n, n
    return k
def descent(a,b,name):
    a2,b2=-2*a,a*a-4*b
    bad=sorted(set(primes_of(2*16*b*b*(a*a-4*b))))
    S_phihat=selmer(a,b,bad)      # image side of E(Q): d | b           -> Sel^phihat(E')
    S_phi=selmer(a2,b2,bad)       # image side of E'(Q): d | a^2-4b     -> Sel^phi(E)
    corr = 0 if isqrt(abs(b2))**2==b2 and b2>0 else 1
    bound=log2(len(S_phi))+log2(len(S_phihat))-corr
    print(f"[{name}] a={a} b={b}; bad primes {bad}")
    print(f"   Sel^phi(E)      (d|a^2-4b) = {sorted(S_phi,key=abs)}  dim {log2(len(S_phi))}")
    print(f"   Sel^phihat(E')  (d|b)      = {sorted(S_phihat,key=abs)}  dim {log2(len(S_phihat))}")
    print(f"   correction dim(E'(Q)[phihat]/phi E(Q)[2]) = {corr};  bound: dim Sel_2(E) <= {bound}")
    return bound
# controls
descent(0,-1,"y^2=x^3-x (rank 0, full 2-torsion, Sha[2]=0: expect bound 2)")
descent(0,-25,"y^2=x^3-25x (rank 1, full 2-torsion: expect bound 3)")
descent(0,-17**2,"y^2=x^3-289x (n=17 not congruent; rank 0; expect bound >= 2)")
descent(-22735,106272484,"seed E (rank 2, tors Z/2, Sha[2]=0: expect bound >= 3)")
descent(159145,5207351716,"twist E^{-7} (rank 0, tors Z/2)")
