# Return: OpenAI rank-two obstruction / determinant machinery against the Mordell–Weil plane (2026-10-07)

**STATUS: EXCESS_OBSTRUCTION_PROVED**

Stage A succeeds. It is a reformulation of the receiver kernel (PRE-CHECK 3 holds, with one correction) and gives no bound on Ш[p]. Stage B stops at its first failure, `GENERIC_RANK1_ONLY` (§3). Stage C was not entered.

Lean: `RequestProject/Continuation/ExcessObstruction.lean`. It builds with no `sorry`; axioms are listed in §6.

Labels: **PROVED** means proved here, from the inputs named on that line. **IMPORTED** means taken from a named source after the audit in §1. **HEURISTIC** means not proved.

Notation: p ∉ B* = {2,3,19,59,487,2243,4547,5843}; Σ = {∞, p, primes dividing N}; G_Σ = Gal(ℚ_Σ/ℚ); S_p = Sel_p(E/ℚ) ⊇ W_p = ⟨κ(P₁),κ(P₂)⟩; S_p⁰ = ker(S_p → E(ℚ_p)/p), the strict space; ℓ_p = W_p ∩ S_p⁰; L_p = ℚ(E[p], p⁻¹E(ℚ)); e is the Weil pairing.

---

## 0. Inputs used from the packet (IMPORTED, not re-derived)

- (R1) The mod-p image is GL₂(𝔽_p) for every odd p (`CURRENT_FRONTIER.md` §0).
- (R2) Saturation of P₁, P₂ and a full Kummer block, Gal(L_p/ℚ(E[p])) ≅ E[p]² (`1_PROVED_STATE/G2/`, "the Kummer block is full, from saturation").
- (R3) For p ∉ B*: E is good at p, and E(ℚ_v)[p] = 0 = E(ℚ_v)/p at every bad v. So H¹(ℚ_v,E[p]) = 0 for v | N (`2_CLOSED_LANES/UNIFORM_STEP_FINDINGS_2026-10-03.md`, Fact 1).
- (R4) Receiver kernel: ker(S_p → H¹(L_p,E[p])) = W_p.
  - PROVED from R1 and R2 by inflation–restriction. H¹(Gal(L_p/ℚ),E[p]) is the extension of Hom_{GL₂}(E[p]², E[p]) ≅ 𝔽_p² by H¹(GL₂(𝔽_p),E[p]) = 0, using Sah's lemma with the central element −I. The 𝔽_p² is spanned by κ(P₁), κ(P₂).
  - This is the kernel statement behind `1_PROVED_STATE/receiver/`; the receiver is not rebuilt.

## 1. Hostile audit of the named OpenAI statements

Sources, read from the raw LaTeX:
- `preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-3-2026/build/sections/04-vertical.tex` (V)
- `preprints/A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-September-24-2026/build/sections/ring-determinants.tex` (RD)

**Structural finding, applying to all of (V).** The residual tests of (V) live over k_r = Frac(𝔽_p[[**u**]]) at t = 0. The coefficients there are T̄ ⊗ χ, where χ is the universal product of the *artificial* tame characters; there are "at least two moving primes" (`vertical:auxiliary-tuples`(3)).
- Sel_p(E/ℚ) is the special point **u** = 0 (χ = 1). It is never a test space of (V).
- κ(P_i) are classes at χ = 1 and do not lie in the generic strict spaces.
- So "the OpenAI machinery sees the excess" can only mean a transport of its first-order mechanism to χ = 1. The table records which hypotheses survive that transport.

| Label | Hypothesis checked at χ = 1 on the seed | Verdict |
|---|---|---|
| `vertical:scalar-localization` | Ш²(G_Σ, μ_p) is dual to the everywhere-unramified, Σ-split 𝔽_p-characters of ℚ, which are 0. | **PASS** (IMPORTED) |
| `vertical:lift-test` | (i) The scalar cup x∪d is locally zero: at p because x is strict; at v ∣ N by R3; at ∞ because p is odd. (ii) Old local complexes are acyclic: by R3, in place of "nonconstant Frobenius scalar". (iii) At the new prime γ, M(γ) − 1 is invertible. (iv) λ vanishes at the old places: every q ∈ Σ is a p-th power mod γ. Its proof is a cochain identity that uses χ ≠ 1 only for (ii). | **PASS after transport** (IMPORTED). z_γ is independent of the cochain choices (§2.1). |
| `vertical:obstruction-span`, eq. (vertical:commutator-change) | The cochain identity: multiplying Frob_γ by [v,w′], with v, w′ fixing E[p], μ_p and the radicals, changes z by −e(x(v),d(w′)) + e(x(w′),d(v)). | **PASS** (IMPORTED, pure cochain calculation) |
| `vertical:obstruction-span`, **statement** | It needs the paired opposite representations to be nonisomorphic ("the rational case … sees χ and χ⁻¹"). At χ = 1, E[p] ≅ Hom(E[p], μ_p) through the Weil pairing. | **FAILS** (PROVED). The commutator changes are then *symmetric* forms (Lean `commChange_symm`, `span_commChange_le`). So the mechanism cannot give the asserted span of all s×(s+a) matrices (`not_mem_span_of_not_symm`, `exists_not_symm`). Replaced in §2 by the diagonal value B(x,x) = −2e(f x, g x), which is enough. |
| `vertical:tests` | (a) The free line uses Euler characteristic −1 (corank one). (b) It kills strict spaces at the *generic* point. At χ = 1 the strict space always contains ℓ_p ≠ 0 (PRE-CHECK 2), so it cannot be killed. | **NOT APPLICABLE** to S_p; not used. |
| `rd:rank-two` (first paragraph) | H is normal and acts trivially on E[p], which is absolutely irreducible by R1. Restriction to H is injective on the classes used (§2.2). | **PASS** (IMPORTED). Used only for: the image of x on H is all of E[p]. |
| `rd:det-switch`, `rd:valuation-switch` | They assume H¹(C_F ⊗ F_O) = F_O·A (generic rank one) and f(A) = v₀ ≠ 0. The unit volume v₀ ∧ x is the whole valuation mechanism. | **FAILS for Δ_W**: a Δ_W-preserving switch forces f|_W = 0 (§3). |
| `rd:away-two` | Generic rank ≤ 1 at characteristic-zero height-one primes of ℤ₂[[t]]. The reduction stops at fiber dimension 1 through the generic rank-one vector. | **FAILS** (rank two; dyadic setting) |
| `rd:outer-bound` | "Every simple-zero ring instance", with a 2-adic outer DVR. | **FAILS** (the seed has a double zero) |

The two-primary paper §12 (conjugate Bockstein alternation) is not used.

## 2. Stage A

### 2.1 Definitions (no complement, no basis of S_p/W_p, no dim Ш[p])

- **Admissible directions.** Adm_p is the set of primes γ ∤ pN with:
  - γ ≡ 1 (mod p);
  - every q ∈ {−1} ∪ {primes dividing pN} a p-th power mod γ;
  - ρ̄(Frob_γ) − 1 invertible on E[p].
  
  For each γ, fix λ_γ, an order-p character of conductor γ. Rescaling λ_γ rescales the row.
- **The direction module.** 𝒟_p is the free 𝔽_p-module on Adm_p × H¹(G_Σ, E[p]).
- **The obstruction map.** For x ∈ S_p⁰, put 𝒪_p(x)([γ, d]) = z_γ(x,d). Here z_γ(x,d) = (u − A∪d)(Frob_γ), where du = x∪d and A = (M(γ)−1)⁻¹x(Frob_γ). This is the `vertical:lift-test` invariant. The strict space is used as the delta prescribes.
  - **Independence of choices (PROVED).** The primitive u is determined up to Kummer classes of Σ-units. These vanish at Frob_γ by the radical condition.
  - Changing x by a coboundary m changes u by m∪d and A by m, which cancel.
  - Changing d by a coboundary n changes the value by −e(σA,σn) + e(A,n) = 0, because σ = Frob_γ fixes μ_p.
- **The restricted direction module.** 𝒟_p^ℓ = {δ : 𝒪_p(y)(δ) = 0 for all y ∈ ℓ_p}. It is intrinsic: ℓ_p is cut out by P₁, P₂ and loc_p.

### 2.2 Theorem A

For every p ∉ B*, including supersingular p:

  **ker(S_p⁰ → Hom(𝒟_p^ℓ, 𝔽_p)) = ℓ_p = W_p ∩ S_p⁰.**

Status: **PROVED**, from R1–R4, the PASS rows of §1, and the Chebotarev density theorem (IMPORTED, classical).

**Universal linear algebra (PROVED, Lean `ker_restrictObs`).** For any obstruction map and any finite-dimensional W:
- ker(S → Hom(𝒟^W)) = W + ker 𝒪.
- Restriction to 𝒟^W never destroys separation, so the fork in the delta resolves *for* restriction.
- (A1) on 𝒟^W holds by definition (`restrictObs_of_mem`).
- Stage A is exactly ker 𝒪 ⊆ W (`ker_restrictObs_eq_iff`, `a2_iff`).

**The fork, tested.** On the full 𝒟_p, ℓ_p is *not* in the kernel. Run the argument below with J in place of J_L (no L_p condition): for every nonzero x ∈ S_p⁰ it gives a direction with 𝒪_p(x) ≠ 0, because x|_J ≠ 0 by Sah's lemma and Kummer disjointness. So 𝒪_p is injective on S_p⁰: the obstruction separates all classes, including those of ℓ_p. Status: PROVED from the same inputs. W_p ⊄ ker 𝒪_p^univ, which is the first branch of the fork. The second branch holds too: restriction to 𝒟_p^ℓ survives, by the universal linear algebra above.

**(A1) with an intrinsic arithmetic reason (PROVED).** Let Ω = ℚ(E[p], μ_p, Σ^{1/p}) and J_L = Gal(ℚ̄/Ω·L_p). Take two admissible primes γ₀ and γ′ with Frob_{γ′} = Frob_{γ₀}·[v,w′] for some v, w′ ∈ J_L, and put δ = [γ′, d] − [γ₀, d]. Such δ are *commutator-difference directions*. By the commutator identity:
- 𝒪_p(y)(δ) = B_{v,w′}(y,d) = −e(y(v),d(w′)) + e(y(w′),d(v)).
- This is 0 for every y ∈ W_p, because κ(P_i)|_{G_{L_p}} = 0: P_i is p-divisible over L_p (Lean `commChange_eq_zero_of_left`).
- So these δ lie in 𝒟_p^ℓ for a reason intrinsic to the points. Directions split completely in L_p are not needed, and they are not admissible (PRE-CHECK 3, §4).

**(A2) (PROVED).** Let x ∈ S_p⁰ ∖ ℓ_p. Then x ∉ W_p, so x|_{G_{L_p}} ≠ 0 by R4.
- *Kummer disjointness.* Gal(L_p(Σ^{1/p})/L_p) is μ_p-isotypic, while E[p] is irreducible of dimension 2. So x|_{J_L} ≠ 0.
- *Surjectivity.* x|_{J_L} is a G_ℚ-equivariant homomorphism, so its image is all of E[p] (R1, `rd:rank-two`). Choose v, w′ ∈ J_L with e(x(v), x(w′)) ≠ 0.
- *Base direction.* γ₀ is admissible with Frob_{γ₀} = −I on E[p], and trivial on μ_p and the radicals. This uses ℚ(E[p]) ∩ ℚ(μ_p, Σ^{1/p}) = ℚ(μ_p), because SL₂(𝔽_p) is perfect for p ≥ 5.
- *Second direction.* Chebotarev, in the finite extension cut out by E[p], μ_p, Σ^{1/p}, L_p, x and the Heisenberg cocycle (x, x, u), gives γ′ with Frob_{γ′} = Frob_{γ₀}[v,w′].
- *Conclusion.* With d = x ∈ S_p⁰ ⊂ H¹(G_Σ,E[p]), 𝒪_p(x)(δ) = B(x,x) = −2e(x(v),x(w′)) ≠ 0, since p is odd (Lean `commChange_self_ne_zero`). The abstract assembly is Lean `stageA_kernel`.

**Consequences.**
- *Explicit extraction (PROVED).* Only after the theorem: choose finitely many δ₁,…,δ_r among these differences to obtain S_p⁰/ℓ_p ↪ 𝔽_p^r.
- *Remark (PROVED).* If loc_p(W_p) ≠ 0, then S_p = W_p + S_p⁰, and S_p⁰/ℓ_p ≅ S_p/W_p ≅ Ш[p]. Theorem A then sees exactly the excess.
- *Remark (HEURISTIC).* If loc_p(W_p) = 0, the strict theory misses at most one non-strict excess direction. A self-dual version with both classes in S_p, using the Bloch–Kato condition at p (which is isotropic), would close this gap but needs the lift test with a Lagrangian, non-strict condition at p. Not checked.

**What `vertical:obstruction-span` adds beyond Chebotarev on L_p.**
- Chebotarev on L_p alone detects x|_{G_{L_p}} ≠ 0, a first-order Kummer fact; that is the receiver.
- Obstruction-span contributes the Heisenberg commutator identity. It turns that fact into a nonzero *second-order Frobenius invariant* z_γ at Frobenius-acyclic primes, the primes where localization of every Selmer class is already zero.
- At χ = 1 it contributes only symmetric forms, which suffice for detection.
- It adds nothing about the size of Ш[p]. Theorem A is an identification of the same kind as receiver exactness and gives no bound. This is consistent with lanes A–D of `UNIFORM_STEP_FINDINGS`: 𝒪_p is a cup product with p-dependent tame characters, the Lane C Lemma 5 shape.

## 3. Stage B: first failure `GENERIC_RANK1_ONLY`

**Lemma B1 (PROVED, Lean `preserve_forces_loc_zero`).** Suppose a switch at one prime keeps the generic H¹ = ⟨P₁,P₂⟩ in both the finite and the switched complex, as preserving the class Δ_W requires. Then loc_γ(W) = 0.
- There is no generic class with f(A) = v₀ ≠ 0.
- The unit volume v₀ ∧ x of `rd:det-switch` is the whole valuation mechanism, so it has nothing to act on. The other two cases each lose Δ_W:

| rank of loc_γ on W | Generic H¹ after the switch | Effect on Δ_W |
|---|---|---|
| 1 | A line | Replaced by a generic rank-one class: the `rd:det-switch` situation |
| 2 | 0 | Destroyed |

**Lemma B2 (PROVED, linear algebra; Lean `single_plane_drop_two`, `single_plane_val_zero`, `det_ratio`).** In the case loc_γ(W) = 0:
- Generically, the relaxed localization image L is a Lagrangian with L ∩ F = L ∩ S = 0. So L is the graph of a self-adjoint φ: F → S.
- Write the Jordan exponents of φ as a_i. This uses congruence diagonalization over the DVR, with 2 a unit; the split local model F ⊕ S with unimodular cross pairing is taken from `rd:local-model` (IMPORTED structure; its transfer to odd p is HEURISTIC).
- The special-fibre change is dim H¹(C_{S,k}) − dim H¹(C_{F,k}) = #{a_i<0} − #{a_i>0}.
- In the top exterior power the two Δ_W coordinates differ by det φ, so the valuation shift has absolute value |Σa_i|.
- For one plane, a drop 2+2r ↦ 2r forces a₁, a₂ > 0, so |Δv| ≥ 2. Conversely, Δv = 0 forces no change of dimension.

So no single-prime switch both lowers the special fibre by two and preserves Δ_W.

**Caveat (PROVED, Lean `two_plane_escape`).** With two planes switched at once, exponents (1,1,1,−3) give a drop by two with Δv = 0. The no-go is specific to one plane.
- A two-plane switch needs relaxed excess classes whose localization orders at two primes have that exact Jordan type.
- No OpenAI lemma supplies such classes, and none is constructed here (HEURISTIC that none is available).

**No DVR family carries the Stage-B target (HEURISTIC, with the noted PROVED parts).**
- **O = ℤ_p.** Generic H¹_f(ℚ,V) = ⟨P₁,P₂⟩ holds iff Ш[p^∞] is finite. That is FIN at p, a forbidden input.
  - Moreover H¹(ℚ_γ, V) = 0 for γ ≠ p (PROVED: a_γ ≠ 1+γ by Hasse). So the local planes are torsion, and the `rd:local-model` free planes do not exist.
- **O = Λ_(t)**, the cyclotomic variable. Generic H¹ = 0 at ordinary p (Kato), and the t-direction is wild: stop 1 at p = 17.
- **O = 𝔽_p[[u]] or ℤ_p[[u]]_(p)**, a tame artificial family, the OpenAI setting.
  - By the fork in §2.2, ℓ_p is obstructed along some admissible direction, so the points do not extend generically along it.
  - `vertical:tests` shows that the generic classes these families carry have rank ≤ 1.

Conclusion: the only switches with valuation control in the audited sources need a generic rank-one class. **First failure of Stage B: `GENERIC_RANK1_ONLY`.**

## 4. PRE-CHECK

1. **Fixed places are blind. VERIFIED (PROVED).**
   - For v ≠ p, E(ℚ_v) is a finite group times a pro-v group, so #E(ℚ_v)/p = #E(ℚ_v)[p]. This is 0 for p large relative to any fixed finite set of places.
   - Admissible directions are therefore p-dependent tame primes. Stage A uses no direction at p.
2. **The strict space. VERIFIED (PROVED; Lean `not_dvd_of_even_card`).**
   - E(ℚ)[2] ≠ 0 forces #E(𝔽_p) to be even. With the Hasse bound this gives p ∤ #E(𝔽_p) for every good p ≥ 7, so E(ℚ_p)/p ≅ 𝔽_p.
   - Hence dim S_p⁰ = 2 + dim Ш[p] − ε_p, and dim ℓ_p ≥ 1.
3. **The receiver already supplies Stage A. VERIFIED WITH A CORRECTION (PROVED).**
   - Primes γ split completely in L_p are **not** admissible: Frob_γ = 1 on E[p], so M(γ) − 1 = 0, the local complex at γ is not acyclic, and A is undefined.
   - The correct directions are commutator differences over J_L (§2.2). The intrinsic reason for (A1) is P_i ∈ pE(L_p).
   - `EXCESS_OBSTRUCTION_PROVED` is a reformulation of the receiver kernel R4.
4. **The tame route is the expected Stage B/C endpoint. NOT TESTED (HEURISTIC).** Stage B fails before any index is produced. In the two-plane escape the index would be a localization determinant of excess classes. That is the kind of p-dependent quantity that would lead to `TAME_LAW_G1`, but this is not verified.
5. **Supersingular p.**
   - Stage A covers them: only the strict condition at p and E(ℚ_p)/p ≅ 𝔽_p are used.
   - The Stage-B sources do not cover them: (V) over ℚ uses "the ordinary global complex", and (RD) is 2-adic. This is moot, because Stage B fails for p-independent reasons.

## 5. Stops

- **(1) p = 17.** Stage A contains no p-adic regulator, and no direction at p.
- **(2) Receiver.** Not rebuilt. Only its kernel statement R4 is used.
- **(3) Fixed local conditions.** All directions are p-dependent tame primes.
- **Not used:** no per-prime computation, no W3, no plectic framework, no FIN/BSD/#Ш/q input.

## 6. Lean (`RequestProject/Continuation/ExcessObstruction.lean`, no `sorry`)

Every theorem below depends only on [propext, Classical.choice, Quot.sound]. The exception is `preserve_forces_loc_zero`, which depends on [propext, Quot.sound].

- **Stage A, universal kernel:** `ker_restrictObs`, `ker_restrictObs_eq_iff`, `a2_iff`, `restrictObs_of_mem`.
- **Commutator change at the trivial twist:** `commChange_symm`, `commChange_self`, `commChange_self_ne_zero`, `commChange_eq_zero_of_left`, `span_commChange_le`, `not_mem_span_of_not_symm`, `exists_not_symm`.
- **Stage A assembly:** `stageA_kernel`.
- **PRE-CHECK 2:** `not_dvd_of_even_card`.
- **Stage B:** `preserve_forces_loc_zero`, `single_plane_drop_two`, `single_plane_val_zero`, `two_plane_escape`, `det_ratio`.

The arithmetic steps (lift test, Chebotarev, Kummer theory) are not formalised; they are labelled in §§0–2.

FIN, ORDER9 and Q36: unchanged.
