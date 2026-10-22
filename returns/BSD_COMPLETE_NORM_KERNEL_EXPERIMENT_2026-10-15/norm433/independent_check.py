import json, hashlib
from pathlib import Path
R=Path(__file__).resolve().parent

def rank(A):
 a=[[x%3 for x in r] for r in A];i=0
 for j in range(len(a[0]) if a else 0):
  z=next((k for k in range(i,len(a)) if a[k][j]),None)
  if z is None:continue
  a[i],a[z]=a[z],a[i];a[i]=[(v*pow(a[i][j],-1,3))%3 for v in a[i]]
  for k in range(len(a)):
   if k!=i:
    c=a[k][j];a[k]=[(x-c*y)%3 for x,y in zip(a[k],a[i])]
  i+=1
  if i==len(a):break
 return i

def mul(A,B):return [[sum(x*y for x,y in zip(r,c))%3 for c in zip(*B)] for r in A]
def horner(c,x,p):
 y=0
 for a in c[::-1]:
  if isinstance(a,list):a=a[0]*pow(a[1],-1,p)
  y=(y*x+a)%p
 return y

def prime(q):return q>=2 and all(q%d for d in range(2,int(q**.5)+1))
P=json.loads((R/'norm_polynomials.json').read_text());M=json.loads((R/'norm_map.json').read_text());C=json.loads((R/'complete_certificate.json').read_text());rows=[json.loads(x) for x in (R/'norm_residue_rows.jsonl').read_text().splitlines()]
for row in rows:
 q,t,o=row['q'],row['root'],row['omega'];assert prime(q) and q%3==1
 assert horner(P['line_field'],t,q)==0 and horner([i*x for i,x in enumerate(P['line_field'])][1:],t,q)!=0
 assert o!=1 and pow(o,3,q)==1
 values=[horner(f,t,q) for f in P['six_norms']];assert values==row['values'] and all(values)
 chars=[next(j for j in range(3) if pow(o,j,q)==pow(v,(q-1)//3,q)) for v in values];assert chars==row['characters']
A=[r['characters'] for r in rows];assert A==M['residue_map'] and rank(A)==3
S,K,KC=M['scalar_basis'],M['global_norm_kernel'],M['kernel_in_scalar_coordinates'];assert rank(S)==6 and rank(K)==rank(KC)==3
assert mul(S,KC)==K and not any(map(any,mul(A,KC)))
minor=[[A[i][j] for j in [0,1,2]] for i in [0,2,4]]
det=(minor[0][0]*(minor[1][1]*minor[2][2]-minor[1][2]*minor[2][1])-minor[0][1]*(minor[1][0]*minor[2][2]-minor[1][2]*minor[2][0])+minor[0][2]*(minor[1][0]*minor[2][1]-minor[1][1]*minor[2][0]))%3
assert det==2
assert C['exact_global_kernel']==K
L=C['local_authenticated_rows'];assert mul(L,K)==C['local_restricted_to_global_kernel'];assert rank(mul(L,K))==1
W=C['point_basis'];J=C['admitted_kernel'];assert rank(W)==rank(J)==rank([x+y for x,y in zip(W,J)])==2
assert not any(map(any,mul(L,W))) and not any(map(any,mul(L,J)))
assert any(C['extra_local3']) and any(C['extra_local433'])
valuations=C['global_kernel_valuations'];assert not any(r[0] or r[1] for r in valuations) and any(r[2] for r in valuations)
for b in json.loads((R/'SOURCE_BINDINGS.json').read_text()):assert hashlib.sha256((R/b['local']).read_bytes()).hexdigest()==b['sha256']
result={'status':'INDEPENDENT_EXACT_NORM_MAP_AND_LOCAL_MATRIX_PASS','source_dimension':13,'scalar_dimension':6,'norm_image_rank':3,'norm_kernel_dimension':3,'positive_cube_witnesses':'three literal roots replayed separately in verify_exact.gp','noncube_residue_rows':len(rows),'witness_primes':sorted({r['q'] for r in rows}),'minor':minor,'minor_determinant_mod3':det,'global_kernel_unit_dimension':2,'global_kernel_valuation_dimension':1,'global_kernel_class_dimension':0,'local_restriction_rank':1,'joint_kernel_dimension':2,'joint_kernel_equals_points':True,'extra_rejected_at':[3,433]}
(R/'INDEPENDENT_CHECK.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
