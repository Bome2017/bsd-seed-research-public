"""Only phase reading supplied class columns, after full kernel construction."""
from pathlib import Path
import json,hashlib,itertools
import calculate as f
R=Path(__file__).resolve().parent
p=R/'KERNEL_RESULTS.json';binding=hashlib.sha256(p.read_bytes()).hexdigest();results=json.loads(p.read_text());out=[];decomp=[]
for row in results['cases']:
 nm=row['case'];d=json.loads((R/'inputs'/f'{nm}_matrices.json').read_text());n=d['source_dimension'];W=d['points'] or [[]for _ in range(n)];wr=f.tr(W)
 U=row['stages']['joint_necessary']['containing_source_basis'];known=json.loads((R/'heldout'/f'{nm}_known.json').read_text())['known_columns'];kr=f.tr(known)
 equal=f.rank(U+kr,n)==len(U)==f.rank(kr,n)
 assert equal
 out.append({'case':nm,'known_span_equals_reconstructed_kernel':equal,'known_classes_read_only_after_kernel_sha256':binding,'source_grade':row['source_grade']})
 # Every basis extension is calculated from the full-source kernels, not the withheld labels.
 S=f.span(wr,n);groups=[]
 for name,key in [('admitted_nonpoint','joint_necessary'),('globally_admitted_but_locally_rejected','exact_global'),('scalar_compatible_but_not_globally_admitted','scalar_only')]:
  if key not in row['stages']:
   continue
  target=row['stages'][key]['containing_source_basis']
  extra=f.outside(S,target,n)
  if name=='scalar_compatible_but_not_globally_admitted' and 'exact_global' not in row['stages']:
   name='outside_joint_admission_containing_kernel'
  groups.append({'category':name,'vectors':[f.structure(v,d,n) for v in extra]});S=f.span(S+extra,n)
 decomp.append({'case':nm,'grade':row['source_grade'],'groups':groups,'scope':'Exact global categories certified only where exact_global present. Without that map, source classes outside joint necessary kernel are not assigned a specific failed global gate.'})
(R/'HOLDOUT_COMPARISON.json').write_text(json.dumps({'kernel_result_sha256':binding,'comparisons':out},indent=2)+'\n')
(R/'ADMISSION_FILTRATION.json').write_text(json.dumps(decomp,indent=2)+'\n')
# Specific433 repaired-point incompatibility on its exact globally admitted extra.
nm='433a1';d=json.loads((R/'inputs'/f'{nm}_matrices.json').read_text());W=d['points'];N=json.loads((R/'exact_global'/f'{nm}.json').read_text())['global_norm_kernel'];a=[r[-1]for r in N];B=json.loads((R/'inputs'/f'{nm}_signatures.json').read_text())['fresh_primes'];rep=[]
for b in B[:2]:
 M=b['source_residue_rows'];MW=f.mul(M,W);target=f.ev(M,a);sol=[list(v)for v in itertools.product(range(3),repeat=2)if f.ev(MW,v)==target];assert len(sol)==1;rep.append({'prime':b['prime'],'point_coefficients':sol[0],'literal_local_class_values':list(target)})
assert rep[0]['point_coefficients']!=rep[1]['point_coefficients']
(R/'433_COMMON_REPAIR.json').write_text(json.dumps({'source_exponents':a,'repairs':rep,'one_common_point_exists':False,'global_status':'Genuine global cohomology class by exact scalar/affine norm certificate','Selmer_status':'Rejected by authenticated local conditions at3 and433; this auxiliary detector alone does not determine that membership.'},indent=2)+'\n')
print(json.dumps({'all_full_kernel_spans_recovered':True,'433_repairs':rep},indent=2))
