#!/usr/bin/env python3
"""Isolated standard-library replay of the sealed class-comparison arithmetic."""
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

root = Path(__file__).resolve().parent
with tempfile.TemporaryDirectory(prefix='bsd-class-comparison-') as temp:
    dst = Path(temp)
    shutil.copytree(root / 'inputs', dst / 'inputs')
    for name in ['compare.py', 'INPUT_BINDINGS.json']:
        shutil.copyfile(root / name, dst / name)
    run = subprocess.run([sys.executable, str(dst / 'compare.py')], cwd=dst,
                         capture_output=True, text=True, timeout=30)
    assert run.returncode == 0, run.stderr
    assert not run.stderr, run.stderr
    assert (dst / 'RESULTS.json').read_bytes() == (root / 'RESULTS.json').read_bytes()
    receipt = {
        'status': 'BYTE_IDENTICAL_ISOLATED_REPLAY',
        'results_sha256': hashlib.sha256((root / 'RESULTS.json').read_bytes()).hexdigest(),
        'stdout': run.stdout,
        'stderr': run.stderr,
        'returncode': run.returncode,
        'scope': 'F3 source-coordinate arithmetic only; antecedent arithmetic retained',
    }
    (root / 'REPLAY_RECEIPT.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt, indent=2))
