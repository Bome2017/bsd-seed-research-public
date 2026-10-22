#!/usr/bin/env python3
"""Read-only root replay. Work only in a temporary copy; emit a JSON receipt."""
from pathlib import Path
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent

def check_manifests(root):
    checked = 0
    for manifest in sorted(root.rglob('MANIFEST.sha256')):
        for line in manifest.read_text().splitlines():
            if not line.strip():
                continue
            digest, relative = line.split(maxsplit=1)
            path = manifest.parent / relative.lstrip('*')
            if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
                raise AssertionError(str(path))
            checked += 1
    return checked

def main():
    manifests = check_manifests(ROOT)
    steps = []
    with tempfile.TemporaryDirectory(prefix='bsd-surviving-bound-') as td:
        work = Path(td) / 'packet'
        shutil.copytree(ROOT, work)
        for rel in ['independent_index/replay.py',
                    'mirror_bound/replay.py',
                    'mirror_bound/positive1913/replay.py',
                    'source_screen/check_group_scope.py']:
            script = work / rel
            proc = subprocess.run([sys.executable, str(script)], cwd=script.parent,
                                  text=True, capture_output=True, timeout=120)
            if proc.returncode or proc.stderr:
                raise RuntimeError((rel, proc.returncode, proc.stdout, proc.stderr))
            steps.append({'script': rel, 'exit_code': proc.returncode,
                          'stdout': proc.stdout, 'stderr': proc.stderr})
        a = json.loads((work/'independent_index/INDEX.json').read_text())
        p = json.loads((work/'independent_index/positive1913/INDEX.json').read_text())
        s = json.loads((work/'independent_index/seed3_divisors/INDEX.json').read_text())
        assert a['A_global_upper_bound'] == 1+a['forward_tD']+a['B_S_class3_length'] == 2
        assert a['B_global_upper_bound'] == 1+a['reverse_tD']+a['A_S_class3_length'] == 3
        assert p['independent_global_upper_bound'] == 2
        assert p['forward_tD'] == 0 and p['source_class3_length'] == 0
        assert s['forward_tD'] == 1
    print(json.dumps({'status': 'PASS', 'manifest_entries_checked': manifests,
                      'root_readonly': True, 'steps': steps,
                      'upper_bounds': {'389a1': 2, 'mirror389': 3, '1913b1': 2},
                      'seed3_divisor_index': 1,
                      'seed_companion_class_bound': 'not_supplied',
                      'FIN': 'unchanged', 'ORDER9': 'unchanged', 'Q36': 'unchanged'}, indent=2))

if __name__ == '__main__':
    main()
