from pathlib import Path
import ast,json,re,math,hashlib
R=Path(__file__).resolve().parent
src=Path('/Users/bsm/BSD_RELATIVE_UNIT_EXECUTION_2026-10-18/source/norm_trials.gp')
rows=[ast.literal_eval(l) for l in src.read_text().splitlines()];panel=json.loads((R/'SELECTED.json').read_text())
w=[]
for line in (R/'private_pivots.gp.data').read_text().splitlines():
 m=re.match(r'\[(\d+), (\d+),',line);assert m
 k,q=map(int,m.groups());i=panel[k-1]['id']-1
 occurrences=[j+1 for j,row in enumerate(rows) if row[-1]%q==0]
 assert occurrences==[i+1],(k,q,occurrences)
 assert rows[i][-1]%(q*q)!=0
 w.append({'panel_index':k,'original_row':i+1,'prime':q,'norm_valuation':1,'occurrences_in_full_log':occurrences})
assert len(w)==80 and len({x['prime'] for x in w})==80
# Each private prime's exact actual-ideal pivot is +1 in its own column, zero in others.
P=[[int(i==j) for j in range(80)] for i in range(80)]
old=json.loads(Path('/Users/bsm/BSD_RELATIVE_UNIT_EXECUTION_2026-10-18/source/DIAGNOSTIC_TOP20.json').read_text())
old_coords={tuple(x[2:7]) for x in old}
overlap=[x['id'] for x in panel if tuple(x['reconstruction'][1:]) in old_coords]
result={'status':'EIGHTY_AUTHENTICATED_PRIVATE_ANTI_DIVISOR_PIVOTS','full_saved_norm_rows':len(rows),'selected_rows':80,'unique_actual_prime_rows':80,'rank_over_Q':80,'rank_mod_7':80,'integer_kernel_dimension':0,'mod7_kernel_dimension':0,'global_norm_support_check':'every selected q occurs in exactly its own row in the full14326 log','old_twenty_overlap':overlap,'warning':'Ranks apply to this selected family only; scalar closure and all unselected element vectors were not computed.','witnesses':w}
(R/'SUPPORT_VERIFICATION.json').write_text(json.dumps(result,indent=2)+'\n');(R/'PRIVATE_PIVOT_MATRIX.json').write_text(json.dumps(P)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='witnesses'},indent=2))
