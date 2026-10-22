from sage.all import *
import json
from pathlib import Path
out=Path(__file__).parent
R=PolynomialRing(QQ,'t'); t=R.gen()
K=NumberField(t*t-t-10934,'a'); a=K.gen(); sq=2*a-1; d=ZZ(43737)
E=EllipticCurve(QQ,[0,0,1,-19766893413,-1937478573143510])
P1=E(QQ(1778638)/9,QQ(1169009812)/27)
P2=E(QQ(6466626346478)/36517849,QQ(2366996613841078836)/220677361507)
f=lambda P: (P[0]-QQ(11)*d/3)*(P[1]+QQ(1)/2)+sq*(-4*P[0]**2+QQ(161)*d*P[0]/6-QQ(785)*d*d/18)
eps=23311+224*a
rho=(-527625*a-54179073)/352403588
assert eps.norm()==1
assert f(P1)==-QQ(1249565229839)/81*a+QQ(393863215501942)/243
assert f(P2)==f(P1)**2*rho**5
S=PolynomialRing(QQ,'X'); X=S.gen()
vv=X**3-19766893413*X-1937478573143510+QQ(1)/4
coef=X-QQ(11)*d/3
Q=-4*X**2+QQ(161)*d*X/6-QQ(785)*d*d/18
assert coef**2*vv-d*Q**2==(X-QQ(14)*d/3)**5
D=EllipticCurve(QQ,[-10,-11,-11,0,0]); A0=EllipticCurve(QQ,[0,-1,1,-10,-20]); iso=D.isomorphism_to(A0)
assert iso(D(0,0))==-A0(5,5)
gamma=-5829-56*a
alpha=gamma/gamma.galois_conjugate()
assert gamma.norm()==11**4
assert alpha==(68266265+655984*a)/14641
assert (1464+7*sq)/(1464-7*sq)==eps
result={"norm_epsilon":str(eps.norm()),"exact_descent_norm_polynomial_identity":True,"both_points_on_A":True,"point_image_fifth_power_relation":True,"Fisher_Tate_generator_image":[str(v) for v in iso(D(0,0))],"normalized_f_generator_image":["5","5","1"],"generator_change":"inversion", "gamma_norm":str(gamma.norm()),"alpha11_exact_expression":True,"Fisher_parameter_equals_epsilon":True}
(out/'independent_exact.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
