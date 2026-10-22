import WitnessContent.GroupRing

/-!
# A1 — stretch targets

* S1 `lemmaA_general`: Lemma A for an arbitrary (possibly non-commutative) group, with the
  augmentation ideal taken as a `ℤ`-submodule of `ℤ[G]` and `ℤ`-submodule powers.
* S2 `gr_finite_Z`: for a finite abelian group the integral graded pieces are finite.
* S3 `gr_rational_trivial`: their rationalisation vanishes.
-/

namespace WitnessContent

open scoped BigOperators

section General

variable {H : Type*} [Group H]

lemma mem_augSubZ_iff (f : MonoidAlgebra ℤ H) :
    f ∈ augSubZ H ↔ (MonoidAlgebra.lift ℤ ℤ H 1) f = 0 := by
  rw [augSubZ, LinearMap.mem_ker]
  rfl

lemma of_sub_one_mem_augSubZ (g : H) : (MonoidAlgebra.of ℤ H g - 1) ∈ augSubZ H := by
  rw [mem_augSubZ_iff]
  simp

/-- The augmentation `ℤ`-submodule is closed under multiplication. -/
lemma augSubZ_mul_le : (augSubZ H) * (augSubZ H) ≤ augSubZ H := by
  rw [Submodule.mul_le]
  intro a ha b hb
  rw [mem_augSubZ_iff] at *
  rw [map_mul, ha, zero_mul]

/-- Binomial expansion in `ℤ[H]`, truncated after the linear term. -/
lemma augSubZ_one_add_pow (x : MonoidAlgebra ℤ H) (hx : x ∈ augSubZ H) (n : ℕ) :
    ∃ z ∈ (augSubZ H) * (augSubZ H), (1 + x) ^ n = 1 + n • x + z := by
  induction n with
  | zero => exact ⟨0, Submodule.zero_mem _, by simp⟩
  | succ n ih =>
      obtain ⟨z, hz, hzn⟩ := ih
      refine ⟨n • (x * x) + z + z * x, ?_, ?_⟩
      · refine Submodule.add_mem _ (Submodule.add_mem _ ?_ hz) ?_
        · exact Submodule.smul_mem _ _ (Submodule.mul_mem_mul hx hx)
        · exact (mul_le_mul' (augSubZ_mul_le (H := H)) (le_refl (augSubZ H)))
            (Submodule.mul_mem_mul hz hx)
      · rw [pow_succ, hzn]
        simp only [succ_nsmul, nsmul_eq_mul]
        noncomm_ring

lemma augSubZ_repr (f : MonoidAlgebra ℤ H) (hf : f ∈ augSubZ H) :
    f = ∑ g ∈ f.support, f g • (MonoidAlgebra.of ℤ H g - 1) := by
  classical
  have hsum : ∑ g ∈ f.support, f g = 0 := by
    rw [mem_augSubZ_iff] at hf
    simpa [MonoidAlgebra.lift_apply, Finsupp.sum] using hf
  have h1 : ∑ g ∈ f.support, f g • (MonoidAlgebra.of ℤ H g - 1)
      = (∑ g ∈ f.support, f g • MonoidAlgebra.of ℤ H g)
        - (∑ g ∈ f.support, f g) • (1 : MonoidAlgebra ℤ H) := by
    rw [Finset.sum_smul, ← Finset.sum_sub_distrib]
    exact Finset.sum_congr rfl fun g _ => by rw [smul_sub]
  have h2 : ∑ g ∈ f.support, f g • MonoidAlgebra.of ℤ H g = f := by
    have hcongr : ∀ g ∈ f.support, f g • MonoidAlgebra.of ℤ H g = Finsupp.single g (f g) := by
      intro g _
      simp [MonoidAlgebra.of_apply]
    rw [Finset.sum_congr rfl hcongr]
    exact Finsupp.sum_single f
  rw [h1, h2, hsum, zero_smul, sub_zero]

/-- `e • I ⊆ I²` for the augmentation `ℤ`-submodule of an arbitrary group. -/
lemma nsmul_augSubZ_le_sq (e : ℕ) (he : ∀ g : H, g ^ e = 1) (x : MonoidAlgebra ℤ H)
    (hx : x ∈ augSubZ H) : e • x ∈ (augSubZ H) * (augSubZ H) := by
  classical
  have hgen : ∀ g : H, e • (MonoidAlgebra.of ℤ H g - 1) ∈ (augSubZ H) * (augSubZ H) := by
    intro g
    set y : MonoidAlgebra ℤ H := MonoidAlgebra.of ℤ H g - 1 with hy
    have hyI : y ∈ augSubZ H := of_sub_one_mem_augSubZ g
    obtain ⟨z, hz, hze⟩ := augSubZ_one_add_pow y hyI e
    have h1 : (1 : MonoidAlgebra ℤ H) + y = MonoidAlgebra.of ℤ H g := by
      rw [hy]; abel
    have h2 : ((1 : MonoidAlgebra ℤ H) + y) ^ e = 1 := by
      rw [h1, ← map_pow, he g, map_one]
    have hzz : e • y = -z := by
      rw [h2] at hze
      have hz0 : e • y + z = 0 := by
        have hcanc : (1 : MonoidAlgebra ℤ H) + (e • y + z) = 1 + 0 := by
          rw [← add_assoc, add_zero]; exact hze.symm
        exact add_left_cancel hcanc
      exact eq_neg_of_add_eq_zero_left hz0
    rw [hzz]
    exact Submodule.neg_mem _ hz
  rw [augSubZ_repr x hx, Finset.smul_sum]
  refine Submodule.sum_mem _ fun g _ => ?_
  rw [smul_comm]
  exact Submodule.smul_mem _ _ (hgen g)

/-- S1: Lemma A for an arbitrary group. -/
theorem lemmaA_general_proof : Spec.LemmaA_general := by
  intro H _ e he r hr x hx
  obtain ⟨s, rfl⟩ : ∃ s, r = s + 1 := ⟨r - 1, by omega⟩
  rw [pow_succ] at hx
  refine Submodule.mul_induction_on hx ?_ ?_
  · intro a ha b hb
    have hcomm : e • (a * b) = a * (e • b) := (mul_smul_comm e a b).symm
    rw [hcomm]
    have h2 : a * (e • b) ∈ (augSubZ H) ^ s * ((augSubZ H) * (augSubZ H)) :=
      Submodule.mul_mem_mul ha (nsmul_augSubZ_le_sq e he b hb)
    have heq : (augSubZ H) ^ s * ((augSubZ H) * (augSubZ H)) = (augSubZ H) ^ (s + 2) := by
      rw [← sq, ← pow_add]
    rwa [heq] at h2
  · intro u v hu hv
    rw [smul_add]
    exact Submodule.add_mem _ hu hv

end General

section Integral

/-- The integral graded pieces of a finite abelian group are killed by its order. -/
lemma gr_card_smul_eq_zero (G : Type*) [CommGroup G] [Finite G] (r : ℕ) (hr : 1 ≤ r)
    (y : gr ℤ G r) : (Nat.card G) • y = 0 :=
  gr_nsmul_exponent_eq_zero (Nat.card G) (fun _ => pow_card_eq_one') r hr y

/-- S2. -/
theorem gr_finite_Z_proof : Spec.Gr_finite_Z := by
  intro G _ _ r hr
  refine Module.finite_of_fg_torsion _ ?_
  intro y
  have hpos : 0 < Nat.card G := Nat.card_pos
  refine ⟨⟨(Nat.card G : ℤ), ?_⟩, ?_⟩
  · simp only [mem_nonZeroDivisors_iff_ne_zero]
    exact_mod_cast hpos.ne'
  · show ((Nat.card G : ℤ)) • y = 0
    rw [natCast_zsmul]
    exact gr_card_smul_eq_zero G r hr y

/-- S3. -/
theorem gr_rational_trivial_proof : Spec.Gr_rational_trivial := by
  intro G _ _ r hr
  have hpos : 0 < Nat.card G := Nat.card_pos
  have hne : (Nat.card G : ℚ) ≠ 0 := by exact_mod_cast hpos.ne'
  have hzero : ∀ a : TensorProduct ℤ ℚ (gr ℤ G r), a = 0 := by
    intro a
    induction a using TensorProduct.induction_on with
    | zero => rfl
    | tmul q m =>
        have h1 : ((Nat.card G : ℤ)) • (q / (Nat.card G : ℚ)) = q := by
          rw [zsmul_eq_mul]; push_cast; field_simp
        rw [← h1, TensorProduct.smul_tmul, natCast_zsmul, gr_card_smul_eq_zero G r hr m,
          TensorProduct.tmul_zero]
    | add x y hx hy => rw [hx, hy, add_zero]
  exact ⟨fun a b => by rw [hzero a, hzero b]⟩

end Integral

end WitnessContent
