# DELTA_DESCENT_FORMALIZATION_FREEZE_002 — status

`OBJECT_TYPE = CANONICAL_FREEZE`
`SUPERSEDES = NOTHING` — Freeze 001 remains valid and is carried forward unchanged
`DATE = 2026-09-11`
`MATHEMATICS_ADDED_BY_THIS_OBJECT = NONE`

```text
DELTA_CERTIFICATION = DOUBLE_INDEPENDENT_LEAN_CERTIFIED
RUN_A = CLEAN   (8030 jobs, Delta.lean 365 lines, 27 declarations, 16 added)
RUN_B = CLEAN   (8030 jobs, Delta.lean 345 lines, 33 declarations, 22 added)

INPUT_IDENTITY            = BYTE_IDENTICAL   (both given b75ba34e…c25052d3)
TARGET_STATEMENT_IDENTITY = BYTE_IDENTICAL   (11/11 shipped declarations, all three trees)
SEMANTIC_CORE_IDENTITY    = BYTE_IDENTICAL   (Basic.lean, Selmer.lean)
HELPER_OVERLAP_BEYOND_V1  = 3 names, all with DIFFERENT proof text
INTERFACE_EQUIVALENT      = YES (one probe compiles unchanged against both)

PROHIBITED_CONSTRUCTS   = 0  (both runs)
AXIOM_FOOTPRINT         = [propext, Classical.choice, Quot.sound]  (both runs)
SORRYAX                 = ABSENT  (both runs)
CLS_ZERO_TRAP_AVOIDED   = YES  (0 code occurrences, both runs)
FORBIDDEN_TOKENS_IN_CODE = 0   (both runs)

INDEPENDENCE_CLASS = PROOF_SEARCH_INDEPENDENCE_UNDER_IDENTICAL_SUPPLIED_MATHEMATICS
PACKAGING_DEFECT   = PRESENT IN BOTH RETURNS, recorded, not repaired
CONTINUATION_BASE_RECOMMENDATION = RUN_B + 3 lemmas ported from RUN_A
```

## The independence caveat — do not drop this line

Both runs received the **same hint**. The V1 `TASK.md` (lines 51–53) and the embedded Pro 2
specification both supply the intersection-cubic / root-product mechanism explicitly. So:

> **This is proof-search independence under identical supplied mathematics. It is not
> independent discovery of the mechanism, and it is not independent proof-assistant
> verification.**

What replicated is the *formalization*: that the supplied mechanism really closes in Lean over
mathlib's own point group, with every case discharged and nothing weakened, twice, from
almost-disjoint helper layers. That is worth having. It is weaker than the saturation
replication, where no hint constrained the two decompositions.

## What is certified

For `a b : ℚ` with `b ≠ 0` and `a² − 4b ≠ 0`, on **mathlib's own** nonsingular point group of
`W : y² = x³ + a·x² + b·x`, with **mathlib's own** `AddCommGroup` instance:

1. `δ(P + Q) = δ(P)·δ(Q)` where `δ(O)=1`, `δ((0,0))=[b]`, `δ((x,y))=[x]`;
2. `range δ = {c | ∃ d : ℚˣ, qcl d = c ∧ Cov ℚ a b d}`;
3. `Point ⧸ ker δ ≃ range δ`.

## What is NOT certified

`FORMALIZATION_LEVEL = EXPLICIT_2_ISOGENY_DESCENT_REALIZATION`
`ACTUAL_H1_SELMER_OBJECT = NO`

Not proved, not assumed, not named by either run:

- `ker δ_{E′} = φ(E(ℚ))` and `ker δ_E = φ̂(E′(ℚ))` — **the next missing identification**;
- therefore `E(ℚ)/2E(ℚ)` is not reached, and `Point ⧸ ker δ` is not an isogeny cokernel;
- `Sel₂`, Ш, rank, BSD. Nothing here touches `L(E,s)`.

Neither development contains anything about `φ`, `φ̂`, `E_q(ℚ)[2] = {O,T}` for the frozen
family, or base change of `δ`. P01 and P03a–e are entirely open.

## Project state

| result | tier |
|---|---|
| Theorem F | `LEAN_CERTIFIED`, two runs |
| `S_dyadic` | `LEAN_CERTIFIED`, two runs |
| `H₄₁` saturation | `LEAN_CERTIFIED`, two runs |
| **δ actual-point descent** | **`LEAN_CERTIFIED`, two runs** ← changed by this object |
| Theorem A | `DOUBLE_INDEPENDENT_CONVENTIONAL_PROOF`, not formalized |
| Theorem B | `CONVENTIONAL, BASE-CONDITIONED, LITERATURE-DEPENDENT` |

Across all four formal results, "independent" means independent **Aristotle proof-search
runs** on the same Lean kernel and the same mathlib revision. A soundness defect in Lean or
mathlib would affect every run identically.

`PRIOR_ART_BLOCKER` for 66b1 remains `UNRESOLVED`. No novelty is claimed.
