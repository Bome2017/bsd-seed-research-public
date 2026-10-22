module

public import RequestProject.Seed.Curve

/-!
# The receiver's auxiliary quadratic point `R_p`, uniformly in `p`

The forward class-group receiver of the research record (wall card W13, source
`FORWARD_RECEIVER_RETAINED.md` §2) uses, for every prime `p`, the integer

  `d_p = 1 - p² - 66020924 p⁴ - 65074271436 p⁶`

and the point `R_p = (p⁻², √d_p · p⁻³)` on the minimal model over `ℚ(√d_p)`.
Its role is to supply the local finite Kummer line at `p` *independently of the rational
basis points*.  This file kernel-checks the elementary arithmetic facts that this step uses,
for **every** prime `p` at once (no finite search):

* `Rp_nonsingular` : `R_p` lies on the minimal model over any characteristic-zero field
  containing a square root of `d_p`;
* `dp_neg` : `d_p < 0`, so `ℚ(√d_p)` is a genuine (imaginary) quadratic field;
* `dp_modEq_one` : `d_p ≡ 1 (mod p²)`;
* `dp_mul_p_not_sq` : `d_p · (±p)` is not a rational square, so `ℚ(√d_p)` is not the quadratic
  subfield `ℚ(√±p)` of `ℚ(μ_p)` (the input to `F_p ∩ ℚ(E[p]) = ℚ` in the record);
* `exists_sqrt_dp_padic` : for odd `p`, `d_p` has a square root `s ∈ ℤ_p` with `‖s‖ = 1`
  (Hensel), so `p` splits in `ℚ(√d_p)`;
* `Rp_padic` : hence `R_p ∈ E(ℚ_p)` with `‖x(R_p)‖ = p²` and formal parameter
  `t(R_p) = -x/y = -p/s` of norm `p⁻¹`, i.e. `R_p ∈ E₁(ℚ_p) \ E₂(ℚ_p)`.

These hold in particular at the bad primes `2243, 4547, 5843`.  What they do **not** give by
themselves is that `R_p` generates `E(ℚ_p)/p E(ℚ_p)`: that needs `[E(ℚ_p) : E₁(ℚ_p)]` prime to
`p` (true at good non-anomalous `p` and at `2243`, `5843`, false at `4547`); see
`RequestProject/Seed/Local4547.lean` and the research return.
-/

@[expose] public section

open WeierstrassCurve

namespace Seed

/-- The receiver's quadratic discriminant `d_p`. -/
def dp (p : ℤ) : ℤ := 1 - p ^ 2 - 66020924 * p ^ 4 - 65074271436 * p ^ 6

/-- `R_p = (p⁻², s p⁻³)` lies on the minimal model whenever `s² = d_p`. -/
theorem Rp_nonsingular {K : Type*} [Field K] [CharZero K] (p : ℤ) (hp : p ≠ 0) (s : K)
    (hs : s ^ 2 = (dp p : K)) :
    (curve K).toAffine.Nonsingular ((p : K) ^ 2)⁻¹ (s * ((p : K) ^ 3)⁻¹) := by
  rw [← Affine.equation_iff_nonsingular, Affine.equation_iff]
  have hp' : (p : K) ≠ 0 := by exact_mod_cast hp
  simp only [curve, dp] at *
  push_cast at hs
  field_simp
  linear_combination hs

/-- `d_p < 0` for every nonzero integer `p`; in particular `ℚ(√d_p)` is imaginary quadratic. -/
theorem dp_neg (p : ℤ) (hp : p ≠ 0) : dp p < 0 := by
  unfold dp
  have : 0 < p ^ 2 := by positivity
  nlinarith [pow_two_nonneg (p ^ 2), pow_two_nonneg (p ^ 3), show p ^ 4 = (p ^ 2) ^ 2 by ring,
    show p ^ 6 = (p ^ 3) ^ 2 by ring]

/-- `d_p` is not a rational square. -/
theorem dp_not_sq (p : ℤ) (hp : p ≠ 0) : ¬ ∃ r : ℚ, r ^ 2 = (dp p : ℚ) := by
  rintro ⟨r, hr⟩
  have h1 : (dp p : ℚ) < 0 := by exact_mod_cast dp_neg p hp
  nlinarith [sq_nonneg r]

/-- `d_p ≡ 1 (mod p²)`. -/
theorem dp_modEq_one (p : ℤ) : dp p ≡ 1 [ZMOD p ^ 2] := by
  apply Int.ModEq.symm
  rw [Int.modEq_iff_dvd]
  exact ⟨-(1 + 66020924 * p ^ 2 + 65074271436 * p ^ 4), by unfold dp; ring⟩

/-- A prime `p` never divides `d_p`. -/
theorem dp_not_dvd (p : ℕ) (hp : p.Prime) : ¬ (p : ℤ) ∣ dp p := by
  intro h
  have : (p : ℤ) ∣ 1 := by
    have h2 : (p : ℤ) ∣ dp p + p * (p + 66020924 * p ^ 3 + 65074271436 * p ^ 5) :=
      dvd_add h (dvd_mul_right _ _)
    have : dp p + p * (p + 66020924 * p ^ 3 + 65074271436 * p ^ 5) = 1 := by unfold dp; ring
    rwa [this] at h2
  have := Int.eq_one_of_dvd_one (by positivity) this
  exact hp.one_lt.ne' (by exact_mod_cast this)

/-- `d_p · (ε p)` is not a rational square for `ε = ±1`.  Hence `ℚ(√d_p)` differs from
`ℚ(√p)` and `ℚ(√-p)`, in particular from the quadratic subfield of `ℚ(μ_p)`. -/
theorem dp_mul_p_not_sq (p : ℕ) [hp : Fact p.Prime] (ε : ℤ) (hε : ε = 1 ∨ ε = -1) :
    ¬ ∃ r : ℚ, r ^ 2 = ((dp p * (ε * p) : ℤ) : ℚ) := by
  rintro ⟨r, hr⟩
  have hd : dp p ≠ 0 := fun h => dp_not_dvd p hp.out (h ▸ dvd_zero _)
  have hεp : ε * (p : ℤ) ≠ 0 := by rcases hε with rfl | rfl <;> simp [hp.out.ne_zero]
  have hr0 : r ≠ 0 := by
    rintro rfl
    have : ((dp p * (ε * p) : ℤ) : ℚ) = 0 := by rw [← hr]; ring
    exact (mul_ne_zero hd hεp) (by exact_mod_cast this)
  have h1 := congrArg (padicValRat p) hr
  rw [padicValRat.pow hr0, padicValRat.of_int, padicValInt.mul hd hεp,
    padicValInt.eq_zero_of_not_dvd (dp_not_dvd p hp.out)] at h1
  have : padicValInt p (ε * p) = 1 := by
    rcases hε with rfl | rfl <;> simp [padicValInt]
  rw [this] at h1
  omega

/-- Hensel: for odd `p`, `d_p` has a unit square root in `ℤ_p`; thus `p` splits in `ℚ(√d_p)`
and both embeddings send `√d_p` to a `p`-adic unit. -/
theorem exists_sqrt_dp_padic (p : ℕ) [hp : Fact p.Prime] (hodd : p ≠ 2) :
    ∃ s : ℤ_[p], s ^ 2 = (dp p : ℤ_[p]) ∧ ‖s‖ = 1 := by
  set F : Polynomial ℤ := Polynomial.X ^ 2 - Polynomial.C (dp p)
  have h2 : ‖((2 : ℤ) : ℤ_[p])‖ = 1 := by
    have : ¬ (p : ℤ) ∣ 2 := by
      intro h
      have := Int.le_of_dvd (by norm_num) h
      have h3 := hp.out.two_le
      have : (p : ℤ) = 2 := by omega
      exact hodd (by exact_mod_cast this)
    rw [← PadicInt.norm_int_lt_one_iff_dvd] at this
    exact le_antisymm (PadicInt.norm_le_one _) (not_lt.mp this)
  have hd : (Polynomial.aeval (1 : ℤ_[p]) (Polynomial.derivative F)) = ((2 : ℤ) : ℤ_[p]) := by
    simp only [F, Polynomial.derivative_sub, Polynomial.derivative_X_pow,
      Polynomial.derivative_C, sub_zero, map_mul, Polynomial.aeval_C, map_pow,
      Polynomial.aeval_X, one_pow, mul_one]
    simp
  have hF : ‖Polynomial.aeval (1 : ℤ_[p]) F‖ < 1 := by
    have : Polynomial.aeval (1 : ℤ_[p]) F = ((1 - dp p : ℤ) : ℤ_[p]) := by simp [F]
    rw [this, PadicInt.norm_int_lt_one_iff_dvd]
    exact ⟨p * (1 + 66020924 * p ^ 2 + 65074271436 * p ^ 4), by unfold dp; ring⟩
  obtain ⟨z, hz, hz1, -, -⟩ :=
    hensels_lemma (F := F) (a := (1 : ℤ_[p])) (by rw [hd, h2]; simpa using hF)
  refine ⟨z, ?_, ?_⟩
  · simpa [F, sub_eq_zero] using hz
  · rw [hd, h2] at hz1
    have := PadicInt.norm_eq_of_norm_add_lt_right (z1 := z) (z2 := -1)
      (by simpa [← sub_eq_add_neg] using hz1)
    simpa using this

/-- For every odd prime `p` there is a point `R_p = (x, y)` of the minimal model over `ℚ_p`
with `x = p⁻²`, `y = s p⁻³` (`s` a unit square root of `d_p`), `‖x‖ = p²` and formal
parameter `t = -x / y` of norm exactly `p⁻¹`: `R_p ∈ E₁(ℚ_p) \ E₂(ℚ_p)`. -/
theorem Rp_padic (p : ℕ) [hp : Fact p.Prime] (hodd : p ≠ 2) :
    ∃ x y : ℚ_[p], (curve ℚ_[p]).toAffine.Nonsingular x y ∧ x = ((p : ℚ_[p]) ^ 2)⁻¹ ∧
      ‖x‖ = (p : ℝ) ^ 2 ∧ ‖-x / y‖ = (p : ℝ)⁻¹ := by
  obtain ⟨s, hs, hs1⟩ := exists_sqrt_dp_padic p hodd
  have hp0 : (p : ℚ_[p]) ≠ 0 := by exact_mod_cast hp.out.ne_zero
  have hs' : ((s : ℚ_[p])) ^ 2 = ((dp (p : ℤ) : ℤ) : ℚ_[p]) := by
    have := congrArg (fun z : ℤ_[p] => (z : ℚ_[p])) hs
    simpa using this
  have hsn : ‖(s : ℚ_[p])‖ = 1 := by simpa using hs1
  have hs0 : (s : ℚ_[p]) ≠ 0 := by
    intro h; rw [h, norm_zero] at hsn; exact zero_ne_one hsn
  have hpn : ‖(p : ℚ_[p])‖ = (p : ℝ)⁻¹ := Padic.norm_p
  refine ⟨((p : ℚ_[p]) ^ 2)⁻¹, (s : ℚ_[p]) * ((p : ℚ_[p]) ^ 3)⁻¹, ?_, rfl, ?_, ?_⟩
  · have := Rp_nonsingular (K := ℚ_[p]) (p : ℤ) (by exact_mod_cast hp.out.ne_zero)
      (s : ℚ_[p]) hs'
    simpa using this
  · rw [norm_inv, norm_pow, hpn, inv_pow, inv_inv]
  · have : -((p : ℚ_[p]) ^ 2)⁻¹ / ((s : ℚ_[p]) * ((p : ℚ_[p]) ^ 3)⁻¹) = -(p : ℚ_[p]) / s := by
      field_simp
    rw [this, norm_div, norm_neg, hpn, hsn, div_one]

end Seed
