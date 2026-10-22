# `S_dyadic` — replicated formalization status

```text
THEOREM_S_DYADIC         = LEAN_CERTIFIED
INDEPENDENTLY_REPLICATED = YES — two Aristotle proof-search runs
FORMALIZATION_LEVEL      = EXPLICIT_2_ISOGENY_DESCENT_REALIZATION
ACTUAL_H1_SELMER_OBJECT  = NO
```

**The theorem-level status did not change.** `S_dyadic` was already formally closed by Run A and
frozen as `S_DYADIC_FORMALIZATION_FREEZE_001`. Run B proves the **same exact statement**, with the
same hypotheses and the same explicit-descent boundary. **Run B did not enlarge `S_dyadic`.**

What it adds is replication evidence and a materially different, reusable local proof architecture.

## Both runs, independently rebuilt and audited here

| | **Run A** | **Run B** |
|---|---|---|
| `lake build` | exit 0, 8047 jobs | exit 0, 8046 jobs |
| modules / lines | 21 / 4 378 | 20 / 5 150 |
| theorems / lemmas | 192 / 13 | 200 / 13 |
| `sorry` / `admit` / `axiom` | 0 / 0 / 0 | 0 / 0 / 0 |
| prohibited constructs | none | none |
| `#print axioms` on the target | `[propext, Classical.choice, Quot.sound]` | same |

Neither shows `sorryAx`.

## The statement is identical

`theorem sdyadic_selmer` (23 lines, the full five-way conjunction) is **byte-identical** in the V1
handoff, Run A and Run B, as are `lam`, `repr`, `phiAnswer` and `dualAnswer`.

## The semantic boundary held in both

`Basic.lean` `4f085a8c…`, `Selmer.lean` `4dda4069…`, `Family.lean` `a866211d…` — **byte-identical
across V1, Run A and Run B**, and the first two identical to the audited 62a1 development. So in
both runs

```lean
def LocalKummerAll (a b d : ℚ) : Prop :=
  InKummer ℝ (a : ℝ) (b : ℝ) (d : ℝ) ∧
    ∀ (p : ℕ) [Fact p.Prime], InKummer ℚ_[p] (a : ℚ_[p]) (b : ℚ_[p]) (d : ℚ_[p])
```

**The universal quantifier over all primes survived in both.** Neither redefined Selmer as a
bad-prime checklist.

## The independence qualification — unchanged and still required

Two independent **Aristotle proof-search runs**: same handoff, same Lean kernel, same mathlib
revision, **separate proof search, no cross-feed**. This is **not** independent proof-assistant
verification. It is two materially different kernel-checked Lean developments — stronger than two
models agreeing, weaker than two independent verifiers.

## Relation to Freeze 001

`S_DYADIC_FORMALIZATION_FREEZE_001` is **not replaced**. It remains the canonical historical record
of the first closure. This object is its replicated successor and should be cited by future packets.

The two completed Pro composition reviews were run against Freeze 001 **before** Run B existed. That
experiment is **not** retroactively rewritten.
