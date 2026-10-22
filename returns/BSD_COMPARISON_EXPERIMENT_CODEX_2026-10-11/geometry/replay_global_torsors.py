from sage.all import *
from pathlib import Path
import json,time,hashlib
root=Path(__file__).resolve().parents[1]
E=EllipticCurve(QQ,[1,1,1,3,12]);R=PolynomialRing(QQ,'X');X=R.gen();psi=R(E.division_polynomial(5))
# Select a second exact specialization, independently of the source's3061 check.
q2=None
for q in prime_range(3062,20000):
    if q%5!=1 or E.discriminant().numerator()%q==0:continue
    F=GF(q);ee=E.change_ring(F);xs=psi.change_ring(F).roots(multiplicities=False)
    if len(xs)!=12:continue
    Ts=[P for x in xs for P in ee.lift_x(x,all=True)]
    if len(Ts)==24:q2=int(q);break
assert q2 is not None
print('HELD_OUT_PRIME',q2,flush=True)
out=[]
for ell,suf,mapname in [(167,'','map_167_0_0.json'),(113,'_113','map_113_1_0.json')]:
    j=json.loads((root/'torsors'/('TORSOR_INPUT'+suf+'.json')).read_text())
    m=json.loads((root/'torsors'/('TORSOR_MAP'+suf+'_0.json')).read_text())
    fm=json.loads((root/'torsion'/mapname).read_text())
    C=EllipticCurve(QQ,[QQ(c) for c in j['target_model']]);P=E([QQ(c) for c in j['P']]);Y=C([QQ(c) for c in j['Y']]);f=R([QQ(c) for c in j['base_fiber_polynomial']]);g=R([QQ(c) for c in j['target_fiber_polynomial']]);assert f.is_irreducible() and g.is_irreducible()
    K=NumberField(f,'u');u=K.gen();rr=R([QQ(c) for c in m['target_x_coeffs']]);vs=R([QQ(c) for c in m['source_v_coeffs']]);vr=R([QQ(c) for c in m['target_v_coeffs']]);r=rr(u)
    assert g(r)==0 and R(r.minpoly())==g
    ek=E.change_ring(K);ck=C.change_ring(K);Q=ek(u,vs(u)-(u+1)/2);Qprime=ck(r,vr(u)-(r+1)/2)
    assert 5*Q==ek(P) and 5*Qprime==ck(Y)
    checks=[]
    for q in [3061,q2]:
        F=GF(q);factors=f.change_ring(F).factor();assert all(e==1 for _,e in factors)
        f0=factors[0][0];k=GF(q**f0.degree(),'a',modulus=f0) if f0.degree()>1 else F
        a=k.gen() if f0.degree()>1 else -f0[0]/f0[1]
        ec=E.change_ring(k);cc=C.change_ring(k);RK=PolynomialRing(k,'Z');RP=RK(rr);VS=RK(vs);VR=RK(vr);Qk=ec(a,VS(a)-(a+1)/2);assert 5*Qk==ec(P)
        phi_x=RK([QQ(c) for c in fm['x_coeffs']]);phi_y=RK([QQ(c) for c in fm['Y_factor_coeffs']]);
        def H(Q):
            z=RP(Q[0]);return cc(z,VR(Q[0])-(z+1)/2)
        def phi(T):
            if T.is_zero():return cc(0)
            x,y=T.xy();z=phi_x(x);v=phi_y(x)*(2*y+x+1);return cc(z,(v-z-1)/2)
        tors=[ec(0)]
        for xx in ec.division_polynomial(5).roots(multiplicities=False):tors.extend(ec.lift_x(xx,all=True))
        assert len(tors)==25 and len(set(tors))==25
        H0=H(Qk);assert 5*H0==cc(Y)
        for T in tors:assert H(Qk+T)-H0==phi(T)
        checks.append({'prime':q,'fiber_extension_degree':int(f0.degree()),'fiber_factor_degrees':[int(ff.degree()) for ff,_ in factors],'distinct_translations':25,'action_equals_selected_global_map':True})
        print('CHECKED',ell,q,flush=True)
    out.append({'ell':ell,'source_fiber_irreducible':True,'target_fiber_irreducible':True,'root_identity_exact':True,'minimal_polynomial_exact':True,'source_point_division_exact':True,'target_point_division_exact':True,'specializations':checks})
(root/'geometry/GLOBAL_TORSOR_REPLAY.json').write_text(json.dumps({'status':'EXACT_RATIONAL_MAP_REPLAY_AND_TWO_SCALAR_SPECIALIZATIONS_PASS','held_out_prime':q2,'results':out},indent=2)+'\n')
