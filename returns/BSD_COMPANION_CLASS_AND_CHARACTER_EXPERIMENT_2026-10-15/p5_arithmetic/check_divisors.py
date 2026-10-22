"""Exact finite-field review of exported arithmetic prime permutations.
No Selmer rank or norm-kernel dimension is an input.
"""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent

def rank(a,p=5):
 a=[[v%p for v in row] for row in a];r=0
 for j in range(len(a[0]) if a else 0):
  k=next((k for k in range(r,len(a)) if a[k][j]),None)
  if k is None:continue
  a[r],a[k]=a[k],a[r];v=pow(a[r][j],-1,p);a[r]=[v*x%p for x in a[r]]
  for k in range(len(a)):
   if k!=r:
    v=a[k][j];a[k]=[(x-v*y)%p for x,y in zip(a[k],a[r])]
  r+=1
 return r

def dimensions(pm):
 n=len(pm);P=[[int(pm[j]==i+1) for j in range(n)] for i in range(n)]
 return {str(c):n-rank([[P[i][j]-c*(i==j) for j in range(n)] for i in range(n)]) for c in (2,3)}

def ap(model,p):
 a1,a2,a3,a4,a6=model
 n=1+sum((y*y+a1*x*y+a3*y-x*x*x-a2*x*x-a4*x-a6)%p==0 for x in range(p) for y in range(p))
 return p+1-n

results={}
for d in [R,R/'control37']:
 path=d/'arithmetic.json';a=json.loads(path.read_text());out=[]
 for q in a['primes']:
  n=len(q['ef']);pm=q['scalar2_permutation'];assert sorted(pm)==list(range(1,n+1))
  assert sum(e*f for e,f in q['ef'])==24
  for i in range(n):
   j=i
   for _ in range(4):j=pm[j]-1
   assert j==i
  dims=dimensions(pm)
  assert dims['2']==len(q['chi2_basis']) and dims['3']==len(q['chi3_basis'])
  for ch in (2,3):
   for v in q[f'chi{ch}_basis']:
    pv=[0]*n
    for j in range(n):pv[pm[j]-1]=v[j]
    assert all((pv[j]-ch*v[j])%5==0 for j in range(n))
  out.append({'prime':q['p'],'primitive_prime_count':n,'faithful_character_dimensions':dims})
 results['389a1' if d==R else '37a1']={'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'primes':out,'a5_independent_count':ap(a['model'],5)}

# Complex conjugation on the actual full-image E[5] permutation representation:
# eigenvalues +1,-1, giving 4 real embeddings and 10 pairs of complex embeddings.
V={(x,y) for x in range(5) for y in range(5)}-{(0,0)}
arch=sorted({tuple(sorted({(x,y),(x,-y%5)})) for x,y in V})
assert sum(len(o)==1 for o in arch)==4 and sum(len(o)==2 for o in arch)==10
pm=[arch.index(tuple(sorted({(2*x%5,2*y%5) for x,y in o})))+1 for o in arch]
assert dimensions(pm)=={'2':3,'3':3}
results['ordinary_unit_character_rank']={'2':3,'3':3,'reason':'nontrivial scalar character in the augmentation-zero archimedean permutation module','archimedean_scalar_permutation':pm,'requires':'full E[5] image and Dirichlet unit representation; no fundamental units supplied'}
results['status']='EXACT_DIVISOR_AND_CHARACTER_CHECK_PASS'
(R/'CHECK_DIVISORS.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
