# P5_REPLAY: replay status and procedure

## Replays performed on 2026-09-19 (after the pipeline finished; ≤ 16 workers)

| replay | what was re-executed | result | cost |
|---|---|---|---|
| **R-X** `downstream/cross_run_p3.py` | **cross-run**: this run's Stage W against the independent p = 3 run (same tiling), all 467 segments. Compared: the verifier SEG records, the verified a_q files re-hashed from disk, and the witness-file hashes | **467/467 byte-identical** on all three; a_q root over segments 0..466 equal (`fcd02437…`) in both runs | seconds |
| **R-W** `replay/replay_stageW_sample.sh` | 16 segments spread over [0, 466] (s = 0, 31, 62, …, 466). For each: the **independent verifier** re-run on the kept witness file, and the **producer** re-run from scratch | **32/32 byte-identical** (`replay/stageW_sample/RESULT.txt`) | 72 s wall, 0.28 CPU-h |
| **R-A25** `replay/replay_msl.sh` | the complete Stage A for m = 25 in a **fresh** directory with **W = 12** (certified run: W = 16) | **the complete output file is byte-identical** to `run/msl_m25.txt`: all 25 class-sum dumps, all 20 XB lines, roots, count identity. **The identified symbols and hence the coefficient residue are identical** | 352.5 s wall, 1.17 CPU-h, RSS 1.07 GB |
| **R-A5** same script | the complete Stage A for m = 5, fresh directory, W = 16 | **byte-identical** to `run/msl_m5.txt` | 71.9 s wall, 0.28 CPU-h |
| **R-D** downstream | a_{2,2} by the audited six-symbol formula (A) and an independent exact 5-adic evaluator (B), plus the LP5 comparison (C) | A = B = 2 (mod 5); C: 20/20 symbols and 152 equal | seconds |
| **R-I** `downstream/p5_integrity.py` | independent re-hash of all a_q and witness files; all 2 790 unit self-hashes; roots; PARAMS | INTEGRITY_PASS 19/19 | < 1 min |
| **R-N** PARI `primepi(7834959871)` | independent prime count | 360 542 141 = the verifier's total | 0.4 s |
| **Hashes** | every final artifact | `P5_MANIFEST.sha256`, verified after writing (see the report) | ≈ 1 min |

**Replay status: PASS.**

## Full independent replay procedure (for an auditor)

1. `cd ~/BSD_RIGOROUS_STREAM_CORE_2026-09-19 && shasum -a 256 -c MANIFEST.sha256 && ./build.sh`. The rebuilt binaries are byte-identical to the MANIFEST.
2. **Coefficients.** For each segment s < 467:

       verifier/wverify wit 0 -22735 0 106272484 0 7834959871 4096 16777216 <run>/wit <scratch> s s+1

   Then compare with `run/ap/ap_<s>.bin`. This is ≈ 2.1 CPU-h, verifier only; soundness needs only the verifier. Alternatively, regenerate the witnesses with `apwit … fast` (deterministic, ≈ 6.2 CPU-h).
3. **Symbols.**

       src/arbcore msl 0 -22735 0 106272484 0 25 6503188012738584 1 7834959871 16777216 <ap dir> <W> <fresh dir> 1024

   and the same with `5 … 1526726655`. The outputs must be byte-identical to `run/msl_m{25,5}.txt` for any W.
4. **Checks.** Run `p3plan/p3_check.py <run> 16777216 1024 0`, `downstream/p5_integrity.py run` and `downstream/p5_downstream.py run`.
