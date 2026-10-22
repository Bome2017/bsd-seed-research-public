# Referee report on 00_REPORT.md (v₂(c₀) ≤ 8)

Date: 2026-09-18. Scope: Steps A and B of `../00_REPORT.md`, checked against `src/Pasten.txt`, `src/Agashe0810.txt`, and `~/BSD_MANIN_4547_EDIXHOVEN_CHECK_2026-09-18/src/CNS.txt`. No downloads. The report, the sources, the ledgers and the memory files were not edited.

## Verdict: PASS_WITH_CORRECTIONS

- Steps A and B are both valid.
- Every correction below is either a presentation fix or fills a justification gap. None changes the bound, which stays **v₂(c₀) ≤ 8**.
- Two small independent computations agree with the argument (§3).

## 1. Source checks

| claim in report | source line | status |
|---|---|---|
| CNS 5.15: ω_f ∈ H⁰(X₀(N), Ω) | CNS l.2691–2700 | matches; Remark 5.16 (l.2720) also gives primitivity |
| CNS 6.2: H⁰(𝒥, Ω¹) ⊆ H⁰(X, Ω), with equality ⇔ rational singularities | l.2749–2757 | matches; the report omits "excellent DVR" and "relative curve". Z₍₂₎ is excellent, and Example 6.3 (l.2787) confirms the hypotheses for X₀(N)_{Z(p)} |
| CNS 6.12(c) | l.3016–3019 | applies: 3 ≡ 3 (mod 4). So do 2243, 4547 and 5843, which are all ≡ 3 (mod 4) |
| multiplicity e(a,b) = φ(p^min(a,b)) | l.2454–2462, footnote 5 l.262–266 | matches; every component has multiplicity 1 at p = 2 |
| supersingular: C = ker Fⁿ | l.2970 | matches |
| ∞ reduces to the (n,0) component | Lemma 5.11 proof, l.2522–2526 | matches |
| ARS12 3.6(a): modular exponent divides congruence exponent; S₂(Z) = integral Fourier coefficients at ∞; ⊥ = Petersson | Agashe l.43–66 and l.75–77; Pasten l.2488–2497 | matches; no hypotheses for part (a) |
| Pasten (25) and the final bound 2v(coker) + v_p(deg π) | Pasten l.2478–2536 | matches |

## 2. Issues

1. **A.4 (repairable: justification gap).** The report says (π^∨)• is "Hecke-equivariant" but does not justify it.
   - π^∨ intertwines the Rosati-transposed operators, and U_ℓ for ℓ | N is not Rosati-self-adjoint.
   - Fix: use the anemic algebra ⟨T_ℓ : ℓ ∤ N⟩. The T_ℓ correspondence is symmetric for ℓ ∤ N, so T_ℓ is self-adjoint. Strong multiplicity one then gives ker((π^∨)*⊗Q) = (Qω_f)^⊥, as Pasten asserts at l.2481.
   - Alternative fix: W_N acts on A_f^∨ by ±1, which makes π^∨ equivariant for all of T.
   - The bound is unchanged.
2. **A.4 (cosmetic).** "(π^∨)•η" is undefined when η ∉ H. Define u through the factorization (π^∨)* = g∘P_χ, taking u·ω = g(η).
3. **B.1 (cosmetic, citation).** KM 6.6.1 covers regularity at non-cuspidal points only (see CNS l.2968).
   - Regularity at the cusps follows from CNS Lemma 5.10 (l.2468–2511): the formal neighbourhoods are Z[ζ][[q]] or Z[ζ][[X]], and each reduces into a single (a,b)-component.
   - Étaleness of α at the generic points follows from CNS Lemma 5.8 (l.2434) and the gerbe remark in Cor 5.4 (l.2322).
   - This also settles audit target 3: there are no extra components or multiplicities over the cusps.
4. **B.3 (cosmetic).** The coefficient of C_∞ in div(α*s₀) is n_∞ ≥ 0, and it is 0 only when s₀ is primitive at ∞. The fix is to assume s₀ primitive without loss of generality. If the term is kept, it gives K + n_∞ ≤ 8, which is stronger.
5. **B.2 (cosmetic).** The bound p_a(C_i) ≥ g′ needs two facts the report does not state. Each C_i is geometrically integral. The (1,2) and (0,3) components map to X′ by E ↦ E purely inseparably, of degrees 2 and 8, so their genus is still g′.
6. **§3 Remark (cosmetic; the remark is not used).**
   - The branches y = x⁸, … are images in X(1)×X(1), not branches in the regular local ring of X_m.
   - However, the same numbers (2,1,1 / 1,1 / 2) are forced if the components are smooth of genus g′. Equate adjunction with CNS Prop 5.6 and 5.12, using d = (0,0,1,3) and deg ω|C = (1,1,2,8)·s.
   - With all three constraints Σ_i B_ji k_i ≤ 6 − c′/s, where B⁻¹·1 = (2/3, 5/6, 5/6), the bound becomes K ≤ **4**, not 5.
7. **§0 and §4 (outside the audited claim).**
   - CNS 6.5 requires connected kernels.
   - "c_E ≤ 512" assumes c_E | 2c₀, and nothing in this file justifies that.
   - "4547 ∤ c₀ (Edixhoven)": Edixhoven's Thm 3 excludes additive potentially ordinary reduction of Kodaira types II, III and IV (CNS l.77–79). That check was not audited here.

## 3. Arithmetic and numeric checks

**By hand.** All of these match the report:
- the Step A inequality chain;
- s = μ/12 (Aut acts freely on points of exact order 5);
- c_m = 4c′ (needs −1 ∈ Γ₀(8));
- 2g_m − 2 = 2μ − 4c′;
- ω·C_{j*} ≤ 3μ/4 − c′;
- K ≤ 9 − 12c′/μ;
- the adjunction sign, which I cross-checked against the Kodaira–Spencer degrees.

**Numeric checks.** PARI 2.17.4, one process at a time, each run ≤ 37 CPU-seconds and ≤ 522 MB. Scripts are `eprime_check.gp` and `stepA_check.gp`.
- **Genus formula.** g(X_{Γ₀(M)∩Γ₁(5)}) for M = 3, 7, 24, 56 comes out as 1, 5, 33, 81. These equal 1 + μ/12 − c/2, as dimension counts over the even characters mod 5.
- **Normalization.** Newform 24a gives v = (−3, −1, 0, 0), exactly on the (5.14.1) thresholds. This is the sharpness CNS state in Example 4.8.
- **e′.** Computing the exact lattice H from (5.14.1) gives e′(24, 56, 88, 152) = 0, 2, 3, 3. All are ≤ 8, and even ≤ 4.
- **Step A on real optimal curves** (c₀ = 1 and deg φ from Cremona's ecdata):

| curve | κ | v₂(deg φ) | v₂(r_E) | e′ + κ |
|---|---|---|---|---|
| 56a1 | 1 | 1 | 1 | 3 |
| 56b1 | 1 | 2 | 2 | 3 |
| 88a1 | 2 | 3 | 4 | 5 |
| 152a1 | 2 | 3 | 4 | 5 |
| 152b1 | 1 | 3 | 3 | 4 |

  Every row satisfies κ ≤ v₂(deg φ) ≤ v₂(r_E) ≤ e′ + κ. The first inequality is tight for 56a1.

## 4. Consistency with the source authors

- **CNS's remark (l.253–260).** CNS say intersection-theoretic bounds are "far from those needed" for (⋆), the statement that ω_f lies in H with zero denominator. A bound of 2⁸ on the exponent of S/H is consistent with that remark.
- **How the report uses it.** The report proves (⋆) by citing CNS 5.15, and uses e′ only to control the other forms in S, through the congruence module.
- **No contradiction with the literature.** The result is compatible with CNS Thm 7.2, and it sharpens Pasten's abstract constant.

## 5. Not verifiable from local sources

- **KM 13.4.7, 13.5.6, 12.2.1 and 6.6.1.** Checked only through CNS's restatements (cited above).
- **Liu 9.1.37 (adjunction).** Not available. The statement needed is ω·C + C² = 2p_a(C) − 2 for an integral vertical divisor C on a regular surface, with p_a(C) = 1 − χ_k(O_C). I checked only the sign, and only through internal consistency.
- **Deuring's mass formula.** Standard; not in the local sources.
- **ARS12 original.** Checked only through two restatements (Agashe l.75–77 and Pasten l.2488), which agree.
- **Conrad's BDP17 Appendix B.** Not available.
