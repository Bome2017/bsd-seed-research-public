from decimal import Decimal, getcontext
getcontext().prec = 50
a, b = -22735, 106272484
N = 2**3*3*2243*4547**2*5843
def v(n,p):
    k=0
    while n%p==0: n//=p; k+=1
    return k
Delta = 16*b*b*(a*a-4*b)
print("N=",N,"7|N:",N%7==0,"7|Delta:",Delta%7==0, "Delta==recorded:", Delta==16586638656786071143743744)
print("b factor check:", b==2**2*4547*5843, "a^2-4b:", a*a-4*b==3**2*2243*4547)
# twist
d=-7
A, B = d*a, d*d*b
print("twist model a',b' =",A,B)
D2 = 16*B*B*(A*A-4*B)
print("Delta' = 7^6 Delta:", D2==7**6*Delta, {p:v(D2,p) for p in [2,3,7,2243,4547,5843]})
# Kronecker chi_{-7}(p)
def chi(p): return pow((-7)%p,(p-1)//2,p)
print("chi_{-7}:",{p:(1 if chi(p)==1 else -1) for p in [3,2243,4547,5843]}, "-7 mod 8 =", (-7)%8)
# E over F_7: f(x)=x^3+a x^2+b x
print("a mod 7, b mod 7:", a%7, b%7)
roots=[x for x in range(7) if (x**3+a*x*x+b*x)%7==0]
print("roots of f mod 7:",roots, "#E[2](F_7)=",1+len(roots))
cnt=1
for x in range(7):
    r=(x**3+a*x*x+b*x)%7
    cnt += 1 if r==0 else (2 if pow(r,3,7)==1 else 0)
print("#E(F_7)=",cnt,"a_7=",7+1-cnt)
# Tate at 7 on twist model: I0* criterion
print("7|A:",A%7==0,"49|B:",B%49==0,"v7(Delta')=",v(D2,7))
P=[T for T in range(7) if (T**3+(A//7)*T*T+(B//49)*T)%7==0]
print("roots of aux cubic T^3+(A/7)T^2+(B/49)T mod 7:",P," -> c_7 =",1+len(P) if len(P)!=3 else 4)
# torsion of twist
import math
def issq(n): 
    if n<0: return False
    r=math.isqrt(n); return r*r==n
print("Z/4 tests: B square?",issq(B)," A^2-4B square?",issq(A*A-4*B), " full 2-torsion? (A^2-4B square)",issq(A*A-4*B))
def count(p):
    c=1
    for x in range(p):
        r=(x**3+A*x*x+B*x)%p
        if r==0: c+=1
        elif pow(r,(p-1)//2,p)==1: c+=2
    return c
g=0
for p in [5,11,13,17,19,23,29,31,37,41,43]:
    g=math.gcd(g,count(p))
print("gcd #E^{-7}(F_p) over small good p:",g)
# E' isogenous curve
A2,B2 = -2*A, A*A-4*B
print("E' coeffs:",A2,B2, "B2==49*91790289:",B2==49*91790289)
DE = 16*B2*B2*(A2*A2-4*B2)
print("E' Delta valuations:",{p:v(DE,p) for p in [2,3,7,2243,4547,5843]})
# Period via AGM
def sqrtD(x): return x.sqrt()
def agm(x,y):
    for _ in range(200):
        x,y=(x+y)/2,sqrtD(x*y)
        if abs(x-y)<Decimal(10)**-45: break
    return x
# roots of x^3+Ax^2+Bx: 0 and roots of x^2+Ax+B
disc=Decimal(A*A-4*B).sqrt()
r1=(-Decimal(A)+disc)/2; r2=(-Decimal(A)-disc)/2
es=sorted([Decimal(0),r1,r2],reverse=True)
e1,e2,e3=es
print("real roots:",[str(e)[:12] for e in es])
pi=Decimal("3.14159265358979323846264338327950288419716939937510")
Om=2*pi/agm(sqrtD(e1-e3),sqrtD(e1-e2))
print("Omega_{E^-7} =",Om)
# sanity: y^2=x^3-x
print("Omega(y^2=x^3-x) =",2*pi/agm(Decimal(2).sqrt(),Decimal(1)))
for L in ["9.054319","9.054421"]:
    print("Q =",Decimal(L)*4/(Om*32))
