import WitnessContent.Spec

/-!
# A1 — group-ring helpers (Lemma A and the graded pieces)

Helper lemmas for the targets T1 (`lemmaA_comm`), T2 (`gr_killed_by_exponent`),
T3 (`gr_p_primary`), T4 (`bridge_517`) and T4b (`cls2_zero_iff`).

Nothing in this file is frozen; the frozen statements live in `Spec.lean`.
-/

namespace WitnessContent

open scoped BigOperators

section CommRingAux

variable {A : Type*} [CommRing A]

/-- Binomial expansion, truncated after the linear term: `(1 + x) ^ n = 1 + n • x + z`
with `z` a multiple of `x * x`. -/
lemma one_add_pow_eq_linear_add (x : A) (n : ℕ) :
    ∃ z ∈ Ideal.span ({x * x} : Set A), (1 + x) ^ n = 1 + n • x + z := by
  induction n with
  | zero => exact ⟨0, Submodule.zero_mem _, by simp⟩
  | succ n ih =>
      obtain ⟨z, hz, hzn⟩ := ih
      refine ⟨n • (x * x) + z + z * x, ?_, ?_⟩
      · exact Submodule.add_mem _
          (Submodule.add_mem _ (nsmul_mem (Ideal.mem_span_singleton_self _) n) hz)
          (Ideal.mul_mem_right _ _ hz)
      · rw [pow_succ, hzn]
        simp only [succ_nsmul, nsmul_eq_mul]
        ring

end CommRingAux

section Aug

variable {R : Type*} [CommRing R] {G : Type*} [CommGroup G]

lemma augHom_apply (f : MonoidAlgebra R G) : augHom R G f = ∑ g ∈ f.support, f g := by
  classical
  simp [augHom, MonoidAlgebra.lift_apply, Finsupp.sum]

lemma mem_augIdeal_iff (f : MonoidAlgebra R G) :
    f ∈ augIdeal R G ↔ ∑ g ∈ f.support, f g = 0 := by
  rw [augIdeal, RingHom.mem_ker, ← augHom_apply]

lemma of_sub_one_mem_augIdeal (g : G) :
    (MonoidAlgebra.of R G g - 1) ∈ augIdeal R G := by
  simp [augIdeal, RingHom.mem_ker, augHom]

/-- An element of the augmentation ideal is the `R`-combination `∑ f g • (g - 1)`. -/
lemma augIdeal_repr (f : MonoidAlgebra R G) (hf : f ∈ augIdeal R G) :
    f = ∑ g ∈ f.support, f g • (MonoidAlgebra.of R G g - 1) := by
  classical
  have hsum : ∑ g ∈ f.support, f g = 0 := (mem_augIdeal_iff f).1 hf
  have h1 : ∑ g ∈ f.support, f g • (MonoidAlgebra.of R G g - 1)
      = (∑ g ∈ f.support, f g • MonoidAlgebra.of R G g)
        - (∑ g ∈ f.support, f g) • (1 : MonoidAlgebra R G) := by
    rw [Finset.sum_smul, ← Finset.sum_sub_distrib]
    exact Finset.sum_congr rfl fun g _ => by rw [smul_sub]
  have h2 : ∑ g ∈ f.support, f g • MonoidAlgebra.of R G g = f := by
    have hcongr : ∀ g ∈ f.support, f g • MonoidAlgebra.of R G g = Finsupp.single g (f g) := by
      intro g _
      simp [MonoidAlgebra.of_apply]
    rw [Finset.sum_congr rfl hcongr]
    exact Finsupp.sum_single f
  rw [h1, h2, hsum, zero_smul, sub_zero]

/-- An `R`-multiple of an element of an ideal of `MonoidAlgebra R G` stays in the ideal. -/
lemma smul_mem_ideal_of_mem (J : Ideal (MonoidAlgebra R G)) (r : R) {w : MonoidAlgebra R G}
    (hw : w ∈ J) : r • w ∈ J := by
  rw [Algebra.smul_def]
  exact Ideal.mul_mem_left _ _ hw

/-- The key step of Lemma A: `e • I ⊆ I²` when every `g : G` satisfies `g ^ e = 1`. -/
lemma nsmul_augIdeal_le_sq (e : ℕ) (he : ∀ g : G, g ^ e = 1) (x : MonoidAlgebra R G)
    (hx : x ∈ augIdeal R G) : e • x ∈ (augIdeal R G) ^ 2 := by
  classical
  have hgen : ∀ g : G, e • (MonoidAlgebra.of R G g - 1) ∈ (augIdeal R G) ^ 2 := by
    intro g
    set y : MonoidAlgebra R G := MonoidAlgebra.of R G g - 1 with hy
    have hyI : y ∈ augIdeal R G := of_sub_one_mem_augIdeal g
    obtain ⟨z, hz, hze⟩ := one_add_pow_eq_linear_add y e
    have h1 : (1 : MonoidAlgebra R G) + y = MonoidAlgebra.of R G g := by
      rw [hy]; ring
    have h2 : ((1 : MonoidAlgebra R G) + y) ^ e = 1 := by
      rw [h1, ← map_pow, he g, map_one]
    have hspan : Ideal.span ({y * y} : Set (MonoidAlgebra R G)) ≤ (augIdeal R G) ^ 2 := by
      rw [Ideal.span_le, Set.singleton_subset_iff, sq]
      exact Ideal.mul_mem_mul hyI hyI
    have hzI : z ∈ (augIdeal R G) ^ 2 := hspan hz
    have hzz : e • y = -z := by
      have h := hze
      rw [h2] at h
      have hz0 : e • y + z = 0 := by
        have hcanc : (1 : MonoidAlgebra R G) + (e • y + z) = 1 + 0 := by
          rw [← add_assoc, add_zero]; exact h.symm
        exact add_left_cancel hcanc
      exact eq_neg_of_add_eq_zero_left hz0
    rw [hzz]
    exact Submodule.neg_mem _ hzI
  rw [augIdeal_repr x hx, Finset.smul_sum]
  refine Submodule.sum_mem _ fun g _ => ?_
  rw [smul_comm]
  exact smul_mem_ideal_of_mem _ _ (hgen g)

/-- Lemma A (commutative case): `e • I^r ⊆ I^(r+1)` for `r ≥ 1`. -/
lemma nsmul_augIdeal_pow (e : ℕ) (he : ∀ g : G, g ^ e = 1) :
    ∀ r : ℕ, 1 ≤ r → ∀ x ∈ (augIdeal R G) ^ r, e • x ∈ (augIdeal R G) ^ (r + 1) := by
  intro r hr x hx
  obtain ⟨s, rfl⟩ : ∃ s, r = s + 1 := ⟨r - 1, by omega⟩
  rw [pow_succ] at hx
  refine Submodule.mul_induction_on hx ?_ ?_
  · intro a ha b hb
    have : e • (a * b) = a * (e • b) := (mul_smul_comm e a b).symm
    rw [this]
    have hb2 : e • b ∈ (augIdeal R G) ^ 2 := nsmul_augIdeal_le_sq e he b hb
    have : a * (e • b) ∈ (augIdeal R G) ^ s * (augIdeal R G) ^ 2 := Ideal.mul_mem_mul ha hb2
    rwa [← pow_add] at this
  · intro u v hu hv
    rw [smul_add]
    exact Submodule.add_mem _ hu hv

/-! ### The graded pieces -/

/-- Membership in the submodule we quotient by. -/
lemma mem_gr_rel {r : ℕ} (a : ↥((augIdeal R G) ^ r)) :
    a ∈ Submodule.comap ((augIdeal R G) ^ r).subtype ((augIdeal R G) ^ (r + 1)) ↔
      (a : MonoidAlgebra R G) ∈ (augIdeal R G) ^ (r + 1) := Iff.rfl

lemma gr_nsmul_exponent_eq_zero (e : ℕ) (he : ∀ g : G, g ^ e = 1) (r : ℕ) (hr : 1 ≤ r)
    (y : gr R G r) : e • y = 0 := by
  induction y using Submodule.Quotient.induction_on with
  | H a =>
      rw [← Submodule.Quotient.mk_smul, Submodule.Quotient.mk_eq_zero]
      have : ((e • a : ↥((augIdeal R G) ^ r)) : MonoidAlgebra R G) = e • (a : MonoidAlgebra R G) := by
        simp
      rw [mem_gr_rel, this]
      exact nsmul_augIdeal_pow e he r hr (a : MonoidAlgebra R G) a.2

/-- T3 helper: the graded piece is killed by `p ^ v_p(e)` when prime-to-`p` naturals are units. -/
lemma gr_pow_factorization_smul_eq_zero (p e : ℕ) (hp : p.Prime) (he0 : 0 < e)
    (he : ∀ g : G, g ^ e = 1) (hu : ∀ u : ℕ, ¬ p ∣ u → IsUnit (u : R))
    (r : ℕ) (hr : 1 ≤ r) (y : gr R G r) : p ^ (e.factorization p) • y = 0 := by
  have hne : e ≠ 0 := by omega
  set v := e.factorization p with hv
  set u := e / p ^ v with hudef
  have hev : p ^ v * u = e := Nat.ordProj_mul_ordCompl_eq_self e p
  have hnd : ¬ p ∣ u := Nat.not_dvd_ordCompl hp hne
  have h0 : e • y = 0 := gr_nsmul_exponent_eq_zero e he r hr y
  set z : gr R G r := p ^ v • y with hz
  have huz : u • z = 0 := by
    rw [hz, smul_smul, mul_comm, hev]; exact h0
  have hcast : ((u : MonoidAlgebra R G)) • z = u • z :=
    Nat.cast_smul_eq_nsmul (MonoidAlgebra R G) u z
  have hunit : IsUnit ((u : MonoidAlgebra R G)) := by
    have h1 : IsUnit ((u : ℕ) : R) := hu u hnd
    have h2 := h1.map (algebraMap R (MonoidAlgebra R G))
    rwa [map_natCast] at h2
  obtain ⟨w, hw⟩ := hunit
  have hcancel : ((w⁻¹ : (MonoidAlgebra R G)ˣ) : MonoidAlgebra R G) •
      (((w : (MonoidAlgebra R G)ˣ) : MonoidAlgebra R G) • z) = z := by
    rw [smul_smul, Units.inv_mul, one_smul]
  rw [hw, hcast, huz, smul_zero] at hcancel
  exact hcancel.symm

/-- T4 helper. -/
lemma bridge_517_aux (θ : MonoidAlgebra R G) (r p : ℕ) (hr : 2 ≤ r) (hp : 3 ≤ p)
    (hθ : θ ∈ (augIdeal R G) ^ (min r p)) :
    θ ∈ (augIdeal R G) ^ 2 ∧ (3 ≤ r → cls2 θ = 0) := by
  have hmin2 : 2 ≤ min r p := le_min hr (by omega)
  have hmem2 : θ ∈ (augIdeal R G) ^ 2 := Ideal.pow_le_pow_right hmin2 hθ
  refine ⟨hmem2, fun hr3 => ?_⟩
  have hmin3 : 3 ≤ min r p := le_min hr3 hp
  have hmem3 : θ ∈ (augIdeal R G) ^ 3 := Ideal.pow_le_pow_right hmin3 hθ
  rw [cls2, dif_pos hmem2, Submodule.Quotient.mk_eq_zero]
  exact hmem3

/-- T4b helper. -/
lemma cls2_eq_zero_iff (θ : MonoidAlgebra R G) (hθ : θ ∈ (augIdeal R G) ^ 2) :
    cls2 θ = 0 ↔ θ ∈ (augIdeal R G) ^ 3 := by
  rw [cls2, dif_pos hθ, Submodule.Quotient.mk_eq_zero]
  exact Iff.rfl

end Aug

end WitnessContent
