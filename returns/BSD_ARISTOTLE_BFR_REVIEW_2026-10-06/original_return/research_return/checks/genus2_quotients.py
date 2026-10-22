"""Exact check for candidate M3 (COLLISION_CHECK.md section D).
C: U^2 = f(T) = 1 - T^2 - a T^4 - b T^6, a=66020924, b=65074271436.
(1) (T,U) -> (x,y)=(T^-2, U/T^3) lands on E: y^2 = x^3 - x^2 - a x - b (identity of rational functions).
(2) s=T^2: U^2 = 1 - s - a s^2 - b s^3; with X=-b s, Y=b U: Y^2 = X^3 - a X^2 + b X + b^2 (E2).
(3) j(E) != j(E2)."""
from fractions import Fraction as Fr
import random, json
a,b=66020924,65074271436
f=lambda T:1-T**2-a*T**4-b*T**6
ok1=ok2=True
for _ in range(50):
    T=Fr(random.randint(1,10**6),random.randint(1,10**6)); U2=f(T)
    x=1/T**2; y2=U2/T**6
    ok1 &= (y2 == x**3-x**2-a*x-b)
    s=T**2; X=-b*s; Y2=b*b*U2
    ok2 &= (Y2 == X**3-a*X**2+b*X+b*b)
def j(a1,a2,a3,a4,a6):
    b2=a1*a1+4*a2;b4=2*a4+a1*a3;b6=a3*a3+4*a6;b8=a1*a1*a6+4*a2*a6-a1*a3*a4+a2*a3*a3-a4*a4
    c4=b2*b2-24*b4;D=-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
    return Fr(c4**3,D)
jE=j(0,-1,0,-a,-b); jE2=j(0,-a,0,b,b*b)
print(json.dumps({"C->E identity (50 random rational T)":ok1,"C->E2 identity":ok2,
  "j(E)":str(jE),"j(E2)":str(jE2),"j differ":jE!=jE2},indent=1))
