# Exploratory predecessor; certified_GZ_ingredients.py is the governing enclosure.
from sage.all import *
E=EllipticCurve(QQ,[1,1,1,1878418,-485198548]);R=RealBallField(200);PR=PolynomialRing(QQ,'t');t=PR.gen();b2,b4,b6,b8=E.b_invariants();z=1-b4*t*t-2*b6*t**3-b8*t**4
candidates=[AA(0),AA(QQ(1)/249)]+[r for r in z.derivative().roots(AA,multiplicities=False) if 0<r<QQ(1)/249]
print([(R(r),R(z(r))) for r in candidates]); print('zbound',all(QQ(1)/1000<z(r)<10**6 for r in candidates))
x=R(480);hs=R(480).log();
for i in range(40):
 zz=1-R(b4)/x**2-2*R(b6)/x**3-R(b8)/x**4
 hs+=zz.log()/R(4)**(i+1)
 x=(x**4-R(b4)*x*x-2*R(b6)*x-R(b8))/(4*x**3+R(b2)*x*x+2*R(b4)*x+R(b6))
hs-=R(QQ(7)/2)*R(3).log();tail=R(10**6).log()/(3*R(4)**40)
hs=hs.add_error(tail); print('h',hs, 'sage',E(480,22723).height(precision=100))
