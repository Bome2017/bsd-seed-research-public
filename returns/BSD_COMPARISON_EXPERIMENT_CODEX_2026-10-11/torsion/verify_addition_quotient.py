from sage.all import *
import json,time,glob
E=EllipticCurve(QQ,[1,1,1,3,12]);F=NumberField(E.division_polynomial(5),'u');u=F.gen(); PP=PolynomialRing(F,'z');z=PP.gen()
f=lambda A,x:x**3+A.b2()/4*x**2+A.b4()/2*x+A.b6()/4
x2=(3*u*u+E.b2()/2*u+E.b4()/2)**2/(4*f(E,u))-E.b2()/4-2*u
psi=PP(E.division_polynomial(5));h=(psi//((z-u)*(z-x2))).monic();L=PP.quotient(h,'v');v=L.gen();d=f(E,L(u))*f(E,v)
# Exact quadratic etale algebra L[w]/(w^2-d), without costly absolute number-field conversion.
class Q:
 def __init__(self,a,b=0):
  if isinstance(a,Q): self.a,self.b=a.a,a.b
  else:self.a,self.b=L(a),L(b)
 def __add__(self,o):o=Q(o);return Q(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __neg__(self):return Q(-self.a,-self.b)
 def __sub__(self,o):return self+-Q(o)
 def __rsub__(self,o):return Q(o)+-self
 def __mul__(self,o):o=Q(o);return Q(self.a*o.a+self.b*o.b*d,self.a*o.b+self.b*o.a)
 __rmul__=__mul__
 def __invert__(self):
  den=self.a*self.a-self.b*self.b*d
  gg,ss,tt=den.lift().xgcd(h); assert gg.degree()==0 and gg!=0
  deninv=L(ss/gg[0]);return Q(self.a*deninv,-self.b*deninv)
 def __truediv__(self,o):return self*~Q(o)
 def __rtruediv__(self,o):return Q(o)*~self
 def __pow__(self,n):
  if n<0:return (~self)**(-n)
  r=Q(1);a=self
  while n:
   if n%2:r=r*a
   a=a*a;n//=2
  return r
 def __eq__(self,o):o=Q(o);return self.a==o.a and self.b==o.b

def ev(cs,x):
 r=Q(0)
 for c in reversed(cs):r=r*x+QQ(c)
 return r
x=Q(u);z=Q(v);w=Q(0,1);fx=f(E,x)
xr=(f(E,z)+fx-2*w)/(z-x)**2-E.b2()/4-x-z
vr=-1+(w/fx-1)*(x-xr)/(z-x)
print('universal independent pair algebra ready; QQ dimension 240',flush=True)
outputs=[]
for fn in sorted(glob.glob('map_*_0.json')):
 t=time.monotonic();j=json.load(open(fn));C=EllipticCurve(QQ,[QQ(q) for q in j['target_ainvs']]);rc=j['x_coeffs'];sc=j['Y_factor_coeffs'];r=lambda x:ev(rc,x);s=lambda x:ev(sc,x)
 sx,sz,rx,rz=s(x),s(z),r(x),r(z)
 xrt=(sz**2*f(E,z)+sx**2*fx-2*sz*sx*w)/(rz-rx)**2-C.b2()/4-rx-rz
 vrt=-sx+(sz*w/fx-sx)*(rx-xrt)/(rz-rx)
 checks={'independent_addition_x':r(xr)==xrt,'independent_addition_y':s(xr)*vr==vrt}
 rp=PolynomialRing(QQ,'q')([QQ(q) for q in rc]);sp=rp.parent()([QQ(q) for q in sc]);xe=F(u);x2e=F(x2);slopee=(3*xe*xe+E.b2()/2*xe+E.b4()/2)/(2*f(E,xe));ve2_over_ve=-1+slopee*(xe-x2e);xt=rp(xe);st=sp(xe);x2t=(3*xt*xt+C.b2()/2*xt+C.b4()/2)**2/(4*f(C,xt))-C.b2()/4-2*xt;vt2_over_ve=-st+(3*xt*xt+C.b2()/2*xt+C.b4()/2)/(2*st*f(E,xe))*(xt-x2t)
 checks.update(doubling_x=rp(x2e)==x2t,doubling_y=sp(x2e)*ve2_over_ve==vt2_over_ve)
 print(fn,checks,'seconds',time.monotonic()-t,flush=True);assert all(checks.values());outputs.append({'map':fn,'checks':checks,'seconds':time.monotonic()-t})
 json.dump(outputs,open('ADDITION_CHECKS.json','w'),indent=2)
