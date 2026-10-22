from sage.all import GF, PolynomialRing, matrix
from itertools import product, combinations
import json
from pathlib import Path
p=Path(__file__).parent
m=json.loads((p/'FISHER_MODEL.json').read_text())
results=[]
for ell in [2,3,5,7,11,13,17,19,61,239]:
 P=PolynomialRing(GF(ell),names=['x0','x1','x2','x3','x4']);xs=P.gens();qs=[P(q) for q in m['signed_pfaffians']]
 J=matrix(P,[[q.derivative(x) for x in xs] for q in qs]); MM=matrix(P,[[P(z) for z in row] for row in m['matrix']]); candidates=[];checked=0;positive_dim=0
 if ell<=11:
  for j in range(5):
   for tail in product(range(ell),repeat=4-j):
    v=(0,)*j+(1,)+tail
    if all(q(*v)==0 for q in qs):candidates.append(v)
 else:
  for j in range(min(ell,15)):
   I=P.ideal(qs+[xs[0]-1,xs[1]-j]);dd=I.dimension()
   if dd>0:positive_dim+=1;continue
   for sol in I.variety():candidates.append(tuple(int(sol[x]) for x in xs))
   if any(J.apply_map(lambda f:f(*v)).rank()==3 for v in candidates):break
 found=None
 for v in candidates:
  JJ=J.apply_map(lambda f:f(*v));rank=int(JJ.rank())
  if rank==3:
   for a in combinations(range(5),3):
    for b in combinations(range(5),3):
     det=JJ.matrix_from_rows_and_columns(a,b).det()
     if det:
      omitted=[z for z in range(5) if z not in a]
      pivot=MM[omitted[0],omitted[1]](*v)
      assert pivot!=0
      found={'point':v,'jacobian_rank':rank,'minor_rows':a,'minor_columns':b,'minor_value':int(det),'pfaffian_syzygy_unit_pivot':int(pivot),'omitted_equations':omitted};break
    if found:break
   break
 result={'prime':ell,'rational_mod_p_points_found':len(candidates),'sliced_positive_dimension':positive_dim,'nonsingular_witness':found,
   'scope':'Hensel witness if found; otherwise no local insolubility inference'}
 results.append(result);print(json.dumps(result),flush=True)
(p/'LOCAL_WITNESSES.json').write_text(json.dumps(results,indent=2)+'\n')
