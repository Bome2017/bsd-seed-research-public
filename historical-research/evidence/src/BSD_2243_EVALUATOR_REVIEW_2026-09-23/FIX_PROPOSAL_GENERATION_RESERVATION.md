# Proposed fix for Codex finding 1: generation reuse before the first checkpoint (NOT applied)

**Defect** (reproduced by Codex, `BSD_2243_ACC_CODEX_CHECK_2026-09-23/restart_probe/`). In `acc2243v2.c` v2.3, run mode sets GEN = 1 + the largest generation found among existing checkpoint *files*.
* A run that dies before writing its first checkpoint leaves no file.
* Its restart therefore reuses the same GEN, hence the same stream directories `stream_g<GEN>_w<ii>`, while orphaned children of the dead run may still be writing there.
* The consumed-bytes hash check keeps this fail-closed (a mixed file cannot pass). But restart isolation, which was the claim, fails, and work is lost.

**Proposed change** (small, run path only; accumulation and merge untouched):
1. After taking the run lock (flock, close-on-exec) and before any worker or stream child starts, **reserve** a generation:
   * GEN = 1 + max(generations in checkpoint names, generations in `gen_<NNN>.reserved` markers);
   * create `outdir/gen_<GEN>.reserved` with `O_CREAT|O_EXCL`, fsync it and fsync the directory;
   * refuse to run if this fails.

   Because the reservation outlives an early crash, every restart gets a fresh GEN.
2. **Belt and braces:** add the PID and a start timestamp to each stream directory name (`stream_g<GEN>_w<ii>_p<pid>`), so no two processes can ever share a scratch directory, even if an operator removes the markers.
3. Merge ignores `.reserved` markers and stream directories, as it ignores `.tmp` files today.

**Tests required before re-freeze:**
* crash **before the first checkpoint**, then an immediate restart while orphans still run: distinct stream directories, no FATAL, digest equal to the reference;
* **repeated** early crashes (two in a row), then completion;
* the existing R4a–R4d and R5-B/C tests re-run;
* the Codex restart probe replayed unchanged against the new binary.

**Afterwards:** an independent re-check of the changed run path by Codex, or another reviewer who did not write it.
