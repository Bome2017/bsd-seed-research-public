# 00 — Verdict (H9R16-C, Lane 1: BCPV W_{N_g p^r} versus Hida w_r)

**Stop condition A reached: an exact formula, proved from the printed definitions.**

1. **Literal equality W = w is ill-typed.** BCPV's X_1(Np^r) classifies (A, P) with P a point of order
   Np^r (BCPV §4.2, DR22 §1.1, KLZ2 §2.3). Hida's X_r classifies (E, μ_{Np^r} ↪ E) (LMW §3, §5). They are
   different Q-forms of the same complex curve; KLZ2 §7.2 prints the resulting diamond-valued Galois twist.
2. **The correct bridge is Galois-rational.** α_r: (A,P) ↦ (A/⟨P⟩, Weil-pairing μ-structure) is defined
   over Q with no choice of root of unity (03 L1).
3. **Exact formula (03 C1-a).** As automorphisms of X_1(Np^r) ⊗ Q(μ_{Np^r}), of its Jacobian, and of
   H^1_et(·, Z_p(1)):

       W^BCPV_{Np^r} = δ_r ∘ α_r^{-1} ∘ w_r ∘ α_r,     δ_r = ⟨c_r⟩^{-1},     ζ^H_{Np^r} = (ζ^B_{Np^r})^{c_r}.

   δ_r is a Q-rational, central, finite-order diamond (03 C1-b). BCPV's printed Lemma
   σ_mΔ^ord[d] = Δ^ord[m^{-1}d] pins the Galois type of their W.
4. **Transition (03 C1-c).** Hida's w-twisted transition on BCPV's curve is
   α_r^{-1}∘π^{r+1}_r∘α_{r+1} = ⟨u_r⟩^{-1}∘ϖ_{1,*}, with u_r ≡ p mod N and ≡ 1 mod p^r. The unit comes from
   Hida's tame-incoherent root ζ_Nζ_{p^r}. The two towers are isomorphic over Q (03 C1-c').
5. **Hecke (03 C1-d, C1-f).** Under α: U'_p ↔ U(p), e'_ord ↔ e, U_p ↔ U^*(p). Also
   A_r = α_r^{-1}∘w_r∘g_{c_r^{-1}}∘U(p)^r∘α_r.
6. **δ_r is harmless (03 §4).** It is MRS-functorial, commutes with Kummer maps, preserves injectivity and
   p-completion, and leaves dagger descent unchanged. On BCPV's own curve nothing needs to be inserted at
   all. Two misuses do break the square:
   * matching BCPV's tower with Hida's untwisted co-ordinary system (Galois-twisted, 03 K1);
   * using Albanese μ-diamonds for G_r, which flips the half-twist (03 D4).

All identities were machine-checked in an exact lattice model, with negative controls (`_verify/`).

LANE = 1 — BCPV W_{N_g p^r} versus Hida w_r (C_W/w_DICTIONARY)
STATUS = STOP_A — EXACT_FORMULA_PROVED_FROM_SOURCES; C_W/w_DICTIONARY = CLOSED; discrepancy = Q-rational central diamond, harmless when inserted per 03 §4
PROVED = (L1) α_r: X_1(Np^r) ≅ X_r^Hida over Q, ζ-free; (C1-a) W^BCPV_{Np^r} = ⟨c_r⟩^{-1}∘α_r^{-1}w_rα_r with ζ^H = (ζ^B)^{c_r}; for KLZ2 roots c_r = ap^r + bN (tame part level dependent); (C1-b) δ_r = ⟨c_r⟩^{-1} is Q-rational, central, finite order, W-inverting; (C1-c) α_r^{-1}π^{r+1}_rα_{r+1} = ⟨u_r⟩^{-1}ϖ_{1,*}, u_r ≡ p (N), ≡ 1 (p^r), and the towers are isomorphic via α_s⟨v_s⟩; (C1-d) U'_p ↔ U(p), e'_ord ↔ e, U_p ↔ U^*(p), U'_q ↔ U(q) (T'_ℓ ↔ T(ℓ) under the printed uniform conventions); (C1-e) α^{-1}g_dα = ⟨d⟩^{-1}; (C1-f) A_r = α_r^{-1}w_r g_{c_r^{-1}}U(p)^rα_r; (§4) δ-insertion rule and harmlessness for the fixed-base dagger/MRS transition
REFUTED = (i) literal W = w (ill-typed: different Q-models); (ii) H9R12's tentative dictionary "U'_p/e'_ord ↔ U^*(p)/co-ordinary untwisted tower" as a Galois-rational identification. It is the ι_ζ-dictionary, which twists Galois by 1 + k + ε_N: TYPE_MISMATCH for Kummer squares over Q or K_0. The Galois-rational match is Hida's w-twisted ordinary system.
FIRST_EXACT_UNPROVED_STATEMENT = R1 (04): Kum_r∘τ_r^MW = τ_r^et∘Kum_{r+1} on (I_{r+1}^†⊗e'_ordĴ_{r+1})(K_0)⊗Q_p → H^1(K_0, Z_p[G_r]^†⊗e'_ordT_pJ_r)⊗Q_p, where τ_r^MW = s_r⊗((U'_p)^{-1}ϖ_{1,*}) = s_r⊗(α_r^{-1}⟨u_r⟩_H U(p)^{-1}π^{r+1}_rα_{r+1}) and τ_r^et is BCPV's contracted dagger transition (group-ring (1/p)-average, ϖ_{1,*}, U'_p-normalization, (1⊗t_2⊗A_rt_3)-contraction)
TYPE_CHECK = PASS for C1-a..f with explicit types (curves, fields of definition, Albanese/Picard, k = 0, full-level Atkin–Lehner); FAIL recorded for the ι_ζ-dictionary over Q/K_0 and for Albanese μ-diamonds in a ⊗_{Z[G_r]} dagger receptacle
NEW_ASSUMPTIONS = none mathematical. Convention readings, all non-load-bearing or absorbed: (a) BCPV's unprinted W_{Np^r} is the KLZ2 §2.5 full-level moduli Atkin–Lehner for some root ζ^B, any root allowed and absorbed into c_r, Galois type pinned by BCPV Lemma (ii); (b) weight two (k = 0), where ⟨−1⟩ = 1 and W^{-1} = W; (c) Picard reading of Hida's ⟨z⟩, used only for consistency and C1-e translation. Standard facts used: Weil-pairing compatibility with dual isogenies; representability for Np^r ≥ 4.
COUNTEREXAMPLE_OR_OBSTRUCTION = none against C1. Obstructions to misuse, each explicit and exactly tested: omitting ⟨u_r⟩ fails whenever p ≢ 1 mod N (NEG6: 48/72 fail); using W^B without ⟨c_r⟩ fails (NEG7: 240/288 fail); the ι-dictionary is off by the Galois character 1 + k + ε_N; Albanese μ-diamonds flip ⟨χ⟩^{-1/2} to ⟨χ⟩^{+1/2}; the p-part W_{p^r} would add ⟨p⟩_N-powers. BCPV print λ_{Np^r}(g_λ) and λ_{N_gp^r}(g) for the same normalization (out of lane, R2).
NEXT_SMALLEST_TEST = decide the receptacle (R3: I^†⊗_Z J versus I^†⊗_{Z[G_r]} J), then extend `_verify/wl_dictionary_check.py` to a tame pair N_g | N and compute the exact diamond/degeneracy identity linking (ϖ^t_1)_*∘W_{Np^r} with W_{N_gp^r} (R2)
ARISTOTLE_READY = NO
STOP_ROUTE = NO
