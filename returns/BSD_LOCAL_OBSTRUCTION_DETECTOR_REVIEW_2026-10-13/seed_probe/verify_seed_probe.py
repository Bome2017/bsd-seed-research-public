"""Independent standard-library exact finite-field check; no PARI/Sage imports."""
from pathlib import Path
import ast,json,hashlib
ROOT=Path(__file__).parent
A2,A4,A6=-1,-66020924,-65074271436
PTS=[(-3031,327384),(-2394,281520)]
b2,b4,b6,b8=4*A2,2*A4,4*A6,4*A2*A6-A4*A4
DISC=-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6

def prime(n):
 if n<2:return False
 return all(n%d for d in range(2,__import__('math').isqrt(n)+1))
def rhs(x,q):return (x*x*x+A2*x*x+A4*x+A6)%q
def oncurve(P,q):return P is None or (P[1]*P[1]-rhs(P[0],q))%q==0

def add(P,Q,q):
 if P is None:return Q
 if Q is None:return P
 x,y=P;xx,yy=Q
 if x==xx:
  if (y+yy)%q==0:return None
  m=(3*x*x+2*A2*x+A4)*pow(2*y,-1,q)%q
 else:m=(yy-y)*pow(xx-x,-1,q)%q
 xxx=(m*m-A2-x-xx)%q
 result=(xxx,(-y+m*(x-xxx))%q)
 assert oncurve(result,q)
 return result

def mul(P,n,q):
 R=None
 while n:
  if n&1:R=add(R,P,q)
  P=add(P,P,q);n>>=1
 return R

def card(q):
 n=q+1
 for x in range(q):
  a=rhs(x,q)
  if a:n+=1 if pow(a,(q-1)//2,q)==1 else -1
 return n

def quotpoint(P,n,q):return mul((P[0]%q,P[1]%q),n//5,q)
rows=[];first=None
for q in range(2,30001):
 if q==5 or not prime(q) or DISC%q==0:continue
 n=card(q)
 if n%5 or n%25==0:continue
 images=[quotpoint(P,n,q) for P in PTS]
 rows.append({'q':q,'cardinality':n,'images':images,'global_image_dimension':int(any(P is not None for P in images))})
 if all(P is None for P in images):first=q;break
assert first==1783
# Bind the PARI producer's rows and independently match every one.
producer=[]
for line in (ROOT/'scan.out').read_text().splitlines():
 if line.startswith('['):
  q,n,h,P,Q=ast.literal_eval(line)
  producer.append({'q':q,'cardinality':n,'images':[None if z==[0] else tuple(z) for z in (P,Q)],'global_image_dimension':int(P!=[0] or Q!=[0])})
assert rows==producer
assert not (ROOT/'scan.err').read_text().strip()
assert (ROOT/'scan.out').read_text().endswith('FIRST_HIT=1783\nDONE\n')
q=first;n=rows[-1]['cardinality'];reduced=[(x%q,y%q) for x,y in PTS]
ytable={}
for y in range(q):ytable.setdefault(y*y%q,[]).append(y)
allpoints=[None]
for x in range(q):allpoints.extend((x,y) for y in ytable.get(rhs(x,q),[]))
assert len(allpoints)==n
preimages=[None,None];local=None
for R in allpoints[1:]:
 S=mul(R,5,q)
 for i,P in enumerate(reduced):
  if preimages[i] is None and S==P:preimages[i]=R
 if local is None and mul(R,n//5,q) is not None:local=R
assert all(P is not None for P in preimages) and local is not None
T=mul(local,n//5,q);assert T is not None and mul(T,5,q) is None
witness={'q':q,'cardinality':n,'cofactor':n//5,'reduced_MW_points':reduced,
         'explicit_five_preimages':preimages,'local_quotient_generator_representative':local,
         'nonzero_order5_projection':T,'all_points_count':len(allpoints)}
result={'status':'BOUNDED_HIT_AND_INDEPENDENT_EXACT_REPLAY','sealed_bound':30000,
        'first_hit':first,'admitted_rows_tested':len(rows),'admitted_rows':rows,'witness':witness,
        'uses_no_new_Selmer_or_Lvalue_data':True,
        'arithmetic_claim':'Local quotient has dimension one and retained full MW basis has zero image',
        'Sha5_vanishing':'RETAINED_SEPARATE_INPUT_NOT_DEDUCED_HERE'}
(ROOT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'admitted_rows_tested':len(rows),'witness':witness},indent=2))
