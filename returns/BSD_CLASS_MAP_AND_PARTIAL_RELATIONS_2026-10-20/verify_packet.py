#!/usr/bin/env python3
"""Check custody only; this does not certify arithmetic or theorem hypotheses."""
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parent
checked = {}
for manifest in sorted(root.rglob("MANIFEST.sha256")):
    count = 0
    for line in manifest.read_text().splitlines():
        digest, name = line.split(maxsplit=1)
        target = (manifest.parent / name.removeprefix("*")).resolve()
        if not target.is_relative_to(manifest.parent.resolve()):
            raise SystemExit(f"Rejected manifest path: {name}")
        if not target.is_file():
            raise SystemExit(f"Missing file: {target}")
        actual = hashlib.sha256(target.read_bytes()).hexdigest()
        if actual != digest:
            raise SystemExit(f"Hash mismatch: {target}")
        count += 1
    checked[str(manifest.relative_to(root))] = count
if "MANIFEST.sha256" not in checked:
    raise SystemExit("Missing root manifest")
print(json.dumps({
    "status": "CUSTODY_VERIFIED",
    "manifest_entries": checked,
    "scope": "File identity only; not mathematical verification",
}, indent=2))
