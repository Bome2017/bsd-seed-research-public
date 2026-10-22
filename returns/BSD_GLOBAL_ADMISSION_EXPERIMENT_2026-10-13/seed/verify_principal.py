"""Standard-library exact check independent of Sage resultant and point routines."""
from fractions import Fraction
import json,pathlib,math
D=pathlib.Path(__file__).parent
A=-66020924;B=-65074271436
def add(a,b):
 c=[0]*max(len(a),len(b))
 for i,x in enumerate(a):c[i]+=x
 for i,x in enumerate(b):c[i]+=x
 while len(c)>1 and c[-1]==0:c.pop()
 return c
def scale(a,n):return [x*n for x in a]
def mul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c
def power(a,n):
 c=[1]
 for _ in range(n):c=mul(c,a)
 return c
b2=-4;b4=2*A;b6=4*B;b8=-4*B-A*A
h=[B,A,-1,1]
p3=[b8,3*b6,3*b4,b2,3]
h4=[b4*b8-b6*b6,b2*b8-b4*b6,10*b8,10*b6,5*b4,b2,2]
f5=add(scale(mul(power(h,2),h4),16),scale(power(p3,3),-1))
assert f5[-1]==5 and len(f5)==13
def det(m):
 m=[r[:] for r in m];n=len(m);prev=1;sgn=1
 for k in range(n-1):
  if m[k][k]==0:
   j=next(j for j in range(k+1,n) if m[j][k]);m[k],m[j]=m[j],m[k];sgn=-sgn
  pivot=m[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    num=m[i][j]*pivot-m[i][k]*m[k][j];assert num%prev==0;m[i][j]=num//prev
   m[i][k]=0
  prev=pivot
 return sgn*m[-1][-1]
def res(a,b):
 da=len(a)-1;db=len(b)-1;ad=a[::-1];bd=b[::-1]
 mat=[[0]*i+ad+[0]*(db-1-i) for i in range(db)]
 mat += [[0]*i+bd+[0]*(da-1-i) for i in range(da)]
 return det(mat)
def val(n,p):
 v=0
 while n%p==0:n//=p;v+=1
 return v
def ev(poly,x,p):
 z=0
 for c in reversed(poly):z=(z*x+c)%p
 return z
rows=json.loads((D/'leak_repair.json').read_text()); receipts=[]
for row in rows:
 r=row['r'];g=h[:];g[0]-=r*r
 norm=Fraction(res(f5,g),125);assert norm==Fraction(row['norm'])
 for p,v in row['small_prime_support']:assert val(norm.numerator,p)==v
 checked=[]
 for loc in row['local_data']:
  p=loc['prime'];roots=[x for x in range(p) if ev(f5,x,p)==0 and ev(g,x,p)==0]
  assert roots==[t['x'] for t in loc['torsion_points_y_r']]
  total=1
  for x in range(p):
   y2=ev(h,x,p)
   total+=1 if y2==0 else 2 if pow(y2,(p-1)//2,p)==1 else 0
  assert total==loc['point_count']
  checked.append({'prime':p,'roots':roots,'point_count':total})
 receipts.append({'r':r,'exact_norm_matches':True,'local_checks':checked})
(D/'verify_principal.json').write_text(json.dumps({'status':'PASS','method':'integer polynomial recurrence,15x15 Bareiss determinant, finite residue enumeration','checks':receipts},indent=2)+'\n')
print('PASS')
