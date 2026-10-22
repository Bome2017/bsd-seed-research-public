# S_DYADIC_SATURATION_FORMALIZATION_FREEZE_002 — status

`OBJECT_TYPE = CANONICAL_FREEZE`
`SUPERSEDES = NOTHING` — Freeze 001 remains valid and is carried forward unchanged
`DATE = 2026-09-11`
`MATHEMATICS_ADDED_BY_THIS_OBJECT = NONE`

```text
SATURATION_CERTIFICATION = DOUBLE_INDEPENDENT_LEAN_CERTIFIED
RUN_A = CLEAN   (8042 jobs, 16 modules, 2329 lines, 103 theorems+lemmas)
RUN_B = CLEAN   (8039 jobs, 13 modules, 2282 lines, 105 theorems+lemmas)

INPUT_IDENTITY            = BYTE_IDENTICAL   (both runs given aacd0de9…)
TARGET_STATEMENT_IDENTITY = BYTE_IDENTICAL   (11/11 declarations, all three trees)
SHARED_MODULES            = NONE
SHARED_PROOF_TEXT         = NONE
ARCHITECTURES             = SUBSTANTIALLY_DIFFERENT

PROHIBITED_CONSTRUCTS   = 0  (both runs)
AXIOM_FOOTPRINT         = [propext, Classical.choice, Quot.sound]  (both runs)
SORRYAX                 = ABSENT  (both runs)

SEMANTIC_TRAP_COV       = GENUINE_COVERING_PREDICATE  (both runs)
SEMANTIC_TRAP_LOCAL     = ALL_PLACES_QUANTIFIER       (both runs)
SEMANTIC_TRAP_GLOBALSET = DEFINED_BY_COV              (both runs)

NON_VACUITY_WITNESSES   = RUN_B_ONLY, both H41 branches, target instantiated
```

## What is certified

For `r = ε·2^m` with `m ≥ 3`, on the stratum `H₄₁`:

- `LocalKummerAll ⟺ Cov ℚ` on both the φ-side and the dual side;
- `GlobalSet = SelmerSet` on both sides;
- `((KExp ε m).subgroupOf (GphiExp ε m q)).index = 2`.

`LocalKummerAll` quantifies over ℝ **and every** ℚ_p — not a finite bad-place list. `Cov` is
the genuine quartic covering predicate. `GlobalSet` is defined **by** `Cov`, not by the
desired answer.

## What is NOT certified

`FORMALIZATION_LEVEL = EXPLICIT_2_ISOGENY_DESCENT_REALIZATION`
`ACTUAL_H1_SELMER_OBJECT = NO`

This is an explicit descent realization, not a cohomological Selmer group. The phrase
"formalized cohomological Selmer group" remains false of this object. No claim is made about
`Sel₂`, rank, Ш, `E(ℚ)/2E(ℚ)`, or `L(E,s)`.

## Independence — the exact meaning

"Double-independent Lean certified" means **two independent Aristotle proof-search runs**,
on the same Lean kernel (`leanprover/lean4:v4.28.0`) and the same mathlib revision
(`8f9d9cff6bd728b17a24e163c9402775d9e6a365`), producing two implementations that share no
module and no proof text.

It does **not** mean independent proof-assistant verification. A soundness defect in Lean or
in mathlib would affect both runs identically. It also does not establish that the two runs
were causally isolated from each other; that rests on the operator's run discipline, not on
anything verifiable from the artifacts.

## Project state after this object

| result | tier |
|---|---|
| Theorem F | `LEAN_CERTIFIED`, two independent runs |
| `S_dyadic` | `LEAN_CERTIFIED`, two independent runs |
| **`H₄₁` saturation** | **`LEAN_CERTIFIED`, two independent runs** ← changed by this object |
| δ actual-point descent | `LEAN_CERTIFIED`, one run (see `DELTA_DESCENT_FORMALIZATION_FREEZE_001`) |
| Theorem A | `DOUBLE_INDEPENDENT_CONVENTIONAL_PROOF`, not formalized |
| Theorem B | `CONVENTIONAL, BASE-CONDITIONED, LITERATURE-DEPENDENT` |

`PRIOR_ART_BLOCKER` for 66b1 remains `UNRESOLVED`. No novelty is claimed.
