# Concrete cached seed evaluator: p=83, auxiliary prime 167

Date: 2026-10-13. Scope: executable evaluator selection and bounded runtime checks. This file does not assert a new singleton witness or a new Sha result. At the time of this preparation, the full production calculation had not been launched by this worker.

## Selection

The smallest previously prepared unresolved coefficient prime is 53, but its frozen useful candidate uses auxiliary prime 743 and requires 9,206 coefficient segments beyond the present 6,445-segment certified prefix. Its saved preflight estimates 254–301 CPU hours, centrally 263, and roughly 59–77 hours of elapsed time. The frozen run remains unlaunched. This is not an inexpensive experiment. The candidate at auxiliary prime 107 had a zero diagnostic tame regulator; that observation is not a computation or proof that its actual Ota coefficient vanishes. No new such coefficient was evaluated here.

The p=59, auxiliary-prime-709 plan similarly needs a large corpus extension if run alone. Its old joint-corpus saving applies only after generating the large p=53 prefix. None of the cached exact seed symbol tables found in the targeted singleton corpus has an auxiliary prime whose predecessor yields a new unresolved coefficient prime at least 53.

The concrete lower-cost choice is instead p=83, auxiliary prime 167. It is new fixed-prime coverage if the unchanged acceptance checker returns NONZERO. It does not settle the first unresolved p=53 case or improve the previously stated minimum possible non-9 Sha order. It does not settle FIN, ORDER9, or Q36.

The source/custody worker independently handles Ota hypotheses and the corpus binding in `P83_OTA_THEOREM_CHECK.md`, `CHECKER_BINDINGS.json`, and `PREFIX_3420_CUSTODY.json`. Those are not inferred from a predicted coefficient. The fresh diagnostic prescreen is only a candidate selector, never an acceptance input.

## Frozen mathematical computation

- Model: `[0,-22735,0,106272484,0]`.
- Conductor: `6503188012738584`.
- Functional-equation sign: `+1`.
- Mode: unchanged `arbcore msl`, modulus `167`.
- Segment width: `16777216`.
- Actual lattice denominator: `1024`.
- Quarter-tail planning denominator: `4096`.
- Fresh minimal cutoff at the planning denominator: `57366635244`.
- Segment-aligned production cutoff: `57378078719 = 3420*16777216-1`.
- Prime-coefficient segments: `3420`.
- Smooth-number blocks: `13680`.
- Total independent work units: `17100`.
- Recommended threads: **8**.
- Full required coefficient-prefix bytes: `9673187648`, already present and hash-checked by the custody worker.
- Prefix SHA-256 root: `53de8838b356300dbb7aed6cfc57cab3498c82bd585954fd244095e338f997da`.
- Unchanged frozen engine SHA-256: `47d07f2e856e82d2fece7834085aa99d30fa65d32137f0fde843022050fd89db`.

Existing read-only coefficient view:

`/Users/bsm/BSD_P17_PREREQUISITES_2026-09-25/singleton_probe/corpus_ext_6445/view`

The evaluator reads `ap/`; the checker reads the corresponding `logs/ver_*.log` receipts. A fresh output directory is mandatory. No Stage-W coefficient producer is necessary.

The exact engine argument vector, after substituting a new output directory, is:

```
arbcore msl 0 -22735 0 106272484 0 167 6503188012738584 1 \
  57378078719 16777216 \
  /Users/bsm/BSD_P17_PREREQUISITES_2026-09-25/singleton_probe/corpus_ext_6445/view/ap \
  8 NEW_OUTPUT_DIRECTORY/units 1024
```

Production must use the staged wrapper/checker and sealed manifest, not this illustrative direct invocation. The unchanged checker must verify every interval, source/corpus identity, coverage count, projected group-ring coefficient, and theorem-profile condition. `INVALID` and `INCONCLUSIVE_ZERO` are not mathematical conclusions about Sha.

## What can and cannot be accelerated safely

The existing engine already performs the useful compression: each summand is accumulated only into the bucket indexed by `n mod 167`. All modular symbols are recovered by a short final Fourier assembly. Computing only c2 does not eliminate the dominating traversal of the certified coefficient corpus and the smooth-number contribution. It would create a new tail/rounding proof burden without a demonstrated saving in that traversal.

The old certified p=43, auxiliary-prime-173 Arb unit files cannot be reused. Their exponential parameter and residue buckets depend on the auxiliary modulus. The certified prime-coefficient files can be reused because they are coefficients of the same seed newform.

The unchanged worker code assigns independent unit indices atomically. Each unit uses fixed parameters, and the final Arb additions are performed in increasing unit order. The parameter-lock routine intentionally omits the thread-count argument. Thus changing worker count changes scheduling, not the mathematical partition or reduction order. The bounded test below verifies that conclusion on actual unchanged-engine outputs, though it is not a full production replay.

Extra hyperthreads did not improve the measured workload. Using 8 workers retains the historical configuration and avoids extra CPU use without sacrificing the observed elapsed time.

## Bounded fresh runtime measurements

The measurement-only harness is the historical `BSD_BAD_PRIME_STREAMING_RETURN_OPUS_2026-09-29/meas/harness`. It includes the previously tested streaming engine source. Its hash and source hashes are saved in `runtime_probe/PROBE_RESULT.json`. Harness measurements are not production certificates.

At the full intended cutoff and modulus, a sequential comparison evaluated the same 16 coefficient segments `[50,66)`, accumulating `763636996` pairs in each run:

| Workers | Elapsed seconds | CPU seconds | Peak RSS MB |
|---|---:|---:|---:|
| 8 | 7.50 | 59.27 | 191 |
| 12 | 8.22 | 77.77 | 268 |
| 16 | 7.58 | 113.34 | 344 |

The initial 48-segment W8/W16 probes may have overlapped. They are retained for custody but excluded from the worker-choice comparison. The later three runs above executed sequentially.

Six individual units at the actual production cutoff supplied a separate bounded cost check:

| Unit | Type | CPU seconds |
|---:|---|---:|
| 1000 | coefficient segment | 0.326 |
| 3000 | coefficient segment | 0.214 |
| 3419 | final coefficient segment | 0.211 |
| 3420 | first smooth block | 0.790 |
| 10260 | middle smooth block | 0.704 |
| 17099 | final smooth block | 0.714 |

These sampled units do not include the most expensive initial coefficient segment and are not extrapolated as a standalone full-runtime model.

A second test invoked the **unchanged frozen production executable** at the deliberately insufficient cutoff `67108863`, keeping modulus 167, with W8 and W16. All 20 complete work-unit files and the entire stdout were byte-identical. The shared stdout SHA-256 is

`4fd3c166bdd93490b1e15792c4439a5ef5c27e5a9c143f68b5cab103d565c021`.

Elapsed times were 3.80 and 4.23 seconds, respectively; peak RSS was approximately 0.56 and 1.09 GB. The deliberately short cutoff cannot certify a seed modular symbol. It tests scheduling determinism and runtime only. Per-file hashes and the identical-output assertions are recorded in `runtime_probe/PROBE_RESULT.json`.

## Honest production estimate

The strongest timing baseline is the completed seed p=43, auxiliary-prime-173 run: cutoff `59475230719`, 3,545 coefficient segments, W8, approximately 3,238 seconds elapsed and 25,574 total CPU seconds. The present cutoff is about 3.5 percent smaller and its modulus is slightly smaller. No coefficient generation is needed.

A practical expectation is therefore **45–60 minutes of elapsed engine time at W8**, approximately **6–8 CPU hours**, plus hashing/checking overhead. This is an estimate, not a promised deadline. The current slice timings do not justify a faster claim. A conservative monitoring envelope would allow 90 minutes and 12 CPU hours before assessing slowdown; it should preserve already-computed units rather than label a resource stop as a mathematical failure.

New disk use should be a few hundred MB: the 17,100 per-unit files are about 10 KB each at this modulus. A 2 GB output allowance is ample under the observed file sizes; the existing 9.67 GB prefix is reused, not copied or regenerated. Historical and bounded RSS measurements support W8 comfortably on this 16 GB host.

## Decision

This is an executable, source-bound attempt at an unresolved seed coefficient prime. Its cost is materially smaller than starting the frozen p=53 expansion. It remains an individual-prime computation, and its only success criterion is the actual fail-closed singleton witness check. There is no uniform-bound claim and no blind sequence of follow-on candidates authorized by this selection.
