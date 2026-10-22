from pathlib import Path
from itertools import product
import json,hashlib
R=Path('/Users/bsm/BSD_CLASS_LIFT_COUPLING_CONTINUATION_CLAUDE_2026-10-14');O=Path(__file__).resolve().parent
labels=['1141a1','1246c1_retry600','1480a1','1525c1','1613a1_grh']
def mv(a,v):return tuple(sum(x*y for x,y in zip(r,v))%3 for r in a)
def cols(a):return list(zip(*a))
def span(a):
 return {mv(a,c):c for c in product(range(3),repeat=len(a[0]))}
def rnk(a):
 a=[list(map(lambda v:v%3,r)) for r in a];p=0
 if not a:return 0
 for j in range(len(a[0])):
  k=next((k for k in range(p,len(a)) if a[k][j]),None)
  if k is None:continue
  a[p],a[k]=a[k],a[p];v=a[p][j];a[p]=[(z*pow(v,-1,3))%3 for z in a[p]]
  for k in range(p+1,len(a)):
   v=a[k][j];a[k]=[(z-v*t)%3 for z,t in zip(a[k],a[p])]
  p+=1
  if p==len(a):break
 return p
out=[]
for label in labels:
 f=R/f'arithmetic/{label}/matrices.json';x=json.loads(f.read_text());N=x['source_dimension'];V=x['valuation'];H=x['valuation_zero_basis'];U=x['units'];P=x['points'];CC=x['class_boundary_H0'];CL=x['class_lifts']
 hs=span(H);us=span(U);ps=span(P);zero=(0,)*N
 assert len(hs)==243 and len(us)==81 and len(ps)==9
 assert N-rnk(V)==5 and all(not any(mv(V,z)) for z in hs)
 assert all(z in hs and not any(mv(CC,hs[z])) for z in us)
 assert {z for z in hs if not any(mv(CC,hs[z]))}==set(us)
 assert all(z in hs for z in ps)
 pnonzero=[j for j,c in enumerate(cols(P)) if any(c)]
 PB=[[r[j] for j in pnonzero] for r in P];pbs=span(PB);assert len(pnonzero)==2 and len(pbs)==9
 blocks=[]
 for name,D in [('scalar',x['scalar']),('scalar_add',x['scalar']+x['additivity']),('local',x['local']),('joint',x['scalar']+x['additivity']+x['local'])]:
  accepted={z for z in hs if not any(mv(D,z))}; acceptedunits=set(us)&accepted
  dc={mv(CC,hs[z]) for z in accepted}
  assert len(dc)==3 and len(acceptedunits)==3 and len(accepted)==9 if name=='joint' else True
  repairs=[]
  for c in cols(CL):
   r=[(u,us[u],tuple((a+b)%3 for a,b in zip(c,u))) for u in us if not any(mv(D,tuple((a+b)%3 for a,b in zip(c,u))))]
   assert r
   z=r[0][2];repairs.append({'raw_defect':mv(D,c),'chosen_unit_exponents':r[0][1],'repaired_column':z,'point_coordinates':pbs.get(z)})
  blocks.append({'block':name,'full_source_kernel_dim':N-rnk(D),'H0_accepted_size':len(accepted),'unit_accepted_size':len(acceptedunits),'class_image_size':len(dc),'repairs':repairs})
  if name=='joint':assert accepted==set(ps) and N-rnk(D)==2
 out.append({'curve':label,'status':'EXHAUSTIVE_H0_UNITS_POINTS_AND_REPAIRS_PASS','input_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'nonzero_point_columns_0based':pnonzero,'H0_size':len(hs),'unit_size':len(us),'point_size':len(ps),'point_unit_intersection_size':len(set(ps)&set(us)),'point_class_coordinates':[mv(CC,hs[tuple(z)]) for z in cols(P)],'blocks':blocks})
(O/'exhaustive_matrix_results.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps([{k:v for k,v in x.items() if k!='blocks'} for x in out],indent=2))
