from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent
D,K=json.loads((R/'saved_divisor_kernel.json').read_text())
def rankmod(A,p):
 a=[[x%p for x in r]for r in A];r=0
 for j in range(len(a[0])):
  piv=next((i for i in range(r,len(a)) if a[i][j]),None)
  if piv is None:continue
  a[r],a[piv]=a[piv],a[r];q=pow(a[r][j],-1,p);a[r]=[(q*x)%p for x in a[r]]
  for i in range(len(a)):
   if i!=r and a[i][j]:
    q=a[i][j];a[i]=[(x-q*y)%p for x,y in zip(a[i],a[r])]
  r+=1
  if r==len(a):break
 return r
zero=all(sum(x*y for x,y in zip(row,col))==0 for row in D for col in zip(*K))
assert zero
ranks={str(p):{'D':rankmod(D,p),'K':rankmod(K,p)} for p in [7,101]}
assert ranks['101']=={'D':57,'K':99}
# With D K=0 and rank K>=99, rank D<=156-99=57; mod101 rank57 proves exactQ rank57.
res={'status':'PASS','D_shape':[len(D),len(D[0])],'K_shape':[len(K),len(K[0])],'integer_product_zero':zero,'finite_field_ranks':ranks,'rational_D_rank_certified_by_complementary_modular_minors':57,'rational_kernel_dimension':99,'p7_modular_kernel_dimension':156-ranks['7']['D'],'new_mod7_relations_beyond_reductions_of_integer_kernel':156-ranks['7']['D']-ranks['7']['K'],'interpretation':'exponent relations authenticate units; no claim their field classes independent or complete; modular additional relations if any are only candidates for class-supported virtual units'}
(R/'DIVISOR_LINEAR_CHECK.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
