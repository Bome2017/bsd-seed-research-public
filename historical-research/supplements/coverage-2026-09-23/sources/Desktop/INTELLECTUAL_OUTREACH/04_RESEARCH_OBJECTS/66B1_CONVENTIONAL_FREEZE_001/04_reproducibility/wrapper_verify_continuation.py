#!/usr/bin/env python3
"""
Wrapper for 01_first_model/continuation_receipts/verify_continuation.py.

The retained script is byte-identical to the first model's original and hardcodes
`/mnt/data/pk66_independent/`, an absolute path from that model's own sandbox. Per the
freeze mandate the original is NOT edited. This wrapper stages the expected layout in a
temporary directory, runs the original unmodified, and reports its exit status.

Usage:  python3 wrapper_verify_continuation.py
"""
import re, shutil, subprocess, sys, tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC  = HERE.parent / "01_first_model" / "continuation_receipts"
ORIG = SRC / "verify_continuation.py"

text = ORIG.read_text(encoding="utf-8")
roots = sorted(set(re.findall(r"/mnt/data/[A-Za-z0-9_./-]+", text)))
print("absolute paths referenced by the unmodified script:")
for r in roots: print("   ", r)

with tempfile.TemporaryDirectory() as tmp:
    data = Path(tmp) / "mnt" / "data"
    # /mnt/data/pk66_continuation  == the continuation receipts directory (retained/ inside it)
    shutil.copytree(SRC, data / "pk66_continuation")
    # /mnt/data/pk66_independent/PRE_COMPARISON_RECONSTRUCTION.md == the first model's frozen file
    (data / "pk66_independent").mkdir(parents=True, exist_ok=True)
    shutil.copy2(SRC / "retained" / "PRE_COMPARISON_RECONSTRUCTION.md",
                 data / "pk66_independent" / "PRE_COMPARISON_RECONSTRUCTION.md")
    patched = Path(tmp) / "run_verify.py"
    patched.write_text(text.replace("/mnt/data/", str(data) + "/"), encoding="utf-8")
    print(f"\nstaged under {data}/ ; running the retained script with only its path prefix "
          f"rebound (no logic change)\n")
    r = subprocess.run([sys.executable, str(patched)], cwd=str(data / "pk66_continuation"),
                       capture_output=True, text=True)
    sys.stdout.write(r.stdout); sys.stderr.write(r.stderr)
    print(f"\nexit status: {r.returncode}")
    sys.exit(r.returncode)
