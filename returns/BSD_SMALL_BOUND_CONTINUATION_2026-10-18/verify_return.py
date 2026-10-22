"""Verify saved-table arithmetic, scope receipts and file custody; not a BSD proof."""
from pathlib import Path
import ast
import hashlib
import json

ROOT = Path(__file__).resolve().parent
def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

manifest_counts = {}
for manifest in sorted(ROOT.glob('*/MANIFEST.sha256')):
    count = 0
    for line in manifest.read_text().splitlines():
        expected, name = line.split(None, 1)
        p = manifest.parent / name.lstrip('*')
        assert p.is_file() and digest(p) == expected, str(p)
        count += 1
    manifest_counts[str(manifest.relative_to(ROOT))] = count

summary = json.loads((ROOT/'explicit_seed_functions/SUMMARY.json').read_text())
total = 0
for table in summary['tables']:
    path = ROOT/'explicit_seed_functions'/table['file']
    assert digest(path) == table['sha256']
    data = json.loads(path.read_text())
    survivors = []
    for m, b, resultant, exponents, remainder in data['candidates']:
        n = abs(resultant)
        assert n > 0
        actual = []
        for prime in data['S']:
            e = 0
            while n % prime == 0:
                n //= prime
                e += 1
            actual.append(e)
        assert actual == exponents and n == remainder
        if n == 1:
            survivors.append([m, b, exponents])
    assert len(data['candidates']) == table['tested']
    assert survivors == table['survivors']
    total += len(data['candidates'])
assert total == 5637 == summary['candidate_tests']

progress = [ast.literal_eval(s) for s in
            (ROOT/'p7_reduced_ideals/walk_progress.gp').read_text().splitlines()]
assert len(progress) == 253
assert [r[0] for r in progress] == list(range(1, 254))
assert all(r[1] == 0 for r in progress)
walk = json.loads((ROOT/'p7_reduced_ideals/WALK_RECEIPT.json').read_text())
assert walk['completed'] is False
assert 'alarm interrupt' in (ROOT/'p7_reduced_ideals/walk.err').read_text()
assert 'PRINCIPAL_IDEAL_WALK_COMPLETE' not in (ROOT/'p7_reduced_ideals/walk.out').read_text()
assert 'COUNT=5637' in (ROOT/'rank_mechanism/replay_all_direct.out').read_text()
assert not (ROOT/'rank_mechanism/replay_all_direct.err').read_text()

result = {'status': 'SAVED_DATA_AND_CUSTODY_PASS',
          'nested_manifest_entries': manifest_counts,
          'candidate_support_arithmetic_rechecked': total,
          'separate_saved_resultant_replay': 5637,
          'partial_reduced_ideal_rows': 253,
          'planned_reduced_ideal_rows': 432,
          'retained_unit_candidates_in_partial_walk': 0,
          'scope': 'No BNF replay, no new class completeness, no independent proof certification',
          'FIN': 'unchanged', 'ORDER9': 'unchanged', 'Q36': 'unchanged'}
print(json.dumps(result, indent=2, sort_keys=True))
