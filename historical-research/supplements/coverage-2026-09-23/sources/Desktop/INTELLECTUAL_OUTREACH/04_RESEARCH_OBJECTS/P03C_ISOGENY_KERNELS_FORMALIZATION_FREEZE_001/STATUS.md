# P03C_ISOGENY_KERNELS_FORMALIZATION_FREEZE_001 — status

`OBJECT_TYPE = CANONICAL_FREEZE`
`DATE = 2026-09-11`
`MATHEMATICS_ADDED_BY_THIS_OBJECT = NONE`

```text
P03C_CERTIFICATION = DOUBLE_RUN_LEAN_CERTIFIED
RUN_A = CLEAN   (8038 jobs, Kernels.lean 115 lines, 5 declarations, 0 added)
RUN_B = CLEAN   (8038 jobs, Kernels.lean 115 lines, 5 declarations, 0 added)

INPUT_IDENTITY              = BYTE_IDENTICAL   (both given bbd2f1f7…635919db)
TARGET_STATEMENT_IDENTITY   = BYTE_IDENTICAL
INHERITED_SOURCES_UNTOUCHED = 11/11 byte-identical in both runs
AUXILIARY_LEMMAS_ADDED      = 0 by either run
PROOF_DIVERGENCE            = 2 substantive lines, after binder normalisation

PROHIBITED_CONSTRUCTS   = 0  (both)
AXIOM_FOOTPRINT         = [propext, Classical.choice, Quot.sound]  (both)
SORRYAX                 = ABSENT
FORBIDDEN_TOKENS_IN_CODE = 0  (no composite, no naturality, no E/2E, Sel₂, Ш, rank)

REPLICATION_STRENGTH = WEAKEST_IN_THE_PROGRAMME — see below
WRAPPER_DEFECT       = stale metadata in both, 27/29 — ninth consecutive occurrence
```

## What is certified

`φ` and `φ̂` are now **actual `AddMonoidHom`s** between mathlib's rational point groups of the
frozen family, with

    ker φ_hom  = { O , T }        on E_q(ℚ)
    ker φ̂_hom = { O , T' }       on E'_q(ℚ)

The bundling was already proved in the handoff (it needs only P03b's `map_add`); the runs
supplied the kernel theorem.

Non-triviality is checked, not assumed: the cross-run probe proves `Q = (q,0)` is **not** in
`ker φ̂`, so the kernel is genuinely two elements and not the whole group.

## Read this before quoting "double-run certified"

**The replication value here is the weakest in the programme, and the freeze says so.**

Neither run added a single auxiliary lemma. After normalising binder names, the two proofs
differ in **exactly two lines** — both instances of closing the `x = 0` branch:

    Run A:  exact Or.inr rfl
    Run B:  exact Or.inr (Wab_pt_eq H (T_mem hP) rfl rfl)

Same tactic skeleton, same case split, same lemmas in the same order. Shared-name counts
across the programme, for calibration:

| stage | divergence |
|---|---|
| saturation | materially different architectures, no route supplied |
| P03b | 0 shared helper names, 12 vs 17 added lemmas |
| P01 | 1 shared name, 6 vs 5 added |
| Delta | 3 shared names, 13 vs 19 added |
| P03a | 4 shared names, 6 vs 7 added |
| **P03c** | **0 added lemmas either side; 2 substantive lines differ** |

This is not a defect. It is the predictable consequence of a handoff whose `TASK.md` supplied
the complete three-case route for a proof short enough that there is essentially one way to
write it — which is exactly what the staging was designed to produce.

**Stated plainly: P03c is double-run certified, and the second run should be read as a
confirmation run rather than an independent re-derivation.** Both searches closed the target,
both rebuild clean here, both carry standard axioms. That is real. It is not the architectural
cross-check that saturation and P03b provided.

`receipts/PROOF_DIVERGENCE_MEASUREMENT.txt` has the measurement.

## What is NOT certified

`FORMALIZATION_LEVEL = EXPLICIT_2_ISOGENY_DESCENT_REALIZATION`
`ACTUAL_H1_SELMER_OBJECT = NO`

| | stage |
|---|---|
| `φ̂ ∘ φ = [2]`, `φ ∘ φ̂ = [2]` | P03d |
| field-embedding naturality | P03e |
| `ker δ = im φ` | the boundary crossing |
| `E(ℚ)/2E(ℚ)`, `Sel₂`, Ш, rank, BSD | further out |

`S_dyadic` remains the explicit descent-realization object, **not** a cohomological elliptic
Selmer object.

## The formal ladder

    F → S_dyadic → H₄₁ saturation → δ → P01 → P03a → P03b → P03c

| result | tier |
|---|---|
| Theorem F | `LEAN_CERTIFIED`, two runs |
| `S_dyadic` | `LEAN_CERTIFIED`, two runs |
| `H₄₁` saturation | `LEAN_CERTIFIED`, two runs |
| δ actual-point descent | `LEAN_CERTIFIED`, two runs |
| P01 actual family 2-torsion | `LEAN_CERTIFIED`, two runs |
| P03a actual isogeny point maps | `LEAN_CERTIFIED`, two runs |
| P03b isogeny additivity | `LEAN_CERTIFIED`, two runs |
| **P03c bundled homs + exact kernels** | **`LEAN_CERTIFIED`, two runs (confirmation-grade)** |
| Theorem A | `DOUBLE_INDEPENDENT_CONVENTIONAL_PROOF`, not formalized |
| Theorem B | `CONVENTIONAL, BASE-CONDITIONED, LITERATURE-DEPENDENT` |

## Continuation base

Either. The two developments differ in two lines and expose an identical interface; the probe
compiles unchanged against both. **Run B** is marginally preferable because
`Wab_pt_eq ... rfl rfl` is a more robust idiom than relying on definitional proof irrelevance,
and it makes the dependence on P01's point-extensionality lemma explicit. That is a style
judgement, not a substantive one.

`PRIOR_ART_BLOCKER` for 66b1 remains `UNRESOLVED`. No novelty is claimed.

## Next

**P03d**: `φ̂(φ(P)) = P + P` and `φ(φ̂(P')) = P' + P'`, stated with mathlib's own group law
rather than a new `[2]` abstraction. No `ker δ = im φ`, no quotients, no `E(ℚ)/2E(ℚ)`.
