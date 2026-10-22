"""Verify the distributed packet, not omitted third-party source copies."""
from pathlib import Path
import hashlib, json

root = Path(__file__).resolve().parent
errors = []
listed = set()
for line in (root/'MANIFEST.sha256').read_text().splitlines():
    expected, name = line.split('  ', 1)
    path = root/name
    if not path.resolve().is_relative_to(root):
        raise ValueError('Unsafe manifest path')
    listed.add(name)
    if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
        errors.append(name)
actual = {p.relative_to(root).as_posix() for p in root.rglob('*')
          if p.is_file() and p != root/'MANIFEST.sha256' and '__pycache__' not in p.parts}
errors += ['unlisted: '+n for n in sorted(actual-listed)]
print(json.dumps({'status':'PASS' if not errors else 'FAIL',
                  'members_checked':len(listed), 'errors':errors},indent=2))
raise SystemExit(bool(errors))
