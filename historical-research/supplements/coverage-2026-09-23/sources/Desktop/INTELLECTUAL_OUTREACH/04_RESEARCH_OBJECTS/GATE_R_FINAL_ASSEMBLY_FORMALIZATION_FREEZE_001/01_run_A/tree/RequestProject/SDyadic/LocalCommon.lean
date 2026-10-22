/-
Common `ℤ_[p]` toolkit and the *parity obstruction*.

The parity obstruction is the standard first step of a descent: if a prime `p` divides `d` exactly
once but does not divide `b`, the covering `n² = d u⁴ + a u²v² + (b/d) v⁴` has no `ℚ_[p]`-point,
because the two sides would have valuations of different parity.  It is proved here for arbitrary
integer coefficients, and is what confines the everywhere-locally-soluble square classes to the
divisors of `b`.
-/
import RequestProject.SDyadic.PadicTools

namespace SDyadic

open Run013

variable {p : ℕ} [hp : Fact p.Prime]

/-! ## Divisibility dictionary for `ℤ_[p]` -/

theorem padicInt_pow_dvd_intCast_iff (k : ℤ) (n : ℕ) :
    ((p : ℤ_[p]) ^ n ∣ (k : ℤ_[p])) ↔ ((p : ℤ) ^ n ∣ k) := by
  rw [← PadicInt.norm_int_le_pow_iff_dvd, PadicInt.norm_le_pow_iff_mem_span_pow,
    Ideal.mem_span_singleton]

theorem padicInt_dvd_intCast_iff (k : ℤ) :
    ((p : ℤ_[p]) ∣ (k : ℤ_[p])) ↔ ((p : ℤ) ∣ k) := by
  simpa using padicInt_pow_dvd_intCast_iff (p := p) k 1

theorem padicInt_isUnit_of_not_dvd {x : ℤ_[p]} (h : ¬ (p : ℤ_[p]) ∣ x) : IsUnit x := by
  rw [PadicInt.isUnit_iff]
  rcases lt_or_eq_of_le (PadicInt.norm_le_one x) with h1 | h1
  · exact absurd ((PadicInt.norm_lt_one_iff_dvd x).mp h1) h
  · exact h1

theorem padicInt_toZMod_eq_zero_iff (x : ℤ_[p]) :
    PadicInt.toZMod x = 0 ↔ (p : ℤ_[p]) ∣ x := by
  rw [← RingHom.mem_ker, PadicInt.ker_toZMod, PadicInt.maximalIdeal_eq_span_p,
    Ideal.mem_span_singleton]

/-- The norm of `p * (unit)` in `ℤ_[p]`. -/
theorem padicInt_norm_p_mul_unit {x : ℤ_[p]} (hx : ¬ (p : ℤ_[p]) ∣ x) :
    ‖(p : ℤ_[p]) * x‖ = ((p : ℝ))⁻¹ := by
  rw [norm_mul, PadicInt.norm_p, PadicInt.isUnit_iff.mp (padicInt_isUnit_of_not_dvd hx), mul_one]

/-! ## The parity obstruction -/

/-- Integral form: with `v_p(d) = 1` and `p ∤ b`, the cleared covering equation has no primitive
`ℤ_[p]`-solution. -/
theorem padicInt_parity_absurd {a b d₀ U V N : ℤ_[p]}
    (hd₀ : ¬ (p : ℤ_[p]) ∣ d₀) (hb : ¬ (p : ℤ_[p]) ∣ b)
    (hprim : ¬((p : ℤ_[p]) ∣ U ∧ (p : ℤ_[p]) ∣ V))
    (heq : ((p : ℤ_[p]) * d₀) * N ^ 2
      = ((p : ℤ_[p]) * d₀) ^ 2 * U ^ 4 + a * ((p : ℤ_[p]) * d₀) * U ^ 2 * V ^ 2 + b * V ^ 4) :
    False := by
  have hπp : Prime ((p : ℤ_[p])) := PadicInt.prime_p
  have hπ0 : ((p : ℤ_[p])) ≠ 0 := hπp.ne_zero
  -- first, `p ∣ V`
  have h1 : (p : ℤ_[p]) ∣ b * V ^ 4 :=
    ⟨d₀ * N ^ 2 - ((p : ℤ_[p]) * d₀ ^ 2 * U ^ 4 + a * d₀ * U ^ 2 * V ^ 2), by
      linear_combination -heq⟩
  have hV : (p : ℤ_[p]) ∣ V := by
    rcases hπp.dvd_mul.mp h1 with h | h
    · exact absurd h hb
    · exact hπp.dvd_of_dvd_pow h
  have hU : ¬ (p : ℤ_[p]) ∣ U := fun h => hprim ⟨h, hV⟩
  obtain ⟨V₁, rfl⟩ := hV
  -- cancel one factor of `p`
  have h2 : d₀ * N ^ 2 = (p : ℤ_[p]) *
      (d₀ ^ 2 * U ^ 4 + a * d₀ * (p : ℤ_[p]) * U ^ 2 * V₁ ^ 2 + b * (p : ℤ_[p]) ^ 2 * V₁ ^ 4) := by
    refine mul_left_cancel₀ hπ0 ?_
    linear_combination heq
  have hN : (p : ℤ_[p]) ∣ N := by
    have : (p : ℤ_[p]) ∣ d₀ * N ^ 2 := ⟨_, h2⟩
    rcases hπp.dvd_mul.mp this with h | h
    · exact absurd h hd₀
    · exact hπp.dvd_of_dvd_pow h
  obtain ⟨N₁, rfl⟩ := hN
  -- cancel a second factor of `p`, and read the result modulo `p`
  have h3 : (p : ℤ_[p]) * (d₀ * N₁ ^ 2)
      = d₀ ^ 2 * U ^ 4 + a * d₀ * (p : ℤ_[p]) * U ^ 2 * V₁ ^ 2 + b * (p : ℤ_[p]) ^ 2 * V₁ ^ 4 := by
    refine mul_left_cancel₀ hπ0 ?_
    linear_combination h2
  have h4 : (p : ℤ_[p]) ∣ d₀ ^ 2 * U ^ 4 :=
    ⟨d₀ * N₁ ^ 2 - (a * d₀ * U ^ 2 * V₁ ^ 2 + b * (p : ℤ_[p]) * V₁ ^ 4), by linear_combination -h3⟩
  rcases hπp.dvd_mul.mp h4 with h | h
  · exact hd₀ (hπp.dvd_of_dvd_pow h)
  · exact hU (hπp.dvd_of_dvd_pow h)

/-- **Parity obstruction.**  If `p` divides `d = p * d₀` exactly once and `p ∤ b`, then the
covering attached to `(a, b)` has no `ℚ_[p]`-point in the class of `d`. -/
theorem not_cov_padic_of_parity {a b d₀ : ℤ} (hd₀ : ¬ (p : ℤ) ∣ d₀) (hb : ¬ (p : ℤ) ∣ b) :
    ¬ Cov ℚ_[p] ((a : ℤ) : ℚ_[p]) ((b : ℤ) : ℚ_[p]) ((((p : ℤ) * d₀ : ℤ)) : ℚ_[p]) := by
  intro hcov
  have hd₀' : ¬ (p : ℤ_[p]) ∣ ((d₀ : ℤ) : ℤ_[p]) := fun h => hd₀ ((padicInt_dvd_intCast_iff _).mp h)
  have hb' : ¬ (p : ℤ_[p]) ∣ ((b : ℤ) : ℤ_[p]) := fun h => hb ((padicInt_dvd_intCast_iff _).mp h)
  have hdne : ((p : ℤ_[p]) * ((d₀ : ℤ) : ℤ_[p])) ≠ 0 := by
    intro h
    rcases mul_eq_zero.mp h with h' | h'
    · exact PadicInt.prime_p.ne_zero h'
    · exact hd₀' (h' ▸ dvd_zero _)
  have hnorm : ((p : ℝ))⁻¹ ≤ ‖(p : ℤ_[p]) * ((d₀ : ℤ) : ℤ_[p])‖ :=
    le_of_eq (padicInt_norm_p_mul_unit hd₀').symm
  have hcov' : Cov ℚ_[p] ((((a : ℤ) : ℤ_[p])) : ℚ_[p]) ((((b : ℤ) : ℤ_[p])) : ℚ_[p])
      (((p : ℤ_[p]) * ((d₀ : ℤ) : ℤ_[p]) : ℤ_[p]) : ℚ_[p]) := by
    have e1 : ((((a : ℤ) : ℤ_[p])) : ℚ_[p]) = ((a : ℤ) : ℚ_[p]) := by push_cast; ring
    have e2 : ((((b : ℤ) : ℤ_[p])) : ℚ_[p]) = ((b : ℤ) : ℚ_[p]) := by push_cast; ring
    have e3 : (((p : ℤ_[p]) * ((d₀ : ℤ) : ℤ_[p]) : ℤ_[p]) : ℚ_[p])
        = (((p : ℤ) * d₀ : ℤ) : ℚ_[p]) := by push_cast; ring
    rw [e1, e2, e3]
    exact hcov
  obtain ⟨U, V, N, hprim, heq⟩ :=
    cov_to_padicInt ((a : ℤ) : ℤ_[p]) ((b : ℤ) : ℤ_[p]) _ hdne hnorm hcov'
  exact padicInt_parity_absurd hd₀' hb' hprim heq

end SDyadic
