"""Check this supplement's manifest without executing any historical code."""
from pathlib import Path
import hashlib

root = Path(__file__).resolve().parent
manifest = root / 'MANIFEST.sha256'
expected = set()
for line in manifest.read_text().splitlines():
    digest, name = line.split('  ', 1)
    rel = Path(name)
    if rel.is_absolute() or '..' in rel.parts or name in expected:
        raise SystemExit('Invalid manifest path: ' + name)
    p = root / rel
    if p.is_symlink() or not p.is_file():
        raise SystemExit('Missing/nonregular file: ' + name)
    if hashlib.sha256(p.read_bytes()).hexdigest() != digest:
        raise SystemExit('Hash mismatch: ' + name)
    expected.add(name)
actual = {p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and p != manifest and '__pycache__' not in p.parts}
if actual != expected:
    raise SystemExit('Manifest coverage mismatch: ' + repr(actual ^ expected))
print('SUPPLEMENT_INTEGRITY_PASS:', len(expected), 'files; no mathematical replay performed')
