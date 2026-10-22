# 01 — Types and objects (Lane 1)

All curves are smooth projective over Q unless a base field is named; M := N p^r with p ∤ N, p odd.
"Albanese" = pushforward on points/divisors; "Picard" = pullback of line bundles. For an automorphism g
of a curve, g_* = (g^{-1})^* on Pic^0.

## 1. The two models of the same complex curve Γ_1(M)\H*

| Symbol | Moduli problem | Source | Q-structure |
|---|---|---|---|
| X^pt_r = X_1(Np^r) | (A, P), P ∈ A of exact order Np^r | BCPV §4.2; DR22 §1.1; KLZ2 §2.3 (Y_1(N) = Y(1,N)); BSV §2.3.1 | cusp ∞ NOT rational (KLZ2 §2.3) |
| X^μ_r = Hida's X_r | (E, φ: μ_{Np^r} ↪ E) | Hida LMW §3, §5; Hida Control §3, §6; Mazur–Wiles 1986 §2; Ohta (per KLZ2 §7.2) | cusp ∞ rational |

J^pt_r := Pic^0(X^pt_r), J^μ_r := Pic^0(X^μ_r), abelian varieties over Q.

## 2. Maps between and on the models (all defined on moduli; complex-analytically all are "τ ↦ τ" or Atkin–Lehner)

| Symbol | Type | Definition | Field of definition |
|---|---|---|---|
| ι_ζ | X^pt_r → X^μ_r | (A,P) ↦ (A, φ_P), φ_P(ζ^a) = aP, ζ a primitive M-th root | Q(μ_M); ι^σ = ι_{σζ} |
| α_r | X^pt_r → X^μ_r (isomorphism) | (A,P) ↦ (A/⟨P⟩, φ), φ = inverse of A[M]/⟨P⟩ → μ_M, Q ↦ ⟨P,Q⟩_{A[M]} | **Q** (no root of unity is used) |
| W_ζ (= "W_{Np^r}") | automorphism of X^pt_r ⊗ Q(μ_M) | KLZ2 §2.5 with Q = M: (A,P) ↦ (A/⟨P⟩, P'), ⟨P,P'⟩ = ζ | Q(μ_M) |
| w_ζ (= Hida "w_r") | automorphism of X^μ_r ⊗ Q(μ_M) | Hida LMW §5: (E,φ) ↦ (E/Im φ, ϕ), ϕ(ζ^m) = i(m), i = (φ^*)^{-1}: Z/M ≅ E[M]/Im φ | Q(μ_M) |
| ⟨d⟩ | automorphism of X^pt_r | (A,P) ↦ (A, dP) (BSV §2.3.1; DR22 §1.2) | Q |
| g_d | automorphism of X^μ_r | (E,φ) ↦ (E, φ∘d) (Hida §3) | Q |
| ϖ_1 | X^pt_{r+1} → X^pt_r | (A,P) ↦ (A, pP) (BCPV §4.2 literal; DR22 §1.2) | Q |
| π = π_{r+1,r} | X^μ_{r+1} → X^μ_r | (E,φ) ↦ (E, φ restricted to μ_{Np^r}) (Hida; MW86 §2) | Q |
| π^{r+1}_r | J^μ_{r+1} → J^μ_r | w_r ∘ π_* ∘ w_{r+1} (Hida LMW §5, Control §6) | Q (Hida) |

Hida's root convention: ζ^H_{Np^r} := ζ_N ζ_{p^r}, ζ_N fixed once, (ζ_{p^r}) p-power coherent.
BCPV/KLZ2 root convention for W: NOT PRINTED in BCPV; KLZ2 §7.1 fixes ζ_m ↔ e^{2πi/m} (coherent in m).
Define c_r ∈ (Z/Np^r)^× by ζ^H_{Np^r} = (ζ^B_{Np^r})^{c_r}, and u_r ∈ (Z/Np^r)^× by
(ζ^H_{Np^{r+1}})^p = (ζ^H_{Np^r})^{u_r}. For Hida's convention u_r ≡ p (mod N), u_r ≡ 1 (mod p^r).

## 3. Hecke-side objects

| BCPV (point model, KLZ2 conventions) | Hida (μ model) |
|---|---|
| T'_ℓ, U'_q (pushforward-type, compatible with the ϖ_{1,*}/pr_{1,*} tower); T_ℓ, U_q their transposes | T(n), U(q) acting on J by Picard functoriality; T^*(n), U^*(p) Rosati duals |
| e'_ord = lim (U'_p)^{n!}; e_ord = lim U_p^{n!} | e = lim U(p)^{n!} (ordinary); e^* = lim U^*(p)^{n!} (co-ordinary) |
| H^1_ord(Y_1(Np^∞)) = e'_ord lim_{ϖ_{1,*}} H^1_et(·, Z_p(1)) | Ĵ_∞(k)^ord = lim_{π^s_r} Ĵ_s(k)^ord (w-twisted); J̃_∞(k)^{co-ord} = lim_{π_*} Ĵ_s(k)^{co-ord} (untwisted) |
| A_r := W_{N_g p^r}^{-1}(U'_p)^r : e'_ord H^1 → e_ord H^1 (BCPV (1.8)) | w_r : ordinary ↔ co-ordinary (Hida Control §5 isomorphism i) |
| diamonds ⟨d⟩; dagger Z_p[G_r]^†, G_Q via ⟨χ⟩_r^{-1/2} (BCPV Def. 4.x) | diamonds ⟨z⟩_H on J_r (Galois formula forces Picard convention, see 03 §1.5) |

## 4. The H9R16-C objects on which the dictionary is evaluated

* O1 (f-side receptacle): e'_ord J^pt_r (and its p-completion), transition ϖ_{1,*}, U'_p-normalization
  (BCPV Cor. to Lemma `DR_lemma_2_5_dual`, Def. `definition_big_Heegner_main`).
* O2 (g^c-side operator): A_r = W_{N_g p^r}^{-1}(U'_p)^r on e'_ord J^pt(level N_g p^r) (BCPV (1.6)/(1.8)).
* O3 (fixed-base receptacle): A_r^† := I_r^† ⊗ J_r over K_0 = Q(μ_p) (H9R8/H9R9), with I_r^† the Z[G_r]
  lattice on which G_Q acts by ⟨χ⟩_r^{-1/2}; Tate module Z_p[G_r]^† ⊗ T_p J_r.
* All statements are for weight-two specializations (coefficient sheaf Z_p(1), i.e. k = 0), which is
  where the H9R16-C points live. For k > 0 every ⟨−1⟩ below acts by (−1)^k and must be kept.
