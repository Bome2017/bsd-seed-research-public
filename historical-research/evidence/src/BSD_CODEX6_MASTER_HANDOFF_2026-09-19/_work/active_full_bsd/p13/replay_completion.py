#!/usr/bin/env python3
"""Recombine only complete, hash-checked saved Arb units and replay Stage C."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import os
import subprocess
import time

ROOT = Path(__file__).resolve().parent
RUN = Path('/Users/bsm/BSD_SEED_P13_RUN_2026-09-21/run')
CORE = Path('/Users/bsm/BSD_RIGOROUS_STREAM_CORE_2026-09-19')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def bind(path):
    return {'path':str(path),'sha256':sha(path),'bytes':path.stat().st_size}


def event(phase, **kw):
    now = datetime.now(timezone.utc).isoformat()
    record = {'time_utc':now,'updated_utc':now,'phase':phase,**kw}
    with (ROOT/'CHECKPOINTS.jsonl').open('a') as f:
        f.write(json.dumps(record)+'\n')
    state = json.loads((ROOT/'STATE.json').read_text())
    state.update(record)
    (ROOT/'STATE.json').write_text(json.dumps(state,indent=2)+'\n')
    print(json.dumps(record),flush=True)


seal = json.loads((ROOT/'CERTIFICATE_BINDINGS.json').read_text())
assert seal['status'] == 'CUSTODY_AND_RECORDED_CHECKS_PASS'
for expected in seal['engine_files']:
    assert bind(Path(expected['path'])) == expected
env = os.environ.copy()
env['DYLD_LIBRARY_PATH'] = '/Users/bsm/H41_ANALYTIC_BLIND_RESEARCH_2026-09-12/sources/research_computation/pari-2.17.4/Odarwin-x86_64'
fresh = []
for t in seal['targets']:
    m = t['modulus']
    directory = RUN/f'units_m{m}'
    # Every unit must already exist. Hash checks precede any engine invocation.
    assert set(directory.glob('*.txt')) == {Path(b['path']) for b in t['all_work_units']}
    for b in t['all_work_units']:
        assert bind(Path(b['path'])) == b
    command = [str(CORE/'src/arbcore'),'msl','0','-22735','0','106272484','0',str(m),
               '6503188012738584','1',str(t['cutoff']),str(2**24),str(RUN/'ap'),'1',str(directory),'1024']
    event('REPLAYING_COMPLETED_UNITS',modulus=m,command=command)
    output = ROOT/f'fresh_m{m}.txt'
    error = ROOT/f'fresh_m{m}.err'
    start = time.monotonic()
    with output.open('w') as out, error.open('w') as err:
        subprocess.run(command,env=env,stdout=out,stderr=err,check=True)
    assert output.read_bytes() == Path(t['arb_output']['path']).read_bytes(), m
    assert error.stat().st_size == 0
    # Confirm the replay did not regenerate or change any saved unit.
    for b in t['all_work_units']:
        assert bind(Path(b['path'])) == b
    fresh.append({'modulus':m,'seconds':time.monotonic()-start,'output':bind(output),
                  'identical_to_original_arb_output':True,'all_saved_units_unchanged':True})
    event('RECOMBINATION_IDENTICAL',modulus=m)

stage = ROOT/'stage_c_replay'
stage.mkdir(exist_ok=True)
links = {'targets.txt':RUN/'targets.txt','logs':RUN/'logs','ap':RUN/'ap',
         'msl_m169.txt':ROOT/'fresh_m169.txt','msl_m13.txt':ROOT/'fresh_m13.txt'}
for name,source in links.items():
    dest = stage/name
    if dest.is_symlink():
        assert dest.resolve() == source.resolve()
    else:
        assert not dest.exists()
        dest.symlink_to(source)
with (ROOT/'STAGE_C_REPLAY.log').open('w') as out:
    subprocess.run(['python3',str(CORE/'p3plan/p3_check.py'),str(stage),str(2**24),'1024','0'],
                   stdout=out,stderr=subprocess.STDOUT,check=True)
assert 'P3_CHECK_PASS failures=0' in (ROOT/'STAGE_C_REPLAY.log').read_text()
for m in (169,13):
    assert (stage/f'SYMBOLS_m{m}.txt').read_bytes() == (RUN/f'SYMBOLS_m{m}.txt').read_bytes()
assert (ROOT/'STAGE_C_REPLAY.log').read_bytes() == (RUN/'P3_CHECK.txt').read_bytes()
down = json.loads((ROOT/'DOWNSTREAM.json').read_text())
assert down['residue_omega1'] == 2 and down['residue_full_real_period'] == 1
assert down['all_checks_passed'] and all(t['all_checks_passed'] for t in down['regressions'])
assert bind(ROOT/'DOWNSTREAM.json') == seal['downstream_result']
for b in json.loads((ROOT/'INPUT_BINDINGS.json').read_text())['original_files']:
    assert bind(Path(b['path'])) == b

report = {'status':'COMPLETION_REVIEW_PASS_WITH_DECLARED_TRUST_BASE',
    'completed_at_utc':datetime.now(timezone.utc).isoformat(),
    'residue_omega1':2,'residue_full_real_period':1,'normalization_discrepancy_resolved':True,
    'group_sums':down['group_sums'],'weighted_sum':down['folded_exact_rational'],
    'fresh_recombinations':fresh,'stage_c_replay':bind(ROOT/'STAGE_C_REPLAY.log'),
    'exact_checks_passed':len(down['checks']),
    'reused_segments_rehashed_against_pre_incident_binding':2333,
    'new_witnesses_hash_bound_and_receipts_checked':948,
    'verified_prime_count_from_receipts':sum(s['prime_count'] for s in seal['segments']),
    'new_verified_prime_count_from_receipts':sum(s['prime_count'] for s in seal['segments'][2333:]),
    'bound_arb_work_units':sum(t['work_unit_count'] for t in seal['targets']),
    'source_run_artifacts_unchanged_by_review':True,
    'historical_write_through_incident_retained':True,
    'full_integer_witness_verifier_rerun':False,'full_coefficient_arithmetic_rerun':False,
    'independent_end_to_end_numerical_implementation':False,'lean_verified':False,
    'certificate_bindings':bind(ROOT/'CERTIFICATE_BINDINGS.json'),
    'scope':'Same retained engine recombines saved units; exact downstream and actual-byte checks. Mathematical imports and the original coefficient/Arb software trust base remain.'}
(ROOT/'COMPLETION_REVIEW.json').write_text(json.dumps(report,indent=2)+'\n')
event('COMPLETION_VERIFIED',residue_omega1=2,residue_full_real_period=1,
      next='Write and integrate the qualified 13-primary theorem; no successor')
