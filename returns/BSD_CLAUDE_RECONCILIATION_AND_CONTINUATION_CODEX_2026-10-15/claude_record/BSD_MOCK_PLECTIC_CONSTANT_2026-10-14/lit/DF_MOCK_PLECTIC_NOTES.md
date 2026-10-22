# Darmon–Fornea, "Mock plectic points": notes for the K_E-constant experiment

Written 2026-10-14. Tags: **[P]** stated in the paper (paraphrased, formulas transcribed); **[Dr]** the McGill-hosted draft; **[I]** my inference; **[S]** my scan of the local Cremona tables (`~/run013-bsd-scout-2026-08-22/_data/ecdata/curvedata`, N < 500000).

**Sources, read in full.** Published version: J. Inst. Math. Jussieu 24(5) (2025) 2107–2131, doi:10.1017/S1474748025000179, open access (CC BY 4.0); received 28 Oct 2023, revised 2 Apr 2025. arXiv:2310.16758 has only v1 (25 Oct 2023), read via ar5iv. Numbering below is the published one. The published version adds Remarks 1.3 and 2.1, so v1's Lemma 1.3, Thm 1.4, Conj 2.1 are published Lemma 1.4, Thm 1.5, Conj 2.2. Section 3 numbering is identical. The McGill URL (`.../83.MPP/Mock_plectic_points.pdf`) is **not** the paper: it is a 4-page undated draft (acknowledgements left as a to-do, an open question in blue) with a general-level set-up (see §1).

## 1. Setting and notation
- [P] **Group and space.** Γ := SL₂(Z[1/p]) (the Ihara group), with no congruence condition. It acts diagonally by Möbius maps on H_p × H, where H_p = P¹(C_p) − P¹(Q_p). The quotient S := Γ\(H_p × H) is the "mock Hilbert modular surface" (Intro). Γ₀(p) appears only as the stabiliser of the edge e_∞ of the Bruhat–Tits tree T (§1.2).
- [P] **Level is p only.** f ∈ S₂(Γ₀(p)) is p-new with rational coefficients, and E/Q is its strong Weil curve, of conductor p (§1.4; Lemma 3.5 assumes semistable of prime conductor p ≥ 11). There is no M. Remark 1.3 says an auxiliary level N prime to p would use the matrices of SL₂(Z[1/p]) that are upper-triangular mod N, with Γ₀(Np) and p-new forms of level Np. This is not developed.
- [P] **Attached to f:**
  - (3): a heuristic two-variable "mock Hilbert modular form" (the authors call it a non-definition).
  - Def. 1.2: a *system of mock residues* c: E(T) → Ω¹(H), with c(e) a weight-2 cusp form on Γ_e and γ*c(γe) = c(e). Γ-invariant systems ≅ S₂(Γ₀(p))^{p-new} via c ↦ c(e_∞).
  - (8): harmonic cocycles c_f[x,y](e) = 2πi∫_x^y f_e(z)dz. For cusps these give Λ_f-valued measures μ_f[r,s] (Manin–Drinfeld; Λ_f is commensurable with Λ_E).
    - (9): μ_f[0,∞](Z_p) = L(E,1) and μ_f[0,∞](Z_p^×) = (1 − a_p)L(E,1).
    - (10): L_p(E,s) = ∫_{Z_p^×}⟨x⟩^{s−1}dμ_f[0,∞].
  - (12): ω_f[r,s] = ∫_{P¹(Q_p)} dz/(z−t) dμ_f[r,s](t) ∈ Ω¹_rig(H_p) ⊗ Λ_f (Teitelbaum's Poisson kernel (7)).
  - Lemma 1.4: multiplicative primitives F_f[r,s] ∈ (A^×/K_p^×) ⊗ Λ_f with dlog F = ω (13). Here K_p is the unramified quadratic extension of Q_p.
  - Thm 1.5: F_f lifts to a Γ-invariant modular symbol in (A^×/q^Z) ⊗ Λ'_f, where q is the Tate period and Λ'_f = t⁻¹Λ_f. The periods J_f satisfy ord_p J_f[0,∞] = δ_p(E)L(E,1) and log J_f[0,∞] = δ_p(E)L'_p(E,1).
  - §3: E(C)-valued cocycles c_f[x] for x ∈ Σ := Γτ_∞ (eq. 17). These become Ê(K_∞)-valued measures μ_f[x], then differentials ω_f[x] ∈ Ω¹_rig(H_p) ⊗̂ Ê(K_∞) (19), then primitives F_f[x] ∈ (A^×/K_p^×) ⊗̂ Ê(K_∞). Here Ê(K_∞) := lim_n E(K_∞)/pⁿ.
  - No H¹ or H² class of Γ is defined. H¹(Γ, MS(·)) appears only as the obstruction group in the proof of Thm 1.5.
- [Dr] **General level, draft only.** The set-up:
  - K imaginary quadratic and N = N⁺N⁻ prime to disc K. The primes of N⁻ are exactly the inert ones; N⁻ is squarefree; ε(E/K) = (−1)^{ω(N⁻)+1}. Take ε = +1 and p | N⁻.
  - B is the indefinite quaternion algebra of discriminant N⁻/p, with an Eichler order of level N⁺p. Γ^p = norm-one units of R[1/p], modulo ±1.
  - Embeddings ψ of conductor c·pⁿ.
  - Def. 1.2: P_{φ,ψ} := ⨏^{τ_ψ}∫^{x_ψ} ω_{φ,ψ} ∈ Ê(K^c_∞) ⊗_{Z_p} K̂_p^×.

  No conjecture, constant or numerics.

## 2. Mock CM points
- [P] **§2 (comparison case).** RM points τ ∈ H_p ∩ K, with K real quadratic and p non-split. The Stark–Heegner point P_τ = F_f[r,γ_τ r](τ) ∈ E(C_p) ⊗ Λ'_f. Conj. 2.2 says P_τ^± is defined over ring class fields.
- [P] **§3 CM points.** K is imaginary quadratic, embedded diagonally in C_p × C, and τ = (τ_p, τ_∞) ∈ (H_p × H) ∩ K.
  - As a simplifying assumption, the associated order (16) is the maximal Z[1/p]-order, with class number one, and p is inert. Ramified p is set aside. No other primes enter.
  - [I] pO_K is principal, so this means h_K = 1: D ∈ {−3,−4,−7,−8,−11,−19,−43,−67,−163} with (D/p) = −1.
- [P] **§3.2 tower and Heegner points.**
  - K_n is the ring class field of conductor pⁿ, and K_∞ = ∪K_n is totally ramified above p. rec gives G_∞ ≅ K_{p,1}^×, the norm-one elements of K_p^×.
  - A is the CM curve by O_K. Its p-isogeny tree T_A ≅ T, edges e_n = (v_{n−1},v_n), and G_n = K_{p,1}^×/U_n.
  - P_n ∈ X₀(p)(K_n) is the point of e_n, with Tr P_{n+1} = U_pP_n.
  - Rem. 3.1: y_n := φ_E(a_p(E)ⁿ(P_n − ∞)) ∈ E(K_n). These are trace-compatible.
  - Key identity (displayed just before (18)): c_f[τ_∞](α·e_n) = y_n^{rec(α)}.
- [I] The P_n are p-isogenies between CM curves with endomorphism rings of conductor p^{n−1} and pⁿ. They are not classical Heegner points, so Sage's `heegner_point` does not give them. [K_n:K] = (p+1)p^{n−1}/u_K, with u_K = 3, 2, 1 for D = −3, −4, and otherwise.
- [P] Every ring-class twist L(E/K,χ,s) of prime-to-p conductor has sign +1, so E(K) has even rank and there are no Heegner points over K.

## 3. The invariant
- [P] **§3.4 definition.** τ_p and τ̄_p are the two fixed points on H_p of the torus ι_τ(K_p^×). Then
  - Q^×(τ) := F_f[τ_∞](τ_p)/F_f[τ_∞](τ̄_p) ∈ Ê(K_∞) ⊗̂ K_{p,1}^×;
  - **Q(τ) := log Q^×(τ) = ∫_{τ̄_p}^{τ_p} ω_f[τ_∞] ∈ Ê(K_∞) ⊗̂ K_p**, which determines Q^× up to (p²−1)-torsion.
- [P] **Where it lives.**
  - Lemma 3.3: Q(τ) is G_∞-invariant.
  - §3.6: after choosing a topological generator of K_{p,1}^×, Q(τ) is viewed, non-canonically, in Ê(K_∞)^{G_∞} ↪ H¹(K,T_pE). Lemma 3.5 gives E[pⁿ](K_m) = 0, and Lemma 3.6 gives H¹(K,E[pⁿ]) ≅ H¹(K_m,E[pⁿ])^{G_m}.
  - So it is a **pro-p Galois cohomology class**. The archimedean input (τ_∞ and φ_E) only produces algebraic Heegner points. The p-adic input is the logs of norm-one units. It is not in C_p, and it is not in E(K_p) ⊗ E(C).
  - [I] On K_{p,1}^×, log ᾱ = −log α, so the K_p-coefficients lie on the line √D·Q_p.
- [P] **§3.5 p-adic L-function.**
  - (20): A(x) = (x−τ_p)/(x−τ̄_p): P¹(Q_p) → K_{p,1}^×, and μ_{f,K} := A_*μ_f[τ_∞].
  - (21): L_p(E,K,s) := ∫⟨α⟩^{s−1}dμ_{f,K}, in the sense of BD96 §2.7.
  - **Thm 3.4: L_p(E,K,1) = 0 and Q(τ) = L'_p(E,K,1).**
  - (22): Q(τ) = lim_n Σ_{α∈K_{p,1}^×/U_n} y_n^{rec(α)} ⊗ log⟨α⟩.
  - Proof of Thm 3.8: Q^×(τ) = lim D_n y_n, with the Kolyvagin derivative D_n y_n := Σ y_n^{rec(α)} ⊗ α, and the cocycle (23).
- **Numerical evaluation.** None is given, and ⟨α⟩ is never defined. [I] The recipe would be (22). The level-n sum gives Q(τ)/p mod p^{n−1}. Level 1 gives nothing, because log kills μ_{p+1}. So n = 2 is the first level with mod-p information.

## 4. Conjectures (§3.8)
- [P] **(24).** Set E⁺ := E and E⁻ := E′ (the twist by K), with δ^± = 1 if a_p(E^±) = +1 and 0 otherwise. Then BD96 Conj. 4.1 suggests ord_{s=1}L_p(E,K,s) = ϱ = max{1, r_alg(E^±/Q) + δ^± − 1}, and 2ϱ ≥ max{2, r_alg(E/K)}. [I] "±" must mean a maximum over both signs; either single sign contradicts Conj. 3.12, in the (2,0) or the (0,4) case.
- [P] **Rem. 3.11.** L_p(E,K,s) is BD96's p-adic L-function with the *extended* Mordell–Weil group collapsed to the usual one.
- [P] **Conj. 3.12.** If L(E/K,1) = 0, then Q(τ) ≠ 0 exactly when (r_alg(E/Q), r_alg(E′/Q)) is:
  - (0,2), if a_p(E) = +1;
  - (1,1), if a_p(E) = −1.
- [P] **Conj. 3.13.** Define log_E^{a_p} := log_E∘(1 − a_p(E)σ_p): E(K_p) → K_p, where σ_p generates Gal(K_p/Q_p). If L(E/K,1) = 0, then Q(τ) **lies in the image** of
  ∂: ∧²E(K) → H¹_f(K,T_pE) ⊗_{Z_p} K_p, P∧Q ↦ δ_∞(P)⊗log_E^{a_p}(Q) − δ_∞(Q)⊗log_E^{a_p}(P).
  Here δ_∞ is the Kummer map and H¹_f is the pro-p Selmer group (Def. 3.7). This is how the abstract's "alternating square of the Mordell–Weil group" is made precise.
- [P] **Rem. 3.14 and closing.** Compare FGM22, Conjs. 1.5 and 1.3. The invariant is forced into one complex-conjugation eigenspace and "can sometimes vanish for trivial reasons" (e.g. E(Q) of rank two). A fuller invariant, the true "mock plectic points" built from Hida deformations of f, is future work. It should avoid the degeneracies of anticyclotomic height pairings in BD96 Conj. 4.1.
- **Specific constant? No.** The paper mentions no Sha, Tamagawa numbers, torsion, Manin constant, L-value or explicit multiple. Literally, ∂ is defined on ∧²E(K) as an abelian group, so for rank E(K) = 2 the conjecture says Q(τ) = m·∂(P∧Q) for some unspecified m ∈ Z.
- [I] **Conventions that change m but are not fixed:**
  - the factor |E(Q)_tors| in (17);
  - replacing E by the isogenous curve C/Λ_f (no Manin constant is mentioned);
  - the sign a_pⁿ in y_n;
  - the differential defining log_E;
  - the choice of generator in §3.6.
- [I] **Coefficient-line check.**
  - In the (0,2) case, with P, Q ∈ E(K)⁻, log^{a_p} = 2log_E lies in √D·Q_p, the same line as Q(τ). So m ∈ Q_p is meaningful.
  - In the (1,1) case, ∂(P∧Q) = −2δ_∞(Q)⊗log_E(P) has Q_p-coefficients, while Q(τ) has √D·Q_p-coefficients. The literal reading would force Q(τ) = 0, against Conj. 3.12.
  - So the conjecture is effectively a proportionality statement. **DF give no canonical rational constant.**

## 5. Hypotheses
- **E.** [P] Conductor p prime, p ≥ 11 (Lemma 3.5, via Mazur's surjectivity theorem). Either split or nonsplit reduction (a_p = ±1) is allowed. The hypothesis of Thm 3.9 forces split.
  - [I] For prime conductor the root number equals a_p, so even rank ⟺ split. Every analytic-rank-2 curve of prime conductor is split.
- **K.** [P] Imaginary quadratic, with the maximal Z[1/p]-order of class number one, and p inert. In BD96's terms this is "non-split exceptional indefinite". There, "non-split" refers to p being inert, not to the reduction type.
- **Ranks.** [P] Conj. 3.12 assumes L(E/K,1) = 0; Thm 3.9 assumes L(E/K,1) ≠ 0. [I] ε(E′) = ε(E), consistent with the (0,2) and (1,1) patterns.

## 6. Theorems
- [P] **Thm 1.5:** uses MTT/Greenberg–Stevens, L'_p(E,1) = (log q/ord_p q)·L(E,1).
- [P] **Thm 3.4:** Q(τ) is the first derivative of the Mordell–Weil-valued anticyclotomic L_p(E,K,s).
- [P] **Thm 3.8:** res_p Q(τ) ∈ H¹_f(K_p,T_pE) ⟺ L(E/K,1) = 0. The proof uses the Néron component groups Φ_n and adapts BD97 Thm 5.1, with Gross and McCallum.
- [P] **Thm 3.9:** L(E/K,1) ≠ 0 ⇒ E′(Q) is finite. Here Q(τ) lies in the minus eigenspace, and res_p Q(τ) spans H¹_sing(Q_p,V_pE′); the argument then uses Poitou–Tate duality (BD97, Cor. 7.2 and Props. 6.5, 6.8).
- [P] **Rem. 3.10:** finiteness of E(K) needs tame deformations.
- Complex L-values enter only as central values. Nothing is proved about L″(E/K,1) or about rank 2.

## 7. Numerical examples
None. There are no curve labels, discriminants, precisions or tables. The Data availability statement says no data were generated or analysed. Experimental work is only cited: DL03 and GM13 (ATR points), FGM22 (plectic p-adic invariants), FG23 (partial evidence).

## 8. Software and reproducibility
- [P] No software is named.
- [I] darmonpoints (Masdeu, Sage) targets the §2 Stark–Heegner points, not §3. This is my recollection and is unchecked.
- [I] There is nothing to reproduce. A from-scratch Sage/PARI build needs custom code: enumerate the edge points P_n, evaluate φ_E by q-expansion, recognise y_n over K_n (or reduce at auxiliary primes), form D_n y_n, descend via Lemma 3.6.
- The obstruction is the degree [K_2:K] (§9 item 5), so Magma's absence is not the bottleneck.

## 9. Assessment for the K_E experiment
1. **The current control curves are useless here.** 389a1 and 433a1 are split at p (prime conductor, rank 2). Conj. 3.12 predicts Q(τ) = 0 for every admissible K. [I] Moreover ∂ ≡ 0 on ∧²E(Q), because (1−σ_p)P = 0 for P ∈ E(Q_p). This is DF's "trivial vanishing". 664a1 (additive at 2, nonsplit at 83) is out of scope. Under a general-level analogue its a_83 = −1 would make ∂ nonzero on ∧²E(Q), but DF state nothing there. So there is no ratio to form.
2. **[S] Admissible curves.** The rank-2 curve must be the twist E′ = E^{(D)}, with E of prime conductor p, rank 0 and split at p.
   - Scan criteria: rank-2 E′ with N′ < 500000 whose minimal quadratic twist has prime conductor p, D of class number one, and p inert.
   - Result: **125 admissible (0,2) triples**, plus 91 (2,2) triples where Q(τ) is predicted to be 0 (e.g. 563a1/203243c1).
   - Smallest p:

     | p | E | D | E′ | E′ data |
     |---|---|---|---|---|
     | 109 | 109a1 | −8 | 6976f1 | Tam 4, Sha 1, tors 1 |
     | 139 | 139a1 | −4 | 2224f1 | Tam 4, Sha 1, tors 1 |
     | 179 | 179a1 | −3 | 1611d1 | Tam 4, Sha 1, tors 1 |
     | 307 | 307b1 | −4 | 4912g1 | also D = −7, −11, −19 at this p |
     | 571 | 571a1 (Sha 4) | −4 | 9136c1 | |

   - There is no triple with p < 109 in the table. The table covers D = −163 only for p ≤ 17.
3. **What to compute.**
   - Compute Q(τ) mod p^{n−1} via (22), i.e. via D_n y_n.
   - Descend it to H¹(K,E[p^{n−1}])⁻ = H¹(Q,E′[p^{n−1}]) and locate it in E′(Q)/p^{n−1}.
   - Prediction: Q(τ) = 2m(δ(P)⊗log_E Q − δ(Q)⊗log_E P), where P, Q generate E′(Q), viewed inside E(K)⁻.
   - [I] Both logs lie in √D·Q_p, so res_p∂(P∧Q) = 0. The directional content of Conj. 3.13 is therefore just res_p Q(τ) = 0. The class sits on the line ℓ_Q P − ℓ_P Q, with ℓ = log_E/√D.
   - [I] All remaining content is the scalar m. No rational localisation (at p or at ℓ ≠ p) sees it; only integral mod-p^k global data can.
4. **Ratio to compare.** Compare m ∈ Q_p (with the §4 conventions fixed) against normalisations of K_{E′} or K_{E/K}.
   - [I] Q(τ) is built from Heegner points, which behave like square roots of L-values (Gross–Zagier index ≈ c·∏c_ℓ·√#Sha). So test m² as well as m, allowing for the factors 2 (from 1−a_pσ_p), |E(Q)_tors| and the Λ_f isogeny.
   - A constant-bearing statement, if one exists, would be BD96 Conj. 4.1 (not read).
   - At n = 2 only m mod p is visible, so the test is weak.
5. **Cost.**
   - [K_2:K] = 11990 (p = 109), 9730 (p = 139), 10740 (p = 179). Recognising y_2 at these degrees is out of reach.
   - Level n = 1 (degrees 110, 70, 60) is feasible in days but carries no p-adic information.
   - [I] **Not computable with Sage and PARI by known methods.**
6. **Two primes p.** This is impossible for a fixed rank-2 curve. p is E′'s unique multiplicative prime, and (E, D) is fixed by the minimal twist. The draft's general level needs (N, disc K) = 1, which E′ violates.
7. **Next reads** for a constant: BD96 Conj. 4.1, and FGM22 Conjs. 1.3, 1.5 and 1.6, which come with numerics.
