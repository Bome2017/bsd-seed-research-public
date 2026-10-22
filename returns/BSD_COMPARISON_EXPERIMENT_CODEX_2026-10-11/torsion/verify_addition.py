from sage.all import *
import json,time,glob
E=EllipticCurve(QQ,[1,1,1,3,12]);F=NumberField(E.division_polynomial(5),'u');u=F.gen(); PP=PolynomialRing(F,'z');z=PP.gen()
f=lambda A,x:x**3+A.b2()/4*x**2+A.b4()/2*x+A.b6()/4
x2=(3*u*u+E.b2()/2*u+E.b4()/2)**2/(4*f(E,u))-E.b2()/4-2*u
psi=PP(E.division_polynomial(5));h=psi//((z-u)*(z-x2));h=h.monic()
print('independent x polynomial degree',h.degree(),flush=True)
L=F.extension(h,'v',check=True);v=L.gen();WW=PolynomialRing(L,'w');w=WW.gen();A=L.extension(w*w-f(E,L(u))*f(E,v),'w',check=True);w=A.gen();x=A(u);z=A(v);fx=f(E,x)
print('comparison algebra relative degree',A.absolute_degree(),flush=True)
outputs=[]
for fn in sorted(glob.glob('map_*.json')):
 t=time.monotonic();j=json.load(open(fn));C=EllipticCurve(QQ,[QQ(q) for q in j['target_ainvs']]);r=PolynomialRing(QQ,'q')([QQ(q) for q in j['x_coeffs']]);s=r.parent()([QQ(q) for q in j['Y_factor_coeffs']])
 # independent pairs P,Q. Work with w=v_P*v_Q, and divide y formulas by v_P.
 xr=(f(E,z)+fx-2*w)/(z-x)**2-E.b2()/4-x-z
 vr=-1+(w/fx-1)*(x-xr)/(z-x)
 xrt=(s(z)**2*f(E,z)+s(x)**2*fx-2*s(z)*s(x)*w)/(r(z)-r(x))**2-C.b2()/4-r(x)-r(z)
 vrt=-s(x)+(s(z)*w/fx-s(x))*(r(x)-xrt)/(r(z)-r(x))
 checks={'independent_addition_x':r(xr)==xrt,'independent_addition_y':s(xr)*vr==vrt}
 # doubling separately; oddness is built into the s(x)*v formula.
 xe=F(u);x2e=F(x2); slopee=(3*xe*xe+E.b2()/2*xe+E.b4()/2)/(2*f(E,xe))
 ve2_over_ve=-1+slopee*(xe-x2e)
 xt=r(xe);st=s(xe); x2t=(3*xt*xt+C.b2()/2*xt+C.b4()/2)**2/(4*f(C,xt))-C.b2()/4-2*xt
 vt2_over_ve=-st+(3*xt*xt+C.b2()/2*xt+C.b4()/2)/(2*st*f(E,xe))*(xt-x2t)
 checks.update(doubling_x=r(x2e)==x2t,doubling_y=s(x2e)*ve2_over_ve==vt2_over_ve)
 print(fn,checks,'seconds',time.monotonic()-t,flush=True);assert all(checks.values());outputs.append({'map':fn,'checks':checks,'seconds':time.monotonic()-t})
 json.dump(outputs,open('ADDITION_CHECKS.json','w'),indent=2)
