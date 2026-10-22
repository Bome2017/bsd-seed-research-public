# 53B PREFLIGHT RETURN — Sha[53^∞] singleton witness at ℓ = 743, streaming mode (2026-10-01/02)

**Status: PREFLIGHT_PASS — package FROZEN, NOT LAUNCHED. STOPPED here as instructed.**
MANDATORY_CORRECTIONS_CODEX.md took precedence over the 53B brief throughout. No production, no pushes, no messages.
**Production needs both of these:** (1) Codex reviews `FROZEN_RUN_PACKAGE_p53_l743` (local commit a766881); (2) the user says
"go 53b", authorizing the target and the caps.

## 1. Answers to the five preflight items
| item | result |
|---|---|
| Qualify immutable-prefix reuse + streamed extension (known-answer handoff, restart, tamper) | **PASS.** 27/27 test ids pass on the final launcher (§3). The certified p23/ℓ47 run was reproduced byte-for-byte from sealed prefix 0..868 plus streamed segments 869..888, through two injected crashes. The unchanged checker returned NONZERO, c₂ = 103854. |
| J ≤ 4; measure the intended configuration; wall time against the caps | **J = 4 producers; engine W = 8 threads, counted separately.** Measured projection: **263 CPU-h central (254–301)** against the 350 cap. **Wall 2.6 days (59–77 h)** on an otherwise idle Mac. Peak new disk ≈ 1.7 GB against 40; floor 60 GB (183 GB free now). These are projections under the caps, not guarantees (§4). |
| Pin theorem profile, c₂ convention, receipt validation, PARAMS; checker compatibility or labeled adapter | **Pinned** (§5). The checker is **byte-identical to the p17 freeze** and its compatibility is **demonstrated** (§6). The only new trust-relevant code is the **labeled launcher adapter** `adapter/launch_stream.py`, audited in ADAPTER_AUDIT.md. |
| Build FROZEN_RUN_PACKAGE_p53_l743 | **Built** by builder v5, which is derived from v4 and refuses unless all evidence passes. 271 files, read-only, local git a766881, FREEZE_MANIFEST sha256 82a5d962… (§7). |
| Optional: price a shared 59/709 run with exact tmin | **Priced** (§8): tmin(709, LATDEN 4096) = 250,333,655,598. Production is shared at no extra cost; the extra engine is ≈ 32 CPU-h. This is a cost comparison only, not a direction to start 59. |

## 2. Brief items corrected or made precise
- **T.** The brief's "T = 262,568,508,022" is the tmin at LATDEN 4096; the frozen engine reproduces it exactly. The run
  cutoff under the v4 ¼-tail rule is the aligned **T = 15,651·2²⁴ − 1 = 262,580,207,615**: k = 15,651 segments, of which
  0..6444 are sealed and 6445..15650 (9,206) are streamed.
- **Launch configuration.** The brief's "J ≤ 10 workers" is superseded: J = 4, as the current orchestrator refuses J > 4
  (tested, T8). The engine's W = 8 threads are counted separately.
- **Payoff wording** follows the corrections. A NONZERO validated by the checker proves Sha[53^∞] = 0 at the retained grade
  and raises the conditional alternative to #Sha = 9 from 25,281 to **31,329**. A zero is inconclusive. A prediction
  mismatch is recorded separately. There is no automatic next auxiliary or prime.
- **Checker.** The brief said "byte-identical to the p17 freeze". That holds for the checker. The launcher cannot be the
  frozen `run_singleton.sh`, which runs the frozen engine on a stored corpus, so a labeled adapter replaces it.

## 3. Qualification suite (`preflight/C_suite/SUITE_RESULTS.json`, launcher sha256 6a805ac5…)
Small configuration: ℓ = 743, T = 2²⁸ − 1, prefix 0..11 sealed, stream 12..15. Reference: the **frozen arbcore 47d07f2e**.
At this T the checker returns INVALID only for lattice identification, as expected; every binding passed.
| id | test | result |
|---|---|---|
| S1 | clean run (J = 4) | msl.txt byte-identical to the frozen engine; 80/80 unit receipts = frozen END hashes; 12..15 regenerated = sealed record |
| S2 | crash in the prefix phase; launcher-only death (`--resume` refused while children live); crash in the block phase | byte-identical |
| S3 | crash after the handoff with the spool lost (J = 1) | lost segments regenerated, superseded receipts identical, byte-identical |
| S4 | SIGTERM to the launcher | exit 5, both groups dead, resume → byte-identical |
| T1 | 1-bit flip in a sealed prefix file (receipts intact) | engine FATAL "inline receipt"; exit 6; no process left; resume refused |
| T2 | forged sealed receipt | refused before anything runs (pinned prefix root) |
| T3 | published stream file tampered in the spool | FATAL inline receipt |
| T4 | engine checkpoint tampered between attempts | FATAL CKPT self-hash |
| T5 | producer failure (receipt dir unwritable) | ABORT → FATAL → exit 6; no process left; resume refused |
| T6 | frozen target without `STREAM_AUTHORIZED=yes` | refused, nothing written (also re-checked on the frozen package) |
| T7 / T8 | producer binary differs from pin / J = 5 | refused |
| T9 / T10 | resume with a changed CONFIG / resume of a completed run | refused; the original CONFIG completes byte-identical |
| T11 | SIGHUP with SIGHUP ignored at start (nohup) | ignored; completes byte-identical |
| **KA-L** | **certified p23/ℓ47** (T = 14,914,945,023): prefix 0..868 sealed + stream 869..888, J = 4, W = 8, crashes at checkpoints 128 and 864 | **msl.txt sha 97407c4f… = certified; 4,445 receipts = frozen; unchanged checker NONZERO, c₀ = 0, c₁ = 9430, c₂ = 103854 ≡ 9 (mod 23), root a83f42e3 = pinned; adapter 0 failures** |
| V0–V9 | `--verify-only` on renamed copies of the KA-L output: untouched control → NONZERO; edited engine receipt, edited verifier receipt, repointed or deleted prefix receipt link, leftover spool file, msl.txt edited, 15th PARAMS field, conflicting receipt, substituted engine binary | each → INVALID (exit 2) |
| C1 | the p17 checker's own 20 negative controls, replayed | 20/20 OK; the shared CONTROLS.json is unchanged |

**Boundary known answer at the real handoff:** segments 6441..6444, regenerated with the production TMAX by the J = 4
configuration, are bit-identical to the sealed record (SEG line, witness sha256, producer log).
**Sealed-prefix custody:** all 6,445 files were re-hashed against their receipts before and after the whole preflight,
with 0 mismatches and 0 changes (size, mtime, mode, inode, link count). The pinned roots reproduce: 6445 → 92cd0222…,
889 → a83f42e3…, 5854 → 9fc6b8e8….

## 4. Measurement of the intended configuration and the projection (`preflight/E_measure`, `preflight/F_model/MODEL.json`)
| quantity | measured |
|---|---|
| producer, all-in CPU per segment (apwit + wverify + checks), J = 4 | 94.2 s at 6441..6452 (under prefix-phase engine load), 87.5 s at 11043..11050, 91.0 s at 15643..15650; apwit 67–71 s; **no PARI fallback even at the top segment** |
| J = 4 throughput | 151 / 163 / 157 segments per hour |
| engine per pair at ℓ = 743, W = 8, alongside 4 producers | 95.3 ns (82.2 ns at ℓ = 311 without producers) |
| smooth block (single thread) | 0.80–0.85 s; 62,604 blocks |
| calibration against the certified p31/ℓ311 run | the harness model gives 26.4k CPU-s against 46.1k actual → factor 1.75 (blocks slow under 8-way load) |
| **projection** | production 230 CPU-h, engine 33 CPU-h (Batch C linear cross-check: 31) → **263 central, 254–301 range**; wall: production 58 h + block tail ≈ 3.2 h → **≈ 61 h (59–77 h)**; unit 0 ≈ 98 min, overlapped with production; peak new disk ≈ 1.7 GB |
| launcher cap settings derived from this | producer_cpu_factor 1.385 (measured all-in/apwit 1.32 × 1.05); engine model 36.5 CPU-h |

**Risk stated plainly:** heavy jobs from other sessions running at the same time inflate CPU-h as well as wall time,
because hyperthreads share cores. A ~40% inflation would push the total over 350. The launcher's pace check at every 10%
would then stop the run fail-closed. Run the production when the Mac is otherwise idle.

## 5. Pins (THEOREM_PROFILE.md, RECEIPT_CHAIN_DESIGN.md, config/)
- **Theorem profile:** Ota Thm 1.5/6.4 with 5.17, the audited singleton route. This is the Ota (good-prime) profile, not
  BH and not LCAP.
  - At p = 53: 53 ∤ 6N; 53 ∤ Tam = 16; a₅₃ = −6 (ordinary); #E(F₅₃) = 60 (not anomalous).
  - ℓ = 743: prime; 742 = 2·7·53, so v₅₃ = 1; 743 ∤ N; E(F₇₄₃) ≅ ℤ/388 × ℤ/2 (#776), so E(F₇₄₃)[53] = 0.
  - Checked with PARI 2.17.3 (`admissibility/`).
- **c₂ convention:** the pipeline convention of SINGLETON_SPEC v1 §3, not BH's c₂/2.
  - g = 5 is the smallest primitive root mod 743 and equals PARI `znprimroot(743)`, which the sealed prescreen used, so
    the sealed residue 20 is directly comparable.
  - Symbols use the ω₁ normalization and are identified in (1/1024)ℤ.
  - c₀ = 0 and c₁ ≡ 0 (mod 53) are enforced.
- **Receipt validation:**
  - R1: the prefix root over 0..6444 is pinned at 92cd0222…, re-derived from receipts with every file re-hashed.
  - R2: each streamed segment passes the verifier, witness, scan and segcheck bindings before it is published.
  - R3: the engine's running receipt chain is bound by its self-hashed checkpoints.
  - R4: post-run checks: engine apsha = verifier receipt for all 15,651 segments; the final checkpoint binds the whole
    receipt file; the spool is drained; the sealed prefix is unchanged. The checker then recomputes the root over all
    15,651 segments against the engine's AP_SEGROOT.
  - R5: preflight probe receipts for 24 extension segments (diagnostic only).
  - The full root cannot be pinned in advance, so the checker runs without `--pinned-segroot`. This is stated, not hidden.
- **PARAMS (14 fields, no LCAP):** `msl 0 -22735 0 106272484 0 743 6503188012738584 1 262580207615 16777216
  …/production/p53_l743/spool …/production/p53_l743/units 1024` (`config/PARAMS_EXPECTED.txt`).
- **Sealed prediction:** c₂ ≡ 20 (mod 53), ADDENDUM_3 sha256 d25bc54a…, bound by hash. The checker never reads it.

## 6. Checker compatibility (demonstrated) and the adapter label
- `singleton_check.py` (cdbb8f32…) and its test file, CONTROLS.json and run_singleton.sh are byte-identical to the p17
  freeze.
- The checker hashes whatever binary `--arbcore` names and compares it with the manifest; it pins no engine. arbstream
  writes the frozen 14-field PARAMS. The adapter supplies one combined receipts glob. KA-L shows the unchanged checker
  certifies a streamed run identically; V-tests show every binding still fires; C1 replays its 20 controls.
- **Acceptance = the checker's NONZERO AND the adapter's post-run checks, with 0 failures.** V1 and V4 show some
  tampering, for example an edited engine receipt, is caught only by the adapter.
- `adapter/launch_stream.py` (6a805ac5…) is **labeled as an adapter** and audited in ADAPTER_AUDIT.md: what it adds, the
  tests that cover each part, its known limits, and the defects found during development.

## 7. Frozen package `~/BSD_P53_L743_RUN_2026-10-01/FROZEN_RUN_PACKAGE_p53_l743` (local git a766881, not pushed)
- **Contents:**
  - bin/: arbstream 169bfa9f, apwit c21429cc, wverify_distinct 3b584567, and arbcore_frozen 47d07f2e (tmin only);
  - engine_src/ (source and diff), orch/, checker/, adapter/;
  - config/RUN_CONFIG.json (pins point inside the package) and PARAMS_EXPECTED.txt;
  - corpus/ (CORPUS_CHECK_6445, PINNED_ROOTS_v4_ext6445, PREFIX_PIN);
  - margin_probe/ (tmin files), prescreen/ (sealed predictions and candidates4), spec/, admissibility/;
  - preflight/ (suite results, measurement, model, custody snapshot, probes) and tools/;
  - PREREGISTRATION.md, THEOREM_PROFILE.md, RECEIPT_CHAIN_DESIGN.md, CAPS_AND_STOP_RULES.md, ADAPTER_AUDIT.md;
  - LAUNCH_COMMAND.txt, RESUME_COMMAND.txt, VERIFY_COMMAND.txt, FREEZE_MANIFEST.json.
- **Post-freeze checks:**
  - 271/271 manifest hashes match;
  - 0 writable files;
  - the frozen target was refused without authorization;
  - `production/` does not exist.
- **LAUNCH_COMMAND (NOT RUN):** `STREAM_AUTHORIZED=yes caffeinate -i nohup python3 …/adapter/launch_stream.py
  …/config/RUN_CONFIG.json …/production/p53_l743 > …/production/launch_attempt1.log 2>&1 &`.

## 8. Optional shared 59/709 pricing (MODEL.json; a cost comparison, not a direction to start 59)
- **Exact tmin and admissibility for (59, 709).**
  - tmin(709) is 237,639,840,640 at LATDEN 1024 and **250,333,655,598 at LATDEN 4096**, so aligned T = 250,349,617,151
    (14,922 segments).
  - Admissibility (PARI): 708 = 12·59, v₅₉ = 1; #E(F₇₀₉) = 696, ≅ ℤ/348 × ℤ/2; a₅₉ = −4; #E(F₅₉) = 64; g = 2.
- **Shared pass (53/743 + 59/709).**
  - 59's segments are a subset of 53's, so it adds **0 production**.
  - Its own engine costs ≈ 31.6 CPU-h.
  - Total ≈ **295 CPU-h central, 336 high**: close to the 350 cap.
  - About +3 h of wall time if the second engine's block tail runs after the first.
- **59/709 later, alone:** it must re-produce 6445..14921 → ≈ **244 CPU-h** (212 production + 32 engine). The shared pass
  saves ≈ 212 CPU-h (≈ 2.2 days).
- **Before any 59 run:**
  - a sealed MT prediction for (59, 709), which does not exist yet;
  - a **two-engine launcher**, because this adapter supports one engine (the orchestrator's shared mode was only tested
    on 389a1 in lane F4), i.e. a separately tested change;
  - its own frozen package and Codex review;
  - a cap decision;
  - the user's go.
- **Payoff:** only if both are NONZERO does the conditional alternative move to 33,489 = 9·61².

## 9. Findings
- **F1 (launcher, fixed):** the CPU estimator raced with the orchestrator's restart rule. The launcher crashed and its
  children ran on unsupervised. They finished correctly, and `--verify-only` accepted that output. Fixed with race-tolerant
  scans, a fail-closed exception path and signal handling.
- **F2 (launcher, fixed):** after a fail-closed stop, the unchanged orchestrator kills only its shells, so apwit/wverify
  stragglers ran on. The launcher now kills both process groups after any nonzero exit; T1 and T5 assert that nothing
  survives.
- **F3 (custody, not changed):** the sealed files for segments 0..3280 (P3/P13 runs) are owner-writable (rw-r--r--). Their
  integrity rests on the pinned root, the inline per-segment hash check and the custody snapshots, not on file modes.
  chmod'ing another run's sealed files was outside this task's scope.
- **F4:** the brief's T is the tmin (§2).
- **Harness only (no product impact):**
  - the first C1 replay relocated fixtures whose PARAMS record absolute paths; the FAIL is kept in the record and was
    superseded by a correct replay;
  - a T3 driver race;
  - a non-flushing `cut` in my result watcher.
- Development history: suite attempts 1–2 were stopped to fix F1, F2 and the nohup SIGHUP issue (the earlier attempts
  are kept in `preflight/C_suite_aborted_*`). Every test was re-run on the final launcher.

## 10. Resources used
- ≈ 4.7 CPU-h (a lower bound; crashed test attempts are only partly metered); 233 MB disk in this folder; $0.
- Test configurations ran at most J = 4 producers plus one engine. Outside the measured tests, at most one other local
  process ran at a time.
- Coefficient files produced for measurement were deleted; only receipts were kept, as probes.
- Nothing was written into `singleton_probe/`, `corpus_ext_6445` or the F4 folder; their hashes and mtimes were verified
  unchanged.

## 11. Not claimed
- No prime was settled, and the prediction is untested.
- The projection is a measured model under stated assumptions (MODEL.json), not a guarantee.
- The adapter is new code. It has a test suite and a self-audit, but no independent review yet.
- Prime-by-prime work is not FIN.

## 12. Manifest
`MANIFEST.sha256` in this folder covers every file except `.git` internals. Key hashes:
- FREEZE_MANIFEST.json 82a5d962…; package HEAD a766881be14e389dc1bff610a2624162c20d97b0
- adapter 6a805ac561bfa070…; builder v5 10d51987…; SUITE_RESULTS.json 18bd85b2…; MODEL.json d3725e32…
