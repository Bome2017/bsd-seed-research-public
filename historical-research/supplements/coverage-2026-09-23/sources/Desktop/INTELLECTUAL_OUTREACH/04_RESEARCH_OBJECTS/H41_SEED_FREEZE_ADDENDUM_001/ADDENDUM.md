# Addendum to CODEX_H41_SEED_RESEARCH_FREEZE_001

**This object does not reopen that freeze.** The freeze stands at archive
`ac82f3ad90ce42a610a411b24a26629affde209ee90d2c33e7cab7148e355560`, 580 entries, unmodified. Nothing
here revises the return, and no new research run is commissioned by it.

Its purpose is to record corrections to **Claude's commentary** on that freeze, and to distinguish
independent rechecking from mathematical progress.

## 1. Five corrections to Claude's proposed amendments

All five were raised by the operator and all five are confirmed.

**C1 — the genus closed form was wrong.** Claude wrote `g(X₀(2p)) = (p−1)/4`. The correct form is

    g(X₀(2p)) = 2^(n−2) − 1 = (p−3)/4        for p = 2^n − 1

`(p−1)/4` is not an integer for any of these p. Claude's numerical table (7, 31, 2047, 32767,
131071, 536870911) was correct; the closed form attached to it was not checked against the numbers
printed beside it.

**C2 — "computing `a` at N = 16382 decides whether the `a = 1` case is empty" is false.** The value
has asymmetric force: `a = 1` there would establish that the case occurs; `a = 0` would add one more
`a = 0` example and exclude nothing at any larger admissible level. Claude also called the
computation cheap without costing it — obtaining `h` there requires identifying the optimal curve at
that level. It is not a prerequisite and should not become a gate.

**C3 — "answer cyclicity before the problem is well-posed" is wrong.** `u₃` is well-defined with or
without multiplicity one; what would fail without it is one particular route that identifies the
required evaluation through a unique congruent Eisenstein class. Uniqueness is also stronger than
needed: over `F₂²` the distinct functionals `f(x,y) = x` and `g(x,y) = x + y` both take the value 1 on
`(1,0)`, so several compatible functionals can agree on the one element under study. The correct test
is the operator's:

    do the proposed congruence data determine the required evaluation on η₃?

Cyclicity or multiplicity one might establish that. Neither is automatically necessary. Separately,
Wake–Wang-Erickson's exclusion of residue characteristic ≤ 3 does not prove that no applicable result
exists; the earlier description of a definite "literature gap" was also withdrawn by the operator.

**C4 — "ℓ = 3 might be unlucky" is refuted by the identity.** For the same curve, quotient,
orientation and normalization, `w_ℓ/B_ℓ = −ν₀λ/h`, so on the negative branch where `B₃ = 4`

    4·w_ℓ = B_ℓ·w₃

Differing raw parity at another prime is therefore *predicted*, not evidence of an unlucky choice.
Recomputed here at the `N = 62` base: `B₃ = 4`, `B₅ = 8`, hence `w₅ = 2w₃`. Such a test can check an
implementation; it is not independent evidence for the seed.

**C5 — the tooling claim was inconsistent with Claude's own evidence.** Claude wrote that no `gp` was
available on the machine, having earlier used the source-built PARI/GP 2.17.4 executable recorded in
the previous return — verifying its digest `ccdb2f08…` and replaying 24 files with it. The correct
statement is that a working PARI is present and recorded; whether it suffices for integral
modular-symbol localization is a separate question, and dimension alone settles neither feasibility
nor infeasibility.

## 2. Three points Claude presented as new findings were already in the report

Claude offered these as things "worth keeping". They are corroborations, not additions. Each was
independently rechecked here, which has some value as confirmation and none as progress.

**`U₀` is free of rank one.** Already stated: Stage II line 72 — *"The trace kernel is saturated, and
U0 is free of rank one. Its primitive generator must not be replaced by a generator of the plus
eigensublattice."* The caution about the plus eigensublattice is the report's, and it is the sharper
half of the observation.

**`B₃ = 4` on the negative branch.** Already stated: Stage II line 91 — *"For D<0 choose ℓ=3, with
B3=4."* Claude's search for this missed it by grepping Stage I only. The structural reason Claude
recomputed — every admissible negative `m` is odd, so `r ≡ 2`, `A ≡ 0`, `B ≡ 1 mod 3`, and the
reduction is always `y² = x³ + x` — is a correct verification of a stated result.

**The adaptive 3/5/7 rule secures `v₂(B_ℓ) = 2`.** Already stated and justified: Stage II line 91
gives the rule with its point counts, and Stage I line 341 uses *"ν₀ = ±1 and v₂(B_ℓ) = 2 for the
adaptive choice"* to prove the equivalence. The reason for switching from 5 to 7 was given, not
missing.

**The report's treatment is strictly more careful than Claude's corroboration.** Line 91 further
identifies the residue class `m ≡ 1 mod 12`, where the rule would select ℓ = 7 and get `B₇ = 8`,
breaking `v₂(B_ℓ) = 2` — and closes it using the frozen positive-index result that `n = m + 2` is
prime or 9. Verified here: `B₇ = 8` and `v₂ = 3` at `m = 13, 25, 37, 49, 61`, and no admissible
positive index in range lies in that class (`m mod 12 ∈ {3,5,7,9,11}`). **Claude's ten-index sweep
could not have detected this**, because no admissible index in range exercises the case. The report
anticipated a counterexample to its own hypothesis and eliminated it.

## 3. A wording correction to Claude's argument against more examples

Claude wrote that "no finite set of valuations constrains a uniform statement." Too strong. A finite
computation can **refute** the universal assertion, and can **distinguish proposed mechanisms**. What
it cannot do, by agreement alone, is prove the universal assertion. That distinction is the one that
separates a useful experiment from the accumulation of further supporting examples, and it is the
distinction the freeze's own reasoning relies on.

## 4. The equivalence, independently re-derived

The operator reconstructed the identity behind H41-W from the primary sources:

    w_ℓ·Ω_{0,R} = −ν₀·B_ℓ·L(E,1)

whence `λ = −w_ℓ·h/(ν₀·B_ℓ)` and, with `ν₀` a unit, `a = −v₂(h)` and `v₂(B_ℓ) = 2`,

    v₂(λ) = v₂(w_ℓ) − a − 2,     and     λ ≠ 0, v₂(λ) = −2  ⟺  w_ℓ ∈ 2^a ℤ \ 2^(a+1) ℤ.

Re-derived independently here; the algebra goes through with those normalizations. This verifies the
reformulation's logic. It does **not** establish the missing nondivisibility, and the part still
warranting specialist scrutiny is the identification of the actual integral quotient lattice and
period — not a further numerical cusp-order check.

## 5. Unchanged conclusion

    negative branch:   u₃ ∈ 2^a U₀            PROVED
                       u₃ ∉ 2^(a+1) U₀        OPEN
    positive branch:   additional 2-primary period and numerator ambiguity remains

**The strict nondivisibility required by H41-W remains unproved.** The inclusion is established; the
exclusion is not, and the exclusion is the half carrying oddness and nonvanishing. Equivalently
`4λ ∈ ℤ` is proved on the negative branch and the required oddness of that integer is not.

The mathematical status stays unchanged until someone supplies an argument that establishes or refutes
the required nondivisibility. No prerequisite in §1 is a gate, no new bottleneck is identified, and no
further model run is authorised by this addendum.
