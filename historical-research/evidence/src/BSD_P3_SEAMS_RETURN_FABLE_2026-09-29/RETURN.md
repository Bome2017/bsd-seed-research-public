# RETURN — Lane P3 residual (Euler-removal interface), Fable 5.1, 2026-09-29

## STATUS
- **Residual (R1_R2_THEOREM.md §3.6 / SU Prop 12.3.6 at inert q = 2243): REDUCED.**
  - Prop 12.3.6 has two consumers in SU's proof. One (U2) is repaired for the seed by a nonvanishing argument that
    needs no μ = 0 (U2_REPAIR.md).
  - The other (U1) is now the one named missing statement: SU Prop 13.4.1(ii) for the seed's data
    (MISSING_STATEMENT.md). It is neither proved nor refuted.
- R3 (Greenberg 1989 Prop 3.2): NOT_ATTEMPTED. R5 (Mazur–Tate σ at multiplicative 3): NOT_ATTEMPTED.
- Skinner's printed Theorem A is not refuted. S.3's grade and wording are untouched by this lane.

## Kill tests (run first; kp1.gp, kp2.gp; PARI 2.17)
- **K-P1: PASS (the review's premise holds).**
  - Computed: v₃(1 − 2243⁻²) = 1, a₂₂₄₃ = 1 (I₁), 2243 ≡ 2 (mod 3).
  - The 3 sits in the factor (1 + 2243⁻¹), i.e. in the f⊗χ_K half of the base change. The factor (1 − 2243⁻¹) is a
    unit (EULER_RECONCILIATION l.47).
  - 2243 is inert in the step's K by hypothesis: SU requires M⁻ to be inert, and M⁻ = 2243 is forced (next item).
- **K-P2: route (b) KILLED within SU's hypotheses.**
  - The hypotheses that fix the auxiliary data are the Prop 12.3.6 and §7.4 bullets: (M, D_K) = 1; M⁺ has only
    split primes and M⁻ only inert ones; M⁻ is squarefree with an odd number of primes; ρ̄ is ramified at M⁻;
    p is split; Σ ⊇ {primes of pMD_K}; ξ = ξ̄^c.
  - For M = N/3 = 2³·2243·4547²·5843, the primes 2 and 4547 appear squared, so they must be split. Hence
    M⁻ ∈ {2243, 5843}.
  - Both are ≡ −1 (mod 3), and v₃(1 − q⁻²) = 1 for each.
  - ξ cannot change the factor: ξ|A_Q^× ∈ {1, χ_K}, and χ_K is excluded, so ξ((q)) = 1.

## Target 1 — the exact use
- **The chain.** Skinner 2016 §3.1 (published pp.191–192) → Thm 2.5.2 for the higher-weight good-ordinary
  specializations f_m of tame level N/3 → SU + Kato → SU Thm 3.6.1 for the Hida family 𝐟 through f.
- **The proof of Thm 3.6.1** (SU §7.4, author copy p.108, l.6100–6135) takes D = (A, I, 𝐟, 1, 1, Σ) with M⁻ = 2243.
  It uses Prop 12.3.6 twice:
  - **(U1)** through Prop 13.4.1(ii) (p.217–218, l.12803–12827): if P | L^Σ_{𝐟,K} then E_D ≢ 0 mod P.
  - **(U2)** directly (l.6122): if ord_P(L^Σ_{𝐟,K}) > 0 then ord_P(L^Σ_1) = 0. Here L^Σ_1 is the Σ-imprimitive
    Kubota–Leopoldt function evaluated at x = (1+W)⁻¹γ₊².
  - Both feed the hypotheses of Thm 7.3.5 (p.107, l.6036–6048).
- **What the printed proof of 12.3.6 needs** (p.202): write L^Σ_{𝐟,K,1} = Σ aᵢ(γ₋−1)ⁱ with aᵢ ∈ I[[Γ_K⁺]]. For the
  weight-2 point φ₀ (f itself, multiplicative at 3; Skinner 2016 p.188 swaps Vatsal for CH Thm C here) with
  φ₀(γ₊) = 1, it needs **some φ₀(aᵢ) ∈ A^×**. That means **μ(L^{Σ,−}_{f,K,1}) = 0** in SU's normalization:
  L^Σ_K(f, χ̄ξ_φ, 1)/((−2πi)²Ω_f⁺Ω_f⁻), canonical periods (SU §3.3.3), with Σ-Euler factors removed using residue
  norms q_v (SU (3.4.5.b), p.39).
- **What is true instead:** μ = 1. This uses CH μ = 0, the review-passed (3.7)–(3.9), the factor 1 − 2243⁻², and
  ramified factors that are units for a good choice of K. For D_K = −311, 3 ∤ 311 + 1 − a₃₁₁. For some other K
  (e.g. −887) the ramified factor would add further μ, so the choice of K matters.

## Target 2(a) — SU's own comparison: not reconciled; the slip is located
- **The μ-equality sentence is a tautology.** On p.202 SU say the μ of both sides of (12.3.5.b) agree. That is
  automatic, since the two sides are equal.
- **The false step is the next sentence:** "by Theorem 1.1 of [Va03] these µ-invariants are zero". Vatsal controls
  only the primitive factor, not the product of removed Euler factors.
- **(12.3.5.b) as printed disagrees with SU's own definition.** It uses ℓ⁻¹ (with a trace inside a determinant),
  whereas SU's (3.4.5.b) uses q_v⁻¹, with q_v the order of the residue field, so q_v = ℓ² at an inert prime.
  - Read literally with ℓ⁻¹, the inert factor would be 1 − 2243⁻¹, which is a 3-unit. So the misprint is consistent
    with the μ claim. That this was SU's intent is UNCHECKED.
  - With SU's own definition the factor is 1 − 2243⁻², and v₃ = 1.
- **The factor cancels between the analytic and algebraic sides only at the level of main-conjecture identities**
  (SU (3.4.5.b) with Cor 3.2.16; Skinner (E1)). That cancellation cannot act inside Prop 12.3.6, which concerns
  L^Σ alone.

## Target 2(b) — avoiding the step: killed (K-P2 above).

## Target 2(c) — repair where the step is consumed (U2_REPAIR.md; THEOREM, written proof)
- L^Σ_1 = unit·(x−1)^{n−1}, provided every ℓ ∈ Σ∖{3} has ℓ² ≢ 1 (mod 9). The seed's primes all do: they are
  ≡ 2 (mod 9). The auxiliary primes are free choices.
- So the only height-one prime containing L^Σ_1 is (x−1). That prime lies in ker φ₀.
- Hence (U2) needs only φ₀(L^Σ) ≠ 0. This follows from CH Thm C nonvanishing. No μ = 0 is needed; μ = 1 is harmless.
- (U1) cannot be repaired this way, because its extended primes come from A_{D,g} (SU 13.3.4), not from L^Σ_1.

## Target 3 — the missing statement (exact form: MISSING_STATEMENT.md)
- **(MS-13.4.1(ii))** No height-one prime of Λ_D contains both L^Σ_{𝐟,K,1} and C_D. Equivalently: for every height-one
  prime Q ⊂ I[[Γ_K⁺]] with L^Σ_{𝐟,K,1} ∈ Q·I[[Γ_K]], we have C_D ⊄ Q·Λ_D.
- Together with Lemma U2, this restores SU Thm 3.6.1 for 𝐟. The rest of Skinner's chain is unchanged.
- New THEOREM: for the seed, the printed conclusion of Prop 12.3.6 implies that the inert Euler factor
  E ∈ I[[Γ_K⁺]] (a nonzero non-unit) does not divide L^Σ.
  - So if the 2243-primitive quotient L^Σ/E is integral (expected; CONJECTURE), then the printed statement of
    Prop 12.3.6 is false for this seed.
  - In that case the primes Q over (E) do contain L^Σ, and (MS-13.4.1(ii)) is needed exactly at those Q.
- No printed interpolation formula reaches the zero set of E. That set is the s = k/2 − 1 ("k = 0") locus and
  contains no point of SU's X^a.

## Grades (kept separate)
- **THEOREM (written here):**
  - K-P1 and K-P2.
  - Lemma U2.
  - E ∈ I[[Γ_K⁺]] and E is a non-unit.
  - [printed 12.3.6] ⇒ E ∤ L^Σ.
  - The location of the (12.3.5.b) inconsistency with (3.4.5.b).
- **CONJECTURE:** L^Σ/E is integral. Hence the printed Prop 12.3.6 statement fails for the seed.
- **UNCHECKED:**
  - (MS-13.4.1(ii)).
  - SU's intended reading of (12.3.5.b).
  - Σ1 ⊆ {ℓ | 2D_K} for the auxiliary θ₁.
  - Any SU erratum. A targeted web search on 2026-09-29 found none; this was not an exhaustive search.
  - The journal body of SU, since only the author copy was read.

## Attempts that did not close (U1)
- The μ-argument at φ₀: it excludes only those Q with φ₀(Q)A ⊉ 3A.
- Interpolation on V(E): there are no X^a points on it.
- The algebraic Euler-factor bypass: SU Cor 3.2.16 has the wrong direction, and it assumes T is unramified at v.
- Varying g: this would need a mod-3 unit Rankin–Selberg value φ₀(A_{D,g}), which is not in print.
- Other main-conjecture routes: Yan–Zhu arXiv:2412.20078 is good-ordinary only. It was not audited.

## Unchanged
- The p = 3 computation was not re-run.
- R1 and R2 (3.1)–(3.9) were not reopened.
- No theorem was relabelled.
- Nothing outside this folder was written. Sources were read in place.

FIN, ORDER9 and Q36 are unchanged.
