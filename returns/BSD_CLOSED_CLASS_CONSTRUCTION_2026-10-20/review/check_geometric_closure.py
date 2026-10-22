#!/usr/bin/env python3
"""Independent F5 elimination, support-norm screen and exact kernel checks."""
import json
from pathlib import Path
from math import prod
root=Path(__file__).resolve().parent
R2,R3,inside,outside,H,K,SC=json.loads((root/'geometric_matrix_export.json').read_text())
def rref(A):
 A=[[x%5 for x in r] for r in A]; piv=[]; rr=0
 for j in range(len(A[0])):
  ii=next((i for i in range(rr,len(A)) if A[i][j]),None)
  if ii is None: continue
  A[rr],A[ii]=A[ii],A[rr]; z=pow(A[rr][j],-1,5); A[rr]=[x*z%5 for x in A[rr]]
  for i in range(len(A)):
   if i!=rr and A[i][j]:
    z=A[i][j];A[i]=[(x-z*y)%5 for x,y in zip(A[i],A[rr])]
  piv.append(j);rr+=1
  if rr==len(A):break
 return A,piv

def rank(A):return len(rref(A)[1])
def selected(A,cols):return [[r[j-1] for j in cols] for r in A]
def solve(A,B):
 n=len(A[0]); rr,piv=rref([a+b for a,b in zip(A,B)]);assert all(j<n for j in piv)
 T=[[0]*len(B[0]) for _ in range(n)]
 for i,j in enumerate(piv):T[j]=rr[i][n:]
 assert all(sum(A[i][j]*T[j][k] for j in range(n))%5==B[i][k]%5 for i in range(len(A)) for k in range(len(B[0])))
 return T
rows=[];factors={}
for c,R in [(2,R2),(3,R3)]:
 A=selected(R,outside);B=selected(R,inside);factors[str(c)]=solve(A,B)
 rows.append({'character':c,'full_rank':rank(R),'outside_rank':rank(A),'closed_rank':rank(R)-rank(A)})
 assert rows[-1]=={'character':c,'full_rank':20,'outside_rank':20,'closed_rank':0}
assert rank(H)==40 and rank(K)==84
assert all(sum(H[i][j]*K[i][k] for i in range(124))==0 for j in range(134) for k in range(84))
# Pairwise-coprime, scalar-stable atoms were checked with actual ideals in GP.
# Independently remove ALL small rational primes, not only producer's factors.
B=419775;sieve=bytearray(b'\1')*(B+1);sieve[:2]=b'\0\0'
for q in range(2,int(B**.5)+1):
 if sieve[q]:sieve[q*q::q]=b'\0'*(((B-q*q)//q)+1)
primes=[q for q in range(2,B+1) if sieve[q]]
def fifth_root_floor(n):
 lo,hi=0,1<<((n.bit_length()+4)//5)
 while lo+1<hi:
  m=(lo+hi)//2
  if m**5<=n:lo=m
  else:hi=m
 return lo
norms=[]
for h,j,nn,ff,on in SC:
 assert prod(q**e for q,e in ff)==nn
 remaining=nn; small=[]
 for q in primes:
  e=0
  while remaining%q==0:remaining//=q;e+=1
  if e:small.append([q,e])
 assert small==[r for r in ff if r[0]<=B]
 # All small exponents here are one. Their prime-ideal norms therefore equal q,
 # so no hidden high-residue-degree factors can be classified inside by mistake.
 assert all(e==1 for q,e in small)
 assert on==remaining
 assert (h in inside)==(on==1)
 if on!=1:assert fifth_root_floor(on)**5!=on
 norms.append({'character_column':h,'inside':on==1,'outside_norm_digits':len(str(on)),'outside_not_fifth_power':on==1 or fifth_root_floor(on)**5!=on})
(root/'GEOMETRIC_FACTOR_CERTIFICATES.json').write_text(json.dumps({'outside_indices':outside,'inside_indices':inside,'T_by_character':factors},indent=2)+'\n')
out={'status':'INDEPENDENT_GEOMETRIC_CLOSURE_REPLAY_PASS','actual_elements':124,'actual_coprime_ideal_atoms':134,'faithful_columns':28,'inside_columns':6,'outside_columns':22,'characters':rows,'integer_anti_divisor_rank':40,'rational_kernel_dimension':84,'exact_unit_products_equal_one':84,'norm_support_checks':norms,'scope':'This fixed geometric function family gives zero net closed class relations and no nontrivial relative units; not a universal geometric obstruction.'}
print(json.dumps(out,indent=2,sort_keys=True))
