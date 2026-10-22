#!/usr/bin/env python3
"""Integrate the completed, reviewed D=-23 certificate into the existing record."""
from pathlib import Path
import hashlib
import json
import re
import sys
from datetime import datetime, timezone

WORK = Path(__file__).resolve().parent
ROOT = WORK.parents[1]
sys.path.insert(0, str(ROOT))
import verify_master


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    return json.loads(path.read_text())


def save(path, value):
    path.write_text(json.dumps(value, indent=2) + '\n')


def replace_once(text, old, new):
    assert text.count(old) == 1, old
    return text.replace(old, new, 1)


now = datetime.now(timezone.utc).isoformat()
result = load(WORK / 'RESULT.json')
review = load(WORK / 'COMPLETION_REVIEW.json')
assert result['status'] == 'TWIST_D23_NONZERO_CERTIFIED'
assert review['result'] == 'PASS_WITH_DECLARED_COMPUTER_ASSISTED_TRUST_BASE'
assert review['zero_excluded'] and review['fresh_recombination_identical']
assert review['sealed_engine_unchanged'] and review['atomic_units_verified'] == 1030
assert result['interval'] == '[39512236, 40182321] / 1000000'
assert verify_master.check()['result'] == 'PASS_WITH_STATED_COVERAGE_LIMITS'

before = ROOT / 'provenance/before_d23_twist_implementation_20260921T191336Z.tar.gz'
assert sha(before) == '0d15aebec64771b8a79696a860edcce86d8682fbb2b78aef4049433502ceb339'

state = load(WORK / 'STATE.json')
state.update({
    'updated_utc': now,
    'phase': 'COMPLETED',
    'next': 'None: certificate complete; no successor authorized by this operation',
    'completed_units': 1030,
    'elapsed_seconds': result['arithmetic_elapsed_seconds'],
    'main_engine_wall_seconds': 708.40,
    'main_engine_peak_resident_bytes': 1004609536,
    'extension_executed': False,
    'completion_review': 'COMPLETION_REVIEW.json',
    'canonical_integration': 'MASTER_BSD_DAG.md updated with exact premise and retained qualifications',
    'successor_started': False,
})
save(WORK / 'STATE.json', state)
exact = load(WORK / 'EXACT_TWIST_INPUTS.json')
exact.update({
    'twist_rank_certified': True,
    'twist_analytic_rank': 1,
    'twist_algebraic_rank': 1,
    'rank_over_K': 3,
    'certificate': 'RESULT.json',
    'theorem_dependencies': 'PROOF.md; retained analytic-rank-one theorem and seed rank theorem',
    'grade': 'Computer-assisted derivative certificate with retained coefficient/software and imported theorem inputs',
})
save(WORK / 'EXACT_TWIST_INPUTS.json', exact)
(WORK / 'RESUME.md').write_text('''# Completed D=-23 certificate

Status: TWIST_D23_NONZERO_CERTIFIED. Read RESULT.md, RESULT.json, PROOF.md and COMPLETION_REVIEW.json. The completed enclosure is 39.512236 <= L'(E^-23,1) <= 40.182321. The initial cutoff T=3,456,106,495 sufficed; no extension was executed. All 1,030 atomic units are retained. Do not restart the supervisor or launch a successor by default.

The certificate supplies analytic rank one for the twist, and the retained rank-one theorem and seed rank give rank E(Q(sqrt(-23)))=3. It does not evaluate a Stark ideal or settle any additional primary group of the seed. FIN, ORDER9 and Q36 remain open.

The source engine and C11 corpus are unchanged. INPUT_BINDINGS.json records 418 preflight-hashed coefficient segments and verifier records; only 206 were consumed. BUILD_BINDINGS.json governs the final adapter identities; initial implementation identities in INPUT_BINDINGS.json are historical. Validation, the reference-harness correction, benchmarks, failed initial test log and restart units are preserved. review_completion.py rechecks the metadata/custody evidence and fresh combination. This is not Lean verification or a second full numerical implementation.

The canonical result is integrated into the existing MASTER_BSD_DAG.md. The external Aristotle host has 32 GB per the user; this local table-free implementation measured about 1.00 GB peak resident memory. No new package or message was sent.
''')

master = (ROOT / 'MASTER_BSD_DAG.md').read_text()
master = replace_once(master,
    'No such twist is certified in this operation.',
    'That audit did not certify a twist. The completed D=-23 certificate below now supplies this premise for K=Q(sqrt(-23)), while leaving the ideal unevaluated.')
master = replace_once(master,
    'No derivative enclosure or adequate cutoff is certified.',
    'That review supplied no derivative enclosure or adequate-cutoff certificate; this numerical gap is superseded by the completed D=-23 computation below.')
start = master.index('**D=-23 certified execution, active.**')
assert master[start:].count('\n\n') <= 1
master = master[:start] + r'''**D=-23 certified execution, completed (September 21).** The isolated table-free [computation and certificate](_work/d23_twist_2026-09-21/RESULT.md) give
\[
\boxed{39.512236\le L'(E^{-23},1)\le40.182321.}
\]
The root number is -1, so the twist has analytic rank exactly one. The retained Gross–Zagier–Kolyvagin rank-one theorem and seed rank theorem therefore give rank E^{-23}(Q)=1 and rank E(Q(sqrt(-23)))=3. This supplies the suitable certified rank-one twist premise in the preceding Fitting-ideal shift. The [proof and precise dependencies](_work/d23_twist_2026-09-21/PROOF.md) verify that this K also satisfies the recorded splitting conditions at p=13. Under the retained source-composition hypotheses and grades, the displayed shift by three now applies to this actual K. No Stark ideal is evaluated, no additional seed primary component is settled, and FIN, ORDER9 and Q36 remain open. Finiteness of Sha of the rank-one twist does not imply finiteness for the seed or for E/K.

The initial cutoff T=3,456,106,495 sufficed: the finite sum is enclosed by 39.847278312318874 +/- 4.28e-16, including finite Arb and Taylor errors, and the infinite tail is at most 0.335041797049. The [completion review](_work/d23_twist_2026-09-21/COMPLETION_REVIEW.json) verifies all 1,030 unit identities, 206 freshly rehashed coefficient segments, the exact coverage count, independent first-segment counts and identical fresh recombination. The main run measured 708.40 seconds and 1,004,609,536 bytes peak resident memory. No seven-billion extension was run. This is a computer-assisted certificate with the explicitly inherited coefficient, software and theorem trust base, not a Lean proof, fresh replay of all prime witnesses, independent human review or second full numerical implementation. The sealed source engine and corpus remain unchanged. The [completed checkpoint](_work/d23_twist_2026-09-21/STATE.json) and [restart instructions](_work/d23_twist_2026-09-21/RESUME.md) preserve the run. The external Aristotle host has 32 GB per the user; this implementation is table-free. No successor is launched.
'''
(ROOT / 'MASTER_BSD_DAG.md').write_text(master)

resume = (ROOT / 'RESUME.md').read_text()
resume = replace_once(resume, '# Saved BSD research checkpoint\n', '''# Saved BSD research checkpoint

**Current arithmetic completion (September 21): TWIST_D23_NONZERO_CERTIFIED.** Read _work/d23_twist_2026-09-21/RESULT.md and PROOF.md. The certified interval is 39.512236 <= L'(E^-23,1) <= 40.182321, proving twist analytic rank one. With the retained rank-one and seed theorems, rank E(Q(sqrt(-23)))=3. This supplies the previously missing twist premise; no Stark ideal or new seed primary group is evaluated. FIN, ORDER9 and Q36 remain open. The run and its completion checks are finished. Do not restart it or launch a successor by default.

The paragraphs below preserve the preceding source-review history. Their statements that no twist was certified or no run had started describe those earlier checkpoints; this completed certificate supersedes precisely that missing numerical premise.
''')
resume = re.sub(r'ACTIVE D=-23 computation:.*?(?=\n\n|\Z)',
    'COMPLETED D=-23 computation: _work/d23_twist_2026-09-21/STATE.json, RESULT.json and COMPLETION_REVIEW.json preserve the finished run. All units, the coefficient root, coverage count and fresh recombination passed verification. No supervisor restart or successor is pending.', resume, count=1, flags=re.S)
(ROOT / 'RESUME.md').write_text(resume)

entry = (ROOT / '00_READ_FIRST.md').read_text()
entry = replace_once(entry, '**Latest arithmetic result: the 11-primary component vanishes.**', '''**Latest arithmetic result: the D=-23 twist has analytic rank one.** The [completed interval certificate](_work/d23_twist_2026-09-21/RESULT.md) proves 39.512236 <= L'(E^-23,1) <= 40.182321. The retained rank-one theorem and seed rank give rank E(Q(sqrt(-23)))=3, supplying the suitable-twist premise of the existing comparison. Its Stark ideal remains unevaluated; no new seed primary component, FIN, ORDER9 or Q36 is proved. The source/certificate qualifications and exact implication are in [PROOF.md](_work/d23_twist_2026-09-21/PROOF.md). The run is complete and saved; no successor is active.

**Latest primary-component result: the 11-primary component vanishes.**''')
(ROOT / '00_READ_FIRST.md').write_text(entry)

canonical = load(ROOT / 'STATE.json')
canonical['preceding_primary_theorem_operation'] = canonical['last_theorem_operation']
canonical['last_theorem_operation'] = {
    'file': str(WORK / 'PROOF.md'),
    'status': 'TWIST_D23_NONZERO_CERTIFIED',
    'derivative_interval': result['interval'],
    'D': -23,
    'twist_analytic_rank': 1,
    'rank_over_Q_sqrt_minus23': 3,
    'certificate_bindings': str(WORK / 'BUILD_BINDINGS.json'),
    'completion_review': str(WORK / 'COMPLETION_REVIEW.json'),
    'imported_qualifications_retained': True,
    'new_seed_primary_group_settled': False,
    'global_BSD_endpoint_changed': False,
    'stark_ideal_evaluated': False,
    'formal_verification': False,
    'successor_started': False,
}
canonical['status'] = 'D23_TWIST_CERTIFIED_FULL_BSD_OPEN'
canonical['last_updated_utc'] = now
canonical['current_research_operation']['status'] = 'COMPLETED'
canonical['current_research_operation']['result'] = str(WORK / 'RESULT.md')
canonical['mathematical_state']['D_minus23_twist'] = {
    'analytic_rank': 1,
    'rank_over_K': 3,
    'grade': 'Computer-assisted with retained coefficient/software and imported rank-theorem inputs',
    'stark_ideal_evaluated': False,
}
canonical['new_arithmetic_computation_this_operation'] = True
canonical['next_authorized_operation'] = 'None launched by this completed D=-23 certificate; no automatic twist, prime scan or Stark-ideal computation.'
canonical['previous_state_archive'] = str(before)
save(ROOT / 'STATE.json', canonical)

inventory = load(ROOT / 'RECONCILIATION_INVENTORY.json')
inventory['integrated_operations'].append({
    'id': 'd23_twist_certificate_completion_2026-09-21',
    'integrated_at_utc': now,
    'result': 'TWIST_D23_NONZERO_CERTIFIED',
    'archive': str(before),
    'archive_sha256': sha(before),
    'new_records_reviewed': [str(WORK / n) for n in ['RESULT.md', 'PROOF.md', 'RESULT.json', 'COMPLETION_REVIEW.json']],
    'closed_premise': 'Suitable certified analytic-rank-one D=-23 twist, hence known rank-three point contribution over K',
    'scope': 'No Stark ideal evaluation, no additional seed primary component, no FIN, ORDER9 or Q36; source and computational qualifications retained',
})
save(ROOT / 'RECONCILIATION_INVENTORY.json', inventory)

with (WORK / 'CHECKPOINTS.jsonl').open('a') as handle:
    handle.write(json.dumps({'time': now, 'phase': 'COMPLETED_AND_INTEGRATED',
        'event': 'Completion review passed and exact twist premise integrated in existing canonical record',
        'interval': result['interval'], 'successor_started': False}) + '\n')

work_files = sorted(p for p in WORK.rglob('*') if p.is_file() and p.name != 'MANIFEST.sha256' and '__pycache__' not in p.parts and not p.name.endswith('.tmp'))
(WORK / 'MANIFEST.sha256').write_text(''.join(f'{sha(p)}  {p.relative_to(WORK)}\n' for p in work_files))

bindings = load(ROOT / 'SOURCE_BINDINGS.json')
assert not verify_master.changed_sources(bindings['sources'])
bind_names = ['RESULT.md', 'PROOF.md', 'DESIGN.md', 'RESULT.json', 'COMPLETION_REVIEW.json',
    'INPUT_BINDINGS.json', 'BUILD_BINDINGS.json', 'VALIDATION_AND_BENCHMARK.json',
    'EXACT_TWIST_INPUTS.json', 'FIRST_SEGMENT_COUNT_CHECK.json', 'twist.c', 'twist',
    'retained_arbcore.c', 'build.sh', 'kernel_test.log', 'block_test.log',
    'block_test_initial_failed.log', 'run_T3456106495.log', 'combine_T3456106495.log',
    'run_T3456106495.time', 'review_completion.py', 'MANIFEST.sha256']
known = {x['path'] for x in bindings['sources']}
for name in bind_names:
    path = WORK / name
    assert str(path) not in known
    bindings['sources'].append({'path': str(path), 'sha256': sha(path),
        'role': 'Completed D=-23 derivative certificate and rank-three premise; retained computer-assisted/source qualifications, no Stark ideal or global BSD conclusion'})
bindings['sources'].sort(key=lambda x: x['path'])
bindings['canonical_document_sha256'] = sha(ROOT / 'MASTER_BSD_DAG.md')
bindings['recorded_at_utc'] = now
save(ROOT / 'SOURCE_BINDINGS.json', bindings)

verification = verify_master.check()
save(ROOT / 'VERIFICATION.json', verification)
assert verification['result'] == 'PASS_WITH_STATED_COVERAGE_LIMITS', verification

paths = {line.split('  ', 1)[1] for line in (ROOT / 'MANIFEST.sha256').read_text().splitlines()}
paths.update(str(p.relative_to(ROOT)) for p in work_files)
paths.add(str((WORK / 'MANIFEST.sha256').relative_to(ROOT)))
(ROOT / 'MANIFEST.sha256').write_text(''.join(f'{sha(ROOT / p)}  {p}\n' for p in sorted(paths)))

for base in [WORK, ROOT]:
    lines = (base / 'MANIFEST.sha256').read_text().splitlines()
    for line in lines:
        expected, name = line.split('  ', 1)
        assert sha(base / name) == expected, name
    print(f'MANIFEST_PASS {base.name} {len(lines)}')
print(json.dumps(verification, indent=2))
