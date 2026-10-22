# PROOF — corrected 2026-10-07 (see CORRECTIONS_2026-10-07.md)

**The first version's Proposition 1, statement 4 (the "Fitting-to-Heegner" equivalence), is
withdrawn.** What survives is listed below with its true grade. None of it is new relative to
the record, and none of it bounds X_p.

## Domain D (unchanged definition, corrected dependency)

D is the set of primes p ≥ 5 such that:
- p ∤ 6·N_E·23·(retained finite exceptional set);
- ρ̄_{E,p} is surjective (retained input);
- Zhang's Hypothesis ♥ holds for (E, K = Q(√−23), p) (retained, not re-derived);
- s⁻_p := dim_Fp Sel_p(E^K/Q) = 1.

The last condition holds for every odd p ∤ #Sha(E^{−23}/Q)·#E^{−23}(Q)_tors **if**
ord_{s=1} L(E^{−23},s) = 1, by Gross–Zagier–Kolyvagin. **Correction:** the first version said
this analytic rank had not been computed in the record. That was wrong. The record contains a
2026-09-21 computer-assisted Arb certificate, 39.512236 ≤ L′(E^{−23},1) ≤ 40.182321, and a
2026-10-06 floating-point value 39.84727806412. The trace and grade are in TWIST_D23_TRACE.md:
the metadata and arithmetic around the certificate recheck, but its core sum cannot be replayed
from the supplied archive. ASSUMPTIONS.json now carries this dependency at that grade.

## Retained statement R1 (record restatement, not new)

For p ∈ D, the following are equivalent:
1. dim_Fp X_p ≤ 1;
2. X_p = 0;
3. ν_p = 1, i.e. some one-prime Kolyvagin class κ_ℓ (Zhang's normalization) is nonzero in H¹(K, E[p]).

Proof. Write s⁺ = 2 + dim X_p and s⁻ = 1, and apply Lemma 8.4. If ν were even, then s⁻ = ν + 1
would force ν = 0 and s⁺ ≤ 0, which is impossible. So ν is odd and s⁺ = ν + 1, giving
dim X_p = ν − 1, and dim X_p ≤ 1 ⇔ ν = 1. ∎

This is exactly the record's kernel-checked bookkeeping `nu_le_two_iff_sha_of_twist` (hypothesis
`ZhangLemma84`; HEEGNER_NU.md §1). The W3 return (HEEGNER_NU_NOTE.md §3) already combined it with
its numerical twist value. It is listed here only because the A2 row uses it.

## Retained statement R2 (standard, cited)

Let C be a perfect Λ-complex of amplitude [1,2] (ordinary p, E[p] irreducible) and T ∈ Λ a
non-zero-divisor. Then

    0 → H¹(C)/T → H¹(C ⊗^L Λ/T) → H²(C)[T] → 0,     H²(C ⊗^L Λ/T) = H²(C)/T.

This is homological algebra. Identifying H^i(C ⊗^L Λ/T) with H^i_f(K,T) for Greenberg
conditions is Nekovář's control theorem, cited at statement level. H² torsion is kept.

## Withdrawn: statement 4 and part (b)

The withdrawn claim was: Θ_1(0) ⊗ F_p is the unit ideal ⇔ some κ_ℓ ≢ 0 mod p. The argument
identified three different Euler-system objects without proving that they agree:
- the DLV ideals, whose construction was never read here;
- Howard's Λ-adic Heegner Kolyvagin system;
- Zhang's classical κ_n.

The missing comparisons C1–C4 (which system is used, the p-dependent specialization factor,
coordinate versus class in a rank-3 module, normalization) are set out in
CORRECTIONS_2026-10-07.md. Until they are supplied, this return makes **no** claim about how the
augmentation image of a DLV ideal relates to X_p or to ν_p.

## Consequence for the assignment

TASK.md asked for a "particular generator/minor" in the higher-Fitting source. This return has
**not** identified one. The first version's identification with κ_ℓ mod p depended on the
withdrawn step. Candidate A1 is therefore left as: control map written (R2, H² kept); generator
comparison open; not developed. It is neither reduced to A2 nor shown to give independent control.
