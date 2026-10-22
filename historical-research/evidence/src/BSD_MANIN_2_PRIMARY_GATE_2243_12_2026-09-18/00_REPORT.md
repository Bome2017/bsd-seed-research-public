# MANIN_2_PRIMARY_GATE_2243_12: v₂(c₀) ≤ 8 (derived; independent referee PASS_WITH_CORRECTIONS, see §6, which governs; MERGED 2026-09-18 with one operator editorial correction, see §8)

**Task (operator, 2026-09-18).** Prove or disprove v₂(c₀) ≤ 17 for the strong Weil curve E₀ in the isogeny class of the seed (2243, 12), N = 2³·3·2243·4547²·5843. Constraints: source-first; do not rerun L₅; no class groups; do not assume Manin's conjecture.

**Verdict proposed: `V2_C0_LE_8_DERIVED`.** The argument below derives **v₂(c₀) ≤ 8** from published theorems. The 17 needed has a margin of 9.
- It is a *derived* lemma. No source states it verbatim.
- It is Pasten's method (arXiv:1705.09251, §10), sharpened with Česnavičius–Neururer–Saha, with the constant made explicit for v₂(N) = 3.
- It uses nothing about E beyond v₂(N) = 3 and 3 | N.
- No computation is used in the proof; the referee ran independent numerical sanity checks.

## 0. Sources read (text extractions with line numbers are in `src/` here and in `~/BSD_MANIN_4547_EDIXHOVEN_CHECK_2026-09-18/src/`)

| label | statement used | where |
|---|---|---|
| CNS 5.15 | ω_f ∈ H⁰(X₀(N), Ω) for a normalized newform f (Ω = relative dualizing sheaf of X₀(N) over Z) | CNS.txt l. 2693 |
| CNS 6.2 | For X normal, proper, flat over a DVR R with X_K irreducible and X^sm ∩ X_k ≠ ∅: H⁰(𝒥, Ω¹) ⊆ H⁰(X, Ω), with **equality iff X has rational singularities** | CNS.txt l. 2749 |
| CNS 6.12(c) | X₀(N)_{Z₍₂₎} has rational singularities if some prime p′ ≡ 3 (mod 4) divides N | CNS.txt l. 3016 |
| CNS 7.2 proof | how (7.2.1) ω_f ∈ H⁰((J_Γ)_{Z(p)}, Ω¹) is combined with π∘π^∨ = [deg φ] | CNS.txt l. 3063–3095 |
| CNS 6.5 | c_π ∈ Z; c_{π′} = c_π · #Coker(Lie ℰ → Lie ℰ′) for isogenous quotients | CNS.txt l. 2815 |
| CNS §5.9 (KM 13.4.7, 13.5.6) | components of X₀(N)_{F_p} ↔ pairs (a, b) with a + b = v_p(N); multiplicity e(a, b) = φ(p^{min(a,b)}) | CNS.txt l. 2454 |
| CNS 6.10(vi) (KM 12.2.1) | over a supersingular point the p-part of the cyclic subgroup is the unique ker(F^n) | CNS.txt l. 2970 |
| ARS12 Thm 3.6(a), per Agashe arXiv:0810.5176v2 §1 | the modular exponent (= deg φ for an elliptic curve) divides the congruence exponent, i.e. the exponent of S₂(Z)/(S₂(Z)[I_f] + S₂(Z)[I_f]^⊥), where S₂(Z) = cusp forms on Γ₀(N) with integral q-expansion | Agashe0810.txt l. 43–77 |
| Pasten 10.1–10.5 | the method: v_p(c_f) is bounded by comparing S₂(R) with H⁰(X, Ω) and using the congruence exponent; the constant is abstract there | Pasten.txt l. 2263–2540 |

The following are standard and are not re-sourced here:
- the adjunction formula ω·C = 2p_a(C) − 2 − C² for vertical prime divisors on a regular arithmetic surface (Liu 9.1.37);
- genus, cusp and supersingular counts for torsion-free congruence subgroups;
- the q-expansion principle at ∞;
- the S2 property of the dualizing sheaf of a normal Cohen–Macaulay surface.

## 1. Notation (R = Z₍₂₎)

| symbol | meaning |
|---|---|
| X | X₀(N)_R |
| 𝒥 | the Néron model of J₀(N) over R |
| π: J₀(N) ↠ E₀ | the optimal quotient; φ = π ∘ ι_∞ |
| ω | a Néron differential of E₀ |
| f, ω_f | the newform and its differential; π•ω = c₀·ω_f (the pullback of ω along the Néron-model extension of π) |
| S | S₂(Γ₀(N), R), the cusp forms with R-integral q-expansion at ∞ |
| H | H⁰(X, Ω) ⊆ S |
| χ | the Hecke eigensystem of f |
| P_χ | the Petersson projection onto the line Q·ω_f |
| M_χ | M ∩ Q·ω_f, for a lattice M |

## 2. Step A (exact reduction): v₂(c₀) ≤ e′, where e′ is the 2-adic exponent of S/H

1. **H is the Néron lattice.** CNS 6.12(c) applies because 3 | N and 3 ≡ 3 (mod 4). So X has rational singularities, and CNS 6.2 gives H = H⁰(𝒥, Ω¹).
2. **H_χ = R·ω_f.** By CNS 5.15, ω_f ∈ H. It has a₁ = 1, so it is primitive in S and therefore in H.
3. **π•ω lies in H** (Néron mapping property). Hence the torsion of H/R·π•ω is H_χ/R·c₀ω_f ≅ R/c₀R, and its exponent is v₂(c₀).
4. **Composition with the dual.** π∘π^∨ = [deg φ] (CNS Lemma 7.1). The map (π^∨)•: H → R·ω is Hecke-equivariant, with T acting on E₀ through χ, so by multiplicity one it factors through P_χ.
   - Write P_χ(H) = R·η, with [P_χ(H) : H_χ] = 2^κ, and (π^∨)•η = u·ω.
   - Then deg φ·ω = (π^∨)•(π•ω) = c₀·2^κ·u·ω.
   - So **v₂(deg φ) ≥ v₂(c₀) + κ.** This is Pasten's (25).
5. **Congruence exponent.** ARS12 Thm 3.6(a) gives v₂(deg φ) ≤ v(S/(S_χ + S_χ^⊥)) = v(P_χ(S)/S_χ). Here S_χ = H_χ = R·ω_f, and 2^{e′}S ⊆ H gives [P_χ(S) : P_χ(H)] ≤ 2^{e′}. So **v₂(deg φ) ≤ e′ + κ.**
6. **Combine 4 and 5:** v₂(c₀) ≤ e′.

The unknown κ cancels. This is where the CNS input ω_f ∈ H improves Pasten's 2v(coker) + v_p(deg π) to a single e′.

## 3. Step B: e′ ≤ 8 by intersection theory at 2

1. **Pull back to a regular model.** Let X_m be the regular model over R of X_{Γ₀(N) ∩ Γ₁(5)} (KM 6.6.1; Γ₁(5) is rigid; 5 ∤ 2). The forgetful map α: X_m → X is étale at the generic points of the components of the special fibre, where Aut = ±1.
2. **The special fibre of X_m.** Set X′ = X_{Γ₀(N/8) ∩ Γ₁(5)}, which has good reduction at 2. Let μ be its PSL₂(Z)-index and c′ its number of cusps.
   - Genus: 2g′ − 2 = μ/6 − c′.
   - Supersingular points over F̄₂: s = μ/12. There is one supersingular curve, with |Aut| = 24.
   - Components: four, (a, b) ∈ {(3,0), (2,1), (1,2), (0,3)}, **all of multiplicity 1**, since φ(2^{min}) = 1 (CNS §5.9).
   - Each component maps finitely onto X′_{F₂}, so p_a(C_i) ≥ g′.
   - Above each supersingular point there is exactly one point (the Γ₀(8)-part is ker F³; CNS 6.10(vi)), and all four components pass through it. So C_i·C_j ≥ s for i ≠ j, and −C_i² = Σ_{j≠i} C_i·C_j ≥ 3s.
   - For the generic fibre: PSL-index 12μ, and c_m = 4c′ cusps (4 cusps of Γ₀(8), coprime levels). So ω·F = 2g_m − 2 = 2μ − 4c′.
3. **Pole orders.** Take s₀ ∈ S. Then α*s₀ is regular on the generic fibre (it is a cusp form) and regular along C_∞ (q-expansion principle at the ∞-cusp, which lies on the reduced (3,0)-component). So div(α*s₀) = D_hor − Σ_{i≠∞} k_i C_i, with D_hor effective and horizontal.
4. **Bound the largest pole.** Let K = k_{j*} be the maximal k_i.
   - For j*: ω·C_{j*} = D_hor·C_{j*} + K·C_∞·C_{j*} + Σ_{i≠∞, j*} (K − k_i) C_i·C_{j*} ≥ K·C_∞·C_{j*}.
   - Adjunction and the lower bounds give ω·C_i ≥ 2g′ − 2 + 3s for i ≠ j*.
   - Therefore ω·C_{j*} ≤ (2μ − 4c′) − 3(μ/6 − c′ + μ/4) = 3μ/4 − c′.
   - Since C_∞·C_{j*} ≥ μ/12, we get **K ≤ 9 − 12c′/μ < 9, so K ≤ 8.**
5. **Descend to X.** 2⁸·α*s₀ has no vertical poles, so it lies in H⁰(X_m, ω_m). Because α is étale at the generic points of the components, 2⁸·s₀ has no poles in codimension 1 on the normal Cohen–Macaulay surface X. So 2⁸·s₀ ∈ H⁰(X, Ω), and **e′ ≤ 8**.

**Remark (sharper, not used).** If the local branches at a supersingular point are the Kronecker-congruence branches y = x⁸, y = x², x = y², x = y⁸, then the local intersection numbers are 2, 1, 1 / 1, 1 / 2. That gives −C_i² = 4s for all i and K ≤ 5. This needs KM's local equations, which were not read here.

## 4. Consequences for the seed (if the audit passes)

1. **The Manin constant is small.** With 4547 ∤ c₀ (Edixhoven, MANIN_4547_EDIXHOVEN_CHECK_001) and Mazur, c₀ = 2^a with a ≤ 8, so c₀ ≤ 256 and c_E ≤ 512.
2. **Both truncation levels certify.** T₂ needs c_E ≤ 399 575 and T₁ needs c_E ≤ 3 999; 512 is below both. So all 20 [b/25]⁺ are exactly the recovered integers, and a₂ ≡ 152 ≡ 2 (mod 5) unconditionally.
3. **The Sha conclusion.** Kato plus Stein–Wuthrich Thm 6.1 then give ord_T L₅ = 2, v₅(L₅*) = 0, b₅ = 0, and **Sha(E/Q)[5^∞] = 0**. No p-adic BSD, no Skinner–Urban, no Manin conjecture.
4. **Scope of Step B.** It is uniform: every optimal E/Q with v₂(N) = 3 and a prime ≡ 3 (mod 4) dividing N has v₂(c₀) ≤ 8. That is a derived statement, not a published one.

## 5. What could break it (audit targets)

1. **Step A.4.** Does multiplicity one give ker(π^∨)• ⊇ H ∩ (Q·ω_f)^⊥? It should: T_ℓ for ℓ ∤ N separates f from oldforms by strong multiplicity one.
2. **Step A.5.** Is ARS12 Thm 3.6(a) stated for Γ₀(N) with integral q-expansion at ∞ and the Petersson complement? This file relies on Agashe's restatement; the original was not read.
3. **Step B.2.** Are there exactly four components, each finite onto X′? Could there be extra multiplicities or components over the cusps?
4. **Step B.3.** Is α*s₀ regular along C_∞ exactly when s₀ has an integral q-expansion (q-expansion principle on a regular model at a reduced component)?
5. **Step B.4.** Arithmetic and signs; the adjunction convention.
6. **Step B.5.** Descent of pole orders through α, and the S2 property of Ω on X.

## 6. Independent referee audit: PASS_WITH_CORRECTIONS. This section governs.

The referee worked in a fresh context, read-only, with PARI capped at 60 CPU-s and 1 GB per run. Notes and scripts: `referee/REFEREE.md`, `referee/eprime_check.gp`, `referee/stepA_check.gp`. **The bound v₂(c₀) ≤ 8 stands**; no correction changes it.

**Corrections applied:**
1. **A.4 (repairable).** Replace "Hecke-equivariant" with the following.
   - π∘t = χ(t)∘π for t ∈ T, since I_f = ker χ. Dualizing gives t^∨∘π^∨ = χ(t)·π^∨, where t^∨ is the Rosati transpose.
   - For ℓ ∤ N the T_ℓ correspondence is symmetric, so T_ℓ^∨ = T_ℓ and (π^∨)•∘T_ℓ• = χ(T_ℓ)·(π^∨)•.
   - The anemic algebra ⟨T_ℓ : ℓ ∤ N⟩ is Petersson-self-adjoint. By strong multiplicity one, its χ-eigenspace in S₂(Γ₀(N), Q) is Q·ω_f.
   - Hence ker((π^∨)•⊗Q) = (Qω_f)^⊥, and (π^∨)• = g∘P_χ with g: P_χ(H) → R·ω injective (compare Pasten l. 2481).
2. **A.4 (cosmetic).** u is defined by g(η) = u·ω, where η generates P_χ(H).
3. **B.1 (cosmetic).** Regularity of X_m: KM 6.6.1 away from the cusps, CNS Lemma 5.10 at the cusps. Étaleness of α at the generic points of the special fibre: CNS Lemma 5.8.
4. **B.3 (cosmetic).** The coefficient of C_∞ in div(α*s₀) is ≥ 0. Take s₀ primitive at ∞, which loses no generality; a positive coefficient only strengthens the inequality.
5. **B.2 (cosmetic).** p_a(C_i) ≥ g′ needs C_i geometrically integral. The (1,2) and (0,3) components map purely inseparably onto X′_{F₂}, with degrees 2 and 8, which preserves the genus.
6. **§3 Remark (not used).** The Kronecker branches describe images in X(1) × X(1), not branches in X_m. If the components are smooth, the same local numbers follow from adjunction together with CNS Prop. 5.6 and 5.12. Using all three pole constraints then gives K ≤ 4. This is conditional and not used.
7. **§0/§4.**
   - CNS 6.5's formula assumes connected kernels, and it is not used for the seed.
   - Instead, the seed's parametrization is φ₀ (if E = E₀) or ψ∘φ₀, with ψ the 2-isogeny. Since ψ*ω_E = c_ψ·ω_{E₀} with c_ψ | deg ψ = 2 (CNS, proof of Cor. 7.3, l. 3110), **c_E | 2c₀**.
   - The 4547 exclusion is audited in MANIN_4547_EDIXHOVEN_CHECK_001.

**Referee numeric checks:**
- X_{Γ₀(M)∩Γ₁(5)} has genus 1, 5, 33, 81 at M = 3, 7, 24, 56, as the formula predicts.
- The newform 24a sits exactly on the CNS (5.14.1) thresholds.
- The exact e′ is 0, 2, 3, 3 at N = 24, 56, 88, 152, all within the bound of 8.
- κ ≤ v₂(deg φ) ≤ v₂(r_E) ≤ e′ + κ holds on 56a1, 56b1, 88a1, 152a1 and 152b1 (Cremona c₀ = 1).

**Not checked against primary sources:**
- Katz–Mazur 13.4.7, 13.5.6, 12.2.1 and 6.6.1 (only through CNS's restatements).
- Liu 9.1.37 (the sign was checked only by internal consistency).
- Deuring's mass formula (for s = μ/12).
- ARS12 (two restatements, which agree).
- Conrad's BDP17 Appendix B.

## 7. Proposed ledger block (NOT merged; awaiting operator acceptance)

```
MANIN_2_PRIMARY_GATE_2243_12 — V2_C0_LE_8_DERIVED  (strong Weil curve of the (2243,12) class; referee PASS_WITH_CORRECTIONS)
  DERIVED lemma (not a verbatim theorem; Pasten 2017 Sec. 10 method, sharpened by CNS and made explicit): every optimal E/Q with
  v_2(N) = 3 and some prime = 3 (mod 4) dividing N has v_2(c0) <= 8.
  Step A: X_0(N)_Z(2) has rational singularities (CNS 6.12(c); 3 | N), so H = H^0(X_0(N),Omega) = H^0(Neron J_0(N),Omega^1)
    (CNS 6.2) and omega_f in H is primitive (CNS 5.15). pi pi^v = [deg phi] with T_l (l not | N) self-adjoint and strong
    multiplicity one gives v_2(deg phi) >= v_2(c0) + kappa. deg phi | congruence exponent (ARS12 Thm 3.6(a), restated in
    Agashe 0810.5176) gives v_2(deg phi) <= e' + kappa, where e' = 2-exponent of S_2(Gamma0(N),Z_(2))/H. So v_2(c0) <= e'.
  Step B: the regular model X_{Gamma0(N) cap Gamma1(5)} has four reduced fibre components (a,b), a+b = 3, at 2 (KM 13.4.7 and
    13.5.6 via CNS 5.9), all through each of the mu/12 supersingular points (ker F^3). Adjunction + genus/cusp counts give pole
    order K <= 9 - 12c'/mu < 9, so e' <= 8. (K <= 4 if the components are smooth; not used.)
  Sanity: exact e' = 0, 2, 3, 3 at N = 24, 56, 88, 152; Step A inequalities hold on 56a1, 56b1, 88a1, 152a1, 152b1.
  Not read directly: Katz-Mazur, Liu 9.1.37, ARS12 itself (two restatements agree), Deuring mass formula.
CONSEQUENCE (with 4547 not | c0): c0 = 2^a, a <= 8; c_E | 2c0 (c_psi | deg psi, CNS Cor 7.3 proof), so c_E <= 512 < 3999 (T1)
  and < 399575 (T2). All 20 [b/25]+ are the recovered integers, a_2 = 2 (mod 5), and
  SMALL_SEED_2243_12_SHA5 = PROVED_ZERO (via the derived lemma above): ord_T L_5 = 2, v_5(L_5*) = 0, b_5 = 0,
  Sha(E/Q)[5^inf] = 0 for the seed (2243,12). Uses Kato + Stein-Wuthrich Thm 6.1 only; no p-adic BSD, no Skinner-Urban,
  no Manin conjecture.
```

## 8. Operator acceptance (2026-09-18). MERGED.

**Decision.** The operator's review (lane 1) accepts the gate and merges it with one editorial change. The review reports an independent reconstruction of Steps A and B and no remaining mathematical gap in the seed-specific argument.

**Editorial correction applied.** §0 header, last bullet: "No computation was run." now reads "No computation is used in the proof; the referee ran independent numerical sanity checks." Nothing mathematical changes. The pre-merge report hash was `0a1f03296873adc8a77609d87502cfea27e39db462386104803370a594068a56`; the backup copy is not part of this record.

**What the operator's review checked against the sources (as reported by the operator; not re-read here):**
- CNS Thm 6.12(c): rational singularities at 2 when a prime ≡ 3 (mod 4) divides N (here 3 | N), so Step A's lattice equality holds.
- ARS Thm 3.6(a), read in the original (Agashe–Ribet–Stein, math.fsu.edu/~agashe/math/moddeg3.pdf): the modular exponent divides the congruence exponent. This removes the "ARS read only through restatements" item at operator level. It was not re-read locally.
- CNS §5.9: the components of X₀(N)_{F₂} are indexed by (a, b) with a + b = 3 and have multiplicity φ(2^{min(a,b)}) = 1.
- CNS's proof identifies the supersingular 2³-level structure as ker(F³), so all four components meet above every supersingular point.
- The intersection bound K ≤ 9 − 12c′/μ < 9, so K ≤ 8.

**Provenance items still open (retained as secondary-source dependencies):** Katz–Mazur 13.4.7, 13.5.6, 12.2.1 and 6.6.1 (through CNS only); Liu 9.1.37 (sign checked by internal consistency only); Deuring's mass formula (s = μ/12); Conrad's BDP17 Appendix B.

**Merged status.**

    MANIN_2_PRIMARY_GATE_2243_12 = V2_C0_LE_8_DERIVED   (MERGED)
    SMALL_SEED_2243_12_SHA5 = PROVED_ZERO   (via the derived v_2(c0) <= 8 lemma)

With 4547 ∤ c₀: c₀ = 2^a with a ≤ 8, and c_E | 2c₀, so c_E ≤ 512 < 3 999 (T₁). All 20 [b/25]⁺ are the recovered integers, and a₂(L₅) ≡ 2 (mod 5) unconditionally. Hence ord_T L₅(E, T) = 2, v₅(L₅*) = 0, b₅ = 0 and **Sha(E/Q)[5^∞] = 0**. The proof uses Kato and Stein–Wuthrich Thm 6.1 only: no Manin conjecture, no p-adic BSD, no Skinner–Urban.
