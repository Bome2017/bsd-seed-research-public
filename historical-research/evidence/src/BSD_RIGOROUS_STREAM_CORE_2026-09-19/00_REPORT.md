# 00_REPORT: rigorous streaming L-series / modular-symbol core (2026-09-19)

## RETURN: **RIGOROUS_STREAM_CORE_READY**

**What this task did:**
- Built a reusable rigorous engine: Arb/FLINT ball arithmetic, streaming, deterministic, with checkpoints. It is fed only by coefficients that an independent verifier has re-proved.
- **Goal B: analytic rank 2 recertified at proof grade.**
  - L″(E,1)/2 ∈ [35.929604, 35.941023]; zero is excluded.
  - Hence ord_{s=1} L(E,s) = 2, using L(E,1) = 0 (rank ≥ 1, Gross–Zagier–Kolyvagin) and w = +1.
  - Cost: 0.14 CPU-h, about 3 min wall.
- Prepared and tested the p = 3 run (and optional p = 7). The script refuses to start on the seed without `P3_AUTHORIZED=yes`.

**Not done, by instruction:** no p = 3 or p = 7 run, and nothing merged.

## Phases

| phase | result | evidence |
|---|---|---|
| **P0 design** | the objects enclosed, kernels, tails, witness format, summation order, rounding assumptions, written before code; a post-implementation addendum lists the additions | `DESIGN.md` |
| **P1 coefficient witnesses** | producer `src/apwit.c` (PARI plus the unchanged LP5 `fastap.c`, sha `7d3f4d51…`); **independent verifier** `verifier/wverify.c` (145 lines, integer-only, shares no producer code): segment tiling, trace certificates, Hasse bound, exhaustive small/bad primes, minimality (v_q(Δ) < 12), a_{p^e} recurrence, composite a_n by a multiplicative sieve, Merkle root. Round trips agree with PARI `ellap` (17 984 + 148 933 primes). **6/6 corrupted-witness tests rejected** | `runs/rt_test.sh`, `runs/negtest/` |
| **P2 Arb core** | `src/arbcore.c` (v3, 412 lines). Modes: `l2` (L″/2), `ms` (natural order), `msl` (table-free Part S/L, RAM independent of T; ready for m = 81, 49), `tmin` (exact truncation planner), `g2t` (unit test). No `M_PI`; no double in any enclosure (doubles only choose loop lengths and node indices, re-checked by an Arb range guard); `fegetround` asserted; write-once self-hashed units; parameter lock; fixed combination order | `src/`, `build.sh` |
| **P3 validation** | **192/192 checks pass**; 1 117 exact eclib symbols contained in both the ms and msl balls (see "Validation"); **7/7 engine negative tests detected** | `validation/`, `runs/negcore/` |
| **P4 seed run** | T = 1.5·10⁸: 8 444 396 a_q verified; a_n Merkle root equal in verifier and engine; **L″/2 ∈ [35.929604, 35.941023], zero excluded**; W = 1 replay (v3) bit-identical to the W = 4 run (v2); a full fresh-directory replay passes 9/9 | `ANALYTIC_RANK_CERTIFICATE.md`, `runs/seed150M/`, `certificate/` |
| **P5 p = 3 readiness** | exact T_min (Arb) for m = 81/27/49/7; cost calibrated at q ≈ 1.48·10¹⁰; guarded run script with checkpoints and a checker (segment roots, count identity, identification, exact U₃/T₇ relations); tested end to end on 24a1 and 37a1 (168/168 symbols equal to Sage) | `P3_RUN_PLAN.md`, `p3plan/` |

## Key numbers

**Seed analytic rank.**
- Partial sum: 2S_T = 35.9353137527517008919390307 ± 2.65·10⁻²⁶.
- Rigorous tail: ≤ 5.709008810·10⁻³.
- Ball dump: `8fbdc2e36e453517571bc5e5f9400837 -7a 17625463 -24`.
- Custody roots:
  - witness: `47f1cb43…`;
  - a_q segments: `916155fe…`;
  - a_n Merkle: `8c0b71cc…`.
- Lane 3's floating-point value 35.93531375315430 lies inside the ball.

**p = 3 plan.**
- T_min(m = 81, lattice 1/1024) = 14 832 175 873. The run uses T = 885·2²⁴ − 1.
- Cost: 15.6 CPU-h for p = 3 and 17.8 CPU-h with p = 7 (NUMERIC model, ±25%). That is about 1.3–1.5 h at 12 workers on an idle host.
- RAM ≤ 2 GB; the ap files take 2.7–2.8 GB.

**Regression against the old p = 5 pipeline** (seed, m = 25, n ≤ 1.5·10⁸, same a_q):
- The rigorous class sums from ms and msl agree.
- The LP5 double-precision A_k agree to 6.2·10⁻¹⁷ relative.
- So the earlier floating-point stream was numerically sound at this scale. It was just not enclosed.

## Validation (P3)

**L-values.**
- **G₂:** 200 000-point Taylor-model vs direct-series test with 0 failures, plus PARI quadrature inside the balls at 6 points.
- **L″/2 (`l2`):**

  | curve | rank | ball | reference |
  |---|---|---|---|
  | 389a1 | 2 | [0.759316500288426770 ± 3.4·10⁻¹⁹] | contains PARI 0.7593165002884267702… |
  | 446d1 | 2 | [0.940282604689620687 ± 1.7·10⁻¹⁹] | contains PARI 0.9402826046896206869… |
  | 234446a1 | 4 | [± 6.6·10⁻¹⁹] | contains 0 (negative control) |

**Modular symbols (`ms` and `msl`), on 9 curves:**
- M = 1:
  - 37a1 (w = −1), 389a1, 446d1 at m = 25, 5, 7, 27;
  - 234446a1 at m = 25, 5, 7, 27, against LP5 eclib, Wuthrich's published [1/7]⁻ and the new Sage run.
- M = 3 (3 ∥ N), at m = 9, 27, 81:
  - s = +1: 15a1, 24a1, 141a1;
  - s = −1: 57b1, 141d1.
- Every exact eclib [b/m]^± lies in both the ms and msl balls.
- **Identification:**
  - On the 7 curves whose symbols lie in ½Z, all 852 plus and 852 minus balls (50 runs) contain exactly one point of ½Z.
  - 15a1 and 24a1 have torsion of order 8 and symbols in ¼Z (for example 3/4 and −5/4). There the ½Z test correctly reports "not determined". At LATDEN = 4 every plus and minus symbol, m = 9, 27, 81, both modes, is determined (`validation/quarter_lattice_15a1_24a1.txt`). At LATDEN = 1024 the p3test run also identified every 24a1 symbol.
- Ω± balls contain PARI's periods.
- The a_n and a_q roots equal the verifier's.
- msl count identities hold.
- ms and msl class sums overlap.

**Hecke/U₃ relations on the reference symbols:** 240 + 24 identities hold. These are the Stage-C checks of the P3 plan.

**Negative tests.**
- *Verifier (P1)*, all rejected: wrong trace (a+2), wrong trace sign, deleted record, composite factor, shifted boundary, trailing byte.
- *Engine*: a corrupted a_q changes both roots and is detected. Also detected: truncated ap file, trailing bytes, parameter change on resume, corrupted checkpoint unit (self-hash), and gcd(Q, m) ≠ 1.
- *Wrong sign s*: only 4 of 20 plus balls land on lattice points (20 of 20 with the correct sign).

## Resources

**Caps:** ≤ 4 threads, ≤ 4 GB, analytic rank ≤ 2 CPU-h.

**Disclosed cap exceedance.** The single-process Sage reference job for the 234446a1 minus symbols was started at about 21:11 and stopped by me at 21:41:47 as non-essential (0.49 CPU-h). By then it had produced all 48 plus symbols of 234446a1 and no minus symbols. It overlapped two other activities:
- the 4-process seed pipeline, 21:12:44–21:15:34, so **5 processes ran for about 3 minutes**;
- briefly at 21:16:53: the W = 1 replay, the calibration and the 2-thread validation rerun, also 5 threads for about 10 s.

Sage's RSS reached 3.0 GB by 21:34; its RSS during the overlap was not recorded. Combined RAM therefore **may have exceeded 4 GB** while `wverify an` (1.37 GB) ran at 21:14:40. At all other times the load was ≤ 4 threads and < 4 GB. From 21:34 a watchdog stood ready to kill Sage above 3.5 GB; it peaked at 3.02 GB. The exceedance affected only resource use, not any result.

| item | CPU | peak RAM |
|---|---|---|
| seed certificate (producer, verifier, a_n root, l2) | 0.138 CPU-h | 1.37 GB (`wverify an`) |
| + two replays and two m = 25 regressions | ≈ 0.34 CPU-h total | 0.9 GB |
| validation (9 curves, all modes, twice: v2 and v3) | ≈ 20 CPU-s | < 0.1 GB |
| p = 3 calibration (one 2²⁰ segment at q ≈ 1.48·10¹⁰) | 4 CPU-s | 8 MB |
| Sage/PARI reference jobs | ≈ 0.5 CPU-h (the stopped 234446a1 sign −1 job dominates) | 3.0 GB (that job) |

## Scope and caveats (wording discipline)

1. **Proof-grade label.** The certificate is PROVED, computer-assisted, relative to the trust base in `ANALYTIC_RANK_CERTIFICATE.md` §7: FLINT/Arb 3.3.1, GMP, MPFR, the compiler, the 145-line verifier and the engine. The producer and PARI are **not** trusted.
2. **Hypotheses.**
   - L(E,1) = 0 comes from rank ≥ 1 via Gross–Zagier–Kolyvagin plus modularity.
   - w = +1 and the curve data are exact PARI computations (`certificate/hypotheses_output.txt`).
3. **Lattice.** The p = 3 identification lattice (1/1024)Z is a **theorem input** (Lane 3 D §1(c); corrected Wuthrich Prop. 1; merged v₂(c₀) ≤ 8 lemma). The run cannot verify it; the U₃ relation is only a consistency check.
4. **Scale.** msl has been exercised up to T = 1.5·10⁸, and at M = 3 only on small curves. The p = 3 run is the first use at T ≈ 1.5·10¹⁰. The cost table is a NUMERIC model, not a measurement.
5. **Minus symbols** use Ω⁻ = π/AGM(√(e₁−e₃), √(e₂−e₃)). They are validated against eclib sign −1 on 8 curves. On 234446a1 the minus side is checked only at Wuthrich's published [1/7]⁻ = 1: the Sage sign −1 space at level 234446 was stopped after 30 min without output (`validation/ref/sage_234446_err.txt`).
6. **Operational notes.**
   - The v2 certified run was allowed to finish when its parent script was stopped for the v3 swap (logged in `runs/seed150M/logs/timeline.log`).
   - Binary hashes change on every link (Mach-O LC_UUID). **Source hashes are the identity.** A rebuilt binary reproduced a validation output byte for byte.
   - The unused-function warning comes from the pinned LP5 `fastap.c`, which is deliberately unedited.
7. **Scope of the claim.** The certificate says nothing about Sha, changes no p-part label, and **nothing is merged**.

## Files

- `00_REPORT.md` (this file), `ANALYTIC_RANK_CERTIFICATE.md`, `P3_RUN_PLAN.md`, `DESIGN.md`
- `src/`: `arbcore.c` (engine), `apwit.c` + `fastap.c` (producer), `inc/` (PARI header symlinks)
- `verifier/`: `wverify.c`
- `validation/`: `run_val.sh`, `curves.txt`, `compare_val.py` + output, `tmin_validation.txt`, `g2*` tests, `hecke_relation_check.*`, `ref/` (Sage/PARI references and scripts)
- `certificate/`: hypotheses script and output, `replay_seed_l2.sh` + output
- `p3plan/`: `run_p3.sh`, `p3_check.py`, `tmin_seed.txt`, `cost_model.txt`, `p3test_vs_sage.txt`
- `runs/`: `seed150M` (witnesses, verified a_q, units, logs), `val`, `negtest`, `negcore`, `calib`, `p3test_24a1`, `p3test_37a1`, `t389`, `tseed`
- `logs/`: source history (v1, v2) and the v2 validation outputs
- Custody: `STATE.json`, `RESUME.md`, `TOOLCHAIN.txt`, `MANIFEST.sha256`
