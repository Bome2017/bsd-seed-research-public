#!/usr/bin/env python3
"""Copy this packet and rebind only its five authenticated input paths.

Does not execute arithmetic. Original execution scripts and receipts stay
unchanged. A new destination is mandatory.
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil

root = Path(__file__).resolve().parent
ap = argparse.ArgumentParser(description=__doc__)
ap.add_argument('destination', type=Path)
args = ap.parse_args()
dest = args.destination.resolve()
if dest.exists() or root == dest or root in dest.parents:
    raise SystemExit('Use a new destination outside the sealed packet.')
bindings = json.loads((root / 'inputs/BINDINGS.json').read_text())
for b in bindings:
    p = root / 'inputs' / b['name']
    assert p.stat().st_size == b['size']
    assert hashlib.sha256(p.read_bytes()).hexdigest() == b['sha256']
manifest = root / 'MANIFEST.sha256'
if manifest.exists():
    for line in manifest.read_text().splitlines():
        expected, name = line.split('  ', 1)
        p = (root / name).resolve()
        assert root in p.parents and p.is_file() and not p.is_symlink()
        assert hashlib.sha256(p.read_bytes()).hexdigest() == expected, name
shutil.copytree(root, dest)
changes = []
for p in sorted(dest.rglob('*.gp')):
    old = p.read_text()
    new = old
    for b in bindings:
        # All bound execution scripts are in arithmetic/ or review/.
        # Rejected preflights are kept as historical evidence, not replay targets.
        if 'rejected_' in str(p.relative_to(dest)):
            continue
        new = new.replace(b['retained_path'], '../inputs/' + b['name'])
    if new != old:
        p.write_text(new)
        changes.append({'path': str(p.relative_to(dest)),
                        'original_sha256': hashlib.sha256(old.encode()).hexdigest(),
                        'rebound_sha256': hashlib.sha256(new.encode()).hexdigest()})
(dest / 'REPLAY_PATH_BINDINGS.json').write_text(json.dumps({
    'status': 'PATHS_REBOUND_ONLY_NO_ARITHMETIC_RUN',
    'source': str(root), 'changes': changes,
    'original_manifests': 'Apply to original packet, not modified replay tree.'
}, indent=2) + '\n')
# GP write() appends. Preserve the saved evidence separately in the replay
# copy so the documented verifier sequence creates one fresh output object.
generated = ['replay_relative_result.gp', 'matrix_audit_input.gp',
             'replay_unit_kernel_result.gp', 'private_support_audit_input.gp']
recorded = dest / 'recorded_outputs'
recorded.mkdir()
for name in generated:
    p = dest / 'review' / name
    if p.exists():
        p.rename(recorded / name)
print(json.dumps({'destination': str(dest), 'scripts_rebound': len(changes),
                  'inputs_checked': len(bindings)}))
