/-
The local obstruction at a prime `ℓ ≡ 3 (mod 4)` dividing the discriminant to an odd power.

Over `ℚ_[ℓ]` with `ℓ ≡ 3 (mod 4)` a nonzero sum of two squares has even valuation.  Since the
completed square of the dual covering at `d = −1` reads

    `W² + (2N)² = Q² Δ V⁴`   with `v_ℓ(Δ)` odd,

no such point exists.  This is what removes the class `−1` on the dual side.
-/
import RequestProject.SDyadic.LocalQ

namespace SDyadic

open Run013

variable {ℓ : ℕ} [hl : Fact ℓ.Prime]

/-- For `ℓ ≡ 3 (mod 4)`, `ℓ` divides a sum of two squares only if it divides both. -/
theorem dvd_of_dvd_sum_sq (hl4 : ℓ % 4 = 3) {X Y : ℤ_[ℓ]}
    (h : (ℓ : ℤ_[ℓ]) ∣ X ^ 2 + Y ^ 2) : (ℓ : ℤ_[ℓ]) ∣ X ∧ (ℓ : ℤ_[ℓ]) ∣ Y := by
  have hmap : (PadicInt.toZMod X) ^ 2 + (PadicInt.toZMod Y) ^ 2 = 0 := by
    have := (padicInt_toZMod_eq_zero_iff (X ^ 2 + Y ^ 2)).mpr h
    simpa using this
  have hY : PadicInt.toZMod Y = 0 := by
    by_contra hY
    refine (ZMod.exists_sq_eq_neg_one_iff (p := ℓ)).mp ⟨PadicInt.toZMod X / PadicInt.toZMod Y, ?_⟩
      hl4
    field_simp
    linear_combination -hmap
  have hX : PadicInt.toZMod X = 0 := by
    have : (PadicInt.toZMod X) ^ 2 = 0 := by rw [hY] at hmap; linear_combination hmap
    exact pow_eq_zero_iff (n := 2) (by norm_num) |>.mp this
  exact ⟨(padicInt_toZMod_eq_zero_iff X).mp hX, (padicInt_toZMod_eq_zero_iff Y).mp hY⟩

/-- Odd powers of `ℓ ≡ 3 (mod 4)` are not sums of two squares times a unit. -/
theorem sum_two_sq_pow_absurd (hl4 : ℓ % 4 = 3) (j : ℕ) (hj : Odd j) (W N G : ℤ_[ℓ])
    (hG : ¬ (ℓ : ℤ_[ℓ]) ∣ G) (heq : W ^ 2 + 4 * N ^ 2 = (ℓ : ℤ_[ℓ]) ^ j * G) : False := by
  induction j using Nat.strong_induction_on generalizing W N with
  | _ j ih =>
    have hpr : Prime ((ℓ : ℤ_[ℓ])) := PadicInt.prime_p
    have hlne : ((ℓ : ℤ_[ℓ])) ≠ 0 := hpr.ne_zero
    have hl2 : ℓ ≠ 2 := by omega
    have hj1 : 1 ≤ j := hj.pos
    have hdvd : (ℓ : ℤ_[ℓ]) ∣ W ^ 2 + (2 * N) ^ 2 := by
      refine ⟨(ℓ : ℤ_[ℓ]) ^ (j - 1) * G, ?_⟩
      have hpow : (ℓ : ℤ_[ℓ]) ^ j = (ℓ : ℤ_[ℓ]) * (ℓ : ℤ_[ℓ]) ^ (j - 1) := by
        rw [← pow_succ']
        congr 1
        omega
      rw [show W ^ 2 + (2 * N) ^ 2 = W ^ 2 + 4 * N ^ 2 by ring, heq, hpow, mul_assoc]
    obtain ⟨hW, h2N⟩ := dvd_of_dvd_sum_sq hl4 hdvd
    have hN : (ℓ : ℤ_[ℓ]) ∣ N := by
      rcases hpr.dvd_mul.mp h2N with h | h
      · exact absurd h (padic_not_dvd_two hl2)
      · exact h
    obtain ⟨W₁, rfl⟩ := hW
    obtain ⟨N₁, rfl⟩ := hN
    rcases Nat.lt_or_ge j 2 with hj2 | hj2
    · -- `j = 1`
      have hj1' : j = 1 := by omega
      subst hj1'
      refine hG ⟨W₁ ^ 2 + 4 * N₁ ^ 2, ?_⟩
      refine mul_left_cancel₀ hlne ?_
      linear_combination -heq
    · -- `j ≥ 3`, descend by two
      refine ih (j - 2) (by omega) (by rcases hj with ⟨t, ht⟩; exact ⟨t - 1, by omega⟩) W₁ N₁ ?_
      have hl2ne : ((ℓ : ℤ_[ℓ])) ^ 2 ≠ 0 := pow_ne_zero _ hlne
      refine mul_left_cancel₀ hl2ne ?_
      have hpow : (ℓ : ℤ_[ℓ]) ^ j = (ℓ : ℤ_[ℓ]) ^ 2 * (ℓ : ℤ_[ℓ]) ^ (j - 2) := by
        rw [← pow_add]
        congr 1
        omega
      rw [show (ℓ : ℤ_[ℓ]) ^ 2 * (W₁ ^ 2 + 4 * N₁ ^ 2) = ((ℓ : ℤ_[ℓ]) * W₁) ^ 2
        + 4 * ((ℓ : ℤ_[ℓ]) * N₁) ^ 2 by ring, heq, hpow, mul_assoc]

/-- **The `ℓ`-adic obstruction.**  With `ℓ ≡ 3 (mod 4)` and `v_ℓ(Δ)` odd, the class `−1` is not
soluble over `ℚ_[ℓ]` for the dual covering. -/
theorem not_cov_ell_neg_one (hl4 : ℓ % 4 = 3) {A R Δ Q w : ℤ} {k : ℕ}
    (hΔ : A ^ 2 - 4 * R ^ 2 = Δ) (hk : Odd k) (hQ : ¬ (ℓ : ℤ) ∣ Q) (hw : ¬ (ℓ : ℤ) ∣ w)
    (hfac : Δ = (ℓ : ℤ) ^ k * w) :
    ¬ Cov ℚ_[ℓ] ((A * Q : ℤ) : ℚ_[ℓ]) ((R ^ 2 * Q ^ 2 : ℤ) : ℚ_[ℓ]) ((-1 : ℤ) : ℚ_[ℓ]) := by
  intro hcov
  have hpr : Prime ((ℓ : ℤ_[ℓ])) := PadicInt.prime_p
  have hl2 : ℓ ≠ 2 := by omega
  have hdunit : ¬ (ℓ : ℤ_[ℓ]) ∣ ((-1 : ℤ) : ℤ_[ℓ]) := by
    intro h
    have := (padicInt_dvd_intCast_iff (p := ℓ) (-1)).mp h
    have h1 : (ℓ : ℤ) ∣ 1 := (dvd_neg.mp this)
    have : (ℓ : ℕ) ∣ 1 := by exact_mod_cast h1
    exact Nat.Prime.one_lt hl.out |>.ne' (Nat.dvd_one.mp this)
  have hdne : ((-1 : ℤ) : ℤ_[ℓ]) ≠ 0 := fun h => hdunit (h ▸ dvd_zero _)
  have hnorm : ((ℓ : ℝ))⁻¹ ≤ ‖((-1 : ℤ) : ℤ_[ℓ])‖ := by
    rw [PadicInt.isUnit_iff.mp (padicInt_isUnit_of_not_dvd hdunit)]
    exact Nat.cast_inv_le_one ℓ
  have hcov' : Cov ℚ_[ℓ] ((((A * Q : ℤ) : ℤ_[ℓ])) : ℚ_[ℓ])
      ((((R ^ 2 * Q ^ 2 : ℤ) : ℤ_[ℓ])) : ℚ_[ℓ]) ((((-1 : ℤ) : ℤ_[ℓ])) : ℚ_[ℓ]) := by
    have e1 : ((((A * Q : ℤ) : ℤ_[ℓ])) : ℚ_[ℓ]) = ((A * Q : ℤ) : ℚ_[ℓ]) := by push_cast; ring
    have e2 : ((((R ^ 2 * Q ^ 2 : ℤ) : ℤ_[ℓ])) : ℚ_[ℓ]) = ((R ^ 2 * Q ^ 2 : ℤ) : ℚ_[ℓ]) := by
      push_cast; ring
    have e3 : ((((-1 : ℤ) : ℤ_[ℓ])) : ℚ_[ℓ]) = ((-1 : ℤ) : ℚ_[ℓ]) := by push_cast; ring
    rw [e1, e2, e3]; exact hcov
  obtain ⟨U, V, N, hprim, heq⟩ := cov_to_padicInt (((A * Q : ℤ)) : ℤ_[ℓ])
    (((R ^ 2 * Q ^ 2 : ℤ)) : ℤ_[ℓ]) _ hdne hnorm hcov'
  have hdisc := covH_disc heq
  have hdiscval : ((((A * Q : ℤ)) : ℤ_[ℓ])) ^ 2 - 4 * ((((R ^ 2 * Q ^ 2 : ℤ)) : ℤ_[ℓ]))
      = ((Q : ℤ) : ℤ_[ℓ]) ^ 2 * ((ℓ : ℤ_[ℓ]) ^ k * ((w : ℤ) : ℤ_[ℓ])) := by
    have hΔ' : ((ℓ : ℤ) ^ k * w : ℤ) = A ^ 2 - 4 * R ^ 2 := by rw [← hfac, hΔ]
    have : (((ℓ : ℤ) ^ k * w : ℤ) : ℤ_[ℓ]) = ((A ^ 2 - 4 * R ^ 2 : ℤ) : ℤ_[ℓ]) := by rw [hΔ']
    push_cast at this ⊢
    linear_combination -((Q : ℤ) : ℤ_[ℓ]) ^ 2 * this
  rw [hdiscval] at hdisc
  have hdcast : (((-1 : ℤ)) : ℤ_[ℓ]) = -1 := by push_cast; ring
  rw [hdcast] at hdisc
  -- `W² + (2N)² = Q² ℓ^k w V⁴`
  have hmain : (2 * (-1 : ℤ_[ℓ]) * U ^ 2 + ((A * Q : ℤ) : ℤ_[ℓ]) * V ^ 2) ^ 2 + 4 * N ^ 2
      = (ℓ : ℤ_[ℓ]) ^ k * (((Q : ℤ) : ℤ_[ℓ]) ^ 2 * ((w : ℤ) : ℤ_[ℓ]) * V ^ 4) := by
    linear_combination hdisc
  have hQ' : ¬ (ℓ : ℤ_[ℓ]) ∣ ((Q : ℤ) : ℤ_[ℓ]) := fun h =>
    hQ ((padicInt_dvd_intCast_iff (p := ℓ) Q).mp h)
  have hw' : ¬ (ℓ : ℤ_[ℓ]) ∣ ((w : ℤ) : ℤ_[ℓ]) := fun h =>
    hw ((padicInt_dvd_intCast_iff (p := ℓ) w).mp h)
  -- first: `ℓ ∤ V`
  have hV : ¬ (ℓ : ℤ_[ℓ]) ∣ V := by
    rintro ⟨V₁, rfl⟩
    have hk1 : 1 ≤ k := hk.pos
    have hdvd : (ℓ : ℤ_[ℓ]) ∣ (2 * (-1 : ℤ_[ℓ]) * U ^ 2
        + ((A * Q : ℤ) : ℤ_[ℓ]) * ((ℓ : ℤ_[ℓ]) * V₁) ^ 2) ^ 2 + (2 * N) ^ 2 := by
      refine ⟨(ℓ : ℤ_[ℓ]) ^ (k - 1) * (((Q : ℤ) : ℤ_[ℓ]) ^ 2 * ((w : ℤ) : ℤ_[ℓ])
        * ((ℓ : ℤ_[ℓ]) * V₁) ^ 4), ?_⟩
      have hpow : (ℓ : ℤ_[ℓ]) ^ k = (ℓ : ℤ_[ℓ]) * (ℓ : ℤ_[ℓ]) ^ (k - 1) := by
        rw [← pow_succ']; congr 1; omega
      rw [show ∀ x y : ℤ_[ℓ], x ^ 2 + (2 * y) ^ 2 = x ^ 2 + 4 * y ^ 2 from fun x y => by ring,
        hmain, hpow, mul_assoc]
    obtain ⟨hW, -⟩ := dvd_of_dvd_sum_sq hl4 hdvd
    obtain ⟨t, ht⟩ := hW
    have hU2 : (ℓ : ℤ_[ℓ]) ∣ 2 * U ^ 2 :=
      ⟨((A * Q : ℤ) : ℤ_[ℓ]) * ((ℓ : ℤ_[ℓ]) * V₁ ^ 2) - t, by linear_combination -ht⟩
    rcases hpr.dvd_mul.mp hU2 with h | h
    · exact padic_not_dvd_two hl2 h
    · exact hprim ⟨hpr.dvd_of_dvd_pow h, ⟨V₁, rfl⟩⟩
  refine sum_two_sq_pow_absurd hl4 k hk _ N _ ?_ hmain
  intro hc
  rcases hpr.dvd_mul.mp hc with h | h
  · rcases hpr.dvd_mul.mp h with h' | h'
    · exact hQ' (hpr.dvd_of_dvd_pow h')
    · exact hw' h'
  · exact hV (hpr.dvd_of_dvd_pow h)

end SDyadic
