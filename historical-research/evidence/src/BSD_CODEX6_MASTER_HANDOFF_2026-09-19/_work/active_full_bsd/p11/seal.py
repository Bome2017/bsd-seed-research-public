#!/usr/bin/env python3
"""Bind a completed p11 certificate to actual coefficient, witness, and engine bytes.

This checks custody and the recorded verification outputs, not the mathematics
of the retained coefficient verifier or Arb engine a second time.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

root = Path(__file__).resolve().parent
run = root / 'run'
core = Path('/Users/bsm/BSD_RIGOROUS_STREAM_CORE_2026-09-19')
old = Path('/Users/bsm/BSD_SEED_2243_12_P5_RIGOROUS_UPGRADE_2026-09-19/prelaunch/source_and_binary_hashes.txt')

def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(8*1024*1024), b''):
            h.update(block)
    return h.hexdigest()

def bind(path):
    return {'path': str(path), 'sha256': sha(path), 'bytes': path.stat().st_size}

retained = json.loads((run/'RETAINED_INPUTS.json').read_text())
assert sha(Path(retained['sealed_manifest'])) == retained['sealed_manifest_sha256']
engines = []
for line in old.read_text().splitlines():
    expected, relative = line.split()
    item = bind(core/relative)
    assert item['sha256'] == expected, relative
    engines.append(item)

prior = {item['segment']: item for item in retained['reused_segments']}
small_primes = [q for q in range(2,4096)
                if all(q % d for d in range(2,int(q**0.5)+1))]
exhaustive_count = len(small_primes) + 2  # bad primes 4547, 5843 exceed4096
assert exhaustive_count == 566
segments = []
for i in range(2333):
    ap = run/f'ap/ap_{i:06d}.bin'
    log = run/f'logs/ver_{i}.log'
    fields = log.read_text().split()
    assert fields[0] == 'SEG' and int(fields[1]) == i
    assert fields[2] == 'lo' and fields[4] == 'hi'
    assert int(fields[3]) == i*2**24 and int(fields[5]) == (i+1)*2**24
    assert fields[6] == 'primes' and fields[8] == 'witnesses'
    assert fields[10] == 'ap_sha256' and len(fields) == 12
    assert int(fields[7])-int(fields[9]) == (exhaustive_count if i == 0 else 0)
    ap_item, log_item = bind(ap), bind(log)
    assert ap_item['sha256'] == fields[11]
    assert ap_item['bytes'] == 4*int(fields[7])
    item = {'segment': i, 'prime_count': int(fields[7]),
            'witness_count':int(fields[9]),
            'coefficients': ap_item, 'verifier_record': log_item}
    if i in prior:
        p = prior[i]
        assert ap.resolve() == Path(p['ap_path'])
        assert log.resolve() == Path(p['verifier_record'])
        assert ap_item['sha256'] == p['ap_sha256']
        assert log_item['sha256'] == p['verifier_sha256']
        item['custody'] = 'REUSED_SEALED_P7_CERTIFICATE'
    else:
        witness = run/f'wit/wit_{i:06d}.bin'
        expected, path = (run/f'logs/witsha_{i}.txt').read_text().split()
        witness_item = bind(witness)
        assert Path(path) == witness and witness_item['sha256'] == expected
        assert (run/f'logs/ver_{i}.err').stat().st_size == 0
        assert (run/f'logs/prod_{i}.err').stat().st_size == 0
        item['witness'] = witness_item
        item['custody'] = 'NEW_RETAINED_INTEGER_WITNESS'
    segments.append(item)

symbols = []
for m,nsegments in ((121,2333),(11,202)):
    path = run/f'msl_m{m}.txt'
    content = path.read_text()
    expected = hashlib.sha256(b''.join(bytes.fromhex(s['coefficients']['sha256'])
                                       for s in segments[:nsegments])).hexdigest()
    got = re.search(r'AP_SEGROOT_SHA256 (\w+) segments (\d+)', content)
    assert got and got.group(1) == expected and int(got.group(2)) == nsegments
    count = re.search(r'^COUNT .*$', content, re.M).group(0)
    count_fields = count.split()
    total = nsegments*2**24-1
    assert int(count_fields[2])+int(count_fields[4]) == int(count_fields[6]) == int(count_fields[8]) == total
    assert count_fields[10] == '1'
    directory = run/f'units_m{m}'
    units = sorted(directory.glob('*.txt'))
    expected_names = {f'lseg_{i:06d}.txt' for i in range(nsegments)} | {f'blk_{i:06d}.txt' for i in range(4*nsegments)}
    assert {p.name for p in units} == expected_names and not list(directory.glob('*.tmp'))
    for unit in units:
        raw = unit.read_bytes()
        end = raw.rstrip(b'\n').rfind(b'\n')+1
        trailer = raw[end:].decode().split()
        assert trailer[0] == 'END' and len(trailer) == 2
        assert hashlib.sha256(raw[:end]).hexdigest() == trailer[1]
        header = raw.splitlines()[0].decode().split()
        index = int(unit.stem.split('_')[1])
        assert int(header[1]) == index
        if unit.name.startswith('lseg'):
            assert header[0] == 'LSEG'
            assert header[header.index('apsha')+1] == segments[index]['coefficients']['sha256']
        else:
            assert header[0] == 'BLK'
    params = (directory/'PARAMS').read_text().strip()
    assert params.startswith(f'msl 0 -22735 0 106272484 0 {m} 6503188012738584 1 {total} 16777216 ')
    assert params.endswith(' 1024')
    symbols.append({'modulus':m,'coefficient_root':expected,'count':count,
                    'arb_output':bind(path),
                    'exact_symbols':bind(run/f'SYMBOLS_m{m}.txt'),
                    'parameters':bind(run/f'units_m{m}/PARAMS'),
                    'all_work_units':[bind(p) for p in units]})
assert 'P3_CHECK_PASS failures=0' in (run/'P3_CHECK.txt').read_text()
downstream = json.loads((root/'DOWNSTREAM.json').read_text())
assert downstream['all_checks_passed']
result = {
    'status':'CUSTODY_AND_RECORDED_CHECKS_PASS',
    'recorded_at_utc':datetime.now(timezone.utc).isoformat(),
    'scope':'Actual byte bindings, independent-verifier receipts, Arb input roots, exact downstream checks. No new formal or independent end-to-end proof audit.',
    'engine_identity_reference':bind(old),
    'engine_files':engines,
    'retained_input_bindings':bind(run/'RETAINED_INPUTS.json'),
    'segments':segments,
    'targets':symbols,
    'check_output':bind(run/'P3_CHECK.txt'),
    'downstream_script':bind(root/'downstream.py'),
    'downstream_result':bind(root/'DOWNSTREAM.json'),
    'coefficient_test_status':downstream['status'],
    'execution_files':[bind(root/name) for name in ('preflight.py','supervise.py','downstream.py','seal.py','PREFLIGHT.json','LAUNCH.json','LAUNCH_RECONCILIATION.json')],
}
(root/'CERTIFICATE_BINDINGS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'reused_segments':len(prior),
                  'new_segments':2333-len(prior),'verified_primes':sum(s['prime_count'] for s in segments),
                  'coefficient_test_status':downstream['status']},indent=2))
