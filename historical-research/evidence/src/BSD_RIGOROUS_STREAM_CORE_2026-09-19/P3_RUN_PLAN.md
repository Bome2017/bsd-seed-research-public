# P3_RUN_PLAN: the p = 3 modular-symbol run (plus optional p = 7) on the rigorous core

**Status: PREPARED, NOT EXECUTED.**
- `p3plan/run_p3.sh` refuses to start on the seed unless `P3_AUTHORIZED=yes`. The guard was tested: exit code 2, no directory created.
- Launching is the operator's decision.
- Nothing here changes any merged label.

## 1. What the run produces

It produces exact modular symbols of the seed E (Δ > 0, Ω⁺ = ω₁ = 0.0280449015194364044483094…):
- **p = 3** (3 ∥ N, so the cusps b/3^k are unitary through W_{N/3}):
  - [b/81]^± for all 54 units b mod 81;
  - [b/27]^± for all 18 units b mod 27, as the U₃ cross-check.
- **p = 7** (optional; 7 ∤ N):
  - [b/49]^± for all 42 units b mod 49;
  - [b/7]^± (6 values), as the T₇ cross-check.

The symbols are written as exact fractions to `SYMBOLS_m<m>.txt`.

The downstream step is outside this plan: Lane 3's evaluator (`D_primes/src/weights.gp`) computes a_{4,2} mod 27 from [b/81]⁺. The theorem chain and its label are the architect's P3 gate and Lane 3 D §1(c).

## 2. Per-target parameters

The class sums use the table-free `arbcore msl` mode.

| target | M = gcd(m,N) | Q | s = −ε_Q | κ = 2π/(m√Q) |
|---|---|---|---|---|
| m = 81 | 3 | N/3 = 2167729337579528 | −w·a₃ = +1 (w = +1, a₃ = −1) | 1.666066460958481308·10⁻⁹ |
| m = 27 | 3 | N/3 | +1 | 4.998199382875443924·10⁻⁹ |
| m = 49 | 1 | N | w = +1 | 1.590086071377491651·10⁻⁹ |
| m = 7 | 1 | N | +1 | 1.113060249964244156·10⁻⁸ |

**Validation of the sign rule and u_b = (Qb)⁻¹ mod m at M = 3.** All 1 117 exact symbols matched on 9 curves (`validation/compare_val_output.txt`). This includes m = 9, 27, 81 on five curves with 3 ∥ N, covering both s = +1 (15a1, 24a1, 141a1) and s = −1 (57b1, 141d1). 24a1 has the seed's local pattern: 2³ ∥ N, 3 ∥ N non-split, w = +1.

## 3. Exact truncation

The criterion (O3, DESIGN.md) is |x_b − Re λ_T(b/m)/Ω⁺| ≤ 2·tail_MS(T)/Ω⁺ < (1 − 2⁻¹⁰)/(2·1024).
- tail_MS(T) is the elementary Hasse + divisor-sum bound, evaluated in Arb.
- The ball then contains at most one point of (1/1024)Z, the identification lattice of Lane 3 D §1(c) (corrected Wuthrich Prop. 1 with the merged v₂(c₀) ≤ 8 lemma).
- **The lattice is a theorem input, not something the run checks.** The U₃ and T₇ relations are internal consistency checks only.

T_min comes from `arbcore tmin` (`p3plan/tmin_seed.txt`). It is exact: the least integer T ≥ 1/κ, and the output also shows T_min − 1 fails. The run uses T = the least k·2²⁴ − 1 ≥ T_min, so every a_q segment is full and one verified data set serves all targets.

| target | T_min at 1/1024 | T used | (k) | T_min at 1/512 (reference) |
|---|---|---|---|---|
| m = 81 | 14 832 175 873 | 14 847 836 159 | 885 | 14 413 217 081 |
| m = 27 | 4 830 360 876 | 4 831 838 207 | 288 | 4 690 653 704 |
| m = 49 | 15 556 089 288 | 15 569 256 447 | 928 | 15 117 117 981 |
| m = 7 | 2 131 827 698 | 2 147 483 647 | 128 | 2 069 073 077 |

The tail at T_min(81) is 6.8402133548·10⁻⁶. The target was Ω⁺·(1023/1024)/4096 ≈ 6.84·10⁻⁶.

## 4. Pipeline (`p3plan/run_p3.sh`)

**Stage W: a_q, one work unit per 2²⁴-segment.** There are 885 segments for p = 3 alone and 928 with p = 7.
1. `apwit … s s+1 fast`: the untrusted producer, using the seed's 2-torsion BSGS and a PARI certificate.
2. `wverify wit … s s+1`: the independent verifier. It writes `ap_<s>.bin` and logs `ap_sha256`.
3. `shasum` of the witness file, which is kept if at least 60 GB is free (`KEEP_WIT`).
4. The done marker `seg/<s>.done`.

The stage runs through `xargs -P J` (default J = 12) and resumes by skipping segments that are done. Any failed certificate is FATAL and stops the stage, so it fails closed. An ERR trap logs the line.

**Stage A: `arbcore msl` per target.** It runs with W threads (default 12) at LATDEN = 1024.
- The work units are the Part-L segments (heaviest first) and the Part-S blocks of 2²² n.
- Each unit is write-once with a SHA-256 self-hash. `PARAMS` locks the parameters.
- Units are combined in a fixed order, so the output is bit-identical for any W. This was shown for l2 at T = 1.5·10⁸, W = 4 against W = 1.

**Stage C: `p3plan/p3_check.py`.** Every check must pass:
1. arbcore's a_q segment root equals the root of the verifier's per-segment hashes over the same segments;
2. the count identity #smooth + #pairs = T holds;
3. every plus and minus symbol is identified, meaning it is contained in the ball and the ball is narrower than 1/1024;
4. the exact relations hold, with a_p read from the verified file:
   - U₃: a₃[b/27] = Σ_{j<3}[(b+27j)/81];
   - T₇: a₇[b/7] = Σ_{j<7}[(b+7j)/49] + [0], with [0]⁺ = L(E,1)/Ω⁺ = 0 by the certificate's Step 1 and [0]⁻ = 0.

**Tests of the script (small curves only, never the seed):**
- 24a1 at m = 81, 27, 9: every symbol identified; U₃ holds with 36 + 12 identities.
- 37a1 at m = 49, 7: T₇ holds with 12 identities.
- All 168 output symbols equal Sage/eclib (`p3plan/p3test_vs_sage.txt`).
- The U₃ relation holds on all 240 reference instances and T₅ on all 24 (`validation/hecke_relation_check.txt`).

## 5. Cost

The model is calibrated on this host (i9-10910) from `p3plan/cost_model.txt`:
- **producer:** 25.8 µs per prime for q ≤ 1.5·10⁸ (seed run) and 65.5 µs at q ≈ 1.48·10¹⁰ (calibration segment). Fitted model: c(q) = 12.3 + 0.1525·q^{1/4} µs.
- **verifier:** 13.9 µs rising to 25.7 µs over the same range, linear in log₂ q.
- **msl:** 38.3 CPU-s at T = 1.5·10⁸ (seed, m = 25), scaled linearly in T with a 1.10 sieve factor.

| scope | primes | producer | verifier | msl | **total CPU-h** | wall at 12 workers (idle host) | RAM | disk |
|---|---|---|---|---|---|---|---|---|
| p = 3 (m = 81 + 27) | 6.64·10⁸ | 9.8 | 4.3 | 1.5 | **15.6** | ≈ 1.3 h | ≤ 0.4 GB (W); ≈ 2 GB (A) | ap 2.7 GB; witness 18.3 GB if kept |
| p = 3 and 7 (m = 81, 27, 49, 7) | 6.95·10⁸ | 10.3 | 4.5 | 2.9 | **17.8** | ≈ 1.5 h | same | ap 2.8 GB; witness 19.2 GB if kept |

- These are NUMERIC model figures with an uncertainty of about ±25%: two calibration points, and the wall time is sensitive to host load. Measured host load was about 3 during this task.
- Each Stage W unit takes about 65 s of CPU near the top. Each Stage A unit takes seconds. **A restart loses at most one unit per worker.**
- The largest single cost is the producer. It is not in the trust base, so it can be sped up freely (for example by reusing the BSGS order instead of re-factoring h) without re-auditing.
- Compare Lane 3 D: ≈ 14 CPU-h for Phase A + Tier 1′ with the double-precision driver. This plan also pays for the independent verification (4.3 CPU-h) and for enclosures.

## 6. Independent replay procedure

1. **Coefficients.** On any machine, rerun `wverify wit` on the kept witness files, or regenerate them with `apwit` (deterministic; witness-file root equality was shown at T = 1.5·10⁸). Compare every `ap_sha256` with `logs/ver_<s>.log`.
   - Soundness needs only the verifier: any valid witness set yields the same a_q.
2. **Engine.** Rerun `arbcore msl` for each target with a different W in a fresh directory. The `SDUMP` and `XB` lines must be byte-identical.
3. **Checks.** Rerun `p3_check.py`.
4. **Optional, not rigorous.** Rerun the LP5 double-precision driver at m = 81 on the same a_q. Expect agreement to about 10⁻¹⁶ relative, as at m = 25 (`runs/seed150M/logs/regression_m25_compare.txt`: max relative difference 6.2·10⁻¹⁷).

## 7. Launch command (operator only)

```
cd ~/BSD_RIGOROUS_STREAM_CORE_2026-09-19 && ./build.sh
P3_AUTHORIZED=yes J=12 W=12 nohup p3plan/run_p3.sh > runs/p3.out 2>&1 &
# with p = 7:
P3_AUTHORIZED=yes TARGETS="81:3:1 27:3:1 49:1:1 7:1:1" J=12 W=12 nohup p3plan/run_p3.sh > runs/p3.out 2>&1 &
```

Progress is in `runs/p3/logs/timeline.log`, the result in `runs/p3/P3_CHECK.txt` and the symbols in `runs/p3/SYMBOLS_m81.txt`.
