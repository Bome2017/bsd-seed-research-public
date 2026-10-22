#!/usr/bin/env python3
"""Durable owner of the one D=-23 certificate attempt. No corpus mutation."""
from pathlib import Path
from datetime import datetime, timezone
import fcntl, hashlib, json, os, re, shutil, signal, subprocess, time

ROOT = Path(__file__).resolve().parent
AP = ROOT.parent / "active_full_bsd/p11/run/ap"

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def record(phase, **fields):
    state = json.loads((ROOT / "STATE.json").read_text())
    state.update(phase=phase, updated_utc=datetime.now(timezone.utc).isoformat(), **fields)
    tmp = ROOT / "STATE.json.tmp"
    tmp.write_text(json.dumps(state, indent=2) + "\n")
    tmp.replace(ROOT / "STATE.json")
    return state

def checkpoint(phase, **fields):
    state = record(phase, **fields)
    with (ROOT / "CHECKPOINTS.jsonl").open("a") as f:
        f.write(json.dumps({"time": state["updated_utc"], "phase": phase, **fields}) + "\n")

def verify_units(out, cutoff):
    nseg = (cutoff + 1) // 2**24
    nblk = (cutoff + 2**22 - 1) // 2**22
    source = json.loads((ROOT / "INPUT_BINDINGS.json").read_text())["segments"]
    paths = [out / f"lseg_{i:06d}.txt" for i in range(nseg)]
    paths += [out / f"blk_{i:06d}.txt" for i in range(nblk)]
    records = []
    for idx, p in enumerate(paths):
        raw = p.read_bytes()
        content, end = raw.rsplit(b"END ", 1)
        assert hashlib.sha256(content).hexdigest() == end.strip().decode(), p
        if idx < nseg:
            expected = source[idx]["coefficients"]["sha256"]
            assert f"apsha {expected}" in raw.split(b"\n", 1)[0].decode(), p
        records.append({"path": str(p), "sha256": digest(p), "bytes": len(raw)})
    expected_root = hashlib.sha256(b"".join(
        bytes.fromhex(s["coefficients"]["sha256"]) for s in source[:nseg]
    )).hexdigest()
    return records, expected_root

def main():
    lock = (ROOT / "supervisor.lock").open("w")
    fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    lock.write(str(os.getpid()) + "\n"); lock.flush()
    build = json.loads((ROOT / "BUILD_BINDINGS.json").read_text())
    for name, expected in build["sha256"].items():
        assert digest(ROOT / name) == expected, name
    validation = json.loads((ROOT / "VALIDATION_AND_BENCHMARK.json").read_text())
    assert validation["block_failures"] == 0 and validation["kernel_nonoverlap"] == 0
    checkpoint("RUNNING", supervisor_pid=os.getpid(), full_sum_launched=True,
               execution_rule="Validated adapter; initial 206 segments, at most one extension to 418 if needed")
    for cutoff in [3456106495, 7012876287]:
        out = ROOT / f"run_T{cutoff}"
        if not out.exists():
            out.mkdir()
        log = ROOT / f"run_T{cutoff}.log"
        timing = ROOT / f"run_T{cutoff}.time"
        cmd = ["/usr/bin/time", "-l", str(ROOT / "twist"), "run", str(cutoff),
               str(AP), "12", str(out)]
        # Benchmark PARAMS used a relative output path. Preserve that exact parameter.
        cmd[-1] = out.name
        start = time.monotonic()
        with log.open("w") as stdout, timing.open("w") as stderr:
            proc = subprocess.Popen(cmd, cwd=ROOT, stdout=stdout, stderr=stderr, start_new_session=True)
            checkpoint("RUNNING", engine_pid=proc.pid, cutoff=cutoff, output=str(out), log=str(log))
            last = -1
            while proc.poll() is None:
                count = len(list(out.glob("lseg_*.txt"))) + len(list(out.glob("blk_*.txt")))
                record("RUNNING", cutoff=cutoff, completed_units=count, elapsed_seconds=time.monotonic()-start)
                if count // 100 != last:
                    checkpoint("RUNNING", cutoff=cutoff, completed_units=count, elapsed_seconds=time.monotonic()-start)
                    last = count // 100
                if shutil.disk_usage(ROOT).free < 25 * 2**30:
                    os.killpg(proc.pid, signal.SIGTERM)
                    proc.wait()
                    raise RuntimeError("Free disk below 25 GiB; saved units retained")
                time.sleep(10)
            if proc.returncode:
                raise RuntimeError(f"Engine exited {proc.returncode}; inspect {timing}")
        records, expected_root = verify_units(out, cutoff)
        raw = log.read_text()
        assert f"AP_SEGROOT_SHA256 {expected_root}" in raw
        assert "identity 1" in raw
        # Fresh deterministic recombination, without rerunning the arithmetic stream.
        replay = subprocess.run([str(ROOT/"twist"), "combine", str(cutoff),
                                 str(AP), "12", out.name], cwd=ROOT, capture_output=True, text=True, check=True)
        (ROOT/f"combine_T{cutoff}.log").write_text(replay.stdout)
        assert raw.split("COUNT ",1)[1] == replay.stdout.split("COUNT ",1)[1]
        nonzero = "ZERO_EXCLUDED 1" in raw
        result = {
            "status": "TWIST_D23_NONZERO_CERTIFIED" if nonzero else "ZERO_NOT_EXCLUDED",
            "cutoff": cutoff, "unit_count": len(records),
            "coefficient_root": expected_root, "fresh_combine_matches": True,
            "interval": re.search(r"^LPRIME_INTERVAL (.*)$", raw, re.M)[1],
            "partial": re.search(r"^PARTIAL_2S (.*)$", raw, re.M)[1],
            "tail": re.search(r"^TAIL_BOUND (.*)$", raw, re.M)[1],
            "arithmetic_elapsed_seconds": time.monotonic()-start,
            "units": records, "build_bindings_sha256": digest(ROOT/"BUILD_BINDINGS.json"),
            "input_bindings_sha256": digest(ROOT/"INPUT_BINDINGS.json"),
            "engine_log_sha256": digest(log), "combine_log_sha256": digest(ROOT/f"combine_T{cutoff}.log"),
        }
        (ROOT/f"RESULT_T{cutoff}.json").write_text(json.dumps(result, indent=2)+"\n")
        checkpoint("VERIFIED_CUTOFF", cutoff=cutoff, nonzero=nonzero,
                   interval=result["interval"], fresh_combine_matches=True)
        if nonzero:
            (ROOT/"RESULT.json").write_text(json.dumps(result, indent=2)+"\n")
            checkpoint("COMPLETED", status=result["status"], interval=result["interval"],
                       cutoff=cutoff, full_sum_finished=True)
            return
    checkpoint("COMPLETED", status="TWIST_D23_ZERO_NOT_RESOLVED",
               full_sum_finished=True, successor_started=False)

if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        checkpoint("FAILED", error=repr(exc))
        raise
