#!/usr/bin/env python3
"""Replay the bound full-source norm calculation in a fresh temporary directory."""
from pathlib import Path
import argparse
import hashlib
import itertools
import json
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent

def mul(matrix, vector):
    return tuple(sum(a*b for a, b in zip(row, vector)) % 3 for row in matrix)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--gp', default=shutil.which('gp'))
    args = ap.parse_args()
    if not args.gp:
        ap.error('Supply --gp /path/to/gp or put PARI/GP on PATH')
    gp = str(Path(args.gp).resolve())
    for item in json.loads((ROOT/'INPUT_BINDINGS.json').read_text()):
        assert hashlib.sha256((ROOT/item['path']).read_bytes()).hexdigest() == item['sha256']
    receipts = []
    with tempfile.TemporaryDirectory(prefix='bsd-complete-norm-') as temp:
        dst = Path(temp)
        shutil.copytree(ROOT/'inputs', dst/'inputs')
        for name in ['construct_norm.gp', 'check_certificate.gp', 'valuation_candidate.gp']:
            shutil.copy2(ROOT/name, dst/name)
        for case in ['1913b1', '389a1']:
            p = dst/case
            p.mkdir()
            for name in ['run.gp', 'check.gp', 'valuation.gp']:
                shutil.copy2(ROOT/case/name, p/name)
            processes = []
            for name, sentinel in [('run.gp', 'KERNEL_COMPLETE=1;'),
                                   ('check.gp', 'COMPLETE_NORM_CERTIFICATE_PASS'),
                                   ('valuation.gp', 'VALUATION_CANDIDATE_COMPLETE')]:
                r = subprocess.run([gp, '-fq', '-s128000000', '--default',
                                    'parisizemax=1000000000', name], cwd=p,
                                   text=True, capture_output=True, timeout=135)
                assert r.returncode == 0 and not r.stderr and sentinel in r.stdout, (name, r)
                processes.append({'script': name, 'stdout': r.stdout, 'stderr': r.stderr,
                                  'exit_code': r.returncode})
            names = ['norms.gp', 'norm_kernel.gp', 'norm_kernel.json', 'valuation_candidate.gpout']
            for name in names:
                assert (p/name).read_bytes() == (ROOT/case/name).read_bytes(), name
            d = json.loads((p/'norm_kernel.json').read_text())
            k = d['norm_kernel_in_scalar_basis']
            coeffs = itertools.product(range(3), repeat=d['kernel_dimension'])
            generated = {mul(k, v) for v in coeffs}
            allvectors = list(itertools.product(range(3), repeat=d['scalar_dimension']))
            zero = {v for v in allvectors if not any(mul(d['norm_rows'], v))}
            assert generated == zero and len(zero) == 3**d['kernel_dimension']
            receipts.append({'case':case, 'artifacts_byte_identical': names,
                             'independent_exhaustive_scalar_vectors':len(allvectors),
                             'kernel_vectors':len(zero), 'processes':processes})
    out = {'status':'FRESH_TEMP_REPLAY_AND_INDEPENDENT_CERTIFICATE_PASS',
           'gp_executable':gp, 'cases':receipts,
           'scope':'Exact norm kernels under retained complete sources. No new BNF or all-place membership replay.'}
    (ROOT/'REPLAY_RECEIPT.json').write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps({'status':out['status'], 'cases':[
        {k:v for k,v in r.items() if k != 'processes'} for r in receipts]},indent=2))

if __name__ == '__main__':
    main()
