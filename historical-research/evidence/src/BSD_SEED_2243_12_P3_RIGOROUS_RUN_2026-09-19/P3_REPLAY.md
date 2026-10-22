# P3_REPLAY: replay status and procedure

## Replays performed on 2026-09-19 (after the pipeline finished, ≤ 16 workers)

| replay | what was re-executed | result | cost |
|---|---|---|---|
| **R-W** `replay/replay_stageW_sample.sh` | 16 segments spread over the whole range (s = 0, 58, 117, …, 884). For each: (1) the **independent verifier** re-run on the kept witness file into a scratch directory; (2) the **producer** re-run from scratch | **32 / 32 byte-identical**: 16 verified a_q files and 16 witness files (`replay/stageW_sample/RESULT.txt`) | 77 s wall, 0.30 CPU-h |
| **R-A81** `replay/replay_msl.sh` | the complete Stage A for m = 81 in a **fresh** unit directory with **W = 12** (certified run: W = 16) | **complete output file byte-identical** to `run/msl_m81.txt`: all 81 SDUMP class sums, all 54 XB lines, roots, count identity | 679 s wall, 2.25 CPU-h, RSS 1.07 GB |
| **R-A27** same script | the complete Stage A for m = 27, fresh directory, W = 16 | **byte-identical** to `run/msl_m27.txt` | 213 s wall, 0.92 CPU-h |
| **R-D** downstream | a_{4,j} by three independent routes: Lane 3's weight files; weights recomputed from scratch in Python; Lane 3's `an2` (gp, verbatim) | all agree: a_{4,2} = 15480 ≡ 9 (mod 27); a_{4,1} = −54; a_{4,0} = 0 | seconds |
| **R-I** `downstream/p3_integrity.py` | independent re-hash of all 885 a_q files (2.5 GB) and 885 witness files (17 GB); all 5 865 unit self-hashes; roots; PARAMS | INTEGRITY_PASS 19/19 | ≈ 1.5 min |
| **R-N** PARI `primepi(14847836159)` | independent prime count | 663 685 727 = the verifier's total | 2.5 s |

**Replay status: PASS.** Every replayed artifact is byte-identical, and every independent recount agrees.

## What a full independent replay requires

This is the procedure for an auditor; it was not executed in full tonight.

1. **Rebuild.** `cd ~/BSD_RIGOROUS_STREAM_CORE_2026-09-19 && shasum -a 256 -c MANIFEST.sha256 && ./build.sh`. The binaries are reproducible: the rebuilt ones are byte-identical to the MANIFEST.
2. **Coefficients, verifier only** (soundness needs only the verifier). For every segment s:

       verifier/wverify wit 0 -22735 0 106272484 0 14847836159 4096 16777216 <run>/wit <scratch> s s+1

   Then compare `<scratch>/ap_<s>.bin` with `run/ap/ap_<s>.bin`. The witness files are kept, 885 files (17 GB).
   - Cost ≈ 4.3 CPU-h.
   - Alternatively, regenerate the witnesses with `apwit … fast` (deterministic; ≈ 12.8 CPU-h at 16 workers) and verify those. Any valid witness set gives the same a_q.
3. **Symbols.** `src/arbcore msl 0 -22735 0 106272484 0 81 2167729337579528 1 14847836159 16777216 <ap dir> <W> <fresh dir> 1024`, and the same with `27 … 4831838207`. The output must be byte-identical to `run/msl_m{81,27}.txt` for any W. Cost ≈ 3.2 CPU-h.
4. **Checks.** `python3 p3plan/p3_check.py`, `downstream/p3_integrity.py` and `downstream/p3_downstream.py`, as in RESUME.md.
5. **Resume after an interruption** (the certified run was not interrupted): relaunch the same command (`prelaunch/LAUNCH_COMMAND.txt`), optionally with smaller J/W.
   - Done segments and complete, self-hashed units are skipped.
   - PARAMS refuses mixed parameters.
