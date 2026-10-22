from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent
F,XP,YP,SIG,UNITS=json.loads((R/'small_conductor7/eval_data.json').read_text())
SPLITS=json.loads((R/'local_rank/11a1_split_primes.json').read_text())
LOCAL=json.loads((R/'local_rank/11a1_formal_8.json').read_text())
LOCAL9=json.loads((R/'local_rank/11a1_formal_9.json').read_text())

def rank(A,p=7):
 B={}
 for a in A:
  a=[x%p for x in a]
  for j,b in sorted(B.items()):
   v=a[j]
   if v:a=[(x-v*y)%p for x,y in zip(a,b)]
  j=next((i for i,x in enumerate(a) if x),None)
  if j is not None:B[j]=[x*pow(a[j],-1,p)%p for x in a]
 return len(B)
def pivcols(A):
 selected=[];r=0
 for j in range(len(A[0])):
  tmp=[[row[k] for k in selected+[j]] for row in A]
  t=rank(tmp)
  if t>r:selected.append(j);r=t
 return selected

def ev(pack,x,q):
 v=0
 for c in reversed(pack[0]):v=(v*x+c)%q
 return v*pow(pack[1],-1,q)%q

def add(P,Q,q):
 if P is None:return Q
 if Q is None:return P
 x,y=P;u,v=Q
 if x==u and (y+v+1)%q==0:return None
 m=((3*x*x-2*x-10)*pow(2*y+1,-1,q) if P==Q else (v-y)*pow(u-x,-1,q))%q
 xx=(m*m+1-x-u)%q
 return (xx,(-y+m*(x-xx)-1)%q)
def mul(P,n,q):
 a=None
 for _ in range(n):a=add(a,P,q)
 return a

outs=[];weights=[6,2,3,1,5,4];allnorm=[]
for q,roots in SPLITS:
 assert all(q%d for d in range(2,int(q**.5)+1))
 assert len(roots)==48 and len(set(roots))==48
 assert all(ev([F,1],x,q)==0 for x in roots)
 pts=[(ev(XP,x,q),ev(YP,x,q)) for x in roots]
 assert len(set(pts))==48
 assert all((y*y+y-x**3+x*x+10*x+20)%q==0 and mul((x,y),7,q) is None for x,y in pts)
 sigma=[roots.index(ev(SIG,x,q)) for x in roots]
 assert all(pts[sigma[i]]==mul(pts[i],3,q) for i in range(48))
 P=pts[-1];line={mul(P,i,q) for i in range(7)};Q=next(t for t in reversed(pts) if t not in line)
 labels={add(mul(P,a,q),mul(Q,b,q),q):(a,b) for a in range(7) for b in range(7)}
 assert len(labels)==49
 cache={}
 def factorvalue(a,x):
  key=(tuple(a[0]),a[1],x)
  if key not in cache:cache[key]=ev(a,x,q)
  return cache[key]
 vals=[]
 for unit in UNITS:
  v=[]
  for x in roots:
   z=1
   for a,e in unit:
    av=factorvalue(a,x);assert av
    z=z*pow(av,e%(q-1),q)%q
   v.append(z)
  vals.append(v)
 z=next(pow(a,(q-1)//7,q) for a in range(2,q) if pow(a,(q-1)//7,q)!=1)
 lg={pow(z,i,q):i for i in range(7)}
 pro=[]
 for row in vals:
  output=[]
  for i in range(48):
   a=1;j=i
   for w in weights:a=a*pow(row[j],w,q)%q;j=sigma[j]
   output.append(lg[pow(a,(q-1)//7,q)])
  pro.append(output)
 assert all(all(row[sigma[i]]==3*row[i]%7 for i in range(48)) for row in pro)
 nr=[];tags=[]
 for a,b in [(1,t) for t in range(7)]+[(0,1)]:
  inds=[i for i,t in enumerate(pts) if (a*labels[t][0]+b*labels[t][1])%7==1]
  assert len(inds)==7
  nr.append([sum(row[i] for i in inds)%7 for row in pro]);tags.append([a,b])
 allnorm+=nr
 # Local coordinates come from separately authenticated exact PARI quotient.
 loc=LOCAL[6];loc9=LOCAL9[6]
 assert len(loc[0])==len(UNITS)
 selected=[];tagselected=[]
 for tag,row in list(zip([['norm',a,b] for a,b in tags],nr))+list(zip([['local8',i] for i in range(len(loc))],loc)):
  if rank(selected+[row])>len(selected):selected.append(row);tagselected.append(tag)
 cols=pivcols(selected);minor=[[row[c] for c in cols] for row in selected]
 assert rank(pro)==4 and rank(nr)==3 and rank(loc)==1 and rank(nr+loc)==4 and rank(nr+loc9)==4
 outs.append({'q':q,'mu7_generator':z,'unit_residue_rank':rank(pro),'affine_norm_rank':rank(nr),'formal_rank':rank(loc),'joint_rank_at_P8':rank(nr+loc),'joint_rank_at_P9':rank(nr+loc9),'independent_row_tags':tagselected,'minor_columns_zero_based':cols,'four_by_four_minor':minor,'minor_rank':rank(minor),'norm_rows':nr})
res={'status':'PASS_ACTUAL_UNIT_JOINT_UPPER_ZERO','coefficient':7,'curve':'11a1','ordinary_chi_unit_dimension':4,'authenticated_compact_units':26,'method':'independent multiplicative evaluation, fresh torsion basis, affine-line sums; local rows retained from exact P8/P9 producer','cases':outs,'class_condition':'No complete ordinary class bound is certified. This is an unconditional complete UNIT bound under retained representation/source inputs.','new_seed_result':False}
(R/'INDEPENDENT_11A1_JOINT.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps({k:v for k,v in res.items() if k!='cases'},indent=2))
