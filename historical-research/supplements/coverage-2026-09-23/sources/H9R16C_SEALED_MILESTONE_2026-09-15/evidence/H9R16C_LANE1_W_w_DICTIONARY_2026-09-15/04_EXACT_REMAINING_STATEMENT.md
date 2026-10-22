# 04 — Exact remaining statements after Lane 1

Lane 1's own target (the literal BCPV-W / Hida-w relation and the rule for inserting the discrepancy)
is closed by 03 §§1–3. What remains belongs to other gates. Each item is stated with the types fixed
in 01 and the dictionary proved in 03.

## R1 — C2, now with fully typed verticals (the first genuinely unproved statement)

For r ≥ 1 let J_r := J^pt_r = Pic^0(X_1(N_f p^r)) over Q, K_0 := Q(μ_p), and let
P_r^{tr,†} ∈ (I_r^† ⊗ e'_ord Ĵ_r)(K_0) ⊗ Q_p be the packaged A_r-twisted finite point of H9R16-A/B.
Define

    τ_r^MW := s_r ⊗ ( (U'_p)^{-1} ∘ ϖ_{1,*} )
            = s_r ⊗ ( α_r^{-1} ∘ ⟨u_r⟩_H ∘ U(p)^{-1} ∘ π^{r+1}_r ∘ α_{r+1} )       (equal by 03 Thm C1-c, C1-d)

    τ_r^et := the BCPV contracted dagger transition: the group-ring map of BCPV Remark
              `remark_2023_11_13_1509`(ii) (ψ ↦ (1/p)Σ ψ_g∘ϖ_1^{*⊗3}·pr(g)) composed with ϖ_{1,*},
              the (U'_p)^{-1} normalization, and the modified contraction (1 ⊗ t_2 ⊗ A_r t_3).

STATEMENT R1. Kum_r ∘ τ_r^MW = τ_r^et ∘ Kum_{r+1} as maps
(I_{r+1}^† ⊗ e'_ord Ĵ_{r+1})(K_0) ⊗ Q_p → H^1(K_0, Z_p[G_r]^† ⊗ e'_ord T_p J_r) ⊗ Q_p.

Lane 1 contributes: no Atkin–Lehner operator and no Hida w_r is needed in τ_r^MW when it is written
on the point model (ϖ_{1,*} is Q-rational and U'_p-equivariant); if Hida's form is used, the only
insertion is the Q-rational central tame diamond ⟨u_r⟩_H (u_r ≡ p mod N, ≡ 1 mod p^r).

## R2 — BCPV-internal tame-level Atkin–Lehner bookkeeping (not a W/w issue; needed for C_POINT_NORMALIZATION)

Δ_r^ord uses W_{Np^r} with N = lcm(N_f,N_g,N_g) (BCPV `eqn_2023_11_08_1351`), while A_r uses
W_{N_g p^r} after the tame pushforward X_1(Np^r) → X_1(N_g p^r) (BCPV Def.
`definition_big_diagonal_Hida_families`). Required identity, with t := N/N_g and
pr^t: (A,P) ↦ (A, tP):

    (pr^t)_* ∘ W_{Np^r} = ⟨?⟩ ∘ W_{N_g p^r} ∘ (pr^t_quot)_*       (exact diamond/degeneracy to be computed)

where pr^t_quot is the other tame degeneracy map. KLZ2 §2.5 (W_{QQ'} = ⟨Q'⟩_Q W_Q W_{Q'}) and BSV
Lemma 6.1 are the relevant printed relations. BCPV print λ_{Np^r}(g_λ) in (1154)/(1858) but
λ_{N_g p^r}(g) in (1848)/(0654); when N_g ≠ N the former is not defined for g new of level N_g p^r.

## R3 — Dagger group-ring convention on the Jacobian factor

If the MRS receptacle is I_r^† ⊗_{Z[G_r]} J_r with G_r acting on J_r through diamonds (rather than
I_r^† ⊗_Z J_r with G_r acting only on I_r), then the G_r-action must be transported by
α_r^{-1}⟨d⟩_H α_r = ⟨d⟩_pt (03 Thm C1-e). Using the Albanese μ-model diamonds g_d instead composes
the group ring with g ↦ g^{-1} and replaces ⟨χ⟩_r^{-1/2} by ⟨χ⟩_r^{+1/2}. Which of the two receptacles
H9R8 intends must be fixed before R1 is attempted.
