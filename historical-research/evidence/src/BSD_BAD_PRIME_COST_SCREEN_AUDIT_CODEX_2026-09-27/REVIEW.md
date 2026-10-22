# Independent audit of the bad-prime singleton cost screen

Date: 2026-09-27. Input: `BSD_BUILD_MAP/bad_prime_cost_screen_2026-09-27/COST_SCREEN_REPORT.md`, SHA-256 `2062824a8a3860085f96f8635b8e9739b4fa1e013336833eb1eb8e2215e36fec`.

**Verdict: RETAIN_NO_LAUNCH_CONCLUSION_WITH_CORRECTIONS.** The auxiliary choices and cutoff arithmetic pass. The dominant production/verification estimates reproduce as models. The current implementation cannot fit the reported local storage budget. The report is not yet a complete execution budget, and its dollar estimates must not become spending recommendations.

The previously reviewed Bullach–Honnor criterion remains at its recorded preprint/retained-input grade. This audit supplies no new nonzero coefficient, primary vanishing theorem, FIN, ORDER9 or Q36 result. It does not re-audit the mathematical imports.

## 1. Custody and bounded execution

- All 20 entries of the supplied manifest passed, including its three explicitly named external references. The initial path guard stopped on those external references; after inspection they were allowlisted and verified. This was not a hash failure.
- The frozen evaluator source has SHA-256 `56a43aac38161d48848df4ed5c2f931f1dc7d5db745600bd140e4be3cac67fd7`. The installed binary matches the frozen SHA-256 `47d07f2e856e82d2fece7834085aa99d30fa65d32137f0fde843022050fd89db`.
- All 12 supplied `tmin` outputs replayed byte-for-byte using the pinned binary and the retained minimal model. This is a replay of the existing Arb planner, not an independent tail-bound implementation.
- Independent standard-library arithmetic checked minimal auxiliaries, segment alignment, work-unit counts and storage arithmetic. An analytic integration of the specified rate model reproduced the detailed production/verifier figures within 0.08 core-hour each.
- The checking command, including the 12 planner invocations, completed in less than one second. There was no build, benchmark, point count, new coefficient, modular-symbol evaluation, production launch, paid activity or repository modification. No Batch C output/corpus was read or changed; its post-extension boundary is treated as contingent. Only previously completed 37/41 records and the frozen evaluator source were inspected.

Files `CUSTODY.json`, `ADDITIONAL_BINDINGS.json`, `CHECKS.json`, `planner_replay/` and `check_cost_screen.py` retain the evidence. All work is additive in this audit folder.

## 2. What reproduces

Trial division independently proves that these are the smallest prime auxiliaries satisfying the stated conditions. Each has `v_p(ell-1)=1` and `ell` does not divide `pN`.

| p | ell | Quarter-tail cutoff, aligned T | Total segments | Additional after 4802 | Additional after contingent 6445 |
|---|---:|---:|---:|---:|---:|
| 4547 | 27,283 | 10,290,674,532,351 | 613,372 | 608,570 | 606,927 |
| 5843 | 35,059 | 13,281,615,937,535 | 791,646 | 786,844 | 785,201 |
| 2243 | 71,777 | 27,530,723,590,143 | 1,640,959 | 1,636,157 | 1,634,514 |

Here `SEGQ=2^24`, `T+1=segments*SEGQ`. The planner uses `LATDEN=4096` to reserve three quarters of the error budget for a final `1/1024` symbol lattice. It does not change that arithmetic lattice to `1/4096`.

The report's rate rule is log-log interpolation of **seconds per segment**. For each adjacent timing pair, this is `r(q)=c*q^a`, so integrating `r(q)/SEGQ` over the new coefficient range has an elementary antiderivative. Independent evaluation gives:

| p | Production, modeled local core-hours | Verification, modeled local core-hours | Sum |
|---|---:|---:|---:|
| 4547 | 18,958.183 | 3,543.652 | 22,501.834 |
| 5843 | 25,646.165 | 4,624.265 | 30,270.430 |
| 2243 | 61,114.125 | 9,947.919 | 71,062.044 |

These agree closely with `cost_model_detail.json`. They interpolate measured anchors; they are not measurements of these future jobs, rigorous runtime bounds, or evidence of cloud throughput. The old S4 script used a different model (per-prime rates and a prime-count approximation), so its script alone does not reproduce this new table. The new audit script now makes the current interpolation explicit.

The extrapolated accumulation allowance, `T/10^10 * [1.15,1.32]` CPU-hours, also reproduces. The combined headline ranges around 24k, 32k and 74k core-hours are reasonable **partial planning models**, subject to the omissions below.

## 3. Storage failure is stronger than the 75-byte estimate

In this frozen `msl` implementation:

- `NSEG = T/2^24 + 1` and `NBLK = ceil(T/2^22)`.
- Each of the `NUNIT=NSEG+NBLK=5*NSEG` work units writes all `ell` ball rows.
- Every unit file is retained until all workers finish, then reread for combination. There is no compaction/deletion step in this path.

The claimed disk model is exactly `75*NUNIT*ell` bytes. However, 75 bytes need not be trusted to decide feasibility. A row is `S <k> <ball dump>\n`. Even pretending that the entire nonempty ball dump occupies **one byte**, the row requires at least `5+digits(k)` bytes. Consequently the unmodified implementation has the following minimum serialized checkpoint payload, before headers, hashes or filesystem overhead:

| p | Ball rows | Minimum payload from line syntax | Report's 75-byte model |
|---|---:|---:|---:|
| 4547 | 83,673,141,380 | 0.802659 TB | 6.275486 TB |
| 5843 | 138,771,585,570 | 1.343740 TB | 10.407869 TB |
| 2243 | 588,915,570,715 | 5.798000 TB | 44.168668 TB |

All exceed the report's 205 GB free-space figure even under that deliberately impossible one-byte encoding. **This is a lower bound for the current file format and retention policy, not a lower bound for the mathematics or a redesigned evaluator.**

The 21 MB per additional corpus segment reproduces the reported 12.7/16.5/34.3 TB, but remains an average-size storage model. Five small archived p=37 unit samples inspected here average 55.10–55.46 bytes per ball row, rather than the report's claimed measured 69–81 range. The report did not bind the samples used for its range. Treat 75 as a planning allowance until that provenance is supplied. This discrepancy cannot rescue the current implementation, as the exact minimum above shows.

## 4. Required corrections

### F1 — The RAM statement omits the principal allocations

The statement “RAM per worker is ell balls, well under 10 MB” is false for this evaluator.

`worker()` allocates `rem[2^22]` and `an[2^22]` at eight bytes per entry, a `2^24`-byte sieve, and a `4*2^24`-byte input buffer: **144 MiB of fixed buffer allocation per worker**, before ball arrays and serialization buffers. The two smooth-block arrays alone occupy and are filled across 64 MiB per worker. Allocated capacity must not be confused with measured resident memory: only part of the large input buffer is normally touched.

Shared allocations additionally include `AMT[isqrt(T)+1]`, `A`, `SP`, `APK`, and hash arrays. `APSH` alone is 18.72/24.16/50.08 MiB and `LEAF` 74.87/96.64/200.31 MiB for the three candidates. Here `isqrt(T)` ranges from 3,207,908 to 5,246,972. Thus even the source header's “RAM independent of T” is not literally correct: several shared arrays grow as `sqrt(T)` or `T/SEGQ`.

This does not show RAM is the binding obstacle. It shows the requested full peak-RAM budget was not provided. Do not replace it with an invented new peak estimate; account for all allocations and Arb limb storage before an execution proposal.

Source: copied `sources/engine/arbcore.c`, lines 141–164, 240–243, 339–356.

### F2 — The model does not yet cost the entire evaluator

The code combines **83.7 billion to 588.9 billion serialized ball rows**, rereading their files, hashing content, parsing balls and performing additions. The report identifies the `T*ell` growth but supplies no separate CPU allowance for this merge, checkpoint serialization/hashing and I/O. Applying the small-ell all-in per-term rate to large ell does not measure those new dominant-in-ell operations.

At prime ell the final inner loop runs exactly `ell*(ell-1)` times and calls `arb_sin_cos_pi_fmpq` twice each time. The table uses ell squared, a harmless rounded operation count. The “1, 2, 7 hours” figures have no bound timing anchor in this packet. They are assumptions, not established assembly costs.

Therefore “95% production, 5% evaluation” should read “production/verification comprise approximately 95% of the currently priced components.” A complete execution budget must also price merge, I/O, initialization, restart/recovery, interval acceptance and the chosen retention policy. Do not benchmark them now while Batch C has priority.

The two JSON models also disagree: `cost_model_out.json` gives production-plus-verification totals 22,588 / 30,358 / 71,169, whereas the detailed figures sum to 22,501.911 / 30,270.506 / 71,062.121. The report uses the latter, which this audit reproduces. Mark the coarse JSON superseded or regenerate it from one model rather than leaving two unexplained outputs.

### F3 — The 5843 historical comparison uses the wrong stopping target

The report attributes `2.566e14` to release claim B.7. The bound copy of B.7 actually states **`1.687e14`**, the old per-symbol cutoff. The historical reconciliation explicitly identifies `2.566e14` as the more expensive **nonzero-only scalar** cutoff.

The comparable cutoff ratio is therefore about **12.70**, rather than 19.32. Neither number is a complete CPU speedup. The old approximately `6.3e5` core-hour estimate and the new approximately 32k model suggest a much larger historical-model CPU ratio, but the different implementations and incomplete new costing prevent promoting that to a measured gain. Keep both figures with their actual scope.

Sources: `sources/history/RELEASE_BRIDGE_CLAIMS.py`, B.7 (lines 150–158), and `sources/history/EXTERNAL_NONZERO_ONLY_RECONCILIATION_2026-09-23.md`, sections 1 and 3.

### F4 — 4547 is not a newly discovered absence of every other route

“First concrete route ever” and “the only route for 4547” must be withdrawn. The retained B.8 already records a two-prime Kurihara sufficient witness, with unresolved existence and an infeasible direct evaluation at its recorded auxiliary pair.

Correct wording: **“The BH application supplies a newly checked quadratic singleton alternative at 4547. Among the three BH candidates screened here, 4547 has the smallest modeled workload.”** No affordable executable route has been established. A mathematically specified sufficient criterion is not an operationally ready computation.

Source: copied `RELEASE_BRIDGE_CLAIMS.py`, B.8 (lines 159–168), and the already reviewed BH criterion.

### F5 — Tail-planner success is not a certificate of the eventual computed intervals

The quarter-tail planner rigorously handles its tail formula, kappa and period enclosure. It does not execute the finite accumulation, the large combination pass, the trigonometric assembly or the final division by the period.

Those future ball errors still must fit the unused margin, and every final symbol must pass the frozen containment/uniqueness test. The present computation has not shown that fixed working precision succeeds at these cutoffs. Retain the exact acceptance test and return invalid/inconclusive on failure; do not describe the planner as budgeting all future division errors.

### F6 — Streaming is a proposed repair, not a complete launch plan

The old 2243 stream engine is a useful existing component, and the report correctly preserves its open restart issue. Using it here still needs a tested adaptation, independent verification, target-specific receipt bindings and a BH acceptance profile. Sparse checkpoints must preserve coverage and a fail-closed restart/merge procedure; merely omitting unit files breaks the current final combiner.

Sharing the coefficient stream across three targets is a valid reuse idea. The current independent accumulators have different cutoffs and need their own exact prefix bindings. The quoted shared-pass total is not an implemented, benchmarked pipeline.

The historical dollars-per-core-hour ratio may be displayed as a scenario, but it is not a current cloud quote or a tested deployment budget. No new prices were researched in this audit. With the user's zero-spend constraint, none of these figures is a funding recommendation.

## 5. Minor accounting corrections

- A post-C prefix of 6445/613372 is **1.05075%** for 4547, so “under 1% either way” is not literally correct. It remains a small fraction. The other two post-C fractions are below 1%.
- `aux_primes.gp` calls `ellcard` for all 15 reported auxiliaries. Describe that honestly as small auxiliary point counts as well as primality searches. They are not a corpus extension, and this audit did not repeat them. BH does not need their torsion-free outcome.
- The approximate 80–100 wall-day conversion for the cheapest priced model is consistent with the retained 10–13 local-core-equivalents per wall-hour, but remains contingent on uninterrupted throughput and the omitted overheads.

## 6. Decision

Keep Batch C's existing authorization and stop rules unchanged. Retain the BH criterion and these exact auxiliary/cutoff specifications. Hold all three bad-prime evaluations under the current budget.

The cost screen establishes that **the current implementation and measured-rate model do not supply an affordable run**. It does not establish that the curves' primary groups need paid computation, that every possible algorithm is too costly, or that further mathematical work cannot help. A different coefficient-generation method, a tighter certified truncation bound, or a different finite certificate would require its own bounded assessment; none is launched by this review.

No edit to the expert repository, new cloud session, purchase or production computation follows from this report.
