#!/usr/bin/env python3
"""Verify the manifest adjacent to this script; custody only, no production."""
import hashlib
import json
from pathlib import Path, PurePosixPath

root = Path(__file__).resolve().parent
manifest = root / 'MANIFEST.sha256'
seen = set()
for line in manifest.read_text().splitlines():
    digest, rel = line.split('  ', 1)
    name = PurePosixPath(rel)
    if name.is_absolute() or '..' in name.parts or rel in seen:
        raise SystemExit('INVALID manifest path: ' + rel)
    seen.add(rel)
    path = root / rel
    if path.is_symlink() or not path.is_file():
        raise SystemExit('Missing or symlinked file: ' + rel)
    if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
        raise SystemExit('Hash mismatch: ' + rel)
print(json.dumps({'status': 'MANIFEST_PASS', 'entries': len(seen),
                  'scope': 'File identity only, not mathematical verification'}))
