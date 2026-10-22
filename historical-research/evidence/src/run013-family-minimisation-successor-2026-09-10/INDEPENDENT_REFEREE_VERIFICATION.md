# Independent referee pass — what was checked here

2026-09-10.  A separate model refereed Propositions A/B from the packet
`PROP_A_REVIEW_PACKET_2026-09-10.zip`, reconstructing Proposition A **before** reading the supplied
proof.  Its verdicts: `PROPOSITION_A = PASS`, `COROLLARY_A1 = PASS`, `PROPOSITION_B = PASS`,
`MODEL_TRANSFER = PASS`, `COUNTEREXAMPLE_FOUND = NO`.

Those verdicts are the referee's.  This file records what **this** session verified about them, so
the chain is not "one model said PASS".

## 1. Bundle integrity

`SHA256SUMS.txt` self-check: **10/10 OK**.

⚠ The separately uploaded `independent_counts.csv` (501,228 bytes, 15,737 lines) is a **truncated
prefix** of the copy inside the bundle (587,596 bytes, 18,220 lines) — it ends mid-row at
`727501,5,-1`.  Verified byte-for-byte that the upload is a prefix of the complete file.  Use the
in-bundle copy; do not circulate the standalone upload.

## 2. Independent recomputation of the referee's counts

Their counts come from a C++17 program using a sieve and finite differences.  I recomputed with a
separate Python implementation (quadratic-residue table, no shared code):

    rows recomputed        : 9,616   (every row with q < 100,000, plus 26 large rows
                                      sampled at random, including their last row q = 999,917)
    fields checked per row : n_minimal, n_descent, v2, a_q, q_mod8, chi_q31, family
    disagreements          : 0

Aggregate claims over all 18,219 rows, re-derived: 9,828 family rows, **all** with `v₂ = 2`; **all**
with `a_q ≡ 2 (mod 8)`; `n_minimal = n_descent` on **every** row; `(−31/q) = (q/31)` on **every** row.

## 3. The referee's new mathematics, checked independently

| claim | verdict here |
|---|---|
| `(−31/q) = (q/31)` for every odd prime `q ≠ 31` | **Confirmed.** The two reciprocity signs cancel because `(31−1)/2 = 15` is odd. No counterexample below 200,000. Cleaner than the `q ≡ 1 (mod 4)` route and now used in v2 of Proposition A. |
| the halving quartic factors as `(x² − (16+4s)x + 64)(x² − (16−4s)x + 64)` when `2 = s²` | **Confirmed symbolically** (sympy, using `s² = 2`): both sides are `x⁴ − 32x³ + 352x² − 2048x + 4096`. |
| `D_± = 32(1 ± 4s)`, `D₊D₋ = −31·32²`, so exactly one is a square | **Confirmed**: `D₊D₋ = −31744 = −31·1024`. |
| the quartic is `−2048` at `x = 8` and `2048·31` at `x = −8`, so `x² ≠ 64` | **Confirmed.** |
| `y = (x²−64)/(4s)` is on the curve and `x(2P) = (2s)² = 8` | **Confirmed** algebraically. |
| necessity: `(2/q) = +1`, `(−31/q) = −1` ⟹ `v₂ ≥ 3` | **No counterexample** among all such primes below 20,000. |
| `q = 11`: `#Ẽ(F₁₁) = 12`, `v₂ = 2`, `a_q = 0` | **Confirmed.** `11 ≡ 3 (mod 8)`, `(11/31) = −1`, `(2/11) = −1`, `(−31/11) = −1`. So `A′` really does not extend `a_q ≠ 0`. |
| `Z/12` with `T = 3` refutes the lemma without the 2-group hypothesis | **Confirmed**: order 4, not in `2S = {evens}`, `|S| = 12`. |
| `Z/4 × Z/2` with `T = (1,0)` refutes it without cyclicity | **Confirmed**: order 4, not a double, `|S| = 8`, and no element of order 8. |
| 15 nonresidues mod 31; 15 CRT classes mod 248; `φ(248) = 120` | **Confirmed**, and the 15 class representatives match theirs exactly. |

## 4. One correction to the referee's report

The referee lists as a defect: *"F62 has six fields, despite the introductory comment saying five."*

The comment (`RequestProject/Run013/Family.lean:16–17`) reads *"All five literal fields are retained
even though the descent uses only primality, `q ≡ 5 (mod 8)` and `(q/31) = -1`."*  It sits directly
under a display of the family as `{ q prime : q ∤ 372, q ≡ 5 (mod 8), (q/31) = −1, v₂(…) = 2,
a_q ≠ 0 }` — five conditions **after** the sort `q prime`.  On that reading the comment is
self-consistent, and it explicitly names primality separately in the same sentence.

So this is an **ambiguity, not a stale error**.  The structure does have six fields — `prime`,
`not_dvd_372`, `mod_eight`, `legendre_31`, `val_two`, `trace_ne_zero` — and passing to `F62min`
removes three.  The wording is worth disambiguating; it should not be reported as incorrect.

## 5. Two fair criticisms of the packet's computational material, both actioned

1. *"The halving search uses the very duplication identity under review."*  Correct — C4 corroborates
   the identity's consequences, not the identity.  Now stated in the script header.
2. *"The script prints violations rather than failing with a nonzero exit status."*  Correct.
   `_receipts/verify.py` now accumulates failures and exits 1 if any check fails.  Re-run: exit 0,
   `ALL CHECKS PASSED`.

## 6. What this does and does not settle

Settled: Propositions A, A′, A1, B as **conventional mathematics**, reconstructed independently and
cross-checked here against a second implementation.

Not settled, and unchanged by any of it: **`F62min q → F62 q` is still absent from Lean.** Inside the
formal development the two predicates remain non-interchangeable; `F62.toMin` exists, the converse
does not.  The referee said the same.  No PASS on conventional mathematics converts into kernel
certification.
