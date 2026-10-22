from sage.all import *
import json
out=[]
for suffix,mapname,actionname in [('', 'TORSOR_MAP_0.json','TORSOR_ACTION_CHECKS.json'),('_113','TORSOR_MAP_113_0.json','TORSOR_ACTION_CHECKS_113.json')]:
 j=json.load(open('TORSOR_INPUT'+suffix+'.json'));m=json.load(open(mapname));E=EllipticCurve(QQ,[QQ(c) for c in j['base_model']]);C=EllipticCurve(QQ,[QQ(c) for c in j['target_model']]);P=E([QQ(c) for c in j['P']]);Y=C([QQ(c) for c in j['Y']]);PR=PolynomialRing(QQ,'x');f=PR([QQ(c) for c in j['base_fiber_polynomial']]);g=PR([QQ(c) for c in j['target_fiber_polynomial']]);X=E.multiplication_by_m(5,x_only=True);Z=C.multiplication_by_m(5,x_only=True)
 checks={'source_fiber_polynomial':f==(X-P[0]).numerator().monic(),'target_fiber_polynomial':g==(Z-Y[0]).numerator().monic(),'source_irreducible':f.is_irreducible(),'target_irreducible':g.is_irreducible()};assert all(checks.values())
 K=NumberField(f,'u');u=K.gen();r=K([QQ(c) for c in m['target_x_coeffs']]);vr=K([QQ(c) for c in m['target_v_coeffs']]);vq=K([QQ(c) for c in m['source_v_coeffs']]);EK=E.change_ring(K);CK=C.change_ring(K);Q=EK(u,vq-(E.a1()*u+E.a3())/2);R=CK(r,vr-(C.a1()*r+C.a3())/2)
 checks.update(target_polynomial_at_r=g(r)==0,source_division_point=5*Q==EK(P),target_division_point=5*R==CK(Y),x_map_degree25=r.minpoly().degree()==25,source_differential_formula=vq==5*(P[1]+(E.a1()*P[0]+E.a3())/2)/X.derivative()(u),target_differential_formula=vr==5*(Y[1]+(C.a1()*Y[0]+C.a3())/2)/Z.derivative()(r))
 q=3061;arrays=[j['base_fiber_polynomial'],j['target_fiber_polynomial'],m['target_x_coeffs'],m['target_v_coeffs'],m['source_v_coeffs'],j['P'],j['Y']];checks['all_relevant_rational_denominators_prime_to_3061']=all(QQ(c).denominator()%q!=0 for a in arrays for c in a);checks['source_fiber_separable_mod3061']=f.change_ring(GF(q)).is_squarefree();checks['target_fiber_separable_mod3061']=g.change_ring(GF(q)).is_squarefree();checks['both_curves_good_at3061']=E.discriminant().valuation(q)==C.discriminant().valuation(q)==0
 checks['source_psi5_irreducible']=E.division_polynomial(5).is_irreducible();checks['transvection_input_at7']=E.c4().valuation(7)==0 and E.discriminant().valuation(7)==2
 assert all(checks.values())
 out.append({'map':mapname,'checks':checks,'source_discriminant':str(E.discriminant()),'source_c4':str(E.c4())});print(mapname,'PASS',len(checks),'exactchecks',flush=True)
json.dump(out,open('SAVED_TORSOR_CHECKS.json','w'),indent=2)
