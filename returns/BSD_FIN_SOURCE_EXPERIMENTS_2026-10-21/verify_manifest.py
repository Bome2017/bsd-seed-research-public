#!/usr/bin/env python3
"""Check byte custody, not mathematical validity."""
from pathlib import Path
import hashlib
R=Path(__file__).resolve().parent
n=0
for line in (R/'MANIFEST.sha256').read_text().splitlines():
    expected,path=line.split('  ',1)
    p=R/path
    assert p.is_file(), path
    assert hashlib.sha256(p.read_bytes()).hexdigest()==expected, path
    n+=1
print(f'PASS_MANIFEST {n} files')
