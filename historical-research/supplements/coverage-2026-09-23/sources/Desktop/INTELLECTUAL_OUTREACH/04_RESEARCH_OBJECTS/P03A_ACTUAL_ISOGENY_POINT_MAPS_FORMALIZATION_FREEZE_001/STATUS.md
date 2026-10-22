# P03A_ACTUAL_ISOGENY_POINT_MAPS_FORMALIZATION_FREEZE_001 — status

`OBJECT_TYPE = CANONICAL_FREEZE`
`DATE = 2026-09-11`
`MATHEMATICS_ADDED_BY_THIS_OBJECT = NONE`

```text
P03A_CERTIFICATION = DOUBLE_INDEPENDENT_LEAN_CERTIFIED
RUN_A = CLEAN   (8036 jobs, PointMaps.lean 212 lines, 21 declarations, 6 added)
RUN_B = CLEAN   (8036 jobs, PointMaps.lean 216 lines, 22 declarations, 7 added)

INPUT_IDENTITY            = BYTE_IDENTICAL   (both given 565d3634…5500ebba)
TARGET_STATEMENT_IDENTITY = BYTE_IDENTICAL   (15/15 shipped declarations, 45 comparisons)
INHERITED_SOURCES_UNTOUCHED = 9/9 byte-identical in both runs
HELPER_OVERLAP            = 4 of the added lemmas are the same statements, renamed
INTERFACE_EQUIVALENT      = YES (one probe compiles unchanged against both)

PROHIBITED_CONSTRUCTS   = 0  (both runs)
AXIOM_FOOTPRINT         = [propext, Classical.choice, Quot.sound]  (both runs, 24 objects)
SORRYAX                 = ABSENT, including on phiPoint / dualPhiPoint / all branch lemmas
FORBIDDEN_TOKENS_IN_CODE = 0  (both runs; no 'ker', no homomorphism bundle, no composites)

INDEPENDENCE_CLASS = PROOF_SEARCH_INDEPENDENCE_UNDER_IDENTICAL_SUPPLIED_MATHEMATICS
WRAPPER_DEFECTS    = RUN_A partial (17/28 files); RUN_B stale metadata (6th occurrence)
CONTINUATION_BASE_RECOMMENDATION = RUN_B, nothing to port
```

## What is certified

On mathlib's own nonsingular point types, under the frozen `Params`:

    φ  : E_q(ℚ)  → E'_q(ℚ)        φ̂ : E'_q(ℚ) → E_q(ℚ)

as **total functions**, with

    O ↦ O ;   the exceptional x = 0 point ↦ O ;
    otherwise  φ : (x,y) ↦ ( y²/x² , y(b−x²)/x² )
               φ̂ : (X,Y) ↦ ( Y²/(4X²) , Y(b′−X²)/(8X²) )

and **every branch proved to construct a valid `Affine.Point`** — which is exactly the target
`isogeny_coords_nonsingular`, since `Affine.Point.some` takes precisely a `Nonsingular`
witness. Branch simp lemmas for all six cases, and the two named exceptional fibres
`φ(T) = O`, `φ̂(T') = O`.

Before this stage `φ` and `φ̂` existed only as classical formulas we intended to formalize.
After it, there are actual total functions between the genuine elliptic point types.

## What is NOT certified

`FORMALIZATION_LEVEL = EXPLICIT_2_ISOGENY_DESCENT_REALIZATION`
`ACTUAL_H1_SELMER_OBJECT = NO`

**These are not isogenies in any formal sense.** They are total functions whose outputs lie on
the opposite curve. Not proved, not assumed, not named — verified with comments stripped, in
both runs:

| | stage |
|---|---|
| `φ(P+Q) = φ(P) + φ(Q)` | P03b |
| `ker φ = {O,T}`, `ker φ̂ = {O,T'}` | P03c |
| `φ̂ ∘ φ = [2]`, `φ ∘ φ̂ = [2]` | P03d |
| field-embedding naturality | P03e |
| `ker δ = im φ` | the boundary crossing after P03e |
| `E(ℚ)/2E(ℚ)`, `Sel₂`, Ш, rank, BSD | further out |

The string `ker` does not occur in either development, no homomorphism bundle is constructed,
and `dualPhiPoint (Qpt hP) = Tpt hP` — a tempting one-liner — was forbidden and not proved.
`S_dyadic` remains the explicit descent-realization object, **not** a cohomological elliptic
Selmer object.

## The independence caveat

The handoff's `TASK.md` supplied the route in full, including the pivotal identity and both
coefficient bridges. So, as with Delta and P01:

> **Proof-search independence under identical supplied mathematics.** Not independent
> discovery of the mechanism, and not independent proof-assistant verification.

Saturation retains the stronger class, because its local-exhaustion architecture was not
supplied.

## The formal ladder

    F → S_dyadic → H₄₁ saturation → δ actual-point descent → P01 actual family 2-torsion → P03a actual isogeny point maps

| result | tier |
|---|---|
| Theorem F | `LEAN_CERTIFIED`, two runs |
| `S_dyadic` | `LEAN_CERTIFIED`, two runs |
| `H₄₁` saturation | `LEAN_CERTIFIED`, two runs |
| δ actual-point descent | `LEAN_CERTIFIED`, two runs |
| P01 actual family 2-torsion | `LEAN_CERTIFIED`, two runs |
| **P03a actual isogeny point maps** | **`LEAN_CERTIFIED`, two runs** ← this object |
| Theorem A | `DOUBLE_INDEPENDENT_CONVENTIONAL_PROOF`, not formalized |
| Theorem B | `CONVENTIONAL, BASE-CONDITIONED, LITERATURE-DEPENDENT` |

Throughout, "independent" means independent **Aristotle proof-search runs** on the same Lean
kernel and the same mathlib revision.

`PRIOR_ART_BLOCKER` for 66b1 remains `UNRESOLVED`. No novelty is claimed.

## Next

**P03b**: `φ(P+Q) = φ(P) + φ(Q)` and `φ̂(P+Q) = φ̂(P) + φ̂(Q)` for the total maps just
constructed. That is where they become genuine group homomorphisms. No kernels, no composites.
