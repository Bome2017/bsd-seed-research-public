# This folder's reported C13 values are SUPERSEDED

**Do not read `RESULT.json` or `STATE.json` here as the current value of C13.** They are preserved unedited as
historical evidence of the run and of the write-through incident. The corrected, certified result is:

    C13 = 2 (mod 13) in the omega1 convention;  1 in the full real period convention.   NONZERO.

Canonical records:
* `~/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/_work/active_full_bsd/p13/NORMALIZATION.md` — the resolution
* `~/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/audits/P13_PRIMARY_THEOREM.md` — the qualified theorem
* `~/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/MASTER_BSD_DAG.md` §3 and the 2026-09-21 completion entry

## What this folder got wrong

Two independent scaling errors, both mine, which happened to compose into the observed uniform factor of three:

1. **Omitted the unit-root factor.** The unit root of `X^2 + 4X + 13` is `alpha = 9 mod 13`, so `alpha^-2 = 9`. The
   correct unfolded weight is `9 * binom(j(b),2)`, folded to `2 * 9 * binom(j(b),2)`. I derived only
   `2 * binom(j(b),2)`. The ratio is `9^-1 = 3 mod 13` — exactly the discrepancy I observed between my weights and the
   predeclared ones. **The predeclared gate weights were correct; mine were not.**

2. **Divided by the lattice denominator that was already divided out.** `SYMBOLS_m169.txt` already reports `S_b`, not
   `1024 * S_b`. I treated its integers as numerators and multiplied by `1024^-1 = 4`.

Both of my reported values correct to 2:

    7 * 1024^-1             = 7 * 4     = 2
    8 * 1024^-1 * alpha^-2  = 8 * 4 * 9 = 2

verified here directly from the exact symbol file: the six predeclared group sums are
`163, -138, 272, -52, -230, -215`, weighted total `-3950 = 2 (mod 13)`.

## The coincidence that hid it

`1024^-1 = 4` and the interpolation factor `(1 - alpha^-1)^2 = 4` are **equal in F_13 and play different roles**. The
gate listed `interpolation_factor_mod_13 = 4`; I read my own `1024^-1 = 4` as confirmation of it and stopped checking.
Two distinct constants colliding numerically in a small field is exactly the situation where agreeing arithmetic proves
nothing.

## What stands from this folder

The computation itself: cutoffs reproduced with `arbcore tmin`, 2333 reused segments rehashed clean, 948 new segments
generated, stage C `P3_CHECK_PASS failures=0`, 156+156 symbols identified in `(1/1024)Z`, the `T_13` Hecke relation with
24 identities, and the exact symbol tables that the corrected evaluation consumes. The nonvanishing verdict also stands
— it was invariant under the error, since 3 is a unit. Only the residue value was wrong.

`INCIDENT_2026-09-21.md` and `POST_ABORT_INTEGRITY.json` remain the record of the write-through incident; the completion
review independently re-confirmed all 2333 reused segments against their pre-incident hashes.
