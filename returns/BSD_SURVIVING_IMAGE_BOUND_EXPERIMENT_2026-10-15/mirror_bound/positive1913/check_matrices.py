from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parent

def rank(a):
 a=[[x%3 for x in r] for r in a];k=0
 for j in range(len(a[0]) if a else 0):
  z=next((i for i in range(k,len(a)) if a[i][j]),None)
  if z is None:continue
  a[k],a[z]=a[z],a[k];c=pow(a[k][j],-1,3);a[k]=[c*x%3 for x in a[k]]
  for i in range(len(a)):
   if i!=k:c=a[i][j];a[i]=[(x-c*y)%3 for x,y in zip(a[i],a[k])]
  k+=1
  if k==len(a):break
 return k

def mul(a,b):return [[sum(x*y for x,y in zip(r,c))%3 for c in zip(*b)] for r in a]
for b in json.loads((R/'INPUT_BINDINGS.json').read_text()):assert hashlib.sha256((R/b['local']).read_bytes()).hexdigest()==b['sha256']
d=json.loads((R/'reverse.json').read_text());U=d['source_unit_basis'];V=d['independent_strict_antiunit_classes'];SC=d['scalar_relation'];AD=d['retained_admission_rows']
assert rank(U)==4 and rank(V)==2 and rank([x+y for x,y in zip(U,V)])==4
assert rank(mul(SC,U))==2 and not any(map(any,mul(SC,V))) and not any(map(any,mul(AD,V)))
assert d['source_signature']==d['line_signature']==[2,3]
out={'status':'INDEPENDENT_POSITIVE_UNIT_MATRIX_CHECK_PASS','unit_rank':4,'odd_unit_rank':2,'independent_admitted_unit_classes':2,'retained_rank_zero_and_torsion_prime_to3':'retained arithmetic inputs, not re-run','no_Sha_order_input':True}
(R/'MATRIX_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
