# The fixed 1-motive M_E = [ℤ² → E], u(e_i) = P_i: receiver, Selmer complex, determinant line (2026-10-07)

**STATUS: `NO_CANONICAL_GENERATOR`**

What this status covers, at the three levels the task keeps separate:
- (i) **The determinant module exists.** It is det of Nekovář's Selmer complex of T_pM_E. For p outside an explicit finite set B it is computed in §4 (one Greenberg choice, ordinary p) and §3.3 (relaxed choice, every good p ∉ B).
- (ii) **A canonical p-adic generator intrinsic to M_E: not proved to exist.** The only element M_E supplies on its own is the rational trivialization ϑ_p of §4.4. It exists only when Ш[p^∞] is finite and a p-adic regulator is nonzero. It is the tautological torsion Euler characteristic, and it is a generator only when Ш[p] = 0 and p ∤ Reg_p. Every other candidate is a generator of E's own determinant line (§5).
- (iii) **A cross-p integral generator.** Not attempted: the run stops at step 5, as the task requires.

Labels: **PROVED** means proved here, either in Lean or in the written argument, from the inputs listed. **IMPORTED** means taken from the stated source. **HEURISTIC** means not proved.

Lean file: `RequestProject/OneMotive/Skeleton.lean`. It builds with no `sorry`. The `#print axioms` output is in §7.

---

## 0. Two corrections to the task files

1. **Relation to G2 (PROVED, definitional).** The torus quotient of G2's 𝓜 = [ℤ² → G₁ ×_E G₂] is not M_E itself. It is M₁₆ = [ℤ² → E] with e_i ↦ Q_i = 16P_i (`1_PROVED_STATE/G2/G2_PROOF.md` §3).
   - Multiplication by 16 on ℤ² gives an isogeny M₁₆ → M_E of 2-power degree.
   - So T_pM₁₆ = T_pM_E for every odd p, and nothing below changes.
2. **PRE-CHECK (f) is wrong once the local conditions are those the framework allows (PROVED from IMPORTED inputs, §4).**
   - The Nekovář / Macias Castillo–Sano (MCS) Selmer structures are unramified at every v ∉ S. On the lattice quotient ℤ_p² they therefore admit the cyclotomic ℤ_p-direction.
   - The Mordell–Weil plane that M_E removes globally comes back as the cyclotomic p-adic height matrix of P₁, P₂.
   - Rationally, H¹_F(ℚ, V_pM_E) ≅ V_pШ ⊕ ker(h_p), not V_pШ.
   - So the Selmer complex is acyclic iff Ш[p^∞] is finite **and** Reg_p(P₁,P₂) ≠ 0.
   - (f)'s first bullet survives and is upgraded to PROVED: the extension classes affect only the trivialization, not the line (§4.2).

---

## 1. Step 1: the fixed receiver. PROVED, without FIN, for every odd p

**Definition.**
- M = M_E = [ℤ² → E], placed in degrees −1 and 0.
- M[n] := H⁻¹(M ⊗^L ℤ/n). It sits in 0 → E[n] → M[n] → (ℤ/n)² → 0, and M ⊗^L ℤ/n ≃ M[n][1].
- Sel(ℚ, M)(n) := ker( H¹(ℚ, M[n]) → ∏_v H¹(ℚ_v, M) ).
- Ш¹(ℚ, M) := ker( H¹(ℚ, M) → ∏_v H¹(ℚ_v, M) ), with v running over all places, ∞ included.

This is the Harari–Szamuely / Jossen Selmer group. The local condition at v is the image of H⁰(ℚ_v, M)/n = (E(ℚ_v)/⟨P₁,P₂⟩)/n (IMPORTED for the agreement of the definitions; the proof below uses only the definition displayed above).

**(a) H⁰ (PROVED).**
- Use the triangle E → M → ℤ²[1].
- H¹(F, ℤ) = Hom_cont(G_F, ℤ) = 0 for F = ℚ and for every ℚ_v. For v real, Hom(ℤ/2, ℤ) = 0.
- Hence H⁰(F, M) = coker(u: ℤ² → E(F)) and H⁻¹(F, M) = ker u.
- Globally:
  - H⁰(ℚ, M) = E(ℚ)/⟨P₁,P₂⟩ ≅ E(ℚ)_tors ≅ ℤ/2;
  - H⁻¹(ℚ, M) = 0, since P₁ and P₂ are independent.
- Consequences:
  - H⁰(ℚ,M)/p = 0 for odd p (Lean `two_torsion_div_odd`);
  - H⁰(ℚ, M[p^n]) = 0, using H⁻¹(M)/p^n → H⁰(M[p^n]) → H⁰(M)[p^n] with both ends 0.

**(b) The Selmer sequence (PROVED).**
- The triangle M →^n M → M ⊗^L ℤ/n gives 0 → H⁰(M)/n → H¹(M[n]) → H¹(M)[n] → 0.
- Sel(n) is the preimage of Ш¹[n], so 0 → H⁰(ℚ,M)/n → Sel(ℚ,M)(n) → Ш¹(ℚ,M)[n] → 0 holds by definition.
- With H⁰/p = 0 this gives Sel ≅ Ш¹[p] (Lean `sel_equiv_sha_of_H0_trivial`).

**(c) Ш¹(ℚ, M_E) ≅ Ш(E/ℚ) (PROVED).**
- H¹(F, ℤ²) = 0, so H¹(F,E) ↪ H¹(F,M), with the next term H²(F, ℤ²), for F = ℚ and for every ℚ_v.
- The obstruction lies in Ш²(ℚ, ℤ)².
- Ш²(ℚ, ℤ) = Ш¹(ℚ, ℚ/ℤ), because H^{≥1}(−, ℚ) = 0.
- A character of G_ℚ that is trivial on every decomposition group is everywhere unramified, hence trivial by Minkowski. (Chebotarev also works.)
- The diagram chase is Lean `sha_equiv_of_sha2_trivial`.

**Theorem 1.** Sel(ℚ, M_E)(p) ≅ Ш(E/ℚ)[p] for every odd p. More generally, Sel(ℚ, M_E)(n) ≅ Ш(E/ℚ)[n] for every odd n.

**Care needed?**
- ∞: none, since H¹(ℝ, M[p]) = 0 for odd p.
- p = 3: none. Sel(ℚ, M_E)(3) ≅ Ш[3] ≅ (ℤ/3)², using the record value Ш[3^∞] ≅ (ℤ/3)², whose 3-torsion is all of it.
- Bad primes: none. The argument is uniform in v.
- No Tamagawa, Manin-constant or FIN input is used.

**Relation to the record receiver.**
- B_p ≅ Ш[p] (p ≥ 5) is defined through L_p = ℚ(E[p], p⁻¹E(ℚ)), which is exactly ℚ(M_E[p]).
- Theorem 1 states the same identification with M_E fixed before p is chosen, and it holds for every odd p.
- Its content is the same group Ш[p]. It gives **no bound**.

**Caveat that matters for step 3 (PROVED).** The local condition defining Sel(ℚ, M_E) is strict on the lattice quotient at every place.
- It is **not** a Mazur–Rubin / Nekovář Selmer structure, because it is not unramified at almost all v.
- At every v that splits completely in ℚ(M_E[p]) (infinitely many, by Chebotarev):
  - #H¹_ur(ℚ_v, M_E[p]) = p⁴;
  - the condition (E(ℚ_v)/(p, P₁, P₂)) has order at most p².

## 2. Step 2: Burns–Sakamoto–Sano and Sakamoto do not apply. PROVED, recorded, not pursued

Both theories need two things, and T = T_pM_E fails both:
- **Residual irreducibility of T̄.** M_E[p] ⊃ E[p], with trivial quotient 𝔽_p², so it is reducible.
- **Some τ with T/(1−τ)T free of rank one.** G_ℚ acts trivially on the lattice quotient ℤ_p², so T/(1−τ)T ↠ ℤ_p² for every τ, and it is never free of rank one (Lean `not_coinvariants_rank_one`).

Related fact (PROVED, Lean `two_le_finrank_ker_sub_one`):
- For q ≡ 1 (mod p) unramified, H¹_{/f}(ℚ_q, M_E[p]) = M_E[p]^{Frob_q} has dimension ≥ 2.
- So the classical Kolyvagin primes (q ≡ 1 mod p^n with rank-one singular quotient) do not exist for T_pM_E.

## 3. Step 3: the Macias Castillo–Sano framework on T_pM_E

**Source.** arXiv:2603.23978v1, read from the TeX source. Theorem numbers are taken from that source's counters (shared within each section).
- The standing setting: p odd, a Greenberg datum T_v^+ ⊂ T at v | p with T_v^± free, and T^{I_v} free for v ∈ S_f \ S_p.
- **Hyp 2.11 ("hyp tech"):**
  - (i) H⁰(K, V/T) = H⁰(K, T^∨(1)) = 0;
  - (ii) H⁰(K_v, T_v^-) = 0;
  - (iii) H⁰(K_v, (T_v^+)^∨(1)) = 0;
  - (iv) H¹_ur = H¹_f at finite v ∤ p.
- **Hyp 2.17 ("hyp core"):** there is a core vertex with χ(F) = χ(𝔉), where χ(𝔉) = rk H⁰(ℝ, T^*(1)) − rk T_p^-.
- **Thm 2.20 (Selmer complex ≃ Poitou–Tate complex)** needs Hyp 2.11 and Hyp 2.17.
- **Thm 3.4 (det ≅ SS_{χ(𝔉)})** additionally needs a core vertex inside 𝒩(𝒫), where 𝒫 = {q : H¹_{/F}(ℚ_q, A_n) ≅ ℤ/p^n}. Stark systems SS_r are defined only for r ≥ 0 (Def 3.2).
- MCS have **no τ or irreducibility hypothesis**. In its place they assume a core vertex exists. This answers PRE-CHECK (e): the obstruction of §2 reappears only through Hyp 2.17.

### 3.1 Hypotheses checked (PROVED unless marked)

**The excluded set B.** B consists of:
- p = 2;
- p | N;
- the p dividing #E(ℚ_ℓ)/E₁(ℚ_ℓ) for some ℓ | N (finite and explicit; not computed: no per-prime work);
- anomalous p. There are none among good p ≥ 7, because a_p is even and |a_p| ≤ 2√p.

**(i), for every odd p.**
- H⁰(ℚ, M_E[p^∞]) = 0 by §1(a).
- H⁰(ℚ, T^∨(1)) = H⁰(ℚ, G[p^∞]) = 0. Here G is the extension of E by 𝔾_m² attached to P₁, P₂ (the Cartier dual), and μ_{p^∞}(ℚ) = 0 = E(ℚ)[p].

**(iv), for p ∉ B.**
- H¹(ℚ_ℓ, T_pE) = 0 for ℓ | N.
- So T|_{G_{ℚ_ℓ}} ≅ T_pE ⊕ ℤ_p², and both summands satisfy (iv).

**At v = p.** H⁰(ℚ_p, T_pM_E) has rank ≥ 1. It is the local Kummer line L = {(a,b) : a·log P₁ + b·log P₂ = 0}, because E(ℚ_p) ⊗ ℤ_p has rank 1. Possible Greenberg choices:

| T_p^+ | (ii) | (iii) | χ(𝔉) | Notes |
|---|---|---|---|---|
| 0, T_pÊ, T_pE, T_pE ⊕ L | **fails** (a trivial quotient survives) | – | – | |
| L (the p-dependent local Kummer line) | holds | holds | **−2** | Thm 3.4 is meaningless: SS_{−2} is undefined. Also no core vertex lies in 𝒩(𝒫): see below. |
| T′ = preimage of the ℤ_p² summand of T/T_pÊ ≅ T_pẼ ⊕ ℤ_p² (ordinary, non-anomalous p) | holds | holds | **0** | the natural ordinary choice; used in §4 |
| T (relaxed at p; every good p ∉ B, supersingular p included) | holds | holds | **1** | the Kato / relaxed setting |

Why no core vertex lies in 𝒩(𝒫) for T_p^+ = L:
- 𝒫 ⊂ {q ≢ 1 (mod p)} by §2.
- At such q the class [p] ⊗ w ∈ H¹(ℚ, μ_{p^n}) ⊗ w is locally trivial, where w is a nonzero character of ℤ_p²/L̄.
- That class satisfies every dual local condition, so it survives in H¹_{(F^𝔫)*} for every 𝔫 ∈ 𝒩(𝒫).

**Hyp 2.17 for T′ and for T: NOT verified, and not refuted.** The standard existence proofs of core vertices (Mazur–Rubin, BSS) use exactly the hypotheses that fail in §2. As a result:
- Thm 2.20 and Thm 3.4 are **not established** for T_pM_E.
- Level (i) does not depend on them. Nekovář's complex is perfect (MCS Prop 2.4, from Nekovář Prop 9.7.2), and its determinant is what §4 computes.
- The step-5 verdict does not depend on them either. Thm 3.4 is an isomorphism of free rank-one modules, so it transports canonical elements in both directions and cannot create one.

### 3.2 The Cartier dual and G2's 𝓜

**Cartier dual T_pG = Hom(T_pM_E, ℤ_p(1)) (PROVED).**
- It is worse on step 1. Sel(ℚ, [0 → G])(p) ⊇ G(ℚ)/p ⊇ (ℚ^×/p)², which is infinite.
- It is no better on the determinant. By Nekovář duality (IMPORTED, Nekovář Prop 9.7.2(i), as used in MCS Lemma 2.14):
  - RΓ_{F*}(T_pG) ≅ RHom(RΓ_F(T_pM_E), ℤ_p)[−3];
  - so the determinant lines are mutually inverse, χ is the same (0 for the dual of T′), and canonical elements correspond.

**G2's 𝓜.**
- Hyp 2.11(i) holds (PROVED, by the same argument as §1(a); G(ℚ)[p] = 0).
- The extra pieces are the Tate factors ℤ_p(1)², whose determinant lines are trivialized by explicit p-units and invariant maps.
- The biextension data (the tame and height pairings) again enter only the trivialization.
- So 𝓜 does no better on step 5. This is HEURISTIC: the Greenberg choices for T_p𝓜 were not classified.
- This agrees with the K-list verdict "1-motive alone: regulator side only".

### 3.3 The relaxed choice T_p^+ = T (χ = 1)

- χ = 1 makes rk H¹ − rk H² = 1, so the complex is never acyclic.
- There is no canonical rational trivialization.
- The only known basis comes from the rank-one Kato zeta element of E's relaxed complex, which is an Euler system and is excluded.

## 4. Step 4: the determinant line for T_p^+ = T′ (ordinary p ∉ B). PROVED from IMPORTED inputs

**4.1 The triangle.** The local conditions are compatible with 0 → T_pE → T_pM_E → ℤ_p² → 0:
- the sub gets T_pÊ, the ordinary condition for E;
- the quotient gets the relaxed condition at p;
- both get the unramified condition at ℓ ∈ S \ {p}, where everything splits for p ∉ B.

This gives an exact triangle RΓ_ord(T_pE) → RΓ_F(T_pM_E) → RΓ_rel(ℤ_p)² (IMPORTED: Nekovář, *Selmer complexes*, functoriality of Selmer complexes for exact sequences compatible with the local conditions).

The two outer complexes:
- **RΓ_rel(ℤ_p) = RΓ(G_{ℚ,{p,∞}}, ℤ_p).**
  - H⁰ = ℤ_p, with basis 1.
  - H¹ = Hom(G_{ℚ,{p}}, ℤ_p) = ℤ_p·χ₀, with χ₀ = log_p∘χ_cyc / p.
  - H² = 0: the Euler characteristic gives h² = h¹ − 1 = 0 mod p.
- **RΓ_ord(T_pE).** Ordinary = Bloch–Kato integrally at non-anomalous p (IMPORTED: Greenberg).
  - H¹ = H¹_f(ℚ, T_pE), with 0 → E(ℚ) ⊗ ℤ_p → H¹ → T_pШ → 0.
  - H² ≅ Sel_{p^∞}(E)^∨ (MCS Lemma 2.14(ii)).

**4.2 The line (PROVED).** The Knudsen–Mumford determinant is multiplicative on exact triangles (IMPORTED). So

det⁻¹ RΓ_F(T_pM_E) ≅ det⁻¹ RΓ_ord(T_pE) ⊗ (det⁻¹ RΓ_rel(ℤ_p))^{⊗2} ≅ det⁻¹ RΓ_ord(T_pE),

where the last isomorphism uses the canonical bases (1, χ₀). P₁ and P₂ do not change the line.

**4.3 Cohomology (PROVED).** The connecting maps are:
- δ⁰: ℤ_p² → H¹_ord(T_pE), the Kummer map of P₁, P₂. It is an isomorphism onto E(ℚ) ⊗ ℤ_p (saturated basis, p odd).
- δ¹: ℤ_p²·χ₀ → H²_ord(T_pE) ≅ Sel_{p^∞}^∨, given by δ¹(χ₀ ⊗ e_i) = ±χ₀ ∪ κ(P_i).

Paired against κ(P_j), δ¹ is Nekovář's cyclotomic height (IMPORTED: Nekovář, *Selmer complexes*, Ch. 11, where the Bockstein equals the cup product with the character). Its comparison with the Mazur–Tate / Schneider height is IMPORTED (same chapter; theorem numbers not re-verified here).

Define Reg_p^int := det(⟨δ¹(χ₀ ⊗ e_i), κ(P_j)⟩) ∈ ℤ_p. It is intrinsic to M_E, up to sign, and equals Reg_p(P₁,P₂)/p² up to a unit (IMPORTED normalization). Then:
- H⁰ = H³ = 0;
- 0 → T_pШ → H¹_F → ker δ¹ → 0;
- H²_F = coker δ¹.

**4.4 Acyclicity and the torsion count (PROVED).**
- RΓ_F(V_pM_E) is acyclic ⟺ Ш[p^∞] is finite **and** Reg_p^int ≠ 0. The second condition is Schneider's non-degeneracy at p, which is open.
- In that case:
  - H¹_F(T) = 0 (it is free by MCS Lemma 2.15, and rationally zero);
  - #H²_F(T) = #Ш(E)[p^∞] · |Reg_p^int|_p⁻¹, since coker of ℤ_p² → ℤ_p² ⊕ Ш^∨ has order #Ш · |det|⁻¹;
  - the canonical rational trivialization gives ϑ_p, with ord_p ϑ_p = ord_p #Ш[p^∞] + ord_p Reg_p^int.
- This is the algebraic side of the Mazur–Tate–Teitelbaum p-adic BSD formula. Tamagawa, torsion and (1 − 1/α) are p-units here.

**4.5 Mod p (PROVED).**
- In the acyclic case, H¹(RΓ_F ⊗ 𝔽_p) ≅ H²_F[p] (MCS Lemma 2.15). It is nonzero ⟺ Ш[p] ≠ 0 **or** p | Reg_p^int.
- So the MCS-admissible receiver is not the step-1 receiver. The two differ exactly at primes with p | Reg_p^int. The fixed-local-condition carrier lemma (`2_CLOSED_LANES/RECEIVER_FIXED_LOCAL_CARRIER.md`) reappears as the height matrix.

## 5. Step 5: is there a canonical element? None is proved. Stop

**PROVED:**
- **The line is E's line.** By §4.2, and the same argument for every compatible Greenberg choice, a canonical generator of det RΓ_F(T_pM_E) is the same thing as a canonical generator of det RΓ(T_pE) with the induced condition. That condition is strict, ordinary or relaxed at p. The Tate factors carry canonical bases: 1, χ₀, and the valuation character in the strict case.
- **The only datum intrinsic to M_E is ϑ_p of §4.4.**
  - Its existence requires FIN at p and Reg_p^int ≠ 0.
  - It is a generator ⟺ Ш[p] = 0 ∧ p ∤ Reg_p^int.
  - Its value is the torsion Euler characteristic, which is tautological (PRE-CHECK (g), first bullet).
- **Every other generator** would be a generator of E's determinant line. The only known ones are Kato's zeta element (BKS), the Heegner basis of MCS Thm 3.9 (an imaginary quadratic K plus the Heegner main conjecture) and the ETNC/BSD normalization. All three are excluded.

**Comparison with s_p (HEURISTIC, under FIN at p and the retained BKS factorization):**
- s_p ≐ x_{ℚ,Σ}·#Ш[p^∞].
- ϑ_p ≐ #Ш[p^∞]·Reg_p^int.
- Both carry #Ш[p^∞]. The other factor of ϑ_p is the **wild** cyclotomic regulator, not the tame R_{p,ℓ}.
- ϑ_p ≐ s_p iff ord_p Reg_p^int = ord_p x_{ℚ,Σ}. This was not tested, since that would be a per-prime computation.
- Neither quantity is Ш-free.

**Step 6:** not entered.

## 6. Summary of labels

| Claim | Label |
|---|---|
| Theorem 1, Sel(ℚ,M_E)(p) ≅ Ш[p] for odd p (PRE-CHECK (a)–(c) verified, no FIN) | PROVED (Lean skeleton plus §1) |
| HS local condition is not unramified almost everywhere | PROVED |
| BSS and Sakamoto inapplicable: reducible, coinvariants ↠ ℤ_p²; no q ≡ 1 Kolyvagin primes | PROVED (Lean) |
| MCS Hyp 2.11 for T′ and T (p ∉ B); list of failing Greenberg choices | PROVED |
| Hyp 2.17 (core vertex) for T′ and T | OPEN (not verified) |
| T_p^+ = L: χ = −2, and no core vertex in 𝒩(𝒫) | PROVED |
| Cartier dual: infinite Selmer, inverse determinant line | PROVED / IMPORTED (duality) |
| 𝓜 does no better | HEURISTIC |
| Determinant line ≅ E's line; extension data only in the trivialization | PROVED from IMPORTED (det multiplicativity, Nekovář triangles) |
| Acyclic ⟺ FIN_p ∧ Reg_p^int ≠ 0; #H² = #Ш[p^∞]·\|Reg_p^int\|⁻¹; mod-p receiver detects Ш[p] or p \| Reg_p^int | PROVED from IMPORTED (Nekovář Ch. 11, Greenberg) |
| No canonical generator intrinsic to M_E | PROVED as stated in §5 (reduction to E plus tautology); existence of one is not excluded, it is unproved |
| ϑ_p versus s_p | HEURISTIC |
| PRE-CHECK (f) | stays HEURISTIC in its original form, and its rational claim is corrected (§0.2) |

## 7. Lean (`RequestProject/OneMotive/Skeleton.lean`, no `sorry`)

| Theorem | Axioms |
|---|---|
| `OneMotive.sel_equiv_sha_of_H0_trivial` | propext, Classical.choice, Quot.sound |
| `OneMotive.sha_equiv_of_sha2_trivial` | propext, Classical.choice, Quot.sound |
| `OneMotive.two_torsion_div_odd` | propext |
| `OneMotive.not_coinvariants_rank_one` | propext, Classical.choice, Quot.sound |
| `OneMotive.two_le_finrank_ker_sub_one` | propext, Classical.choice, Quot.sound |

FIN, ORDER9 and Q36: unchanged.
