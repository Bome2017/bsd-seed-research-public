#!/usr/bin/env python3
import itertools,json,hashlib,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'theory'))
import dual_overlap as z
from analyze import matvec,witness,freshkiller

base=ROOT/'heldout/mirror_extension';raw=json.loads((base/'matrices.json').read_text());d=z.adapt(raw)
extra=json.loads((base/'blocks.json').read_text());assert extra['source_sha256']==hashlib.sha256((base/'matrices.json').read_bytes()).hexdigest()
blocks=extra['blocks'];assert len(blocks)==60
C=z.complement(d['U'],d['H0']);assert z.cols(C)==1;beta=z.tr(C)[0]
Kbase=z.ker(d['G0']+d['A']+d['L'],d['n']);assert z.cols(Kbase)==0
results=[]
for b in blocks:
    G=d['G0']+b['rows'];p=z.profile(d,G,d['L'],f"extension_{b['q']}__all_local")
    p['prime']=b['q'];p['kernel_recovered']=p['full_joint_dimension']==0;results.append(p)
fails=[p for p in results if not p['kernel_recovered']]
detail=None
if fails:
    fail=fails[0];b=next(b for b in blocks if b['q']==fail['prime']);G=d['G0']+b['rows']
    good=next((p for p in results if p['kernel_recovered'] and p['dual_overlap_dimension']==fail['dual_overlap_dimension']),None)
    repairs=[]
    for u in itertools.product(range(3),repeat=z.cols(d['U'])):
        v=[(a+b)%3 for a,b in zip(beta,matvec(d['U'],u))]
        repairs.append((sum(a!=0 for a in u),u,v,not any(matvec(G,v)),not any(matvec(d['L'],v))))
    repairs.sort();gu=next(r for r in repairs if r[3]);lu=next(r for r in repairs if r[4]);common=[r for r in repairs if r[3]and r[4]]
    K=z.ker(G+d['L'],d['n']);v=witness(K,z.eye(d['n']))
    detail=dict(prime=fail['prime'],matched_passing_prime=good['prime'] if good else None,
       failing_profile=fail,matched_passing_profile=good,source_beta=beta,
       global_unit_repair=list(gu[1]),local_unit_repair=list(lu[1]),
       common_unit_repairs=[list(r[1])for r in common],common_repaired_sources=[r[2]for r in common],
       smallest_extra_source_exponents=v,valuations=matvec(d['V'],v),
       local_defects={str(b['prime']):matvec(b['rows'],v)for b in d['locals']},
       fresh_eliminating_row=freshkiller(v,blocks,[fail['prime']]),
       first_larger_prime_eliminating_row=freshkiller(v,[b for b in blocks if b['q']>fail['prime']],[]),
       failing_global_unit_kernel=z.ker(z.mm(G,d['U']),z.cols(d['U'])),
       matched_passing_global_unit_kernel=z.ker(z.mm(d['G0']+next(b['rows']for b in blocks if b['q']==good['prime']),d['U']),z.cols(d['U'])) if good else None)
posthoc=[]
if fails:
    fb=[b for b in blocks if b['q']in [p['prime']for p in fails]]
    combos=list(itertools.combinations(fb,2))+[tuple(fb)]
    for combo in combos:
        G=d['G0']+[r for b in combo for r in b['rows']]
        v=detail['smallest_extra_source_exponents'];assert not any(matvec(G+d['L'],v))
        p=z.profile(d,G,d['L'],'posthoc_failure_union')
        posthoc.append(dict(primes=[b['q']for b in combo],full_joint_dimension=p['full_joint_dimension'],
          marginal_class_dimension=p['separately_repairable_class_dimension'],omega_rank=p['compatibility_defect_rank'],
          point_relative_dimensions=p['point_relative_dimensions'],common_survivor=v))
out=dict(status='SEALED_MIRROR_EXTENSION_ANALYZED',blocks=60,failed_primes=[p['prime']for p in fails],
   first_failure=detail,profiles=results,source_sha256=extra['source_sha256'],blocks_sha256=hashlib.sha256((base/'blocks.json').read_bytes()).hexdigest())
out['posthoc_failed_block_combinations']=posthoc
out['posthoc_scope']='These combinations were chosen after viewing the sealed single-block extension outcomes; they are not original-panel H_pair predictions.'
(ROOT/'heldout_analysis/MIRROR_EXTENSION.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'failed_primes':out['failed_primes'],'first_failure_prime':None if detail is None else detail['prime'],'matched_passing_prime':None if detail is None else detail['matched_passing_prime']}))
