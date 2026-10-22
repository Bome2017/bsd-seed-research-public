from sage.all import *
import json,hashlib,time
from pathlib import Path
OUT=Path(__file__).resolve().parent
R=RealBallField(200);C=ComplexBallField(200)
E=EllipticCurve(QQ,[1,1,1,1878418,-485198548]); Y=E(480,22723);Tw=E.quadratic_twist(-19)
PR=PolynomialRing(QQ,'t');t=PR.gen();b2,b4,b6,b8=E.b_invariants()
# Tate archimedean series. The real component has x >= real root >249.
f=t**3+b2/4*t*t+b4/2*t+b6/4
roots=f.roots(QQbar,multiplicities=False);realroot=next(r for r in roots if r.imag()==0); assert realroot>249
z=1-b4*t*t-2*b6*t**3-b8*t**4
critical=[AA(0),AA(QQ(1)/249)]+[r for r in z.derivative().roots(AA,multiplicities=False) if 0<r<QQ(1)/249]
assert all(QQ(1)/1000<z(r)<10**6 for r in critical)
x=R(480);height=R(480).log();nheight=42
for i in range(nheight):
 zz=1-R(b4)/x**2-2*R(b6)/x**3-R(b8)/x**4
 assert zz>0
 height+=zz.log()/R(4)**(i+1)
 x=(x**4-R(b4)*x*x-2*R(b6)*x-R(b8))/(4*x**3+R(b2)*x*x+2*R(b4)*x+R(b6))
# At3: nonsplit I14, singular Y, unique nonzero rational component has label7.
# At7,11,167 Y nonsingular => no component correction.
assert E.ap(3)==-1 and E.discriminant().valuation(3)==14
sing={}
for q in [3,7,11,167]:
 xx,yy=map(ZZ,Y.xy());sing[q]=bool((E.a1()*yy-3*xx*xx-2*E.a2()*xx-E.a4())%q==0 and (2*yy+E.a1()*xx+E.a3())%q==0)
assert sing=={3:True,7:False,11:False,167:False}
height-=R(QQ(7)/2)*R(3).log()
height=height.add_error(R(10**6).log()/(3*R(4)**nheight))
# Period fundamental area, via algebraic cubic roots and complete elliptic integrals.
e1=C(realroot);e2=C(next(r for r in roots if r.imag()>0));e3=C(next(r for r in roots if r.imag()<0))
m=(e2-e3)/(e1-e3);w1=2*m.elliptic_k()/(e1-e3).sqrt();w2=2*C.gen(0)*(1-m).elliptic_k()/(e1-e3).sqrt();area=abs((w1.conjugate()*w2).imag())
# Exact elliptic coefficients, with |a_n|<=d(n)sqrt(n)<=2n.
def L_eval(curve,deriv,M):
 N=ZZ(curve.conductor());c=2*R.pi()/R(N).sqrt(); coeff=curve.anlist(M,python_ints=True)
 val=R(0)
 for n in range(1,M+1):
  if coeff[n]:
   kernel=R(0).gamma_inc(c*n) if deriv else (-c*n).exp()
   val+=2*R(coeff[n])/n*kernel
 tail=4*(-c*(M+1)).exp()/(1-(-c).exp())
 if deriv:tail/=c*(M+1)
 val=val.add_error(tail)
 return val,tail,hashlib.sha256(','.join(map(str,coeff)).encode()).hexdigest()
assert E.root_number()==-1 and Tw.root_number()==1
print('height',height,'area',area,flush=True)
l1,t1,a1=L_eval(E,True,12000); print('derivative',l1,flush=True)
l0,t0,a0=L_eval(Tw,False,120000);print('twist',l0,flush=True)
# GZ and degree ratio70, K-relative height=2*height, c0 retained explicitly.
ratio=R(19).sqrt()*l1*l0/(280*area*height)
# Bound c0 using recorded delta0 and cusp strip y>=1: ||f||² >= exp(-4pi)/(4pi).
# delta0*area=4pi²*c0²*||f||².
delta0=ZZ(20576640);c0sqbound=delta0*area*(4*R.pi()).exp()/R.pi()
assert c0sqbound<100000**2
# Corrected integral CM point is -2*Hodge point. If Y generates C(Q)/torsion,
# rank twist0 ensures 2*corrected point is rational modulo torsion. Thus4*nH integral.
# nH²/c0² has denominator<=16*10^10. Isolate 9 in that bounded lattice.
bound=R(1)/(16*100000**2)
assert abs(ratio-9)<bound
result={'status':'BALL_INGREDIENTS_AND_BOUNDED_RATIONAL_ISOLATION_PASS','scope':'Arithmetic deduction requires source normalization, K-height convention, GZ theorem, degree-ratio proof, and retained classical degree upper bound plus full rational generator Y. This file does not compute a CM point.', 'height_BSD_absolute':str(height),'height_tail':str(R(10**6).log()/(3*R(4)**nheight)),'period_area':str(area),'Lprime':str(l1),'Lprime_tail':str(t1),'Lprime_coeff_sha256':a1,'Ltwist':str(l0),'Ltwist_tail':str(t0),'Ltwist_coeff_sha256':a0,'n_Hodge_squared_over_Manin_squared':str(ratio),'identified_rational':9,'Manin_square_upper_bound':str(c0sqbound),'bounded_denominator_separation':str(bound),'source_Hecke_multiplier':-2,'corrected_n_squared_over_Manin_squared':36,'singular_reductions':sing,'height_term_count':nheight,'L_cutoffs':[12000,120000],'ball_precision':200,'exact_curve_model':[str(a) for a in E.a_invariants()]}
(OUT/'CERTIFIED_GZ_INGREDIENTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2),flush=True)
