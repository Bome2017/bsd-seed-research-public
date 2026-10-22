#!/usr/bin/env python3
"""Finite geometric integral incidence checks, not number-field unit indices."""
from pathlib import Path
import json,itertools

def rank(A,p):
 A=[[x%p for x in r] for r in A]; i=0
 for j in range(len(A[0]) if A else 0):
  z=next((z for z in range(i,len(A)) if A[z][j]),None)
  if z is None:continue
  A[z],A[i]=A[i],A[z];inv=pow(A[i][j],-1,p);A[i]=[x*inv%p for x in A[i]]
  for z in range(len(A)):
   if z!=i:
    c=A[z][j];A[z]=[(a-c*b)%p for a,b in zip(A[z],A[i])]
  i+=1
 return i

def mul(A,B,n):return [[sum(x*y for x,y in zip(r,c))%n for c in zip(*B)] for r in A]
def prime_cases(p):
 n=p**4
 # omega(a) = a^(p^3) mod p^4 is the Teichmuller lift at this precision.
 om={a:pow(a,p**3,n) for a in range(1,p)}
 assert all(pow(x,p-1,n)==1 for x in om.values())
 assert all(om[a]*om[b]%n==om[a*b%p] for a in om for b in om)
 P=[(1,a) for a in range(p)]+[(0,1)]
 def full(k):
  return [[0 if (t:=(x*u+y*v)%p)==0 else pow(om[t],-k,n) for x,y in P] for u,v in P]
 # c=diag(1,-1): invariant coordinates0 and pairs a,-a. Infinity vanishes for odd k.
 inds=list(range((p+1)//2)); cols=[(0,)]+[(a,p-a) for a in inds[1:]]
 def real(k):
  A=full(k)
  return [[sum(A[b][j] for j in col)%n for col in cols] for b in inds]
 rows=[]
 for k in range(1,p-1,2):
  kinv=p-1-k;U=full(k);V=full(kinv)
  assert mul(V,U,n)==[[p if i==j else 0 for j in range(p+1)] for i in range(p+1)]
  R=real(k);S=real(kinv);d=(p+1)//2
  assert mul(S,R,n)==[[p if i==j else 0 for j in range(d)] for i in range(d)]
  sf=(p+1)-rank(U,p);sr=d-rank(R,p)
  assert sf==k+1 and sr==(k+1)//2
  rows.append({'k':k,'inverse_k':kinv,'full_rank':p+1,'full_mod_p_kernel':sf,
   'real_rank':d,'real_geometric_index':sr,'real_matrix_mod_p4':R})
 assert sum(row['real_geometric_index'] for row in rows)==(p*p-1)//8
 return {'p':p,'precision':4,'idempotent_denominator_unit':(p-1)%p!=0,'characters':rows,
         'sum_geometric_indices':(p*p-1)//8,'arithmetic_unit_index':None}
res={'status':'PASS','cases':[prime_cases(p) for p in (5,7,11)],
 'scope':'exact finite geometry modulo p^4; not arithmetic unit-lattice or class-number data'}
Path(__file__).with_name('CHARACTER_CHECKS.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps({'status':res['status'],'rows':[(c['p'],[(r['k'],r['real_geometric_index']) for r in c['characters']]) for c in res['cases']]}))
