from pathlib import Path
import json,itertools,hashlib,ast
R=Path(__file__).resolve().parent
CASES=['1913b1','389a1','433a1','seed3','28042a1']
def rr(A,n):
 B=[[int(x)%3 for x in row]for row in A];assert all(len(row)==n for row in B);p=[]
 for c in range(n):
  j=next((j for j in range(len(p),len(B))if B[j][c]),None)
  if j is None:continue
  i=len(p);B[i],B[j]=B[j],B[i];u=pow(B[i][c],-1,3);B[i]=[u*x%3 for x in B[i]]
  for j in range(len(B)):
   if j!=i and B[j][c]:
    u=B[j][c];B[j]=[(a-u*b)%3 for a,b in zip(B[j],B[i])]
  p.append(c)
 return B[:len(p)],p
def span(A,n):return rr(A,n)[0]
def rank(A,n):return len(span(A,n))
def ker(A,n):
 B,P=rr(A,n);out=[]
 for j in range(n):
  if j in P:continue
  v=[0]*n;v[j]=1
  for row,k in zip(B,P):v[k]=-row[j]%3
  out.append(v)
 return out
def tr(A):return [list(x)for x in zip(*A)]if A else[]
def mul(A,B):return [[sum(x*y for x,y in zip(a,b))%3 for b in tr(B)]for a in A]
def ev(A,v):return tuple(sum(a*b for a,b in zip(row,v))%3 for row in A)
def solve(A,v,n):
 B,P=rr([row+[a]for row,a in zip(A,v)],n+1)
 if n in P:return None
 ans=[0]*n
 for row,j in zip(B,P):ans[j]=row[-1]
 assert ev(A,ans)==tuple(v)
 return ans
def outside(W,Z,n):
 base=span(W,n);out=[]
 for v in Z:
  if rank(base+[v],n)>len(base):out.append(v);base=span(base+[v],n)
 return out
def structure(v,d,n):
 vs=ev(d['valuation'],v);U=d['units'];un=solve(U,v,len(U[0]))is not None
 ans={'source_exponents':v,'valuation_mod3':list(vs),'valuation_zero':not any(vs),'in_displayed_global_unit_space':un}
 if not any(vs)and 'class_boundary_H0'in d:
  H=d.get('valuation_zero_basis',tr(ker(d['valuation'],n)));c=solve(H,v,len(H[0]));assert c is not None
  ans['computed_ordinary_class_coordinates']=list(ev(d['class_boundary_H0'],c))
 return ans
def detect(A,W,blocks,n):
 M=[row for b in blocks for row in b['source_residue_rows']];D=[]
 for b in blocks:
  e=b['source_residue_rows'];EW=mul(e,W);ann=ker(tr(EW),len(e));D+=mul(ann,e)
 wr=tr(W);U=ker(A,n);Z=span(wr+ker(A+M,n),n);old=ker(A+D,n)
 assert rank(old+Z,n)==len(old)
 assert all(not any(ev(A,w))for w in wr)
 return {'primes':[b['prime']for b in blocks],'containing_dimension':len(U),'point_dimension':len(wr),'raw_evaluation_rank_on_U':len(U)-len(ker(A+M,n)),'raw_evaluation_kernel_basis':ker(A+M,n),'separate_kernel_dimension':len(old),'common_kernel_dimension':len(Z),'separate_quotient_kernel_dimension':len(old)-len(wr),'common_quotient_kernel_dimension':len(Z)-len(wr),'separate_detected_rank':len(U)-len(old),'common_detected_rank':len(U)-len(Z),'separate_kernel_source_basis':old,'common_kernel_source_basis':Z,'separate_nonpoint_kernel_basis':outside(wr,old,n),'common_nonpoint_kernel_basis':outside(wr,Z,n)}
def enumerate_check(A,W,blocks,n,Z):
 U=ker(A,n);M=[row for b in blocks for row in b['source_residue_rows']];MW=mul(M,W);r=len(W[0])if W else 0
 pointvals={ev(MW,a)for a in itertools.product(range(3),repeat=r)};surv=[]
 for c in itertools.product(range(3),repeat=len(U)):
  v=[sum(c[i]*U[i][j]for i in range(len(U)))%3 for j in range(n)]
  if ev(M,v)in pointvals:surv.append(v)
 assert len(surv)==3**len(Z)and rank(surv,n)==len(Z)
 return {'containing_combinations_tested':3**len(U),'common_repair_survivors':len(surv),'passed':True}
def main():
 # Convert only raw source evaluation output for the newly sealed433 scan.
 blocks,skips=ast.literal_eval((R/'433_scan/scan.gpdata').read_text().replace(']~',']'))
 raw={'fresh_primes':[dict(zip(['prime','roots','torsion_points','cubic_root','source_residue_rows','addition_triples'],b))for b in blocks],'skipped':skips}
 (R/'inputs/433a1_signatures.json').write_text(json.dumps(raw,indent=2)+'\n')
 out=[]
 for nm in CASES:
  d=json.loads((R/'inputs'/f'{nm}_matrices.json').read_text());n=d['source_dimension'];W=d['points']or[[]for _ in range(n)];blocks=json.loads((R/'inputs'/f'{nm}_signatures.json').read_text())['fresh_primes'];wr=tr(W)
  stages={'scalar_only':d['scalar'],'global_necessary':d['scalar']+d['additivity'],'scalar_local':d['scalar']+d['local'],'joint_necessary':d['scalar']+d['additivity']+d['local']}
  exact=R/'exact_global'/f'{nm}.json'
  if exact.exists():
   z=json.loads(exact.read_text());N=z['global_norm_kernel'];rows=tr(N);stages['exact_global']=ker(rows,n);stages['exact_global_and_local']=ker(rows,n)+d['local']
  row={'case':nm,'source_dimension':n,'source_grade':('CERTIFIED_COMPLETE_RETAINED'if nm in ['1913b1','389a1','433a1']else 'CONDITIONAL_OR_INCOMPLETE_DISPLAYED_SOURCE_ONLY'),'point_dimension':len(wr),'kernel_construction_uses_known_excess_columns':False,'stages':{}}
  for tag,A in stages.items():
   u=ker(A,n);prefix=[]
   for k in range(1,len(blocks)+1):prefix.append(detect(A,W,blocks[:k],n))
   full=prefix[-1];full['common_residual_structure']=[structure(v,d,n)for v in full['common_nonpoint_kernel_basis']];full['separate_residual_structure']=[structure(v,d,n)for v in full['separate_nonpoint_kernel_basis']]
   row['stages'][tag]={'containing_source_basis':u,'containing_dimension':len(u),'containing_structure':[structure(v,d,n)for v in u],'prefix_results':prefix,'full':full}
   if tag in ['joint_necessary','exact_global_and_local']:row['stages'][tag]['exhaustive_repair_check']=enumerate_check(A,W,blocks,n,full['common_kernel_source_basis'])
  if nm=='seed3':
   row['sealed_old_blind_prefixes']=[detect(stages['joint_necessary'],W,[next(b for b in blocks if b['prime']==q)for q in qs],n)for qs in [[1213],[1213,1543],[1213,1543,1699]]]
  if nm=='1913b1':row['weak_then_strong']=[detect(stages['joint_necessary'],W,[next(b for b in blocks if b['prime']==q)for q in qs],n)for qs in [[1867],[997],[1867,997]]]
  out.append(row)
 (R/'KERNEL_RESULTS.json').write_text(json.dumps({'status':'FULL_SOURCE_KERNEL_EXPERIMENT','known_excess_columns_used':False,'cases':out,'scope':'Detectors constrain invisible kernels only; they are never added as Selmer admission conditions. Whole-source interpretation requires retained completeness; seed and28042 remain displayed-source-only.'},indent=2)+'\n')
 print(json.dumps([{ 'case':z['case'],'grade':z['source_grade'],'stages':{k:{a:v['full'][a]for a in ['containing_dimension','point_dimension','separate_quotient_kernel_dimension','common_quotient_kernel_dimension','common_detected_rank']}for k,v in z['stages'].items()}}for z in out],indent=2))

if __name__ == "__main__":
 main()
