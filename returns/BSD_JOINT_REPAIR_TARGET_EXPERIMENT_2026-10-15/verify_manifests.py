#!/usr/bin/env python3
"""Check every manifest in this return. Hash identity is not proof validation."""
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parent
count=0; summaries=[]
for manifest in sorted(root.rglob('MANIFEST.sha256')):
    entries=0
    for line in manifest.read_text().splitlines():
        if not line.strip():continue
        expected,name=line.split('  ',1)
        p=(manifest.parent/name).resolve()
        assert root in p.parents, (manifest,'outside return',name)
        assert p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest()==expected,(manifest,name)
        entries+=1;count+=1
    summaries.append({'manifest':str(manifest.relative_to(root)),'entries':entries})
print(json.dumps({'status':'MANIFESTS_VERIFIED','total_entries_with_nested_repetition':count,'manifests':summaries},indent=2))
