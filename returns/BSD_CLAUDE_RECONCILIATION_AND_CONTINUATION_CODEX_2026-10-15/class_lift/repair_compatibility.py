from pathlib import Path
import json,runpy,hashlib
O=Path(__file__).resolve().parent;R=Path('/Users/bsm/BSD_CLASS_LIFT_COUPLING_CONTINUATION_CLAUDE_2026-10-14')
f=runpy.run_path(str(O/'mirror389/coupling_variable_rank.py'));mul,ker,tr,rank,solve,zero,cat=[f[k] for k in ['mul','ker','tr','rank','solve','zero','cat']]
labels=['718b1','997c1','1070a1','1141a1','1246c1_retry600','1480a1','1525c1','1613a1_grh','mirror389'];out=[]
for label in labels:
 p=O/'mirror389/matrices.json' if label=='mirror389' else R/f'arithmetic/{label}/matrices.json';d=json.loads(p.read_text());U=d['units'];G=d['scalar']+d['additivity'];L=d['local'];C=d['class_lifts'];nu=len(U[0]);GU,LU=mul(G,U),mul(L,U);KG,KL=ker(GU,nu),ker(LU,nu);SUM=cat(KG,KL);Q=tr(ker(tr(SUM),nu));assert zero(mul(Q,SUM));rows=[]
 for beta in tr(C):
  Gb=mul(G,[[a]for a in beta]);Lb=mul(L,[[a]for a in beta]);ug=solve(GU,[-r[0]for r in Gb],nu);ul=solve(LU,[-r[0]for r in Lb],nu);diff=[(a-b)%3 for a,b in zip(ug,ul)];qv=[r[0]for r in mul(Q,[[x]for x in diff])];sep=None
  for j,v in enumerate(qv):
   if v:
    sep=[pow(v,-1,3)*a%3 for a in Q[j]];assert zero(mul([sep],SUM)) and sum(a*b for a,b in zip(sep,diff))%3==1;break
  rows.append({'global_repair':ug,'local_repair':ul,'difference_global_minus_local':diff,'compatibility_quotient_coordinates':qv,'compatible':not any(qv),'separating_functional':sep})
 out.append({'curve':label,'input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'units_dimension':nu,'global_admitted_units':nu-rank(GU),'local_admitted_units':nu-rank(LU),'sum_of_repair_kernels_rank':rank(SUM),'compatibility_quotient_dimension':nu-rank(SUM),'quotient_map':Q,'class_lifts':rows})
(O/'repair_compatibility.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps([{k:v for k,v in x.items() if k not in ['input_sha256','quotient_map']} for x in out],indent=2))
