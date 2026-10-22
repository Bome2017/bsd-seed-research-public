# P04B_SATURATION_RECONNECT_FORMALIZATION_FREEZE_001 — status

`OBJECT_TYPE = CANONICAL_FREEZE`
`DATE = 2026-09-11`
`MATHEMATICS_ADDED_BY_THIS_OBJECT = NONE`

```text
P04B_CERTIFICATION = DOUBLE_INDEPENDENT_LEAN_CERTIFIED
RUN_A = CLEAN   (8055 jobs, Reconnect.lean 290 lines, 12 helper lemmas added)
RUN_B = CLEAN   (8055 jobs, Reconnect.lean 285 lines, 15 helper lemmas added)

INPUT_IDENTITY              = BYTE_IDENTICAL   (both given 7d7daa55…cb968167)
TARGET_STATEMENT_IDENTITY   = BYTE_IDENTICAL
INHERITED_SOURCES_UNTOUCHED = 29/29 byte-identical in both runs
SHARED_HELPER_NAMES         = 5   (reported only for continuity; carries no grade)
ROLE-MATCHED HELPERS        = 3 of 12 / 3 of 15 — the decompositions are NOT in bijection
NORMALISED LINE DIVERGENCE  = ~131% of the larger file (P04a, for calibration: 39%)
CITATION PROFILE            = DIFFERENT: Run A cites sdyadic_saturation twice, Run B never

PROHIBITED_CONSTRUCTS   = 0  (both)
AXIOM_FOOTPRINT         = [propext, Classical.choice, Quot.sound]  (both)
SORRYAX                 = ABSENT
FORBIDDEN_TOKENS_IN_CODE = 0 in Reconnect.lean — no quotient, no index, no subgroupOf,
                           no Fintype/Finite/Nat.card/Finset/card

REPLICATION_STRENGTH = ARCHITECTURAL CROSS-CHECK — strongest on the citation axis since P03e
WRAPPER_DEFECTS      = both stale metadata (47/49); twelfth and thirteenth occurrences
```

## What is certified

    range δ_{E'}   = GphiExp = ⟨[D],[q]⟩
    range δ_E      = {1}                      (elementwise, and as `= ⊥`)
    δ_{E'}(ker φ̂)  = KExp    = ⟨[D]⟩

**The two branches of the programme are now one Lean development.** The H₄₁ saturation theorem,
proved entirely in the language of square classes, and the point-level 2-isogeny package,
proved in mathlib's group law, had never been compiled together before this stage. They merge
with **zero declaration collisions** and are now known to be describing the same subgroups of
`ℚ*/ℚ*²`.

## The orientation correction is now formal

`KExp` is **not** `range δ_E`. It is the image of `ker φ̂` under `δ_{E'}`, which is the third
conjunct. `range δ_E` is trivial. That correction was made by reading the frozen saturation
sources — `SDyadic.dual_exhaustion` allows only the class `1`, and `cov_dual_one` is the only
dual witness — before any Lean statement was written, so the wrong identification never
entered a frozen object. It is now a certified theorem rather than a reading.

## What the cross-run probe adds

One probe, byte-identical, naming no run-specific helper. In **both** developments:

| | |
|---|---|
| `delta_E_trivial` | **every** rational point of `E_q` has trivial descent class — the whole family, not a sample |
| `every_point_in_image_dualPhi` | therefore every rational point of `E_q` is in `im φ̂` |
| `coker_dualPhi_trivial` | the P04a quotient `E_q(ℚ) ⧸ φ̂(E'_q(ℚ))` is the **trivial group** |
| `KExp_le_GphiExp` | derived from conjuncts 1 and 4, not assumed |
| `cls_DD_is_delta_of_T'pt` | `δ_{E'}(T') = [D]` |

`coker φ̂ = 0` was previously a bounded numerical observation. It is now a theorem about an
actual quotient object.

## The replication, measured three ways

Five shared helper names — and that number runs **backwards** here: P04a scored 0 and was
confirmation-grade, P04b scores 5 and is a cross-check. Per the P04a correction (ERRATA E7) the
count is reported only for continuity. The measurements that carry the grade:

1. **Only 3 of the added helpers role-match one-to-one** (the three conjunct theorems). Run A's
   other 4 and Run B's other 10 have no counterpart; the decompositions are not in bijection.
   P04a had 8 of 10 matching.
2. **Normalised line divergence ~131%** of the larger file after α-renaming the role matches
   and stripping comments — essentially the whole proof body. P04a: 39%.
3. **Different entry point into the certified inputs.** Run A takes `Cov ⟹ LocalKummerAll`
   from `sdyadic_saturation`'s first component; Run B never cites `sdyadic_saturation` at all
   and derives that step from `Run013.localKummerAll_iff_cov` with `cov_base_change`, using
   only the two exhaustion theorems from the saturation tree. Both are certified material.

Structurally: Run A repackages the additive range as an honest `Subgroup Qsq` and applies
`Subgroup.closure_le` once; Run B never repackages and closes the same inclusion by
`Subgroup.closure_induction` elementwise, having first factored the forward direction into two
reusable square-class lemmas (`cls_mem_GphiExp_of_cov`, `cls_eq_one_of_cov_dual`) in which no
point group appears.

**Honest note on what was consumed.** Neither proof needs the *hard* direction of the
saturation equivalence. Both need only `Cov ⟹ LocalKummerAll` (base change) plus
`phi_exhaustion` / `dual_exhaustion` — which are the hard local analysis, taken at lemma level.
The headline `GlobalSet = SelmerSet` is not a dependency of either P04b proof. This does not
weaken P04b; a name-level comparison would simply have hidden it.

## Wording that must stay precise

`FORMALIZATION_LEVEL = EXPLICIT_2_ISOGENY_DESCENT_REALIZATION`
`ACTUAL_H1_SELMER_OBJECT = NO`

Three subgroup identities in `ℚ*/ℚ*²`. No quotient was formed, and **no index, order or
cardinality was stated** — the certified `((KExp ε m).subgroupOf (GphiExp ε m q)).index = 2`
was deliberately not touched. Still not `E(ℚ)/2E(ℚ)`, not `Sel₂`, not Ш, not rank, not `L(E,s)`.

## What is NOT certified

| | stage |
|---|---|
| `E_q(ℚ)/2E_q(ℚ) ≅ GphiExp/KExp`, hence `≅ C₂` | **P04c — the finish line** |
| `Sel₂`, Ш, rank, BSD | a separate phase, with its own go/no-go |

## The formal ladder

    F → S_dyadic → H₄₁ saturation → δ → P01 → P03a → P03b → P03c → P03d → P03e → P04a → P04b

| result | tier |
|---|---|
| Theorem F, `S_dyadic`, `H₄₁` saturation, δ, P01, P03a, P03b | `LEAN_CERTIFIED`, two runs |
| P03c bundled homs + kernels | `LEAN_CERTIFIED`, two runs — confirmation-grade |
| P03d dual composites | `LEAN_CERTIFIED`, two runs — architectural cross-check |
| P03e descent kernel = isogeny image | `LEAN_CERTIFIED`, two runs — constructive cross-check |
| P04a isogeny cokernels | `LEAN_CERTIFIED`, two runs — confirmation-grade |
| **P04b saturation reconnect** | **`LEAN_CERTIFIED`, two runs — architectural cross-check** |
| Theorem A | `DOUBLE_INDEPENDENT_CONVENTIONAL_PROOF`, not formalized |
| Theorem B | `CONVENTIONAL, BASE-CONDITIONED, LITERATURE-DEPENDENT` |

## Continuation base

**Run B.** `cls_mem_GphiExp_of_cov` and `cls_eq_one_of_cov_dual` are statements about square
classes and coverings with no point group in them, which is the level P04c's abstract
two-map argument will want to quote; `deltaHomE'_T'pt` names the descent class of `T'`
standalone; and Run B's proof has one fewer dependency, since it does not go through
`sdyadic_saturation`. Run A's `rangeDeltaE'` subgroup packaging is elegant but is a coercion
device rather than an arithmetic fact.

`PRIOR_ART_BLOCKER` for 66b1 remains `UNRESOLVED`. No novelty is claimed.

## Next

**P04c** — `E_q(ℚ)/2E_q(ℚ) ≅ GphiExp/KExp`, then `≅ C₂` from the certified index-2 fact. All
four inputs to the standard two-map cokernel argument are now theorems in one project:
`φ̂ ∘ φ = [2]` (P03d), `ker φ̂ = {O,T'}` (P03c), `coker φ ≅ GphiExp` (P04a + P04b),
`coker φ̂ = 0` and `KExp ≤ GphiExp` (this object's probe).
