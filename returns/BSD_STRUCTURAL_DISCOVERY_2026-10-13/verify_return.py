#!/usr/bin/env python3
"""Verify custody and accepted output; --gp PATH replays the portable certificate."""
import argparse, hashlib, json, pathlib, subprocess, sys

root = pathlib.Path(__file__).resolve().parent
args = argparse.ArgumentParser()
args.add_argument('--gp', help='Optional GP executable for fresh portable replay')
opt = args.parse_args()

def check_gp(out, err, marker):
    for line in err.splitlines():
        if line.strip() and 'Warning: increasing stack size to ' not in line:
            raise RuntimeError('Rejected GP diagnostic: '+line)
    if not out.rstrip().endswith(marker):
        raise RuntimeError('Missing final accepted marker')

manifest = root/'MANIFEST.sha256'
count = 0
if manifest.exists():
    for line in manifest.read_text().splitlines():
        digest, name = line.split('  ', 1)
        f = root/name
        if hashlib.sha256(f.read_bytes()).hexdigest() != digest:
            raise RuntimeError('Manifest mismatch: '+name)
        count += 1

seal = json.loads((root/'seed3/PREDICTION_SEAL.json').read_text())
if hashlib.sha256((root/'seed3/PREDICTIONS.md').read_bytes()).hexdigest() != seal['predictions_sha256']:
    raise RuntimeError('Prediction seal mismatch')
check_gp((root/'seed3/probe.out').read_text(), (root/'seed3/probe.err').read_text(), 'EXPERIMENT_COMPLETE')
check_gp((root/'checks/portable_unit.out').read_text(), (root/'checks/portable_unit.err').read_text(), 'PORTABLE_UNIT_CERTIFICATE_PASS')
check_gp((root/'checks/irreducible_source.out').read_text(), (root/'checks/irreducible_source.err').read_text(), 'NO_RATIONAL_3_ISOGENY_FROM_ORBIT')
sys.path.insert(0, str(root/'reviewer'))
from check_producer_matrices import run
_, actual = run(root/'seed3')
if actual['dimensions'] != {'valuation':0,'unit':1,'class':1}:
    raise RuntimeError('Unexpected actual filtration')

if opt.gp:
    got = subprocess.run([opt.gp,'-q','-D','parisizemax=1000000000','-f','verify_unit_portable.gp'],cwd=root/'checks',capture_output=True,text=True,timeout=110)
    if got.returncode:
        raise RuntimeError('GP process failed')
    check_gp(got.stdout,got.stderr,'PORTABLE_UNIT_CERTIFICATE_PASS')
    if got.stdout != (root/'checks/portable_unit.out').read_text():
        raise RuntimeError('Portable replay differs')

print(json.dumps({'status':'PASS','manifest_entries':count,'filtration':actual['dimensions'],'portable_replayed':bool(opt.gp),'scope':'Custody and exact outputs; class-group completeness remains conditional.'},indent=2))
