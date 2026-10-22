# P03B_ISOGENY_ADDITIVITY_FORMALIZATION_FREEZE_001 — status

`OBJECT_TYPE = CANONICAL_FREEZE`
`DATE = 2026-09-11`
`MATHEMATICS_ADDED_BY_THIS_OBJECT = NONE`

```text
P03B_CERTIFICATION = DOUBLE_INDEPENDENT_LEAN_CERTIFIED
RUN_A = CLEAN   (8037 jobs, Additivity.lean 532 lines, 13 declarations, 12 added)
RUN_B = CLEAN   (8037 jobs, Additivity.lean 610 lines, 18 declarations, 17 added)

INPUT_IDENTITY            = BYTE_IDENTICAL   (both given 632f8f93…fe3fde23)
TARGET_STATEMENT_IDENTITY = BYTE_IDENTICAL
INHERITED_SOURCES_UNTOUCHED = 10/10 byte-identical in both runs
SHARED_HELPER_NAMES       = 0   — the most disjoint pair at any stage
INTERFACE_EQUIVALENT      = YES (one probe compiles unchanged against both)

PROHIBITED_CONSTRUCTS   = 0  (both runs)
AXIOM_FOOTPRINT         = [propext, Classical.choice, Quot.sound]  (both, 16 objects)
SORRYAX                 = ABSENT
FORBIDDEN_TOKENS_IN_CODE = 0  (no 'ker', no MonoidHom/AddMonoidHom/MulHom, no composite)

INDEPENDENCE_CLASS = PROOF_SEARCH_INDEPENDENCE_UNDER_IDENTICAL_SUPPLIED_MATHEMATICS
WRAPPER_DEFECT     = stale metadata in both, 26/28 — seventh consecutive occurrence
CONTINUATION_BASE_RECOMMENDATION = RUN_B, weakly
```

## What is certified

On mathlib's actual rational-point groups of the frozen family, for the certified P03a total
maps:

    ∀ P Q,  φ(P + Q)  = φ(P)  + φ(Q)
    ∀ P Q,  φ̂(P + Q) = φ̂(P) + φ̂(Q)

The maps are no longer merely rational coordinate functions that happen to land on the other
curve. **They are certified group-homomorphic functions.** They have deliberately not been
*bundled* as `AddMonoidHom`s — that is P03c's first step — but mathematically the homomorphism
property is established.

## What is NOT certified

`FORMALIZATION_LEVEL = EXPLICIT_2_ISOGENY_DESCENT_REALIZATION`
`ACTUAL_H1_SELMER_OBJECT = NO`

| | stage |
|---|---|
| `ker φ = {O,T}`, `ker φ̂ = {O,T'}` | P03c |
| `φ̂ ∘ φ = [2]`, `φ ∘ φ̂ = [2]` | P03d |
| field-embedding naturality | P03e |
| `ker δ = im φ` | the boundary crossing |
| `E(ℚ)/2E(ℚ)`, `Sel₂`, Ш, rank, BSD | further out |

The string `ker` does not occur in either development's code, no homomorphism bundle is
constructed, and no composite identity is asserted. `S_dyadic` remains the explicit
descent-realization object, **not** a cohomological elliptic Selmer object.

## Independence caveat

The handoff named the case structure and pointed at `isogeny_core`, so the class is the usual
`PROOF_SEARCH_INDEPENDENCE_UNDER_IDENTICAL_SUPPLIED_MATHEMATICS`. But less was supplied here
than at any stage since saturation — no proof strategy for the chord/tangent algebra — and the
result shows it: **the two helper layers share no name at all**, and both independently found
the same scaled-map reduction that the handoff never mentioned. That convergence is a genuine
finding.

## The formal ladder

    F → S_dyadic → H₄₁ saturation → δ → P01 → P03a → P03b

| result | tier |
|---|---|
| Theorem F | `LEAN_CERTIFIED`, two runs |
| `S_dyadic` | `LEAN_CERTIFIED`, two runs |
| `H₄₁` saturation | `LEAN_CERTIFIED`, two runs |
| δ actual-point descent | `LEAN_CERTIFIED`, two runs |
| P01 actual family 2-torsion | `LEAN_CERTIFIED`, two runs |
| P03a actual isogeny point maps | `LEAN_CERTIFIED`, two runs |
| **P03b isogeny additivity** | **`LEAN_CERTIFIED`, two runs** ← this object |
| Theorem A | `DOUBLE_INDEPENDENT_CONVENTIONAL_PROOF`, not formalized |
| Theorem B | `CONVENTIONAL, BASE-CONDITIONED, LITERATURE-DEPENDENT` |

"Independent" means independent **Aristotle proof-search runs** on the same Lean kernel and
the same mathlib revision.

`PRIOR_ART_BLOCKER` for 66b1 remains `UNRESOLVED`. No novelty is claimed.

## Next

**P03c**: bundle `φ` and `φ̂` as additive homomorphisms using this theorem for `map_add`, then
prove `ker φ_hom = {O,T}` and `ker φ̂_hom = {O,T'}`. No `[2]` composites.
