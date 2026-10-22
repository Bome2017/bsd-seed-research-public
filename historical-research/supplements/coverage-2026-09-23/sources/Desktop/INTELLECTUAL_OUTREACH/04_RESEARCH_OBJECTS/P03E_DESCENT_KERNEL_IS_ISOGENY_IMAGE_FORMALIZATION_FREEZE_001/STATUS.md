# P03E_DESCENT_KERNEL_IS_ISOGENY_IMAGE_FORMALIZATION_FREEZE_001 — status

`OBJECT_TYPE = CANONICAL_FREEZE`
`DATE = 2026-09-11`
`MATHEMATICS_ADDED_BY_THIS_OBJECT = NONE`

```text
P03E_CERTIFICATION = DOUBLE_INDEPENDENT_LEAN_CERTIFIED
RUN_A = CLEAN   (8040 jobs, Bridge.lean 386 lines, 11 helper lemmas added)
RUN_B = CLEAN   (8040 jobs, Bridge.lean 405 lines, 12 helper lemmas added)

INPUT_IDENTITY              = BYTE_IDENTICAL   (both given 1daf41ef…70ae4f8a)
TARGET_STATEMENT_IDENTITY   = BYTE_IDENTICAL
INHERITED_SOURCES_UNTOUCHED = 12/12 byte-identical in both runs
SHARED_HELPER_NAMES         = 4  (forced by the statement and by TASK.md)
REVERSE CONSTRUCTIONS       = DIFFERENT — built twice, differently

PROHIBITED_CONSTRUCTS   = 0  (both)
AXIOM_FOOTPRINT         = [propext, Classical.choice, Quot.sound]  (both)
SORRYAX                 = ABSENT
FORBIDDEN_TOKENS_IN_CODE = 0  (no quotient, subgroup, cokernel, Fintype, Nat.card,
                               rank, Sel₂ or Ш anywhere in code — comments stripped)

REPLICATION_STRENGTH = CONSTRUCTIVE ARCHITECTURAL CROSS-CHECK
WRAPPER_DEFECTS      = RUN_A partial (19/33 handoff files); RUN_B stale metadata (30/32)
```

## What is certified

    ∀ P  : E_q(ℚ),   δ_E(P)   = 1  ↔  ∃ P', φ̂(P') = P
    ∀ P' : E'_q(ℚ),  δ_{E'}(P') = 1  ↔  ∃ P,  φ(P)  = P'

i.e. **`ker δ_E = im φ̂` and `ker δ_{E'} = im φ`**, with the orientation the Pro audits
insisted on, in mathlib's own group law.

This is the bridge. The δ maps come from the audited 62a1 descent core (`Descent/Delta.lean`,
`Run013/Basic.lean`); the φ maps come from the point-level package built in P03a–P03d. Until
now those two halves of the project were only known to agree numerically. They are now proved
to be the same subgroup.

## Why the hard direction is the whole point

Forward (`∃ P' ⟹ δ = 1`) is computation. The reverse — from "the square class is trivial"
produce **an actual rational point on the other curve** — requires extracting a square root
and constructing a genuine point, and it is where a proof could have cheated by importing
rank, finiteness, or an unformalized isogeny theorem. Neither run did:

`receipts/RUN_{A,B}_INDEPENDENT_VERIFICATION.txt` §6 shows, with comments stripped,
**zero** code occurrences of `Quotient`, `QuotientAddGroup`, `AddSubgroup`, `cokernel`,
`Fintype`, `Finite`, `Nat.card`, `rank`, `Sel₂`, `Ш`. Both reverse directions are explicit
constructions.

## The replication

Four shared helper names — `cls_phiB_ne_one`, `dualPhiPoint_Qpt`, `exists_phi_preimage`,
`exists_dualPhi_preimage` — all forced by the statement and by the handoff's own TASK.md,
which named the two exceptional behaviours as self-consistency checks. Beyond those the
constructions differ:

    Run A   phi_preimage_coords / dualPhi_preimage_coords — generic coordinate solvers that
            take a square abscissa and directly manufacture the opposite-curve coordinates.

    Run B   phi_preimage_core / dual_preimage_core — separates the polynomial construction
            first, builds the actual point preimages afterwards, isolates dualB_eq_sq.

`receipts/PROOF_DIVERGENCE_MEASUREMENT.txt` calibrates this against every earlier stage. P03e
sits below P03b/P03d (0 shared names) and well above confirmation-grade P03c (2 lines differ).

## What the cross-run probe adds

One probe file, byte-identical, compiled against **both** developments
(`receipts/CROSS_RUN_SEMANTIC_CHECK.txt`). Besides instantiating the bridge at
(ε,m,q) = (1,3,13) and (−1,3,5) it proves, through the theorem:

| | |
|---|---|
| `T_in_image` | `T ∈ im φ̂`, because `δ_E(T) = [b] = [r²q²]` is a square |
| `T'_not_in_image` | `T' ∉ im φ`, because `δ_{E'}(T') = [D q²] = [D]` is not — that is `Params.legendre_D_q` |

The certified Legendre obstruction from P01 and the certified image of the isogeny now meet
at exactly the awkward exceptional points, **proved through the bridge** rather than checked
numerically as it was before the handoff was sent.

## Wording that must stay precise

`FORMALIZATION_LEVEL = EXPLICIT_2_ISOGENY_DESCENT_REALIZATION`
`ACTUAL_H1_SELMER_OBJECT = NO`

We have built a **point-level homomorphism package with certified kernels, composites and
image characterisation**. We have **not** created a mathlib algebraic-geometric `Isogeny`
object, and P03e is not a cohomological statement. Nothing here is a Selmer group.

## What is NOT certified

| | stage |
|---|---|
| `E'_q(ℚ)/φ(E_q(ℚ))` as an actual quotient group | **P04a** |
| `range(δ_{E'}) = G_{φ,exp}` — reconnecting saturation | P04b |
| `E_q(ℚ)/2E_q(ℚ) ≅ C₂` | P04c |
| `Sel₂`, Ш, rank, BSD | further out |

## The formal ladder

    F → S_dyadic → H₄₁ saturation → δ → P01 → P03a → P03b → P03c → P03d → P03e

| result | tier |
|---|---|
| Theorem F, `S_dyadic`, `H₄₁` saturation, δ, P01, P03a, P03b | `LEAN_CERTIFIED`, two runs |
| P03c bundled homs + kernels | `LEAN_CERTIFIED`, two runs — confirmation-grade |
| P03d dual composites | `LEAN_CERTIFIED`, two runs — architectural cross-check |
| **P03e descent kernel = isogeny image** | **`LEAN_CERTIFIED`, two runs — constructive cross-check** |
| Theorem A | `DOUBLE_INDEPENDENT_CONVENTIONAL_PROOF`, not formalized |
| Theorem B | `CONVENTIONAL, BASE-CONDITIONED, LITERATURE-DEPENDENT` |

**P03 is closed.** The point-level bridge the two hostile Pro audits prescribed is built:
actual maps, additivity, exact kernels, dual composites, and now the image characterisation.

## Continuation base

**Run B.** `phi_preimage_core` / `dual_preimage_core` separate the polynomial construction
from the point construction, and `dualB_eq_sq` is an explicitly named standalone fact. P04a
needs the surjection onto `range(δ_{E'})` as a map-level statement, which is easier to state
over Run B's split.

`PRIOR_ART_BLOCKER` for 66b1 remains `UNRESOLVED`. No novelty is claimed.

## Next

**P04a — actual isogeny cokernels.** First isomorphism theorem plus P03e:
`E'_q(ℚ)/φ(E_q(ℚ)) ≅ range(δ_{E'})` and `E_q(ℚ)/φ̂(E'_q(ℚ)) ≅ range(δ_E)`. No Sel₂.
