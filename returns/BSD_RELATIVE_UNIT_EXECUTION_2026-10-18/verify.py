#!/usr/bin/env python3
"""Read-only custody and saved-output consistency, not a BSD proof checker."""
from pathlib import Path
import argparse, ast, hashlib, json, re

R = Path(__file__).resolve().parent

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def manifest(p):
    count = 0
    for line in p.read_text().splitlines():
        if not line.strip():
            continue
        h, name = line.split('  ', 1)
        f = (p.parent / name).resolve()
        assert f.is_relative_to(R), ('outside packet', name)
        assert f.is_file() and digest(f) == h, ('manifest mismatch', str(f))
        count += 1
    return count

ap = argparse.ArgumentParser(description=__doc__)
ap.add_argument('--skip-root-manifest', action='store_true')
a = ap.parse_args()
counts = {d: manifest(R / d / 'MANIFEST.sha256') for d in ('source', 'evaluation', 'review')}
review_bindings = json.loads((R/'FINAL_SCOPE_BINDINGS.json').read_text())
for name,h in review_bindings['reviewed_files'].items():
    assert digest(R/name) == h, ('final review binding', name)
inputs = json.loads((R/'INPUT_BINDINGS.json').read_text())
for row in inputs['files']:
    p = R/row['new_relative']
    assert p.stat().st_size == row['bytes'] and digest(p) == row['sha256']
s = R/'source'
rows = [ast.literal_eval(t) for t in (s/'norm_trials.gp').read_text().splitlines() if t.strip()]
ideals = json.loads((s/'IDEAL_NORMS.json').read_text())
rejected = [t for t in rows if abs(t[5]) == ideals[t[3]-1][1]]
assert len(rows) == 14326 and not rejected
out = (s/'search.gp.out').read_text()
pat = r'CHECKPOINT stage=(\d+) amplitude=(\d+) direction=(\d+) ideal=(\d+) exact_norms=(\d+) pure_skips=(\d+) duplicates=(\d+) admitted=(\d+) wall_ms=(\d+)'
cp = [tuple(map(int,m.groups())) for m in re.finditer(pat,out)]
assert cp[-1][0] == 1317 and cp[-1][4] == len(rows) and cp[-1][7] == 0
assert 'SEARCH_SCHEDULE_COMPLETE' not in out
assert 'alarm interrupt' in (s/'search.gp.err').read_text()
assert json.loads((s/'PAIR_RESULT.json').read_text()) == [20,190,380,0]
assert json.loads((s/'ANTI_DIVISOR_RESULT.json').read_text()) == [20,127,20,20,0]
assert 'ANTI_DIVISOR_CHECK_COMPLETE=' in (s/'anti_finish.gp.out').read_text()
assert (s/'anti_divisor.gp.out').read_text().count('ANTI_FACTOR_AUTH=') == 20
assert 'nonexistent component' in (s/'anti_divisor.gp.err').read_text()
assert not (s/'anti_finish.gp.err').read_text().strip()
factor = json.loads((s/'anti_divisor.gp.receipt.json').read_text())
finish = json.loads((s/'anti_finish.gp.receipt.json').read_text())
assert factor['elapsed_seconds']+finish['elapsed_seconds'] < 60
result=json.loads((s/'RESULT.json').read_text())
assert result['relative_units_admitted'] == 0 and result['anti_divisor_complete']
assert result['complete_source_bound'] is None and result['class_group_bound'] is None
evalstate=json.loads((R/'evaluation/STATE.json').read_text())
assert evalstate['actual_rank'] == 'UNMEASURED'
assert evalstate['new_arithmetic_rank_runs'] == 0
assert evalstate['new_unit_kernel_bound'] is None and evalstate['new_class_bound'] is None
assert (R/'review/FINAL_ACCOUNTING.json').read_bytes() == (R/'review/FINAL_ACCOUNTING_REPLAY.json').read_bytes()
res = {
    'status':'CUSTODY_AND_SAVED_OUTPUT_CONSISTENCY_PASS',
    'portable_input_files':len(inputs['files']),
    'final_review_file_bindings':len(review_bindings['reviewed_files']),
    'nested_manifest_entries':counts,
    'mixed_exact_norm_output_rows':len(rows),
    'completed_search_stages':cp[-1][0],
    'planned_search_stages':1344,
    'main_search_completed_schedule':False,
    'pair_HNF_comparisons':380,
    'anti_divisor_record':[20,127,20,20,0],
    'anti_divisor_factor_and_repair_seconds':factor['elapsed_seconds']+finish['elapsed_seconds'],
    'admitted_units':0,
    'actual_norm_local_rank':'UNMEASURED',
    'arithmetic_reexecuted_by_this_script':False,
    'scope':'Hashes and deterministic saved-output consistency only. See independent reviews for arithmetic replay. No seed theorem certification.'
}
if not a.skip_root_manifest and (R/'MANIFEST.sha256').exists():
    res['root_manifest_entries']=manifest(R/'MANIFEST.sha256')
print(json.dumps(res,indent=2))
