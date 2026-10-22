# P03D_ISOGENY_COMPOSITES_FORMALIZATION_FREEZE_001 — status

`OBJECT_TYPE = CANONICAL_FREEZE`
`DATE = 2026-09-11`
`MATHEMATICS_ADDED_BY_THIS_OBJECT = NONE`

```text
P03D_CERTIFICATION = DOUBLE_INDEPENDENT_LEAN_CERTIFIED
RUN_A = CLEAN   (8039 jobs, Composites.lean 215 lines, 3 helper lemmas added)
RUN_B = CLEAN   (8039 jobs, Composites.lean 221 lines, 5 helper lemmas added)

INPUT_IDENTITY              = BYTE_IDENTICAL   (both given 6fb1b4ab…75c6f3f3)
TARGET_STATEMENT_IDENTITY   = BYTE_IDENTICAL
INHERITED_SOURCES_UNTOUCHED = 12/12 byte-identical in both runs
SHARED_HELPER_NAMES         = 0
ROUTES                      = MATERIALLY DIFFERENT — see below

PROHIBITED_CONSTRUCTS   = 0  (both)
AXIOM_FOOTPRINT         = [propext, Classical.choice, Quot.sound]  (both)
SORRYAX                 = ABSENT
FORBIDDEN_TOKENS_IN_CODE = 0  (RHS stayed P + P; no [2]/zsmul, no quotient, no image object)

REPLICATION_STRENGTH = ARCHITECTURAL CROSS-CHECK — the strong kind, unlike P03c
WRAPPER_DEFECTS      = RUN_A partial (19/31 files); RUN_B stale metadata (29/31)
```

## What is certified

    ∀ P : E_q(ℚ),   φ̂(φ(P))  = P + P
    ∀ P : E'_q(ℚ),  φ(φ̂(P)) = P + P

in mathlib's own group law, with no `[2]` abstraction introduced on either side.

**The point-level classical 2-isogeny package is now complete**: actual maps (P03a),
additivity (P03b), exact kernels (P03c), dual composites (P03d) — all double-run certified,
built manually because the pinned mathlib supplies no isogeny API.

## Wording that must stay precise

We have built the **point-level homomorphism package**. We have **not** created a mathlib
algebraic-geometric `Isogeny` object, and nothing here is one. The phrase to use is "a
manually constructed degree-2 point-map pair with certified kernels and composites", never
"the isogeny is formalized in mathlib".

## The replication is the strong kind

Zero shared helper names, and the two runs took **materially different routes**:

    Run A   gen_composite — a generic scaled-map composition theorem: if c·c' = 2 then
            g(f(P)) = P + P; instantiated at (c,c') = (1,2) and (2,1).

    Run B   double_of_coords, comp_phi_X/Y, comp_dual_X/Y — goes through mathlib's own
            tangent doubling law, identifying the composite's X- and Y-coordinates
            separately and matching them to addX/addY for P + P.

Structure-from-composition versus explicit-coordinates-into-mathlib's-doubling. Calibration
against every earlier stage is in `receipts/PROOF_DIVERGENCE_MEASUREMENT.txt`; P03d sits with
saturation and P03b in the architectural-cross-check class, **not** with confirmation-grade
P03c.

Run A's route also vindicates the P03b finding: both P03b runs independently discovered the
scaled-map reduction with `c = 1` and `c = 2`, and Run A's `gen_composite` is exactly the
`c·c' = 2` composition theorem that observation predicted would be useful here.

## What is NOT certified

`FORMALIZATION_LEVEL = EXPLICIT_2_ISOGENY_DESCENT_REALIZATION`
`ACTUAL_H1_SELMER_OBJECT = NO`

| | stage |
|---|---|
| `ker δ_E = im φ̂`, `ker δ_{E'} = im φ` | **P03e — the bridge** |
| `E'_q(ℚ)/φ(E_q(ℚ))` as an actual cokernel | after P03e |
| `E(ℚ)/2E(ℚ)`, `Sel₂`, Ш, rank, BSD | further out |

`S_dyadic` remains the explicit descent-realization object, **not** a cohomological elliptic
Selmer object.

## The formal ladder

    F → S_dyadic → H₄₁ saturation → δ → P01 → P03a → P03b → P03c → P03d

| result | tier |
|---|---|
| Theorem F, `S_dyadic`, `H₄₁` saturation, δ, P01, P03a, P03b | `LEAN_CERTIFIED`, two runs |
| P03c bundled homs + kernels | `LEAN_CERTIFIED`, two runs — **confirmation-grade** |
| **P03d dual composites** | **`LEAN_CERTIFIED`, two runs — architectural cross-check** |
| Theorem A | `DOUBLE_INDEPENDENT_CONVENTIONAL_PROOF`, not formalized |
| Theorem B | `CONVENTIONAL, BASE-CONDITIONED, LITERATURE-DEPENDENT` |

## Continuation base

**Run B**, marginally. Its `comp_phi_X`, `comp_phi_Y`, `comp_dual_X`, `comp_dual_Y` give the
composite's coordinates as standalone named facts, and P03e works at exactly that level — it
must relate a coordinate's square class to the existence of a preimage. Run A's
`gen_composite` is the more elegant object but is about composition structure rather than
coordinates, which is one level too abstract for P03e.

`PRIOR_ART_BLOCKER` for 66b1 remains `UNRESOLVED`. No novelty is claimed.

## Next

**P03e**: `δ_E(P) = 1 ↔ ∃ P', φ̂(P') = P` and `δ_{E'}(P') = 1 ↔ ∃ P, φ(P) = P'`.
