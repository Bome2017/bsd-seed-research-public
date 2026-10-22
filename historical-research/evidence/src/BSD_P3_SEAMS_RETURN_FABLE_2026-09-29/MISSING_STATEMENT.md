# The residual after this lane: one named missing statement

Notation and data as in U2_REPAIR.md (seed, p = 3, 𝐟 through f, K with M⁻ = 2243, D = (A, I, 𝐟, 1, 1, Σ) from SU
Prop 13.4.1, C_D = {c_D(β_i, x)} the non-singular Fourier–Jacobi coefficients of E_D, SU p.217, l.12803–12825).

## (MS-13.4.1(ii)) — the exact missing statement
**No height-one prime of Λ_D contains both L^Σ_{𝐟,K,1} and C_D.**
Equivalent form, using SU 13.4.1(i) (whose printed proof does not use Prop 12.3.6): for every height-one prime
Q ⊂ I[[Γ_K⁺]] with L^Σ_{𝐟,K,1} ∈ Q·I[[Γ_K]], one has C_D ⊄ Q·Λ_D.
This is SU Prop 13.4.1(ii) specialised to the seed's data. Its printed proof reads, in full: "Part (ii) follows from
part (i) and Proposition 12.3.6" (p.218, l.12827). Prop 12.3.6's printed proof fails here (review §1; K-P1).
The statement itself is NOT refuted. Grade: UNCHECKED (neither proved nor disproved here).

## Why this is the only open consumer
SU cites Prop 12.3.6 at l.2308 (a remark on hypotheses), l.6122 (§7.4: consumer U2), l.11788 (the statement) and
l.12827 (13.4.1(ii): consumer U1). U2 is repaired for the seed in U2_REPAIR.md (THEOREM, nonvanishing only).
With U2 and (MS-13.4.1(ii)), SU §7.4 applies Thm 7.3.5 (p.107, l.6036–6048) at every height-one P dividing L^Σ, so
Ch^Σ_K ⊆ (L^Σ_{𝐟,K}) and SU Thm 3.6.1 holds for 𝐟. Downstream (Skinner 2016 Thm 2.5.2 for f_m, then the (E3) chain in
EULER_RECONCILIATION §3) is unchanged.

## THEOREM (this lane): the printed Prop 12.3.6 forces a pole on the ℓ0-primitive function
Let E := det(1 − q_w^{−1} ε_K ρ_𝐟(frob_w) | V^{I_w}), w = 2243·O_K (SU (3.4.5.b), p.39). Then:
(a) E ∈ I[[Γ_K⁺]]: the idele (2243 at w) is ≡ (2243^{−1} at every other place) mod K^×; its image in Γ_K comes from
    (2243^{−1}, 2243^{−1}) ∈ O_𝔭^× × O_𝔭̄^×, which is c-invariant, so frob_w ∈ Γ_K⁺ (p odd, Γ_K = Γ_K⁺ × Γ_K⁻).
(b) E is a nonzero non-unit: mod 𝔪 it is 1 − 2243^{−2}·a_2243(f)² = 1 − 2243^{−2} ≡ 0 (mod 3) (ε_K ≡ 1 mod 𝔪); at
    every X^a point E(φ) = 1 − 2243^{−k}ζ ≠ 0.
(c) If the printed Prop 12.3.6 holds for the seed data, then E ∤ L^Σ_{𝐟,K,1} in I[[Γ_K]].
    Proof: if E | L^Σ, take a minimal prime Q of I[[Γ_K⁺]] over (E); it has height one (Krull), and L^Σ ∈ Q·I[[Γ_K]].
Reading (CONJECTURE, not proved): the ℓ0-primitive quotient L^Σ/E is expected to be integral (no pole along E = 0).
If so, the printed statement of Prop 12.3.6 is false for this seed, (E)·I_K divides L^Σ, and (MS-13.4.1(ii)) needs
C_D ⊄ Q·Λ_D for the height-one primes Q over (E).

## Why interpolation cannot settle it
On X^a, φ(γ₊) = ζ₊(1+p)^{k−2} (p.38). The zero set of E is the "k = 0" locus x = (1+p)^{−2}·(root of unity),
x = (1+W)^{−1}γ₊² (the critical point s = k/2 − 1). It contains no X^a point, and on it the auxiliary CM family g has
non-classical weight 2 − k/2. So neither L^Σ nor A_{D,g} is pinned down there by any printed interpolation formula.

## Sufficient inputs (none proved here)
(S1) One admissible g (SU 13.3.4, p.213) with A_{D,g} ∉ Q for each Q above. For example, φ₀(A_{D,g}) ∈ A^× makes A_{D,g}
     a unit of the local ring I[[Γ_K⁺]], and then (MS-13.4.1(ii)) holds for every Q.
(S2) Integrality E | L^Σ (then SU's μ-argument runs on L^Σ/E, using CH μ = 0 and the review-passed (3.7)–(3.9); the
     only candidate Q are the primes over (E)), plus C_D ⊄ Q·Λ_D for those Q.
(S3) A bypass at primes over (E): ord(L^Σ) ≤ ord(E) there, plus an algebraic lower bound ord(Ch^Σ_K) ≥ ord(E) at the
     Steinberg inert place. SU Cor 3.2.16 (p.26) gives only the opposite inequality, and only where T is unramified.
