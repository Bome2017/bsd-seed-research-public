# Return: degree-two coefficient of the definite Gross-point theta element over K = ℚ(√−7) (delta 2026-10-06)

## STATUS: PRECISE_OBSTRUCTION

**One-line verdict.**
- With the height pairing canonically attached to the theta element's group (the anticyclotomic tame Mazur–Tate pairing), the 2×2 determinant on E(ℚ) = E(K)⁺ is **identically zero** for every odd p. So Θ⁽²⁾ = m_E·det(H) reads 0 = 0, or else is false. This is PROVED, given the standard functoriality of the pairing.
- The only well-typed nonzero substitute is G2's cyclotomic pairing over ℚ(μ_ℓ). It transfers canonically to the degree-two piece for split ℓ (PROVED). But no printed theorem and no distribution relation produces the resulting identity, and every printed or conjectural leading-term formula of this kind carries #Ш (or BSD over subfields) in its constant.
- That identity would imply Ш[p^∞] = 0 at all but finitely many good ordinary p (PROVED bookkeeping, Lean). So it is not a reduction to anything weaker.

**Labels.**
- **PROVED**: proved here, either in the Lean file `RequestProject/DerivedGross/Obstruction.lean` (builds, no `sorry`) or by the short argument given.
- **IMPORTED**: taken from the canonical packet (file named) or from a published source. A theorem number I did not check in this run is marked "(number HEURISTIC)".
- **HEURISTIC**: everything else.

**Scope.** Theoretical only. No Brandt-module or Gross-point computation, no per-prime work, no W3, no Result 002 transplant, no plectic material, and R1–R5 are not redone. Nothing here uses FIN, BSD, #Ш, Selmer lengths, Q36 or q ∈ ℚ as an input.

---

## 1. The object (stop condition 1)

### 1.1 Quaternion algebra, order and Gross points
- **IMPORTED** (delta file, definite-field gate 09-22).
  - N = 2³·3·2243·4547²·5843 splits as N⁺ = 2³·4547² and N⁻ = 3·2243·5843.
  - Every prime of N⁺ splits in K, and every prime of N⁻ is inert in K. #N⁻ = 3 is odd, so ε(E/K) = +1 (definite case).
  - h(−7) = 1 and O_K^× = {±1}, so u_K = 1.
- **The algebra and the order.** B is the definite quaternion algebra over ℚ ramified exactly at {3, 2243, 5843, ∞}. R ⊂ B is an Eichler order of level N⁺ = 2³·4547². Eichler orders of non-squarefree level exist, and N⁺ is coprime to disc B.
  - The Gross set is X = B^×\B̂^×/R̂^×, a finite set of total mass about 5.4·10¹⁴ (IMPORTED from the record).
- **The eigenfunction.** f : X → ℤ is the Jacquet–Langlands transfer of the newform of E. It is normalized to be primitive (gcd of its values is 1), which fixes it up to sign.
  - IMPORTED: multiplicity one for JL transfer at level (N⁺, N⁻) with N⁻ squarefree. Gross 1987, §§3–5; Cai–Shu–Tian, Algebra & Number Theory 8 (2014), §1 (number HEURISTIC).
- **Gross points.**
  - Let O_c = ℤ + c·O_K be the order of conductor c, for c coprime to N.
  - A Gross point of conductor c is a class [b] ∈ X such that b̂R̂b̂⁻¹ ∩ B ⊇ an optimal image of O_c. The orientation at N⁺ is fixed by choosing the ideal 𝔑⁺ with O_K/𝔑⁺ ≅ ℤ/N⁺. This is possible because 2 and 4547 split.
  - x₁ is the (unique, since h = 1) Gross point of conductor 1. Since Pic(O_K) = 1, X contains exactly one conductor-1 point up to the orientation choice.

### 1.2 Characters, group ring, theta element, augmentation ideal
- **Auxiliary conductor.** Fix a prime ℓ ∤ 7N.
- **The group.** G_ℓ := Pic(O_ℓ) = Gal(K[ℓ]/K[1]) = Gal(K[ℓ]/K).
  - G_ℓ ≅ (O_K⊗ℤ/ℓ)^×/(ℤ/ℓ)^×, which is cyclic of order ℓ − (−7/ℓ) (IMPORTED: class number formula for orders, with h = u = 1).
  - Complex conjugation τ acts on G_ℓ by g ↦ g⁻¹, since K[ℓ]/ℚ is dihedral.
- **The theta element.** Let x_ℓ be a Gross point of conductor ℓ lying above x₁ (compatible orientation). Then
  - θ_ℓ := Σ_{σ∈G_ℓ} f(x_ℓ^σ)·σ ∈ ℤ[G_ℓ].
  - θ_ℓ* denotes the image of θ_ℓ under σ ↦ σ⁻¹.
- **The characters.** χ ranges over the characters of G_ℓ, i.e. the ring class characters of conductor dividing ℓ. For p-adic work only the characters of p-power order matter, i.e. the group ring ℤ_p[G_ℓ] ↠ ℤ_p[G_ℓ ⊗ ℤ_p].
- **The augmentation ideal.** I = ker(ℤ[G_ℓ] → ℤ, σ ↦ 1). Lean: `DerivedGross.augIdeal` (any commutative ring R and commutative group G).
  - For cyclic G, I/I² ≅ G. After ⊗ℤ_p, every I^k/I^{k+1} is a quotient of the cyclic group (G⊗ℤ_p)^{⊗k}. (HEURISTIC that it is exactly this group. Only the surjection is used below.)
  - Only primes p | #G_ℓ give anything. If p ∤ #G_ℓ then Iℤ_p[G_ℓ] = I²ℤ_p[G_ℓ].
- **Interpolation.** For χ primitive of conductor ℓ:
  - χ(θ_ℓ)·χ̄(θ_ℓ) = χ(θ_ℓθ_ℓ*) = κ_χ · L(E/K, χ, 1)/Ω_{E,N⁻}, with κ_χ an explicit nonzero constant.
  - At χ = 1 the same holds for θ₁ = f(x₁): κ₁·θ₁² = L(E/K,1)/Ω = L(E,1)·L(E^{−7},1)/Ω.
  - IMPORTED: Gross 1987 (prime level), Zhang 2001, Cai–Shu–Tian 2014, explicit Waldspurger formula (number HEURISTIC). This is the level-(N⁺,N⁻) generalization, with N⁺ split and not necessarily squarefree.
  - The Bertolini–Longo–Venerucci anticyclotomic main conjecture is stated for the p-adic limit of these θ (IMPORTED, delta file). Their Remark 1.4 exception (trivial character, exceptional case) is exactly our χ = 1.

### 1.3 Which element starts in I²/I³, and why
1. **θ₁ = 0.** PROVED, given IMPORTED inputs. Lean: `augmentation_vanishes`.
   - κ₁·θ₁² = L(E,1)·L(E^{−7},1), with κ₁ ≠ 0, and L(E,1) = 0 (IMPORTED: analytic rank 2). So θ₁ = 0.
2. **θ_ℓ ∈ I.** PROVED, given the distribution relation.
   - The distribution relation (IMPORTED: Bertolini–Darmon, Ann. of Math. 162 (2005), §2; number HEURISTIC) comes from the ℓ+1 neighbours of x₁ under T_ℓ:
     - if ℓ splits as λλ̄: aug(θ_ℓ) = Σ_σ f(x_ℓ^σ) = (a_ℓ − 2)·θ₁, because two neighbours (x₁^{λ}, x₁^{λ̄}, both equal to x₁ since h = 1) have conductor 1 and ℓ−1 have conductor ℓ;
     - if ℓ is inert: aug(θ_ℓ) = a_ℓ·θ₁.
   - Either way aug(θ_ℓ) = 0.
3. **θ_ℓ ∈ I²** after ⊗ℤ_p, for odd p. PROVED in Lean (`mem_augIdeal_sq_of_functional_eq`), given the functional equation θ_ℓ* = ε·σ_ℓ·θ_ℓ with σ_ℓ ∈ G_ℓ and ε = +1.
   - Lean statement: in R[G] with 2 ∈ R^×, θ ∈ I and θ* = σθ imply θ ∈ I².
   - Proof: g + g⁻¹ − 2 = −(g−1)(g⁻¹−1) ∈ I², so θ + θ* ∈ I². Also (σ−1)θ ∈ I². Hence 2θ ∈ I².
   - The sign ε = +1 here is HEURISTIC as to exact form. The functional equation itself is IMPORTED (Bertolini–Darmon 2005, §2.2; number HEURISTIC). The sign matches the expected parity: the order of θ is max(r⁺, r⁻) = 2.
4. **Answer to the "which element" question.** The element whose first possibly nonzero coefficient lies in I²/I³ is θ_ℓ itself; call that coefficient Θ⁽²⁾_ℓ.
   - θ_ℓθ_ℓ* ∈ I⁴, so its I²/I³ coefficient is 0 (PROVED: product of two elements of I²).
   - Its first possible coefficient is (Θ⁽²⁾)² ∈ I⁴/I⁵, since * acts by (−1)² = +1 on degree two.
   - This is the object the record's detector M₂(p) reads (IMPORTED, record B.3).

### 1.4 The height pairings (specified)
- **(H^ac) Anticyclotomic tame Mazur–Tate pairing.** ⟨ , ⟩_ℓ^{ac} : E(K) × E(K) → G_ℓ ⊗ ℤ_p.
  - This is the canonical pairing for the extension K[ℓ]/K, built from Mazur–Tate local symbols (IMPORTED: Mazur–Tate, "Canonical height pairings via biextensions", 1983; number HEURISTIC). It is the pairing paired with θ_ℓ in every refined conjecture of Darmon / Bertolini–Darmon type.
  - Normalization: values in G_ℓ⊗ℤ_p through the Artin map, with no extra constant.
- **(H^cyc) Cyclotomic tame pairing.** ⟨ , ⟩_ℓ^{cyc} : E(ℚ) × E(ℚ) → Gal(ℚ(μ_ℓ)/ℚ) ⊗ ℤ_p ≅ F_ℓ^× ⊗ ℤ_p.
  - This is G2's pairing, with the record's normalization (`CURRENT_FRONTIER.md` §1.7: g = least primitive root, b₁₂ = (h(Q₁+Q₂) − h₁ − h₂)/2, R = det/M⁴). Its determinant is R_{p,ℓ}.

## 2. The degree-two analysis (stop condition 2)

### 2.1 The canonical pairing has zero determinant on E(ℚ)
- **Equivariance** (IMPORTED, Mazur–Tate functoriality under automorphisms of K that extend to K[ℓ]; number HEURISTIC). ⟨τP, τQ⟩^{ac} = τ⟨P,Q⟩^{ac}τ⁻¹ = −⟨P,Q⟩^{ac} in G_ℓ ⊗ ℤ_p. The second equality holds because τ inverts G_ℓ.
- **PROVED** (Lean `pairing_vanishes_on_fixed`, `gram_det_eq_zero_of_anti`). If 2 is invertible, an anti-invariant pairing vanishes on τ-fixed vectors. E(ℚ) = E(K)⁺ is τ-fixed, so ⟨P_i, P_j⟩^{ac} = 0 for i, j ∈ {1, 2} and det(H^{ac}(P_i, P_j)) = 0 for every odd p and every ℓ.
- **Consequence** (PROVED, Lean `degenerate_identity_forces_zero`). An identity Θ⁽²⁾_ℓ = m_E·det(H^{ac}) forces Θ⁽²⁾_ℓ = 0 at every level. Then:
  - either it is 0 = 0 and the definite detector M₂ never fires;
  - or a single nonzero Θ⁽²⁾ refutes it.
  - In either case it gives nothing for the endpoint.
- **Reading** (HEURISTIC, consistent with Bertolini–Darmon derived heights). The first-order anticyclotomic height on E(K)⁺ × E(K)⁺ vanishes, so the leading term of θ is governed by a **second derived** anticyclotomic height h⁽²⁾ with values in I²/I³. The conjectural leading-term shape is (Θ⁽²⁾)² ≐ c_{E/K}·det(h⁽²⁾(P_i,P_j)) in I⁴/I⁵. This is a formula for θθ*, not for Θ⁽²⁾, and with a regulator that is not a determinant of a first-order pairing.

### 2.2 The cyclotomic substitute: well typed, but no identity
- **PROVED** (Lean `sq_tmul_sign_invariant`, plus class field theory as follows). For ℓ = λλ̄ split, the ray class group mod ℓ of K is (F_ℓ^× × F_ℓ^×)/±1.
  - Its τ-invariant quotient (a, b) ↦ ab is Gal(K(μ_ℓ)/K) ≅ Gal(ℚ(μ_ℓ)/ℚ).
  - Its τ-anti-invariant quotient (a, b) ↦ a/b is G_ℓ.
  - The map a ↦ (a, 1) identifies both quotients with F_ℓ^×. Swapping λ and λ̄ changes this identification by a ↦ a⁻¹ on G_ℓ.
  - So (G_ℓ⊗ℤ_p)^{⊗2} ≅ (Gal(ℚ(μ_ℓ)/ℚ)⊗ℤ_p)^{⊗2} canonically, because (−a)⊗(−a) = a⊗a.
  - Hence det(H^{cyc}) ∈ (Gal(ℚ(μ_ℓ)/ℚ)⊗ℤ_p)^{⊗2} lands canonically in the target of Θ⁽²⁾_ℓ.
  - For inert ℓ there is no such identification at p ∤ ℓ−1, since #G_ℓ = ℓ+1.
- **The candidate identity, stated at every level with one constant:**

  (CAND) for all split ℓ ∤ 7N and all odd p ∉ S: Θ⁽²⁾_ℓ = m_E·det(⟨P_i,P_j⟩_ℓ^{cyc}) in I²/I³ ⊗ ℤ_p, with m_E ∈ ℚ^× fixed. (A variant has an extra Euler factor (a_ℓ − 2); the analysis below is unchanged.)

- **First failing arrow: the derivation.** Steps 1–3 of §1.3 use every distribution relation available: the trace relation for Gal(K[ℓ]/K[1]) and the functional equation.
  - They determine aug(θ_ℓ) and the degree-one part. They say nothing about Θ⁽²⁾, because the trace relation sees only aug, and the functional equation constrains only the parity of the leading degree.
  - The interpolation formula sees Θ⁽²⁾ only through L-values L(E/K,χ,1) with χ ≠ 1. These have no Mordell–Weil side (record R4).
  - No printed theorem expresses the I²-coefficient of a definite theta element through a height pairing on E(K)⁺:
    - Bertolini–Darmon (Duke 1994, Amer. J. Math. 1995; derived heights) give conjectures, and proved results only in other directions (number HEURISTIC).
    - Tan (Ann. Inst. Fourier 1995) assumes BSD over intermediate fields and gives the constant only up to F_p^× (IMPORTED, `ADMISSION.md`).
    - BLV (Math. Ann. 2026) exclude this exact case, Remark 1.4 (IMPORTED, delta file).
  - A proof of (CAND) would also have to compare a second derived anticyclotomic height on E(K)⁺ with the first-order cyclotomic height. No such comparison exists in print, and the record has no mechanism for it (U22's missing map is the same comparison; IMPORTED, delta file).
- **The constant** (stop condition 3, HEURISTIC).
  - Every printed or conjectural leading-term formula of this type (Mazur–Tate refined conjecture; Darmon; Bertolini–Darmon; Tan) normalizes the leading coefficient by #Ш(E/K)·Tam/tors² (or its square root for θ), or assumes BSD.
  - The only Ш-free alternative is analytic: the BSD quotient of E/K, which is q times the rational number L(E^{−7},1)/Ω_{E^{−7}}. That is Q36-type data.
  - Both are excluded constants. So if (CAND) were taken from the existing literature or conjectures, the return would be CIRCULAR_CONSTANT.
  - The status is not CIRCULAR_CONSTANT because no proved identity exists whose constant could be inspected. The obstruction is reached earlier, at the derivation (and, for the canonical pairing, at §2.1).
- **Strength of (CAND)** (PROVED, Lean `ordinary_bad_primes_finite_of_identity`). Assume:
  - (CAND), with m_E = a/b;
  - G2 (IMPORTED: for p ∉ S₀ there are auxiliary ℓ with R_{p,ℓ} ≢ 0; these ℓ ≡ 1 + p mod p² have to be split in K for (CAND) to apply, which is an extra Chebotarev condition, HEURISTIC that it is compatible);
  - the definite detector (IMPORTED, record B.3, conditional, good ordinary p only).

  Then {good ordinary p : Ш[p^∞] ≠ 0} ⊆ S ∪ {p | a}, which is finite.
  - So (CAND) is at least as strong as the ordinary part of FIN-tail. It does not cover supersingular p, where the detector does not apply.
  - It is therefore not a reduction to a weaker new theorem, which is why the status is not REDUCTION_TO_ONE_NEW_THEOREM.
- **Calibration** (HEURISTIC). Under BSD for E/K, a correct m_E in (CAND) would have to vanish mod every p ∈ Supp Ш(E/K) ⊇ Supp Ш(E/ℚ) at which det^{cyc} is a unit (e.g. p = 3 against the record's Ш[3^∞] ≅ (ℤ/3)²).
  - So any correct m_E is forced to encode Ш(E/K), as in the record's calibration K_E = 4c∞·Tam·#Ш/tors².
  - A Ш-free definition of it is exactly the missing rank-two identity.

## 3. The obstruction, precisely
1. **PROVED.** For the canonical pairing of the theta element's group, det(H^{ac}) ≡ 0 on E(ℚ) for every odd p. Θ⁽²⁾ = m_E·det(H^{ac}) is therefore degenerate (§2.1).
2. **PROVED.** The only nonzero first-order determinant in the right degree is G2's cyclotomic one, transferred through the canonical isomorphism of degree-two pieces at split ℓ (§2.2).
3. **First missing arrow.** A theorem computing Θ⁽²⁾_ℓ from E(K)⁺ = E(ℚ). Equivalently, a comparison of the second derived anticyclotomic height with the first-order cyclotomic height, with a constant fixed at every level. Distribution relations stop at degree one; the printed interpolation formula has no Mordell–Weil side.
4. **PROVED (bookkeeping).** Such a theorem implies the ordinary part of FIN-tail. HEURISTIC: every known normalization of its constant involves #Ш(E/K) or the BSD quotient.

**What would change the verdict.** A proved formula Θ⁽²⁾_ℓ ≡ m_E·det(⟨P_i,P_j⟩_ℓ^{cyc}) for split ℓ (or (Θ⁽²⁾)² ≡ m_E′·det h⁽²⁾ together with a proved comparison h⁽²⁾ ↔ (h^{cyc})^{⊗2}), with m_E defined by a formula involving neither #Ш nor L-value quotients.

## 4. Lean

- **File and build.** `RequestProject/DerivedGross/Obstruction.lean`. It builds with `lake build RequestProject.DerivedGross.Obstruction` and contains no `sorry` and no new axioms.
- **Inputs.** Every arithmetic input is an explicit hypothesis. No statement in the file concerns Ш of the seed.

```
'DerivedGross.mem_augIdeal_sq_of_functional_eq' depends on axioms: [propext, Classical.choice, Quot.sound]
'DerivedGross.add_invol_sub_mem_sq' depends on axioms: [propext, Classical.choice, Quot.sound]
'DerivedGross.pairing_vanishes_on_fixed' depends on axioms: [propext, Quot.sound]
'DerivedGross.gram_det_eq_zero_of_anti' depends on axioms: [propext, Classical.choice, Quot.sound]
'DerivedGross.sq_tmul_sign_invariant' depends on axioms: [propext, Quot.sound]
'DerivedGross.augmentation_vanishes' depends on axioms: [propext, Classical.choice, Quot.sound]
'DerivedGross.degenerate_identity_forces_zero' does not depend on any axioms
'DerivedGross.ordinary_bad_primes_finite_of_identity' depends on axioms: [propext, Classical.choice, Quot.sound]
```

FIN, ORDER9 and Q36: unchanged.
