#!/usr/bin/env python3
"""Prepare a fresh, dependency-checked replay; never modifies sealed arithmetic."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import uuid

ROOT = Path(__file__).resolve().parent
ARITH = ROOT / "arithmetic"
STAGES = [
    ("norm_screen", 120, "NORM_SCREEN_COMPLETE"),
    ("geometric_gcd", 120, "GEOMETRIC_GCD_COMPLETE"),
    ("geometric_rank", 120, "GEOMETRIC_RANK_COMPLETE"),
    ("geometric_units", 120, "GEOMETRIC_UNITS_COMPLETE"),
]
SOURCE_MAP = {
    "/Users/bsm/BSD_SEED_COMPLETE_BOUND_SCALING_2026-10-20/seed_five/nf.gp": "seed_nf.gp",
    "/Users/bsm/BSD_SEED_COMPLETE_BOUND_SCALING_2026-10-20/seed_five/field.gp": "seed_field.gp",
    "/Users/bsm/BSD_RELATIVE_UNIT_CLASS_ALTERNATIVE_2026-10-20/relative_source/fields.gp": "relative_fields.gp",
    "/Users/bsm/BSD_RELATIVE_UNIT_CLASS_ALTERNATIVE_2026-10-20/relative_source/nf12.gp": "nf12.gp",
    "/Users/bsm/BSD_RELATIVE_UNIT_CLASS_ALTERNATIVE_2026-10-20/relative_source/nf6.gp": "nf6.gp",
}
CALL = re.compile(r'\b(readvec|readstr|read|write1|writebin|write)\s*\(\s*("(?:[^"\\]|\\.)*")')
ANY_CALL = re.compile(r'\b(?:readvec|readstr|read|write1|writebin|write)\s*\(')
READS = {"read", "readvec", "readstr"}

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def inside(path: Path, base: Path) -> bool:
    try:
        path.resolve().relative_to(base.resolve())
        return True
    except ValueError:
        return False

def verify_manifest() -> dict[str, str]:
    entries = {}
    for line in (ARITH / "MANIFEST.sha256").read_text().splitlines():
        digest, name = line.split("  ", 1)
        p = ARITH / name
        if not re.fullmatch(r"[0-9a-f]{64}", digest) or not inside(p, ARITH):
            raise RuntimeError("Invalid arithmetic manifest entry")
        if name in entries or not p.is_file() or sha(p) != digest:
            raise RuntimeError(f"Arithmetic manifest mismatch: {name}")
        entries[name] = digest
    return entries

def verify_inputs() -> dict[str, dict]:
    records = json.loads((ROOT / "inputs/BINDINGS.json").read_text())
    result = {}
    for rec in records:
        p = ROOT / rec["path"]
        if not inside(p, ROOT / "inputs") or not p.is_file() or sha(p) != rec["sha256"]:
            raise RuntimeError(f"Input binding mismatch: {rec['path']}")
        if "bytes" in rec and p.stat().st_size != rec["bytes"]:
            raise RuntimeError(f"Input length mismatch: {rec['path']}")
        if p.name in result:
            raise RuntimeError("Duplicate input binding")
        result[p.name] = {"path": str(p.resolve()), "sha256": rec["sha256"]}
    for name in SOURCE_MAP.values():
        if name not in result:
            raise RuntimeError(f"Required portable input absent: {name}")
    historical = json.loads((ARITH / "INPUT_BINDINGS.json").read_text())
    for rec in historical:
        if rec["path"] in SOURCE_MAP:
            if result[SOURCE_MAP[rec["path"]]]["sha256"] != rec["sha256"]:
                raise RuntimeError("Portable input differs from executed source")
    return result

def prepare_sources(dest: Path, inputs: dict[str, dict]):
    generated = set()
    scripts, graph = {}, []
    for stage, _, _ in STAGES:
        name = stage + ".gp"
        source = (ARITH / name).read_text()
        calls = list(CALL.finditer(source))
        if len(calls) != len(ANY_CALL.findall(source)):
            raise RuntimeError(f"Unmatched/nonliteral file dependency in {name}")
        rewrites = []
        def replace(match):
            action = match.group(1)
            old = json.loads(match.group(2))
            if Path(old).is_absolute():
                if action not in READS or old not in SOURCE_MAP:
                    raise RuntimeError(f"Unmatched absolute file path in {name}: {old}")
                new = inputs[SOURCE_MAP[old]]["path"]
                kind = "bound_input"
            else:
                if Path(old).name != old or old in {".", ".."}:
                    raise RuntimeError(f"Unsafe relative dependency in {name}: {old}")
                if action in READS:
                    if old not in generated:
                        raise RuntimeError(f"Transitive dependency lacks earlier producer: {name}: {old}")
                    kind = "earlier_stage_output"
                else:
                    generated.add(old)
                    kind = "fresh_output"
                new = str((dest / old).resolve())
            rewrites.append({"action": action, "old": old, "new": new, "kind": kind})
            return match.group(0)[:match.start(2)-match.start()] + json.dumps(new, ensure_ascii=False)
        transformed = CALL.sub(replace, source)
        # Reject remaining unrecognized absolute string paths, even outside known APIs.
        for quoted in re.findall(r'"(?:[^"\\]|\\.)*"', transformed):
            value = json.loads(quoted)
            if value.startswith("/"):
                allowed = {v["path"] for v in inputs.values()} | {str((dest / n).resolve()) for n in generated}
                if value not in allowed:
                    raise RuntimeError(f"Unmatched absolute string in {name}: {value}")
        scripts[name] = transformed
        graph.append({"script": name, "source_sha256": sha(ARITH/name),
                      "prepared_sha256": hashlib.sha256(transformed.encode()).hexdigest(),
                      "file_dependencies": rewrites})
    return scripts, graph, sorted(generated)

RUN_ALL = r'''#!/usr/bin/env python3
import json, os
from pathlib import Path
import re, shutil, subprocess, sys
root=Path(__file__).resolve().parent
receipt=json.loads((root/"PREPARATION_RECEIPT.json").read_text())
gp=os.environ.get("BSD_GP") or receipt.get("configured_gp") or shutil.which("gp")
if not gp: raise SystemExit("Set BSD_GP to the PARI/GP 2.17.3 executable")
version=subprocess.run([gp,"--version-short"],capture_output=True,text=True,timeout=5,check=True).stdout.strip()
if not re.match(r"^2\.17\.3(?:\D|$)",version): raise SystemExit("Replay requires recorded PARI/GP 2.17.3; got "+version)
for name in receipt["generated_outputs"]:
    if (root/name).exists(): raise SystemExit("Refusing appended/stale output; prepare a new directory: "+name)
env=dict(os.environ,BSD_GP=gp)
for stage,cap,marker in receipt["stages"]:
    subprocess.run([sys.executable,str(root/"run_streaming_profile.py"),stage,str(cap),marker,"--stack","512M"],cwd=root,env=env,check=True)
    result=json.loads((root/(stage+".receipt.json")).read_text())
    if not result.get("accepted"): raise SystemExit("Stage not accepted: "+stage)
print("ALL_FOUR_REPLAY_STAGES_ACCEPTED")
'''

def portable_runner() -> str:
    source = (ARITH/"run_streaming_profile.py").read_text()
    old = 'gp = "/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/gp"'
    if source.count(old) != 1:
        raise RuntimeError("Unrecognized runner runtime declaration")
    source = source.replace("import signal\n", "import signal\nimport shutil\nimport sys\n")
    source = source.replace(old, 'gp = os.environ.get("BSD_GP") or shutil.which("gp")\nif not gp: raise SystemExit("Set BSD_GP to PARI/GP 2.17.3")')
    old_command = 'command = ["/usr/bin/time", "-l", gp, "-q", "-f", "-s", a.stack, script.name]'
    if source.count(old_command) != 1:
        raise RuntimeError("Unrecognized runner command")
    source = source.replace(old_command,
        'command = [gp, "-q", "-f", "-s", a.stack, script.name]\n'
        'if sys.platform == "darwin": command = ["/usr/bin/time", "-l"] + command\n'
        'elif Path("/usr/bin/time").exists(): command = ["/usr/bin/time", "-v"] + command')
    # Keep missing RSS honest on platforms with different time(1) output.
    return source

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dest", help="New subdirectory under this packet root")
    ap.add_argument("--gp", help="Optional PARI/GP 2.17.3 executable; no arithmetic is run")
    ap.add_argument("--check-only", action="store_true", help="Validate hashes/dependencies without creating files")
    args=ap.parse_args()
    entries=verify_manifest(); inputs=verify_inputs()
    requested=args.dest or ("replays/"+datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")+"-"+uuid.uuid4().hex[:8])
    dest=(ROOT/requested).resolve()
    if not inside(dest,ROOT) or dest==ROOT or any(inside(dest,ROOT/n) for n in ["arithmetic","inputs","review","theory"]):
        raise RuntimeError("Destination must be a fresh, unsealed subdirectory under packet root")
    if dest.exists(): raise RuntimeError("Destination already exists; choose a fresh directory")
    configured=None
    if args.gp:
        configured=shutil.which(args.gp) or str(Path(args.gp).expanduser().resolve())
        if not Path(configured).is_file() or not os.access(configured,os.X_OK):
            raise RuntimeError("--gp is not an executable file")
    scripts,graph,outputs=prepare_sources(dest,inputs)
    runner=portable_runner()
    compile(runner,"prepared run_streaming_profile.py","exec")
    compile(RUN_ALL,"prepared run_all.py","exec")
    receipt={"status":"PREPARED_NOT_EXECUTED","destination":str(dest),"configured_gp":configured,
             "arithmetic_manifest_sha256":sha(ARITH/"MANIFEST.sha256"),
             "manifest_entries_verified":len(entries),"inputs":inputs,"stages":STAGES,
             "scripts":graph,"generated_outputs":outputs,
             "runner_source_sha256":sha(ARITH/"run_streaming_profile.py"),
             "runner_prepared_sha256":hashlib.sha256(runner.encode()).hexdigest(),
             "runtime_note":"No GP process is started by this preparer; run_all requires 2.17.3."}
    if args.check_only:
        print(json.dumps({"status":"DEPENDENCIES_AND_HASHES_VALIDATED","manifest_entries":len(entries),"stages":len(STAGES),"outputs":len(outputs)}))
        return
    dest.mkdir(parents=True,exist_ok=False)
    for name,body in scripts.items(): (dest/name).write_text(body)
    (dest/"run_streaming_profile.py").write_text(runner)
    (dest/"run_all.py").write_text(RUN_ALL)
    (dest/"PREPARATION_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n")
    print(json.dumps({"status":"PREPARED_NOT_EXECUTED","directory":str(dest),"next_command":["python3",str(dest/"run_all.py")]}))

if __name__=="__main__": main()
