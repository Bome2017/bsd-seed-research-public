#!/usr/bin/env python3
"""Custody and receipt checks only. Does not launch GP or certify mathematics."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_manifest(manifest):
    count = 0
    for line in manifest.read_text().splitlines():
        expected, name = line.split(maxsplit=1)
        name = name.strip().lstrip("*")
        path = (manifest.parent / name).resolve()
        assert path.is_relative_to(ROOT), name
        assert path.is_file(), name
        assert digest(path) == expected, name
        count += 1
    return count


manifests = {
    str(m.relative_to(ROOT)): verify_manifest(m)
    for m in sorted(ROOT.rglob("MANIFEST.sha256"))
}

lane = ROOT / "memory_diagnosis"
expected = [
    ("unmodified_small_base", 732577792),
    ("random_relations", 734720000),
    ("balanced_relations", 933396480),
]
for name, peak in expected:
    r = json.loads((lane / f"{name}.receipt.json").read_text())
    assert r["accepted"] is False
    assert r["completion_marker"] is False
    assert r["maximum_resident_set_bytes"] == peak
    assert digest(lane / f"{name}.out") == r["stdout_sha256"]
    assert digest(lane / f"{name}.err") == r["stderr_sha256"]
    assert digest(lane / f"{name}.gp") == r["script_sha256"]
    error_log = (lane / f"{name}.err").read_text()
    assert "alarm interrupt" in error_log
    assert "stack overflows" not in error_log
    assert "LIMC2 = 419775" in error_log
    assert not (lane / f"{name}_bnf.bin").exists()

assert 8 * 35749**2 == 10223928008
assert 8 * 5077**2 == 206207432
assert 8 * 721**2 == 4158728
state = json.loads((ROOT / "STATE.json").read_text())
assert state["complete_seed_unit_class_bound"] is False
assert state["bound_across_primes_proved"] is False
assert state["actual_seed_bnf_returned"] is False

print(json.dumps({
    "status": "CUSTODY_AND_RECEIPT_CONSISTENCY_PASS",
    "manifests": manifests,
    "seed_arithmetic_recomputed": False,
    "mathematical_proof_certified": False,
    "complete_bound_obtained": False,
}, indent=2))
