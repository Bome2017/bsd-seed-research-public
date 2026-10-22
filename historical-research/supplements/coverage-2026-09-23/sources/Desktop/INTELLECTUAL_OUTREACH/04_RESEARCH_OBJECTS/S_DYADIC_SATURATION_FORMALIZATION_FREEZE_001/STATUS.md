# Explicit descent saturation — formalization status

```text
SATURATION_THEOREM       = LEAN_CERTIFIED
IMPLEMENTATIONS          = ONE (Run A).  Run B still running; see "Relation to a future Freeze 002".
FORMALIZATION_LEVEL      = EXPLICIT_2_ISOGENY_DESCENT_REALIZATION
ACTUAL_H1_SELMER_OBJECT  = NO
EXPLICIT_QUOTIENT_IS_NOT_SEL2 = ACKNOWLEDGED
```

**No `sorryAx`.** Independently rebuilt and audited here, not taken on report.

## What is certified

On the certified `(4,1)` stratum `H₄₁`, for both coefficient pairs of the `S_dyadic` family:

    LocalKummerAll a b d  ⟺  Cov ℚ a b d        for every nonzero rational d

hence `GlobalSet = SelmerSet` for both pairs, and the explicit descent quotient

    ((KExp ε m).subgroupOf (GphiExp ε m q)).index = 2      i.e.  |⟨[D],[q]⟩/⟨[D]⟩| = 2

This is a **local-to-global saturation theorem**: every everywhere-locally-soluble square class for
these covering families is in fact **rationally** soluble.

## Independent verification performed here

```text
V2 archive  5e32f77f5b75732fb033f5d58138efa788f38be37b83b8a6184d67fd0c30568d   MATCH
successor root manifest
            4181a7073dc29c24c9af4bcaa8efae602416a83e210b666922805449da0a465b   MATCH
successor manifest replay   32/32 entries, 0 mismatches, 0 missing
lake build                  exit 0, 8042 jobs, no "declaration uses sorry"
construct scan              16 modules, 2 329 lines, 90 theorems, 13 lemmas
                            sorry 0 · admit 0 · axiom 0 · unsafe 0
                            native_decide 0 · ofReduceBool 0 · implemented_by 0 · extern 0
```

Axiom audit — **every** object, not just the target:

```text
SDyadic.sdyadic_saturation   [propext, Classical.choice, Quot.sound]
SDyadic.GlobalSet            [propext, Classical.choice, Quot.sound]
SDyadic.H41                  [propext, Classical.choice, Quot.sound]
Run013.Cov                   [propext, Classical.choice, Quot.sound]
Run013.LocalKummerAll        [propext, Classical.choice, Quot.sound]
SDyadic.phi_exhaustion       [propext, Classical.choice, Quot.sound]
SDyadic.dual_exhaustion      [propext, Classical.choice, Quot.sound]
```

The `docs/MANIFEST.sha256` shipped in the return hashes to `7166fb79…684340a4`, which is exactly the
root manifest of the V1 handoff — so the input identity is independently confirmed from the return
side as well.

## The two semantic traps, both checked

**1. `Cov ℚ` is the genuine covering predicate**, not a stand-in:

```lean
def Cov (K : Type*) [Field K] (a b d : K) : Prop :=
  ∃ u v n : K, ¬(u = 0 ∧ v = 0) ∧ n ^ 2 = d * u ^ 4 + a * u ^ 2 * v ^ 2 + (b / d) * v ^ 4
```

and `GlobalSet` is defined **by it**, byte-identical to the handoff — **not** as membership in an
asserted answer set. That was the specific hazard of this target.

**2. `LocalKummerAll` still quantifies over ℝ and every ℚ_p:**

```lean
def LocalKummerAll (a b d : ℚ) : Prop :=
  InKummer ℝ (a : ℝ) (b : ℝ) (d : ℝ) ∧
    ∀ (p : ℕ) [Fact p.Prime], InKummer ℚ_[p] (a : ℚ_[p]) (b : ℚ_[p]) (d : ℚ_[p])
```

`Basic.lean` `4f085a8c…`, `Selmer.lean` `4dda4069…`, `Family.lean` `a866211d…` — all **byte-identical
to the handoff**, and the first two identical to the audited 62a1 development.

## Statement preservation

`theorem sdyadic_saturation` is byte-identical to the handoff, as are `H41`, `GlobalSet`, `GphiExp`
and `KExp`. No hypothesis added, dropped or weakened; `m ≥ 3` retained; orientation untouched.

## The new mathematics: two from-scratch exhaustion theorems

Not present in the handoff; written by this run.

    SDyadic.phi_exhaustion   (PhiSide.lean:86)
      On H₄₁, every everywhere-locally-soluble squarefree e lies in one of the four square
      classes 1, [D], [q], [Dq].

    SDyadic.dual_exhaustion  (DualSide.lean:18)
      On H₄₁, the only everywhere-locally-soluble square class for (dualA, dualB) is trivial.

These carry the hard direction. The explicit rational witnesses then discharge each class, and
`cov_sqEq` transports along square equivalence.

## The boundary that must travel with this

The quotient `⟨[D],[q]⟩/⟨[D]⟩` is an **explicit descent quotient**. It is **not** a formal `Sel₂`.
No `H¹`, no cocycles, no comparison map is constructed. Nothing here formalizes rank or Ш.

## Relation to a future Freeze 002

Saturation Run B is still running and was **not** waited for. If it passes, build
`S_DYADIC_SATURATION_FORMALIZATION_FREEZE_002` containing both developments. **Do not rewrite this
object** — it is the canonical, independently reproduced first closure, and Run B cannot invalidate
it.
