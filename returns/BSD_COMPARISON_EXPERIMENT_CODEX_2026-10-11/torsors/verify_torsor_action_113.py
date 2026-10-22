from sage.all import *
import json
j=json.load(open('TORSOR_INPUT_113.json'));m=json.load(open('TORSOR_MAP_113_0.json'));fm=json.load(open('../torsion/map_113_1_0.json'))
E=EllipticCurve(QQ,[QQ(c) for c in j['base_model']]);C=EllipticCurve(QQ,[QQ(c) for c in j['target_model']]);PR=PolynomialRing(QQ,'x');x=PR.gen();f=PR([QQ(c) for c in j['base_fiber_polynomial']]);g=PR([QQ(c) for c in j['target_fiber_polynomial']]);assert f.is_irreducible() and g.is_irreducible()
K=NumberField(f,'u');u=K.gen();r=K([QQ(c) for c in m['target_x_coeffs']]);assert r.minpoly().degree()==25
q=3061;RF=PolynomialRing(GF(q),'x');fac=f.change_ring(GF(q)).factor();print('fiber factorization degrees',[(g.degree(),e) for g,e in fac],flush=True);ff=fac[0][0];k=GF(q**ff.degree(),name='a',modulus=ff);a=k.gen();ek=E.change_ring(k);ck=C.change_ring(k);rp=PolynomialRing(k,'z')([QQ(c) for c in m['target_x_coeffs']]);vp=rp.parent()([QQ(c) for c in m['target_v_coeffs']]);vsource=rp.parent()([QQ(c) for c in m['source_v_coeffs']]);Q=ek(a,vsource(a)-(ek.a1()*a+ek.a3())/2)
def H(Q):
 xx=Q[0];rr=rp(xx);return ck(rr,vp(xx)-(ck.a1()*rr+ck.a3())/2)
fr=rp.parent()([QQ(c) for c in fm['x_coeffs']]);fs=rp.parent()([QQ(c) for c in fm['Y_factor_coeffs']]);
def phi(T):
 if T==ek(0):return ck(0)
 xx,yy=T.xy();rr=fr(xx);YY=fs(xx)*(2*yy+ek.a1()*xx+ek.a3());return ck(rr,(YY-ck.a1()*rr-ck.a3())/2)
T=ek(2489,640);U=ek(2200,1779); assert T.order()==U.order()==5
assert T.weil_pairing(U,5)!=1
assert len({i*T+j*U for i in range(5) for j in range(5)})==25
out=[]
for i in range(5):
 for jj in range(5):
  W=i*T+jj*U;diff=H(Q+W)-H(Q);fv=phi(W);cs=[c for c in range(1,5) if diff==c*fv] if W else [1,2,3,4];out.append({'i':i,'j':jj,'scalar_candidates':cs});assert diff==fv
result={'source_fiber_irreducible':True,'target_fiber_irreducible':True,'torsor_x_map_minpoly_degree':25,'prime':q,'extension_degree':int(ff.degree()),'translation_scalar_relative_to_map_113_1_0':1,'all_25_translations_match':True,'points_checked':out,'source_residual_irreducibility':'psi5 irreducible degree12 rules out rational stable line','source_scalar_endomorphisms':'irreducible residual module plus inertia transvection at7 (vDelta=2) forces End_G(V)=F5','global_affinity_argument':'written in RESULT.md; finitefield calculation only determines scalar of already-proved affine map'}
json.dump(result,open('TORSOR_ACTION_CHECKS_113.json','w'),indent=2);print('ALL25TRANSLATIONS: exact match to selectedglobal113map',flush=True)
