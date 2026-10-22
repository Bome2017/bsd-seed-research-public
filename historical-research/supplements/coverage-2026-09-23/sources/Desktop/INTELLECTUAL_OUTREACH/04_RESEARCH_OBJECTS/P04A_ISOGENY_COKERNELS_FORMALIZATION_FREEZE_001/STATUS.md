# P04A_ISOGENY_COKERNELS_FORMALIZATION_FREEZE_001 — status

`OBJECT_TYPE = CANONICAL_FREEZE`
`DATE = 2026-09-11`
`MATHEMATICS_ADDED_BY_THIS_OBJECT = NONE`

```text
P04A_CERTIFICATION = DOUBLE_INDEPENDENT_LEAN_CERTIFIED
RUN_A = CLEAN   (8041 jobs, Cokernels.lean 224 lines, 10 helper lemmas added)
RUN_B = CLEAN   (8041 jobs, Cokernels.lean 220 lines,  9 helper lemmas added)

INPUT_IDENTITY              = BYTE_IDENTICAL   (both given 03394e93…764a95c4)
TARGET_STATEMENT_IDENTITY   = BYTE_IDENTICAL   (9a660dd5… in all three copies)
INHERITED_SOURCES_UNTOUCHED = 14/14 byte-identical in both runs
SHARED_HELPER_NAMES         = 0  — AND THAT NUMBER IS MISLEADING HERE, see below
ROUTES                      = THE SAME

PROHIBITED_CONSTRUCTS   = 0  (both)
AXIOM_FOOTPRINT         = [propext, Classical.choice, Quot.sound]  (both)
SORRYAX                 = ABSENT
FORBIDDEN_TOKENS_IN_CODE = 0 in Cokernels.lean — no Fintype, Finite, Nat.card, card,
                           Finset, SelmerSet, LocalKummerAll, rank, Sel₂, Ш, BSD

REPLICATION_STRENGTH = CONFIRMATION-GRADE — predicted before the handoff was sent, and
                       now measured rather than asserted
WRAPPER_DEFECTS      = both stale metadata (33/35); tenth and eleventh occurrences
```

## What is certified

    ker δ_{E'} = range φ            ker δ_E = range φ̂           (as AddSubgroups)

    E'_q(ℚ) ⧸ φ(E_q(ℚ))   ≃+   range δ_{E'}
    E_q(ℚ)  ⧸ φ̂(E'_q(ℚ))  ≃+   range δ_E

each isomorphism **induced by the corresponding descent map itself** — the statement carries
the clause `e ⟦P⟧ = δ(P)`, so this is not the weak claim that two groups happen to be
abstractly isomorphic. Plus:

* the class of `T'` is **nonzero** in `E'_q(ℚ) ⧸ φ(E_q(ℚ))` — the cokernel is not trivial;
* `range δ_{E'}` is the set of square classes with a rational point on the quartic covering.

These are the first **actual quotient groups** in the development. Everything before P04a was
maps and identities.

## Why the nontriviality conjunct is the one that matters

`δ_{E'}(T') = [D q²] = [D]`, and `Params.legendre_D_q` says `D` is a nonsquare mod `q`. That
obstruction has been certified since P01, but until now it could only be stated about square
classes. It is now visible as **nontriviality of an actual point cokernel**.

The cross-run probe proves the complementary pair through the quotient objects themselves, in
both developments:

| | |
|---|---|
| `coker_dual_kills_T` | class of `T` **= 0** in `E_q(ℚ) ⧸ φ̂(E'_q(ℚ))`, because `δ_E(T) = [r²q²]` is a square |
| `coker_phi_nontrivial` | class of `T'` **≠ 0** in `E'_q(ℚ) ⧸ φ(E_q(ℚ))`, at both certified instances |

## The replication, and a correction to how we have been measuring it

**P04a is confirmation-grade.** The two runs took the same route: same six facts, same
`quotientAddEquivOfEq ∘ quotientKerEquivRange` term, same `rfl` canonical-map clauses, same
final `exact ⟨…⟩`. After α-renaming the eight role-matched helpers and stripping comments,
89 versus 94 code lines with 37 differing, and every difference is a local tactic choice.

This was predicted in the handoff itself before it was sent, so the prediction is now measured.

**The correction.** P04a scores **0 shared helper names** — the same score as P03b and P03d,
which were genuine architectural cross-checks. Here the zero means only that the two runs
chose different *names* for the same lemmas (`cokerEquivE'` versus `cokerPhiEquiv`, and so on:
eight one-to-one correspondences). Name overlap measures vocabulary, not architecture. From
P04a on it is reported only alongside a normalised route comparison; both are in
`receipts/PROOF_DIVERGENCE_MEASUREMENT.txt`.

Confirmation-grade is not a defect at this stage. P04a was scoped to turn a certified bridge
into stable quotient objects, and there is essentially one way to do that with Noether's first
isomorphism theorem. What two runs buy here is that the assembly is not idiosyncratic and that
both independently accepted the statement — canonical-map clauses included — as provable.

## Wording that must stay precise

`FORMALIZATION_LEVEL = EXPLICIT_2_ISOGENY_DESCENT_REALIZATION`
`ACTUAL_H1_SELMER_OBJECT = NO`

These are **isogeny cokernels for a single 2-isogeny**. They are not the 2-descent quotient,
not `E(ℚ)/2E(ℚ)`, and not a Selmer group. No finiteness or cardinality claim is made anywhere:
nothing here says how big either quotient is, only that one of them is not trivial.

## What is NOT certified

| | stage |
|---|---|
| `range δ_{E'} = G_{φ,exp}`, `range δ_E = K_exp` — reconnecting H₄₁ saturation | **P04b** |
| `E_q(ℚ)/2E_q(ℚ) ≅ G_{φ,exp}/K_exp ≅ C₂` | P04c |
| `Sel₂`, Ш, rank, BSD | a separate phase, with its own go/no-go |

## The formal ladder

    F → S_dyadic → H₄₁ saturation → δ → P01 → P03a → P03b → P03c → P03d → P03e → P04a

| result | tier |
|---|---|
| Theorem F, `S_dyadic`, `H₄₁` saturation, δ, P01, P03a, P03b | `LEAN_CERTIFIED`, two runs |
| P03c bundled homs + kernels | `LEAN_CERTIFIED`, two runs — confirmation-grade |
| P03d dual composites | `LEAN_CERTIFIED`, two runs — architectural cross-check |
| P03e descent kernel = isogeny image | `LEAN_CERTIFIED`, two runs — constructive cross-check |
| **P04a isogeny cokernels** | **`LEAN_CERTIFIED`, two runs — confirmation-grade** |
| Theorem A | `DOUBLE_INDEPENDENT_CONVENTIONAL_PROOF`, not formalized |
| Theorem B | `CONVENTIONAL, BASE-CONDITIONED, LITERATURE-DEPENDENT` |

## Continuation base

**Run B**, marginally. `delta_T'pt` is a standalone named fact of exactly the kind P04b needs —
the descent class of a specific point — and Run B's defensive `Additive`/`congrArg` spelling in
the range lemma is the one that will survive being reused against saturation's `Qsq`-level
statements. Run A's two `Iff.rfl` bridging lemmas are convenient but are not facts about the
arithmetic.

`PRIOR_ART_BLOCKER` for 66b1 remains `UNRESOLVED`. No novelty is claimed.

## Next

**P04b** — identify `range δ_{E'}` and `range δ_E` with the explicit H₄₁ square-class groups
already certified by saturation. Orientation must be read off the frozen saturation
definitions, not inferred from notation.
