# Lemma U2 — consumer (U2) of SU Prop 12.3.6, repaired for the seed without μ = 0

Source: SU = author copy `~/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/audits/p3_r1_r2_2026-09-19/sources/SkinnerUrban_MC.{pdf,txt}`
(page = printed author-copy page; l. = line in the .txt). Grade: THEOREM (written proof, this file; not refereed).

**Setting (SU §7.4, p.108, l.6100–6135, for the seed).** p = 3; 𝐟 ∈ M^ord(M,1;I), M = N/3 = 2³·2243·4547²·5843, the
Hida family through f, with φ₀(𝐟) = f (weight 2, trivial character); I an integrally closed domain (a §7.4 bullet);
K with 3, 2, 4547, 5843 split, 2243 inert, (D_K, 3N) = 1 (example D_K = −311, kp2.gp); D = (A, I, 𝐟, 1, 1, Σ) from
Prop 13.4.1; Λ_D = I[[Γ_K⁻ × Γ_K]] = I_K[[Γ_K⁻]] (p.97); L^Σ_1 := L^Σ_{χ̄_𝐟 ξ̄'} with χ_𝐟 = 1, ξ' = ξ|A_Q^× = 1.

**Condition (h).** Every prime ℓ ∈ Σ∖{3} satisfies ℓ² ≢ 1 (mod 9).
Seed: 2, 2243, 4547, 5843 are all ≡ 2 (mod 9) (kp2.gp). Σ = Σ0 ∪ Σ1 ∪ {ℓ0'} (or ∪{ℓ | ℓ0'D_L}) (p.218–219,
l.12860–12884); ℓ0' and D_L are free choices and can satisfy (h). Σ1 (ramification of θ1) ⊆ {ℓ | 2D_K} is UNCHECKED.

**Lemma U2.** Assume (h). If P ⊂ Λ_D is a height-one prime with ord_P(L^Σ_{𝐟,K,1}) > 0, then ord_P(L^Σ_1) = 0.
This is the exact assertion SU draw from Prop 12.3.6 at l.6122 ("by Proposition 12.3.6 ord_P(L^Σ_1) = 0 if …").

**Proof.**
1. L^Σ_1 is the image of G^Σ_1 ∈ A[[Γ_Q]] under γ ↦ x := (1+W)^{−1}γ₊² (p.98, l.5516–5519; exponent 2 checked on the
   rendered page). SU p.37 (l.2068–2070): G_1 ∈ Λ_Q^× and (γ−1)G^S_1 ∼ ∏_{ℓ∈S,ℓ≠p}(1 − Ψ_{Q,ℓ}(ℓ)).
2. Ψ_Q = ε_Q ∘ rec_Q (p.31, l.1622), so Ψ_{Q,ℓ}(ℓ) = γ^{±s(ℓ)} with ⟨ℓ⟩ = (1+p)^{s(ℓ)} (γ ↔ 1+p, l.1631).
   For p = 3: v_3(s(ℓ)) = v_3(⟨ℓ⟩ − 1) − 1 = v_3(ℓ² − 1) − 1, which is 0 under (h). Hence 1 − γ^{±s(ℓ)} = (γ − 1)·unit,
   and L^Σ_1 = u·(x − 1)^{n−1} with u a unit of I[[Γ_K⁺]] and n = #(Σ∖{3}) ≥ 4.
3. Q_1 := (x − 1)·I[[Γ_K⁺]] is prime: with γ₊ = 1+T₊, (1+T₊)² − (1+W) = (T₊ − t₀)(2 + T₊ + t₀), t₀ := (1+W)^{1/2} − 1 ∈ 𝔪_I
   (binomial series; 2 ∈ Z_3^×), the second factor is a unit, and I[[T₊]]/(T₊ − t₀) ≅ I, a domain.
   Λ_D is a power-series ring over I[[Γ_K⁺]], so Q_1Λ_D is a height-one prime and Q_1Λ_D ∩ I_K = Q_1·I_K.
4. If P is height one and L^Σ_1 ∈ P, then x − 1 ∈ P, so P ⊇ Q_1Λ_D, hence P = Q_1Λ_D. So the only height-one prime
   at which ord_P(L^Σ_1) > 0 is Q_1Λ_D, and it suffices to show L^Σ_{𝐟,K,1} ∉ Q_1·I_K.
5. Let φ₀ be as in SU's proof of Prop 12.3.6 (p.202): the weight-2 point with f = f_{φ₀}, extended by φ₀(γ₊) = 1. The
   character of f is trivial, so φ₀(1+W) = 1 and φ₀(x) = 1: Q_1 ⊆ ker φ₀. If L^Σ ∈ Q_1·I_K then every coefficient
   a_i (L^Σ = Σ a_i(γ₋−1)^i, a_i ∈ I[[Γ_K⁺]]) lies in Q_1, so φ₀(a_i) = 0 for all i, i.e. L^{Σ,−}_{f,K,1} = 0
   (SU p.202: "for some u ∈ A^×, uL^{Σ,−}_{f,K,ξ} = φ(a_0) + φ(a_1)(γ⁻−1) + …").
6. L^{Σ,−}_{f,K,1} ≠ 0. By SU §12.3.5 (p.201, first display) its value at an anticyclotomic φ with p | n_φ equals a
   nonzero factor times L^Σ_K(f, ξ_φ, 1). Each removed factor is nonzero: inert 2243: 1 − 2243^{−2} ≠ 0; split v over
   ℓ | M multiplicative: 1 − a_ℓ χ(v) ℓ^{−1} ≠ 0; v over ℓ ∤ M: the eigenvalues of ρ_f(frob_v) have absolute value
   q_v^{1/2} ≠ q_v, so det(1 − q_v^{−1}…) ≠ 0; additive ℓ (2, 4547): V^{I_v} = 0, factor 1. By Chida–Hsieh Thm C (applicability PASS in
   P3_R1_R2_REVIEW §3.4), Θ_∞ ≠ 0, so its square, which interpolates L(f/K, χ, 1) up to nonzero factors (CH Thm A,
   (4.3)), vanishes at only finitely many χ (Weierstrass preparation). So L(f/K, χ, 1) ≠ 0 for almost all χ of
   3-power conductor. This contradicts step 5. ∎

**What this does not use:** μ = 0, the period unit (3.9), the Gauss-sum/conductor unit checks, or the form of the
Euler factor at 2243. Only nonvanishing is used. μ(L^{Σ,−}) = 1 at 2243 is harmless here.
**What it does not repair:** the other consumer, SU Prop 13.4.1(ii) (see MISSING_STATEMENT.md).
