import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import signal
import subprocess
import time

ap = argparse.ArgumentParser()
ap.add_argument("stage")
ap.add_argument("cap", type=float)
ap.add_argument("marker")
ap.add_argument("--stack", default="2G")
a = ap.parse_args()
root = Path(__file__).resolve().parent
gp = "/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/gp"
script = root / (a.stage + ".gp")
command = ["/usr/bin/time", "-l", gp, "-q", "-f", "-s", a.stack, script.name]
seal = {
    "command": command,
    "script_sha256": hashlib.sha256(script.read_bytes()).hexdigest(),
    "wall_cap_seconds": a.cap,
    "completion_marker_expected": a.marker,
    "log_mode": "direct file descriptors",
    "timeout_scope": "new process group",
}
(root / (a.stage + ".seal.json")).write_text(json.dumps(seal, indent=2) + "\n")
start = time.monotonic()
with (root / (a.stage + ".out")).open("wb") as out, (
    root / (a.stage + ".err")
).open("wb") as err:
    proc = subprocess.Popen(
        command, cwd=root, stdout=out, stderr=err, start_new_session=True
    )
    (root / (a.stage + ".pid.json")).write_text(
        json.dumps({"process_group": proc.pid, "parent_pid": os.getpid()}) + "\n"
    )
    timed_out = False
    try:
        code = proc.wait(timeout=a.cap)
    except subprocess.TimeoutExpired:
        timed_out = True
        os.killpg(proc.pid, signal.SIGTERM)
        try:
            code = proc.wait(timeout=3)
        except subprocess.TimeoutExpired:
            os.killpg(proc.pid, signal.SIGKILL)
            code = proc.wait()
out = (root / (a.stage + ".out")).read_bytes()
err = (root / (a.stage + ".err")).read_bytes()
stderr = err.decode(errors="replace")
rss = re.search(r"(\d+)\s+maximum resident set size", stderr)
error = bool(
    re.search(
        r"\*\*\*.*(overflows|error|alarm|precision too low|not a function|attempt to)",
        stderr,
    )
)
receipt = {
    **seal,
    "elapsed_seconds": time.monotonic() - start,
    "exit_code": code,
    "timed_out": timed_out,
    "maximum_resident_set_bytes": int(rss.group(1)) if rss else None,
    "completion_marker": a.marker.encode() in out,
    "explicit_gp_error": error,
    "stdout_sha256": hashlib.sha256(out).hexdigest(),
    "stderr_sha256": hashlib.sha256(err).hexdigest(),
}
receipt["accepted"] = (
    code == 0
    and receipt["completion_marker"]
    and not timed_out
    and not error
)
(root / (a.stage + ".receipt.json")).write_text(json.dumps(receipt, indent=2) + "\n")
print(json.dumps(receipt, indent=2))
