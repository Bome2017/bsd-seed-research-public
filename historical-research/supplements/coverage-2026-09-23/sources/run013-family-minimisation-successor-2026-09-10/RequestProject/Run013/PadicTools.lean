/-
Run013 — `PadicTools.lean`

Elementary `p`-adic tools used by the local analysis:

* integral normalisation of a projective point on the cleared covering
  (weighted scaling `(u,v,M) ↦ (λu, λv, λ²M)`),
* "a square cannot have odd valuation".

No local solubility table is assumed anywhere; these are genuine arithmetic lemmas.
-/
import RequestProject.Run013.Basic

namespace Run013

open PadicInt

variable {p : ℕ} [Fact p.Prime]

lemma padicInt_coe_inj {x y : ℤ_[p]} (h : (x : ℚ_[p]) = y) : x = y := Subtype.ext h

/-- A square in `ℤ_[p]` cannot equal `p^(2k+1)` times a `p`-adic unit. -/
theorem not_sq_odd_val (w : ℤ_[p]) (hw : ¬ (p : ℤ_[p]) ∣ w) :
    ∀ (k : ℕ) (M : ℤ_[p]), M ^ 2 ≠ (p : ℤ_[p]) ^ (2 * k + 1) * w := by
  intro k
  induction k with
  | zero =>
      intro M hM
      have hdvd : (p : ℤ_[p]) ∣ M ^ 2 := ⟨w, by simpa using hM⟩
      obtain ⟨M', rfl⟩ := (PadicInt.prime_p (p := p)).dvd_of_dvd_pow hdvd
      have hp0 : (p : ℤ_[p]) ≠ 0 := (PadicInt.prime_p (p := p)).ne_zero
      have h1 : (p : ℤ_[p]) * (M' ^ 2 * (p : ℤ_[p])) = (p : ℤ_[p]) * w := by
        rw [show ((p : ℤ_[p]) * M') ^ 2 = (p : ℤ_[p]) * (M' ^ 2 * (p : ℤ_[p])) by ring] at hM
        rw [hM]; ring
      have h2 : M' ^ 2 * (p : ℤ_[p]) = w := mul_left_cancel₀ hp0 h1
      exact hw ⟨M' ^ 2, by rw [← h2]; ring⟩
  | succ k ih =>
      intro M hM
      have hdvd : (p : ℤ_[p]) ∣ M ^ 2 := by
        refine ⟨(p : ℤ_[p]) ^ (2 * k + 2) * w, ?_⟩
        rw [hM]; ring
      obtain ⟨M', rfl⟩ := (PadicInt.prime_p (p := p)).dvd_of_dvd_pow hdvd
      have hp0 : (p : ℤ_[p]) ≠ 0 := (PadicInt.prime_p (p := p)).ne_zero
      have hsq : (p : ℤ_[p]) ^ 2 * M' ^ 2
          = (p : ℤ_[p]) ^ 2 * ((p : ℤ_[p]) ^ (2 * k + 1) * w) := by
        rw [show ((p : ℤ_[p]) * M') ^ 2 = (p : ℤ_[p]) ^ 2 * M' ^ 2 by ring] at hM
        rw [hM]; ring
      exact ih M' (mul_left_cancel₀ (pow_ne_zero 2 hp0) hsq)

/-- Integral normalisation: a `ℚ_[p]`-point of the cleared covering with integral
coefficients may be scaled so that `u, v, M` are `p`-adic integers with `u = 1` or `v = 1`. -/
theorem covM_integral (a b d : ℤ_[p]) (h : CovM ℚ_[p] (a : ℚ_[p]) (b : ℚ_[p]) (d : ℚ_[p])) :
    ∃ U V M : ℤ_[p], (U = 1 ∨ V = 1) ∧
      M ^ 2 = d ^ 3 * U ^ 4 + a * d ^ 2 * U ^ 2 * V ^ 2 + b * d * V ^ 4 := by
  obtain ⟨u, v, M, huv, hM⟩ := h
  have main : ∀ lam : ℚ_[p], ‖lam * u‖ ≤ 1 → ‖lam * v‖ ≤ 1 →
      ∃ U V N : ℤ_[p], (U : ℚ_[p]) = lam * u ∧ (V : ℚ_[p]) = lam * v ∧
        N ^ 2 = d ^ 3 * U ^ 4 + a * d ^ 2 * U ^ 2 * V ^ 2 + b * d * V ^ 4 := by
    intro lam hu hv
    set U : ℤ_[p] := ⟨lam * u, hu⟩ with hUdef
    set V : ℤ_[p] := ⟨lam * v, hv⟩ with hVdef
    have hUc : ((U : ℤ_[p]) : ℚ_[p]) = lam * u := rfl
    have hVc : ((V : ℤ_[p]) : ℚ_[p]) = lam * v := rfl
    have key : (lam ^ 2 * M) ^ 2 =
        ((d ^ 3 * U ^ 4 + a * d ^ 2 * U ^ 2 * V ^ 2 + b * d * V ^ 4 : ℤ_[p]) : ℚ_[p]) := by
      push_cast [hUc, hVc]
      linear_combination lam ^ 4 * hM
    have hNnorm : ‖lam ^ 2 * M‖ ≤ 1 := by
      have h1 : ‖(lam ^ 2 * M) ^ 2‖ ≤ 1 := by
        rw [key]; exact PadicInt.norm_le_one _
      rw [norm_pow] at h1
      nlinarith [norm_nonneg (lam ^ 2 * M)]
    exact ⟨U, V, ⟨lam ^ 2 * M, hNnorm⟩, hUc, hVc, padicInt_coe_inj (by rw [← key]; rfl)⟩
  rcases le_total ‖v‖ ‖u‖ with hle | hle
  · have hu : u ≠ 0 := by
      intro h
      refine huv ⟨h, ?_⟩
      rw [h] at hle
      simpa using le_antisymm (by simpa using hle) (norm_nonneg v)
    have h1 : ‖u⁻¹ * u‖ ≤ 1 := by rw [inv_mul_cancel₀ hu]; simp
    have h2 : ‖u⁻¹ * v‖ ≤ 1 := by
      rw [norm_mul, norm_inv]
      rw [inv_mul_le_iff₀ (by positivity)]
      linarith
    obtain ⟨U, V, N, hU, hV, hN⟩ := main u⁻¹ h1 h2
    refine ⟨U, V, N, Or.inl ?_, hN⟩
    exact padicInt_coe_inj (by rw [hU, inv_mul_cancel₀ hu]; rfl)
  · have hv : v ≠ 0 := by
      intro h
      refine huv ⟨?_, h⟩
      rw [h] at hle
      simpa using le_antisymm (by simpa using hle) (norm_nonneg u)
    have h1 : ‖v⁻¹ * u‖ ≤ 1 := by
      rw [norm_mul, norm_inv]
      rw [inv_mul_le_iff₀ (by positivity)]
      linarith
    have h2 : ‖v⁻¹ * v‖ ≤ 1 := by rw [inv_mul_cancel₀ hv]; simp
    obtain ⟨U, V, N, hU, hV, hN⟩ := main v⁻¹ h1 h2
    refine ⟨U, V, N, Or.inr ?_, hN⟩
    exact padicInt_coe_inj (by rw [hV, inv_mul_cancel₀ hv]; rfl)

end Run013
