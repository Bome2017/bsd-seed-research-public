"""Independent exhaustive common-point repair check. No pilot/library imports."""
from pathlib import Path
from itertools import product
import json,hashlib
R=Path(__file__).resolve().parent
contracts=[p for p in R.glob('COMMON_POINT_CONTRACT*') if p.is_file()]
inputs={name:json.loads((R/'inputs'/name).read_text()) for name in ['seed3_SIGNATURES.json','seed3_coordinates.json']}
S=inputs['seed3_SIGNATURES.json'];C=inputs['seed3_coordinates.json'];W=C['points'];K=C['known']
def mul(A,B):
 return [[sum(x*y for x,y in zip(a,b))%3 for b in zip(*B)]for a in A]
def act(A,v):return tuple(sum(a*b for a,b in zip(row,v))%3 for row in A)
blocks=[]
for q in (1213,1543,1699):
 b=next(z for z in S['fresh_primes']if z['prime']==q);M=b['source_residue_rows'];MW=mul(M,W);MK=mul(M,K)
 repairs=[]
 for j in range(4):
  target=tuple(row[j]for row in MK);sol=[a for a in product(range(3),repeat=2)if act(MW,a)==target]
  assert len(sol)==1,(q,j,sol)
  repairs.append(list(sol[0]))
 A=[list(row)for row in zip(*repairs)]
 assert mul(MW,A)==MK
 assert [row[:2]for row in A]==[[1,0],[0,1]]
 blocks.append({'prime':q,'point_evaluations':MW,'class_evaluations':MK,'repair_matrix':A})
results=[]
for count in (2,3):
 selected=blocks[:count];D=[]
 for b in selected[1:]:D += [[(a-c)%3 for a,c in zip(x,y)]for x,y in zip(selected[0]['repair_matrix'],b['repair_matrix'])]
 records=[];common=[]
 for c in product(range(3),repeat=4):
  each=[]
  for b in selected:
   target=act(b['class_evaluations'],c)
   sol=[a for a in product(range(3),repeat=2)if act(b['point_evaluations'],a)==target]
   assert len(sol)==1
   each.append(sol[0])
  joint=[a for a in product(range(3),repeat=2)if all(act(b['point_evaluations'],a)==act(b['class_evaluations'],c)for b in selected)]
  predicted=all(v==0 for v in act(D,c))
  assert bool(joint)==predicted
  if joint:common.append(list(c))
  records.append({'class_coefficients':list(c),'individual_repairs':[list(a)for a in each],'common_repairs':[list(a)for a in joint]})
 image={act(D,c)for c in product(range(3),repeat=4)}
 rk=next(i for i in range(5)if 3**i==len(image))
 residual_excess=sorted({tuple(c[2:])for c in common})
 results.append({'primes':[b['prime']for b in selected],'difference_matrix':D,'rank_by_exhaustive_image_cardinality':rk,'tested_class_combinations':81,'point_coefficients_per_local_test':9,'separate_local_repairs_exist_for':81,'common_local_repairs_exist_for':len(common),'common_kernel_vectors':common,'residual_excess_vectors':[list(c)for c in residual_excess],'all_combinations':records})
assert results[0]['residual_excess_vectors']==[[0,0],[1,1],[2,2]]
assert results[1]['residual_excess_vectors']==[[0,0]]
result={'status':'INDEPENDENT_EXHAUSTIVE_COMMON_POINT_REPAIR_PASS','curve':'seed3','class_order':['P1','P2','beta1','beta2'],'blocks':blocks,'pair_and_triple':results,'bindings':[{'path':str(p.relative_to(R)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}for p in contracts+[R/'inputs'/n for n in inputs]],'scope':'Actual saved source arithmetic, independent finite verification. Known four-dimensional span only; no completeness or unseen-kernel assertion. Separate local point repairs may differ; common-point repair must use one rational-point coefficient vector at every place. Input W is used unchanged; repair matrices have identity point columns.'}
(R/'INDEPENDENT_COMMON_POINT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'repair_matrices':[(b['prime'],b['repair_matrix'])for b in blocks],'results':[{k:v for k,v in a.items()if k not in ['all_combinations','common_kernel_vectors']}for a in results]},indent=2))
