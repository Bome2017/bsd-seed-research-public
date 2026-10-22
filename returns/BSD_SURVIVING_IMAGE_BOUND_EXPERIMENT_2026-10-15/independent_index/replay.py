#!/usr/bin/env python3
"""Read-only isolated replay of the independent arithmetic bound inputs."""
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def replay_case(source):
    for binding in json.loads((source / 'INPUT_BINDINGS.json').read_text()):
        assert hashlib.sha256((source / binding['copy']).read_bytes()).hexdigest() == binding['sha256']
    with tempfile.TemporaryDirectory(prefix='bsd-independent-index-') as temp:
        dest = Path(temp)
        shutil.copytree(source / 'inputs', dest / 'inputs')
        for name in ['produce.gp', 'run.py']:
            shutil.copyfile(source / name, dest / name)
        run = subprocess.run([sys.executable, 'run.py'], cwd=dest,
                             capture_output=True, text=True, timeout=110)
        assert run.returncode == 0 and not run.stderr, (run.stdout, run.stderr)
        assert (dest / 'INDEX.json').read_bytes() == (source / 'INDEX.json').read_bytes()
        assert (dest / 'divisor_certificate.gp').read_bytes() == (source / 'divisor_certificate.gp').read_bytes()
        return {'case': source.name, 'status': 'BYTE_IDENTICAL',
                'index_sha256': hashlib.sha256((source / 'INDEX.json').read_bytes()).hexdigest(),
                'certificate_sha256': hashlib.sha256((source / 'divisor_certificate.gp').read_bytes()).hexdigest()}


if __name__ == '__main__':
    results = [replay_case(p) for p in [ROOT, ROOT / 'positive1913', ROOT / 'seed3_divisors']]
    run = subprocess.run([sys.executable, str(ROOT / 'verify_certificate.py')],
                         capture_output=True, text=True, timeout=210)
    assert run.returncode == 0 and not run.stderr, (run.stdout, run.stderr)
    assert json.loads(run.stdout) == json.loads((ROOT / 'LITERAL_REPLAY.json').read_text())
    print(json.dumps({'status': 'ISOLATED_PRODUCER_AND_LITERAL_REPLAY_PASS',
                      'cases': results, 'literal_checks': 'PASS',
                      'source_files_modified': False}, indent=2))
