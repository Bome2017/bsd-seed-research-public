# Step 2: does the chain hold before p-completion?

Grades used here:
- **SOURCE**: printed in BD05 or H06, cited by page.
- **DERIVED**: a short argument given here from SOURCE statements. It is same-session and unreviewed.
- **HEURISTIC**: everything else.

## 2.0 What "integral" has to mean (the CRT trap)

Fix E, K, ℓ and the sign ε. Let m be the part of d_ε := ℓ + 1 − εa_ℓ that is prime to a bad set B. B consists of:
- 2 and 3;
- the primes dividing ℓ² − 1;
- the primes dividing N;
- the primes failing H2–H6;
- the primes dividing η_f, the congruence module of f on S;
- the Eisenstein primes.

Every p-local identity in BD05 holds up to a unit u_p ∈ (Z/p^{n_p})^×. By CRT, such identities glue to one identity in Z/m up to u ∈ (Z/m)^× = ∏_p (Z/p^{n_p})^×. **The glued identity carries exactly the same information.** So "holds over Z/m up to units" adds nothing across p.

The real test is therefore: **can the unit be pinned before p is chosen, to a sign chosen once (not once per p)?**

## 2.1 What BD05 already proves over Z (SOURCE)

These statements involve no p:
- Thm 5.1 (Čerednik–Drinfeld, p. 46).
- Props 5.2–5.5, Lemma 5.6, Props 5.7–5.8.
- Prop 5.9, Ribet's sequence; its remark says the identifications "can be made entirely canonical" (p. 53).
- Cor 5.10.
- Prop 5.11: Φ_ℓ = coker(X_ℓ → X_ℓ^∨).
- Cor 5.12.
- **Prop 5.13**: ω̄_ℓ : Im δ_*/((U'_ℓ)²−1) → Φ_ℓ has Eisenstein kernel and cokernel (p. 55).
- **Prop 5.14**: ∂_ℓ([D]) = ω_ℓ(r_ℓ(D)) (p. 57).
- The Mumford–Tate sequence (49) (p. 60).
- The reduction step of §8: r_ℓ(P_m) = v_m (p. 69).
- The Eichler–Shimura relations of Lemma 9.1 and the Ihara isomorphism (66) (pp. 71–72).

Together these give, inside Φ_ℓ itself (no tensoring with T/I, no p):

  **(G)** the component of a Heegner divisor is ω_ℓ of the divisor of its CM vertices.

## 2.2 Derived integral statements (not stated in BD05 or H06)

### D1. Integral form of Thm 5.15 (DERIVED)

Setup:
- S is the definite Shimura set of discriminant N⁻ and level N⁺ (p ∤ N⁺).
- f : Z[S] → Z is the primitive Jacquet–Langlands eigenform, unique up to ±1.
- I_f⁰ = ker(T → Z).
- Assume (m, η_f) = 1, where η_f is the order of the torsion of Z[S]⁰/I_f⁰Z[S]⁰ (the congruence module of f on S). For p ∤ η_f, f is p-isolated (Def 1.2), and then T_{m_f} = Z_p, so BD's hypothesis (2) holds automatically: Z[S]⁰ ⊗ Z_p localized at m_f is torsion-free of rank 1. So (m, η_f) = 1 is a **sufficient** integral form of hypothesis (2), not an equivalent one.

Then:
1. **f-reading of Z[S]⁰.** Z[S]⁰/(I_f⁰ + m) ≅ Z/m via f.
2. **The 2×2 step.** On Im δ_*/I ≅ (Z/m)², use t_ℓ ≡ a_ℓ ≡ ε(ℓ+1) (mod m).
   - The image of U'_ℓ − ε is {(z, εz)}.
   - U'_ℓ + ε has determinant ≡ 2(ℓ+1), so it is invertible.
   - Over Z, the cokernel of [[a_ℓ−ε, −1], [ℓ, −ε]] is cyclic of order ℓ+1−εa_ℓ, and φ(x,y) = x − εy kills the image.
   - This is BD's computation on p. 59, done over Z. `checks/integral_2x2_check.py` confirms it on 16 seed cases (Smith normal form diag(1, d), 16/16).
3. **The f-reading of Φ_ℓ/I.** With Prop 5.13 (integral) and m non-Eisenstein, the map

     ρ_f : Φ_ℓ/I ≅ Z/m,  ω̄_ℓ(x, y) ↦ f(x) − ε f(y),

   is an isomorphism. It is canonical up to one global sign: the sign of f, and the even/odd labelling (swapping the labels turns ρ_f into −ε·ρ_f).

Thm 5.17 is not used, and neither is multiplicity one mod pⁿ.

### D2. Integral first law at a fixed ℓ, for all p | m at once (DERIVED; tautological)

Let D_ℓ = Σ_σ P_σ be the conductor-1 Heegner divisor on X_{N⁺,N⁻ℓ}, and x_σ the Gross points on S. Then

  ρ_f(∂_ℓ[D_ℓ]) = ± Σ_{σ∈Pic O_K} f(x_σ)  (mod m).

**Proof.** Combine (G) with D1.

**Parity (HEURISTIC detail).** All the vertices v(P_σ) should carry the same even/odd label, so that only one global sign appears. Reason: ℓ is inert, so N(K_ℓ^×) = ℓ^{2Z}Z_ℓ^×. This is consistent with BD's (61) (p. 69), ∂_{λ_m}(P_m^σ) = [σ, e_m]_f, which has no σ-dependent sign. Not checked line by line against Lemma 5.6's {0,1} labelling.

**What this replaces in BD.** It is BD's step C8 read through ρ_f. The multiplicity-one step C9 and its (Z/pⁿ)^× disappear, because no abstract isomorphism Φ_ℓ/I ≃ Z/pⁿ was chosen.

**For the seed.** Σ_σ f(x_σ) = 0, by Gross's formula at the trivial character: L(E,1)·L(E^{−7},1) = 0 (record R4, `BSD_ARISTOTLE_RANK2_ANCHOR_RETURN_2026-10-06/RESULT_RANK2_ANCHOR.md` l.70–79). So D2 reads 0 = 0, which is what rank 2 requires. **This is the endpoint's "best case" depth-1 law: it exists and is vacuous for the seed.**

### D3. Transport to E[m] (DERIVED from SOURCE)

1. **Existence.** An isomorphism u : T(J)/I ≅ E[m] exists: apply Thm 5.17 at each p | m and glue by CRT, since T(J)/I = ⊕_p Ta_p(J)/I.
2. **Non-uniqueness.** Aut_{G_Q}(E[m]) = (Z/m)^× (Schur at each p, by the GL₂(F_p) image).
3. **No geometric source.** No morphism J^{(ℓ)} → E induces u. J^{(ℓ)} is ℓ-new (Cor 5.10) and E has level N with ℓ ∤ N, so Hom(J^{(ℓ)}, E) = 0.

Consequence: every statement BD make in H¹(·, T_{f,n}), including both laws as printed, carries an independent unit at each p, and CRT adds nothing. **This is the exact content of the remark on p. 37.**

### D4. The u-balanced rank-2 constant (DERIVED): the test of kill-clause (ii)

**Setting.** Bottom layer; E(K) ⊗ Z[1/2] = E(Q) ⊗ Z[1/2] (seed: E^{−7}(Q) has rank 0, record). P₁, P₂ is a Z-basis of E(Q)/tors, so P₁ ∧ P₂ is canonical up to sign. (ℓ₁, ε₁) and (ℓ₂, ε₂) are admissible, and m | gcd(d_{ε₁}(ℓ₁), d_{ε₂}(ℓ₂)) is prime to B.

**Canonical objects** (no generator is chosen anywhere):

| Object | Definition | Why canonical |
|---|---|---|
| H₁ | Hom_{G_Q}(E[m], T(J₁)/I) | free of rank 1 over Z/m (Thm 5.17 per p, plus Schur); a module, not a generator |
| α₁ | Φ_ℓ₁/I ≅ H¹_sing(K_ℓ₁, T(J₁)/I) | the geometric map of Cor 5.18 |
| duality | H¹_sing(K_ℓ₁, E[m]) ≅ H¹_fin(K_ℓ₁, E[m])^∨ | Tate duality with **E's own** Weil pairing |
| ⇒ | H₁ ≅ Φ_ℓ₁/I ⊗ H¹_fin(K_ℓ₁, E[m]) | combine the three rows |
| Ξ₁ | H¹_fin(K_ℓ₂, T(J₁)/I) = H₁ ⊗ H¹_fin(K_ℓ₂, E[m]) ≅ Φ_ℓ₁/I ⊗ H¹_fin(K_ℓ₁,E[m]) ⊗ H¹_fin(K_ℓ₂,E[m]) | from the previous row |
| β₁(x'_K) | Kummer ∘ (red_ℓ₂)^{−1} ∘ [x'_K] ∈ H¹_fin(K_ℓ₂, T(J₁)/I) | BD (62)–(65); x'_K is the Gross divisor on S′ (disc N⁻ℓ₁ℓ₂, level N⁺), which is the supersingular locus of X_{N⁺,N⁻ℓ₁} at ℓ₂ (Thm 9.3 proof, p. 74) |
| R(ℓ₁,ℓ₂) | red₁P₁⊗red₂P₂ − red₁P₂⊗red₂P₁ ∈ H¹_fin(K_ℓ₁,E[m]) ⊗ H¹_fin(K_ℓ₂,E[m]) | built only from the points of E(Q) |

**Definition.** When R(ℓ₁,ℓ₂) generates the tensor product,

  **C(ℓ₁,ℓ₂) := Ξ₁(β₁(x'_K)) / R(ℓ₁,ℓ₂) ∈ Φ_ℓ₁/I ≅_{ρ_f} Z/m.**

**Invariance.** No isomorphism u appears in the definition, only the module H₁. If one does pick u and transports to E's side:
- κ = u_*κ_J has u-weight 1;
- the Selmer coefficient c ∈ H¹_fin(K_ℓ₁, E[m])^∨ has u-weight 1;
- pulling back by u^{−1} to H¹_sing(K_ℓ₁, T(J₁)/I) has u-weight −1.

The total weight is 0, so C does not depend on u. The choices that remain are the sign of P₁∧P₂, the sign of f, the parity convention at ℓ₁, and the sign of the Weil pairing. Each is made once per (E, ℓ₁), not once per p. **So C(ℓ₁,ℓ₂) is canonical up to one global sign, with no unit at each p.**

**Ш-free.** The definition uses only E(Q)'s generators, the Gross/Heegner geometry and f. It does not assume Sel(K, E[m]) = E(K)/m.

**Relation to BD and Howard (SOURCE + DERIVED).** Assume Ш(E/K)[m] = 0, so that Sel(K, E[m]) = E(K)/m.
1. At the bottom layer, Thm 4.1's argument gives loc_ℓ₁ κ_J(ℓ₁) = 0. First, v_ℓ₁ = 0, because the Kummer image of local points factors through Φ (Remark 2 after Thm 5.17, p. 63; sequence (49) is integral). Second, ∂_ℓ₁ is the Gross sum (D2), which is 0.
2. Hence κ_J ∧ Q = c_J(red₁Q)·(P₁∧P₂) for a unique c_J ∈ H¹_fin(K_ℓ₁,E[m])^∨ ⊗ H₁ ≅ Φ_ℓ₁/I.
3. Thm 4.2 then gives Ξ₁β₁(x'_K) = −c_J(ℓ₁) ⊗ R(ℓ₁,ℓ₂). So C(ℓ₁,ℓ₂) = −c_J(ℓ₁), independent of ℓ₂.
4. H06 Thm 2.5.1 gives v_p(c_J(ℓ₁)) = δ_p for every ℓ₁.

So everything BD and Howard prove is the statement v_p(C) = δ_p for all (ℓ₁, ℓ₂). **The residue of C mod p is canonical (by D4) but not determined by the sources.**

### D5. Strength of the natural conjecture (DERIVED, using H06 Thm 2.3.7)

**RIGID_LR** (named, not tested). There is C_E ∈ Q such that Ξ₁β₁(x'_K) = ±C_E·R(ℓ₁,ℓ₂) for all admissible pairs and all good m. This is the level-raising analogue of the record's tame law.

If RIGID_LR holds with C_E ≠ 0, take p ∤ C_E·B and a pair with R(ℓ₁,ℓ₂) a unit mod p. Such pairs exist by BD Thm 3.2 / H06 Lemma 2.3.3 (Chebotarev). Then:
1. λ_{ℓ₁ℓ₂} is a unit, so M_{ℓ₁ℓ₂} = 0 and Sel_{F(ℓ₁ℓ₂)} = 0 (H06 Thm 2.3.7, p. 9).
2. The strict Selmer group sits inside it, so it is 0 too.
3. So Sel(K, E[p]) injects into H¹_fin(K_ℓ₁) ⊕ H¹_fin(K_ℓ₂), which has dimension 2, and Ш(E/K)[p] = 0.

So RIGID_LR implies Ш(E/K)[p] = 0 for every good p ∤ C_E. **That is the strength of FIN.** RIGID_LR is a target in a new coordinate (the number of level-raising primes), not a route around the open problem. Equivalent ≠ circular. This is consistent with the record's "any success needs new input" (RESULT_RANK2_ANCHOR §3).

## 2.3 Kill test, clause by clause (fixed in advance; RESUME.md)

**(i) "Thm 5.17's identification or the multiplicity-one/freeness input exists only after choosing p (no integral version in the sources)": FIRES as worded.**
- Thm 5.17 is stated and proved for Ta_p, through [BoLeRi] mod p, Nakayama over Z/pⁿ and the GL₂(F_p) image (pp. 61–62).
- Freeness is a completion at m_f (Thm 5.15 hyp. 2, p. 58). Multiplicity one enters mod pⁿ (§8, p. 69). The Ihara step is mod p plus Nakayama (Prop 9.2, p. 73).
- H06 is local by definition (p. 3).
- Neither source states an integral version.

**(ii) "BD's remark shows the unit ambiguity is intrinsic": does NOT fire.**
- The remark attributes the ambiguity to two normalizations (the identification H¹_sing ≅ Λ/pⁿ, and L_f). It does not attribute it to lost information.
- D1–D4 dispose of each source of ambiguity:

| Source | Disposed of by |
|---|---|
| N1 (f up to Z_p^×) | ±1 over Z |
| N2 (G_∞) | trivial at the bottom layer |
| N3 and N5 (abstract isomorphisms with Z/pⁿ) | replaced by ρ_f and the canonical modules |
| N4 (the Thm 5.17 unit u) | cancels in C(ℓ₁,ℓ₂) |

**Verdict: `INTEGRAL_LAW_NOT_AVAILABLE_IN_BD`**, scoped to BD05 and H06, triggered by clause (i).
- **Sub-finding (DERIVED, unreviewed): `UNIT_AMBIGUITY_NOT_INTRINSIC`.** A unit-free, p-free, Ш-free depth-2 invariant C(ℓ₁,ℓ₂) exists.
- So the stop is a stop on what the sources contain, not an impossibility. Step 3 was **not run**, per the rule.
