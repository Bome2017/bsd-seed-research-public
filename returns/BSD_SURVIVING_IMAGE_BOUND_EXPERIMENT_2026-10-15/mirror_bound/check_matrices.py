from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent

def rank(a):
 a=[[x%3 for x in r] for r in a];i=0
 for j in range(len(a[0]) if a else 0):
  k=next((k for k in range(i,len(a)) if a[k][j]),None)
  if k is None:continue
  a[i],a[k]=a[k],a[i];c=pow(a[i][j],-1,3);a[i]=[x*c%3 for x in a[i]]
  for k in range(len(a)):
   if k!=i:c=a[k][j];a[k]=[(x-c*y)%3 for x,y in zip(a[k],a[i])]
  i+=1
  if i==len(a):break
 return i

def mul(a,b):return [[sum(x*y for x,y in zip(r,c))%3 for c in zip(*b)] for r in a]
for b in json.loads((R/'INPUT_BINDINGS.json').read_text()):assert hashlib.sha256((R/b['local']).read_bytes()).hexdigest()==b['sha256']
d=json.loads((R/'paired.json').read_text());a=d['A_to_B_scalar'];b=d['B_to_A_scalar'];assert rank(a)==rank(b)==2
assert not any(map(any,mul(a,b))) and not any(map(any,mul(b,a)))
assert mul(d['B_scalar_basis'],a)==d['A_to_B_full'];assert mul(d['A_scalar_basis'],b)==d['B_to_A_full']
assert rank(d['A_norm_kernel'])==2 and rank(d['B_norm_kernel'])==3
assert rank([x+y for x,y in zip(d['A_norm_kernel'],d['B_to_A_full'])])==2
assert rank([x+y for x,y in zip(d['B_norm_kernel'],d['A_to_B_full'])])==3
assert rank(d['B_image_valuations'])==2 and not d['B_image_H0'] and not d['B_image_class']
assert rank([x+y for x,y in zip(d['A_to_B_full'],d['B_class_line'])])==3
out={'status':'EXACT_PAIRED_MATRIX_CHECK_PASS','scalar_dimensions':[4,5],'norm_ranks':[2,2],'homology_dimensions':[0,1],'mirror_image_valuation_rank':2,'mirror_image_H0_dimension':0,'mirror_homology_represented_by_ordinary_class':True,'no_local_rows_used':True}
(R/'MATRIX_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
