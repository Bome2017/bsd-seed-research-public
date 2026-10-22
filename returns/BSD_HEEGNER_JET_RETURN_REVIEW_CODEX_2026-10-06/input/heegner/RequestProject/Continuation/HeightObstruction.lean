module

public import Mathlib

/-!
# Archimedean heights cannot certify the cross-prime Kolyvagin index

New Lean source for the 2026-10-06 continuation run (`research_return/PROOF.md`, §4).

Notation: `m = ℓ + 1`, `y = y_ℓ` the Heegner point of conductor `ℓ`, and `D y` its Kolyvagin
derivative. Decompose the Néron–Tate height over the characters `χ` of `G_ℓ ≅ ℤ/m`. The
component `e_χ (D y)` is `λ_χ · e_χ y` with `λ_χ = m / (χ(σ) - 1)` when `χ(σ) ≠ 1`
(`Continuation.CrossPrime.derivative_root_of_unity`). When `a_ℓ = 0`, the trivial
component of `y` vanishes. The two lemmas below give the inequalities used:

* `norm_sq_div_sub_one_ge`: `‖m / (ζ - 1)‖² ≥ m² / 4` for `‖ζ‖ = 1`, `ζ ≠ 1`.
* `weighted_sum_ge`: hence `ĥ(D y) = Σ_χ |λ_χ|² ĥ(e_χ y) ≥ (m² / 4) ĥ(y)`.

`height_obstruction` is the resulting no-go statement. Let `μ` be any lower bound for the
heights of non-torsion points of `E(H_ℓ)`; the point `y` itself shows `μ ≤ ĥ(y)`. Then
`ĥ(D y) / p² ≥ μ` for every odd prime `p ∣ m` with `m` even. A hypothetical `Q` with
`p Q = D y` would have height `ĥ(D y) / p² ≥ μ`. So no lower bound for heights can rule out
the `p`-divisibility of `D y`, however sharp it is.
-/

@[expose] public section

namespace Continuation.Height

open Finset

/-- For `ζ` on the unit circle, `ζ ≠ 1`: `‖m / (ζ - 1)‖² ≥ m² / 4`. -/
theorem norm_sq_div_sub_one_ge (m : ℝ) (ζ : ℂ) (hζ : ‖ζ‖ = 1) (hne : ζ ≠ 1) :
    m ^ 2 / 4 ≤ ‖(m : ℂ) / (ζ - 1)‖ ^ 2 := by
  have h1 : ‖ζ - 1‖ ≤ 2 := by
    calc ‖ζ - 1‖ ≤ ‖ζ‖ + ‖(1 : ℂ)‖ := norm_sub_le _ _
      _ = 2 := by rw [hζ, norm_one]; norm_num
  have h0 : 0 < ‖ζ - 1‖ := norm_pos_iff.mpr (sub_ne_zero.mpr hne)
  rw [norm_div, Complex.norm_real, div_pow, Real.norm_eq_abs, sq_abs]
  rw [div_le_div_iff₀ (by norm_num) (by positivity)]
  have : ‖ζ - 1‖ ^ 2 ≤ 4 := by nlinarith
  nlinarith [sq_nonneg m]

/-- Weighted orthogonal sum: if every coefficient satisfies `|λ_k|² ≥ c` and every weight is
nonnegative, then `Σ |λ_k|² h_k ≥ c Σ h_k`. -/
theorem weighted_sum_ge {ι : Type*} (s : Finset ι) (c : ℝ) (lam h : ι → ℝ)
    (hlam : ∀ k ∈ s, c ≤ lam k) (hh : ∀ k ∈ s, 0 ≤ h k) :
    c * ∑ k ∈ s, h k ≤ ∑ k ∈ s, lam k * h k := by
  rw [mul_sum]
  exact sum_le_sum fun k hk => mul_le_mul_of_nonneg_right (hlam k hk) (hh k hk)

/-- Lower bound for the height of the Kolyvagin derivative in its character decomposition:
`Σ_k ‖m / (ζ_k - 1)‖² h_k ≥ (m² / 4) Σ_k h_k`, for characters with `ζ_k ≠ 1` on the unit circle
and nonnegative component heights `h_k`. -/
theorem derivative_height_lower_bound {ι : Type*} (s : Finset ι) (m : ℝ) (ζ : ι → ℂ)
    (h : ι → ℝ) (hζ : ∀ k ∈ s, ‖ζ k‖ = 1) (hne : ∀ k ∈ s, ζ k ≠ 1)
    (hh : ∀ k ∈ s, 0 ≤ h k) :
    m ^ 2 / 4 * ∑ k ∈ s, h k ≤ ∑ k ∈ s, ‖(m : ℂ) / (ζ k - 1)‖ ^ 2 * h k :=
  weighted_sum_ge s _ _ h (fun k hk => norm_sq_div_sub_one_ge m (ζ k) (hζ k hk) (hne k hk)) hh

/-- **Height obstruction.** Let `m > 0` be even and `p` an odd prime dividing `m`. Suppose
`ĥ(D y) ≥ (m² / 4) ĥ(y)` and `μ ≤ ĥ(y)`. Then `ĥ(D y) / p² ≥ μ`: a point `Q` with
`p Q = D y` would not violate the height lower bound `μ`. -/
theorem height_obstruction (m p : ℕ) (hm0 : 0 < m) (hp : p.Prime) (hp2 : p ≠ 2) (hm : 2 ∣ m)
    (hpm : p ∣ m) (hD hy μ : ℝ) (hlow : (m : ℝ) ^ 2 / 4 * hy ≤ hD) (hμ : μ ≤ hy)
    (hy0 : 0 ≤ hy) : μ ≤ hD / (p : ℝ) ^ 2 := by
  have hcop : Nat.Coprime 2 p :=
    (Nat.coprime_primes Nat.prime_two hp).mpr (Ne.symm hp2)
  obtain ⟨k, hk⟩ : 2 * p ∣ m := Nat.Coprime.mul_dvd_of_dvd_of_dvd hcop hm hpm
  have hp0 : (0 : ℝ) < p := by exact_mod_cast hp.pos
  have hm' : (2 * p : ℝ) ≤ m := by
    have hk0 : 0 < k := Nat.pos_of_ne_zero (by rintro rfl; simp at hk; omega)
    have : (2 * p : ℕ) ≤ m := by rw [hk]; exact Nat.le_mul_of_pos_right _ hk0
    exact_mod_cast this
  rw [le_div_iff₀ (by positivity)]
  have hsq : (p : ℝ) ^ 2 ≤ (m : ℝ) ^ 2 / 4 := by nlinarith
  nlinarith [mul_le_mul_of_nonneg_right hsq hy0]

end Continuation.Height
