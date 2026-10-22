# Labels used in the claim index

*Generated from `claims/spec/common.py`.*

## Evidence grades

* **IMPORTED_PUBLISHED** — A published theorem, applied. The source-check level is stated per import.
* **IMPORTED_PREPRINT** — A theorem from a preprint (not refereed), applied.
* **PROVED_WRITTEN** — A written proof or deduction in the project records (possibly combining imported theorems).
* **PROVED_COMPUTER_ASSISTED** — A certificate with rigorous error control (Arb balls, directed rounding, or exact arithmetic), with a stated trust base.
* **EXACT_COMPUTATION** — A finite exact computation (integers or rationals), replayable in seconds or minutes.
* **LEAN_CHECKED** — Machine-checked in Lean 4 from explicit hypotheses; the hypotheses are listed and are not themselves formalized unless stated.
* **NUMERICAL_EVIDENCE** — Floating-point or heuristic evidence; never used as a proof input.

## Kinds of statement

* **FACT** — Exact data about the curve.
* **THEOREM** — Unconditional, relative to the listed imports and trust base.
* **CONDITIONAL** — An implication whose antecedent is not established; the antecedent is a sufficient witness, never an obligation.
* **EQUIVALENCE** — A reformulation proved equivalent to an open statement; it earns no difficulty reduction by itself.
* **OBSTRUCTION** — A stopped route; see stop_kind and scope.
* **OPEN** — An open obligation of full BSD for this curve.
* **HISTORICAL** — A completed result about other curves or families, retained for context; it does not transfer to this curve.
* **WITHDRAWN** — An assertion that was made in the records and is withdrawn or superseded; listed to prevent resurrection.

## Kinds of stop (never conflated)

* **PROVED_OBSTRUCTION** — A theorem shows the route cannot succeed within an explicitly delimited class; nothing is claimed outside that class.
* **EQUIVALENT_REFORMULATION** — The route target is proved equivalent to the open problem; absent an independent proof method this gives no demonstrated difficulty reduction. It is not an impossibility.
* **DEFECTIVE_SOURCE** — The imported mechanism is false (counterexample recorded).
* **UNAFFORDABLE** — A known implementation exists, but its measured or modeled cost exceeds what has been authorized; not a mathematical stop.
* **UNSUCCESSFUL_ATTEMPT** — An attempt that found nothing; no impossibility is claimed.
* **PROCEDURAL** — Stopped by a stopping rule or decision (archived), not refuted.

## Review levels

* **NONE** — No review beyond the author.
* **MODEL_SAME_FAMILY** — A fresh-context review by a model of the same family as the author.
* **MODEL_CROSS_FAMILY** — A review by a model of a different family.
* **HUMAN** — Independent human review (none recorded for any claim).

A sufficient witness (for example a nonzero coefficient) is never an obligation: its failure proves nothing, and the obligation it serves may be met another way.
