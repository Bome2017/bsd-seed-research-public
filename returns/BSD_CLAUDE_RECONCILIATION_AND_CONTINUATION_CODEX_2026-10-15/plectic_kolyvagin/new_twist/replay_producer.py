#!/usr/bin/env python3
"""Replay exact producer in an empty temporary directory; require exact rows."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import time

base = Path(__file__).resolve().parent
gp = os.environ.get('GP_BIN') or shutil.which('gp')
if not gp:
    raise SystemExit('Set GP_BIN to a PARI/GP binary, or put gp on PATH.')
start = time.monotonic()
with tempfile.TemporaryDirectory(prefix='bsd-6465-exact-twist-') as d:
    run = subprocess.run([gp, '-fq', '-s', '128000000', '--default',
                          'parisizemax=1000000000', str(base/'exact_twists.gp')],
                         cwd=d, text=True, capture_output=True, timeout=180)
    assert run.returncode == 0
    assert run.stdout.rstrip().endswith('COMPLETE')
    errors = [s for s in run.stderr.splitlines()
              if s.strip() and 'Warning: increasing stack size' not in s]
    assert not errors, errors
    matches = {}
    for name in ('rows_83.gp', 'rows_107.gp', 'exact_symbol.gp'):
        raw = (Path(d)/name).read_bytes()
        matches[name] = {
            'byte_identical': raw == (base/name).read_bytes(),
            'sha256': hashlib.sha256(raw).hexdigest()}
    assert all(x['byte_identical'] for x in matches.values())
    print(json.dumps({'status': 'EXACT_REPLAY_MATCH', 'same_engine': True,
                      'fresh_empty_directory': True, 'outputs': matches,
                      'elapsed_seconds': round(time.monotonic()-start, 3),
                      'stderr': run.stderr}, indent=2, sort_keys=True))
