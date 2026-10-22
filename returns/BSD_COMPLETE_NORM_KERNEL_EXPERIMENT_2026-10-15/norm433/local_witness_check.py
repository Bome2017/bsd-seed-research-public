from fractions import Fraction as F
from pathlib import Path
import json
R=Path(__file__).resolve().parent
ainv=[1,0,0,0,1];a1,a2,a3,a4,a6=ainv

def val(a,p):
 if not a:return None
 n,d=a.numerator,a.denominator;v=0
 while n%p==0:n//=p;v+=1
 while d%p==0:d//=p;v-=1
 return v
out=[]
for row in json.loads((R/'local_precision.json').read_text()):
 p=row['prime'];xx,yy=F(row['x']),F(row['y']);fun=yy*yy+a1*xx*yy+a3*yy-xx**3-a2*xx**2-a4*xx-a6;der=2*yy+a1*xx+a3
 assert fun==F(row['F']) and der==F(row['Fp'])
 if fun:assert val(fun,p)>2*val(der,p);N=val(fun,p)-val(der,p)
 else:N=row['certified_precision']
 assert N==row['certified_precision'];m=[e*N-v-depth for e,v,depth,_ in row['prime_ideal_data']];assert min(m)>=0
 out.append({'prime':p,'certified_precision':N,'margins':m})
result={'status':'EXACT_RATIONAL_HENSEL_CHECK_PASS','ainvariants':ainv,'samples':len(out),'minimum_margin':min(v for r in out for v in r['margins']),'checks':out}
(R/'local_witness_check.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
