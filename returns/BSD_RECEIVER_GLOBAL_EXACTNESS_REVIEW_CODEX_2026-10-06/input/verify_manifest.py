#!/usr/bin/env python3
"""Verify package file hashes; this does not check the mathematical proof."""
from hashlib import sha256
from pathlib import Path

root = Path(__file__).resolve().parent
lines = (root/'MANIFEST.sha256').read_text(encoding='utf-8').splitlines()
verified = []
for line in lines:
    expected, name = line.split('  ', 1)
    target = (root/name).resolve()
    if not target.is_relative_to(root):
        raise SystemExit(f'Unsafe path: {name}')
    if not target.is_file():
        raise SystemExit(f'Missing: {name}')
    actual = sha256(target.read_bytes()).hexdigest()
    if actual != expected:
        raise SystemExit(f'Hash mismatch: {name}')
    verified.append(name)
actual_names = {str(p.relative_to(root)) for p in root.rglob('*')
                if p.is_file() and p.name != 'MANIFEST.sha256'
                and '__pycache__' not in p.parts}
if actual_names != set(verified):
    raise SystemExit('Manifest does not match the package inventory')
print(f'PASS: {len(verified)} package files; this is an integrity check only.')
