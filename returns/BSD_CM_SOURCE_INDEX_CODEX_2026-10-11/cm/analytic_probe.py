from sage.all import *
import json,time
R=RealField(140)
C=EllipticCurve(QQ,[1,1,1,1878418,-485198548]);Y=C(480,22723);T=C.quadratic_twist(-19)
print('START',flush=True)
basis=C.period_lattice().basis(prec=140)
res={'scope':'exploratory real approximations with Sage reported series-tail bounds; not independent rounding-certified enclosures','curve':[int(a) for a in C.a_invariants()],'N':int(C.conductor()),'discriminant':str(C.discriminant().factor()),'Y':[str(a) for a in Y.xy()],'height_normalised_BSD':str(Y.height(precision=140)),'periods':[str(a) for a in basis],'period_area':str(R(basis[0]*basis[1].imag())),'a5':int(C.ap(5)),'a13':int(C.ap(13)),'source_multiplier':int(2*(C.ap(5)-6)-(C.ap(13)-14)), 'classical_modular_degree_record':20576640,'classical_degree_factors':str(factor(20576640)), 'locals':{str(q):{'kodaira':str(C.local_data(q).kodaira_symbol()),'tamagawa':int(C.tamagawa_number(q)),'vdisc':int(C.discriminant().valuation(q))} for q in [3,7,11,167]}}
Lprime,err=C.lseries().deriv_at1(16000)
res.update(Lprime=str(Lprime),Lprime_tail=str(err));print('LPRIME',res['Lprime'],flush=True)
Ltw,errtw=T.lseries().at1(120000)
res.update(twist_L=str(Ltw),twist_tail=str(errtw),twist_N=int(T.conductor()))
res['raw_GZ_ratio_using_degree_and_Sage_height']=str(R(19).sqrt()*R(Lprime)*R(Ltw)/(2*20576640*R(res['period_area'])*R(res['height_normalised_BSD'])))
print(json.dumps(res,indent=2),flush=True)
open(__import__('pathlib').Path(__file__).resolve().parent/'analytic_probe.json','w').write(json.dumps(res,indent=2)+'\n')
