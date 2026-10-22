from fractions import Fraction as Q
import json,hashlib
from pathlib import Path
A=(0,1,1,-36,20); p=5
def on(P):
 if P is None:return True
 x,y=P;a1,a2,a3,a4,a6=A
 return y*y+a1*x*y+a3*y==x*x*x+a2*x*x+a4*x+a6
def add(P,R):
 if P is None:return R
 if R is None:return P
 x,y=P;z,w=R;a1,a2,a3,a4,a6=A
 if x==z and y+w+a1*x+a3==0:return None
 if x==z:
  den=2*y+a1*x+a3
  lam=(3*x*x+2*a2*x+a4-a1*y)/den
  nu=(-x*x*x+a4*x+2*a6-a3*y)/den
 else:lam=(w-y)/(z-x);nu=(y*z-w*x)/(z-x)
 xx=lam*lam+a1*lam-a2-x-z;yy=-(lam+a1)*xx-nu-a3
 ans=(xx,yy);assert on(ans);return ans
def mul(n,P):
 R=None
 while n:
  if n&1:R=add(R,P)
  n//=2;P=add(P,P)
 return R
def vpint(n):
 if n==0:return None
 v=0
 while n%p==0:v+=1;n//=p
 return v
def modq(x,q):return x.numerator*pow(x.denominator,-1,q)%q
pts=[(Q(-6),Q(7)),(Q(9),Q(22))];G=(Q(0),Q(4))
cycle=[None]+[tuple(modq(c,2) for c in mul(k,G)) for k in range(1,5)]
logs=[];dlogs=[];detail=[]
for P in pts:
 assert on(P)
 Y=mul(12,P);t=-Y[0]/Y[1]
 assert vpint(t.numerator)-vpint(t.denominator)==1
 rho=modq(t/5,5);logs.append(rho)
 rp=tuple(modq(c,2) for c in P);dl=cycle.index(rp);dlogs.append(dl)
 detail.append({'point':list(map(str,P)),'12P':list(map(str,Y)),'t_over_5_mod5':rho,'dlog_mod2':dl})
assert logs==[1,4] and dlogs==[4,3]
assert (dlogs[0]*logs[1]-dlogs[1]*logs[0])%5==3
out={'curve':A,'coefficient_prime':5,'auxiliary_prime':2,'cycle_E_F2':cycle,'points':detail,'determinant_mod5':3,'scope':'exact rational group law and formal parameter; log(12P)=t mod25 for the integral formal logarithm. Uses no padic-log engine, rank oracle or Sha input. Common multiplier12 is a5-unit.'}
Path('experiment/independent_points.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
