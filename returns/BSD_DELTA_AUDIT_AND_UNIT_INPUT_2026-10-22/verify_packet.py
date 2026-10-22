#!/usr/bin/env python3
"""Custody and bounded isolated replay; no new arithmetic search."""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile

root = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument('--gp')
args = parser.parse_args()

def check_manifest(path):
    count = 0
    for line in path.read_text().splitlines():
        expected, name = line.split(None, 1)
        name = name.lstrip('*')
        rel = Path(name)
        assert not rel.is_absolute() and '..' not in rel.parts
        p = path.parent / rel
        assert p.is_file() and not p.is_symlink(), name
        assert hashlib.sha256(p.read_bytes()).hexdigest() == expected, str(p)
        count += 1
    return count

manifests = {str(p.relative_to(root)): check_manifest(p)
             for p in sorted(root.rglob('MANIFEST.sha256'))}
assert 'MANIFEST.sha256' in manifests
covered = {line.split(None, 1)[1].lstrip('*')
           for line in (root / 'MANIFEST.sha256').read_text().splitlines()}
actual = {str(p.relative_to(root)) for p in root.rglob('*') if p.is_file()}
assert actual - {'MANIFEST.sha256', 'VERIFICATION.json'} == covered
runs = []
with tempfile.TemporaryDirectory(prefix='bsd-delta-complete-replay-') as td:
    work = Path(td) / root.name
    shutil.copytree(root, work)
    commands = [[sys.executable, str(work / 'review/replay_supplied_audit.py')]]
    if args.gp:
        commands.append([sys.executable, str(work / 'source_recovery/replay.py'),
                         str(Path(args.gp).resolve())])
    for cmd in commands:
        cp = subprocess.run(cmd, cwd=work, capture_output=True, text=True, timeout=180)
        assert cp.returncode == 0, (cmd, cp.stdout, cp.stderr)
        assert not cp.stderr, cp.stderr
        runs.append(json.loads(cp.stdout))
print(json.dumps({'status': 'PASS', 'manifests': manifests,
                  'audit_replay': runs[0],
                  'gp_replay': runs[1] if len(runs) > 1 else 'SKIPPED',
                  'sealed_inputs_unchanged': True,
                  'scope': 'Exact replay using retained field inputs; no new complete seed bound'},
                 indent=2))
