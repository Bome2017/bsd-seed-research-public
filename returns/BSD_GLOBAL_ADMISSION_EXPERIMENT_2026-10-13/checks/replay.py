"""Replay this return in a temporary copy, leaving the sealed evidence untouched.
Use --sage-python /path/to/Sage/python. No seed class-group job is launched.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--sage-python', required=True)
args = parser.parse_args()
sage = str(Path(args.sage_python).resolve())
jobs = [
    ('explicit', [(sage, 'admission.py'), (sys.executable, 'verify_local.py')],
     ['admission.json', 'independent_local.json']),
    ('seed', [(sage, 'principal_probe.py'), (sage, 'leak_repair.py'),
              (sage, 'line_source_probe.py'), (sys.executable, 'verify_line_source.py')],
     ['principal_probe.json', 'leak_repair.json', 'line_source_probe.json',
      'verify_principal.json', 'verify_line_source.json']),
    ('local_pairing', [(sage, 'check.py'), (sage, 'line_source.py')],
     ['RESULT.json', 'LINE_SOURCE.json']),
    ('duality', [(sage, 'local_row.py'), (sage, 'audit_quartic.py')],
     ['local_row.json', 'audit_quartic.json']),
]

with tempfile.TemporaryDirectory(prefix='bsd-admission-replay-') as temp:
    copy = Path(temp)/ROOT.name
    shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns(
        '__pycache__', 'sources', '*.pdf', 'REPLAY_RESULT.json'))

    def run(job):
        directory, commands, outputs = job
        receipts = []
        for runtime, filename in commands:
            start = time.monotonic()
            result = subprocess.run([runtime, filename], cwd=copy/directory,
                                    capture_output=True, text=True, timeout=120)
            receipts.append({'script': directory+'/'+filename,
                             'exit_code': result.returncode,
                             'seconds': round(time.monotonic()-start, 3),
                             'stderr': result.stderr[-2000:]})
            if result.returncode:
                raise RuntimeError(json.dumps(receipts[-1])+result.stdout[-2000:])
        comparisons = []
        for filename in outputs:
            old = (ROOT/directory/filename).read_bytes()
            new = (copy/directory/filename).read_bytes()
            same = old == new
            comparisons.append({'path': directory+'/'+filename,
                                'byte_identical': same,
                                'original_sha256': hashlib.sha256(old).hexdigest(),
                                'replayed_sha256': hashlib.sha256(new).hexdigest()})
            if not same:
                raise RuntimeError('Output changed: '+directory+'/'+filename)
        return {'directory': directory, 'runs': receipts, 'outputs': comparisons}

    # The duality audit reads the baseline explicit JSON in its own temporary
    # copy. Producers may rewrite that file, so run that audit after the others.
    with ThreadPoolExecutor(max_workers=2) as pool:
        results = list(pool.map(run, jobs[:3]))
    results.append(run(jobs[3]))

out = {'status': 'PASS', 'replayed_outputs': sum(len(j[2]) for j in jobs),
       'all_outputs_byte_identical': True, 'sage_python': sage,
       'python': sys.executable, 'jobs': results,
       'scope': 'Producer reruns plus separately implemented exact controls; '
                'not independent class-group software or formal verification.'}
(ROOT/'checks/REPLAY_RESULT.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({'status': out['status'], 'replayed_outputs': out['replayed_outputs']}))
