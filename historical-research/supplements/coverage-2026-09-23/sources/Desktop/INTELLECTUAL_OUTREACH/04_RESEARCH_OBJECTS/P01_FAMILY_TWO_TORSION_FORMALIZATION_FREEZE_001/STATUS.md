# P01_FAMILY_TWO_TORSION_FORMALIZATION_FREEZE_001 — status

`OBJECT_TYPE = CANONICAL_FREEZE`
`DATE = 2026-09-11`
`MATHEMATICS_ADDED_BY_THIS_OBJECT = NONE`

```text
P01_CERTIFICATION = DOUBLE_INDEPENDENT_LEAN_CERTIFIED
RUN_A = CLEAN   (8034 jobs, TwoTorsion.lean 346 lines, 42 declarations, 16 added)
RUN_B = CLEAN   (8034 jobs, TwoTorsion.lean 329 lines, 31 declarations,  5 added)

INPUT_IDENTITY            = BYTE_IDENTICAL   (both given fe845046…d489e2)
TARGET_STATEMENT_IDENTITY = BYTE_IDENTICAL   (26/26 shipped declarations, 78 comparisons)
CERTIFIED_INPUTS_UNTOUCHED = 7/7 byte-identical in both runs
HELPER_OVERLAP_BEYOND_HANDOFF = 1 name (Wab_negY_eq, a one-line negY unfolding)
INTERFACE_EQUIVALENT      = YES (one probe compiles unchanged against both)

PROHIBITED_CONSTRUCTS   = 0  (both runs)
AXIOM_FOOTPRINT         = [propext, Classical.choice, Quot.sound]  (both runs)
SORRYAX                 = ABSENT  (both runs)
FORBIDDEN_TOKENS_IN_CODE = 0  (both runs; 'ker' does not occur at all)
NON_VACUITY             = SHIPPED AND UNTOUCHED (Params 1 3 13 and Params (-1) 3 5)

INDEPENDENCE_CLASS = PROOF_SEARCH_INDEPENDENCE_UNDER_IDENTICAL_SUPPLIED_MATHEMATICS
PACKAGING_DEFECT   = PRESENT IN BOTH RETURNS (fourth and fifth consecutive occurrence)
CONTINUATION_BASE_RECOMMENDATION = RUN_A + 2 lemmas ported from RUN_B
```

## What is certified

Under the frozen `Params`, on **mathlib's own** nonsingular point groups:

    E_q  : y² = x(x² + A q x + r² q²)        E'_q : Y² = X(X − q)(X − D q)

- both models are nonsingular;
- `T = (0,0)` on `E_q`; `T' = (0,0)`, `Q = (q,0)`, `R = (Dq,0)` on `E'_q`, all nonzero and
  pairwise distinct;
- **`E_q(ℚ)[2] = {O, T}`**;
- **`E'_q(ℚ)[2] = {O, T', Q, R}`**.

The hypothesis is demonstrably satisfiable: `Params 1 3 13` (`D = −31`) and
`Params (-1) 3 5` (`D = 33 = 3·11`) are proved in the shipped `P01/Instances.lean`, which
**neither run modified**. The cross-run probe extracts both classifications at both witnesses
as named theorems with standard axioms.

## What is NOT certified

`FORMALIZATION_LEVEL = EXPLICIT_2_ISOGENY_DESCENT_REALIZATION`
`ACTUAL_H1_SELMER_OBJECT = NO`

`{O, T}` and `{O, T', Q, R}` are rational **2-torsion sets**. Neither is called a kernel, and
the string `ker` does not occur in either development. Not proved, not assumed, not named:
`φ`, `φ̂`, any isogeny, any kernel identity, `[2]` composites, base change, `E(ℚ)/2E(ℚ)`,
`Sel₂`, Ш, rank, BSD. Nothing here touches `L(E,s)`.

## The independence caveat — do not drop this line

The handoff's `TASK.md` spelled out the route, including the full Legendre obstruction chain.
So, as with Delta:

> **This is proof-search independence under identical supplied mathematics. It is not
> independent discovery of the mechanism, and it is not independent proof-assistant
> verification.**

What replicated is the formalization, twice, from helper layers sharing one trivial lemma.
Saturation retains the stronger class, because its local-exhaustion architecture was not
supplied.

## The formal ladder

    F  →  S_dyadic  →  H₄₁ saturation  →  δ actual-point descent  →  P01 actual family 2-torsion

| result | tier |
|---|---|
| Theorem F | `LEAN_CERTIFIED`, two runs |
| `S_dyadic` | `LEAN_CERTIFIED`, two runs |
| `H₄₁` saturation | `LEAN_CERTIFIED`, two runs |
| δ actual-point descent | `LEAN_CERTIFIED`, two runs |
| **P01 actual family 2-torsion** | **`LEAN_CERTIFIED`, two runs** ← this object |
| Theorem A | `DOUBLE_INDEPENDENT_CONVENTIONAL_PROOF`, not formalized |
| Theorem B | `CONVENTIONAL, BASE-CONDITIONED, LITERATURE-DEPENDENT` |

Throughout, "independent" means independent **Aristotle proof-search runs** on the same Lean
kernel and the same mathlib revision. A soundness defect in Lean or mathlib affects every run
identically.

`PRIOR_ART_BLOCKER` for 66b1 remains `UNRESOLVED`. No novelty is claimed.

## Next

P03a: define total `φ` and `φ̂` with all exceptional cases, and prove only that every input
point maps to an actual point on the opposite curve. No homomorphism, no kernels, no `[2]`
composites, no descent-kernel identity.
