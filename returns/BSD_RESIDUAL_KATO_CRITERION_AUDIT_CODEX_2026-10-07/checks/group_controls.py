from itertools import product
import json

def mul(a,b,m):
 return ((a[0]*b[0]+a[1]*b[2])%m,(a[0]*b[1]+a[1]*b[3])%m,(a[2]*b[0]+a[3]*b[2])%m,(a[2]*b[1]+a[3]*b[3])%m)
def power(a,n,m):
 b=(1,0,0,1)
 while n:
  if n&1:b=mul(b,a,m)
  a=mul(a,a,m);n//=2
 return b
rows=[]
for p in [5,7]:
 count=0
 for a,b,c,d in product(range(p),repeat=4):
  x=(1+p*a,1+p*b,p*c,1+p*d)
  assert power(x,p,p*p)==(1,p,0,1)
  count+=1
 rows.append({"p":p,"all_matrix_lifts_checked":count})
x=(1,1,-3,-2)
assert (x[0]*x[3]-x[1]*x[2])%9==1
assert tuple(v%3 for v in x)==(1,1,0,1)
assert power(x,3,9)==(1,0,0,1)
print(json.dumps({"status":"PASS","positive_controls":rows,"p3_scope_countercontrol":"an SL2(Z/9) lift of the residual transvection has order three","scope":"finite group formula controls, not a seed image certificate or a proof of the all-prime lifting lemma"},indent=2))
