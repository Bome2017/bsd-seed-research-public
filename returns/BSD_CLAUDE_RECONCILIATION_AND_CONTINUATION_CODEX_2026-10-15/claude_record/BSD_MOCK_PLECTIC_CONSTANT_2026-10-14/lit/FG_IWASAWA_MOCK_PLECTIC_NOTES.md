# Fornea–Gehrmann, "Iwasawa theory and mock plectic points": implementation notes

Paper: arXiv:2311.03100v2 (HTML dated 2 Dec 2024). I read the whole text on 2026-10-14, through WebFetch and the hash-bound snapshot `~/BSD_PLECTIC_ACTUAL_EVALUATOR_ATTEMPT_CODEX_2026-09-30/sources/FG_v2.html` (sha256 b8981a06…). The two copies agree.

Tags: **[FG x]** paraphrase of the paper at x (no verbatim quotes); **[INF]** my inference; **[REC]** project record; **[DATA]** my point counts or local Cremona ecdata; **[LEAD]** not read.

## 0. Bottom line

1. **FG define no p-adic L-function of E.** There is also no interpolation formula, no leading-term formula, no rational constant and no value of Q_K. FG say they cannot yet test Q_K ≠ 0 numerically [§1, after Rem. 1.4].
2. **Their only Gross-point objects are the mod-p^k theta elements λ_m of level-raised forms** [§3.4.4]. By Thm 3.16 (m = 1) plus Lemma 3.12, λ_ℓ vanishes at 𝟙, with first derivative ord_p(q)·loc_ℓ(Q_K) mod p^k [INF]. This is the record's P_D.
3. **Without normalization (25), this sees Q_K only up to a unit in (Z/p^k)^× per ℓ.** It tests the direction in Conj. 2.16 and the valuation v_p of its scalar, not the scalar's rational value [INF].
4. **For rank-2 E/Q with rank E^K(Q) = 0, Q_K ≠ 0 requires non-split p (a_p = −1).** At split p, Thm 3.4 forces Q_K = 0 [INF]. So **389a1 (a_389 = +1 [DATA]) is a zero control, not a constant source.**

## 1. Main theorems and normalizations

**Setting** [Ass. 1.1, §2.1]:
- K is imaginary quadratic, K ≠ Q(i), Q(√−3), with p inert.
- E/Q has conductor N, unramified in K, and multiplicative reduction at p.
- N = pN⁺N⁻, where N⁻ (the part of N/p made of primes inert in K) is squarefree with an even number of primes. Hence ε(E/K) = +1.
- B is indefinite of discriminant N⁻, R is an Eichler order of level pN⁺, and X is its Shimura curve (X₀(N) if N⁻ = 1).
- Γ^p = R[1/p]^×₁.

**Q_K** [§2.2; Prop. 2.6; Def. 2.7; (8), (9), (12), (13)]:
- **Lift of φ.** The parametrization φ: J_X → E is normalized by x ↦ (T_{ℓ₀}−ℓ₀−1)[x]/(a_{ℓ₀}−ℓ₀−1). Because E is multiplicative at p, it lifts uniquely to a Γ^p-equivariant class c_φ on Z[𝓗] ⊗ St(Z).
- **Definition.** Q_ψ := c_ψ(z_ψ ⊗ f_ψ), with f_ψ(t) = (t−τ_ψ)/(t−τ̄_ψ). This is a multiplicative integral.
- **Limit form (9).** Q_ψ = lim_n Σ_{α∈U₀/U_n} (ᵠP_n)^{rec(α)} ⊗ α.
  - ᵠP_n = c_ψ(z_ψ ⊗ e_n^ψ) are the trace-compatible Heegner points of conductor cp^n (8).
  - Tr_{H_{cp}/H_c} ᵠP₁ = 0 (Lemma 2.8).
  - K_p^×/Q_p^× ≅ K^×_{p,1} via x ↦ x^{1−σ_p}.
- **Target.** Kummer maps (10) and Tate's uniformization (11) put Q_ψ in H¹(H_c,V_pE) ⊗ H¹_f(K_p,V_pE)^{−a_p}. Then Q^χ = e_χQ_ψ, and **Q_K = Q^𝟙 with c = 1** (13).
- **Conventions.** rec uses geometric Frobenius (1). Q_ψ depends only on φ and the Γ^p-class of ψ. e_𝟙 = h_K^{−1}Σ_{Pic O_K}σ [INF].

**Proved:**
- **Cor. 2.9:** Q_ψ is G_{H_c}-invariant, in the (−a_p·ε(E/Q))-eigenspace of complex conjugation.
- **Prop. 2.11:** Q^χ is a Selmer class (⊗ local) ⇔ L(E/K,χ,1) = 0.
- **Lemma 3.12, eq. (22):** κ^∞ ∈ H¹(K, V_pE⊗I) and **ord_p(q)·Q_K ≡ κ^∞ (mod I²)**.
  - κ^∞ = lim_k κ₁ is the Λ-adic Heegner class.
  - q is the Tate period; Λ = Z_p[[G]], G = Gal(K_∞/K), I its augmentation ideal.
  - Q_K is read through K^×_{p,1} ≅ K_p^×/Q_p^× →rec G ≅ I/I² [§3.4.3].
- **Thm 3.4 (= 1.3)**, under Ass. 1.1–1.2: if L(E/K,1) = 0 and Q_K ≠ 0, then r_p(E/K) = 2 and max_±{r_p(E^±/Q) + δ_p^±} = 2.
  - Notation: E⁻ = E^K, and δ^± = 1 iff a_p(E^±) = +1.
  - Proof: ord_I κ^∞ ≤ 1, so Thm 3.3 (Howard: ord_P char X_tors ≤ 2·ord_P κ^∞) gives rank X_G ≤ 3. Parity then gives 2.
  - The global factor of Q_K lies in Sel(E^∘), ∘ = sign(−a_p ε(E/Q)).

**Conjectures** (both assume L(E/K,χ,1) = 0):
- **Conj. 2.13.** For χ quadratic (including 𝟙): Q^χ ≠ 0 ⇔ max_±{r^±_alg + δ_p^±} = 2. Otherwise: Q^χ ≠ 0 ⇔ r_alg(E/K,χ) = 2.
- **Conj. 2.16.** Q^χ lies in the image of ∧²E(H_c)^χ under
  P∧Q ↦ 𝒦(P) ⊗ 𝒦_p^{−a_p}(Q) − 𝒦(Q) ⊗ 𝒦_p^{−a_p}(P),
  where 𝒦_p^{−a_p} := (1−a_pσ_p)∘loc_p∘𝒦. **No scalar is specified.**

FG link Q_K only to κ^∞, never to an L-function.

## 2. Hypotheses

- **E:** multiplicative at p (split or non-split). Thm 3.4 and §3 also need p ≥ 5, ρ̄_{E,p} surjective, and ρ̄ ramified at every ℓ | N⁻ with ℓ² ≡ 1 mod p [Ass. 1.2]. Lemma 3.12's proof uses the Hecke-optimal quotient of J_X.
- **p:** inert in K. E/K_p is then split multiplicative [§3.0.1].
- **Primes of N/p:** split ones go to N⁺ (any exponent; split is used in Prop. 3.10). Inert ones go to N⁻ (squarefree, even count).
- **Signs:** ε(E/K) = +1. Thm 3.4 also assumes L(E/K,1) = 0.
- **Admissible ℓ** [§3.1, (16)–(17)]: ℓ ∤ N, inert in K, ℓ² ≢ 1 mod p, and a_ℓ ≡ ε_ℓ(ℓ+1) mod p^k.
- **Pairing (20):** needs 6 to be invertible.

**My consequences for rank-2 E/Q with rank E^K(Q) = 0** [INF]:
- a_p = −1: the global factor lies in the E(Q)-part.
- a_p = +1: r_p(E/Q)+δ⁺ ≥ 3, so Thm 3.4 gives Q_K = 0. Consistently, (1−σ_p) kills E(Q_p).
- For a semistable rank-2 curve the number of split primes is odd, so two usable primes need ω(N) ≥ 3.
- [DATA] a₁₉(817a1) = −1, a₄₃ = +1, a₃₇(37a1) = −1, a₁₀₉(109a1) = +1, consistent with FG's examples.

## 3. The anticyclotomic L-function objects

**(a) Nothing for E.**
- The only mention is Rem. 3.5. The Burungale–Castella–Kim argument needs anticyclotomic p-adic L-functions that are nonzero mod p at 𝟙. In the multiplicative case these have an exceptional zero there, citing [CH18, Thm A].
- FG give no construction, no θ·θ*, no interpolation formula and no Euler factors.

**(b) Why there is none** [INF, Tunnell–Saito]:
- For χ ramified at p, the Steinberg local sign at p is +1. The ramification set N⁻∪{∞} is then odd, so ε(E/K,χ) = −1.
- Those characters are handled by Heegner points on FG's indefinite X, through κ^∞.
- Characters unramified at p get a definite algebra ramified at pN⁻∞, which has no Bruhat–Tits tree at p.
- Definite algebras with a tree at p arise only after level-raising at an odd number of admissible primes.

**(c) Recipe for λ_m** [§3.3, §3.4.4]:
- **Index.** m ∈ 𝒩_k^def is a product of an odd number of k-admissible primes.
- **Algebra and order.**
  - B_m is **definite of discriminant mN⁻**, ramified at the primes of mN⁻ and at ∞.
  - R_m is an Eichler order of **level pN⁺**.
  - S_m = B_m^×\B̂_m^×/R̂_m^×.
- **Eigensystem mod p^k** (Def. 3.6, (18)): T_q ↦ a_q(E) for q ∤ Nm; U_q ↦ a_q(E) for q | N; U_ℓ ↦ ε_ℓ for ℓ | m.
- **Multiplicity one** (Cor. 3.9): the eigenspace in (Z/p^k)[S_m] is free of rank one, so g_m is unique up to a unit. FG's display writes S_{mℓ}, an evident typo for S_m.
- **Pairing (20):** ⟨[a],[b]⟩ = δ_ab·w_[a]^{−1}, with w_[a] having prime factors ≤ 3. Hecke operators are self-adjoint.
- **Tree model.** Forms are R_m[1/p]^×-invariant functions on oriented edges of the PGL₂(Q_p) tree, with U_p g(e) = Σ_{s(e')=t(e)} g(e'). The sum excludes e' = ē, as Lemma 2.8 and π(h_{n+1}) = U_p h_n require [INF].
- **CM data.**
  - ψ: K ↪ B_m with ψ(K) ∩ R_m[1/p] = ψ(O_K[1/p]) (23).
  - e_n^ψ are consecutive edges leaving the K_p^×-fixed vertex v_ψ.
  - e_n^ψ is an order with ψ(O_{p^n}) optimal, O_{p^n} = Z+p^nO_K. These are the Gross points of conductor p^n; there are h_K(p+1)p^{n−1} of them [INF].
- **Theta element.**
  - h_n^ψ = Σ_{σ∈Gal(H_{p^n}/K)} [σ]·[ψ_σ(e_n^ψ)], and π(h_{n+1}) = U_p h_n.
  - (24): λ̃⋄_m = lim a_p^{−n}h_n^ψ ∈ Z[S_m]/I_{φ_m} ⊗ Λ, projecting to Gal(K_n/K) with K_n = H_{p^n} ∩ K_∞.
  - λ⋄_m = ⟨λ̃⋄_m, g_m⟩, and **λ_m = ord_p(q)·λ⋄_m ∈ Λ/p^k** (Def. 3.14).
  - Other choices change λ by a group-like element (Rem. 3.13).
- **Status.** λ_m belongs to a congruent level-raised system, not to E, and exists only mod p^k.

## 4. Vanishing order and leading terms

**From FG.**
- κ^∞ vanishes at 𝟙, from Tr P₁ = 0, and its first derivative is ord_p(q)·Q_K [L. 3.12].
- If Q_K ≠ 0, then ord_I char X_tors ≤ 2 [Thm 3.4 proof]. The 2 is the square in Perrin-Riou's main conjecture.

**Derivative of λ_ℓ** [INF].
- Thm 3.16 at m = 1 gives λ_ℓ = loc_ℓ(κ₁), via the identification fixed by (25).
- Hence **λ_ℓ ≡ ord_p(q)·(loc_ℓ⊗id)(Q_K) mod (I², p^k)**, and λ_ℓ(𝟙) ≡ 0.
- The zero at 𝟙 also follows from p-newness: star sums vanish and f(ē) = −a_p f(e).
- The derivative is therefore independent of the Rem. 3.13 choices.
- The product λλ* (not in FG) would have I²/I³ coefficient −λ'(𝟙)².

**Under Conj. 2.16**, with E(K)⊗Q = QP⊕QQ [INF]:
- Q_K = c·(𝒦(P)⊗ρ(Q) − 𝒦(Q)⊗ρ(P)), with c ∈ Q_p.
- ρ is 𝒦_p^{−a_p}, then (11)⁻¹, then rec.
- For P, Q ∈ E(Q) with a_p = −1, ρ(X) is twice the anticyclotomic log of X's Tate parameter.
- If p ∤ ord_p(q):
  **λ⋄_ℓ'(𝟙) ≡ u_ℓ·c·[dlog_ℓ(P)ρ(Q) − dlog_ℓ(Q)ρ(P)] (mod p^k).**
  - dlog_ℓ is taken in the cyclic group E(F_{ℓ²})[p^∞].
  - u_ℓ ∈ (Z/p^k)^× is fixed only by (25).

**Constant: FG predict none.**
- There are no Sha, Tamagawa numbers, torsion or height regulator anywhere.
- ord_p(q) enters only through Selmer integrality (Prop. 3.10).
- The Conj. 2.16 regulator is a mixed Kummer ⊗ Tate-parameter determinant, not det⟨P_i,P_j⟩. A bridge to "K_E × height determinant" needs outside input.
- [LEAD] Darmon, "A refined conjecture of Mazur–Tate type for Heegner points", Invent. Math. 110 (1992), is the likely place to look for such constants. I saw only a search snippet; the PDF returned 403.

## 5. Sections 3.3–3.4 and the record's P_D

**§3.3 defines:** B_m (indefinite for m ∈ 𝒩^ind, with m = 1 giving FG's B; definite for m ∈ 𝒩^def; level pN⁺), X_m, J_m, S_m, 𝕋_m, the level raising φ_m (Def. 3.6, (18)), and (19). It proves existence (§3.3.1: Ribet, BD05 Thm 5.15, Lemma 3.7) and gives the pairing (20) and Cor. 3.9.

**§3.4 defines:** CM families with Tr x_{n+1} = U_p x_n (21); κ⋄_m(p^n) = a_p^{−n}Σ_{Gal(H_{p^n}/K_n)} 𝒦(δ_m(x_n^ψ)^σ), Selmer after multiplying by ord_p(q) (Prop. 3.10, Def. 3.11); Lemma 3.12; and λ_m. Reciprocity: Thm 3.15 gives loc_ℓκ_m = λ_{m/ℓ} (ordinary part, ℓ | m); Thm 3.16 gives loc_ℓκ_m = λ_{mℓ} (unramified part, ℓ ∤ m), with g_{mℓ} *defined* by (25) as the local Kummer map ⟨·, g_{mℓ}⟩. Cor. 3.17: a bipartite Euler system.

**Link to Q_K:** only via (22) at m = 1, and to the λ's only by reciprocity.

**The record's P_D** [REC, 02_FINITE_FIELD_REDUCTION.md]:
- P_D = π([D₁]), with D₁ = Σ_σ j(σ̄)([x_σ]−[x₀]) over conductor-p² CM reductions.
- It equals c₁(λ_ℓ) via (25), at k = 1, ℓ = 46807, p = 5843.
- By §4, P_D ∝ ord_p(q)·loc_ℓ(Q_K) [INF].
- The seed had |S_ℓ| = 2.5·10¹⁹. With N⁻ = 1, |S_ℓ| ≈ (ℓ−1)ψ(N)/12.

## 6. Algorithm for a small control [INF]

**Candidates** [DATA, ecdata]. All are proved Γ₀-optimal with Manin constant 1, and `nonmax_primes` is empty. The rank of E^K(Q) is still to be checked.

| curve | p (non-split) | K (h_K) | ord_p q | K_E | role |
|---|---|---|---|---|---|
| 817a1 = 19·43 (FG Ex. 1.7) | 19 | Q(√−7) (1) | 2 | 8 | first test |
| 817a1 | 43 (split) | Q(√−15) (2) | – | 8 | zero control |
| 1001c1 = 7·11·13 | 7; 13 | Q(√−43); Q(√−19) (1; 1) | 2; 2 | 48 | two primes |
| 3565a1 = 5·23·31 | 5 | Q(√−43) (1) | 2 | 40 | v₅(K_E) = 1 (k = 2) |

**Steps.** Throughout, N⁻ = 1, so X = X₀(N) and B_ℓ is ramified at {ℓ, ∞}.

1. **Checks:** a_p = −1; p inert in K and every prime of N/p split; p ∤ h_K; ρ̄_p surjective; L(E^K,1) ≠ 0; E Γ₀(N)-optimal.
2. **Admissible ℓ:**
   - Search ℓ ∤ N·d_K with ℓ inert in K, ℓ ≢ ±1 mod p, and a_ℓ ≡ ε_ℓ(ℓ+1) mod p^k. The Hasse bound forces ℓ ≥ (p^{k/2}−1)².
   - Primes with ε_ℓ = +1 are informative.
   - Primes with ε_ℓ = −1 are zero controls: E(F_ℓ) has no p-torsion and the global factor is in the E(Q)-part.
3. **Class set S_ℓ:**
   - Build it with Sage `BrandtModule(ℓ, N)` (prime discriminant) or the project's E02 `brandt.py` (certified equivalence, mass check).
   - The mass is (ℓ−1)ψ(N)/12, i.e. 73, 112 or 384 times (ℓ−1) for the three curves.
4. **Eigenfunction f: S_ℓ → Z/p^k:**
   - Take the joint kernel of T_q − a_q(E) for small q ∤ Nℓ, using neighbor-count matrices on functions. Then f(x) = ⟨[x], g_ℓ⟩ and the w-weights are built in.
   - Check U_q (q | N) and the ℓ-involution eigenvalue ε_ℓ, and require dimension 1.
   - Lift to mod p^k by Hensel lifting.
5. **Gross points of conductor p^n, n = k+1** ([K_n:K] = p^{n−1}; the record used H_{p²}):
   - Fix one optimal ψ_n: O_{p^n} ↪ R, with R a level-N order.
   - Set x_σ = the class of Rψ_n(𝔞) for each [𝔞] ∈ Pic(O_{p^n}). Sage `BruhatTitsQuotient` is an alternative; check whether it needs Magma when N⁺ > 1.
   - The count is h_K(p+1)p^k: 380 (p = 19, k = 1), 7220 (k = 2), 30 or 150 (p = 5).
   - Choosing the wrong orientation multiplies f by −a_p = +1, so it is harmless.
   - Compute j(σ̄) through σ^{h_K} = rec(α), using the trace-zero coordinate of log_p(α^{p+1}). Use the same coordinate for ρ.
6. **Derivative:**
   - Check Σ_σ f(x_σ) ≡ 0.
   - Set D_ℓ := (−1)^n Σ_σ j(σ̄)f(x_σ) mod p^k. This is λ⋄_ℓ'(𝟙).
7. **Global side:** take Cremona's generators P, Q and compute dlog_ℓ in E(F_ℓ)[p^∞]. Compute ρ from the Tate parameter u ∈ O^×_{K_p,1} (component group cleared) via log_p(u^{p+1}); test PARI `ellpointtoz` and Sage `tate_curve` on non-split curves. Precision O(p^{k+3}) suffices.
8. **Comparison.** Compare with det_ℓ := dlog_ℓ(P)ρ(Q) − dlog_ℓ(Q)ρ(P), **not** with the height determinant. Tests that need no normalization unit:
   - (i) the zero at 𝟙;
   - (ii) zeros at every ε_ℓ = −1 prime;
   - (iii) over ε_ℓ = +1 primes, v_p(D_ℓ) − v_p(det_ℓ) is constant and equals v_p(c); at k = 1 this is the vanishing pattern;
   - (iv) at split p, D_ℓ ≡ 0 for all ℓ;
   - (v) at fixed (E, p, ℓ), two fields K₁ and K₂ share S_ℓ and g_ℓ, since (25) does not involve K. So u_ℓ cancels in (D/det)_{K₁}/(D/det)_{K₂}, giving c_{K₁}/c_{K₂} mod p^k.
   - **c itself mod p^k needs (25)**: the mod-ℓ modular parametrization on a supersingular divisor with nonzero E(F_ℓ)[p]-part. This is the record's open problem.
   - Across two primes, only each v_{p_i}(c) can be compared.
9. **Cost** (rough): class enumeration dominates, at about |S_ℓ|·(q+1) equivalence tests. k = 1 with N ≲ 10³ gives 10³–10⁵ classes (routine); k = 2 only for p ≤ 7; k ≥ 3 is out of reach except perhaps at p = 5.

## 7. Numerical examples in the paper

FG give only Examples 1.5–1.7:
- **37a1**, K = Q(√−2): ranks 1 over Q and 2 over K; non-split at 37.
- **109a1**, K = Q(√−2): ranks 0 and 2.
- **817a1**, K = Q(√−7), p = 19: ranks 2 and 2.

FG expect Q_K ≠ 0 in all three. They check only L(E/K,1) = 0, by sign for 1.5 and in SageMath for 1.6–1.7; the curves came from LMFDB. Nothing is computed for Q_K, κ^∞ or λ_m.
