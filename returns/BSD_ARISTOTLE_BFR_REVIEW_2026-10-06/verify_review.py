"""Verify custody and receipt consistency; does not replay or prove BFR."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent


def verify_manifest(path, base):
    checked = 0
    for line in path.read_text().splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        digest, name = line.split("  ", 1)
        rel = Path(name)
        assert not rel.is_absolute() and ".." not in rel.parts, name
        file = base / rel
        assert file.is_file() and not file.is_symlink(), name
        assert hashlib.sha256(file.read_bytes()).hexdigest() == digest, name
        checked += 1
    return checked


count = verify_manifest(ROOT / "MANIFEST.sha256", ROOT)
original_count = verify_manifest(
    ROOT / "original_return/research_return/MANIFEST.sha256",
    ROOT / "original_return",
)
assert original_count == 21
replay = json.loads((ROOT / "checks/LEAN_REPLAY.json").read_text())
assert replay["all_four_passed"]
audit = json.loads((ROOT / "checks/AUDIT_LEAN_REPLAY.json").read_text())
assert audit["exit_code"] == 0
axioms = (ROOT / "checks/FRESH_AXIOM_AUDIT.txt").read_text()
assert "sorryAx" not in axioms
lines = re.findall(r"^'([^']+)' depends on axioms: \[([^\]]*)\]$", axioms, re.M)
targets = json.loads((ROOT / "checks/AXIOM_TARGETS.json").read_text())
assert [name for name, _ in lines] == targets
allowed = {"propext", "Classical.choice", "Quot.sound"}
for name, ax in lines:
    assert {a.strip() for a in ax.split(",") if a.strip()} <= allowed, name
controls = json.loads((ROOT / "checks/PYTHON_REPLAY.json").read_text())
assert len(controls) == 3
assert all(c["exit_code"] == 0 and c["byte_matches"] for c in controls)
print(json.dumps(dict(status="CUSTODY_AND_RECEIPTS_VERIFIED",
                      review_manifest_entries=count,
                      original_research_entries=original_count,
                      axiom_declarations=len(lines),
                      does_not_prove_BFR=True), indent=2))
