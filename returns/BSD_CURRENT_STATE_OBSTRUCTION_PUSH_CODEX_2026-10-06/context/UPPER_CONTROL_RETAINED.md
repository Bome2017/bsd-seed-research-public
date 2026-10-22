# UPPER CONTROL of the receiver `B_p`: derivation (2026-10-06, continuation)

## PRIMARY STATUS: **PRECISE_ARITHMETIC_OBSTRUCTION**

Summary of what is proved here (in writing, with the imports listed in §12):

* **Theorem A (transgression vanishes).** For every prime `p ≥ 5`, `H²(Γ_p, E[p]) = 0`.
* **Theorem B (the receiver is a Selmer group over ℚ).** For every prime `p ≥ 5`, restriction
  induces an isomorphism `𝒮_p / W ≅ B_p`. Here `𝒮_p ⊂ H¹(ℚ, E[p])` is the Selmer group whose
  local conditions are `ℒ_v = ker(H¹(ℚ_v, E[p]) → H¹(I_{L_p,w} or G_{L_p,w}, E[p]))`, and
  `W = E(ℚ)/p`.
* **Theorem C (comparison of local conditions).** `ℒ_v` equals the Selmer condition at every
  place `v`, for every `p ≥ 5` with `p ≠ 4547`. At `p = 4547`, `ℒ_p` contains the Selmer
  condition with codimension at most one.
* **Corollary D.** For every prime `p ≥ 5`, `p ≠ 4547`, the retained BFR injection
  `Sha(E/ℚ)[p] ↪ B_p` **is an isomorphism**. For `p = 4547`,
  `dim Sha[p] ≤ dim B_p ≤ dim Sha[p] + 1`. Hence, for **every** `p ≥ 5`,

      dim_{𝔽_p} B_p ≤ 1   ⟺   Sha(E/ℚ)[p] = 0.

  The direction `⇐` is new. The direction `⇒` is the retained BFR criterion, which uses parity.

**Obstruction.** The receiver carries no information beyond `Sha(E/ℚ)[p]` itself. Each of the
four requested devices (S-units/S-ideals, ambiguous and relative classes, Hochschild–Serre for
`P_p ⊲ Γ_p`, and the `V`-isotypic `G_{0,p}`-functor) is computed exactly below. Together they
give `B_p ≅ Sha[p]`, not a smaller object. The locally admissible transgression defect is `0`.
So **no independent upper bound on `B_p` exists that is not literally an upper bound on
`Sha(E/ℚ)[p]`.** The additional arithmetic input that is necessary and sufficient is:

> **(Sel_p)** `dim_{𝔽_p} Sel_p(E/ℚ) = 2`, i.e. `Sha(E/ℚ)[p] = 0`, for the primes in question.
> For `p ≠ 4547` this is equivalent to `dim B_p ≤ 1`. Because of parity it is also equivalent to
> `dim_{𝔽_p} Sel_p(E/ℚ) ≤ 3`.

The input must come from outside this construction, for example an Euler system with a
`p`-integral bottom class, or a `p`-adic BSD input with a unit leading term. The
class-field-theoretic side of `L_p/K'_p` cannot supply it, because by Theorem B the class-group
side *is* the Selmer side.

FIN, ORDER9 and BSD: **unchanged**. Q36: unchanged and separate. No primary component of `Sha`
is settled.

Labels used below:

* **[RET]** a retained input fixed by the task (BFR and its inputs, not reproved);
* **[IMP]** an imported standard theorem;
* **[NEW]** a statement derived here;
* **[COMP]** a computational check (Lean kernel-evaluated where stated);
* **[CONJ]** a conjectural statement. None is used in any proof.

---

## 1. Setting and retained inputs

The curve is `E: y² = x³ − x² − 66020924x − 65074271436`, with `E(ℚ) = ⟨T⟩ ⊕ ℤP1 ⊕ ℤP2` and
`T` of order 2. Let `p ≥ 5` be prime and `V = E[p]`. Write
`d_p = 1 − p² − 66020924p⁴ − 65074271436p⁶` and `F_p = ℚ(√d_p)`. Put `K_p = ℚ(E[p])` and
`K'_p = K_p F_p`. Let `L_p = K'_p(Q1, Q2, Q3)`, where `pQ1 = P1`, `pQ2 = P2` and `pQ3 = R_p`.
Then `Γ = Γ_p = Gal(L_p/ℚ)`, `P = Gal(L_p/K'_p)` and `G₀ = Gal(K'_p/ℚ)`. Finally
`A_p = Cl(O_{L_p}[1/p])/p` and `B_p = Hom_Γ(A_p, V)`.

* **[RET-1]** `G₀ = GL₂(𝔽_p) × C₂`. The `C₂` factor is `Gal(F_p/ℚ)` and acts trivially on `V`.
  `End_{𝔽_p[G₀]}(V) = 𝔽_p`.
* **[RET-2]** As a `G₀`-module, `P ≅ V ⊕ V ⊕ U` with `U ∈ {0, Vε}`, where `ε` is the character
  of `F_p`. The first two coordinates are the Kummer maps `κ₁`, `κ₂` of `P1` and `P2`. The
  third constituent may degenerate at `4547`. In all cases `Hom_{G₀}(U, V) = 0`.
* **[RET-3]** `H¹(Γ, V) = W := E(ℚ)/p = 𝔽_p κ₁ ⊕ 𝔽_p κ₂`, and
  `ker(H¹(ℚ, V) → H¹(L_p, V)) = W`. This is BFR (★).
* **[RET-4]** (BFR) `res(Sel_p(E/ℚ)) ⊂ B_p`, which gives `Sha[p] ↪ B_p`. This is the retained
  injection at every `p ≥ 5`, including `2243, 4547, 5843`. The `p`-adic input is: the
  division point of the local Kummer generator is rational over every completion `L_{p,w}`,
  `w | p`. The generator is `R_p` at `p ≠ 4547` and `P2` at `p = 4547`.
* **[RET-5]** Reduction types and Tamagawa numbers:
  * `2: I₁*` (`c = 2`);
  * `3: I₂` non-split (`c = 2`);
  * `2243: I₁` split (`c = 1`);
  * `4547: III` (`c = 2`);
  * `5843: I₂` non-split (`c = 2`).

  Retained parity: `dim Sha[p]` is even.
* **[RET-6]** `E(ℚ_p)[p] = 0` for every `p ≥ 5`.
  * At good `p` this holds because rational 2-torsion excludes anomalous primes (record
    Lemma A1). Indeed `2 | #Ẽ(𝔽_p)`, and `#Ẽ(𝔽_p) ∈ (0, 2p)`, so `p ∤ #Ẽ(𝔽_p)`. At `p = 5`,
    `#Ẽ(𝔽₅) = 8` [Lean `card_affine_F5`].
  * At `2243` and `5843` the index `[E(ℚ_p):E₁(ℚ_p)]` is prime to `p` [Lean `index_coprime`].
  * At `4547` this is BFR Lemma L(ii).

  Consequently `dim E(ℚ_p)/p = 1`.
* **[RET-7]** `p` splits in `F_p` [Lean `exists_sqrt_dp_padic`]. So `ε` is trivial on
  `G_{ℚ_p}`, and `K'_{p,w} = ℚ_p(E[p])`.

## 2. Group cohomology of `G₀` (all `p ≥ 5`; `p` divides `|G₀|`)

No semisimplicity of `𝔽_p[G₀]` is used. The only tools are those listed below.

**Lemma 2.1 (central involution) [NEW, elementary].** Let `z = (−I, 1) ∈ G₀`. If `z` acts by
`−1` on an `𝔽_p[G₀]`-module `M`, then `H^i(G₀, M) = 0` for all `i ≥ 0`.

*Proof.* Conjugation by a central element induces the identity on `H^*(G₀, M)` [IMP: Brown,
*Cohomology of Groups*, II.6.2]. Here this conjugation is induced by the module automorphism
`m ↦ zm = −m`. So `−1 = 1` on a group killed by `p`, and `p` is odd. ∎

* `z` acts by `−1` on `V`, on `Vε`, on `P` (by RET-2) and on `Λ²P ⊗ V`.
* `z` acts by `+1` on `Hom(P, V)` and on `Λ²P`.

Hence:

    H^i(G₀, V) = 0,   H^i(G₀, P) = 0,   Hom_{G₀}(Λ²P, V) = 0.              (2.1)

In particular the extension `1 → P → Γ → G₀ → 1` splits, since its class lies in
`H²(G₀, P) = 0`. So `Γ ≅ P ⋊ G₀`.

**Lemma 2.2 (stable elements, TI Sylow) [IMP + NEW].** Let `U₀ = {(1 *; 0 1)} × 1`, which is a
Sylow `p`-subgroup of `G₀`, of order `p`. It is TI, and `N := N_{G₀}(U₀) = B × C₂` with `B` the
Borel subgroup. For every `𝔽_p[G₀]`-module `M` and `n ≥ 1`,
`H^n(G₀, M) ≅ H^n(U₀, M)^{N}`.

*Proof.* Restriction to a Sylow subgroup is injective onto the stable elements [IMP: Brown
III.10.4; Cartan–Eilenberg XII.10.1], for arbitrary coefficients. For `g ∉ N`,
`U₀ ∩ gU₀g⁻¹ = 1`, so the stability conditions are vacuous in positive degree, and only
`N`-invariance remains. ∎

**Lemma 2.3 [NEW].** `H¹(G₀, 𝔽_p) = 0` and `H¹(G₀, ad⁰V) = 0` for every `p ≥ 5`. Hence
`H¹(G₀, End V) = 0`. Also `H¹(G₀, Hom(Vε, V)) = 0`.

*Proof.*

* `G₀^{ab} = 𝔽_p^× × C₂`, because `SL₂(𝔽_p)` is perfect for `p ≥ 5`. This has order prime
  to `p`.
* For `ad⁰`: `u = (1 1; 0 1)` acts on `ad⁰ = ⟨e, h, f⟩` with `(u−1)f = h − e`, `(u−1)h = −2e`
  and `(u−1)e = 0`. So `(u−1)³ = 0` and the norm `(u−1)^{p−1}` is `0` (`p ≥ 5`). Hence
  `H¹(U₀, ad⁰) = ad⁰/(u−1)ad⁰ = ⟨f̄⟩`.
* Let `t = diag(a, d)`. Then `t⁻¹ut = u^{d/a}`, and the twisted action on cocycles gives
  `(t·c)(u) ≡ (d/a)·t·c(u)`. Also `t·f = (d/a)f`. So `T` acts on `H¹(U₀, ad⁰)` by the
  character `(d/a)²`.
* With `a = 2`, `d = 1` this character is `1/4 ≠ 1` in `𝔽_p` for `p ≥ 5` [Lean
  `Seed.Exceptional.torus_weight_nontrivial`]. So `H¹(G₀, ad⁰) = 0` by Lemma 2.2.
* For `SL₂` the character is `a⁻⁴`, which is trivial at `p = 5`. This is the familiar
  exception `H¹(SL₂(𝔽₅), ad⁰) ≠ 0`. It does **not** occur for `G₀ ⊃ GL₂(𝔽_p)`.
* `End V = 𝔽_p ⊕ ad⁰`, since `p` is odd. For `Hom(Vε, V) = End(V) ⊗ ε`, the central factor
  `(1, c)` acts by `−1`, and the argument of Lemma 2.1 applies. ∎

So `H¹(G₀, Hom(P, V)) = H¹(G₀, End V)² ⊕ H¹(G₀, Hom(U, V)) = 0`.             (2.2)

## 3. Hochschild–Serre for `P ⊲ Γ`: restriction to `P` is injective on `H²`

The Hochschild–Serre spectral sequence is
`E₂^{i,j} = H^i(G₀, H^j(P, V)) ⇒ H^{i+j}(Γ, V)`. Here `P` acts trivially on `V`.

* `E₂^{2,0} = H²(G₀, V) = 0` by (2.1).
* `E₂^{1,1} = H¹(G₀, Hom(P, V)) = 0` by (2.2).

Hence **[NEW 3.1]** restriction `H²(Γ, V) → H²(P, V)^{G₀}` is injective.

The target is computed as follows. Since `P` acts trivially on `V`, there is an exact sequence
of `G₀`-modules:

    0 → Ext¹_ℤ(P, V) ≅ Hom(P, V) → H²(P, V) → Hom(Λ²P, V) → 0.

* The quotient map records the commutator pairing of a central extension.
* The sub consists of the abelian extensions. These are classified by their `p`-power map
  `φ: P → V`, `x̄ ↦ x̃^p`.

By (2.1), `Hom_{G₀}(Λ²P, V) = 0`. So

    H²(P, V)^{G₀} = Hom_{G₀}(P, V) = 𝔽_p·pr₁ ⊕ 𝔽_p·pr₂.                       (3.1)

These are exactly the two Mordell–Weil translation directions (RET-2).

**So the only possible transgression targets are the `V^{⊕2}` Mordell–Weil directions.** The
`U` (that is, `R_p`) direction contributes nothing, because `Hom_{G₀}(U, V) = 0`.

## 4. Theorem A: `H²(Γ_p, V) = 0` for every `p ≥ 5` [NEW]

*Proof.* Let `ξ ∈ H²(Γ, V)` and let `1 → V → Γ̃ → Γ → 1` be the corresponding extension.

1. Fix a splitting `s: G₀ → Γ` (§2). Then `s^*ξ ∈ H²(G₀, V) = 0`, so `s` lifts to
   `s̃: G₀ → Γ̃`.
2. Let `X ⊂ Γ̃` be the preimage of `P`. It is a central extension `1 → V → X → P → 1`, and
   `G₀` acts on it by conjugation through `s̃`. The commutator pairing `Λ²P → V` is
   `G₀`-equivariant, so it is zero by (2.1). Hence `X` is abelian: a `ℤ[G₀]`-module extension
   of `P` by `V`, with `G₀`-equivariant `p`-power map `φ: P → V`.
3. Suppose `ξ ≠ 0`. By §3, `ξ|_P ≠ 0`, so `φ ≠ 0`. Since `V` is irreducible, `pX = φ(P) = V`.
4. `X[p]` is an extension `0 → V → X[p] → ker φ → 0` of `𝔽_p[G₀]`-modules. `P` is a direct sum
   of simple modules, so `ker φ ≅ V ⊕ U` is a direct summand of `P`. Then
   `Ext¹_{G₀}(ker φ, V) = H¹(G₀, Hom(ker φ, V))` is a summand of `H¹(G₀, Hom(P, V)) = 0` by
   (2.2). So `X[p] = V ⊕ K` with `K` a `G₀`-submodule.
5. Put `Y = X/K`. Then `|Y| = p⁴`, `pY ≅ V` and `Y[p] = X[p]/K ≅ V = pY`. (If `px ∈ K`, then
   `px ∈ K ∩ V = 0`.) So `Y ≅ (ℤ/p²)²`, and multiplication by `p` gives
   `Y/pY ≅ pY ≅ V` as `G₀`-modules.
6. So `G₀ → Aut(Y) = GL₂(ℤ/p²)` lifts the standard representation. Restrict it to
   `SL₂(𝔽_p) × 1`. The determinant of the lift is a homomorphism from a perfect group into the
   abelian group `1 + pℤ/p²`, so it is trivial. This gives a section of
   `SL₂(ℤ/p²) → SL₂(𝔽_p)`.
7. That is impossible for `p ≥ 5`. Every lift `x` of `u = (1 1; 0 1)` satisfies
   `x^p = 1 + p·e₁₂ ≠ 1`, while `u^p = 1`. This is [Lean, kernel-checked for every prime
   `p ≥ 5`: `Seed.NoLift.pow_eq_of_lift`, `Seed.NoLift.no_section_SL2`]; classically, Serre,
   *Abelian ℓ-adic representations*, IV-23, Lemma 3.

Hence `ξ = 0`. ∎

**Remark 4.1.** Equivalently, the differential `d₂: E₂^{0,2} = Hom_{G₀}(P, V) → E₂^{2,1}` is
injective. Its target contains `H²(G₀, End V)²`, and `H²(U₀, ad⁰)^T ≠ 0` (weight
`(a/d)(d/a) = 1`). The class of `GL₂(ℤ/p²) → GL₂(𝔽_p)` lives there. Each Mordell–Weil
direction is "transgressed" onto the non-split class of `GL₂(ℤ/p²)`. That is the precise sense
in which the `V^{⊕2}` directions are eaten.

## 5. Theorem B: `B_p ≅ 𝒮_p / W` (all `p ≥ 5`) [NEW]

**CFT translation [IMP: class field theory].** `Hom(A_p, V)` is the group of homomorphisms
`f: G_{L} → V` (`L = L_p`) such that:

* `f` vanishes on every inertia group `I_{L,w}`, for `w ∤ p` finite;
* `f` vanishes on every decomposition group `G_{L,w}`, for `w | p`.

`L` is totally complex, so there is no archimedean condition. `Γ`-equivariance means
`f ∈ H¹(L, V)^Γ`. So

    B_p = H¹_∅(L, V)^Γ,   with the local conditions just described.              (5.1)

**Five-term sequence [IMP: Hochschild–Serre].** `V^{G_L} = V`. So:

    0 → H¹(Γ, V) → H¹(ℚ, V) →^{res} H¹(L, V)^Γ →^{tr} H²(Γ, V) → H²(ℚ, V).

By Theorem A, `res` is **surjective**. Its kernel is `W` (RET-3).

**Local conditions pulled back to ℚ.** For each place `v` of ℚ, fix `w | v` and define:

* `ℒ_v := ker(H¹(ℚ_v, V) → H¹(I_{L,w}, V)) = H¹(G_{ℚ_v}/I_{L,w}, V)` for `v ∤ p` finite;
* `ℒ_p := ker(H¹(ℚ_p, V) → H¹(L_w, V)) = H¹(Gal(L_w/ℚ_p), V)`;
* `ℒ_∞ := H¹(ℝ, V) = 0`.

The equalities are inflation–restriction, using that `I_{L,w}` and `G_{L,w}` act trivially on
`V`. For `c ∈ H¹(ℚ, V)`, `res(c)` satisfies the conditions of (5.1) at all `w | v` iff
`c_v ∈ ℒ_v`. (The conditions at the conjugates of `w` follow by conjugation, since `c` is
defined over ℚ.) Put `𝒮_p := {c ∈ H¹(ℚ, V) : c_v ∈ ℒ_v for all v}`. Then

    0 → W → 𝒮_p →^{res} B_p → 0   is exact.                                    (5.2)

By RET-4, `Sel_p(E/ℚ) ⊂ 𝒮_p`, i.e. `f_v := H¹_f(ℚ_v, V) ⊂ ℒ_v` for all `v`. Therefore

    0 → Sha(E/ℚ)[p] → B_p → 𝒮_p/Sel_p(E/ℚ) → 0,
    𝒮_p/Sel_p ↪ ⊕_v ℒ_v/f_v.                                                  (5.3)

**Transgression screen, answered.** Here `T_p := tr(B_p) = 0`. The locally admissible
transgression defect is zero: not just after quotienting the Mordell–Weil directions, but
identically. The rank-two contribution is absorbed into `P` (the `V^{⊕2}` summand), and
`H²(Γ, V)` has no room left (Theorem A). Any rank-two class-group contribution seen over
`K_p` or `K'_p` (§7) dies over `L_p`.

## 6. Theorem C: the local comparison `ℒ_v` versus `f_v` [NEW]

Write `δ_v = dim ℒ_v − dim f_v ≥ 0`.

**6.1 `v = ∞`.** Here `ℒ_∞ = f_∞ = 0`.

**6.2 `v = q ≠ p` with `L/ℚ` unramified at `q`, or ramified only with inertia of order prime to
`p`.** Then `ℒ_q = H¹(G_q/I_q, V^{I_q}) = H¹_ur = f_q` [IMP: for `q ≠ p` and `p ∤ c_q`,
`f_q = H¹_ur`]. So `δ_q = 0`.

This covers every `q ∤ pN`:

* `ℚ(E[p])` is unramified at `q`;
* `F_p` contributes inertia of order 2;
* the Kummer classes of `P1` and `P2` (over ℚ) and of `R_p` (over `F_p`) are unramified
  at `q ≠ p`. This is because the local Tamagawa numbers over ℚ and over `F_p` are at most 4
  (see §7), hence prime to `p`.

It also covers `q = 4547` for `p ≠ 4547`. Type `III` is potentially good, so the inertia image
has order dividing 4, prime to `p`.

**6.3 `q ∈ {2, 3, 2243, 5843}`, `q ≠ p`.**

* If `h⁰(ℚ_q, V) = 0`, then `H¹(ℚ_q, V) = 0`, by the local Euler characteristic and Tate duality
  with `V ≅ V^∨(1)` [IMP]. So `δ_q = 0`.
* `h⁰ ≠ 0` happens only in these cases:
  * `q = 2243`, split `I₁`: `μ_p ⊂ ℚ_q`, i.e. `p | 2242`;
  * `q = 5843`, non-split `I₂`: `q ≡ −1 (mod p)`, i.e. `p | 5844`;
  * `q = 3`, non-split: `p | 4`.

  For `q = 2`, type `I₁*`: the twisting character is ramified while `ω` is unramified, so never.
  Since the Tate extension is ramified (`p ∤ v_q(Δ_min) ∈ {1, 2}`), invariants lie in the sub.
  For `p ≥ 5` this leaves exactly `p ∈ {19, 59}` (from `q = 2243`) and `p = 487` (from
  `q = 5843`) [Lean `Seed.Exceptional.exceptional_local_primes`].
* In those cases `δ_q ≤ dim H¹ − dim f_q = 2h⁰ − h⁰ = 1`.

(In fact `ℒ_q = H¹(ℚ_q, V)`. The inertia of `L/ℚ` at `q` has a nontrivial `p`-part, and the
norm `Σ_{i<p^k} σ^i = p^{k−1}(σ−1)^{p−1}` kills `V`.)

**6.4 `v = p`, `p ∤ N` (good), or `p ∈ {2243, 5843}`.**

*Step 1.* Put `D = Gal(L_w/ℚ_p)` and `P_w = Gal(L_w/K'_w) ⊂ P`. By RET-7, `K'_w = ℚ_p(E[p])`.
The `ℚ_p`-image `Im` of `ρ̄|_{G_{ℚ_p}}` has `H¹(Im, V) = 0`:

* **Ordinary good reduction or multiplicative reduction.** `V|_{G_{ℚ_p}}` is an extension of
  `χ₂` by `χ₁`, with `χ₁|_I = ω` and `χ₂|_I = 1` [IMP: Serre 1972 §1.11–1.12, Tate curve].
  * If `Im` has no element of order `p`, then `H¹ = 0` because `p ∤ |Im|`.
  * Otherwise the stable-element argument gives `H¹(Im, V) = H¹(U, V)^{Im/U}`. Its character
    is `χ₂²χ₁⁻¹`, whose restriction to inertia is `ω⁻¹ ≠ 1`. So `H¹(Im, V) = 0`.
* **Supersingular.** `p ∤ |Im|` [IMP: Serre 1972 Prop. 12], so `H¹(Im, V) = 0`.

*Step 2.* By inflation–restriction, `ℒ_p = H¹(D, V) ↪ Hom_D(P_w, V)`.

*Step 3.* The local classes of `P1`, `P2` and `R_p` all lie in `f_p`, which is one-dimensional
(RET-6). So `P_w` is the image of `G_{K'_w}` under the class `ρ` of a generator of
`E(ℚ_p)/p ≅ E₁(ℚ_p)/p`. Such a class comes from `H¹(ℚ_p, Ê[p])` (formal-group Kummer sequence)
[IMP].

* **Ordinary or multiplicative.** `Ê[p]` is the `χ₁`-line, and `P_w ⊂ χ₁`. Since `χ₁ ≠ χ₂` on
  inertia, `dim Hom_D(P_w, V) ≤ 1`.
* **Supersingular.** `V|_D` is absolutely irreducible (`ψ₂ ≠ ψ₂^p` on inertia). So
  `Hom_D(P_w, V) ⊂ End_D(V) = 𝔽_p`.

Either way, `dim ℒ_p ≤ 1 = dim f_p`, so `δ_p = 0`.

**6.5 `v = p = 4547`.** Here `h⁰(ℚ_p, V) = 0` by RET-6. So
`dim H¹(ℚ_p, V) = 2 + h⁰ + h² = 2`, and `δ_p ≤ 2 − 1 = 1`. The local structure at `4547` is
**not** reopened (task constraint), so `δ_{4547} ∈ {0, 1}` is left open. For `p = 4547` there
is no other `q` with `δ_q ≠ 0`: `4547 ∤ 2242·5844·4`.

**6.6 The exceptional primes `p ∈ {19, 59, 487}`.** By 6.2–6.4, `δ = δ_q = 1`, with
`q = 2243, 2243, 5843` respectively. So `𝒮_p` relaxes `Sel_p` only at `q`.

* By Greenberg–Wiles [IMP: DDT Thm 2.19], with `V ≅ V^∨(1)` and the balanced Selmer structure
  (Σ = 0):

      dim 𝒮_p − dim 𝒮_p^* = δ_q = 1,
      𝒮_p^* = ker(loc_q : Sel_p → f_q).

* So `dim 𝒮_p = dim Sel_p + 1 − η_p`, where `η_p = dim loc_q(Sel_p) ∈ {0, 1}`.
* **[COMP, Lean kernel-evaluated: `Seed.EtaCheck.eta_19`, `eta_59`, `eta_487`; also
  `checks/eta_exceptional.py`].** The reductions of `P1` and `P2` mod `q` are nonsingular.
  In the cyclic group `Ẽ_ns(𝔽_q)` (of order 2242, resp. 5844, divisible exactly once by `p`),
  `(n/p)·c_q·P̃_i ≠ 0`.
* Using `E(ℚ_q)/p ≅ E₀(ℚ_q)/p ≅ Ẽ_ns(𝔽_q)/p` (`E₁` is pro-`q`; `c_q` is prime to `p`) [IMP],
  this says `loc_q(P_i) ≠ 0`. Hence `η_p = 1` and `𝒮_p = Sel_p`.

**Theorem C [NEW].** `𝒮_p = Sel_p(E/ℚ)` for every prime `p ≥ 5`, `p ≠ 4547`. For `p = 4547`,
`dim 𝒮_p/Sel_p ≤ 1`.

**Corollary D [NEW].** Combine with (5.2) and (5.3):

* `B_p ≅ Sha(E/ℚ)[p]` for every `p ≥ 5`, `p ≠ 4547`. The BFR map is an isomorphism.
* `dim Sha[p] ≤ dim B_p ≤ dim Sha[p] + 1` for `p = 4547`.
* For all `p ≥ 5`: `dim B_p ≤ 1 ⟺ Sha[p] = 0`, using parity for `⇒`.

## 7. Items 1–2: S-units, S-ideals, ambiguous and relative classes for `L_p/K'_p` [NEW, with explicit local terms]

Let `S` be the set of places of `K'` above `p`, with `S_L` the places of `L` above them.

* **`L/K'` is unramified outside `S`.** `L = K'(Q1, Q2, Q3)`, and `E[p] ⊂ K'`. Take a place
  above `q ≠ p`. The Kummer class of `P1` or `P2` (over ℚ), or of `R_p` (over `F_p`), lies in
  the local Kummer image `E(·)/p`. That image is unramified whenever the local Tamagawa number
  is prime to `p` [IMP].
  * The types over ℚ are `I₁*`, `I₂`, `I₁`, `III`, `I₂`.
  * Their quadratic base changes are among `I₂*`, `I₄`, `I₂`, `I₀*`, `III`.
  * All of these have `c ≤ 4 < p`.

  So the restriction of each Kummer class to the inertia of `K'` (which acts trivially on `V`)
  vanishes. Hence `I_q(L/K') = 1`.

**7.1 Ambiguous-class sequence.** Take `P`-cohomology of
`0 → O_{L,S}^× → L^× → Pr_{L,S} → 0` (Hilbert 90: `H¹(P, L^×) = 0`) and of
`0 → Pr_{L,S} → I_{L,S} → Cl_S(L) → 0`. Here `I_{L,S} = ⊕_{v∉S} ℤ[P/D_v]`, so
`I_{L,S}^P = I_{K',S}` (unramified) and `H¹(P, I_{L,S}) = ⊕ Hom(D_v, ℤ) = 0`. The result is the
exact sequence

    0 → H¹(P, O_{L,S}^×) → Cl_S(K') →^{j} Cl_S(L)^P → ker(H²(P, O_{L,S}^×) → H²(P, L^×)) → 0,

where `j` is extension of ideals. Also `H²(P, L^×) ↪ ⊕_{w∈S} H²(P_w, L_w^×)`, and the
`P_w`-local terms are the local Brauer groups.

**7.2 Genus (coinvariant) sequence.** By CFT, the norm corresponds to restriction of Artin
maps. Let `H_S(K')` be the `S`-split Hilbert class field. Then

    Cl_S(L)_P →^{N} Cl_S(K') → Gal((L ∩ H_S(K'))/K') → 0   is exact.

Apply the left-exact functor `Hom_{G₀}(− ⊗ 𝔽_p, V)`. Since `P` acts trivially on `V`,
`Hom_{G₀}(Cl_S(L)_P/p, V) = Hom_Γ(A_p, V) = B_p`. So

    0 → Hom_{G₀}(Gal(L∩H_S(K')/K'), V) → Hom_{G₀}(Cl_S(K')/p, V) →^{N^*} B_p.   (7.1)

**7.3 The local term, computed.** `Gal(L ∩ H_S(K')/K') = P / ⟨gP_wg⁻¹⟩`, because `L/K'` is
unramified outside `S`. So

    Hom_{G₀}(Gal(L∩H_S(K')/K'), V) = {a·pr₁ + b·pr₂ : (aκ₁ + bκ₂)|_{G_{K'_w}} = 0}
                                    = ℓ_p := {(a,b) : aP1 + bP2 ∈ pE(ℚ_p)}

for good `p`, `2243` and `5843`. The second equality uses `H¹(Im, V) = 0` (6.4, Step 1) and the
injectivity of the Kummer map. Here `dim ℓ_p = 2 − dim loc_p(W) ≥ 1`.

**So over `K'_p` the Mordell–Weil directions do force class-group content.** The `ℓ_p` line
(the locally `p`-divisible combination of `P1` and `P2`) gives an everywhere-unramified,
`p`-split `V`-extension `K'(p⁻¹(aP1 + bP2))/K'`. This is the "inevitable" contribution; it
agrees with the record's K-level formula `m_p = 2 + s − ε_p`. By (7.1) and Corollary D:

    dim Hom_{G₀}(Cl_S(K'_p)/p, V) ≤ dim ℓ_p + dim Sha(E/ℚ)[p]   (p ≠ 4547).

Inside `L_p` this contribution is absorbed into `P`. The extensions (7.1–7.3) do not produce a
smaller receiver: the kernel term is exactly the Mordell–Weil line, and the image lies in
`B_p ≅ Sha[p]`. The terms of 7.1 are not independently computable either. For example,
`H¹(P, O_{L,S}^×)` involves the full `S`-unit group of a field of degree about `2p¹⁰`. The
cohomological route (§§3–6) computes `B_p` exactly instead.

## 8. Transgression screen: the answers

1. The relevant part of `H²(Γ_p, V)`: the whole group is `0` (Theorem A), for every `p ≥ 5`,
   including `2243`, `4547` and `5843`.
2. Do the `V^{⊕2}` translation directions account for the rank-two contribution? Yes.
   `H²(P, V)^{G₀}` is exactly the Mordell–Weil plane (3.1). Every nonzero direction there is
   obstructed by the non-split class of `GL₂(ℤ/p²)` (§4, Remark 4.1).
3. After quotienting those directions, the remaining locally admissible transgression defect
   has dimension **0**. The residual receiver is `𝒮_p/Sel_p`, which is `0` for `p ≠ 4547` and
   has dimension at most 1 at `p = 4547`.
4. The only "C_p" objects produced are `C_p^{(0)} = Sha[p]` and
   `C_p^{(1)} = 𝒮_p/Sel_p ⊂ ⊕_v ℒ_v/f_v`. They are not smaller than the target, since
   `C^{(0)}` *is* the target.

## 9. Literature collision check

The source texts are not in the supplied input. The hypothesis and conclusion summaries below
come from the record's own source checks (FULL_COMPENDIUM units E16-183, E20b-*, E22b-041, and
the "Division-field source applicability audit"). I did not re-read the papers. **None of these
results is invoked in any proof above.**

* **Prasad–Shekhar** (arXiv 1912.12928; Pacific J. Math. 312 (2021)). These concern
  `K = ℚ(E[p])`, under `E(ℚ_p)[p] = 0` and `p`-unit Tamagawa numbers.
  * Thm 3.1: `rank ker(res^{ur}_p) ≥ rank Sel_p − 1`.
  * Thm 4.1: `m_p ≤ rank Sel_p + #T`.

  These are statements about the class group of `K`, where the Mordell–Weil directions survive.
  The present Theorem B concerns `L_p ⊃ K`, where they are absorbed. The two are consistent: §7
  recovers the `ℓ_p` contribution over `K'`.
* **Ray–Weston** (arXiv 2204.09757v2, J. Aust. Math. Soc. 118 (2025)). Their §5 assumes `Sha`
  is finite and gives rank `≥ 2` lower bounds. The record found their quotation of the PS upper
  bound unfaithful. Not used.
* **Dainobu** (JNT 264 (2024), arXiv 2304.05035; arXiv 2405.19142). Rational points contribute
  class-group quotients (lower bounds), and the second paper assumes analytic rank one. This is
  consistent with the `ℓ_p` term of §7.3. Not used.
* **Reflection, genus or Chevalley theorems**: not invoked. §7.1 is derived directly from
  Hilbert 90. §7.2 is plain CFT (norm ↔ restriction).
* **Shape of Theorem B.** That `Sha[p]` embeds in a class group of the field generated by
  `p`-division points of `E(ℚ)` is classical in spirit. I did not locate the exact isomorphism
  `B_p ≅ 𝒮_p/W`, with these local conditions and with `H²(Γ, V) = 0` via the non-split
  `GL₂(ℤ/p²)` extension, in the available record. This was not an exhaustive search.

## 10. Audit of the hypothesis "`p | |Γ_p|`"

Every step that touches `𝔽_p[G₀]` or `𝔽_p[Γ]` is listed here, with why it is valid even though
`p` divides the group order.

| Step | Tool | Why it is valid when `p` divides the group order |
|---|---|---|
| (2.1) | central `z` of order 2 | needs only that `2` is invertible in `𝔽_p` |
| Lemma 2.2 | Sylow restriction and stable elements | valid for all coefficients and all groups |
| Lemma 2.3 | weight computation on `H¹(U₀, −)` | uses explicit nilpotency, `(u−1)³ = 0` with `p ≥ 5` |
| §4 step 4 | `P` is a sum of simple modules, so its submodules are summands | true for any ring |
| §4 step 4 | splitting `X[p]` | `Ext¹ = H¹(G₀, Hom) = 0` by Lemma 2.3, not by semisimplicity |
| §4 step 7 | no-lift lemma | explicit matrix identity (Lean) |
| 6.4 | `H¹(Im, V) = 0` | either `p ∤ |Im|`, or the TI-Sylow weight computation |

No character idempotent or prime-to-`p` reflection is used.

## 11. Endpoint effect

* **Upper control of `B_p`.** Proved to be **equivalent** to `Sha(E/ℚ)[p] = 0` at every
  `p ≥ 5`, with `B_p ≅ Sha[p]` exactly for `p ≠ 4547`. So `dim B_p ≤ 1` is **not established**
  for any `p`, and none of the six statuses requiring a bound applies.
* **FIN, ORDER9, BSD**: unchanged. **Q36**: unchanged and separate.
* **Consequence for the program.** The forward-receiver route (W13/W21) is now known to be a
  reformulation: `B_p` is `Sha[p]`. A future uniform theorem must bound `Sel_p(E/ℚ)` by an input
  external to `L_p/K'_p`. The relative-class/transgression side is exhausted: its contribution
  is `0` (transgression), or the Mordell–Weil line `ℓ_p` (over `K'`), which is not part of `Sha`.
* **The single open local datum** of this analysis is `δ_{4547} ∈ {0, 1}`. It does not affect
  the equivalence.

## 12. Ledger

**Imported theorems [IMP].**

* Hochschild–Serre spectral sequence and five-term exact sequence.
* Central elements act trivially on cohomology (Brown II.6.2).
* Stable elements (Brown III.10.4).
* Universal coefficients for `H²(P, V)`, and the classification of central extensions.
* Class field theory: `S`-split Hilbert class field; norm ↔ restriction.
* Hilbert 90.
* Local Tate duality and the local Euler characteristic.
* `f_q = H¹_ur` for `q ≠ p`, `p ∤ c_q`.
* Greenberg–Wiles formula (DDT Thm 2.19).
* Serre 1972: local `p`-adic structure of `E[p]` (ordinary, supersingular, Tate curve).
* Formal-group Kummer sequence.
* `E₀/E₁ ≅ Ẽ_ns(𝔽_q)`, with `E₁` pro-`q`.
* Serre's non-splitting of `SL₂(ℤ/p²) → SL₂(𝔽_p)`. This one is also kernel-checked here.

**Retained inputs [RET].** RET-1 to RET-7 (§1), including the BFR theorem as fixed input.

**New derived statements [NEW].**

* Lemmas 2.1–2.3.
* Prop. 3.1 and formula (3.1).
* Theorem A.
* Theorem B, with (5.2) and (5.3).
* Theorem C (6.1–6.6).
* Corollary D.
* The sequences (7.1) and 7.1, and the identification 7.3.

**Conjectural steps [CONJ].** None used.

**Computational checks [COMP].**

| Module | Declarations | What they check | Axioms |
|---|---|---|---|
| `RequestProject/Seed/NoLift.lean` | `pow_eq_of_lift`, `pow_ne_one_of_lift`, `no_section_SL2` | the no-lift lemma, for every prime `p ≥ 5` | `propext`, `Classical.choice`, `Quot.sound` |
| `RequestProject/Seed/Exceptional.lean` | `primeFactors_2242`, `primeFactors_5844`, `exceptional_local_primes`, `torus_weight_nontrivial` | the arithmetic behind the exceptional set and the torus weight | `propext`, `Classical.choice`, `Quot.sound` |
| `RequestProject/Seed/EtaCheck.lean` | `eta_19`, `eta_59`, `eta_487`, `order_kills` | the local images at the auxiliary primes (`decide +kernel`) | same three; no `native_decide` |

`research_return/checks/eta_exceptional.py` is an independent Python recomputation of
`EtaCheck`, and it agrees.

**Not formalized.** Galois cohomology, Selmer groups, CFT, formal groups and Néron models are
not formalized. Theorems A–D are written proofs. They are therefore reported "in progress" in
the Properties table, not "proved".
