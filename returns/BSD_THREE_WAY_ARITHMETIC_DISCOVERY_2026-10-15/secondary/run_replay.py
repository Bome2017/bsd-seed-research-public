#!/usr/bin/env python3
"""Strict, isolated replay; uses GP but never accepts stdout after GP errors."""
from pathlib import Path
import argparse, hashlib, json, os, shutil, subprocess, tempfile

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gp", default=os.environ.get("GP") or shutil.which("gp"))
    parser.add_argument("--output", default="REPLAY_RECEIPT.json")
    args = parser.parse_args()
    if not args.gp:
        parser.error("give --gp /path/to/gp or set GP")
    gp = Path(args.gp).resolve()
    base = Path(__file__).resolve().parent
    inp = json.loads((base / "INPUTS.json").read_text())
    for row in inp:
        f = base / row["path"]
        if f.stat().st_size != row["bytes"] or digest(f) != row["sha256"]:
            raise SystemExit("Input binding failed: " + row["path"])
    records = []
    with tempfile.TemporaryDirectory(prefix="bsd-secondary-") as d:
        work = Path(d)
        for row in inp:
            target = work / row["path"]
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(base / row["path"], target)
        for name in ["root_test.gp", "verify_roots.gp", "check_scaling.gp"]:
            shutil.copyfile(base / name, work / name)
        for script, marker in [
            ("root_test.gp", "COMPLETE;MS="),
            ("verify_roots.gp", "INDEPENDENT_DETERMINANT_NORM_PASS;ROWS=6"),
            ("check_scaling.gp", "SCALING_CONTROL_PASS;ROWS=5"),
        ]:
            command = [str(gp), "-fq", "-s", "128000000", "--default", "parisizemax=1000000000", script]
            r = subprocess.run(command, cwd=work, capture_output=True, text=True, timeout=60)
            # GP can return zero despite recoverable script errors. Reject every diagnostic.
            if r.returncode or r.stderr or marker not in r.stdout:
                raise SystemExit(json.dumps({"script":script,"returncode":r.returncode,"stdout":r.stdout,"stderr":r.stderr}))
            records.append({"script":script,"returncode":r.returncode,"stdout":r.stdout,"stderr":r.stderr})
        expected = (base / "root_test.out").read_text().split("COMPLETE;MS=")[0]
        if records[0]["stdout"].split("COMPLETE;MS=")[0] != expected:
            raise SystemExit("Actual rows differ from recorded result")
        if records[2]["stdout"] != (base / "check_scaling.out").read_text():
            raise SystemExit("Scaling controls differ")
        if digest(work / "ROOT_CERTIFICATES.gp") != digest(base / "ROOT_CERTIFICATES.gp"):
            raise SystemExit("Root certificate bytes differ")
        receipt={"status":"EXACT_COUNTERCONTROL_REPLAYED", "inputs_checked":len(inp),
                 "gp_executable_sha256":digest(gp), "root_certificate_sha256":digest(work / "ROOT_CERTIFICATES.gp"),
                 "executions":records, "scope":"First-descent norm/root test, not Cassels-Tate or nine-Selmer computation"}
    (base / args.output).write_text(json.dumps(receipt,indent=2)+"\n")
    print(json.dumps({"status":receipt["status"],"inputs_checked":len(inp),"cases":6,"independent_norm":"multiplication determinant"}))

if __name__ == "__main__":
    main()
