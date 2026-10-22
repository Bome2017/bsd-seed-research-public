# S4: all-in cost of the 2243 certificate stream, reconciled across cutoffs (2026-09-23)

Nothing here launches anything or spends money. All work figures come from **measured** rates:
* the S3 benchmark (single-thread, idle host);
* the S3b loaded-host test;
* the earlier feasibility measurements at q ≈ 3.9·10¹³ and 1.69·10¹⁴;
* exact-structure term counts computed from the verified a_q.

The **unit** is the local core-hour (lch): one single-thread hour on the measurement host (Intel i9-10910, 10 cores, 20 threads).

Scripts, all rerunnable:
* `term_counts.py`: exact L-pair and L-term counts;
* `parse_rates.py` → `rates.json`;
* `cost_model_s4.py` → `cost_s4.txt` / `cost_s4.json`;
* `allin.py` → `allin.txt`.

## 1. Measured rates (single thread, idle host)

| height q | producer (fixed) µs/prime | verifier µs/prime | source |
|---|---|---|---|
| ≈ 8.4·10⁶ (segment 0) | 21.35 | 11.42 | S3 |
| ≈ 1.0·10⁹ | 40.14 | 16.71 | S3 |
| ≈ 1.0·10¹¹ | 88.10 | 28.43 | S3 |
| ≈ 1.0·10¹³ | 233.07 | 38.51 | S3 |
| **3.912·10¹³ (top of the planned range)** | **320.55** | **43.90** | feasibility (fixed producer) |
| 1.687·10¹⁴ | 445.28 | 54.28 | feasibility |

* **Producer model.** The producer follows 20 µs + 0.118 µs·q^{1/4} within 2% at every point. The model interpolates the measured points; it does not use the fit.
* **Part L (accumulator), least squares over 5 measured sub-units:**
  * traversal 0.099 s per sub-unit + 1.27 ns per pair;
  * kernel 47 ns per prime + 99.9 ns per term;
  * interval (fixed-point) summation 113.7 ns per term.
* **Part S:** 0.55–0.70 s traversal per 2²²-block, 0.89–0.94 s in total, measured at n ≈ 10¹⁰, 10¹², 3.9·10¹³.
* **Checkpoint:** 80.5 MB written with fsync in 0.308 s.
* **Full-length DFT** (m = 5 031 049, 128 bits): 185 s.

### Loaded host (S3b)

S3b ran 30 top-range segments; every one verified.

| | producer throughput per core | verifier throughput per core |
|---|---|---|
| 10 processes, one per physical core | 0.914× single-thread | 0.888× |
| 20 processes, SMT | 1.331× | 1.520× |

Segment-to-segment spread at the top was < 0.5%.

**Term counts** (`term_counts.py`) come from the verified a_p. They reproduce the measured unit term counts to 0.02%; the difference is the primes with a_q = 0, which the engine skips. At T_run:
* 1.293·10¹² primes;
* 2.657·10¹³ Part-L pairs and 1.259·10¹³ Part-L terms;
* 9 326 908 Part-S blocks;
* 2 355 152 L sub-units at production UNIT_TERMS = 10⁹.

Segments 0–2047 have several sub-units and must be pre-produced, about 5.9 GB of a_q. Every other segment streams.

## 2. Components, reported separately (local core-hours)

| component | **per-symbol exact identification, T_run = 3.912·10¹³ (the design)** | nonzero-only scalar screen, best case, T = 5.741·10¹³ | exact scalar identification, T = 6.798·10¹³ |
|---|---|---|---|
| production (untrusted fast producer) | **92 816** (83.9%) | 146 903 | 179 808 |
| verification (independent wverify) | **14 469** (13.1%) | 21 781 | 26 149 |
| traversal (L: segment sieve, a_q read, SHA, pair loop; S: block a_n and SHA) | **1 848** (1.7%) | 2 728 | 3 239 |
| kernel (Arb ball products) | **910** (0.8%) | 1 326 | 1 566 |
| interval summation (exact fixed-point, error tally, fingerprint) | **522** (0.5%) | 759 | 896 |
| checkpoint writes (every 600 s per worker) | **57** (0.05%) | 89 | 109 |
| process setup | 0.8 | 0.8 | 0.8 |
| merge + final DFT (one machine) | 0.2 | 0.2 | 0.2 |
| **total** | **110 623** | **173 588** (+57%) | **211 769** (+91%) |

**Storage** is small and never the bottleneck:

| item | size |
|---|---|
| pre-produced low segments | 5.9 GB |
| checkpoints (96 workers × 10 restart generations × 80.5 MB, uncompacted) | 77 GB |
| stream and timing logs | 0.7 GB |
| final class sums and symbols | 0.2 GB |
| transient per worker (witnesses and a_q of one segment) | 17 MB |

**Streaming is the data-flow design** (validated in S5): produce → verify → accumulate → delete. The 5 TB of a_q and 35 TB of witnesses are never stored.

**Reconciliation with the earlier estimate.** The feasibility report gave 1.170·10⁵ / 1.820·10⁵ / 2.212·10⁵ CPU-h for the three cutoffs, using a two-point producer fit. S4 gives 1.106·10⁵ / 1.736·10⁵ / 2.118·10⁵ lch, 4–6% lower, because it interpolates six measured points and uses exact term counts. The component split confirms the earlier claim that production and verification are 97% of the cost; the engine is 3%.

## 3. The stopping rule, with the nonzero-only criterion included

**Both criteria are implemented in the merge** and evaluated on the same class sums:
* `UNIT_TEST`, which uses the exact K = 1024·Z from the identified symbols;
* `NONZERO_ONLY`, a ball test for [1024L, 1024U] ∩ pZ = ∅ on the weighted scalar.

**The per-symbol route stops earliest.** The rigorous error is the a priori tail bound tail_MS(κ, T) plus a tiny rounding tally, and the tail bound depends only on T. The stopping point is therefore fixed in advance by the planner; no data-dependent early stop exists. At T_run every symbol ball has radius < 1/2048, so every symbol is identified exactly. That gives K exactly, and K mod 2243 then settles the nonzero question as a by-product.

**The nonzero-only screen needs a smaller error on a weighted sum of 2.5 million symbols.** Its condition is W_p·δ(T) < p/2048 with weight mass W₂₂₄₃ = 1 397 925 114, which requires T = 5.741·10¹³ (1.47×).

**Why the screen cannot win here.** In the planner's normalization the screen is an effective LATDEN of ⌈1023·W_p/p⌉ ≈ 6.4·10⁸. Even the idealized Parseval-floor bound F = 725 141 gives 1023·F/p ≈ 3.3·10⁵. Per-symbol identification uses LATDEN 1024. The screen could win only if its effective LATDEN fell below 1024, which needs a weight bound below about p = 2243. The floor is about 323·p, so this is impossible here.

**Exact integer recovery is therefore not assumed necessary; it is simply cheaper.** The scalar screen's only advantage, O(1) memory, does not bind: 80 MB of class sums per worker.

## 4. All-in projection and its uncertainties (scenarios, not probabilities)

dollars = W · (1 + ops) / f · price + storage + merge, with W = 110 623 lch for the per-symbol design. The terms:

* **f is the cloud core's throughput relative to one idle local thread.** It is the dominant technical unknown and exactly what the pilot measures (P2, P4). The band 0.75 / 1.0 / 1.25 reflects AMD Genoa at 3.7 GHz against Comet Lake at up to 5.0 GHz single-core turbo. The fully loaded local host itself gives 0.914.
* **price per physical core-hour.** AWS c7a has 1 vCPU = 1 Genoa core. Spot is $1.199/h ÷ 64 = $0.0187 (vantage.sh, 2026-09-23; spot moves, band 0.015–0.025). On-demand is $3.2845/h ÷ 64 = $0.0513 (us-east-1).
* **ops** covers interruptions (about 400 s lost per worker per interruption at 600 s checkpoints), reruns and compaction: 1–6%.

| scenario (per-symbol design) | core-h | compute | storage and merge | **total** | wall on 20 × 64 cores |
|---|---|---|---|---|---|
| low: spot $0.015, f = 1.25, ops 1% | 89 383 | $1 341 | $27 | **$1 368** | 2.9 d |
| **central: spot $0.0187, f = 1.0, ops 3%** | 113 941 | $2 131 | $31 | **$2 162** | 3.7 d |
| high spot: $0.025, f = 0.75, ops 6% | 156 346 | $3 909 | $38 | **$3 947** | 5.1 d |
| on-demand: $0.0513, f = 1.0, ops 1% | 111 729 | $5 732 | $31 | **$5 762** | 3.6 d |
| worst: on-demand, f = 0.75, ops 6% | 156 346 | $8 021 | $38 | **$8 059** | 5.1 d |

* **Plus the pilot:** ≤ $50 by construction, with a $100 hard cap (see `S5_pipeline/pilot/PILOT_PROPOSAL.md`).
* **Scalar screens for comparison** (central): nonzero-only $3 386, exact scalar $4 128.
* **This host alone** (20 threads, exclusive use): about 110 623 / 13.3 = 8 300 h, roughly 11.5 months.

**$ per fully verified, accumulated chunk** (the purchase metric):

| chunk | local cost | central (spot) | on-demand |
|---|---|---|---|
| top-range chunk (one 2²⁴ segment at q ≈ 3.912·10¹³: produce, verify, accumulate) | 196 lch-s | **$0.00102** | $0.00279 |
| average segment chunk | 167 lch-s | $0.00087 | $0.00238 |

The full run is 2 331 727 segment chunks plus 9 326 908 Part-S blocks, which cost about $45 at spot. **The pilot measures $/chunk directly on the cloud (P4)**, including a kill -9 of the whole process group and a restart.

**What the uncertainty is made of, in order of size:**
1. Spot versus on-demand pricing and spot availability (2.7×). This is the purchaser's choice. About 1 280 cores for about 4 days in one region is not guaranteed; c7a, m7a and r7a share the CPU and can be mixed.
2. Cloud per-core speed f (±25%, removed by the pilot).
3. Ops overhead (1–6%).
4. Measurement and interpolation of W (±3–4%).

**Not included:** people's time, the D2/D5 mathematical work, the Codex review, and GPU acceleration. GPU was not benchmarked and is not assumed; nor is Aristotle assumed to be a compute cluster.

## 5. What the money buys (unchanged from S1)

**If K ≢ 0 (mod 2243)**, the conclusion is Sha(E/Q)[2243^∞] = 0, provided D1–D8 hold. **D2 (the split Selmer comparison) and D5 (an independent nonzero split-case height) are open** and must be discharged before a full run is purchased.

**If K ≡ 0, nothing is established.** The converse is not claimed, so the run should not be bought on the assumption that both outcomes decide something.

Even the successful outcome is finite-prime progress at one of the three bad primes. It implies neither FIN nor BSD.

## 6. A defect found before any spend: symbol radii at m = 2243² (fixed in v2.1)

**The error budget at the stopping point is thin by design.** `arbcore tmin` sets T so that 2·tail(T)/Ω⁺ ≤ (1 − 2⁻¹⁰)/(2·LATDEN). That leaves only 2⁻¹⁰/2048 ≈ 4.8·10⁻⁷ per symbol for everything other than the tail. The fixed-point accumulator adds exactly 2 units of 2⁻⁹⁶ per term, a tally E ≈ 4.4·10⁻¹⁶ at full scale. Ω⁺ = 0.028045.

**The v2 merge charged E to every class sum as a radius and fed those balls to `acb_dft`.** The probe (`S5_pipeline/probe/dft_radius_probe.c`, FLINT 3.3.1, 128 bits) measured how the transform propagates input radii, as a multiple of the ideal ℓ1 bound:

| length | algorithm | inflation over the ℓ1 bound |
|---|---|---|
| m = 81 | radix 3 | 2.3× |
| m = 2243 (prime) | Bluestein/Rader | 1.7·10³× |
| m = 2243² (production) | two-level | **7.0·10⁶×** |

At production length the output radius reaches 1.6·10⁻², so symbol radii would be up to 0.55 against the 1/2048 needed. **A full run would have ended fail-closed with no symbol identified.** No wrong answer was possible, but about $2k would have bought nothing. The small-m tests could not show this, because at m = 27 and 81 the transform is radix-3.

**Fix (v2.1, merge only; accumulation, checkpoints and digests unchanged).** Class sums enter the transform as exact dyadic midpoints. The accumulated rounding is added once per symbol as 2E. This is rigorous by the same ℓ1 argument the certified core uses for the tail: each term's bound is charged to exactly one class, so Σ_k |e_k| ≤ E, and the combination coefficients are at most 2 in absolute value.

**Full-scale budget under v2.1:**

| term | size |
|---|---|
| tail | ≤ 4.878·10⁻⁴ by construction |
| rounding 2E/Ω⁺ | ≈ 3·10⁻¹⁴ |
| the transform's own rounding on exact inputs | ≤ 7.2·10⁻²⁵ at m = 2243² for inputs of size 10⁻³ (probe, 232 s), about 3·10⁻²³ after dividing by Ω⁺ |
| threshold | 4.883·10⁻⁴ |

**Total:** about 4.878·10⁻⁴ + 3·10⁻¹⁴ < 4.883·10⁻⁴. The merge now prints `SYMBOL_RADIUS_BUDGET` and the maximum symbol radius. The R5-M test and pilot P3 check the full-length path against the threshold at T_run.

**A second margin-eater, found by the full-size merge test (fixed in v2.3).** The v2.2 R5-M merge at m = 2243² passed, with maximum symbol radius 4.8810·10⁻⁴ against the 4.8828·10⁻⁴ threshold. But the maximum sat 3.0·10⁻⁷ above the tail budget, and the transform's own rounding on those same inputs is only 2·10⁻²⁵ (`probe/merge_diag.c`).

The cause is `arb_div`. FLINT works at a precision tied to the operand's relative accuracy, and a symbol ball has about 17 accurate bits. Dividing it by Ω⁺ added about |x|·2⁻²⁸ to the radius (`probe/div_diag.c`); for the full run's larger symbols this term would have exceeded the margin.

v2.3 divides the exact midpoint and adds rad/|Ω|_lower. At m = 81 the maximum radius now equals the budget, 4.753284·10⁻⁴.

## 7. Erratum (2026-09-23, after the evaluator-review request)

1. **Checkpoint storage at fleet scale was understated.** The storage line (77 GB) assumed 96 workers × 10 generations. The central scenario runs 20 × 64 = 1 280 workers.
   * Per-worker checkpoints (80.5 MB each) come to **≈ 103 GB per restart generation**.
   * One aggregated checkpoint per process would bring this to ≈ 1.6 GB. Aggregation (or compaction) is designed but not implemented.
   * The dollar effect is small, tens of dollars in storage. The effect on merge time and disk per instance is real.
2. **The spot scenarios silently assume checkpoint persistence across interruptions.** The pilot launcher deletes the volume on termination, so a production run needs checkpoint upload to durable storage, or persistent volumes, plus fleet orchestration. Neither is implemented. Without them the ops overhead (1–6%) does not hold on spot.
3. **The dollar scenarios are modeled, not quoted.** They assume cloud throughput, pricing and availability that only the pilot and an actual purchase can establish.

See `/Users/bsm/BSD_2243_EVALUATOR_REVIEW_2026-09-23/REMAINING_BEFORE_PRODUCTION.md`.
