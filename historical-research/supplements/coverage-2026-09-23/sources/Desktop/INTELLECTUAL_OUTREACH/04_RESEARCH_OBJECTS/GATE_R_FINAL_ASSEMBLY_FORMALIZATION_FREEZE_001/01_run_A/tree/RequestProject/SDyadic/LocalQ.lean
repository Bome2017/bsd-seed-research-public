/-
The local condition at `q` for the dual covering.

The dual coefficient pair is `(a, b) = (A q, R² q²)`, whose discriminant is `a² − 4b = q² Δ` with
`Δ = A² − 4R²`.  Since `Δ` is a quadratic non-residue mod `q`, the binary quadratic form of
discriminant `Δ` is anisotropic mod `q`; this forces

* the `q`-valuation of a locally soluble `d` to be even, and
* the unit part of `d` to be a square mod `q`.
-/
import RequestProject.SDyadic.LocalCommon

namespace SDyadic

open Run013

variable {q : ℕ} [hq : Fact q.Prime]

/-! ## Small facts about an odd prime `q` -/

theorem padic_not_dvd_two (hq2 : q ≠ 2) : ¬ (q : ℤ_[q]) ∣ (2 : ℤ_[q]) := by
  intro h
  have hcast : ((2 : ℤ) : ℤ_[q]) = (2 : ℤ_[q]) := by push_cast; ring
  rw [← hcast] at h
  have h1 := (padicInt_dvd_intCast_iff (p := q) 2).mp h
  have h2 : (q : ℕ) ∣ 2 := by exact_mod_cast h1
  exact hq2 ((Nat.prime_dvd_prime_iff_eq hq.out Nat.prime_two).mp h2)

theorem padic_not_dvd_four (hq2 : q ≠ 2) : ¬ (q : ℤ_[q]) ∣ (4 : ℤ_[q]) := by
  intro h
  refine padic_not_dvd_two hq2 ?_
  rw [show (4 : ℤ_[q]) = 2 * 2 by norm_num] at h
  rcases PadicInt.prime_p.dvd_mul.mp h with h' | h' <;> exact h'

theorem zmod_four_ne_zero (hq2 : q ≠ 2) : (4 : ZMod q) ≠ 0 := by
  intro hc
  have h4 : ((4 : ℤ) : ZMod q) = 0 := by push_cast; exact hc
  rw [ZMod.intCast_zmod_eq_zero_iff_dvd] at h4
  have h4' : (q : ℕ) ∣ 4 := by exact_mod_cast h4
  have : (q : ℕ) ∣ 2 := hq.out.dvd_of_dvd_pow (n := 2) (by simpa using h4')
  exact hq2 ((Nat.prime_dvd_prime_iff_eq hq.out Nat.prime_two).mp this)

theorem toZMod_ne_zero_of_not_dvd {x : ℤ_[q]} (h : ¬ (q : ℤ_[q]) ∣ x) :
    PadicInt.toZMod x ≠ 0 := fun hc => h ((padicInt_toZMod_eq_zero_iff x).mp hc)

theorem toZMod_q : PadicInt.toZMod ((q : ℤ_[q])) = 0 := by rw [padicInt_toZMod_eq_zero_iff]

/-! ## The two branches -/

/-- Odd `q`-valuation is impossible on the dual side. -/
theorem not_cov_q_of_odd_val {A R Δ d₀ : ℤ} (hq2 : q ≠ 2)
    (hΔ : A ^ 2 - 4 * R ^ 2 = Δ) (hd₀ : ¬ (q : ℤ) ∣ d₀)
    (hleg : legendreSym q Δ = -1) :
    ¬ Cov ℚ_[q] ((A * (q : ℤ) : ℤ) : ℚ_[q]) ((R ^ 2 * (q : ℤ) ^ 2 : ℤ) : ℚ_[q])
      (((q : ℤ) * d₀ : ℤ) : ℚ_[q]) := by
  intro hcov
  have hpr : Prime ((q : ℤ_[q])) := PadicInt.prime_p
  have hqne : (q : ℤ_[q]) ≠ 0 := hpr.ne_zero
  have hd₀' : ¬ (q : ℤ_[q]) ∣ ((d₀ : ℤ) : ℤ_[q]) := fun h =>
    hd₀ ((padicInt_dvd_intCast_iff (p := q) d₀).mp h)
  have hdne : ((q : ℤ_[q]) * ((d₀ : ℤ) : ℤ_[q])) ≠ 0 :=
    mul_ne_zero hqne (fun h => hd₀' (h ▸ dvd_zero _))
  have hnorm : ((q : ℝ))⁻¹ ≤ ‖(q : ℤ_[q]) * ((d₀ : ℤ) : ℤ_[q])‖ :=
    le_of_eq (padicInt_norm_p_mul_unit hd₀').symm
  have hcov' : Cov ℚ_[q] ((((A * (q : ℤ) : ℤ) : ℤ_[q])) : ℚ_[q])
      ((((R ^ 2 * (q : ℤ) ^ 2 : ℤ) : ℤ_[q])) : ℚ_[q])
      (((q : ℤ_[q]) * ((d₀ : ℤ) : ℤ_[q]) : ℤ_[q]) : ℚ_[q]) := by
    have e1 : ((((A * (q : ℤ) : ℤ) : ℤ_[q])) : ℚ_[q]) = ((A * (q : ℤ) : ℤ) : ℚ_[q]) := by
      push_cast; ring
    have e2 : ((((R ^ 2 * (q : ℤ) ^ 2 : ℤ) : ℤ_[q])) : ℚ_[q])
        = ((R ^ 2 * (q : ℤ) ^ 2 : ℤ) : ℚ_[q]) := by push_cast; ring
    have e3 : (((q : ℤ_[q]) * ((d₀ : ℤ) : ℤ_[q]) : ℤ_[q]) : ℚ_[q])
        = (((q : ℤ) * d₀ : ℤ) : ℚ_[q]) := by push_cast; ring
    rw [e1, e2, e3]; exact hcov
  obtain ⟨U, V, N, hprim, heq⟩ := cov_to_padicInt (((A * (q : ℤ) : ℤ)) : ℤ_[q])
    (((R ^ 2 * (q : ℤ) ^ 2 : ℤ)) : ℤ_[q]) _ hdne hnorm hcov'
  have hdisc := covH_disc heq
  have hcastA : ((((A * (q : ℤ) : ℤ)) : ℤ_[q])) = ((A : ℤ) : ℤ_[q]) * (q : ℤ_[q]) := by
    push_cast; ring
  have hcast2 : ((((A * (q : ℤ) : ℤ)) : ℤ_[q])) ^ 2
      - 4 * ((((R ^ 2 * (q : ℤ) ^ 2 : ℤ)) : ℤ_[q])) = (q : ℤ_[q]) ^ 2 * ((Δ : ℤ) : ℤ_[q]) := by
    have hΔ' : (Δ : ℤ) = A ^ 2 - 4 * R ^ 2 := hΔ.symm
    rw [hΔ']; push_cast; ring
  rw [hcast2, hcastA] at hdisc
  -- pull a factor `q` out of the completed square
  have hkey : (q : ℤ_[q]) * ((2 * ((d₀ : ℤ) : ℤ_[q]) * U ^ 2 + ((A : ℤ) : ℤ_[q]) * V ^ 2) ^ 2
      - ((Δ : ℤ) : ℤ_[q]) * V ^ 4) = 4 * (((d₀ : ℤ) : ℤ_[q]) * N ^ 2) := by
    refine mul_left_cancel₀ hqne ?_
    linear_combination hdisc
  have hNdvd : (q : ℤ_[q]) ∣ N := by
    have h1 : (q : ℤ_[q]) ∣ 4 * (((d₀ : ℤ) : ℤ_[q]) * N ^ 2) := ⟨_, hkey.symm⟩
    rcases hpr.dvd_mul.mp h1 with h | h
    · exact absurd h (padic_not_dvd_four hq2)
    · rcases hpr.dvd_mul.mp h with h' | h'
      · exact absurd h' hd₀'
      · exact hpr.dvd_of_dvd_pow h'
  obtain ⟨N₁, rfl⟩ := hNdvd
  have hkey2 : (2 * ((d₀ : ℤ) : ℤ_[q]) * U ^ 2 + ((A : ℤ) : ℤ_[q]) * V ^ 2) ^ 2
      - ((Δ : ℤ) : ℤ_[q]) * V ^ 4
      = (q : ℤ_[q]) * (4 * (((d₀ : ℤ) : ℤ_[q]) * N₁ ^ 2)) := by
    refine mul_left_cancel₀ hqne ?_
    rw [hkey]; ring
  -- `q ∤ V`
  have hV : ¬ (q : ℤ_[q]) ∣ V := by
    rintro ⟨V₁, rfl⟩
    have hW : (q : ℤ_[q]) ∣ (2 * ((d₀ : ℤ) : ℤ_[q]) * U ^ 2
        + ((A : ℤ) : ℤ_[q]) * ((q : ℤ_[q]) * V₁) ^ 2) ^ 2 :=
      ⟨4 * (((d₀ : ℤ) : ℤ_[q]) * N₁ ^ 2) + ((Δ : ℤ) : ℤ_[q]) * ((q : ℤ_[q]) ^ 3 * V₁ ^ 4), by
        linear_combination hkey2⟩
    obtain ⟨w, hw⟩ := hpr.dvd_of_dvd_pow hW
    have hU : (q : ℤ_[q]) ∣ 2 * ((d₀ : ℤ) : ℤ_[q]) * U ^ 2 :=
      ⟨w - ((A : ℤ) : ℤ_[q]) * ((q : ℤ_[q]) * V₁ ^ 2), by linear_combination hw⟩
    rcases hpr.dvd_mul.mp hU with h | h
    · rcases hpr.dvd_mul.mp h with h' | h'
      · exact padic_not_dvd_two hq2 h'
      · exact hd₀' h'
    · exact hprim ⟨hpr.dvd_of_dvd_pow h, ⟨V₁, rfl⟩⟩
  -- reduce mod `q`: `Δ` becomes a square
  refine (legendreSym.eq_neg_one_iff q).mp hleg ?_
  have hmap := congrArg (PadicInt.toZMod (p := q)) hkey2
  simp only [map_sub, map_mul, map_pow, map_add, map_ofNat, map_intCast, toZMod_q,
    zero_mul] at hmap
  have hVne : PadicInt.toZMod V ≠ 0 := toZMod_ne_zero_of_not_dvd hV
  refine ⟨(2 * ((d₀ : ℤ) : ZMod q) * (PadicInt.toZMod U) ^ 2
    + ((A : ℤ) : ZMod q) * (PadicInt.toZMod V) ^ 2) / (PadicInt.toZMod V) ^ 2, ?_⟩
  field_simp
  linear_combination -hmap

/-- Even `q`-valuation: the unit part of `d` must be a square mod `q`. -/
theorem isSquare_of_cov_q {A R Δ d : ℤ} (hq2 : q ≠ 2)
    (hΔ : A ^ 2 - 4 * R ^ 2 = Δ) (hd : ¬ (q : ℤ) ∣ d) (hR : ¬ (q : ℤ) ∣ R)
    (hcov : Cov ℚ_[q] ((A * (q : ℤ) : ℤ) : ℚ_[q]) ((R ^ 2 * (q : ℤ) ^ 2 : ℤ) : ℚ_[q])
      ((d : ℤ) : ℚ_[q])) :
    IsSquare ((d : ℤ) : ZMod q) := by
  have hpr : Prime ((q : ℤ_[q])) := PadicInt.prime_p
  have hd' : ¬ (q : ℤ_[q]) ∣ ((d : ℤ) : ℤ_[q]) := fun h =>
    hd ((padicInt_dvd_intCast_iff (p := q) d).mp h)
  have hR' : ¬ (q : ℤ_[q]) ∣ ((R : ℤ) : ℤ_[q]) := fun h =>
    hR ((padicInt_dvd_intCast_iff (p := q) R).mp h)
  have hdne : ((d : ℤ) : ℤ_[q]) ≠ 0 := fun h => hd' (h ▸ dvd_zero _)
  have hnorm : ((q : ℝ))⁻¹ ≤ ‖((d : ℤ) : ℤ_[q])‖ := by
    rw [PadicInt.isUnit_iff.mp (padicInt_isUnit_of_not_dvd hd')]
    exact Nat.cast_inv_le_one q
  have hcov' : Cov ℚ_[q] ((((A * (q : ℤ) : ℤ) : ℤ_[q])) : ℚ_[q])
      ((((R ^ 2 * (q : ℤ) ^ 2 : ℤ) : ℤ_[q])) : ℚ_[q]) ((((d : ℤ) : ℤ_[q])) : ℚ_[q]) := by
    have e1 : ((((A * (q : ℤ) : ℤ) : ℤ_[q])) : ℚ_[q]) = ((A * (q : ℤ) : ℤ) : ℚ_[q]) := by
      push_cast; ring
    have e2 : ((((R ^ 2 * (q : ℤ) ^ 2 : ℤ) : ℤ_[q])) : ℚ_[q])
        = ((R ^ 2 * (q : ℤ) ^ 2 : ℤ) : ℚ_[q]) := by push_cast; ring
    have e3 : ((((d : ℤ) : ℤ_[q])) : ℚ_[q]) = ((d : ℤ) : ℚ_[q]) := by push_cast; ring
    rw [e1, e2, e3]; exact hcov
  obtain ⟨U, V, N, hprim, heq⟩ := cov_to_padicInt (((A * (q : ℤ) : ℤ)) : ℤ_[q])
    (((R ^ 2 * (q : ℤ) ^ 2 : ℤ)) : ℤ_[q]) _ hdne hnorm hcov'
  have hdisc := covH_disc heq
  have hcastA : ((((A * (q : ℤ) : ℤ)) : ℤ_[q])) = ((A : ℤ) : ℤ_[q]) * (q : ℤ_[q]) := by
    push_cast; ring
  have hcast2 : ((((A * (q : ℤ) : ℤ)) : ℤ_[q])) ^ 2
      - 4 * ((((R ^ 2 * (q : ℤ) ^ 2 : ℤ)) : ℤ_[q])) = (q : ℤ_[q]) ^ 2 * ((Δ : ℤ) : ℤ_[q]) := by
    have hΔ' : (Δ : ℤ) = A ^ 2 - 4 * R ^ 2 := hΔ.symm
    rw [hΔ']; push_cast; ring
  rw [hcast2, hcastA] at hdisc
  have hdne' : PadicInt.toZMod (((d : ℤ) : ℤ_[q])) ≠ 0 := toZMod_ne_zero_of_not_dvd hd'
  have hdcast : PadicInt.toZMod (((d : ℤ) : ℤ_[q])) = ((d : ℤ) : ZMod q) := by simp
  by_cases hU : (q : ℤ_[q]) ∣ U
  · -- `q ∣ U`, so `q ∤ V`
    obtain ⟨U₁, rfl⟩ := hU
    have hV : ¬ (q : ℤ_[q]) ∣ V := fun h => hprim ⟨⟨U₁, rfl⟩, h⟩
    have hq2ne : ((q : ℤ_[q])) ^ 2 ≠ 0 := pow_ne_zero _ hpr.ne_zero
    have hkey : (q : ℤ_[q]) ^ 2 *
        ((2 * ((d : ℤ) : ℤ_[q]) * (q : ℤ_[q]) * U₁ ^ 2 + ((A : ℤ) : ℤ_[q]) * V ^ 2) ^ 2
          - ((Δ : ℤ) : ℤ_[q]) * V ^ 4) = 4 * (((d : ℤ) : ℤ_[q]) * N ^ 2) := by
      linear_combination hdisc
    have hNdvd : (q : ℤ_[q]) ∣ N := by
      have h1 : (q : ℤ_[q]) ∣ 4 * (((d : ℤ) : ℤ_[q]) * N ^ 2) := by
        refine ⟨(q : ℤ_[q]) *
          ((2 * ((d : ℤ) : ℤ_[q]) * (q : ℤ_[q]) * U₁ ^ 2 + ((A : ℤ) : ℤ_[q]) * V ^ 2) ^ 2
            - ((Δ : ℤ) : ℤ_[q]) * V ^ 4), ?_⟩
        rw [← hkey]; ring
      rcases hpr.dvd_mul.mp h1 with h | h
      · exact absurd h (padic_not_dvd_four hq2)
      · rcases hpr.dvd_mul.mp h with h' | h'
        · exact absurd h' hd'
        · exact hpr.dvd_of_dvd_pow h'
    obtain ⟨N₁, rfl⟩ := hNdvd
    have hkey2 : (2 * ((d : ℤ) : ℤ_[q]) * (q : ℤ_[q]) * U₁ ^ 2 + ((A : ℤ) : ℤ_[q]) * V ^ 2) ^ 2
        - ((Δ : ℤ) : ℤ_[q]) * V ^ 4 = 4 * (((d : ℤ) : ℤ_[q]) * N₁ ^ 2) := by
      refine mul_left_cancel₀ hq2ne ?_
      rw [hkey]; ring
    have hmap := congrArg (PadicInt.toZMod (p := q)) hkey2
    simp only [map_sub, map_mul, map_pow, map_add, map_ofNat, map_intCast, toZMod_q, zero_mul,
      mul_zero, zero_add] at hmap
    -- now `A² V⁴ − Δ V⁴ = 4 d N₁²`, and `A² − Δ = 4 R²`
    have hAR : ((A : ℤ) : ZMod q) ^ 2 - ((Δ : ℤ) : ZMod q) = 4 * ((R : ℤ) : ZMod q) ^ 2 := by
      have : ((A ^ 2 - 4 * R ^ 2 : ℤ) : ZMod q) = ((Δ : ℤ) : ZMod q) := by rw [hΔ]
      push_cast at this ⊢
      linear_combination this
    have hRcast : PadicInt.toZMod (((R : ℤ) : ℤ_[q])) = ((R : ℤ) : ZMod q) := by simp
    have hVne : PadicInt.toZMod V ≠ 0 := toZMod_ne_zero_of_not_dvd hV
    have hRne : ((R : ℤ) : ZMod q) ≠ 0 := hRcast ▸ toZMod_ne_zero_of_not_dvd hR'
    have hfin : 4 * (((R : ℤ) : ZMod q) ^ 2 * (PadicInt.toZMod V) ^ 4)
        = 4 * (((d : ℤ) : ZMod q) * (PadicInt.toZMod N₁) ^ 2) := by
      linear_combination hmap - (PadicInt.toZMod V) ^ 4 * hAR
    have h4 : (4 : ZMod q) ≠ 0 := zmod_four_ne_zero hq2
    have hfin2 : ((R : ℤ) : ZMod q) ^ 2 * (PadicInt.toZMod V) ^ 4
        = ((d : ℤ) : ZMod q) * (PadicInt.toZMod N₁) ^ 2 := mul_left_cancel₀ h4 hfin
    have hN₁ne : PadicInt.toZMod N₁ ≠ 0 := by
      intro hc
      rw [hc] at hfin2
      simp at hfin2
      rcases hfin2 with h | h
      · exact hRne h
      · exact hVne h
    refine ⟨((R : ℤ) : ZMod q) * (PadicInt.toZMod V) ^ 2 / PadicInt.toZMod N₁, ?_⟩
    field_simp
    linear_combination -hfin2
  · -- `q ∤ U`
    have hmap := congrArg (PadicInt.toZMod (p := q)) hdisc
    simp only [map_sub, map_mul, map_pow, map_add, map_ofNat, map_intCast, toZMod_q, zero_mul,
      mul_zero, add_zero] at hmap
    have hUne : PadicInt.toZMod U ≠ 0 := toZMod_ne_zero_of_not_dvd hU
    have h4 : (4 : ZMod q) ≠ 0 := zmod_four_ne_zero hq2
    have hfin : ((d : ℤ) : ZMod q) ^ 2 * (PadicInt.toZMod U) ^ 4
        = ((d : ℤ) : ZMod q) * (PadicInt.toZMod N) ^ 2 := by
      refine mul_left_cancel₀ h4 ?_
      linear_combination hmap
    have hdne'' : ((d : ℤ) : ZMod q) ≠ 0 := hdcast ▸ hdne'
    have hfin2 : ((d : ℤ) : ZMod q) * (PadicInt.toZMod U) ^ 4 = (PadicInt.toZMod N) ^ 2 :=
      mul_left_cancel₀ hdne'' (by linear_combination hfin)
    refine ⟨PadicInt.toZMod N / (PadicInt.toZMod U) ^ 2, ?_⟩
    field_simp
    linear_combination hfin2

end SDyadic
