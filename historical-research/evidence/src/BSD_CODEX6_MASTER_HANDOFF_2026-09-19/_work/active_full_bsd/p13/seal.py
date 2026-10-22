#!/usr/bin/env python3
"""Read-only verification and byte binding of the finished P13 run.

Writes review artifacts only. Never invokes a producer or writes into the corpus.
The integer witness verifier's saved receipts are checked, not rerun here.
"""
from pathlib import Path
from datetime import datetime, timezone
from math import isqrt
import hashlib
import json
import re
import struct

ROOT = Path(__file__).resolve().parent
MASTER = ROOT.parents[2]
EXTERNAL = Path('/Users/bsm/BSD_SEED_P13_RUN_2026-09-21')
RUN = EXTERNAL/'run'
CORE = Path('/Users/bsm/BSD_RIGOROUS_STREAM_CORE_2026-09-19')
SEG, BLK = 2**24, 2**22
PRIOR = ROOT.parent/'p11/CERTIFICATE_BINDINGS.json'


def now():
    return datetime.now(timezone.utc).isoformat()


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(8*1024*1024), b''):
            h.update(chunk)
    return h.hexdigest()


def bind(path):
    return {'path':str(path), 'sha256':sha(path), 'bytes':path.stat().st_size}


def event(phase, **kw):
    x = {'time_utc':now(), 'phase':phase, **kw}
    with (ROOT/'CHECKPOINTS.jsonl').open('a') as f:
        f.write(json.dumps(x)+'\n')
    state = json.loads((ROOT/'STATE.json').read_text())
    state.update(x)
    (ROOT/'STATE.json').write_text(json.dumps(state,indent=2)+'\n')
    print(json.dumps(x),flush=True)


inputs = json.loads((ROOT/'INPUT_BINDINGS.json').read_text())
for b in inputs['original_files']:
    assert sha(Path(b['path'])) == b['sha256'], b['path']
prior = json.loads(PRIOR.read_text())
engines = []
for expected in prior['engine_files']:
    actual = bind(Path(expected['path']))
    assert actual == expected, expected['path']
    engines.append(actual)
reference = prior['engine_identity_reference']
assert bind(Path(reference['path'])) == reference
for line in Path(reference['path']).read_text().splitlines():
    expected, rel = line.split()
    assert sha(CORE/rel) == expected, rel

event('CHECKING_CORPUS', expected_segments=3281, reused_segments=2333)
segments = []
for i in range(3281):
    ap, log = RUN/f'ap/ap_{i:06d}.bin', RUN/f'logs/ver_{i}.log'
    fields = log.read_text().split()
    assert len(fields) == 12 and fields[:3] == ['SEG',str(i),'lo']
    assert fields[4] == 'hi' and fields[6] == 'primes' and fields[8] == 'witnesses' and fields[10] == 'ap_sha256'
    lo,hi,np,nw = map(int,[fields[3],fields[5],fields[7],fields[9]])
    assert lo == i*SEG and hi == (i+1)*SEG
    assert np-nw == (566 if i == 0 else 0)
    a,l = bind(ap),bind(log)
    assert a['sha256'] == fields[11] and a['bytes'] == 4*np
    entry = {'segment':i,'prime_count':np,'witness_count':nw,'coefficients':a,'verifier_record':l}
    if i < 2333:
        old = prior['segments'][i]
        assert old['segment'] == i and old['prime_count'] == np and old['witness_count'] == nw
        assert ap.resolve() == Path(old['coefficients']['path']).resolve()
        assert log.resolve() == Path(old['verifier_record']['path']).resolve()
        for key,actual in [('coefficients',a),('verifier_record',l)]:
            assert actual['sha256'] == old[key]['sha256'] and actual['bytes'] == old[key]['bytes']
        entry['custody'] = 'REUSED_C11_BYTES_MATCH_PRE_INCIDENT_BINDINGS'
    else:
        witness = RUN/f'wit/wit_{i:06d}.bin'
        expected,path = (RUN/f'logs/witsha_{i}.txt').read_text().split()
        assert Path(path) == witness
        witness_binding = bind(witness)
        assert witness_binding['sha256'] == expected
        with witness.open('rb') as f:
            assert struct.unpack('<QQQ',f.read(24)) == (lo,hi,nw)
        assert (RUN/f'logs/ver_{i}.err').stat().st_size == 0
        assert (RUN/f'logs/prod_{i}.err').stat().st_size == 0
        entry['witness'] = witness_binding
        entry['witness_hash_receipt'] = bind(RUN/f'logs/witsha_{i}.txt')
        entry['custody'] = 'NEW_RETAINED_INTEGER_WITNESS_AND_VERIFIER_RECEIPT'
    segments.append(entry)
    if (i+1)%512 == 0 or i == 3280:
        event('CHECKING_CORPUS',checked_segments=i+1)

targets = []
for m,nseg in [(169,3281),(13,240)]:
    total = nseg*SEG-1
    output = RUN/f'msl_m{m}.txt'
    text = output.read_text()
    root = hashlib.sha256(b''.join(bytes.fromhex(s['coefficients']['sha256']) for s in segments[:nseg])).hexdigest()
    match = re.search(r'^AP_SEGROOT_SHA256 (\w+) segments (\d+)$',text,re.M)
    assert match and match.group(1) == root and int(match.group(2)) == nseg
    directory = RUN/f'units_m{m}'
    nblk = (total+BLK-1)//BLK
    expected = {f'lseg_{i:06d}.txt' for i in range(nseg)}|{f'blk_{i:06d}.txt' for i in range(nblk)}
    units = sorted(directory.glob('*.txt'))
    assert {p.name for p in units} == expected and not list(directory.glob('*.tmp'))
    small_top = isqrt(total)
    prime = bytearray(b'\1')*(small_top+1)
    prime[:2] = b'\0\0'
    for q in range(2,isqrt(small_top)+1):
        if prime[q]:
            prime[q*q::q] = b'\0'*((small_top-q*q)//q+1)
    small_count = sum(prime)
    smooth,pairs,bindings,leaves = 0,0,[],{}
    for unit in units:
        raw = unit.read_bytes()
        body, trailer = raw.rsplit(b'END ',1)
        assert trailer.endswith(b'\n') and len(trailer) == 65
        assert hashlib.sha256(body).hexdigest() == trailer.decode().strip()
        lines = body.splitlines()
        assert len(lines) == m+1
        for j,line in enumerate(lines[1:]):
            assert line.split(maxsplit=2)[:2] == [b'S',str(j).encode()]
        h = lines[0].decode().split()
        idx = int(unit.stem.split('_')[1])
        assert int(h[1]) == idx
        field = lambda key:h[h.index(key)+1]
        if unit.name.startswith('lseg'):
            assert h[0] == 'LSEG' and int(field('lo')) == idx*SEG and int(field('hi')) == (idx+1)*SEG
            assert field('apsha') == segments[idx]['coefficients']['sha256']
            assert int(field('bigprimes')) == segments[idx]['prime_count']-(small_count if idx==0 else 0)
            pairs += int(field('pairs'))
        else:
            assert h[0] == 'BLK' and int(field('lo')) == idx*BLK+1
            assert int(field('hi')) == min((idx+1)*BLK+1,total+1)
            smooth += int(field('smooth'))
            leaves[idx] = bytes.fromhex(field('leaf'))
        bindings.append({'path':str(unit),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)})
    assert smooth+pairs == total
    count = re.search(r'^COUNT .*$',text,re.M).group(0)
    assert count == f'COUNT smooth {smooth} pairs {pairs} sum {total} T {total} identity 1'
    merkle = hashlib.sha256(b''.join(leaves[i] for i in range(nblk))).hexdigest()
    assert f'SMOOTH_MERKLE_SHA256 {merkle} blocks {nblk}' in text
    params = (directory/'PARAMS').read_text().strip()
    expected_params = f'msl 0 -22735 0 106272484 0 {m} 6503188012738584 1 {total} {SEG} {RUN}/ap {directory} 1024'
    assert params == expected_params
    targets.append({'modulus':m,'cutoff':total,'segment_count':nseg,'coefficient_root':root,
        'smooth_merkle_root':merkle,'count':{'smooth':smooth,'pairs':pairs,'total':total},
        'work_unit_count':len(units),'arb_output':bind(output),
        'exact_symbols':bind(RUN/f'SYMBOLS_m{m}.txt'),'parameters':bind(directory/'PARAMS'),
        'all_work_units':bindings})
    event('WORK_UNITS_VERIFIED',modulus=m,units=len(units))

assert 'P3_CHECK_PASS failures=0' in (RUN/'P3_CHECK.txt').read_text()
down = json.loads((ROOT/'DOWNSTREAM.json').read_text())
assert down['all_checks_passed'] and down['residue_omega1'] == 2
for b in inputs['original_files']:
    assert sha(Path(b['path'])) == b['sha256'], b['path']
answer = {'status':'CUSTODY_AND_RECORDED_CHECKS_PASS','recorded_at_utc':now(),
    'scope':'Fresh actual-byte checks and saved independent-verifier receipts; no new integer-witness replay or second full numerical implementation',
    'engine_identity_reference':reference,'engine_files':engines,'prior_C11_binding':bind(PRIOR),
    'inputs':bind(ROOT/'INPUT_BINDINGS.json'),'segments':segments,'targets':targets,
    'check_output':bind(RUN/'P3_CHECK.txt'),'downstream_script':bind(ROOT/'downstream.py'),
    'downstream_result':bind(ROOT/'DOWNSTREAM.json'),
    'incident':bind(EXTERNAL/'INCIDENT_2026-09-21.md'),
    'post_incident_reused_corpus_matches_prior_bindings':True,
    'external_execution_files':[bind(EXTERNAL/n) for n in ['preflight.py','PREFLIGHT.json','STATE.json','RESUME.md','RESULT.json','POST_ABORT_INTEGRITY.json']],
    'coefficient_test_status':down['status']}
(ROOT/'CERTIFICATE_BINDINGS.json').write_text(json.dumps(answer,indent=2)+'\n')
event('CUSTODY_PASSED',verified_primes=sum(s['prime_count'] for s in segments),
    new_verified_primes=sum(s['prime_count'] for s in segments[2333:]),
    bound_work_units=sum(t['work_unit_count'] for t in targets),
    next='Replay completed-unit combination, fresh Stage C, then integrate')
