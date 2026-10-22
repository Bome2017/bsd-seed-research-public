#!/usr/bin/env python3
"""Replay supplied audit in disposable copies; never rewrite source evidence."""
from pathlib import Path
import ast
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "supplied/BSD_GITHUB_DELTA_AUDIT_2026-10-22"
HERE = Path(__file__).resolve().parent
PRIOR = HERE / "inputs/BSD_PRIMARY_TORSION_BOUND_2026-10-22"
JOINT = HERE / "inputs/BSD_JOINT_CLASS_CONTINUATION_2026-10-22"

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

for row in json.loads((HERE / "INPUT_BINDINGS.json").read_text()):
    assert digest(ROOT / row["packet_path"]) == row["sha256"]

before = {p.name: digest(p) for p in SOURCE.iterdir() if p.is_file()}
manifest = []
for line in (SOURCE / "MANIFEST.sha256").read_text().splitlines():
    expected, name = line.split(None, 1)
    name = name.lstrip("*")
    assert Path(name).parts == (name,), name
    actual = digest(SOURCE / name)
    assert actual == expected, name
    manifest.append({"file": name, "sha256": actual})
assert len(manifest) == 5
assert set(before) == {r["file"] for r in manifest} | {"MANIFEST.sha256"}

imports = {}
for script in ["check_numeric_claims.py", "check_algebra_claims.py"]:
    tree = ast.parse((SOURCE / script).read_text())
    modules = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            modules.extend(n.name for n in node.names)
        elif isinstance(node, ast.ImportFrom):
            modules.append(node.module)
    assert set(modules) <= {"fractions", "math", "pathlib", "json"}
    imports[script] = sorted(set(modules))

runs = []
for run in [1, 2]:
    with tempfile.TemporaryDirectory(prefix="bsd-delta-audit-") as td:
        work = Path(td)
        for p in SOURCE.iterdir():
            if p.is_file():
                shutil.copyfile(p, work / p.name)
        checks = []
        for script, output in [
            ("check_numeric_claims.py", "NUMERIC_CHECK_RESULTS.json"),
            ("check_algebra_claims.py", "ALGEBRA_CHECK_RESULTS.json"),
        ]:
            start = time.monotonic()
            result = subprocess.run([sys.executable, str(work / script)], cwd=work,
                                    capture_output=True, text=True, timeout=30)
            elapsed = time.monotonic() - start
            (HERE / f"RUN{run}_{script}.stdout.txt").write_text(result.stdout)
            (HERE / f"RUN{run}_{script}.stderr.txt").write_text(result.stderr)
            assert result.returncode == 0, (script, result.stderr)
            byte_equal = (work / output).read_bytes() == (SOURCE / output).read_bytes()
            semantic_equal = json.loads((work / output).read_text()) == json.loads((SOURCE / output).read_text())
            assert byte_equal and semantic_equal, output
            checks.append({"script": script, "exit_code": result.returncode,
                           "elapsed_seconds": round(elapsed, 6), "output": output,
                           "byte_equal": byte_equal, "semantic_equal": semantic_equal,
                           "sha256": digest(work / output)})
        runs.append({"run": run, "checks": checks})

numeric = json.loads((SOURCE / "NUMERIC_CHECK_RESULTS.json").read_text())
packing = json.loads((PRIOR / "theory/PRIMARY_PACKING_RESULT.json").read_text())
assert len(numeric["packing_prefixes"]) == len(packing["all_prefixes"]) == 13
for supplied, original in zip(numeric["packing_prefixes"], packing["all_prefixes"]):
    assert supplied["max_norm"] == original["max_norm"]
    assert supplied["pairs"] == original["pairs"]
    assert supplied["radius"] == list(map(int, original["radius_lower"]))
    assert supplied["computed_rank_upper"] == original["five_torsion_rank_upper"]
    assert supplied["computed_order_upper"] == original["torsion_order_upper_integer"]
gate = json.loads((JOINT / "sources/RECONSTRUCTION_GATE_CHECK.json").read_text())
for supplied, original in zip(numeric["precision_table"], gate["precision_gate_examples_not_observed_unit_indices"]):
    assert supplied["hypothetical_J"] == original["assumed_certified_unit_index_upper_J"]
    assert supplied["bits"] == original["sufficient_relative_binary_precision_bits"]
    assert supplied["decimal_digits"] == original["sufficient_relative_decimal_precision_digits"]

algebra = json.loads((SOURCE / "ALGEBRA_CHECK_RESULTS.json").read_text())
incidence = json.loads((JOINT / "theory/INCIDENCE_GATE_RESULT.json").read_text())
for supplied, original in zip(algebra["incidence_checks"], incidence["prime_checks"]):
    assert supplied["p"] == original["p"]
    assert supplied["N1_rank_mod_p"] == original["norm_rank"]
    assert supplied["operator_span_rank"] == original["orbit_map_span_dimension"]
    assert supplied["coordinate_kernel_dimension"] == original["kernel_dimension"]
    assert supplied["orbit_sizes"] == [r["size"] for r in original["pair_orbits"]]

after = {p.name: digest(p) for p in SOURCE.iterdir() if p.is_file()}
assert before == after
receipt = {
    "status": "SUPPLIED_AUDIT_REPLAYED_EXACTLY_WITH_RETAINED_INPUT_SCOPE",
    "python_version": sys.version,
    "manifest_entries_verified": manifest,
    "source_files": 6,
    "imports": imports,
    "runs": runs,
    "crosschecks": {
        "packing_rows_radii_ranks_exact_order_bounds": 13,
        "hypothetical_precision_rows": 4,
        "finite_incidence_cases": 5,
        "source_unchanged": True,
    },
    "comparison_bindings": [
        {"file": str(p.relative_to(ROOT)), "sha256": digest(p)} for p in [
            PRIOR / "theory/PRIMARY_PACKING_RESULT.json",
            JOINT / "sources/RECONSTRUCTION_GATE_CHECK.json",
            JOINT / "theory/INCIDENCE_GATE_RESULT.json",
        ]
    ],
    "scope": "Agent replay of supplied exact arithmetic and finite-algebra checks. No new number-field arithmetic, unit subgroup, class group, complete source bound, endpoint theorem, human review, or formal verification."
}
(HERE / "AUDIT_REPLAY_RECEIPT.json").write_text(json.dumps(receipt, indent=2) + "\n")
print(json.dumps({"status": receipt["status"], "manifest": 5, "runs": 2,
                  "crosschecks": receipt["crosschecks"]}, indent=2))
