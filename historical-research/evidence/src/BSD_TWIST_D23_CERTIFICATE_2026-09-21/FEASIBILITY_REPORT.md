# `L'(E^{-23},1) != 0` — cutoff adequacy and cost, measured

Date 2026-09-21. Executes the two gating questions before any engine run: **does the proposed cutoff suffice**, and
**what does the computation actually cost**. No sum computed, no engine launched. Formulas (1) and (2) taken from
`MCS_TWIST_IDEAL_REVIEW.md` §3, not re-derived.

## Summary

| question | answer |
|---|---|
| Is `T = 3.45e9` an adequate cutoff? | **No.** `B_D(T) = 0.343`. |
| What is adequate? | `T = 5e9` gives `1.3e-3`; **`T = 7e9` gives `1.1e-6`** — 418 of 2333 segments, **17.9%** of the corpus. |
| Is the coefficient corpus sufficient? | **Yes, with 5.6x headroom** at `T = 7e9`. |
| Is the expensive stage already paid? | **Yes.** Stage W (prime-coefficient generation, 2h33m) is exactly the corpus we reuse. |
| Streaming cost for `T = 7e9` | **~5.7 minutes**, extrapolated from recorded engine timings. |
| What is not measured | the `E_1`-in-balls kernel, which is the one genuinely new piece. |

## 1. Cutoff adequacy

`c = 2 pi / (|D| sqrt N) = 3.3875747e-9` with `sqrt N = 80 642 346`, `D = -23`. Evaluating (2):

| `T` | `cT` | `B_D(T)` |
|---|---|---|
| 1.00e8 | 0.339 | 2.99e6 |
| **3.45e9** | 11.687 | **0.343** |
| 5.00e9 | 16.938 | 1.27e-3 |
| **7.00e9** | 23.713 | **1.08e-6** |
| 1.00e10 | 33.876 | 3.14e-11 |
| 3.914e10 (full corpus) | 132.590 | 1.71e-54 |

The certificate logic is `|truncated sum| > B_D(T) => L' != 0`. At `T = 3.45e9` that needs `|L'| > 0.343`, which is
not known and cannot be assumed. **The proposed cutoff is a comparison cutoff, not a certificate cutoff** — as the
review itself cautions.

The gap between where the bound permits truncation and where the terms actually die is structural, not slack in the
proof: (2) uses `|a_n| <= d(n) sqrt n`, and that `sqrt n` growth fights the exponential. The genuine decay sets in once
`cn > 1`, i.e. `n > 1/c = 2.95e8`, roughly 24x earlier than the rigorous cutoff.

**Recommendation: `T = 7e9`.** It costs 2x the proposed prefix, gives six orders of margin, and stays inside the
already-verified part of the corpus.

## 2. Corpus format — verified independently

`run/ap/ap_NNNNNN.bin`, one segment per `2^24` block, **int32 little-endian, one value per prime in increasing order**,
all primes in range including the bad ones. Segment 0: 1 077 871 values in 4 311 484 bytes = exactly 4 bytes each, and
`pi(2^24) = 1 077 871` confirms the indexing.

Cross-checked against coefficients computed independently here by direct point counts on `y^2 = x^3 - 22735x^2 + 106272484x`:

| `p` | file | independent |
|---|---|---|
| 2 | 0 | bad, `2^3 \| N` |
| 3 | -1 | bad, `3 \|\| N`, `±1` |
| 5, 7, 11, 13 | -2, -2, -2, -4 | -2, -2, -2, -4 |
| 17, 19, 23, 29, 31, 37 | -6, 4, 0, 0, -8, 10 | identical |
| 2243 | 1 | bad, `2243 \|\| N`, `±1` |

`a_13 = -4` agrees with the value I verified for the Aristotle archive earlier today, from a different route.

## 3. Cost, from the engine's own recorded timings

`run/logs/timeline.log`, C11 run of 2026-09-20 (host: 16 GiB, 20 logical CPUs, J=12 producers):

    16:45:19  stage W start                                        (prime coefficients)
    19:18:19  stage W done                          2h 33m 00s     TMAX = 39,141,244,927
    19:18:19  stage A m=121 T=39,141,244,927 start
    19:50:36  stage A m=121 done                       32m 17s     -> 2.02e7 terms/sec
    19:53:09  stage A m=11  T= 3,388,997,631 done       2m 33s     -> 2.22e7 terms/sec

Two consequences:

1. **Stage W is already paid.** It produced exactly the corpus this certificate reuses. No prime-coefficient
   generation is required — confirming, with a timing, the review's reuse finding.
2. **Stage A is the structural analogue of our sum**: it streams `n = 1..T`, builds composite `a_n` from the prime
   corpus, and accumulates. At the measured 2.0-2.2e7 terms/sec, `T = 7e9` streams in **~5.7 minutes**.

## 4. What is not measured, stated plainly

Stage A accumulates in modular integer arithmetic. Our sum needs `chi_{-23}(n) a_n / n * E_1(cn)` accumulated in a
**ball enclosure**. Two differences:

* `chi_{-23}(n)`: negligible — `-23 = 1 mod 4`, so the character is the Legendre symbol mod 23, a 23-entry table.
* `E_1(cn)`: the real unknown. Evaluated naively 7e9 times it dominates everything. The standard remedy is a piecewise
  polynomial approximation with a rigorous remainder, reducing it to ~10 flops per term — but **that kernel does not
  exist yet and is not benchmarked here.** Any multiplier from 1.5x to 20x over Stage A is defensible without it.

So the honest cost statement is: **the streaming half is measured at ~6 minutes; the arithmetic half is unmeasured,
and writing it is the remaining work.** It is a new Arb kernel in an existing C engine, not new mathematics.

## 5. Status and recommendation

Both gating questions are answered. Nothing is certified: no sum was computed and `L'(E^{-23},1)` remains of unknown
size and sign.

If this proceeds, the order I would follow is (a) a **double-precision** pass at `T = 1e9` purely to learn the scale of
`L'`, which decides between the `5e9` and `7e9` cutoffs and costs under a minute of streaming; then (b) the ball kernel
at the chosen `T`. Step (a) proves nothing but removes the only remaining unknown in the cost model. **Neither is
launched here.**

Unchanged: a certificate would supply `rank E(Q(sqrt -23)) = 3` and make the rank-three Selmer-to-Sha comparison
applicable at primes meeting the join's other hypotheses. It would give **no** new Sha vanishing on its own; the
independent evaluation or bound of `I_3` remains the separate obligation, with no method.
