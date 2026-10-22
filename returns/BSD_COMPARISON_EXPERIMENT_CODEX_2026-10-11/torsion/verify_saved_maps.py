from sage.all import *
import json,glob
E=EllipticCurve(QQ,[1,1,1,3,12]);psi=E.division_polynomial(5);assert psi.is_irreducible();F=NumberField(psi,'u');u=F.gen();out=[]
f=lambda C,x:4*x**3+C.b2()*x**2+2*C.b4()*x+C.b6()
for fn in sorted(glob.glob('map_*.json')):
 j=json.load(open(fn));C=EllipticCurve(QQ,[QQ(c) for c in j['target_ainvs']]);r=F([QQ(c) for c in j['x_coeffs']]);s=F([QQ(c) for c in j['Y_factor_coeffs']]);checks={'source_model':j['source_ainvs']==list(map(str,E.a_invariants())),'target_division_polynomial':C.division_polynomial(5)(r)==0,'curve_identity':s*s*f(E,u)==f(C,r),'Y_factor_nonzero':s!=0,'x_map_primitive':r.minpoly().degree()==12}
 assert all(checks.values());out.append({'map':fn,'checks':checks})
json.dump({'irreducible_source_psi5':True,'maps':out},open('SAVED_MAP_CHECKS.json','w'),indent=2);print('All',len(out),'saved coordinate maps pass exact checks.')
