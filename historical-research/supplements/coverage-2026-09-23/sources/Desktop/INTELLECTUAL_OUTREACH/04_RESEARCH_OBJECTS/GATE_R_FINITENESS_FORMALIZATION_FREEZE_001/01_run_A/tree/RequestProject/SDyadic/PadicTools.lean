/-
Bridging `Run013.Cov ℚ_[p]` to an integral, primitive solution over `ℤ_[p]`.

The covering equation in its cleared form `d n² = d²u⁴ + a d u²v² + b v⁴` is weighted-homogeneous,
so a projective solution can always be rescaled so that `u, v ∈ ℤ_[p]` with at least one of them a
unit.  If moreover `a, b ∈ ℤ_[p]` and `‖d‖ ≥ p⁻¹` (i.e. `v_p(d) ≤ 1`), the third coordinate `n` is
then forced to be integral as well.  This is the only entry point used by the local analyses.
-/
import RequestProject.SDyadic.CovAlg

namespace SDyadic

open Run013

variable {p : ℕ} [hp : Fact p.Prime]

/-- The `p`-adic norm is discrete: a norm whose square is at most `p` is at most `1`. -/
theorem padic_norm_le_one_of_sq_le {n : ℚ_[p]} (h : ‖n‖ ^ 2 ≤ (p : ℝ)) : ‖n‖ ≤ 1 := by
  have hp1 : (1 : ℝ) < (p : ℝ) := by exact_mod_cast hp.out.one_lt
  by_contra hcon
  push_neg at hcon
  have hn0 : n ≠ 0 := by rintro rfl; simp at hcon; linarith
  have hval : n.valuation < 0 := by
    by_contra hv
    push_neg at hv
    exact absurd ((Padic.norm_le_one_iff_val_nonneg n).mpr hv) (not_le.mpr hcon)
  have hle : (1 : ℤ) ≤ -n.valuation := by omega
  have hnorm : ‖n‖ = (p : ℝ) ^ (-n.valuation) := Padic.norm_eq_zpow_neg_valuation hn0
  have hge : (p : ℝ) ≤ ‖n‖ := by
    rw [hnorm]
    calc (p : ℝ) = (p : ℝ) ^ (1 : ℤ) := by norm_num
      _ ≤ (p : ℝ) ^ (-n.valuation) := by
          exact zpow_le_zpow_right₀ (le_of_lt hp1) hle
  nlinarith [norm_nonneg n]

/-- Any projective pair `(u, v) ≠ (0,0)` in `ℚ_[p]` can be rescaled to a primitive integral pair. -/
theorem exists_primitive_scaling {u v : ℚ_[p]} (huv : ¬(u = 0 ∧ v = 0)) :
    ∃ c : ℚ_[p], ‖c * u‖ ≤ 1 ∧ ‖c * v‖ ≤ 1 ∧ (‖c * u‖ = 1 ∨ ‖c * v‖ = 1) := by
  rcases le_total ‖v‖ ‖u‖ with hle | hle
  · have hu : u ≠ 0 := by
      rintro rfl
      exact huv ⟨rfl, by simpa using norm_le_zero_iff.mp (by simpa using hle)⟩
    refine ⟨u⁻¹, ?_, ?_, Or.inl ?_⟩
    · rw [inv_mul_cancel₀ hu]; simp
    · rw [norm_mul, norm_inv]
      rw [inv_mul_le_iff₀ (norm_pos_iff.mpr hu)]
      simpa using hle
    · rw [inv_mul_cancel₀ hu]; simp
  · have hv : v ≠ 0 := by
      rintro rfl
      exact huv ⟨by simpa using norm_le_zero_iff.mp (by simpa using hle), rfl⟩
    refine ⟨v⁻¹, ?_, ?_, Or.inr ?_⟩
    · rw [norm_mul, norm_inv]
      rw [inv_mul_le_iff₀ (norm_pos_iff.mpr hv)]
      simpa using hle
    · rw [inv_mul_cancel₀ hv]; simp
    · rw [inv_mul_cancel₀ hv]; simp

/-- **The bridge.**  A `ℚ_[p]`-point of the covering with integral coefficients and
`v_p(d) ≤ 1` yields an integral, primitive solution of the cleared equation over `ℤ_[p]`. -/
theorem cov_to_padicInt (a b d : ℤ_[p]) (hd : d ≠ 0) (hdn : ((p : ℝ))⁻¹ ≤ ‖d‖)
    (h : Cov ℚ_[p] (a : ℚ_[p]) (b : ℚ_[p]) (d : ℚ_[p])) :
    ∃ U V N : ℤ_[p], ¬((p : ℤ_[p]) ∣ U ∧ (p : ℤ_[p]) ∣ V) ∧
      d * N ^ 2 = d ^ 2 * U ^ 4 + a * d * U ^ 2 * V ^ 2 + b * V ^ 4 := by
  have hp0 : (0 : ℝ) < (p : ℝ) := by
    exact_mod_cast hp.out.pos
  have hd' : (d : ℚ_[p]) ≠ 0 := by simpa using hd
  rw [cov_iff_covH hd'] at h
  obtain ⟨u, v, n, huv, heq⟩ := h
  obtain ⟨c, hcu, hcv, hprim⟩ := exists_primitive_scaling huv
  have heq' : (d : ℚ_[p]) * (c ^ 2 * n) ^ 2 =
      (d : ℚ_[p]) ^ 2 * (c * u) ^ 4 + (a : ℚ_[p]) * (d : ℚ_[p]) * (c * u) ^ 2 * (c * v) ^ 2
        + (b : ℚ_[p]) * (c * v) ^ 4 := covH_scale c heq
  set u' : ℚ_[p] := c * u with hu'def
  set v' : ℚ_[p] := c * v with hv'def
  set n' : ℚ_[p] := c ^ 2 * n with hn'def
  obtain ⟨U, hU⟩ : ∃ U : ℤ_[p], (U : ℚ_[p]) = u' := ⟨⟨u', hcu⟩, rfl⟩
  obtain ⟨V, hV⟩ : ∃ V : ℤ_[p], (V : ℚ_[p]) = v' := ⟨⟨v', hcv⟩, rfl⟩
  -- bound the right-hand side, by exhibiting it as the image of an element of `ℤ_[p]`
  have hR : ‖(d : ℚ_[p]) ^ 2 * u' ^ 4 + (a : ℚ_[p]) * (d : ℚ_[p]) * u' ^ 2 * v' ^ 2
      + (b : ℚ_[p]) * v' ^ 4‖ ≤ 1 := by
    have hcoe : ((d ^ 2 * U ^ 4 + a * d * U ^ 2 * V ^ 2 + b * V ^ 4 : ℤ_[p]) : ℚ_[p])
        = (d : ℚ_[p]) ^ 2 * u' ^ 4 + (a : ℚ_[p]) * (d : ℚ_[p]) * u' ^ 2 * v' ^ 2
          + (b : ℚ_[p]) * v' ^ 4 := by
      rw [← hU, ← hV]; push_cast; ring
    rw [← hcoe, ← PadicInt.norm_def]
    exact PadicInt.norm_le_one _
  have hn' : ‖n'‖ ≤ 1 := by
    apply padic_norm_le_one_of_sq_le
    have hkey : ‖(d : ℚ_[p])‖ * ‖n'‖ ^ 2 ≤ 1 := by
      have h0 : ‖(d : ℚ_[p]) * n' ^ 2‖ ≤ 1 := by rw [heq']; exact hR
      rwa [norm_mul, norm_pow] at h0
    have hx : (0 : ℝ) ≤ ‖n'‖ ^ 2 := sq_nonneg _
    have h1 : ((p : ℝ))⁻¹ * ‖n'‖ ^ 2 ≤ 1 :=
      le_trans (mul_le_mul_of_nonneg_right hdn hx) hkey
    have h2 := mul_le_mul_of_nonneg_left h1 (le_of_lt hp0)
    have hpc : (p : ℝ) * ((p : ℝ))⁻¹ = 1 := mul_inv_cancel₀ (ne_of_gt hp0)
    nlinarith
  obtain ⟨N, hN⟩ : ∃ N : ℤ_[p], (N : ℚ_[p]) = n' := ⟨⟨n', hn'⟩, rfl⟩
  refine ⟨U, V, N, ?_, ?_⟩
  · rintro ⟨h1, h2⟩
    rw [← PadicInt.norm_lt_one_iff_dvd] at h1 h2
    rw [PadicInt.norm_def, hU] at h1
    rw [PadicInt.norm_def, hV] at h2
    rcases hprim with hx | hx
    · exact absurd hx (ne_of_lt h1)
    · exact absurd hx (ne_of_lt h2)
  · have hfin : ((d * N ^ 2 : ℤ_[p]) : ℚ_[p])
        = ((d ^ 2 * U ^ 4 + a * d * U ^ 2 * V ^ 2 + b * V ^ 4 : ℤ_[p]) : ℚ_[p]) := by
      push_cast
      rw [hU, hV, hN]
      exact heq'
    exact Subtype.ext hfin

end SDyadic
