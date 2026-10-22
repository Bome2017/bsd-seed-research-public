from sage.all import *
import json,time
E=EllipticCurve(QQ,[1,1,1,3,12]);C=EllipticCurve(QQ,[1,1,1,1878418,-485198548]);P1=E(0,3);P2=E(7,17);P=2*P1+P2;Y=C(480,22723)
print('P',P,'Y',Y,flush=True)
X5=E.multiplication_by_m(5,x_only=True);Z5=C.multiplication_by_m(5,x_only=True)
f=(X5-P[0]).numerator().monic();g=(Z5-Y[0]).numerator().monic();print('DEGREES',f.degree(),g.degree(),flush=True)
json.dump({'base_model':list(map(str,E.a_invariants())),'target_model':list(map(str,C.a_invariants())),'P':list(map(str,P)),'Y':list(map(str,Y)),'base_fiber_polynomial':list(map(str,f.list())),'target_fiber_polynomial':list(map(str,g.list()))},open('TORSOR_INPUT.json','w'),indent=2)
t=time.monotonic();K=NumberField(f,'u');u=K.gen();print('FIELD READY',time.monotonic()-t,flush=True)
# invariant differentials imply v([5]Q)=X5'(x(Q))*v(Q)/5.
vP=P[1]+(E.a1()*P[0]+E.a3())/2;vY=Y[1]+(C.a1()*Y[0]+C.a3())/2
vQ=5*vP/X5.derivative()(u);Q=E.change_ring(K)(u,vQ-(E.a1()*u+E.a3())/2);assert 5*Q==E.change_ring(K)(P)
print('ROOT START',time.monotonic()-t,flush=True)
roots=g.change_ring(K).roots(multiplicities=False);print('ROOTS',len(roots),'seconds',time.monotonic()-t,flush=True)
for i,r in enumerate(roots):
 vR=5*vY/Z5.derivative()(r);R=C.change_ring(K)(r,vR-(C.a1()*r+C.a3())/2);assert 5*R==C.change_ring(K)(Y)
 out={'target_x_coeffs':list(map(str,r.polynomial().list())),'target_v_coeffs':list(map(str,vR.polynomial().list())),'source_v_coeffs':list(map(str,vQ.polynomial().list())),'verified_5Q_P':True,'verified_5R_Y':True,'action_compatibility':'NOT_YET_CHECKED'}
 json.dump(out,open(f'TORSOR_MAP_{i}.json','w'),indent=2);print('SAVED',i,flush=True)
