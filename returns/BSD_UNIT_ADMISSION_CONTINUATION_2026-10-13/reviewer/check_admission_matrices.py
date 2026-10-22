#!/usr/bin/env python3
"""Independent exact F3 replay of source/local admission matrices."""
import hashlib,itertools,json,pathlib
P=3
def rr(rows,n):
 a=[[x%3 for x in row] for row in rows];j=0;piv=[]
 if any(len(row)!=n for row in a):raise ValueError('width')
 for col in range(n):
  z=next((k for k in range(j,len(a)) if a[k][col]),None)
  if z is None:continue
  a[j],a[z]=a[z],a[j];s=pow(a[j][col],-1,3);a[j]=[x*s%3 for x in a[j]]
  for k in range(len(a)):
   if k!=j and a[k][col]:s=a[k][col];a[k]=[(x-s*y)%3 for x,y in zip(a[k],a[j])]
  piv.append(col);j+=1
  if j==len(a):break
 return a[:j],piv
def rank(a,n):return len(rr(a,n)[1])
def ns(a,n):
 a,piv=rr(a,n);b=[]
 for j in range(n):
  if j in piv:continue
  v=[0]*n;v[j]=1
  for row,k in zip(a,piv):v[k]=-row[j]%3
  b.append(v)
 return b
def tr(a):return list(map(list,zip(*a))) if a else []
def mul(a,b):
 if not a:return []
 if not b:return [[] for _ in a]
 return [[sum(x*y for x,y in zip(row,col))%3 for col in zip(*b)] for row in a]
def add(a,b):return [[(x+y)%3 for x,y in zip(r,s)] for r,s in zip(a,b)]
def zer(a):return not any(any(x%3 for x in row) for row in a)
def same_row(a,b,n):return rank(a,n)==rank(b,n)==rank(a+b,n)
def span_dim(a):return rank(tr(a),len(a))

root=pathlib.Path(__file__).resolve().parents[1];source=root/'data/MATRICES.json';d=json.loads(source.read_text())
n=d['source_dimension'];assert n==15 and d['field']==3
V=d['valuation_rows'];T=d['tau_matrix'];A=d['additivity_rows'];L=d['local_rows']
I=[[int(i==j) for j in range(n)] for i in range(n)];N=add(T,I)
assert mul(T,T)==I
F=d['residue_injectivity_matrix'];assert rank(F,n)==15
X=d['actual_coordinates'];assert span_dim(X)==4
assert all(zer(mul(C,X)) for C in [V,N,A,L])

# Reconstruct each local constraint from the local image, including dimension0.
imgs=dict(d['local_image_basis_rows']);evs=dict(d['local_source_evaluation_rows']);given=dict(d['local_block_rows'])
rebuilt=[];oldskip=[];blocks=[]
for ell,B in imgs.items():
 E=evs[ell];q=len(E)
 if not B:B=[[] for _ in range(q)]
 assert len(B)==q
 ann=ns(tr(B),q)
 C=mul(ann,E)
 assert same_row(C,given[ell],n)
 assert zer(mul(ann,B))
 rebuilt+=C
 if B and B[0]:oldskip+=C
 blocks.append({'prime':ell,'local_target_dimension':q,'point_image_dimension':span_dim(B),
                'annihilator_dimension':len(ann),'source_constraint_rank':rank(C,n),
                'producer_block_rowspace_matches':True})
assert same_row(L,rebuilt,n)

spaces={'full':I,'unramified':d['unramified_basis_rows'],'units':d['unit_basis_rows']}
maps={'V':V,'N':N,'A':A,'L':L};dims={}
for name,B in spaces.items():
 k=span_dim(B);assert k==len(B[0]);result={}
 for mask in range(16):
  names=[name for i,name in enumerate(maps) if mask>>i&1]
  C=sum([maps[name] for name in names],[])
  result['+'.join(names) or 'none']=k-rank(mul(C,B),k)
 dims[name]=result
assert dims['full']['N']==dims['full']['L']==4
assert same_row(N,L,n)
assert dims['units']['N']==dims['units']['L']==2
assert dims['units']['N+A+L']==2

U=d['unit_basis_rows'];NU=d['norm_unit_basis_rows'];KU=d['known_unit_basis_rows']
assert span_dim(U)==4 and span_dim(NU)==span_dim(KU)==2
assert zer(mul(N,NU)) and zer(mul(A,NU)) and zer(mul(L,NU))
assert rank(tr(NU)+tr(KU),n)==2
CL=d['class_lifts_rows'];UR=d['repair_unit_basis_rows'];RC=d['repair_coordinates']
repaired=add(CL,mul(UR,RC));assert zer(mul(N+A+L,repaired))
couplings={}
for name,C in [('norm',N),('norm_additivity',N+A),('norm_additivity_local',N+A+L)]:
 CU=mul(C,U);CQ=mul(C,CL)
 couplings[name]=rank(tr(CU)+tr(CQ),len(C))-rank(tr(CU),len(C))
assert all(v==0 for v in couplings.values())
assert span_dim(mul(d['class_rows_on_unramified_basis'], [[int(i==j) for j in range(6)] for i in range(6)]))==2
out={'status':'PASS','source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
     'local_block_reconstruction':blocks,'dimensions':dims,
     'reproduced_old_zero_target_skip_dimension':n-rank(oldskip,n),
     'corrected_all_local_dimension':n-rank(rebuilt,n),
     'norm_kernel_equals_local_kernel':True,'known_units_span_admitted_unit_component':True,
     'class_lift_repairs_cancel_norm_additivity_and_local_rows':True,'coupling_quotient_ranks':couplings,
     'scope':'Exact matrix replay. Cached source completeness and numerical local evaluation provenance retain producer grades; this does not prove a new Selmer upper bound.'}
(pathlib.Path(__file__).with_name('ADMISSION_MATRIX_CHECK.json')).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
