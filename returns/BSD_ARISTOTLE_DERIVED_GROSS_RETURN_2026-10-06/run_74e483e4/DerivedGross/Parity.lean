module

public import Mathlib

/-!
# Derived Gross identity over `ℚ(√−7)`: the algebra behind the obstruction

Lean source for `DERIVED_GROSS_RESULT.md`.  Every statement here is pure commutative algebra.
Nothing in this file is a statement about `Ш` of the seed curve, about `L`-values, or about the
existence of Gross points. The arithmetic inputs (Mazur–Tate functoriality under complex
conjugation, the functional equation of the theta element) enter only as explicit hypotheses.

Setting.  `R` is a commutative ring. The model case is the group ring `ℤ_p[G]`, where `G` is the
`p`-part of an anticyclotomic tame Galois group `Gal(K[ℓ]/K)`. `I ⊆ R` is the augmentation ideal,
and `ι : R →+* R` is the involution induced by complex conjugation, which acts on the
anticyclotomic group by inversion. `2` is a unit (`p` odd).

* `inv_add_mem_sq_of_span`, `GroupRing.inv_add_self_mem_sq` : `ι` acts as `−1` on `I/I²`.
* `theta_mem_sq_of_functional_equation` : an element of `I` with `ι θ = u θ`, `u ≡ 1 (mod I)`,
  lies in `I²`.
* `mul_star_mem_pow` : `θ ∈ I^k`, `θ* ∈ I^k` give `θ θ* ∈ I^(2k)`.
* `pairing_mem_sq_of_fixed` : a pairing with values in `I` that is `ι`-equivariant modulo `I²`
  takes values in `I²` on `τ`-fixed points (this is `E(ℚ) = E(K)^+`).
* `det_two_mem_cube` : the `2 × 2` determinant of such a pairing on two fixed points lies in
  `I³` (in fact in `I⁴`), i.e. its class in `I²/I³` is zero.
* `degree_two_identity_iff`, `degree_two_identity_iff_vanishing`,
  `GroupRing.degree_two_identity_iff_vanishing` : hence the candidate identity
  `Θ ≡ m·det (mod I³)` holds for one `m` iff it holds for every `m` iff `Θ ∈ I³`.
* `invol_sub_mem_cube` : `ι` acts as `+1` on `I²/I³`.
* `one_add_pow_mem_cube`, `theta_expansion_mod_cube` : the degree-two coefficient of
  `θ = Σ φ_i γ^{a_i}` is the binomial moment `Σ φ_i C(a_i, 2)`.
-/

@[expose] public section

namespace DerivedGross

open Ideal

variable {R : Type*} [CommRing R]

/-- If `x + x ∈ I²` and `2` is a unit, then `x ∈ I²`. -/
theorem mem_sq_of_two_mul_mem {I : Ideal R} (h2 : IsUnit (2 : R)) {x : R}
    (hxx : x + x ∈ I ^ 2) : x ∈ I ^ 2 := by
  obtain ⟨u, hu⟩ := h2
  have h : (2 : R) * x ∈ I ^ 2 := by rw [two_mul]; exact hxx
  have : (↑u⁻¹ : R) * ((2 : R) * x) ∈ I ^ 2 := Ideal.mul_mem_left _ _ h
  rwa [← hu, ← mul_assoc, Units.inv_mul, one_mul] at this

/-- **`ι` acts as `−1` on `I/I²`, abstract form.**  Let `I = span S`, assume `r − ι r ∈ I` for all
`r` and `ι s + s ∈ I²` on the generators.  Then `ι x + x ∈ I²` for every `x ∈ I`. -/
theorem inv_add_mem_sq_of_span (ι : R →+* R) (S : Set R) (I : Ideal R) (hI : I = Ideal.span S)
    (hdiff : ∀ r, r - ι r ∈ I) (hgen : ∀ s ∈ S, ι s + s ∈ I ^ 2) :
    ∀ x ∈ I, ι x + x ∈ I ^ 2 := by
  intro x hx
  rw [hI] at hx
  induction hx using Submodule.span_induction with
  | mem s hs => exact hgen s hs
  | zero => simp
  | add a b _ _ ha hb =>
      have : ι (a + b) + (a + b) = (ι a + a) + (ι b + b) := by rw [map_add]; ring
      rw [this]; exact Ideal.add_mem _ ha hb
  | smul r a ha' ha =>
      have hmem : a ∈ I := by rw [hI]; exact ha'
      have : ι (r • a) + r • a = ι r * (ι a + a) + (r - ι r) * a := by
        rw [smul_eq_mul, map_mul]; ring
      rw [this]
      refine Ideal.add_mem _ (Ideal.mul_mem_left _ _ ha) ?_
      rw [pow_two]; exact Ideal.mul_mem_mul (hdiff r) hmem

/-- **An `ι`-invariant class in `I/I²` vanishes.**  If `θ ∈ I` and `ι θ = u·θ` with `u ≡ 1 (mod I)`
(`u` a group element, as in the functional equation of a theta element with sign `+`), and `ι`
acts as `−1` on `I/I²`, then `θ ∈ I²`. -/
theorem theta_mem_sq_of_functional_equation (ι : R →+* R) (I : Ideal R) (h2 : IsUnit (2 : R))
    (hanti : ∀ x ∈ I, ι x + x ∈ I ^ 2) {θ u : R} (hθ : θ ∈ I) (hu : u - 1 ∈ I)
    (hfe : ι θ = u * θ) : θ ∈ I ^ 2 := by
  apply mem_sq_of_two_mul_mem h2
  have h1 := hanti θ hθ
  have h2' : (u - 1) * θ ∈ I ^ 2 := by rw [pow_two]; exact Ideal.mul_mem_mul hu hθ
  have : θ + θ = (ι θ + θ) - (u - 1) * θ := by rw [hfe]; ring
  rw [this]; exact Ideal.sub_mem _ h1 h2'

/-- If `θ ∈ I^k` and `θ* ∈ I^k` then `θ·θ* ∈ I^(2k)`.  So `θ·θ*` can have a nonzero class in
`I²/I³` only if `θ ∉ I²`. -/
theorem mul_star_mem_pow (I : Ideal R) {θ θs : R} {k : ℕ} (hθ : θ ∈ I ^ k) (hθs : θs ∈ I ^ k) :
    θ * θs ∈ I ^ (2 * k) := by
  rw [two_mul, pow_add]; exact Ideal.mul_mem_mul hθ hθs

/-- **Parity vanishing of the first-order pairing on fixed points.**  Let `h` be a biadditive
pairing with values in `I`, equivariant modulo `I²` for an involution `τ` of `M` and the
involution `ι` of `R` (`h (τ x) (τ y) ≡ ι (h x y)`), with `ι` acting as `−1` on `I/I²`.  Then on
`τ`-fixed points `h` takes values in `I²`. -/
theorem pairing_mem_sq_of_fixed {M : Type*} [AddCommGroup M] (h : M →+ M →+ R) (τ : M →+ M)
    (ι : R →+* R) (I : Ideal R) (h2 : IsUnit (2 : R)) (hval : ∀ x y, h x y ∈ I)
    (hequiv : ∀ x y, h (τ x) (τ y) - ι (h x y) ∈ I ^ 2)
    (hanti : ∀ x ∈ I, ι x + x ∈ I ^ 2) {x y : M} (hx : τ x = x) (hy : τ y = y) :
    h x y ∈ I ^ 2 := by
  apply mem_sq_of_two_mul_mem h2
  have e := hequiv x y
  rw [hx, hy] at e
  have a := hanti _ (hval x y)
  have : h x y + h x y = (h x y - ι (h x y)) + (ι (h x y) + h x y) := by ring
  rw [this]; exact Ideal.add_mem _ e a

/-- A `2 × 2` determinant whose entries lie in `I²` lies in `I³` (indeed in `I⁴`). -/
theorem det_two_mem_cube_of_entries (I : Ideal R) (H : Matrix (Fin 2) (Fin 2) R)
    (hH : ∀ i j, H i j ∈ I ^ 2) : H.det ∈ I ^ 3 := by
  have h4 : H.det ∈ I ^ (2 + 2) := by
    rw [Matrix.det_fin_two, pow_add]
    exact Ideal.sub_mem _ (Ideal.mul_mem_mul (hH 0 0) (hH 1 1))
      (Ideal.mul_mem_mul (hH 0 1) (hH 1 0))
  exact Ideal.pow_le_pow_right (by norm_num) h4

/-- **The determinant of the first-order pairing on `E(ℚ) = E(K)^+` is zero in `I²/I³`.** -/
theorem det_two_mem_cube {M : Type*} [AddCommGroup M] (h : M →+ M →+ R) (τ : M →+ M)
    (ι : R →+* R) (I : Ideal R) (h2 : IsUnit (2 : R)) (hval : ∀ x y, h x y ∈ I)
    (hequiv : ∀ x y, h (τ x) (τ y) - ι (h x y) ∈ I ^ 2)
    (hanti : ∀ x ∈ I, ι x + x ∈ I ^ 2) (P : Fin 2 → M) (hP : ∀ i, τ (P i) = P i) :
    (Matrix.of fun i j => h (P i) (P j)).det ∈ I ^ 3 :=
  det_two_mem_cube_of_entries I _ fun i j =>
    pairing_mem_sq_of_fixed h τ ι I h2 hval hequiv hanti (hP i) (hP j)

/-- **The candidate identity determines nothing.**  If `d ∈ I³`, then "`Θ ≡ m·d (mod I³)` for
some `m`", "for every `m`" and "`Θ ∈ I³`" are equivalent.  So an identity
`Θ^{(2)} = m_E · det` with such a determinant is either false or holds for every `m_E`. -/
theorem degree_two_identity_iff (I : Ideal R) {Θ d : R} (hd : d ∈ I ^ 3) :
    ((∃ m : R, Θ - m * d ∈ I ^ 3) ↔ Θ ∈ I ^ 3) ∧
      ((∀ m : R, Θ - m * d ∈ I ^ 3) ↔ Θ ∈ I ^ 3) := by
  have key : ∀ m : R, Θ - m * d ∈ I ^ 3 ↔ Θ ∈ I ^ 3 := fun m => by
    have hmd : m * d ∈ I ^ 3 := Ideal.mul_mem_left _ _ hd
    constructor
    · intro h; simpa using Ideal.add_mem _ h hmd
    · intro h; exact Ideal.sub_mem _ h hmd
  exact ⟨⟨fun ⟨m, hm⟩ => (key m).1 hm, fun h => ⟨0, (key 0).2 h⟩⟩,
    ⟨fun h => (key 0).1 (h 0), fun h m => (key m).2 h⟩⟩

/-- Combined statement: for the anticyclotomic first-order pairing on two `τ`-fixed points, the
degree-two identity with constant `m` is equivalent to `Θ ∈ I³`, for every `m`. -/
theorem degree_two_identity_iff_vanishing {M : Type*} [AddCommGroup M] (h : M →+ M →+ R)
    (τ : M →+ M) (ι : R →+* R) (I : Ideal R) (h2 : IsUnit (2 : R)) (hval : ∀ x y, h x y ∈ I)
    (hequiv : ∀ x y, h (τ x) (τ y) - ι (h x y) ∈ I ^ 2)
    (hanti : ∀ x ∈ I, ι x + x ∈ I ^ 2) (P : Fin 2 → M) (hP : ∀ i, τ (P i) = P i) (Θ m : R) :
    Θ - m * (Matrix.of fun i j => h (P i) (P j)).det ∈ I ^ 3 ↔ Θ ∈ I ^ 3 := by
  have hd := det_two_mem_cube h τ ι I h2 hval hequiv hanti P hP
  have hmd := Ideal.mul_mem_left _ m hd
  constructor
  · intro hx; simpa using Ideal.add_mem _ hx hmd
  · intro hx; exact Ideal.sub_mem _ hx hmd

/-- **`ι` acts as `+1` on `I²/I³`.**  If `ι` acts as `−1` on `I/I²`, then `ι x − x ∈ I³` for every
`x ∈ I²`.  (So on `I²/I³` the involution, and hence the choice of `λ` versus `λ̄` for a split
`ℓ = λ λ̄`, is invisible.) -/
theorem invol_sub_mem_cube (ι : R →+* R) (I : Ideal R) (hanti : ∀ x ∈ I, ι x + x ∈ I ^ 2) :
    ∀ x ∈ I ^ 2, ι x - x ∈ I ^ 3 := by
  have hI : ∀ a ∈ I, ι a ∈ I := fun a ha => by
    have h1 : ι a + a ∈ I := Ideal.pow_le_self (by norm_num) (hanti a ha)
    simpa using Ideal.sub_mem _ h1 ha
  intro x hx
  rw [pow_two] at hx
  refine Submodule.mul_induction_on (C := fun z => ι z - z ∈ I ^ 3) hx ?_ ?_
  · intro a ha b hb
    have e : ι (a * b) - a * b = (ι a + a) * ι b - a * (ι b + b) := by rw [map_mul]; ring
    show ι (a * b) - a * b ∈ I ^ 3
    rw [e]
    have h3 : (3 : ℕ) = 2 + 1 := rfl
    refine Ideal.sub_mem _ ?_ ?_
    · rw [h3, pow_add, pow_one]; exact Ideal.mul_mem_mul (hanti a ha) (hI b hb)
    · rw [h3, add_comm, pow_add, pow_one]; exact Ideal.mul_mem_mul ha (hanti b hb)
  · intro a b ha hb
    have e : ι (a + b) - (a + b) = (ι a - a) + (ι b - b) := by rw [map_add]; ring
    show ι (a + b) - (a + b) ∈ I ^ 3
    rw [e]; exact Ideal.add_mem _ ha hb

/-- **Binomial expansion to second order.**  For `y ∈ J`,
`(1 + y)^a ≡ 1 + a·y + C(a,2)·y² (mod J³)`. -/
theorem one_add_pow_mem_cube (J : Ideal R) {y : R} (hy : y ∈ J) (a : ℕ) :
    (1 + y) ^ a - (1 + (a : R) * y + (a.choose 2 : R) * y ^ 2) ∈ J ^ 3 := by
  induction a with
  | zero => simp
  | succ a ih =>
      have hy3 : y ^ 3 ∈ J ^ 3 := Ideal.pow_mem_pow hy 3
      have hc : ((a + 1).choose 2 : R) = (a.choose 2 : R) + a := by
        rw [Nat.choose_succ_succ, Nat.choose_one_right]; push_cast; ring
      have e : (1 + y) ^ (a + 1) - (1 + ((a + 1 : ℕ) : R) * y + ((a + 1).choose 2 : R) * y ^ 2) =
          ((1 + y) ^ a - (1 + (a : R) * y + (a.choose 2 : R) * y ^ 2)) * (1 + y) +
            (a.choose 2 : R) * y ^ 3 := by
        rw [hc]; push_cast; ring
      rw [e]
      exact Ideal.add_mem _ (Ideal.mul_mem_right _ _ ih) (Ideal.mul_mem_left _ _ hy3)

/-- **The degree-two coefficient of a theta element as a binomial moment.**  If
`θ = Σ_i φ_i γ^{a_i}` with `γ = 1 + y`, `y ∈ J`, then
`θ ≡ Σ φ_i + (Σ φ_i a_i)·y + (Σ φ_i C(a_i,2))·y² (mod J³)`. -/
theorem theta_expansion_mod_cube {ι : Type*} (s : Finset ι) (J : Ideal R) {y : R} (hy : y ∈ J)
    (φ : ι → R) (a : ι → ℕ) :
    (∑ i ∈ s, φ i * (1 + y) ^ a i) -
      ((∑ i ∈ s, φ i) + (∑ i ∈ s, φ i * (a i : R)) * y +
        (∑ i ∈ s, φ i * ((a i).choose 2 : R)) * y ^ 2) ∈ J ^ 3 := by
  have e : (∑ i ∈ s, φ i * (1 + y) ^ a i) -
      ((∑ i ∈ s, φ i) + (∑ i ∈ s, φ i * (a i : R)) * y +
        (∑ i ∈ s, φ i * ((a i).choose 2 : R)) * y ^ 2) =
      ∑ i ∈ s, φ i * ((1 + y) ^ a i - (1 + (a i : R) * y + ((a i).choose 2 : R) * y ^ 2)) := by
    simp only [Finset.sum_mul, ← Finset.sum_add_distrib, ← Finset.sum_sub_distrib]
    refine Finset.sum_congr rfl fun i _ => ?_
    ring
  rw [e]
  exact Ideal.sum_mem _ fun i _ => Ideal.mul_mem_left _ _ (one_add_pow_mem_cube J hy (a i))

namespace GroupRing

variable (k : Type*) [CommRing k] (G : Type*) [CommGroup G]

/-- The augmentation ideal of `k[G]`, as the span of the elements `g − 1`. -/
noncomputable def augIdeal : Ideal (MonoidAlgebra k G) :=
  Ideal.span (Set.range fun g : G => MonoidAlgebra.single g (1 : k) - 1)

/-- The involution of `k[G]` induced by inversion on `G` (complex conjugation on an
anticyclotomic group). -/
noncomputable def invol : MonoidAlgebra k G →+* MonoidAlgebra k G :=
  MonoidAlgebra.mapDomainRingHom k (invMonoidHom : G →* G)

variable {k G}

theorem invol_single (g : G) (c : k) :
    invol k G (MonoidAlgebra.single g c) = MonoidAlgebra.single g⁻¹ c := by
  simp [invol, MonoidAlgebra.mapDomainRingHom_apply]

theorem single_sub_one_mem (g : G) : MonoidAlgebra.single g (1 : k) - 1 ∈ augIdeal k G :=
  Ideal.subset_span ⟨g, rfl⟩

theorem sub_invol_mem (r : MonoidAlgebra k G) : r - invol k G r ∈ augIdeal k G := by
  induction r using MonoidAlgebra.induction_linear with
  | zero => simp
  | add x y hx hy =>
      have : x + y - invol k G (x + y) = (x - invol k G x) + (y - invol k G y) := by
        rw [map_add]; ring
      rw [this]; exact Ideal.add_mem _ hx hy
  | single g c =>
      rw [invol_single]
      have e : MonoidAlgebra.single g c - MonoidAlgebra.single g⁻¹ c =
          MonoidAlgebra.single 1 c * ((MonoidAlgebra.single g 1 - 1) -
            (MonoidAlgebra.single g⁻¹ 1 - 1)) := by
        rw [mul_sub, mul_sub, mul_sub, MonoidAlgebra.single_mul_single,
          MonoidAlgebra.single_mul_single]
        simp
      rw [e]
      exact Ideal.mul_mem_left _ _ (Ideal.sub_mem _ (single_sub_one_mem g)
        (single_sub_one_mem g⁻¹))

/-- **In `k[G]` with inversion, the involution acts as `−1` on `I/I²`.** -/
theorem inv_add_self_mem_sq (x : MonoidAlgebra k G) (hx : x ∈ augIdeal k G) :
    invol k G x + x ∈ augIdeal k G ^ 2 := by
  refine inv_add_mem_sq_of_span (invol k G) _ (augIdeal k G) rfl sub_invol_mem ?_ x hx
  rintro s ⟨g, rfl⟩
  have e : invol k G (MonoidAlgebra.single g 1 - 1) + (MonoidAlgebra.single g 1 - 1) =
      -((MonoidAlgebra.single g (1 : k) - 1) * (MonoidAlgebra.single g⁻¹ 1 - 1)) := by
    rw [map_sub, map_one, invol_single, sub_mul, mul_sub, mul_sub,
      MonoidAlgebra.single_mul_single]
    simp only [mul_inv_cancel, mul_one, one_mul]
    rw [show (MonoidAlgebra.single (1 : G) (1 : k)) = 1 from rfl]
    ring
  rw [e, pow_two]
  exact neg_mem (Ideal.mul_mem_mul (single_sub_one_mem g)
    (single_sub_one_mem g⁻¹))

/-- **Group-ring form of the obstruction.**  In `k[G]` (`G` commutative, `2` invertible), for any
biadditive pairing `h` with values in the augmentation ideal that is equivariant modulo `I²` for an
involution `τ` and inversion on `G`, and any two `τ`-fixed points, the identity
`Θ ≡ m · det (h (P i) (P j)) (mod I³)` is equivalent to `Θ ∈ I³`, whatever `m` is. -/
theorem degree_two_identity_iff_vanishing {M : Type*} [AddCommGroup M]
    (h2 : IsUnit (2 : MonoidAlgebra k G)) (h : M →+ M →+ MonoidAlgebra k G) (τ : M →+ M)
    (hval : ∀ x y, h x y ∈ augIdeal k G)
    (hequiv : ∀ x y, h (τ x) (τ y) - invol k G (h x y) ∈ augIdeal k G ^ 2)
    (P : Fin 2 → M) (hP : ∀ i, τ (P i) = P i) (Θ m : MonoidAlgebra k G) :
    Θ - m * (Matrix.of fun i j => h (P i) (P j)).det ∈ augIdeal k G ^ 3 ↔
      Θ ∈ augIdeal k G ^ 3 :=
  DerivedGross.degree_two_identity_iff_vanishing h τ (invol k G) (augIdeal k G) h2 hval hequiv
    inv_add_self_mem_sq P hP Θ m

end GroupRing

end DerivedGross
