# Relative-unit construction: executed, no new bound

Date: 2026-10-18. Baseline: lab commit `89b0566ef61ba78d9d95853508f831ee3ee03440`.

**Result: the bounded relative-unit workaround produced no admitted ordinary unit. The intended rank-two joint bound was not reached.** This return records actual field arithmetic and exact finite-family exclusions. It supplies no new seed-prime result, complete-unit bound, ordinary class bound, or uniform theorem. FIN, ORDER9 and Q36 are unchanged.

## What was attempted and why

The previous coefficient-seven calculation obtained joint global/local rank four on the entire four-dimensional faithful unit component of the rank-zero 11a1 control. Its transfer to a rank-two curve failed at source generation: the harvested units were fixed by point negation and supplied no faithful component. The present experiment changes that producer, without redesigning the detector.

The field here is the actual degree-48 nonzero 7-torsion point field of the rank-two -47 twist of 11a1, model `[0,-1,1,-22826,2411880]`. This is a control curve, not the original BSD seed. The field, maximal order, scalar action, split primes and formal branch are retained inputs copied and hash-bound in `INPUT_BINDINGS.json`.

Write tau for scalar -1. For an integral tau-stable ideal I and alpha in I, exact equality `|Norm(alpha)|=Norm(I)` implies `(alpha)=I`. Then `alpha/tau(alpha)` is an ordinary relative norm-one unit. The unrestricted construction reaches every faithful unit class modulo seven: tau acts by -1 there, so `u/tau(u)` acts by multiplication by two. Conversely, for a relative norm-one unit epsilon other than -1, `alpha=1+epsilon` has a tau-stable principal ideal and produces epsilon. These facts justify the construction but give no finite search bound. See `review/PROOF_REVIEW.md` and `evaluation/SOURCE_COVERAGE_LEMMA.md`.

The intended payoff was two independent rejecting images under the existing norm/local map. With retained unit dimension four, that would give a complete-unit kernel upper bound two. It would still leave the ordinary class-supported contribution and any transfer to the original seed to be controlled.

## Executed arithmetic

| Operation | Exact outcome | Scope |
| --- | --- | --- |
| Weighted mixed-element search in 14 stable ideals | 14,326 distinct mixed exact norm tests; no assigned-ideal generator | 1,317 of 1,344 planned stages completed before the fixed alarm |
| Replace the assigned ideal by each candidate's actual principal ideal | All 20 selected principal ideals fail tau stability | Twenty smallest exact norm ratios, deterministic selection |
| Equal or conjugate principal-ideal pairs | Zero matches in 380 HNF comparisons | All 190 pairs of those twenty candidates |
| Arbitrary products of the twenty relative ratios | 127-row, 20-column divisor matrix has rank 20 over Q and F7; integer kernel zero | Exactly these twenty ratios; other scalar translates and other candidates are not included |

The weighted search uses opposite powers of two at twelve exchanged archimedean place pairs. Its integer LLL transforms and candidate norms are exact; cached numerical embeddings select candidates only. A separate check confirms that all sixteen initial weighted metrics break the old symmetry. No numerical approximation authorizes unit admission.

The main search stopped at its internal alarm after 177.11 seconds. The actual-principal-ideal and pair checks took 2.76 and 0.213 seconds. The complete factorization, anti-divisor kernel calculation and export repair together took about 25.31 seconds within their separately recorded sixty-second budget. There was no full BNF computation. A formatting error on the empty kernel was preserved and repaired from the already saved exact data without repeating the factorization; exit code zero was not used as evidence of success.

For the final check, set `beta_i=alpha_i/tau(alpha_i)`. Every actual principal-ideal factorization and its tau conjugate was reconstructed. The matrix has columns `div(beta_i)`. Its zero integer kernel proves that no nonzero exponent vector in this twenty-element family produces an ordinary unit. This is stronger than the individual and paired failures, but it is only a finite-family conclusion.

## What was checked separately

The separate review checks the admission argument, the stable ideal setup, the change of search geometry and the complete saved norm-log accounting. It does not regenerate all 14,326 candidate norms. The additive final review independently recomputes the twenty selected element norms and their actual ideal HNFs, and checks the final exact divisor data and rank at its stated scope. Read `FINAL_SCOPE_REVIEW.md` for its precise replay limits.

No ordinary unit was admitted, so the existing norm/local evaluator was not run on a new source. Its status is **ACTUAL_RANK_UNMEASURED**, not rank zero on the complete unit group. The retained field/evaluator bindings and source-completeness qualification are in `evaluation/`.

## Decision after the experiment

The changed producer successfully reached mixed elements but did not turn them into ordinary units carrying a faithful component. Products of the selected twenty relative ratios do not repair that failure. Continuing those same combinations cannot produce the required unit source; a larger or different source family would be a new experiment, not an unfinished part of this one.

There is no proof that relative units are absent or that this route is impossible. The unrestricted coverage statement shows that the desired component is not excluded by the relative-unit formulation itself. The unresolved step is an effective construction of units in that component, with enough independently measured rejection rank; the ordinary class contribution also remains unbounded.

For the retained zero valuation allowance, the complete-source formula still has the form

`dim(kernel) = (4 - r_U) + (c - r_C)`,

where `r_U` is rank on the entire faithful unit source and `r_C` is the compatible class-lift obstruction rank modulo that same full unit image. This run supplies neither new term. Partial lists, failed searches and rational norm-one identities cannot replace them.

**No seed endpoint advanced in this run.** The meaningful output is a reproducible execution and exact limit of the proposed workaround, not a claim of progress from the number of trials. See `REPLAY.md`, `VERIFICATION.json` and the manifest for custody and verification. Publication to the authorized lab branch does not upgrade the mathematical grade.
