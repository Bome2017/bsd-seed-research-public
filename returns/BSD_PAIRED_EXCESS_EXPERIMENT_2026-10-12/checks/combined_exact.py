"""Independent exact rational and finite-field audit for d=329233.
Only the rank upper bound is retained from the separate PARI 2-descent.
Uses stdlib; no L-value, height, class number or Sha-order input.
"""
from fractions import Fraction as F
from pathlib import Path
import json,math
D=329233
CA=-1;AA=-1120075138986;BA=-826418095533154920
CF=-1;AF=-847680091476076;BF=-9499397825675855099600
P=[(F(98165584318497,61716736),F(576969269528443132623,484846678016)),(F(10267334825985669,508502500),F(1038884602172450739859303,11466731375000))]
Q=[(F(768989753271757,14455204),F(17024641241085675393245,54958685608)),(F(1029644930091713,27164944),F(16034242814568548143769,141583688128))]
P=[(x,y+F(1,2)) for x,y in P];Q=[(x,y+F(1,2)) for x,y in Q]
def trim(a):
 while len(a)>1 and a[-1]==0:a.pop()
 return a
def addp(a,b):return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def sc(a,c):return trim([x*c for x in a])
def mul(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return trim(c)
def pw(a,n):
 z=[F(1)]
 for _ in range(n):z=mul(z,a)
 return z
def der(a):return [i*a[i] for i in range(1,len(a))]
def ev(a,x):
 z=F(0)
 for c in reversed(a):z=z*x+c
 return z
h=list(map(F,[7924834935264,-6694405,1]))
fshort=[F(-1055452232006930855081468799690695),F(1785006106838454418422154818),F(-3048154507970508390805,3),F(689930207714723,3),F(-40166431,3),F(1)]
# PARI's short target -> minimal target change is [1,-1/3,0,1/2].
f=addp(fshort,sc(pw(h,2),F(1,3)))
g=addp(mul(h,der(f)),sc(mul(f,der(h)),-2))
def phi(pt):
 x,y=pt;hh=ev(h,x);return ev(f,x)/hh**2,y*ev(g,x)/hh**3
lhs=addp(addp(addp(pw(f,3),sc(mul(pw(f,2),pw(h,2)),CF)),sc(mul(f,pw(h,4)),AF)),sc(pw(h,6),F(BF)+F(1,4)))
rhs=mul([F(BA)+F(1,4),AA,CA,1],pw(g,2))
assert addp(lhs,sc(rhs,-1))==[0]
def inv(x,p=None):return pow(int(x),-1,p) if p else 1/x
def add(pt,qt,A,C,p=None):
 if pt is None:return qt
 if qt is None:return pt
 x,y=pt;u,v=qt
 eq=lambda a,b:(a-b)%p==0 if p else a==b
 red=lambda a:a%p if p else a
 if eq(x,u):
  if eq(y,-v):return None
  m=red((3*x*x+2*C*x+A)*inv(red(2*y),p))
 else:m=red((v-y)*inv(red(u-x),p))
 xx=red(m*m-C-x-u);return xx,red(m*(x-xx)-y)
def times(pt,n,A,C,p=None):
 if n<0:return times((pt[0],-pt[1]),-n,A,C,p)
 out=None
 while n:
  if n&1:out=add(out,pt,A,C,p)
  pt=add(pt,pt,A,C,p);n//=2
 return out
for pts,A,B,C in [(P,AA,BA,CA),(Q,AF,BF,CF)]:assert all(y*y==x**3+C*x*x+A*x+F(B)+F(1,4) for x,y in pts)
assert phi(P[0])==add(times(Q[0],-2,AF,CF),times(Q[1],-1,AF,CF),AF,CF)
assert phi(P[1])==add(Q[0],times(Q[1],-2,AF,CF),AF,CF)
def res(x,q):return x.numerator*pow(x.denominator,-1,q)%q
def isprime(n):return n>1 and all(n%k for k in range(2,math.isqrt(n)+1))
def disc(A,B,C):
 b2=4*C;b4=2*A;b6=1+4*B;b8=4*C*B+C-A*A
 return -b2*b2*b8-8*b4**3-27*b6**2+9*b2*b4*b6
assert isprime(D)
assert disc(AA,BA,CA)==-11**5*D**6
assert disc(AF,BF,CF)==-11*D**6

def count(A,B,C,q):
 assert disc(A,B,C)%q
 b=res(F(B)+F(1,4),q);cnt=1
 for x in range(q):
  z=(x**3+C*x*x+A*x+b)%q
  cnt+=1+(0 if z==0 else 1 if pow(z,(q-1)//2,q)==1 else -1)
 return cnt

def cert(A,B,C,pts):
 rows=[]
 for q in range(7,3000):
  if not isprime(q) or disc(A,B,C)%q==0:continue
  if any(x.denominator%q==0 or y.denominator%q==0 for x,y in pts):continue
  cnt=count(A,B,C,q)
  if cnt%5 or cnt%25==0:continue
  b=res(F(B)+F(1,4),q);point=None
  for x in range(q):
   z=(x**3+C*x*x+A*x+b)%q
   for y in range(q):
    if y*y%q!=z:continue
    point=times((x,y),cnt//5,A,C,q)
    if point is not None:break
   if point is not None:break
  assert point and times(point,5,A,C,q) is None
  table={times(point,i,A,C,q):i for i in range(5)}
  vals=[table[times((res(x,q),res(y,q)),cnt//5,A,C,q)] for x,y in pts]
  row={'q':q,'cardinality':cnt,'generator':point,'point_images':vals}
  for old in rows:
   v=old['point_images'];dt=(v[0]*vals[1]-v[1]*vals[0])%5
   if dt:return {'rows':[old,row],'determinant_mod_5':dt}
  if vals!=[0,0]:rows.append(row)
 raise AssertionError('No certificate within q<3000')

def vp(a,p):
 a=F(a)
 def v(n):
  if n==0:return 10**9
  k=0
  while n%p==0:n//=p;k+=1
  return k
 return v(a.numerator)-v(a.denominator)

def local(A,B,C):
 b2=4*C;b4=2*A;b6=1+4*B
 c4=b2*b2-24*b4;c6=-b2**3+36*b2*b4-216*b6
 assert vp(c4,11)==0 and pow((-c6)%11,5,11)==1
 n=vp(disc(A,B,C),11)
 q=D;r=(1-D)//3
 a2=3*r+C;a4=3*r*r+2*C*r+A;a6=F(r**3+C*r*r+A*r+B)+F(1,4)
 assert vp(a2,q)>=1 and vp(a4,q)>=2 and vp(a6,q)>=3
 co=[res(a6/q**3,q),res(F(a4,q*q),q),res(F(a2,q),q),1]
 roots=[t for t in range(q) if ev(co,t)%q==0]
 sep=all((3*t*t+2*co[2]*t+co[1])%q!=0 for t in roots)
 assert sep and len(roots)==3
 return {'11':{'type':'split I_'+str(n),'c':n},str(q):{'type':'I_0*','c':1+len(roots),'cubic':co,'roots':roots,'separable':sep},'product':n*(1+len(roots))}

hhdisc=h[1]**2-4*h[0];rr=math.isqrt(hhdisc.numerator);assert F(rr*rr)==hhdisc
roots=[(-h[1]-rr)/2,(-h[1]+rr)/2]
real=[]
for x in roots:
 Y2=x**3+CA*x*x+AA*x+F(BA)+F(1,4)
 assert Y2>0 and ev(f,x)!=0
 z=Y2/D;n=math.isqrt(z.numerator);d=math.isqrt(z.denominator);assert F(n*n,d*d)==z
 real.append({'x':str(x),'Y2_over_D_square_root':str(F(n,d))})
# Differential pullback is exactly one by the defining polynomial g.
assert addp(mul(h,der(f)),sc(mul(f,der(h)),-2))==g
# For each candidate rational torsion prime, at least one different good prime
# has point count not divisible by it. In this sample gcd of counts at 7,13,19
# is one and no characteristic-prime exception survives the other counts.
cts={str(q):count(AA,BA,CA,q) for q in [5,7,13,19]}
assert cts=={str(q):count(AF,BF,CF,q) for q in [5,7,13,19]}
poss=set()
for v in cts.values():
 for l in range(2,v+1):
  if isprime(l) and v%l==0:poss.add(l)
for l in poss:assert any(int(q)!=l and v%l!=0 for q,v in cts.items())
la=local(AA,BA,CA);lf=local(AF,BF,CF);assert la['product']==20 and lf['product']==4
out={'status':'PASS_EXACT_ARITHMETIC_UNDER_RETAINED_RANK_TWO_UPPER_BOUND','d':D,'models':{'A':[0,CA,1,AA,BA],'F':[0,CF,1,AF,BF]},'isogeny_polynomial_identity':True,'differential_pullback':1,'point_matrix':[[-2,1],[-1,-2]],'point_matrix_determinant':5,'point_images_exact':True,'source_saturation':cert(AA,BA,CA,P),'target_saturation':cert(AF,BF,CF,Q),'small_counts':cts,'rational_torsion_order':1,'real_kernel':real,'period_F_over_A':'1/5','local_A':la,'local_F':lf,'Cassels_Selmer_phi_over_dual':'1/25','Sha_F_dual_kernel_dimension_minus_Sha_A_phi_kernel_dimension':2,'Sha_F_5_dimension_lower_bound':2,'retained_input':'rank(A)<=2 from saved PARI two-descent; no descent replay','not_proved':['Sha upper bound','Sha finiteness','exact Sha order','full residual image','seed consequence']}
Path('outputs/combined_exact.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
