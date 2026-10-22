#!/usr/bin/env python3
"""Verify file custody only; no assertion of mathematical correctness."""
from pathlib import Path
import hashlib,json,sys
root=Path(__file__).resolve().parent
bad=[];count=0
for line in (root/'MANIFEST.sha256').read_text().splitlines():
    digest,name=line.split('  ',1);p=(root/name).resolve()
    if not p.is_relative_to(root):bad.append({'path':name,'error':'unsafe path'});continue
    if not p.is_file():bad.append({'path':name,'error':'missing'});continue
    actual=hashlib.sha256(p.read_bytes()).hexdigest();count+=1
    if actual!=digest:bad.append({'path':name,'error':'hash mismatch'})
print(json.dumps({'status':'FILE_CUSTODY_PASS' if not bad else 'FAIL','files_checked':count,
                  'failures':bad,'proves_seed_BSD':False},indent=2))
sys.exit(bool(bad))
