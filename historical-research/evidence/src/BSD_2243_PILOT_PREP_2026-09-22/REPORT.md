# 2243 capped-pilot preparation: report (2026-09-23)

**Scope.** p = 2243 only. **Nothing has been launched, nothing has been spent, and no full certificate has been started.** Sealed artifacts are untouched; every step is recorded in `STATE.json` and `RESUME.md`.

## 1. Certificate consequence (S1, `S1_RESULTS.md`)

**K ≢ 0 (mod 2243) ⟹ Sha(E/Q)[2243^∞] = 0**, with K = 1024·Z and Z = Σ_{b mod ±1} bal_p(2·C(ℓ(b), 3))·[b/p²]⁺. This is the depth-two coefficient a_{2,3} in the Stein–Wuthrich normalization, and it holds only if D1–D8 hold.

**K ≡ 0 establishes nothing**; the converse is not claimed.

**What was checked:**
* **The sign rule s = −w·a_M at M ≥ 5.** 24/24 checks pass, and 3 728 exact symbols are contained. The wrong-sign controls reject 24/24.
* **The split-case height.** PARI's extended regulator is calibrated 9/9 against p-adic BSD, including three rank-2 curves of the seed's shape. v_p(Reg_p) = 2.

**Open before any full run:**
* **D2:** the split Selmer comparison char(X_Gr) = T·char(X_cl), the extra-zero step.
* **D5:** an independent certificate that the split-case height regulator is nonzero.

**The payoff is modest even on success.** It is finite-prime progress at one of three bad primes and implies neither FIN nor BSD.

## 2. Accumulator: implementation and validation (S2, S5)

**What it is.** An exact fixed-point class-sum accumulator:
* i128 with 96 fractional bits, plus an exact error tally;
* linear fingerprints;
* cumulative checkpoints with tmp + fsync + rename and a SHA-256 trailer.

It was derived from the certified stream core; the arithmetic is verbatim and only the data flow is new. The S5 pipeline version, v2.3, adds:
* streaming a_q (produce → verify → accumulate → delete), with the verifier's hash checked against the bytes actually consumed;
* unit selection, shards and tags, and a run lock;
* DFT symbol extraction;
* chunk digests;
* a portable SHA-256 for Linux.

**Validation:**

| test | result |
|---|---|
| T1 | 16/16: 8 small curves, 3 648 exact eclib symbols contained |
| T2 | retained certified seed cases. At m = 27 and 81 **all 144 symbols equal the certified values**, and **a_{4,2} = 15480** exactly |
| T3 | bit-identical results across worker counts, crash and restart, and versions |

**S5 (v2.3) final validation, `S5_pipeline/tests/final_driver.log`: 24 PASS, 0 FAIL.** Details are in `S5_pipeline/S5_RESULTS.md`. Highlights:
* The streamed produce → verify → accumulate path gives the same class-sum digest as the certified a_q.
* Crash and restart, including restart from partial checkpoints over 3 generations, is bit-identical. So is recombination of shards pooled from separate directories.
* Every negative control is refused: corrupted, duplicated or missing checkpoints; wrong selection; a failing producer; a corrupted witness; a tampered a_q file.
* **At full 2243 scale** (m = 2243², T = T_run), the streamed, stored, crash/restart and shard paths all give one digest. The full-size merge (DFT 176 s, 5 028 806 symbols) has maximum symbol radius 4.878033·10⁻⁴, exactly the tail budget, against the 4.882812·10⁻⁴ identification threshold.

**Five defects were found and fixed before any spend.**
* Defects 1, 2, 3 and 5 fail closed or cost only throughput, but 1 and 2 would each have wasted the full run.
* **Defect 4 was a correctness hazard.** In a narrow crash-and-restart race, two writers sharing one stream directory could leave zero-filled holes in an a_q file of the right length, and the pre-fix engine would have consumed it silently. Two independent guards now close it.
1. **`acb_dft` inflates input radii 7·10⁶× at m = 2243²** (Bluestein/Rader). The v2 merge would have identified **no** symbol. Fixed: exact midpoints go into the transform, and the rounding is added once per symbol by an ℓ1 bound.
2. **`arb_div` adds about |x|·2⁻²⁸ to a wide symbol ball**, through reduced working precision. That eats the 4.8·10⁻⁷ margin for large symbols. Fixed: the radius is carried separately through the division.
3. **libc `system()` from worker threads ran serially on macOS.** Streaming was one producer at a time. Fixed with `posix_spawn`.
4. **Orphaned stream children of a killed run could share a directory with the restart.** Fixed with per-generation directories and a check that the consumed bytes' hash equals the verifier's hash.
5. **The run lock was inherited by stream children.** A restart after a crash was refused while orphans lived. Fixed with close-on-exec.

Probes and diagnostics are in `S5_pipeline/probe/`; S4 §6 has the error budget.

**Independent check:** not done yet. Codex is to review against the certified small cases; the self-contained request is `S5_pipeline/CODEX_CHECK_REQUEST.md`.

## 3. Cost: measured, component by component (S3, S4, `S4_cost/S4_COST_RECONCILIATION.md`)

Per-symbol exact identification at T_run = 3.912·10¹³ costs **110 623 local core-hours**. That is a single-thread hour on an i9-10910; the host is idle.

| component | local core-hours | share |
|---|---|---|
| production | 92 816 | 84% |
| verification | 14 469 | 13% |
| traversal | 1 848 | |
| kernel | 910 | |
| interval summation | 522 | |
| checkpoint writes | 57 | |
| merge + DFT | 0.2 | |

**Storage** is at most about 85 GB, all transient. The run streams: 5 TB of a_q and 35 TB of witnesses are never stored.

**Scalar-mode cutoffs cost more:** the nonzero-only screen is 173 588 (+57%) and exact scalar identification is 211 769 (+91%). Exact per-symbol identification stops earliest, and it yields K exactly, which also settles the nonzero question. Both tests are implemented in the merge.

**All-in (scenarios, not probabilities):**

| scenario | total |
|---|---|
| **central: AWS c7a spot, cloud cores as fast as this host** | **≈ $2.2k** |
| spot range | $1.4k–$3.9k |
| on-demand | $5.8k |
| worst (on-demand, slow cores) | $8.1k |

The central case takes about 3.7 days on 20 × 64 cores. **The purchase metric** is about $0.001 per fully verified, accumulated top-range chunk at spot, and $0.0028 on-demand. This host alone would need about 11.5 months.

The dominant uncertainties are the pricing mode (the purchaser's choice) and the cloud per-core speed f, which the pilot measures.

**Not assumed:** GPU speedups, which are unbenchmarked, and Aristotle as a compute cluster.

## 4. The proposed pilot (`S5_pipeline/pilot/PILOT_PROPOSAL.md`)

**Machine and cap.** One AWS c7a.16xlarge (64 physical Genoa cores) at spot. The instance terminates itself after 5 h. A launcher ledger enforces a **hard cap of $100 by construction**. The planned spend is ≤ $50 worst case and about $3–7 expected.

**Stages:**

| stage | content |
|---|---|
| P1 | certified replay: full m = 27 and m = 81 runs from scratch, bit-identical to the local digests; a_{4,2} = 15480 |
| P2 | component rates at 4 heights under load |
| P3 | the 2243-scale data flow with crash, restart and shards; digests equal to the local R5 digests; the full-size symbol-radius budget |
| P4 | sustained streaming throughput with a kill -9 of the whole process group, giving **measured $ per chunk** |

**Deliverable:** f measured, and the S4 model re-run with cloud rates.

**Scripts:** `make_bundle.sh`, `launch_aws.sh` (a dry run unless given `--launch`), `bootstrap.sh`, `pilot_run.sh`, `fetch_results.sh` and `parse_cloud_rates.py`.

## 5. What is being asked

**Authorization for the capped pilot only: ≤ $100 hard cap, one instance at a time.** It needs your AWS account; I hold no credentials.

**The full run is not requested.** Four things must come first:
* D2 and D5 discharged;
* the Codex check of the prototype;
* the pilot's measured f and $/chunk;
* your decision, knowing that a K ≡ 0 outcome proves nothing.
