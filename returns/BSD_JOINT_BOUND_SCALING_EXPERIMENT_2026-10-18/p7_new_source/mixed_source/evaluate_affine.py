"""Exact scalar-character and incidence evaluation of authenticated compact units."""
from pathlib import Path
from functools import lru_cache
import json,time,hashlib
R=Path(__file__).resolve().parent
F,XP,YP,SIG,bases,K=json.loads((R/'compact_units_eval.json').read_text())
splits=json.loads((R/'../../local_rank/split_primes.json').read_text())
p=7;n=48;nu=len(K[0]);coeff=[6,2,3,1,5,4]
def pack(a):return tuple(a[0]),a[1]
XP,YP,SIG=map(pack,[XP,YP,SIG]);bases=list(map(pack,bases))
def rank(A):
 a=[[x%p for x in r] for r in A]; i=0
 if not a:return 0
 for j in range(len(a[0])):
  k=next((k for k in range(i,len(a)) if a[k][j]),None)
  if k is None:continue
  a[i],a[k]=a[k],a[i];t=pow(a[i][j],-1,p);a[i]=[x*t%p for x in a[i]]
  for k in range(len(a)):
   if k!=i:
    t=a[k][j];a[k]=[(x-t*y)%p for x,y in zip(a[k],a[i])]
  i+=1
  if i==len(a):break
 return i
def add(P,Q,q):
 if P is None:return Q
 if Q is None:return P
 x,y=P;u,v=Q
 if x==u and (y+v+1)%q==0:return None
 if P==Q:m=(3*x*x+2*x-2)*pow(2*y+1,-1,q)%q
 else:m=(v-y)*pow(u-x,-1,q)%q
 z=(m*m-1-x-u)%q
 return z,(-y+m*(x-z)-1)%q
def mul(P,k,q):
 z=None
 for _ in range(k):z=add(z,P,q)
 return z
allU=[];allN=[];out=[];start=time.monotonic()
for q,roots in splits:
 assert q%p==1 and len(set(roots))==n
 assert all(sum(c*pow(r,i,q) for i,c in enumerate(F))%q==0 for r in roots)
 @lru_cache(None)
 def ev(a,r):
  cs,d=a
  if d%q==0:raise ZeroDivisionError('denominator')
  z=0
  for c in reversed(cs):z=(z*r+c)%q
  return z*pow(d,-1,q)%q
 try:
  pts=[(ev(XP,r),ev(YP,r)) for r in roots];idx={P:i for i,P in enumerate(pts)}
  assert len(idx)==n
  assert all((y*y+y-x*x*x-x*x+2*x)%q==0 and mul((x,y),p,q) is None for x,y in pts)
  pm=[roots.index(ev(SIG,r)) for r in roots]
  assert all(pts[pm[i]]==mul(pts[i],3,q) for i in range(n))
  orb=[]
  for i in range(n):
   row=[i]
   for _ in range(5):row.append(pm[row[-1]])
   assert pm[row[-1]]==i and len(set(row))==6
   orb.append(row)
  z=next(pow(a,(q-1)//p,q) for a in range(2,q) if pow(a,(q-1)//p,q)!=1)
  dl={pow(z,k,q):k for k in range(p)}
  bl=[]
  for r in roots:
   row=[]
   for b in bases:
    v=ev(b,r)
    if not v:raise ZeroDivisionError('base factor')
    row.append(dl[pow(v,(q-1)//p,q)])
   bl.append(row)
  logs=[]
  for i in range(n):
   fl=[bl[orb[i][j]][k] for k in range(len(bases)) for j in range(6)]
   logs.append([sum(fl[k]*K[k][h] for k in range(len(K)))%p for h in range(nu)])
  U=[[sum(c*logs[o][h] for c,o in zip(coeff,orb[i]))%p for h in range(nu)] for i in range(n)]
  assert all(U[pm[i]]==[3*x%p for x in U[i]] for i in range(n))
  lines=set()
  for T in pts:
   line={mul(T,j,q) for j in range(p)}
   for P in pts:
    if P not in line:lines.add(tuple(sorted(idx[add(P,mul(T,j,q),q)] for j in range(p))))
  assert len(lines)==n
  lines=sorted(lines)
  N=[[sum(U[i][h] for i in L)%p for h in range(nu)] for L in lines]
  allU+=U;allN+=N
  out.append(dict(q=q,mu7=z,points=pts,scalar_permutation=pm,projected_rows=U,affine_cosets=lines,norm_rows=N,unit_rank=rank(U),norm_rank=rank(N),cumulative_unit_rank=rank(allU),cumulative_norm_rank=rank(allN)))
 except ZeroDivisionError as e:out.append(dict(q=q,excluded=str(e)))
result=dict(curve='389a1',p=7,arithmetic_base_elements=len(bases),scalar_orbit_factors=len(K),authenticated_compact_relations=nu,projector=coeff,unit_image_rank=rank(allU),norm_image_rank=rank(allN),ambient_unit_dimension=4,unit_kernel_upper=4-rank(allN),rows=out,elapsed_seconds=time.monotonic()-start,scope='Unitness follows from full integer divisor relations; no fundamental-unit or class completeness is claimed.')
assert result['unit_image_rank']<=4 and result['norm_image_rank']<=result['unit_image_rank']
(R/'AFFINE_RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
