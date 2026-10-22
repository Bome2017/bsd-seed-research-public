#!/usr/bin/env python3
"""Join the published chunks after checking each hash; does not extract or run code."""
from pathlib import Path
import hashlib,json,sys
r=Path(__file__).resolve().parent;info=json.loads((r/'CLAUDE_SOURCE_ARCHIVE.json').read_text())
src=Path(sys.argv[1]) if len(sys.argv)>1 else r.parent/'archives'
out=Path(sys.argv[2]) if len(sys.argv)>2 else Path(info['archive'])
assert not out.exists(),'Choose a new output path; existing files are never overwritten.'
h=hashlib.sha256()
with out.open('xb') as f:
 for item in info['parts']:
  b=(src/item['name']).read_bytes();assert len(b)==item['bytes'] and hashlib.sha256(b).hexdigest()==item['sha256'],item['name']
  h.update(b);f.write(b)
assert h.hexdigest()==info['sha256'],'Joined archive digest mismatch'
print(json.dumps({'archive':str(out),'sha256':h.hexdigest(),'status':'HASH_VERIFIED_NOT_EXTRACTED'}))
