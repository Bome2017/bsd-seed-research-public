import RequestProject.R1.Bezout
import RequestProject.Descent.Delta

/-!
# Tying the duplication pair to mathlib's chord–tangent law, and the 2-torsion locus

Two ingredients are supplied here, both for the model `Wab a b : y² = x(x² + a x + b)`.

* `Wab_addX_self` — the `x`-coordinate `mathlib` produces for `P + P` (namely
  `addX x x (slope x x y y)`) satisfies `x(2P) · 4x(x² + ax + b) = (x² − b)²` whenever `y ≠ 0`.
  This is the identity `F/G` of the R1 interface, proved against mathlib's own tangent law rather
  than assumed.
* `hgt_le_of_two_torsion` — the points killed by doubling.  If `x(x² + ax + b) = 0` with integral
  `a, b` and `b ≠ 0`, then `x` is an integer dividing `b` (or `0`), so its height is at most
  `|b| + 1`.  This handles `T = (0,0)` and the whole of `E(ℚ)[2]`, whose `x`-coordinates are
  exactly this locus.
-/

namespace R1

open Descent WeierstrassCurve

/-! ## The duplication identity on mathlib's point group -/

/-- `negY` on `Wab a b` is just `-y`. -/
theorem Wab_negY (a b x y : ℚ) : (Wab a b).toAffine.negY x y = -y := by
  simp [WeierstrassCurve.Affine.negY]

/-- **The duplication identity.**  For a nonsingular affine point `(x, y)` of `Wab a b` with
`y ≠ 0`, the `x`-coordinate of `(x,y) + (x,y)` computed by mathlib's chord–tangent law satisfies
`x(2P) · 4x(x² + ax + b) = (x² − b)²`. -/
theorem Wab_addX_self {a b x y : ℚ} (heq : y ^ 2 = x ^ 3 + a * x ^ 2 + b * x) (hy : y ≠ 0) :
    (Wab a b).toAffine.addX x x ((Wab a b).toAffine.slope x x y y)
      * ((4 : ℚ) * x * (x ^ 2 + a * x + b)) = (x ^ 2 - b) ^ 2 := by
  have hne : y ≠ (Wab a b).toAffine.negY x y := by
    rw [Wab_negY]
    intro h
    exact hy (by linarith)
  have hslope : (Wab a b).toAffine.slope x x y y = (3 * x ^ 2 + 2 * a * x + b) / (2 * y) := by
    rw [WeierstrassCurve.Affine.slope_of_Y_ne rfl hne, Wab_negY]
    simp only [Wab_a₁, Wab_a₂, Wab_a₄]
    congr 1
    · ring
    · ring
  have haddX : (Wab a b).toAffine.addX x x ((Wab a b).toAffine.slope x x y y)
      = ((3 * x ^ 2 + 2 * a * x + b) / (2 * y)) ^ 2 - a - 2 * x := by
    simp only [WeierstrassCurve.Affine.addX, Wab_a₁, Wab_a₂, hslope]
    ring
  have h4 : (4 : ℚ) * x * (x ^ 2 + a * x + b) = 4 * y ^ 2 := by linear_combination -4 * heq
  have h1 : ((3 * x ^ 2 + 2 * a * x + b) / (2 * y)) ^ 2 * (4 * y ^ 2)
      = (3 * x ^ 2 + 2 * a * x + b) ^ 2 := by
    field_simp
    ring
  rw [haddX, h4]
  linear_combination h1 - 4 * (a + 2 * x) * heq

/-! ## The 2-torsion locus -/

/-- A rational root of the monic integral quadratic `X² + aX + b` is an integer dividing `b`. -/
theorem den_eq_one_of_quadratic_root {a b : ℤ} {x : ℚ}
    (hroot : x ^ 2 + (a : ℚ) * x + (b : ℚ) = 0) : x.den = 1 ∧ x.num ∣ b := by
  have hvpos : (0 : ℤ) < (x.den : ℤ) := by exact_mod_cast x.pos
  have hcop : IsCoprime x.num ((x.den : ℤ)) := by
    rw [Int.isCoprime_iff_gcd_eq_one]
    simpa [Int.gcd] using x.reduced
  have hxnum : (x.num : ℚ) = x * (x.den : ℚ) := (Rat.mul_den_eq_num x).symm
  have hint : x.num ^ 2 + a * x.num * (x.den : ℤ) + b * (x.den : ℤ) ^ 2 = 0 := by
    have h : ((x.num ^ 2 + a * x.num * (x.den : ℤ) + b * (x.den : ℤ) ^ 2 : ℤ) : ℚ) = ((0 : ℤ) : ℚ) := by
      push_cast
      rw [hxnum]
      linear_combination ((x.den : ℚ) ^ 2) * hroot
    exact_mod_cast h
  -- the denominator divides `x.num ^ 2`, hence is a unit
  have hdvd : (x.den : ℤ) ∣ x.num ^ 2 := ⟨-(a * x.num + b * (x.den : ℤ)), by linarith [hint]⟩
  have hden : (x.den : ℤ) = 1 := by
    have hcop2 : IsCoprime (x.num ^ 2) ((x.den : ℤ)) := hcop.pow_left
    obtain ⟨s, t, hst⟩ := hcop2
    have h1 : (x.den : ℤ) ∣ 1 := by
      rw [← hst]
      exact dvd_add (Dvd.dvd.mul_left hdvd s) (Dvd.dvd.mul_left dvd_rfl t)
    exact Int.eq_one_of_dvd_one (le_of_lt hvpos) h1
  have hden' : x.den = 1 := by exact_mod_cast hden
  refine ⟨hden', ?_⟩
  refine ⟨-(x.num + a), ?_⟩
  rw [hden] at hint
  linarith [hint]

/-- **The points killed by doubling.**  If `x(x² + ax + b) = 0` with `a, b` integral and `b ≠ 0`,
then the height of `x` is at most `|b| + 1`.  This covers `x = 0` (the point `T = (0,0)`) and the
two remaining `2`-torsion `x`-coordinates. -/
theorem hgt_le_of_two_torsion {a b : ℤ} (hb : b ≠ 0) {x : ℚ}
    (hroot : x * (x ^ 2 + (a : ℚ) * x + (b : ℚ)) = 0) : hgt x ≤ b.natAbs + 1 := by
  rcases mul_eq_zero.mp hroot with hx | hq
  · subst hx
    simp [hgt]
  · obtain ⟨hden, hdvd⟩ := den_eq_one_of_quadratic_root hq
    have hnum : x.num.natAbs ≤ b.natAbs :=
      Nat.le_of_dvd (Int.natAbs_pos.mpr hb) (Int.natAbs_dvd_natAbs.mpr hdvd)
    simp only [hgt, hden]
    omega

end R1
