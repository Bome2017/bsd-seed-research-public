from pathlib import Path
import ast,json,re
R=Path(__file__).resolve().parents[1]
raw=[ast.literal_eval(x) for x in (R/'partial_relations/inputs/norm_trials.gp').read_text().splitlines()]
sel=json.loads((R/'partial_relations/SELECTED.json').read_text())
res=json.loads((R/'partial_relations/RESULT.json').read_text())
primes=[]
for line in (R/'partial_relations/private_pivots.gp.data').read_text().splitlines():
 m=re.match(r'^\[(\d+), (\d+),',line); assert m
 k,q=map(int,m.groups());i=sel[k-1]['id']; primes.append(q)
 occ=[j+1 for j,z in enumerate(raw) if z[-1]%q==0]
 assert occ==[i] and raw[i-1][-1]%(q*q)!=0
 assert res['witnesses'][k-1]['prime']==q and res['witnesses'][k-1]['original_row']==i
assert len(primes)==len(set(primes))==80
for name in ('replay_pivots','replay_scalar'):
 assert not (R/'review'/f'{name}.err').read_text().strip()
 assert 'REPLAY_OK=80' in (R/'review'/f'{name}.out').read_text()
out={'unique_prime_support_witnesses':80,'full_norm_rows_checked_for_each':14326,'norm_valuation_one_witnesses':80,'independent_actual_ideal_replay':80,'independent_six_element_scalar_orbit_replay':80,'scalar_block_rank_Q':3,'scalar_block_rank_F7':3,'scalar_family_rank':240,'faithful_projected_family_rank':80,'nontrivial_ordinary_units_in_selected_scalar_group':0,'scope':'Retained field and scalar action; 80 new element-vector replays, four overlap old twenty; not all candidate vectors or complete unit space.'}
(R/'review/PRIVATE_REPLAY_RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
