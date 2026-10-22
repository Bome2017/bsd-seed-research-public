#!/usr/bin/env python3
"""Replay the small receipt/custody joins, not the external coefficient corpus."""
import csv, hashlib, json, re, sys
from pathlib import Path
if sys.flags.optimize:
    raise SystemExit('Assertions must be enabled')
R=Path(__file__).resolve().parents[2]
sha=lambda b:hashlib.sha256(b).hexdigest()
d=json.loads((R/'review/followup_logs/corpus_acceptance_receipts.json').read_text())
scan=R/'review/replay_logs/witness_structure_scan.tsv'
assert sha(scan.read_bytes())==d['scan_sha256']
rows={x['path']:x for x in csv.DictReader(scan.open(),delimiter='\t')}
assert len(rows)==len(d['joins'])==3757
for x in d['documents'].values():assert sha(x['text'].encode())==x['sha256']
seen=set()
for j in d['joins']:
    assert j['witness'] not in seen; seen.add(j['witness']); s=rows[j['witness']]
    assert j['scan_sha256']==s['sha256']
    raw=d['documents'][j['acceptance_receipt']]['text']
    assert j['acceptance_line'] in raw.splitlines()
    m=re.fullmatch(r'SEG (\d+) lo (\d+) hi (\d+) primes (\d+) witnesses (\d+) ap_sha256 ([0-9a-f]{64})',j['acceptance_line'])
    assert m and tuple(map(int,(m[1],m[2],m[3],m[5])))==(j['segment'],int(s['lo']),int(s['hi']),int(s['witnesses']))
    raw=d['documents'][j['witness_hash_receipt']]['text']
    matches=[l for l in raw.splitlines() if l.split()[-1].endswith(Path(j['witness']).name)]
    assert len(matches)==1 and matches[0].split()[0]==s['sha256']
print('PASS: all 3757 original acceptance and witness-hash receipts join the supplemental scan')
d=json.loads((R/'review/followup_logs/c13_custody_reconciliation.json').read_text())
for x in d['unchanged_calculation_inputs']:
    assert sha((R/x['path']).read_bytes())==x['current_sha256']==x['original_sha256']
for x in d['changed_metadata']:
    assert sha((R/x['path']).read_bytes())==x['current_sha256']!=x['original_sha256']
assert len(d['changed_metadata'])==3 and len(d['unchanged_calculation_inputs'])==9
print('PASS: C13 calculation-input bindings intact; three metadata mismatches explicitly retained')
print('ALL PASS (receipt and custody checks only; no new numerical-series or group-arithmetic replay)')
