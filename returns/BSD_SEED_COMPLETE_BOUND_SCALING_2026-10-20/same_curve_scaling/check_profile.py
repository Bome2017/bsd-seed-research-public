"""Checks exact residual matrices, archimedean character dimension and prime support."""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent

def rank(a,p=5):
 a=[[v%p for v in row] for row in a];r=0
 for j in range(len(a[0]) if a else 0):
  k=next((k for k in range(r,len(a)) if a[k][j]),None)
  if k is None:continue
  a[r],a[k]=a[k],a[r];u=pow(a[r][j],-1,p);a[r]=[u*x%p for x in a[r]]
  for k in range(len(a)):
   if k!=r:
    u=a[k][j];a[k]=[(x-u*y)%p for x,y in zip(a[k],a[r])]
  r+=1
 return r

def eigdim(pm,ch):
 n=len(pm)
 return n-rank([[int(pm[j]==i)-ch*int(i==j) for j in range(n)] for i in range(n)])

V={(x,y) for x in range(5) for y in range(5)}-{(0,0)}
arch=sorted({tuple(sorted({(x,y),(x,-y%5)})) for x,y in V})
pm=[arch.index(tuple(sorted({(2*x%5,2*y%5) for x,y in o}))) for o in arch]
assert len(arch)==14 and sum(len(o)==1 for o in arch)==4
assert eigdim(pm,2)==eigdim(pm,3)==3
primechecks=[]
for q,ef,pm,c2,c3 in json.loads((R/'divisor_profile.json').read_text()):
 assert sum(e*f for e,f in ef)==24
 pm=[a-1 for a in pm]
 assert sorted(pm)==list(range(len(pm)))
 assert eigdim(pm,2)==c2==0 and eigdim(pm,3)==c3==0
 primechecks.append({'prime':q,'ef':ef,'faithful_valuation_dimension':0})
a=json.loads((R/'NORM_UPPER.json').read_text())
vr=[];nr=[]
for case in a['rows']:
 if 'excluded_reason' in case:continue
 p=case['projected_residue_rows'];n=case['norm_rows']
 assert n==[[sum(p[i][j] for i in c)%5 for j in range(13)] for c in case['affine_cosets']]
 vr+=p;nr+=n
 assert rank(vr)==case['cumulative_projected_rank'];assert rank(nr)==case['cumulative_norm_rank']
assert rank(vr)==3 and rank(nr)==1
accepted=json.loads((R/'authenticate_units.gp.receipt.json').read_text())['accepted']
assert accepted
cert=json.loads((R/'class_quotient.gp.receipt.json').read_text())
assert cert['accepted'] is False
res={'curve':'1664n1','coefficient_prime':5,'faithful_unit_dimension':3,'certified_norm_rank_lower':1,'full_faithful_unit_kernel_upper':2,'faithful_valuation_allowance':0,'ordinary_class5_contribution':'UNRESOLVED: provisional BNF=C3; quotient certification alarm after110sec','rigorous_full_source_upper':'2 + dim_F5 Cl(A)[5]^chi','conditional_on_class5_absence_upper':2,'class_absence_certified':False,'prime_checks':primechecks,'status':'UNIT_AND_VALUATION_PROFILE_CERTIFIED_CLASS_TERM_UNRESOLVED'}
(R/'RESULT.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
