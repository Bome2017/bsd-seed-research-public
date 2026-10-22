"""Check saved gate custody without rerunning any arithmetic producer."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent
stages = [
    "diagnosis",
    "smoke",
    "changed_seed",
    "profile_seed",
    "unmodified_small_base",
    "random_relations",
    "default_kc_count",
    "balanced_relations",
]
checked = []
for stage in stages:
    receipt = json.loads((root / (stage + ".receipt.json")).read_text())
    for suffix, key in [
        ("gp", "script_sha256"),
        ("out", "stdout_sha256"),
        ("err", "stderr_sha256"),
    ]:
        actual = hashlib.sha256((root / (stage + "." + suffix)).read_bytes()).hexdigest()
        assert actual == receipt[key], (stage, key)
    checked.append({"stage": stage, "accepted": receipt["accepted"]})
assert [
    row["stage"] for row in checked if row["accepted"]
] == ["smoke", "default_kc_count"]
for stage in ["random_relations", "balanced_relations"]:
    assert not (root / (stage + "_bnf.bin")).exists()
    receipt = json.loads((root / (stage + ".receipt.json")).read_text())
    assert not receipt["completion_marker"]
    assert receipt["explicit_gp_error"]
    assert receipt["elapsed_seconds"] < 180
print(json.dumps({
    "status": "RECEIPT_BINDINGS_VERIFIED",
    "checked": checked,
    "seed_bnf_completed": False,
    "scope": "saved output custody only; no arithmetic producer rerun"
}, indent=2))
