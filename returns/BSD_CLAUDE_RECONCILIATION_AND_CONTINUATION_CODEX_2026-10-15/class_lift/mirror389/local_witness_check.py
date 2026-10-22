from pathlib import Path
from fractions import Fraction as F
import json,runpy
R=Path(__file__).resolve().parent
f=runpy.run_path(str(R/'coupling_variable_rank.py'));mul=f['mul'];x=json.loads((R/'matrices.json').read_text());b=json.loads((R/'coupling.json').read_text())['cases'][0]['blocks'];g=b[1]['repairs'][0]['source_exponents'];l=b[2]['repairs'][0]['source_exponents'];out=[]
for block in x['local_blocks']:
 a=[r[0] for r in mul(block['rows'],[[v]for v in g])];c=[r[0]for r in mul(block['rows'],[[v]for v in l])];assert not any(c)
 out.append({'prime':block['prime'],'global_repaired_class_local_defect':a,'nonzero_rows_0based':[[i,v]for i,v in enumerate(a)if v],'local_repair_defect':c})
def val(a,p):
 if not a:return None
 z=0;n,d=a.numerator,a.denominator
 while n%p==0:n//=p;z+=1
 while d%p==0:d//=p;z-=1
 return z
cert=[]
for row in json.loads((R/'local_precision.json').read_text()):
 p=row['prime'];xx,yy=F(row['x']),F(row['y']);fun=yy*yy+yy-xx**3+21*xx+27;der=2*yy+1
 assert fun==F(row['F']) and der==F(row['Fp'])
 if fun:assert val(fun,p)>2*val(der,p);N=val(fun,p)-val(der,p)
 else:N=row['certified_precision']
 assert N==row['certified_precision'];m=[e*N-v-depth for e,v,depth,_ in row['prime_ideal_data']];assert min(m)>=0;cert.append({'prime':p,'N':N,'margins':m})
result={'status':'LOCAL_DEFECT_AND_RATIONAL_HENSEL_PASS','defects':out,'samples':len(cert),'minimum_margin':min(v for r in cert for v in r['margins']),'hensel':cert}
(R/'local_witness_check.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
