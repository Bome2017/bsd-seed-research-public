# Independent check of the derived local data for E^{-7}, pure Python.
from decimal import Decimal, getcontext
from math import gcd, isqrt
getcontext().prec = 60
a, b = -22735, 106272484                 # E: y^2 = x^3 + a x^2 + b x
A, B = -7*a, 49*b                        # E^{-7}: y^2 = x^3 + A x^2 + B x
print("A,B =", A, B)
def disc(a,b): return 16*b*b*(a*a-4*b)
def c4(a,b): return 16*(a*a-3*b)
def c6(a,b): return -32*a*(2*a*a-9*b)
D, Dt = disc(a,b), disc(A,B)
print("c4(E),c6(E),Delta(E) =", c4(a,b), c6(a,b), D)
print("Delta(E^-7) == 7^6 Delta(E):", Dt == 7**6*D)
def fac(n, ps):
    out={}
    for p in ps:
        v=0
        while n%p==0: n//=p; v+=1
        if v: out[p]=v
    return out, n
ps=[2,3,7,2243,4547,5843]
print("vals Delta(E):", fac(abs(D),ps)); print("vals Delta(E^-7):", fac(abs(Dt),ps))
print("b factor:", fac(b,ps), " a^2-4b factor:", fac(a*a-4*b,ps))
print("B factor:", fac(B,ps), " A^2-4B factor:", fac(A*A-4*B,ps))
N = 2**3*3*2243*4547**2*5843
print("N =", N, " 49N =", 49*N, " 7 | N ?", N%7==0)
# Kronecker symbol (-7/p)
def legendre(x,p): 
    x%=p; return 0 if x==0 else (1 if pow(x,(p-1)//2,p)==1 else -1)
for p in [3,7,2243,4547,5843]: print("(-7/%d) ="%p, legendre(-7,p))
print("-7 mod 8 =", (-7)%8, "(1 mod 8 => 2-adic square)")
# E over F_7: a_7, #E(F_7), 2-torsion
p=7; cnt=1
for x in range(p):
    r=(x**3+a*x*x+b*x)%p
    cnt += 1 if r==0 else (2 if legendre(r,p)==1 else 0)
print("#E(F_7) =", cnt, " a_7 =", p+1-cnt)
print("roots of x^2+a x+b mod 7:", [x for x in range(7) if (x*x+a*x+b)%7==0], " (a mod 7 =", a%7, ", b mod 7 =", b%7, ")")
# Tate's algorithm at 7 on twist model: a2=A, a4=B, a6=0
print("7|A:",A%7==0," 49|B:",B%49==0," v7(Delta')=",fac(abs(Dt),[7])[0])
cub=[t for t in range(7) if (t**3+(A//7)*t*t+(B//49)*t)%7==0]
# separability: check cubic and derivative no common root mod 7
der=[t for t in range(7) if (3*t*t+2*(A//7)*t+(B//49))%7==0]
print("aux cubic T^3+(A/7)T^2+(B/49)T mod 7: roots", cub, " common with derivative:", set(cub)&set(der), " => I0*, c_7 =", 1+len(cub))
# torsion of E^{-7}
print("A^2-4B square?", isqrt(A*A-4*B)**2==A*A-4*B, " B square?", isqrt(B)**2==B, " A^2-4B =", A*A-4*B)
def count(p):
    c=1
    for x in range(p):
        r=(x**3+A*x*x+B*x)%p
        c += 1 if r==0 else (2 if legendre(r,p)==1 else 0)
    return c
g=0
for p in [5,11,13,17,19,23,29,31,37,41,43]:
    g=gcd(g,count(p))
print("gcd #E^-7(F_p) over p=5..43:", g)
# a_p(E^{-7}) vs chi(p) a_p(E) at a few good primes
for p in [5,11,13,23]:
    cE=1
    for x in range(p):
        r=(x**3+a*x*x+b*x)%p
        cE += 1 if r==0 else (2 if legendre(r,p)==1 else 0)
    print(" p=%d a_p(E)=%d chi=%d a_p(E^-7)=%d"%(p,p+1-cE,legendre(-7,p),p+1-count(p)))
# real period via AGM
def roots_cubic(A,B):
    # x(x^2+Ax+B)=0
    d=Decimal(A*A-4*B).sqrt()
    return sorted([Decimal(0), (-A+d)/2, (-A-d)/2], reverse=True)
def agm(x,y):
    for _ in range(200):
        x,y=(x+y)/2,(x*y).sqrt()
        if abs(x-y)<Decimal(10)**-55: break
    return x
pi=Decimal("3.14159265358979323846264338327950288419716939937510582097494459")
def period(A,B):
    e1,e2,e3=roots_cubic(A,B)
    return 2*pi/agm((e1-e3).sqrt(),(e1-e2).sqrt())   # both components, Neron diff dx/2y
print("roots E^-7:", [str(r)[:14] for r in roots_cubic(A,B)])
OmT=period(A,B); OmE=period(a,b)
print("Omega(E^-7) =", OmT); print("Omega(E) =", OmE)
# sanity: y^2=x^3-x : A=0,B=-1 -> period 2*2.622057554... = 5.24411510858
print("check y^2=x^3-x:", period(0,-1))
for L in (Decimal("9.054319"),Decimal("9.054421")):
    print("Q =", L*4/(OmT*32))
print("Omega(E)/Omega(E^-7) =", OmE/OmT, " sqrt7/? ", Decimal(7).sqrt())
