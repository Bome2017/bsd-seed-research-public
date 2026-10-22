#!/usr/bin/env python3
"""Independent F3 reconstruction of actual unit/class repair matrices."""
import json,sys,hashlib
from pathlib import Path

def tr(a): return [list(c) for c in zip(*a)]
def rr(a,n):
 a=[[x%3 for x in row] for row in a]; piv=[]
 for j in range(n):
  k=next((k for k in range(len(piv),len(a)) if a[k][j]),None)
  if k is None:continue
  i=len(piv);a[i],a[k]=a[k],a[i];v=pow(a[i][j],-1,3);a[i]=[x*v%3 for x in a[i]]
  for k in range(len(a)):
   if k!=i:
    v=a[k][j];a[k]=[(x-v*y)%3 for x,y in zip(a[k],a[i])]
  piv.append(j)
 return a,piv
def rank(a,n=None):return len(rr(a,n if n is not None else len(a[0]) if a else 0)[1])
def ker(a,n):
 a,piv=rr(a,n);cols=[]
 for j in range(n):
  if j in piv:continue
  v=[0]*n;v[j]=1
  for i,k in enumerate(piv):v[k]=-a[i][j]%3
  cols.append(v)
 return tr(cols) if cols else [[]for _ in range(n)]
def mul(a,b):return [[sum(x*y for x,y in zip(row,col))%3 for col in zip(*b)]for row in a]
def cat(a,b):return [x+y for x,y in zip(a,b)]
def zero(a):return all(x==0 for row in a for x in row)
def solve(a,b,n):
 ab,piv=rr([row+[c%3]for row,c in zip(a,b)],n)
 if any(not any(row[:n]) and row[n]for row in ab):raise ValueError('inconsistent')
 x=[0]*n
 for i,j in enumerate(piv):x[j]=ab[i][n]
 assert [r[0]for r in mul(a,[[t]for t in x])]==[t%3 for t in b]
 return x

def inspect(path):
 d=json.loads(path.read_text());n=d['source_dimension'];V,U,S,A,L,W,H,C=[d[k]for k in ('valuation','units','scalar','additivity','local','points','valuation_zero_basis','class_lifts')]
 W=W or [[] for _ in range(n)]; pd=rank(W); u=len(U[0]);c=len(C[0]);h=len(H[0]);cb=d['class_boundary_H0']
 assert rank(H)==h==n-rank(V) and zero(mul(V,H))
 assert rank(U)==u and zero(mul(V,U)) and zero(mul(V,C))
 assert rank(cat(U,C))==h==u+c and rank(cb)==c
 coordsU=tr([solve(H,v,h) for v in tr(U)])
 assert zero(mul(cb,coordsU)) and h-rank(cb)==u
 coordsW=tr([solve(H,v,h) for v in tr(W)])
 points_class=mul(cb,coordsW)
 out=[]
 for label,D in [('scalar',S),('scalar_additivity',S+A),('local',L),('joint',S+A+L)]:
  DU,DC=mul(D,U),mul(D,C);m=len(D)
  Z=tr(ker(tr(DU),m));assert zero(mul(Z,DU)) and m-rank(Z)==rank(DU)
  K=mul(Z,DC);nu=u-rank(DU);nc=c-rank(K)
  assert h-rank(mul(D,H))==nu+nc
  repairs=[]
  for cc in tr(ker(K,c)):
   v=[x[0]for x in mul(DC,[[x]for x in cc])];uc=solve(DU,[-x for x in v],u)
   bv=[x[0]for x in mul(C,[[x]for x in cc])];uv=[x[0]for x in mul(U,[[x]for x in uc])];fixed=[(x+y)%3 for x,y in zip(bv,uv)]
   assert zero(mul(D,[[x]for x in fixed]))
   try:point_coordinates=solve(W,fixed,len(W[0]))
   except ValueError:point_coordinates=None
   repairs.append({'class_coordinates':cc,'unit_correction':uc,'source_exponents':fixed,'point_coordinates':point_coordinates})
  rejects=[]
  for j in range(c):
   i=next((i for i,row in enumerate(K)if row[j]),None)
   if i is None:continue
   factor=pow(K[i][j],-1,3);lam=[factor*x%3 for x in Z[i]]
   beta=[row[j]for row in C]
   assert zero(mul([lam],DU)) and mul([lam],[[r[j]]for r in DC])==[[1]]
   rejects.append({'class_basis_column':j,'source_exponents':beta,'annihilator_row':lam,'value':1})
  out.append({'block':label,'unit_admitted_dimension':nu,'class_defect_rank':rank(K),'class_admitted_dimension':nc,'kernel_on_H0_dimension':nu+nc,'repairs':repairs,'unrepairable_lift_certificates':rejects})
 assert zero(mul(S+A+L,W))
 return {'curve':path.parent.name,'input_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'source_dimension':n,'valuation_zero_dimension':h,'unit_dimension':u,'ordinary_class3_dimension':c,'point_class_coordinates':points_class,'point_dimension':pd,'point_unit_intersection':pd-rank(points_class),'full_joint_kernel_dimension':n-rank(S+A+L),'blocks':out}

if __name__=='__main__':
 paths=[Path(p) for p in sys.argv[1:]]
 assert paths,'supply actual matrices.json path(s)'
 print(json.dumps({'status':'INDEPENDENT_CLASS_COUPLING_CHECK_PASS','scope':'Independent elimination of exported actual matrices, not producer/source theorem certification.','cases':[inspect(p)for p in paths]},indent=2))
