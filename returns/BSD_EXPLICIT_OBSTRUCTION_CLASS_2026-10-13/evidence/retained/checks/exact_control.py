"""Exact rational point/isogeny and finite-field saturation checks; stdlib only.
The rank upper bound remains the separate PARI 2-descent result.
"""
from fractions import Fraction as F
from pathlib import Path
import json
AE,BE=-19766893413,-1937478573143510
AF,BF=-14959712463303,-22270654620235278500
P=[(F(1778638,9),F(1169009812,27)),(F(6466626346478,36517849),F(2366996613841078836,220677361507))]
Q=[(F(6288329),F(-11502941299)),(F(8502485),F(21568458354))]
# Work with y'=y+1/2 and short equation y'^2=x^3+A*x+(B+1/4).
P=[(x,y+F(1,2)) for x,y in P];Q=[(x,y+F(1,2)) for x,y in Q]
def trim(a):
 while len(a)>1 and a[-1]==0:a.pop()
 return a
def addpoly(a,b):return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def scale(a,c):return trim([x*c for x in a])
def mul(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return trim(c)
def power(a,n):
 z=[F(1)]
 for _ in range(n):z=mul(z,a)
 return z
def der(a):return [i*a[i] for i in range(1,len(a))]
def ev(a,x):
 z=F(0)
 for c in reversed(a):z=z*x+c
 return z
f=list(map(F,[-43668321039996772149044128719,555932503837435168004716,-2382059022317513158,4058589566895,-1778638,1]))
h=list(map(F,[139856084578,-889319,1]))
g=addpoly(mul(h,der(f)),scale(mul(f,der(h)),-2))
def phi(pt):
 x,y=pt;hh=ev(h,x);return ev(f,x)/hh**2,y*ev(g,x)/hh**3
lhs=addpoly(addpoly(power(f,3),scale(mul(f,power(h,4)),AF)),scale(power(h,6),F(BF)+F(1,4)))
rhs=mul([F(BE)+F(1,4),AE,0,1],power(g,2))
assert addpoly(lhs,scale(rhs,-1))==[0]
def inv(x,p=None):return pow(int(x),-1,p) if p else 1/x
def add(pt,qt,A,p=None):
 if pt is None:return qt
 if qt is None:return pt
 x,y=pt;u,v=qt
 eq=lambda a,b: (a-b)%p==0 if p else a==b
 red=lambda a:a%p if p else a
 if eq(x,u):
  if eq(y,-v):return None
  m=red((3*x*x+A)*inv(red(2*y),p))
 else:m=red((v-y)*inv(red(u-x),p))
 xx=red(m*m-x-u);return xx,red(m*(x-xx)-y)
def times(pt,n,A,p=None):
 if n<0:return times((pt[0],-pt[1]),-n,A,p)
 out=None
 while n:
  if n&1:out=add(out,pt,A,p)
  pt=add(pt,pt,A,p);n//=2
 return out
assert all(y*y==x**3+AE*x+F(BE)+F(1,4) for x,y in P)
assert all(y*y==x**3+AF*x+F(BF)+F(1,4) for x,y in Q)
assert phi(P[0])==add(times(Q[0],-1,AF),times(Q[1],-1,AF),AF)
assert phi(P[1])==add(times(Q[0],3,AF),times(Q[1],-2,AF),AF)
def primes(n):
 for q in range(7,n+1):
  if all(q%k for k in range(2,int(q**.5)+1)):yield q
def res(x,q):return x.numerator*pow(x.denominator,-1,q)%q
def cert(A,B,pts):
 rows=[]
 for q in primes(3000):
  if (4*A**3+27*(F(B)+F(1,4))**2).numerator%q==0:continue
  if any(x.denominator%q==0 or y.denominator%q==0 for x,y in pts):continue
  b=res(F(B)+F(1,4),q)
  count=1
  point=None
  for x in range(q):
   z=(x**3+A*x+b)%q
   ch=0 if z==0 else (1 if pow(z,(q-1)//2,q)==1 else -1)
   count+=1+ch
  if count%5 or count%25==0:continue
  # Find any nonzero 5-torsion point in the cyclic 5-part.
  for x in range(q):
   z=(x**3+A*x+b)%q
   for y in range(q):
    if y*y%q!=z:continue
    point=times((x,y),count//5,A,q)
    if point is not None:break
   if point is not None:break
  assert point and times(point,5,A,q) is None
  table={times(point,i,A,q):i for i in range(5)}
  vals=[table[times((res(x,q),res(y,q)),count//5,A,q)] for x,y in pts]
  row={'q':q,'cardinality':count,'generator':point,'point_images':vals}
  for old in rows:
   v=old['point_images'];det=(v[0]*vals[1]-v[1]*vals[0])%5
   if det:return {'rows':[old,row],'determinant_mod_5':det}
  if vals!=[0,0]:rows.append(row)
 raise AssertionError('No independent reduction pair found within cap')
result={'isogeny_polynomial_identity':True,'exact_point_matrix':[[-1,3],[-1,-2]],'point_matrix_determinant':5,'source_saturation':cert(AE,BE,P),'target_saturation':cert(AF,BF,Q),'leading_quotient_check':(4*pow(4*4*4,-1,5))%5,'not_checked':['rank upper bound by independent descent','independent modular-symbol implementation','Sha upper bound or finiteness']}
assert result['leading_quotient_check']==1
Path('outputs/EXACT_CONTROL.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
