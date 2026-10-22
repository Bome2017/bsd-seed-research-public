# Reconciliation: external nonzero-only cutoff report (pasted 2026-09-23) against the S4 / feasibility figures

## 1. The numbers agree

The external report's ideal nonzero-only cutoffs reproduce the feasibility §6 and S4 values to the digits available:

| prime | external report | feasibility / S4 |
|---|---|---|
| 2243 | 57 406 180 556 799 = 3 421 675 · 2²⁴ − 1 | T = 5.7406·10¹³ |
| 5843 | 256 601 260 818 431 = 15 294 627 · 2²⁴ − 1 | T = 2.5660·10¹⁴ |

* The report's "1/1024 reserve" variants also agree: 3 418 474 and 15 291 682 additional segments.
* Its "reduction" figures are the nonzero-only cutoff against exact scalar identification (6.7981·10¹³ and 3.0657·10¹⁴). They reproduce as 15.56% and 16.30%.
* **This is a replication of the arithmetic, not of the method.** Both computations use the same `arbcore tmin` routine and the same mapping D = 1023·W_p/p.

## 2. Nit

The column "multiple of existing prefix" is total cutoff ÷ prefix: 3 421 675 / 3 281 = 1 042.88, and 4 661.57 at 5843. Additional segments ÷ prefix is 1 041.88 and 4 660.57. The implied existing prefix is 3 281 segments, about 5.5·10¹⁰. The difference is immaterial.

## 3. What changes the verdict's scope

**The report's verdict is about scalar evaluation.** It reads "2243_BLOCKED / 5843_BLOCKED: the certificate still needs an affordable certified evaluator", and it is correct for a scalar evaluator under the retained absolute-weight tail bound.

**The cheapest stopping rule is not scalar.** Per-symbol exact identification at T_min is below both scalar cutoffs and yields K exactly:

| prime | per-symbol T_min | nonzero-only cutoff is |
|---|---|---|
| 2243 | 3.912·10¹³ | 1.467× higher |
| 5843 | 1.687·10¹⁴ | 1.521× higher |

**That evaluator now exists and is costed for 2243** (S2–S5):
* **the engine:** the v2.3 class-sum accumulator with length-m DFT symbol extraction; final validation 24 PASS / 0 FAIL, including at m = 2243² and T_run;
* **measured work:**
  * **1.106·10⁵ local core-hours** for per-symbol identification;
  * 1.736·10⁵ (+57%) at the nonzero-only cutoff;
  * 2.118·10⁵ (+91%) for exact scalar identification;
* **all-in:** about **$2.2k central** (AWS c7a spot, cloud per-core speed f = 1). The scenario range is $1.4k–$3.9k on spot, $5.8k on-demand and $8.1k worst case. See `S4_cost/S4_COST_RECONCILIATION.md`.

**For 2243 the block is therefore no longer "no affordable evaluator".** What remains is:
* a budget decision;
* D2 and D5;
* the independent (Codex) check;
* the capped pilot, which measures f.

**For 5843**, S4 did not re-cost anything; the scope was 2243 only. The feasibility figure is 6.35·10⁵ CPU-h for per-symbol identification, about 5.7× the 2243 work.

## 4. Points of agreement

* Early stopping alone does not justify a scalar engine; it was not built.
* The segment count is not the cost unit. Per-segment cost grows with height (production ~ q^{1/4}), which S4 integrates over the measured heights.
* A better tail bound, one that does not use absolute weights, or a different evaluation algorithm could change every figure.
* All theorem and lattice qualifications stand. K ≡ 0 establishes nothing; K ≢ 0 gives Sha[2243^∞] = 0 only given D1–D8.
