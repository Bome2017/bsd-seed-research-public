#!/usr/bin/env python3
"""Verify custody and replay small exact checks. This is not proof certification."""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument("--quick", action="store_true", help="also replay four bounded Python arithmetic checks")
args = parser.parse_args()
counts = {}
for base in (ROOT, ROOT / "arithmetic", ROOT / "theory", ROOT / "review"):
    manifest = base / "MANIFEST.sha256"
    count = 0
    for line in manifest.read_text().splitlines():
        digest, rel = line.split(maxsplit=1)
        rel = rel.lstrip("*")
        path = (base / rel).resolve()
        assert path.is_relative_to(base.resolve()), f"unsafe manifest path: {rel}"
        assert path.is_file(), f"missing: {path}"
        assert hashlib.sha256(path.read_bytes()).hexdigest() == digest, f"hash mismatch: {path}"
        count += 1
    counts[str(base.relative_to(ROOT))] = count

for row in json.loads((ROOT / "inputs/BINDINGS.json").read_text()):
    path = ROOT / row["path"]
    assert path.stat().st_size == row["bytes"]
    assert hashlib.sha256(path.read_bytes()).hexdigest() == row["sha256"]

checks = []
if args.quick:
    pairs = [
        ("theory/certify_analytic_bound.py", "theory/EXACT_BOUND.json"),
        ("review/check_analytic_coarse.py", "review/ANALYTIC_COARSE_REVIEW.json"),
        ("review/parent_coarse_recombination.py", "review/PARENT_COARSE_RECOMBINATION.json"),
        ("review/check_line_norms.py", "review/NORM_REPLAY.json"),
    ]
    for script, result in pairs:
        run = subprocess.run([sys.executable, str(ROOT / script)], cwd=ROOT,
                             capture_output=True, text=True, timeout=30, check=True)
        assert not run.stderr, f"unexpected stderr: {script}"
        assert json.loads(run.stdout) == json.loads((ROOT / result).read_text()), script
        checks.append(script)

print(json.dumps({
    "status": "HASH_AND_REQUESTED_EXACT_REPLAYS_PASS",
    "manifest_entries": counts,
    "portable_field_inputs": 5,
    "exact_python_checks": checks,
    "proof_assistant_verification": False,
    "new_FIN_ORDER9_Q36_result": False,
}, indent=2))
