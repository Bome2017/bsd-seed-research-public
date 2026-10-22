/-
The dyadic local condition for the `φ` covering.

For the coefficient pair `(a, b) = (-(Q + D Q), D Q²)` the quartic factors over `ℤ` as

    `d n² = (d u² − Q v²) (d u² − D Q v²)`,

and the two factors are congruent modulo `32` whenever `32 ∣ D − 1`.  A short `2`-adic argument
then shows that any odd `d` carrying a `ℚ_[2]`-point satisfies `d ≡ 1 (mod 4)`.  This is the only
condition needed on the `φ` side beyond the parity obstruction and (when `D > 0`) positivity.
-/
import RequestProject.SDyadic.LocalCommon

namespace SDyadic

open Run013

/-! ## Dyadic units -/

theorem padicInt_two_cast : ((2 : ℕ) : ℤ_[2]) = (2 : ℤ_[2]) := by norm_num

theorem padicInt_prime_two : Prime (2 : ℤ_[2]) := by
  have h := PadicInt.prime_p (p := 2)
  rwa [padicInt_two_cast] at h

theorem padicInt_two_pow_dvd_int_iff (k : ℤ) (n : ℕ) :
    ((2 : ℤ_[2]) ^ n ∣ (k : ℤ_[2])) ↔ ((2 : ℤ) ^ n ∣ k) := by
  have h := padicInt_pow_dvd_intCast_iff (p := 2) k n
  rw [padicInt_two_cast] at h
  rw [h]
  norm_num

theorem padicInt_two_dvd_int_iff (k : ℤ) : ((2 : ℤ_[2]) ∣ (k : ℤ_[2])) ↔ ((2 : ℤ) ∣ k) := by
  simpa using padicInt_two_pow_dvd_int_iff k 1

/-- Every element of `ℤ_[2]` is even or odd. -/
theorem two_dvd_or_odd (x : ℤ_[2]) : (2 : ℤ_[2]) ∣ x ∨ (2 : ℤ_[2]) ∣ (x - 1) := by
  have hz : ∀ y : ZMod 2, y = 0 ∨ y = 1 := by decide
  rcases hz (PadicInt.toZMod x) with h | h
  · exact Or.inl (padicInt_two_cast ▸ (padicInt_toZMod_eq_zero_iff (p := 2) x).mp h)
  · refine Or.inr (padicInt_two_cast ▸ (padicInt_toZMod_eq_zero_iff (p := 2) (x - 1)).mp ?_)
    simp [h]

/-- The square of a `2`-adic unit is `1` modulo `8`. -/
theorem eight_dvd_sq_sub_one {x : ℤ_[2]} (hx : ¬ (2 : ℤ_[2]) ∣ x) : (8 : ℤ_[2]) ∣ x ^ 2 - 1 := by
  obtain ⟨w, hw⟩ : (2 : ℤ_[2]) ∣ (x - 1) := (two_dvd_or_odd x).resolve_left hx
  have hx' : x = 1 + 2 * w := by linear_combination hw
  have hww : (2 : ℤ_[2]) ∣ w * (w + 1) := by
    rcases two_dvd_or_odd w with h | h
    · exact h.mul_right _
    · obtain ⟨t, ht⟩ := h
      exact ⟨w * (t + 1), by linear_combination w * ht⟩
  obtain ⟨t, ht⟩ := hww
  exact ⟨t, by rw [hx']; linear_combination 4 * ht⟩

/-- If `d n² = s² − 8c` with `s`, `n` odd, then `d ≡ 1 (mod 8)`. -/
theorem eight_dvd_sub_one_of_eq {d s n c : ℤ_[2]} (hs : ¬ (2 : ℤ_[2]) ∣ s)
    (hn : ¬ (2 : ℤ_[2]) ∣ n) (h : d * n ^ 2 = s ^ 2 - 8 * c) : (8 : ℤ_[2]) ∣ d - 1 := by
  obtain ⟨ks, hks⟩ := eight_dvd_sq_sub_one hs
  obtain ⟨kn, hkn⟩ := eight_dvd_sq_sub_one hn
  exact ⟨ks - c - d * kn, by linear_combination h - d * hkn + hks⟩

/-! ## The integral dyadic dichotomy -/

/-- The dyadic heart of the `φ`-side argument, over `ℤ_[2]`.  From a primitive integral solution
of the factored covering equation with `D ≡ 1 (mod 32)` one gets either `4 ∣ d − Q` (when the two
factors are divisible by `4`) or `8 ∣ d − 1`. -/
theorem padicInt_two_phi_dichotomy {dd QQ DD2 U V N K : ℤ_[2]}
    (hddodd : ¬ (2 : ℤ_[2]) ∣ dd) (hQodd : ¬ (2 : ℤ_[2]) ∣ QQ)
    (hprim : ¬((2 : ℤ_[2]) ∣ U ∧ (2 : ℤ_[2]) ∣ V))
    (hD : DD2 = 1 + 32 * K)
    (hfac : dd * N ^ 2 = (dd * U ^ 2 - QQ * V ^ 2) * (dd * U ^ 2 - DD2 * QQ * V ^ 2)) :
    (4 : ℤ_[2]) ∣ dd - QQ ∨ (8 : ℤ_[2]) ∣ dd - 1 := by
  have hpr := padicInt_prime_two
  by_cases h4 : (4 : ℤ_[2]) ∣ dd * U ^ 2 - QQ * V ^ 2
  · left
    have hSeven : (2 : ℤ_[2]) ∣ dd * U ^ 2 - QQ * V ^ 2 := dvd_trans ⟨2, by norm_num⟩ h4
    obtain ⟨s2, hs2⟩ := hSeven
    have hUodd : ¬ (2 : ℤ_[2]) ∣ U := by
      intro hU
      have hV : ¬ (2 : ℤ_[2]) ∣ V := fun hV => hprim ⟨hU, hV⟩
      obtain ⟨u1, rfl⟩ := hU
      have hdvd : (2 : ℤ_[2]) ∣ QQ * V ^ 2 :=
        ⟨dd * (2 * u1 ^ 2) - s2, by linear_combination -hs2⟩
      rcases hpr.dvd_mul.mp hdvd with h' | h'
      · exact hQodd h'
      · exact hV (hpr.dvd_of_dvd_pow h')
    have hVodd : ¬ (2 : ℤ_[2]) ∣ V := by
      intro hV
      obtain ⟨v1, rfl⟩ := hV
      have hdvd : (2 : ℤ_[2]) ∣ dd * U ^ 2 :=
        ⟨s2 + QQ * (2 * v1 ^ 2), by linear_combination hs2⟩
      rcases hpr.dvd_mul.mp hdvd with h' | h'
      · exact hddodd h'
      · exact hUodd (hpr.dvd_of_dvd_pow h')
    obtain ⟨cU, hcU⟩ := eight_dvd_sq_sub_one hUodd
    obtain ⟨cV, hcV⟩ := eight_dvd_sq_sub_one hVodd
    obtain ⟨s, hs⟩ := h4
    exact ⟨s - 2 * dd * cU + 2 * QQ * cV, by linear_combination hs - dd * hcU + QQ * hcV⟩
  · right
    have hTS : dd * U ^ 2 - DD2 * QQ * V ^ 2
        = (dd * U ^ 2 - QQ * V ^ 2) - 32 * (K * QQ * V ^ 2) := by rw [hD]; ring
    by_cases h2S : (2 : ℤ_[2]) ∣ dd * U ^ 2 - QQ * V ^ 2
    · obtain ⟨S₁, hS₁eq⟩ := h2S
      have hS₁ : ¬ (2 : ℤ_[2]) ∣ S₁ := by
        rintro ⟨t, rfl⟩
        exact h4 ⟨t, by rw [hS₁eq]; ring⟩
      have hfac' : dd * N ^ 2 = 4 * (S₁ * (S₁ - 16 * (K * QQ * V ^ 2))) := by
        rw [hfac, hTS, hS₁eq]; ring
      have hNeven : (2 : ℤ_[2]) ∣ N := by
        have hdvd : (2 : ℤ_[2]) ∣ dd * N ^ 2 :=
          ⟨2 * (S₁ * (S₁ - 16 * (K * QQ * V ^ 2))), by rw [hfac']; ring⟩
        rcases hpr.dvd_mul.mp hdvd with h' | h'
        · exact absurd h' hddodd
        · exact hpr.dvd_of_dvd_pow h'
      obtain ⟨N₁, rfl⟩ := hNeven
      have hfin : dd * N₁ ^ 2 = S₁ ^ 2 - 8 * (2 * (K * QQ * V ^ 2) * S₁) := by
        refine mul_left_cancel₀ (show (4 : ℤ_[2]) ≠ 0 by norm_num) ?_
        linear_combination hfac' 
      have hN₁ : ¬ (2 : ℤ_[2]) ∣ N₁ := by
        rintro ⟨t, rfl⟩
        refine hS₁ (hpr.dvd_of_dvd_pow (n := 2) ?_)
        exact ⟨dd * (2 * t ^ 2) + 8 * ((K * QQ * V ^ 2) * S₁), by linear_combination -hfin⟩
      exact eight_dvd_sub_one_of_eq hS₁ hN₁ hfin
    · have hTodd : ¬ (2 : ℤ_[2]) ∣ dd * U ^ 2 - DD2 * QQ * V ^ 2 := by
        rintro ⟨t, ht⟩
        exact h2S ⟨t + 16 * (K * QQ * V ^ 2), by rw [hTS] at ht; linear_combination ht⟩
      have hNodd : ¬ (2 : ℤ_[2]) ∣ N := by
        rintro ⟨t, rfl⟩
        have hdvd : (2 : ℤ_[2]) ∣ (dd * U ^ 2 - QQ * V ^ 2) * (dd * U ^ 2 - DD2 * QQ * V ^ 2) :=
          ⟨dd * (2 * t ^ 2), by linear_combination -hfac⟩
        rcases hpr.dvd_mul.mp hdvd with h' | h'
        · exact h2S h'
        · exact hTodd h'
      have hfin : dd * N ^ 2 = (dd * U ^ 2 - QQ * V ^ 2) ^ 2
          - 8 * (4 * (K * QQ * V ^ 2) * (dd * U ^ 2 - QQ * V ^ 2)) := by
        rw [hfac, hTS]; ring
      exact eight_dvd_sub_one_of_eq h2S hNodd hfin

/-! ## The dyadic condition on the `φ` side -/

/-- **The dyadic condition.**  On the `φ` side, an odd `d` that is soluble over `ℚ_[2]`
satisfies `d ≡ 1 (mod 4)`. -/
theorem four_dvd_sub_one_of_cov_two {Q D d : ℤ} (hd : ¬ (2 : ℤ) ∣ d)
    (hQ4 : (4 : ℤ) ∣ (Q - 1)) (hD32 : (32 : ℤ) ∣ (D - 1))
    (h : Cov ℚ_[2] ((-(Q + D * Q) : ℤ) : ℚ_[2]) ((D * Q ^ 2 : ℤ) : ℚ_[2]) ((d : ℤ) : ℚ_[2])) :
    (4 : ℤ) ∣ (d - 1) := by
  have hQodd : ¬ (2 : ℤ) ∣ Q := by obtain ⟨k, hk⟩ := hQ4; omega
  have hddodd : ¬ (2 : ℤ_[2]) ∣ ((d : ℤ) : ℤ_[2]) := fun hc =>
    hd ((padicInt_two_dvd_int_iff d).mp hc)
  have hQodd' : ¬ (2 : ℤ_[2]) ∣ ((Q : ℤ) : ℤ_[2]) := fun hc =>
    hQodd ((padicInt_two_dvd_int_iff Q).mp hc)
  have hdne : ((d : ℤ) : ℤ_[2]) ≠ 0 := fun hz => hddodd (hz ▸ dvd_zero _)
  have hnorm : (((2 : ℕ) : ℝ))⁻¹ ≤ ‖((d : ℤ) : ℤ_[2])‖ := by
    rw [PadicInt.isUnit_iff.mp (padicInt_isUnit_of_not_dvd (padicInt_two_cast ▸ hddodd))]
    norm_num
  have hcov : Cov ℚ_[2] (((((-(Q + D * Q) : ℤ)) : ℤ_[2])) : ℚ_[2])
      (((((D * Q ^ 2 : ℤ)) : ℤ_[2])) : ℚ_[2]) ((((d : ℤ) : ℤ_[2])) : ℚ_[2]) := by
    have e1 : (((((-(Q + D * Q) : ℤ)) : ℤ_[2])) : ℚ_[2]) = ((-(Q + D * Q) : ℤ) : ℚ_[2]) := by
      push_cast; ring
    have e2 : (((((D * Q ^ 2 : ℤ)) : ℤ_[2])) : ℚ_[2]) = ((D * Q ^ 2 : ℤ) : ℚ_[2]) := by
      push_cast; ring
    have e3 : ((((d : ℤ) : ℤ_[2])) : ℚ_[2]) = ((d : ℤ) : ℚ_[2]) := by push_cast; ring
    rw [e1, e2, e3]; exact h
  obtain ⟨U, V, N, hprim, heq⟩ :=
    cov_to_padicInt (((-(Q + D * Q) : ℤ)) : ℤ_[2]) (((D * Q ^ 2 : ℤ)) : ℤ_[2]) _ hdne hnorm hcov
  rw [padicInt_two_cast] at hprim
  obtain ⟨kD, hkD⟩ := hD32
  have hDeq : ((D : ℤ) : ℤ_[2]) = 1 + 32 * ((kD : ℤ) : ℤ_[2]) := by
    have hD' : (D : ℤ) = 1 + 32 * kD := by omega
    rw [hD']; push_cast; ring
  have hfac : ((d : ℤ) : ℤ_[2]) * N ^ 2 =
      (((d : ℤ) : ℤ_[2]) * U ^ 2 - ((Q : ℤ) : ℤ_[2]) * V ^ 2) *
      (((d : ℤ) : ℤ_[2]) * U ^ 2 - ((D : ℤ) : ℤ_[2]) * ((Q : ℤ) : ℤ_[2]) * V ^ 2) := by
    refine covH_factor (a := (((-(Q + D * Q) : ℤ)) : ℤ_[2])) (b := (((D * Q ^ 2 : ℤ)) : ℤ_[2]))
      (e₁ := ((Q : ℤ) : ℤ_[2])) (e₂ := ((D : ℤ) : ℤ_[2]) * ((Q : ℤ) : ℤ_[2])) ?_ ?_ heq
    · push_cast; ring
    · push_cast; ring
  rcases padicInt_two_phi_dichotomy hddodd hQodd' hprim hDeq hfac with hkey | hkey
  · have hz : (2 : ℤ) ^ 2 ∣ (d - Q) := by
      refine (padicInt_two_pow_dvd_int_iff (d - Q) 2).mp ?_
      have e : (((d - Q : ℤ)) : ℤ_[2]) = ((d : ℤ) : ℤ_[2]) - ((Q : ℤ) : ℤ_[2]) := by push_cast; ring
      rw [e, show (2 : ℤ_[2]) ^ 2 = 4 by norm_num]
      exact hkey
    omega
  · have hz : (2 : ℤ) ^ 3 ∣ (d - 1) := by
      refine (padicInt_two_pow_dvd_int_iff (d - 1) 3).mp ?_
      have e : (((d - 1 : ℤ)) : ℤ_[2]) = ((d : ℤ) : ℤ_[2]) - 1 := by push_cast; ring
      rw [e, show (2 : ℤ_[2]) ^ 3 = 8 by norm_num]
      exact hkey
    omega

end SDyadic
