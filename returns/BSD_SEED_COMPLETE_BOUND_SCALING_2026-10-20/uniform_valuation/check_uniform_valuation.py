"""Exact bounded finite-group checks of the multiplicative primitive divisor map.

The matrices are constructed from D-orbits of actual nonzero vectors and dual
vectors, then incidence is counted by enumerating lambda(x)=1. No predicted
matrix entry or predicted kernel dimension is used in the construction.
"""
from pathlib import Path
import json,time,hashlib
from collections import Counter
R=Path(__file__).resolve().parent

def prime(p):
 return p>=2 and all(p%d for d in range(2,int(p**.5)+1))
def primitive(p):
 return next(g for g in range(2,p) if len({pow(g,k,p) for k in range(p-1)})==p-1)
def rank(a,p):
 if not a:return 0
 a=[[v%p for v in row] for row in a];r=0
 for j in range(len(a[0])):
  k=next((k for k in range(r,len(a)) if a[k][j]),None)
  if k is None:continue
  a[r],a[k]=a[k],a[r];z=pow(a[r][j],-1,p);a[r]=[z*x%p for x in a[r]]
  for k in range(r+1,len(a)):
   if a[k][j]:
    z=a[k][j];a[k]=[(x-z*y)%p for x,y in zip(a[k],a[r])]
  r+=1
  if r==len(a):break
 return r

def make_orbits(p,q,eps,dual):
 # I=(1,1;0,1), F=eps*diag(q,1). Dual action is inverse transpose.
 fi=pow(eps*q%p,-1,p)
 def acts(v):
  x,y=v
  if dual:return ((x,(y-x)%p),(fi*x%p,eps*y%p))
  return (((x+y)%p,y),(eps*q*x%p,eps*y%p))
 reps=[];sizes=[];ram=[];belongs={}
 for x in range(p):
  for y in range(p):
   v=(x,y)
   if v==(0,0) or v in belongs:continue
   idx=len(reps);reps.append(v);queue=[v];belongs[v]=idx
   for a in queue:
    for b in acts(a):
     if b not in belongs:belongs[b]=idx;queue.append(b)
     else:assert belongs[b]==idx
   sizes.append(len(queue))
   # Compute inertia orbit directly, rather than using e=1/p by formula.
   a=v;seen=set()
   while a not in seen:
    seen.add(a);a=acts(a)[0]
   ram.append(len(seen))
 assert len(belongs)==p*p-1
 return reps,sizes,ram,belongs

def scalar_perm(reps,belongs,g,p):
 pm=[belongs[(g*x%p,g*y%p)] for x,y in reps]
 assert sorted(pm)==list(range(len(pm)))
 return pm

def eigenbasis(pm,lam,p):
 seen=set();out=[]
 for i in range(len(pm)):
  if i in seen:continue
  cy=[];j=i
  while j not in seen:seen.add(j);cy.append(j);j=pm[j]
  assert j==i
  if pow(lam,len(cy),p)!=1:continue
  v=[0]*len(pm)
  for k,j in enumerate(cy):v[j]=pow(lam,-k,p)
  pv=[0]*len(pm)
  for j,k in enumerate(pm):pv[k]=v[j]
  assert pv==[lam*x%p for x in v]
  out.append(v)
 return out

def image(M,v,p):
 # Sparse basis cycles avoid a dense cubic operation at p=487.
 nz=[(j,a) for j,a in enumerate(v) if a]
 return [sum(row[j]*a for j,a in nz)%p for row in M]
def image_rank(M,bs,p):
 vals=[image(M,v,p) for v in bs]
 return rank(vals,p)

def one(p,q,eps,tag):
 assert prime(p) and p>=5 and q%p and eps in (-1,1)
 start=time.monotonic();q%=p;g=primitive(p)
 sr,ss,se,sd=make_orbits(p,q,eps,False)
 tr,ts,te,td=make_orbits(p,q,eps,True)
 sp=scalar_perm(sr,sd,g,p);tp=scalar_perm(tr,td,g,p)
 raw=[];weighted=[]
 for i,(a,b) in enumerate(tr):
  # Enumerate exactly p solutions of ax+by=1. None is the zero vector.
  if b:
   bi=pow(b,-1,p);pts=((x,(1-a*x)*bi%p) for x in range(p))
  else:
   ai=pow(a,-1,p);pts=((ai,y) for y in range(p))
  ct=Counter(sd[v] for v in pts)
  row=[ct[j] for j in range(len(sr))]
  assert sum(row)==p
  rr=[]
  for j,n in enumerate(row):
   assert (te[i]*n)%se[j]==0
   rr.append(te[i]*n//se[j])
  raw.append(row);weighted.append(rr)
 # u sigma_source = sigma_target^-1 u, checked entrywise.
 assert all(weighted[i][sp[j]]==weighted[tp[i]][j] for i in range(len(tr)) for j in range(len(sr)))
 character_results=[]
 for lam in (g,pow(g,-1,p)):
  bs=eigenbasis(sp,lam,p);tb=eigenbasis(tp,pow(lam,-1,p),p)
  form=[];off=[]
  for v in bs:
   supp=[j for j,x in enumerate(v) if x]
   if all(sr[j][1]==0 for j in supp):form.append(v)
   else:
    assert all(sr[j][1]!=0 for j in supp);off.append(v)
  for v in bs:
   y=image(weighted,v,p);yp=[0]*len(tp)
   for j,k in enumerate(tp):yp[k]=y[j]
   assert yp==[pow(lam,-1,p)*x%p for x in y]
  nr=image_rank(weighted,bs,p);fr=image_rank(weighted,form,p);orr=image_rank(weighted,off,p)
  cr={'character_value':lam,'target_character_value':pow(lam,-1,p),'source_dimension':len(bs),'target_dimension':len(tb),'formal_dimension':len(form),'off_formal_dimension':len(off),'norm_rank':nr,'kernel_dimension':len(bs)-nr,'formal_image_rank':fr,'off_formal_image_rank':orr,'unweighted_kernel_dimension':len(bs)-image_rank(raw,bs,p),'unweighted_formal_image_rank':image_rank(raw,form,p),'unweighted_off_formal_image_rank':image_rank(raw,off,p)}
  # Assertions compare the measured outcome with the proposed lemma only now.
  assert cr['kernel_dimension']==int(eps*q%p==1)
  assert cr['formal_dimension']==int(eps*q%p==1)
  assert cr['off_formal_dimension']==int(eps==1)
  assert fr==0 and orr==len(off)
  character_results.append(cr)
 matrix_digest=hashlib.sha256(json.dumps(weighted,separators=(',',':')).encode()).hexdigest()
 out={'p':p,'q_mod_p':q,'epsilon':eps,'tags':tag,'primitive_scalar':g,'source_orbits':len(sr),'target_orbits':len(tr),'source_ramification_histogram':dict(Counter(se)),'target_ramification_histogram':dict(Counter(te)),'primitive_matrix_sha256':matrix_digest,'characters':character_results,'seconds':time.monotonic()-start}
 # Small cases retain the entire actual matrix for direct review.
 if p<=7:out.update(source_representatives=sr,target_representatives=tr,source_e=se,target_e=te,primitive_matrix=weighted,unweighted_matrix=raw)
 return out

def main():
 start=time.monotonic();tests={}
 def put(p,q,e,tag):tests.setdefault((p,q%p,e),[]).append(tag)
 for p in (5,7,11,13,17,19,29,59):
  for q in sorted({1,p-1,2,3,3%p,2243%p,5843%p}):
   if not q:continue
   for e in (-1,1):put(p,q,e,'generic residue/sign panel')
  for q,e in ((3,-1),(2243,1),(5843,-1)):
   if q%p:put(p,q,e,f'seed q={q}, epsilon={e}')
 # Direct check of the large exceptional coefficient, not an extrapolation.
 put(487,5843,-1,'seed exceptional q=5843, p=487')
 out=[]
 for (p,q,e),tags in tests.items():
  a=one(p,q,e,tags);out.append(a)
  if p==487:print('P487_EXPLICIT_ORBIT_CHECK_COMPLETE',a['seconds'],flush=True)
 negative=[{'p':t['p'],'q_mod_p':t['q_mod_p'],'epsilon':t['epsilon'],'character_value':c['character_value'],'weighted_kernel':c['kernel_dimension'],'unweighted_kernel':c['unweighted_kernel_dimension'],'weighted_formal_image_rank':c['formal_image_rank'],'unweighted_formal_image_rank':c['unweighted_formal_image_rank'],'weighted_off_formal_image_rank':c['off_formal_image_rank'],'unweighted_off_formal_image_rank':c['unweighted_off_formal_image_rank']} for t in out for c in t['characters'] if c['formal_image_rank']!=c['unweighted_formal_image_rank'] or c['off_formal_image_rank']!=c['unweighted_off_formal_image_rank']]
 assert negative and any(x['weighted_kernel']!=x['unweighted_kernel'] for x in negative)
 result={'status':'EXACT_FINITE_GROUP_LEMMA_CHECKS_PASS','cases':len(out),'character_checks':2*len(out),'elapsed_seconds':time.monotonic()-start,'scope':'Finite group local multiplicative models; not a global class or seed FIN bound. The uniform proof is separate.','predicted_rule_checked_after_actual_matrix_construction':'kernel dimension = 1 iff epsilon*q=1 mod p; off-formal unit channel exists iff epsilon=1','tests':out,'ramification_negative_controls':negative}
 (R/'FINITE_GROUP_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({k:v for k,v in result.items() if k not in ('tests','ramification_negative_controls')},indent=2))
if __name__=='__main__':main()
