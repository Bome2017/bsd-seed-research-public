#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path
import subprocess
import time

ROOT = Path(__file__).resolve().parent
GP = "/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/gp"
script = ROOT / "replay_fields_and_units.gp"
start = time.monotonic()
try:
    r = subprocess.run([GP, "-fq", "-s", "256000000", str(script)], cwd=ROOT,
                       capture_output=True, timeout=60)
    timed_out = False
    code, stdout, stderr = r.returncode, r.stdout, r.stderr
except subprocess.TimeoutExpired as e:
    timed_out = True
    code, stdout, stderr = None, e.stdout or b"", e.stderr or b""
(ROOT / "field_unit_replay.out").write_bytes(stdout)
(ROOT / "field_unit_replay.err").write_bytes(stderr)
result = {
    "script_sha256": hashlib.sha256(script.read_bytes()).hexdigest(),
    "elapsed_seconds": time.monotonic() - start,
    "outer_cap_seconds": 60,
    "timed_out": timed_out,
    "exit_code": code,
    "accepted": code == 0 and not timed_out and not stderr
                and b"INDEPENDENT_FIELD_UNIT_REPLAY_PASS" in stdout,
    "stdout_sha256": hashlib.sha256(stdout).hexdigest(),
    "stderr_sha256": hashlib.sha256(stderr).hexdigest(),
}
(ROOT / "FIELD_UNIT_REPLAY.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
if not result["accepted"]:
    raise SystemExit(1)
