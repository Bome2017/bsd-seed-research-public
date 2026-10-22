#!/usr/bin/env python3
from pathlib import Path
import ast, hashlib, json, math, collections
R=Path(__file__).resolve().parents[1]
checks={}
for lane in ('class_map','partial_relations'):
 seal=json.loads((R/lane/'SEAL.json').read_text())
 for name,digest in seal.items():
  path=R/lane/name if not name.startswith('/') else (R/lane/'CONTRACT.md' if Path(name).name=='CONTRACT.md' else R/lane/'inputs'/Path(name).name)
  assert hashlib.sha256(path.read_bytes()).hexdigest()==digest, path
 checks[lane+'_seal_entries']=len(seal)
raw=[ast.literal_eval(x) for x in (R/'partial_relations/inputs/norm_trials.gp').read_text().splitlines()]
support=json.loads((R/'partial_relations/NORM_SUPPORT.json').read_text())
rs=support['records']; assert len(raw)==len(rs)==14326
for i,(r,z) in enumerate(zip(raw,rs),1):
 assert z['id']==i and z['reconstruction']==r
 assert math.prod(int(p)**e for p,e in z['small_factors'].items())*z['cofactor']==abs(r[-1])
 assert z['shared_gcd']*z['private']==z['cofactor']
 assert z['cofactor']%z['shared_gcd']==0
checks['exact_norm_stripping_rows']=len(rs)
sel=json.loads((R/'partial_relations/SELECTED.json').read_text())
expected=sorted(rs,key=lambda z:(z['private'].bit_length(),z['cofactor'].bit_length(),abs(z['reconstruction'][-1]).bit_length(),z['id']))[:80]
assert sel==expected
checks['deterministic_selected_rows']=len(sel)
checks['distinct_abs_norms']=len({abs(r[-1]) for r in raw})
checks['private_one']=sum(z['private']==1 for z in rs)
checks['fully_smooth']=sum(z['cofactor']==1 for z in rs)
checks['shared_nontrivial']=sum(z['shared_gcd']>1 for z in rs)
# Independent pairwise gcd replay for a deterministic sample, retaining valuations.
for i in [0,1,17,999,5000,10000,14325]+[z['id']-1 for z in sel[:8]]:
 n=rs[i]['cofactor']; accum=1
 for j,z in enumerate(rs):
  if j!=i: accum=(accum*(z['cofactor']%n))%n
 assert math.gcd(n,accum)==rs[i]['shared_gcd'], i
checks['batch_gcd_independent_rows']=15
sc=json.loads((R/'class_map/SCREEN_CANDIDATES.json').read_text());sr=json.loads((R/'class_map/SCREEN_RESULT.json').read_text())
assert len(sc)==len(sr['results'])==64
for c,z in zip(sc,sr['results']):
 assert c['label']==z['label']
 d=R/'class_map/screen'/c['label']
 assert (d/'screen.out').read_text().strip()==z['stdout']
 if z['status']=='screened': assert not (d/'screen.err').read_text().strip()
checks['class_panel_status']=dict(collections.Counter(z['status'] for z in sr['results']))
checks['class_dim_distribution']=dict(collections.Counter(z['stdout'].split('DIM=')[1].splitlines()[0] for z in sr['results'] if z['status']=='screened'))
checks['scope']='Saved-output replay and exact integer identities; no BNF rerun, class certification, source search, or new seed arithmetic.'
(R/'review/REPLAY_RESULT.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2))
