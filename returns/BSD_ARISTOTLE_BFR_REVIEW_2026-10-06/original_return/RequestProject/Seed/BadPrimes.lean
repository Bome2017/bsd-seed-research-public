module

public import RequestProject.Seed.AuxPoint

/-!
# Specialisations at the bad coefficient primes and the `p = 5` count

* `Rp_padic_2243`, `Rp_padic_4547`, `Rp_padic_5843`: the receiver point `R_p` exists over
  `ℚ_p` and lies in `E₁(ℚ_p) \ E₂(ℚ_p)` at each bad coefficient prime.
* `card_affine_F5`: the reduction mod `5` has `7` affine points, so `#E(𝔽₅) = 8`
  (the retained non-anomalous input at `p = 5`), and `5 ∤ Δ` (good reduction at `5`).
-/

@[expose] public section

namespace Seed

instance fact_prime_2243 : Fact (Nat.Prime 2243) := ⟨by norm_num⟩
instance fact_prime_4547 : Fact (Nat.Prime 4547) := ⟨by norm_num⟩
instance fact_prime_5843 : Fact (Nat.Prime 5843) := ⟨by norm_num⟩

theorem Rp_padic_2243 :
    ∃ x y : ℚ_[2243], (curve ℚ_[2243]).toAffine.Nonsingular x y ∧
      x = ((2243 : ℚ_[2243]) ^ 2)⁻¹ ∧ ‖x‖ = (2243 : ℝ) ^ 2 ∧ ‖-x / y‖ = (2243 : ℝ)⁻¹ := by
  simpa using Rp_padic 2243 (by norm_num)

theorem Rp_padic_4547 :
    ∃ x y : ℚ_[4547], (curve ℚ_[4547]).toAffine.Nonsingular x y ∧
      x = ((4547 : ℚ_[4547]) ^ 2)⁻¹ ∧ ‖x‖ = (4547 : ℝ) ^ 2 ∧ ‖-x / y‖ = (4547 : ℝ)⁻¹ := by
  simpa using Rp_padic 4547 (by norm_num)

theorem Rp_padic_5843 :
    ∃ x y : ℚ_[5843], (curve ℚ_[5843]).toAffine.Nonsingular x y ∧
      x = ((5843 : ℚ_[5843]) ^ 2)⁻¹ ∧ ‖x‖ = (5843 : ℝ) ^ 2 ∧ ‖-x / y‖ = (5843 : ℝ)⁻¹ := by
  simpa using Rp_padic 5843 (by norm_num)

/-- Good reduction at `5`: `5 ∤ Δ`. -/
theorem five_not_dvd_disc : ¬ (5 : ℤ) ∣ 16586638656786071143743744 := by decide

/-- The reduction mod `5` of the minimal model has exactly `7` affine points; with the point at
infinity, `#E(𝔽₅) = 8`, which is prime to `5`. -/
theorem card_affine_F5 :
    ((Finset.univ : Finset (ZMod 5 × ZMod 5)).filter
      (fun q => q.2 ^ 2 = q.1 ^ 3 - q.1 ^ 2 - 66020924 * q.1 - 65074271436)).card = 7 := by
  decide

end Seed
