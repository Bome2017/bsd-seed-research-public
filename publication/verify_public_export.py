#!/usr/bin/env python3
"""Verify publication identity. Does not certify mathematical statements."""
from pathlib import Path
import hashlib,json,sys
root=Path(__file__).resolve().parent.parent
manifest=root/'publication/PUBLIC_MANIFEST.sha256'
errors=[];listed=set();checked=0
for line in manifest.read_text().splitlines():
 digest,name=line.split('  ',1)
 p=Path(name)
 if p.is_absolute() or '..' in p.parts or name in listed:
  errors.append(['unsafe_or_duplicate_path',name]);continue
 listed.add(name);f=root/p
 if not f.is_file() or f.is_symlink():errors.append(['missing_or_symlink',name]);continue
 if hashlib.sha256(f.read_bytes()).hexdigest()!=digest:errors.append(['hash',name])
 checked+=1
allowed={'publication/PUBLIC_MANIFEST.sha256','publication/VERIFICATION.json'}
actual={f.relative_to(root).as_posix() for f in root.rglob('*') if f.is_file() and '.git' not in f.relative_to(root).parts and '__pycache__' not in f.relative_to(root).parts}
for name in sorted(actual-listed-allowed):errors.append(['unlisted_file',name])
records=json.loads((root/'publication/SOURCE_BINDINGS.json').read_text())
for row in records:
 p=root/row['public_path']
 if not p.is_file():errors.append(['source_binding_missing',row['public_path']]);continue
 if hashlib.sha256(p.read_bytes()).hexdigest()!=row['public_sha256']:errors.append(['source_binding_hash',row['public_path']])
 if row['transformation']=='byte_identical' and row['source_sha256']!=row['public_sha256']:errors.append(['false_byte_identity',row['public_path']])
scan=json.loads((root/'publication/PRIVACY_SCAN.json').read_text())
if scan['status']!='PASS':errors.append(['privacy_scan_not_pass'])
result={'status':'PUBLIC_EXPORT_IDENTITY_VERIFIED' if not errors else 'FAIL','manifest_entries_checked':checked,'source_records_checked':len(records),'source_grades':'preserved; not mathematically recertified','errors':errors}
print(json.dumps(result,indent=2))
sys.exit(bool(errors))
