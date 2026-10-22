#!/usr/bin/env python3
"""Custody plus portable downstream replays; no BNF/Fourier producer rerun."""
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

root = Path(__file__).resolve().parents[1]

def verify_manifest(base):
    records = []
    for line in (base / 'MANIFEST.sha256').read_text().splitlines():
        digest, rel = line.split('  ', 1)
        p = base / rel
        assert not p.is_symlink() and p.is_file(), rel
        assert p.resolve().is_relative_to(base.resolve()), rel
        assert hashlib.sha256(p.read_bytes()).hexdigest() == digest, rel
        records.append(rel)
    assert len(records) == len(set(records)), 'duplicate manifest entry'
    return len(records)

n = verify_manifest(root)
nested = verify_manifest(root / 'synthesis')
trials = []
with tempfile.TemporaryDirectory(prefix='bsd-joint-check-') as temp:
    copy = Path(temp) / 'packet'
    shutil.copytree(root, copy)
    for script, output in [
        ('synthesis/checks/distill.py', 'synthesis/DISTILLATION_DATA.json'),
        ('checks/independent_rank_check.py', 'checks/independent_rank_check.json'),
        ('checks/prime_features.py', 'checks/prime_features.json'),
    ]:
        expected = (root / output).read_bytes()
        process = subprocess.run([sys.executable, str(copy / script)],
                                 cwd=copy, capture_output=True, timeout=30)
        assert process.returncode == 0 and not process.stderr, (
            script, process.returncode, process.stderr.decode())
        assert (copy / output).read_bytes() == expected, output
        trials.append({'script': script, 'result': 'byte_identical'})
    script = 'controls/check_gl2_3.py'
    process = subprocess.run([sys.executable, str(copy / script)],
                             cwd=copy, capture_output=True, timeout=30)
    assert process.returncode == 0 and not process.stderr
    assert json.loads(process.stdout) == json.loads((root / 'controls/GL2_3.json').read_text())
    trials.append({'script': script, 'result': 'identical_group_enumeration'})

print(json.dumps({'status': 'PACKAGE_AND_DOWNSTREAM_REPLAY_PASS',
                  'manifest_entries': n, 'nested_manifest_entries': nested,
                  'replays': trials,
                  'scope': 'Hash custody and exact downstream arithmetic. '
                           'Consumes saved producer outputs. Fresh complete-source '
                           'BNF replay is separately documented in controls/REPLAY.json; '
                           'historical Fourier/symbol production is not replayed.'}, indent=2))
