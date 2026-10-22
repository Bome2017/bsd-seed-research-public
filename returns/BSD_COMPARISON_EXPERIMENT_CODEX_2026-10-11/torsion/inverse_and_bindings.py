from sage.all import *
import json,glob,hashlib,platform
E=EllipticCurve(QQ,[1,1,1,3,12]);F=NumberField(E.division_polynomial(5),'u');u=F.gen();assert E.division_polynomial(5).is_irreducible()
rows=[]
for fn in sorted(glob.glob('map_*_0.json')):
 j=json.load(open(fn));C=EllipticCurve(QQ,[QQ(c) for c in j['target_ainvs']]);r=F([QQ(c) for c in j['x_coeffs']]);s=F([QQ(c) for c in j['Y_factor_coeffs']]);M=matrix(QQ,[(r**i).vector() for i in range(12)]).transpose();assert M.det()!=0
 rc=M.solve_right(u.vector());sc=M.solve_right((1/s).vector());RP=PolynomialRing(QQ,'x');rp=RP(rc.list());sp=RP(sc.list());assert rp(r)==u and sp(r)*s==1
 inv={'source_map':fn,'source_ainvs':j['target_ainvs'],'target_ainvs':j['source_ainvs'],'x_coeffs':list(map(str,rc)),'Y_factor_coeffs':list(map(str,sc)),'composition_checks':{'x_inverse':True,'Y_inverse':True}}
 out='inverse_'+fn;json.dump(inv,open(out,'w'),indent=2)
 denom=lambda a:lcm([QQ(c).denominator() for c in a])
 rows.append({'map':fn,'forward_x_denominator':str(denom(j['x_coeffs'])),'forward_x_denominator_factors':str(factor(denom(j['x_coeffs']))),'forward_Y_denominator':str(denom(j['Y_factor_coeffs'])),'forward_Y_denominator_factors':str(factor(denom(j['Y_factor_coeffs']))),'inverse_x_denominator_factors':str(factor(denom(rc))),'inverse_Y_denominator_factors':str(factor(denom(sc))),'power_basis_change_determinant':str(M.det()),'power_basis_change_determinant_factors':str(factor(M.det()))})
json.dump({'source_division_polynomial_irreducible':True,'maps':rows},open('INVERSE_AND_DENOMINATORS.json','w'),indent=2)
selected=json.load(open('map_113_1_0.json'));selected['weil_pairing_multiplier_mod5']=1;selected['convention']='Y=2y+a1*x+a3; (x,Y) maps to (r(x),s(x)*Y). Set phi(O)=O.';json.dump(selected,open('SELECTED_SYMPLECTIC_MAP.json','w'),indent=2)
print(json.dumps(rows,indent=2))
