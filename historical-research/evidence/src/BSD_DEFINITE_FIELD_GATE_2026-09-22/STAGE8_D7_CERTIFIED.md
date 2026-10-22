# Stage 8 — the D = -7 certificate is obtained. `d^- = 0` is no longer conditional.

Date 2026-09-22. **Additive.** Discharges the stage-7 minus-side obligation. Full artifact:
`~/BSD_TWIST_D7_CERTIFICATE_2026-09-22/` (13 files sealed, RESULT.md).

## Result

    L(E^{-7}, 1)  in  [9.054319, 9.054421]     ZERO_EXCLUDED, POSITIVE, margin 1.79e5

`w(E^{-7}) = +1` (stage 1), so this is the central value and the analytic rank of `E^{-7}` is 0. By the retained
Gross-Zagier-Kolyvagin theorem at analytic rank zero:

    rank E^{-7}(Q) = 0          Sha(E^{-7}/Q) finite

Nothing else is claimed: no BSD statement, no order formula, no Sha order.

## What it discharges

| gate item | before | after |
|---|---|---|
| `DEFINITE_TWIST_RANK0` | NOT CERTIFIED | **CERTIFIED** |
| gate condition 3 (`rank E^D(Q) = 0`, so `rank E(K) = 2`) | OPEN | **SETTLED** |
| `(r^+, r^-)` | intended, uncertified | **`(2, 0)` established** |
| `M4_FROM_RANK_DATA` (needs `r^- <= 2`) | unexcluded above 2 | **holds**, `r^- = 0` |
| stage-7 `A2a` minus side: `d^- in {0,1,2}` | three live rows | **`d^- = 0`**, one row left |

The stage-7 enumeration now reduces to its first row: `d^+ = 0` free from the derived-height inequality, `d^- = 0`
from this certificate, hence `Div Sha(E/K)[p^inf] = 0` — **conditional on `sigma = 4`**, i.e. on `[c_2] != 0`, and on
the module identification. Those two remain open; this certificate removes the third.

## Method note worth keeping

The central value is the **base case** of the tail family the sealed adapters already used: `L''` uses
`2[..]/(cT)^2`, the `D = -23` first derivative uses `2 tail_MS/(cT)`, both from `E_1(x) <= e^{-x}/x`, so the central
value is `2 tail_MS` itself. Cross-checked by recomputing the sealed run's own recorded tail to 12 digits before
writing any new code. Consequence: the adapter drops the entire `E_1` Taylor node-table apparatus and calls `arb_exp`
directly — smaller and cheaper than the derivative adapter, not larger.

Cutoff discipline held: the tail was tabulated first as a stopping criterion, no cutoff chosen in advance, and the run
stopped at the first admissible `T` excluding zero (120 of 3281 segments, ~4.5 min, 0.83 GB).

Corpus integrity: **0** `ap_*.bin` segments modified. The 2026-09-21 write-through-symlink failure mode did not recur.

## Next

    A1 residue : module identification -- is BLV's Char_p(f) the characteristic ideal of the same X_inf
                 that BD's derived-height theorem applies to (same local conditions)?     OPEN
    EXACT_M4   : [c_2] != 0                                                               OPEN  <- now the sole
                 (and would itself force r^- <= 2, which this certificate has now proved directly)   remaining
    A2b        : formal given A2a                                                                    input to A2a
    A3         : supersingular signed analogue                                            OPEN, separate
    B          : a_p = +-1 ordinary primes                                                moot unless A closes
