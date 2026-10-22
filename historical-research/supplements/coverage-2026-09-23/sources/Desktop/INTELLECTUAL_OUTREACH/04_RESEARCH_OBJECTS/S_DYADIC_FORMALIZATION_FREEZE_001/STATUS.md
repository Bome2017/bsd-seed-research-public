# `S_dyadic` — formalization status

```text
THEOREM_S_DYADIC              = LEAN_CERTIFIED
FORMALIZATION_LEVEL           = EXPLICIT_2_ISOGENY_DESCENT_REALIZATION
ACTUAL_H1_SELMER_OBJECT       = NO
ALL_REAL_AND_PADIC_PLACES_RETAINED = YES

TARGET_STATEMENT_PRESERVED    = YES   (byte-identical to the V1 handoff)
LAKE_BUILD                    = PASS  (independent rebuild here: exit 0, 8047 jobs)
SORRY_COUNT                   = 0
ADMIT_COUNT                   = 0
CUSTOM_AXIOMS                 = 0
PROHIBITED_CONSTRUCTS         = NONE
TARGET_AXIOMS                 = propext, Classical.choice, Quot.sound
```

**No `sorryAx`.** That is the line that matters, and it was reproduced here, not taken on report.

## The certification chain

1. Extracted from the frozen 62a1 and 66b1 cases.
2. Independently reconstructed **before seeing the proposed proof** by two separate hostile
   referees, both returning `STAGE_I_RESULT = PROVED`, `S_DYADIC_OVERALL = PASS`,
   `COUNTEREXAMPLE_FOUND = NO`.
3. Proved in Lean 4 by Aristotle against the genuine local-solubility definition.
4. Independently extracted, rebuilt and audited in this freeze.

## The semantic boundary — the thing that makes this meaningful

The theorem is stated about `Run013.SelmerSet`, which is defined **only** as

```lean
def LocalKummerAll (a b d : ℚ) : Prop :=
  InKummer ℝ (a : ℝ) (b : ℝ) (d : ℝ) ∧
    ∀ (p : ℕ) [Fact p.Prime], InKummer ℚ_[p] (a : ℚ_[p]) (b : ℚ_[p]) (d : ℚ_[p])

def SelmerSet (a b : ℚ) : Set Qsq :=
  {c | ∃ d : ℚˣ, qcl d = c ∧ LocalKummerAll a b (d : ℚ)}
```

**The universal quantifier over all primes survived.** Verified here: `Basic.lean` and `Selmer.lean`
in the completed tree are **byte-identical** to the versions shipped in the V1 handoff, which are in
turn byte-identical to the audited 62a1 development:

```text
Basic.lean   4f085a8c7f3cb0621af4341a87a8aed26bde2cee5f0d9148a58a4c3332115947
Selmer.lean  4dda4069454b2dd02a7c1a821d0a7e7cf7ecae775147f6e38f9e877f57fa3a0b
```

`Family.lean` — the parameters, both coefficient pairs and `Params` — is likewise byte-identical, as
are `lam`, `repr`, `phiAnswer` and `dualAnswer`. **Aristotle did not redefine Selmer as a bad-prime
checklist, and did not adjust the hypotheses or the claimed answer.**

## What may and may not be said

**May:** *a Lean-certified Selmer computation, at the explicit 2-isogeny descent realization level.*

**May not:** *a formalized cohomological Selmer group.* No `H¹`, no cocycles, no restriction maps.
See `01_completed_proof_A/tree/FORMALIZATION_BOUNDARY.md`.

## Environment

```text
Lean     leanprover/lean4:v4.28.0
mathlib  8f9d9cff6bd728b17a24e163c9402775d9e6a365
```

## Run B

Not present. This freeze covers **Run A only**, which has independently earned it. If Run B also
passes, this object can be upgraded or succeeded by a two-implementation freeze, as happened for F.
