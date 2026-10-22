#!/usr/bin/env python3
"""Complete-source filtered bounds, recomputed without saved coupling outputs."""
from pathlib import Path
from itertools import product
import json,hashlib
ROOT=Path(__file__).resolve().parent;P=3

def tr(a):return list(map(list,zip(*a)))
def echelon(a,n):
 a=[[v%P for v in row] for row in a];piv=[]
 for c in range(n):
  r=next((r for r in range(len(piv),len(a)) if a[r][c]),None)
  if r is None:continue
  j=len(piv);a[j],a[r]=a[r],a[j];f=pow(a[j][c],-1,P);a[j]=[f*v%P for v in a[j]]
  for k in range(len(a)):
   if k==j:continue
   f=a[k][c];a[k]=[(v-f*w)%P for v,w in zip(a[k],a[j])]
  piv.append(c)
 return a,piv

def rank(a,n=None):return len(echelon(a,n if n is not None else (len(a[0]) if a else 0))[1])
def null(a,n):
 rr,ps=echelon(a,n);cols=[]
 for c in range(n):
  if c in ps:continue
  v=[0]*n;v[c]=1
  for i,p in enumerate(ps):v[p]=-rr[i][c]%P
  cols.append(v)
 return tr(cols) if cols else [[] for i in range(n)]
def mm(a,b):return [[sum(v*w for v,w in zip(row,col))%P for col in zip(*b)] for row in a]
def cat(a,b):return [x+y for x,y in zip(a,b)]
def solve(a,b):
 n=len(a[0]);ab=[r+v for r,v in zip(a,b)];red,ps=echelon(ab,n)
 assert len(ps)==n
 assert all(not any(r[:n]) and not any(r[n:]) for r in red[n:])
 ans=[r[n:] for r in red[:n]];assert mm(a,ans)==b
 return ans

def dimcols(a):return len(a[0]) if a else 0
def zero(a):return not any(v for row in a for v in row)
def intersection_dim(a,b):return rank(a)+rank(b)-rank(cat(a,b))
def adapt(d):
 if 'field' not in d:return d
 n=d['source_dimension'];tau=d['tau_matrix'];return {'source_dimension':n,'valuation':d['valuation_rows'],'valuation_zero_basis':d['unramified_basis_rows'],'units':d['unit_basis_rows'],'scalar':[[(tau[i][j]+(i==j))%3 for j in range(n)] for i in range(n)],'additivity':d['additivity_rows'],'local':d['local_rows'],'points':[row[:2] for row in d['actual_coordinates']],'class_boundary_H0':d['class_rows_on_unramified_basis']}

def inspect(path):
 d=adapt(json.loads(path.read_text()));n=d['source_dimension'];V=d['valuation'];H=d['valuation_zero_basis'];U=d['units'];S=d['scalar'];A=d['additivity'];L=d['local'];C=d['class_boundary_H0'];W=d['points'] or [[] for _ in range(n)]
 h=dimcols(H);u=dimcols(U);c=rank(C)
 assert rank(H)==h==n-rank(V) and zero(mm(V,H));assert rank(U)==u and zero(mm(V,U))
 cu=solve(H,U);assert zero(mm(C,cu)) and h-c==u
 # Scalar source, with exact inherited unit/class filtration.
 HS=mm(H,null(mm(S,H),h));US=mm(U,null(mm(S,U),u));hs=dimcols(HS);us=dimcols(US)
 CHS=mm(C,solve(H,HS));cs=rank(CHS);assert hs==us+cs
 CG=mm(C,solve(H,mm(H,null(mm(S+A,H),h))));CL=mm(C,solve(H,mm(H,null(mm(L,H),h))))
 R=S+A+L;RH=mm(R,H);RU=mm(R,U);RSU=mm(A+L,US)
 full=n-rank(R);hkeep=h-rank(RH);ukeep=u-rank(RU);ckeep=hkeep-ukeep;dkeep=full-hkeep
 assert 0<=ckeep<=c and dkeep>=0 and ukeep==us-rank(RSU)
 marginal_intersection=intersection_dim(CG,CL);compatibility_rank=marginal_intersection-ckeep
 assert compatibility_rank>=0
 # Faithful-character class defect rank after quotient by all legitimate unit images.
 joint_class_defect=cs-ckeep
 assert full==us-rank(RSU)+cs-joint_class_defect+dkeep
 # Independent enumeration of every unramified source element after row reduction.
 rows,ps=echelon(RH,h);rows=rows[:len(ps)];srows,sps=echelon(mm(S,H),h);srows=srows[:len(sps)]
 enum=[];scalar_enum=[]
 for x in product(range(P),repeat=h):
  if all(sum(a*b for a,b in zip(row,x))%P==0 for row in srows):scalar_enum.append(x)
  if all(sum(a*b for a,b in zip(row,x))%P==0 for row in rows):enum.append(x)
 assert len(enum)==P**hkeep and len(scalar_enum)==P**hs
 classes={tuple(sum(a*b for a,b in zip(row,x))%P for row in C) for x in enum}
 assert len(classes)==P**ckeep
 # Read the known point subspace only after the upper bound is calculated.
 assert zero(mm(R,W)) and zero(mm(V,W));w=rank(W);WC=mm(C,solve(H,W));wc=rank(WC);wu=w-wc
 assert ukeep>=wu and ckeep>=wc
 # The separate global containing source bound is for comparison, not claimed equality to exact incidence kernel.
 gfull=n-rank(S+A);gh=h-rank(mm(S+A,H));gu=u-rank(mm(S+A,U));gc=gh-gu;gd=gfull-gh
 return {'label':path.stem,'input_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'source_dimension':n,'raw_ordinary_unit_dimension':u,'raw_ordinary_class_dimension':c,'faithful_unit_dimension':us,'faithful_class_dimension':cs,'global_necessary_screen':{'units':gu,'classes':gc,'valuation_layer':gd,'full_upper':gfull},'joint':{'unit_rejection_rank_on_faithful_units':rank(RSU),'admitted_units':ukeep,'class_defect_rank_after_unit_repairs':joint_class_defect,'admitted_classes':ckeep,'admitted_valuation_layer':dkeep,'whole_source_upper':full},'compatible_repair':{'separately_repairable_class_intersection':marginal_intersection,'compatibility_rank':compatibility_rank},'point_comparison_after_upper':{'rank':w,'units':wu,'classes':wc,'unit_excess_upper':ukeep-wu,'class_excess_upper':ckeep-wc,'valuation_excess_upper':dkeep,'total_excess_upper':full-w},'all_unramified_elements_enumerated':P**h,'retained_source_grade':'GRH-dependent complete class presentation' if path.stem=='seed3' else 'certified complete class/unit source; retained arithmetic replay'}

out={'status':'PASS','arithmetic_is_new':False,'purpose':'Reapply unchanged complete-source data to the combined unit/class/valuation upper bound','cases':[inspect(p) for p in sorted((ROOT/'inputs').glob('*.json'))]}
(ROOT/'FILTERED_BOUNDS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
