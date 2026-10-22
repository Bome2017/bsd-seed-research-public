# ASSUMPTIONS — A1: every hypothesis at the formal boundary, tagged

Tags:
- **FORMAL_ASSUMPTION** — a modelling choice or bookkeeping hypothesis, justified below;
- **PROVED_IN_PACKAGE** — discharged by another target of this package;
- **IMPORTED_ARITHMETIC_THEOREM** — a published theorem or standard fact about the curve, entered as a hypothesis and never proved here;
- **NOT_PART_OF_THIS_TASK** — deliberately outside the task. This includes the open antecedent, which appears as an explicit hypothesis.

## Hypotheses of T7 `WC_abstract` (abstract witness form)
| # | hypothesis (Lean) | tag | justification / source |
|---|---|---|---|
| H1 | `∀ p ∈ P, ∀ S, ∃ a, ∀ x : M p S, p^a • x = 0` | FORMAL_ASSUMPTION; PROVED_IN_PACKAGE for the group-ring model (T3 + T10) | Codex WC §1: "M(p,S) is a finite p-primary module" |
| H2 | `AddMonoid.IsTorsion Sha` | IMPORTED_ARITHMETIC_THEOREM | Sha ⊆ H¹(Q, E) is a torsion group (standard). Used in WC (3) |
| H3 | `∀ p ∈ P, ¬ (Sha[p^∞]).Finite → 3 ≤ r p` | IMPORTED_ARITHMETIC_THEOREM | Codex WC §2: Sel(Q, E[p^∞]) is cofinitely generated; corank = rank E(Q) + corank Sha[p^∞]; rank E(Q) = 2 (RANK, retained); a cofinitely generated p-primary group of corank 0 is finite |
| H4 | `∀ p ∈ P, ∀ S, 3 ≤ r p → t p S = 0` | IMPORTED_ARITHMETIC_THEOREM (witness form of Ota Thm 5.17) | the group-ring form (T8/H11) implies it by T4 (PROVED_IN_PACKAGE) |
| H5 | `∀ p ∈ P, ∀ S, ¬ PDvd p 1 (t p S) → ∀ x : Sha, p • x = 0 → x = 0` | IMPORTED_ARITHMETIC_THEOREM (Ota Thm 1.5, a special case of Thm 6.4) | a witness not in p·M(p,S) forces Sha[p] = 0 (Ota also gives p ∤ J_S, unused). See the S-class note in SOURCE_EXCERPTS |
| H6 | `A ≠ 0`, `A ∈ JE t (primesOutside S0)` | **NOT_PART_OF_THIS_TASK** (the open antecedent) | Codex: "WC_ANTECEDENT_FOR_SEED = UNKNOWN; NONZERO_ELEMENT_OF_J_E = NOT CONSTRUCTED". Never to be proved |
| H7 | hypothesis of conclusion (3): the primary groups at S0 are finite | NOT_PART_OF_THIS_TASK | for the seed, the parts at 2, 3, 5 are retained theorems and those at 2243, 4547, 5843 are OPEN (Codex) |

## Additional hypotheses of T8 `WC_groupRing` (Ota 5.17 in group-ring form)
| # | hypothesis | tag | justification / source |
|---|---|---|---|
| H8 | `2 ∈ S0` | FORMAL_ASSUMPTION | Codex's S0 = {2,3,5,2243,4547,5843}. It gives p ≥ 3 on P, hence min(r, p) ≥ 3 ⟺ r ≥ 3 |
| H9 | `0 < e p S ∧ ∀ g, g^(e p S) = 1` | FORMAL_ASSUMPTION; PROVED_IN_PACKAGE for (ZMod S)ˣ (T11) | G_S ≅ (Z/SZ)^× is finite abelian. The cyclotomic identification itself is NOT_PART_OF_THIS_TASK (standard) |
| H10 | `∀ p ∈ P, ∀ u, ¬ p ∣ u → IsUnit (u : Rp p)` | FORMAL_ASSUMPTION; PROVED_IN_PACKAGE for ℤ_[p] (T10) | the only property of Z_p that is used |
| H11 | `∀ p ∈ P, ∀ S, θ p S ∈ I^(min (r p) p)` | IMPORTED_ARITHMETIC_THEOREM (Ota Thm 5.17, as printed) | hypotheses of Ota 5.17 at p ∈ P: p ∤ 6N·\|E(F_p)\|·∏ m_ℓ, ρ_{p^∞} surjective; S a squarefree product of good ℓ with E(F_ℓ)[p] cyclic. Codex checked them for the seed (non-anomalous by 2-torsion + Hasse; ∏ m_ℓ = 16; residual image GL₂(F_p) for odd p, lifted for p ≥ 5) |
| H12 | `∀ p ∈ P, 2 ≤ r p` | IMPORTED_ARITHMETIC_THEOREM | corank Sel ≥ rank E(Q) = 2 |
| H13 | H2, H3, H5 (with t := cls2 θ), H6, H7 | as above | — |

## Implicit modelling choices (FORMAL_ASSUMPTION, documented)
- **F1. Base change.**
  - Ota's I_S lives in R[G_S] with R ⊂ Q (p ∉ R^×); Codex's M(p,S) is over Z_p.
  - Since Z_p is flat over R and R/p = F_p, the condition "θ̃ ∉ p·M" is the same over R and over Z_p. Not formalized.
- **F2. p-integrality.**
  - θ_S ∈ Z_p[G_S] for p ∈ P: the seed's modular-symbol denominators are powers of 2.
  - This is IMPORTED (retained project fact) and implicit in modelling θ as an element of `MonoidAlgebra (Rp p) (G p S)`.
- **F3. The admissible family W p.**
  - Codex's family: squarefree products of good ℓ ∤ pN, ℓ ≡ 1 (mod p), E(F_ℓ)[p] cyclic.
  - The Ota inputs H4, H5 and H11 are assumed for all S : W p. This matches Ota Thm 1.5 exactly (see SOURCE_EXCERPTS).
- **F4. The factor ½ and the "+" quotient** in Ota's §2 normalisation do not change depths at odd p.
- **F5. Universes.** Objects live in `Type`. This is harmless: every arithmetic object is a set-sized structure.

## What is NOT assumed anywhere (hostile checks passed)
- **No hidden `J_E ≠ 0`.** The antecedent appears only as the explicit hypothesis H6. No definition presupposes it.
- **No hidden FIN.**
  - Local finiteness (1) and vanishing (2) are conclusions.
  - Global finiteness (3) is a conclusion conditional on H7.
  - No hypothesis mentions finiteness of Sha or of Sha[p^∞] for p ∈ P, except inside the contrapositive form of H3
    ("infinite ⇒ corank ≥ 3"), which is a Selmer fact.
- **Finite support and local finiteness are not conflated.**
  - (1), (2) and (3) are separate conclusions.
  - The regression targets T9a and T9b refute "nonzero at every p ⇒ finite support".
- **No LINE, GPR, ETNC, BSD, FIN or FORMULA** input.
