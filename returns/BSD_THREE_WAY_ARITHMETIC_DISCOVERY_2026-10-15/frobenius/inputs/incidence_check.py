#!/usr/bin/env python3
"""Independent finite verification; no producer matrices or libraries imported."""
import itertools,json,math
from pathlib import Path
P=3
R=[(1,0),(0,1),(1,1),(1,2)]
def dot(a,b):return sum(x*y for x,y in zip(a,b))%3
def det(a):return (a[0]*a[3]-a[1]*a[2])%3
def mv(a,v):return ((a[0]*v[0]+a[1]*v[1])%3,(a[2]*v[0]+a[3]*v[1])%3)
def inv(a):
 d=pow(det(a),-1,3);return tuple((d*x)%3 for x in (a[3],-a[1],-a[2],a[0]))
def mm(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def tr(a):return list(map(list,zip(*a)))
def rank(A):
 A=[[x%3 for x in r] for r in A];n=len(A);m=len(A[0]) if A else 0;r=0
 for c in range(m):
  j=next((j for j in range(r,n) if A[j][c]),None)
  if j is None:continue
  A[r],A[j]=A[j],A[r];k=pow(A[r][c],-1,3);A[r]=[x*k%3 for x in A[r]]
  for j in range(n):
   if j!=r:
    k=A[j][c];A[j]=[(x-k*y)%3 for x,y in zip(A[j],A[r])]
  r+=1
 return r

def canonical(v):
 for j,r in enumerate(R):
  if tuple(v)==r:return j,1
  if tuple((-x)%3 for x in v)==r:return j,-1
 raise ValueError(v)
def signed_action(mapfn):
 # coefficient row f -> f composed with mapfn
 A=[]
 for v in R:
  j,s=canonical(mapfn(v));row=[0]*4;row[j]=s;A.append(row)
 return A
N=[[0 if dot(l,v)==0 else (1 if dot(l,v)==1 else -1) for v in R] for l in R]
assert N==[[1,0,1,1],[0,1,1,-1],[1,1,-1,0],[1,-1,0,-1]]
assert mm(N,tr(N))==[[3*int(i==j) for j in range(4)] for i in range(4)]
assert rank(N)==2
V=list(itertools.product(range(3),repeat=4))
image={tuple(x%3 for x in r) for v in V for r in [mm(N,[[x] for x in v])] } if False else {tuple(sum(N[i][j]*v[j] for j in range(4))%3 for i in range(4)) for v in V}
kernel={v for v in V if all(sum(N[i][j]*v[j] for j in range(4))%3==0 for i in range(4))}
linear={tuple(dot(a,v) for v in R) for a in itertools.product(range(3),repeat=2)}
assert kernel==linear
G=[a for a in itertools.product(range(3),repeat=4) if det(a)]
assert len(G)==48
line_actions=[];point_actions=[]
for a in G:
 # f' (v) = f(a v): norm f' at l = norm f at l a^-1
 A=signed_action(lambda v:mv(a,v));ai=inv(a)
 B=signed_action(lambda l:((l[0]*ai[0]+l[1]*ai[2])%3,(l[0]*ai[1]+l[1]*ai[3])%3))
 assert [[x%3 for x in row] for row in mm(N,A)]==[[x%3 for x in row] for row in mm(B,N)]
 line_actions.append(B);point_actions.append(A)
projective=set()
for v in image-{(0,0,0,0)}:
 k=next(x for x in v if x);projective.add(tuple(x*pow(k,-1,3)%3 for x in v))
assert len(projective)==4
invariant=[]
for v in sorted(projective):
 line={tuple(c*x%3 for x in v) for c in range(3)}
 if all(tuple(sum(A[i][j]*v[j] for j in range(4))%3 for i in range(4)) in line for A in line_actions):invariant.append(v)
assert not invariant
row_invariant=[]
for v in sorted(projective):
 line={tuple(c*x%3 for x in v) for c in range(3)}
 for A in point_actions:
  rv=tuple(sum(v[i]*A[i][j] for i in range(4))%3 for j in range(4))
  assert rv in image
 if all(tuple(sum(v[i]*A[i][j] for i in range(4))%3 for j in range(4)) in line for A in point_actions):row_invariant.append(v)
assert not row_invariant
# Smith invariant factors via gcd of all minors, integer Bareiss not a CAS.
def determinant(A):
 if not A:return 1
 return sum((-1)**j*A[0][j]*determinant([r[:j]+r[j+1:] for r in A[1:]]) for j in range(len(A)))
divs=[1]
for k in range(1,5):
 minors=[determinant([[N[i][j] for j in J] for i in I]) for I in itertools.combinations(range(4),k) for J in itertools.combinations(range(4),k)]
 divs.append(math.gcd(*minors))
smith=[divs[i+1]//divs[i] for i in range(4)]
assert smith==[1,1,3,3]
out={'status':'EXACT_ALGEBRA_VERIFIED','point_representatives':R,'incidence_matrix':N,'integer_smith':smith,'mod3_rank':rank(N),'kernel_is_additive_linear_functions':True,'group_elements_checked':len(G),'image_order':len(image),'invariant_projective_lines':invariant,'row_span_invariant_projective_lines':row_invariant,'scope':'Finite algebra only. Actual Kummer specialization, noncube witness and Chebotarev hypotheses require the written arithmetic argument.'}
p=Path(__file__).with_name('RESULT.json');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,sort_keys=True))
