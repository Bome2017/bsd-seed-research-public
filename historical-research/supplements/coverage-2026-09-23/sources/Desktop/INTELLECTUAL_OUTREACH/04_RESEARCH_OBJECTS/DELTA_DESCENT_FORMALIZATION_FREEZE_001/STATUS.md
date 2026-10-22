# DELTA_DESCENT_FORMALIZATION_FREEZE_001 — status

`OBJECT_TYPE = CANONICAL_FREEZE`
`DATE = 2026-09-11`
`MATHEMATICS_ADDED_BY_THIS_OBJECT = NONE` (packaging, verification and provenance only)

```text
DELTA_CERTIFICATION = LEAN_CERTIFIED_ONE_RUN
RUN_A = CLEAN   (8030 jobs, 4 modules, 27 declarations in Delta.lean)
RUN_B = NOT_YET_RUN

TARGET_STATEMENT_PRESERVED = YES  (byte-identical, hypotheses included)
DELTA_DEFINITION_PRESERVED = YES  (byte-identical)
CURVE_DEFINITION_PRESERVED = YES  (byte-identical)
V1_DECLARATIONS_REMOVED    = 0
V1_DECLARATIONS_WEAKENED   = 0
DECLARATIONS_ADDED         = 16  (all proved)

BUILD_SOURCE_SORRY      = 0
PROHIBITED_CONSTRUCTS   = 0
AXIOM_FOOTPRINT         = [propext, Classical.choice, Quot.sound]
SORRYAX                 = ABSENT

CLS_ZERO_TRAP_AVOIDED   = YES  (0 occurrences of `cls 0`)
FORBIDDEN_TOKENS_IN_CODE = 0   (Sel₂, Sha, rank, BSD, E/2E, isogeny, cokernel)
COV_IFF_INKUMMER        = USED_NOT_REPROVED
SEMANTIC_NONVACUITY     = VERIFIED_EXTERNALLY (receipts/semantic_probe.lean)

PACKAGING_DEFECT_IN_RETURN = YES, recorded as ERRATA E2, not repaired
```

## What is certified

For `a b : ℚ` with `b ≠ 0` and `a² − 4b ≠ 0`, on **mathlib's own** group of nonsingular
rational points of `W : y² = x³ + a·x² + b·x`, with **mathlib's own** `AddCommGroup`
instance, the map

    δ(O) = 1,   δ((0,0)) = [b],   δ((x,y)) = [x]  for x ≠ 0

satisfies:

1. `δ(P + Q) = δ(P)·δ(Q)`;
2. `range δ = {c | ∃ d : ℚˣ, qcl d = c ∧ Cov ℚ a b d}` — the certified global solubility set;
3. `Point ⧸ ker δ ≃ range δ`, by the existing first isomorphism theorem.

## Why this is a different kind of result from F, S_dyadic and saturation

Those three are statements about explicit square classes and quartic coverings. This is the
first certified statement in the project whose subject is an **actual arithmetic group
supplied by mathlib**. `Run013.KummerImage` was defined by coordinates; it is now known to be
the image of a genuine homomorphism.

## What is NOT certified

`FORMALIZATION_LEVEL = EXPLICIT_2_ISOGENY_DESCENT_REALIZATION`
`ACTUAL_H1_SELMER_OBJECT = NO`

Explicitly **not** proved, **not** assumed, **not** named:

- `ker δ_{E′} = φ(E(ℚ))` and `ker δ_E = φ̂(E′(ℚ))`. These need the actual `φ, φ̂` point maps,
  which do not exist yet. **This is the next missing identification.**
- Consequently `E(ℚ)/2E(ℚ)` is not reached. `Point ⧸ ker δ` is not an isogeny cokernel.
- `Sel₂`, Ш, rank, BSD. Nothing here touches `L(E,s)`.

## Certification tier

**One Aristotle run.** Not double. The original unchanged handoff
(`b75ba34edce636035eb2d4c22b998d70ab51298434ffb0ae8558ab58c25052d3`) is preserved in
`_external/originals/` precisely so a second account can be given the identical input.

"Lean certified" here means a proof search closed the target on the Lean 4.28.0 kernel at
mathlib `8f9d9cff…`, independently rebuilt and axiom-audited on this machine. It does not
mean independent proof-assistant verification.

## Project state after this object

| result | tier |
|---|---|
| Theorem F | `LEAN_CERTIFIED`, two runs |
| `S_dyadic` | `LEAN_CERTIFIED`, two runs |
| `H₄₁` saturation | `LEAN_CERTIFIED`, two runs |
| **δ actual-point descent** | **`LEAN_CERTIFIED`, one run** ← this object |
| Theorem A | `DOUBLE_INDEPENDENT_CONVENTIONAL_PROOF`, not formalized |
| Theorem B | `CONVENTIONAL, BASE-CONDITIONED, LITERATURE-DEPENDENT` |

`PRIOR_ART_BLOCKER` for 66b1 remains `UNRESOLVED`. No novelty is claimed.
