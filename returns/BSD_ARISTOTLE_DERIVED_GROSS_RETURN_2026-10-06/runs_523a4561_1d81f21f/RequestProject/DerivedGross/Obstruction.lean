module

public import Mathlib

/-!
# Degree-two analysis of the definite theta element over `ℚ(√−7)`

Lean companion of `DERIVED_GROSS_RESULT.md`. Everything about the curve, the Gross points, the
Gross–Waldspurger formula and the Mazur–Tate pairing enters as an explicit hypothesis; nothing
here is a statement about `Ш` of the seed.

* `mem_augIdeal_sq_of_functional_eq`: in `R[G]` with `2` invertible, an element `θ` of the
  augmentation ideal `I` with `θ* = σ·θ` (`*` induced by `g ↦ g⁻¹`, `σ ∈ G`) lies in `I²`.
  This is why the first possibly nonzero coefficient of the definite theta element is in `I²/I³`.
* `pairing_vanishes_on_fixed`, `gram_det_eq_zero_of_anti`: a pairing that is anti-invariant
  under an involution (as the anticyclotomic Mazur–Tate pairing is under complex conjugation)
  vanishes on fixed vectors once `2` is invertible, so its Gram determinant on `E(ℚ) = E(K)⁺`
  is zero.
* `sq_tmul_sign_invariant`: `(−a) ⊗ (−a) = a ⊗ a`; the identification of the degree-two pieces of
  the anticyclotomic and cyclotomic groups does not depend on the choice of prime above `ℓ`.
* `augmentation_vanishes`, `degenerate_identity_forces_zero`,
  `ordinary_bad_primes_finite_of_identity`: the bookkeeping consequences used in the return.
-/

@[expose] public section

namespace DerivedGross

open MonoidAlgebra

variable {R G : Type*} [CommRing R] [CommGroup G]

/-- The augmentation `R[G] → R`, `g ↦ 1`. -/
noncomputable def aug (R G : Type*) [CommRing R] [CommGroup G] : MonoidAlgebra R G →ₐ[R] R :=
  MonoidAlgebra.lift R R G 1

/-- The augmentation ideal `I = ker(aug)`. -/
noncomputable def augIdeal (R G : Type*) [CommRing R] [CommGroup G] :
    Ideal (MonoidAlgebra R G) :=
  RingHom.ker (aug R G).toRingHom

/-- The involution `θ ↦ θ*` induced by `g ↦ g⁻¹`. -/
noncomputable def invol (R G : Type*) [CommRing R] [CommGroup G] :
    MonoidAlgebra R G →+* MonoidAlgebra R G :=
  MonoidAlgebra.mapDomainRingHom R (invMonoidHom : G →* G)

lemma aug_of (g : G) : aug R G (of R G g) = 1 := by
  simp [aug]

lemma of_sub_one_mem (g : G) : of R G g - 1 ∈ augIdeal R G := by
  simp only [augIdeal, RingHom.mem_ker, AlgHom.toRingHom_eq_coe, RingHom.coe_coe, map_sub,
    aug_of, map_one, sub_self]

lemma invol_of (g : G) : invol R G (of R G g) = of R G g⁻¹ := by
  simp [invol, MonoidAlgebra.mapDomainRingHom_apply, of_apply]

/-- `x + x* − 2·aug(x) ∈ I²` for every `x` (from `g + g⁻¹ − 2 = −(g − 1)(g⁻¹ − 1)`). -/
lemma add_invol_sub_mem_sq (x : MonoidAlgebra R G) :
    x + invol R G x - algebraMap R (MonoidAlgebra R G) (2 * aug R G x) ∈ augIdeal R G ^ 2 := by
  induction x using MonoidAlgebra.induction_on with
  | hM g =>
    have h : of R G g + invol R G (of R G g) -
        algebraMap R (MonoidAlgebra R G) (2 * aug R G (of R G g)) =
        -((of R G g - 1) * (of R G g⁻¹ - 1)) := by
      rw [invol_of, aug_of]
      have : of R G g * of R G g⁻¹ = 1 := by
        rw [← map_mul, mul_inv_cancel, map_one]
      simp only [mul_one, map_ofNat]
      linear_combination this
    rw [h, sq]
    exact (Ideal.neg_mem_iff _).mpr (Ideal.mul_mem_mul (of_sub_one_mem g) (of_sub_one_mem _))
  | hadd x y hx hy =>
    have := Ideal.add_mem _ hx hy
    convert this using 1
    simp only [map_add, mul_add]
    ring
  | hsmul r x hx =>
    have := Ideal.mul_mem_left _ (algebraMap R (MonoidAlgebra R G) r) hx
    convert this using 1
    have hi : invol R G (r • x) = algebraMap R (MonoidAlgebra R G) r * invol R G x := by
      rw [Algebra.smul_def, map_mul]
      congr 1
      simp [invol, MonoidAlgebra.coe_algebraMap, MonoidAlgebra.mapDomainRingHom_apply]
    rw [hi, map_smul, smul_eq_mul, Algebra.smul_def]
    simp only [map_mul]
    ring

/-- **Degree one vanishes under a `+` functional equation.** If `2` is invertible, `θ ∈ I` and
`θ* = σ·θ` for some `σ ∈ G`, then `θ ∈ I²`. -/
theorem mem_augIdeal_sq_of_functional_eq [Invertible (2 : R)] (θ : MonoidAlgebra R G) (σ : G)
    (hθ : θ ∈ augIdeal R G) (hfe : invol R G θ = of R G σ * θ) :
    θ ∈ augIdeal R G ^ 2 := by
  have h0 : aug R G θ = 0 := by simpa [augIdeal, RingHom.mem_ker] using hθ
  have h1 := add_invol_sub_mem_sq θ
  rw [h0, mul_zero, map_zero, sub_zero, hfe] at h1
  have h2 : (of R G σ - 1) * θ ∈ augIdeal R G ^ 2 := by
    rw [sq]; exact Ideal.mul_mem_mul (of_sub_one_mem σ) hθ
  have h3 : (2 : MonoidAlgebra R G) * θ ∈ augIdeal R G ^ 2 := by
    have := Ideal.sub_mem _ h1 h2
    convert this using 1; ring
  have h4 := Ideal.mul_mem_left _ (algebraMap R (MonoidAlgebra R G) (⅟2)) h3
  convert h4 using 1
  rw [← mul_assoc, show (2 : MonoidAlgebra R G) = algebraMap R _ 2 from (map_ofNat _ 2).symm, ← map_mul,
    invOf_mul_self, map_one, one_mul]

/-- **Anti-invariant pairings vanish on fixed vectors.** If `H(τx, τy) = −H(x, y)` and `2` is
invertible in the scalars, then `H(x, y) = 0` whenever `τx = x` and `τy = y`. -/
theorem pairing_vanishes_on_fixed {V M : Type*} [AddCommGroup V] [Module R V] [AddCommGroup M]
    [Module R M] [Invertible (2 : R)] (H : V →ₗ[R] V →ₗ[R] M) (τ : V → V)
    (hanti : ∀ x y, H (τ x) (τ y) = -H x y) {x y : V} (hx : τ x = x) (hy : τ y = y) :
    H x y = 0 := by
  have h := hanti x y
  rw [hx, hy] at h
  have h2 : (2 : R) • H x y = 0 := by
    rw [two_smul]; nth_rewrite 1 [h]; exact neg_add_cancel _
  have := congrArg (fun z => (⅟2 : R) • z) h2
  simpa [smul_smul] using this

/-- The Gram determinant of an anti-invariant pairing on any family of fixed vectors is zero. -/
theorem gram_det_eq_zero_of_anti {V A : Type*} [AddCommGroup V] [Module R V] [CommRing A]
    [Algebra R A] [Invertible (2 : R)] {n : ℕ} (H : V →ₗ[R] V →ₗ[R] A) (τ : V → V)
    (hanti : ∀ x y, H (τ x) (τ y) = -H x y) (P : Fin (n + 1) → V) (hP : ∀ i, τ (P i) = P i) :
    (Matrix.of fun i j => H (P i) (P j)).det = 0 := by
  have hz : (Matrix.of fun i j => H (P i) (P j)) = 0 := by
    ext i j
    exact pairing_vanishes_on_fixed H τ hanti (hP i) (hP j)
  rw [hz, Matrix.det_zero ⟨0⟩]

/-- The square class `a ⊗ a` is unchanged by `a ↦ −a`, so the identification of degree-two pieces
does not depend on which prime above a split `ℓ` is used. -/
theorem sq_tmul_sign_invariant {A : Type*} [AddCommGroup A] [Module R A] (a : A) :
    ((-a) ⊗ₜ[R] (-a) : TensorProduct R A A) = a ⊗ₜ[R] a := by
  rw [TensorProduct.neg_tmul, TensorProduct.tmul_neg, neg_neg]

/-- **The trivial-character coefficient and the augmentation.** If the Gross–Waldspurger formula
reads `κ·θ₁² = L(E/K,1)` with `κ ≠ 0`, and `L(E/K,1) = 0`, then `θ₁ = 0`; the distribution relation
`aug(θ_ℓ) = c_ℓ·θ₁` then gives `aug(θ_ℓ) = 0` for every auxiliary `ℓ`. -/
theorem augmentation_vanishes (θ₁ : ℤ) (κ Lval : ℝ) (hκ : κ ≠ 0)
    (hGW : κ * (θ₁ : ℝ) ^ 2 = Lval) (hL : Lval = 0) (augθ c : ℤ) (hdist : augθ = c * θ₁) :
    θ₁ = 0 ∧ augθ = 0 := by
  have : (θ₁ : ℝ) ^ 2 = 0 := by
    rcases mul_eq_zero.mp (hGW.trans hL) with h | h
    · exact absurd h hκ
    · exact h
  have hθ : θ₁ = 0 := by exact_mod_cast pow_eq_zero_iff (n := 2) (by norm_num) |>.mp this
  exact ⟨hθ, by rw [hdist, hθ, mul_zero]⟩

/-- **A degenerate identity carries no information.** If `θ₂ = m·D` with `D = 0` (the Gram
determinant of the anticyclotomic pairing on `E(ℚ)`), then `θ₂ = 0`; in particular such an
identity is refuted by a single nonzero degree-two coefficient. -/
theorem degenerate_identity_forces_zero {A : Type*} [CommRing A] (θ₂ m D : A)
    (hid : θ₂ = m * D) (hD : D = 0) : θ₂ = 0 := by
  rw [hid, hD, mul_zero]

/-- **What the cyclotomic candidate identity would give.** Suppose, for every prime `p` outside a
finite set `S`, and every auxiliary `ℓ`, `b·θ₂(p,ℓ) = a·D(p,ℓ)` in `ZMod p` (the candidate identity
with `m_E = a/b`); suppose some `ℓ` has `D(p,ℓ) ≠ 0` (the role of G2), and that a nonzero
`θ₂(p,ℓ)` at a good ordinary `p ∉ S` forces `Ш[p^∞] = 0` (the per-prime detector). Then the good
ordinary primes with `Ш[p^∞] ≠ 0` are finite: they lie in `S` or divide `a`. -/
theorem ordinary_bad_primes_finite_of_identity (S : Finset ℕ) (a b : ℤ) (ha : a ≠ 0)
    (Ord ShaZero : ℕ → Prop) (θ₂ D : (p : ℕ) → ℕ → ZMod p)
    (hid : ∀ p, p.Prime → p ∉ S → ∀ ℓ, (b : ZMod p) * θ₂ p ℓ = (a : ZMod p) * D p ℓ)
    (hG2 : ∀ p, p.Prime → p ∉ S → ∃ ℓ, D p ℓ ≠ 0)
    (hdet : ∀ p, p.Prime → p ∉ S → Ord p → (∃ ℓ, θ₂ p ℓ ≠ 0) → ShaZero p) :
    {p | p.Prime ∧ Ord p ∧ ¬ ShaZero p} ⊆ (S : Set ℕ) ∪ (a.natAbs.primeFactors : Set ℕ) ∧
      {p | p.Prime ∧ Ord p ∧ ¬ ShaZero p}.Finite := by
  have hsub : {p | p.Prime ∧ Ord p ∧ ¬ ShaZero p} ⊆
      (S : Set ℕ) ∪ (a.natAbs.primeFactors : Set ℕ) := by
    rintro p ⟨hp, hord, hbad⟩
    by_cases hS : p ∈ S
    · exact Or.inl hS
    right
    simp only [Finset.mem_coe, Nat.mem_primeFactors]
    refine ⟨hp, ?_, Int.natAbs_ne_zero.mpr ha⟩
    haveI := Fact.mk hp
    by_contra hpa
    have haz : (a : ZMod p) ≠ 0 := by
      rw [Ne, ZMod.intCast_zmod_eq_zero_iff_dvd]
      exact fun h => hpa (Int.natCast_dvd.mp h)
    obtain ⟨ℓ, hℓ⟩ := hG2 p hp hS
    have hne : θ₂ p ℓ ≠ 0 := by
      intro h0
      have := hid p hp hS ℓ
      rw [h0, mul_zero] at this
      exact (mul_ne_zero haz hℓ) this.symm
    exact hbad (hdet p hp hS hord ⟨ℓ, hne⟩)
  exact ⟨hsub, ((Finset.finite_toSet _).union (Finset.finite_toSet _)).subset hsub⟩

end DerivedGross
