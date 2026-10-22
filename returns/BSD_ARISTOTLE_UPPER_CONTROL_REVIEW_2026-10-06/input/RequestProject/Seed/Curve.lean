module

public import Mathlib

/-!
# The fixed rank-two seed curve: concrete definitions

This file records, as kernel-checked facts, the concrete Weierstrass data of the seed
curve used throughout the research record.

* `Seed.orig R`  : `y² = x³ - 22735 x² + 106272484 x`  (original model)
* `Seed.curve R` : `y² = x³ - x² - 66020924 x - 65074271436` (global minimal model)

They are defined over an arbitrary commutative ring so that the same equations can be
used over `ℚ`, `ℚ_[p]`, `ZMod n`, quadratic fields, etc.

Nothing here is a statement about Selmer or Tate–Shafarevich groups; those objects are not
available in Mathlib and are treated in the accompanying research documents as explicit
imports.
-/

@[expose] public section

open WeierstrassCurve

namespace Seed

/-- The global minimal model `y² = x³ - x² - 66020924 x - 65074271436`. -/
def curve (R : Type*) [CommRing R] : WeierstrassCurve R :=
  ⟨0, -1, 0, -66020924, -65074271436⟩

/-- The original model `y² = x³ - 22735 x² + 106272484 x`. -/
def orig (R : Type*) [CommRing R] : WeierstrassCurve R :=
  ⟨0, -22735, 0, 106272484, 0⟩

/-- The two models are related by the `u = 1` translation `x = X + 7578`
(Mathlib convention: `X = u² X' + r` with `r = -7578`), so the invariant differential is
preserved. -/
theorem translate_curve_eq_orig (R : Type*) [CommRing R] :
    (⟨1, -7578, 0, 0⟩ : VariableChange R) • curve R = orig R := by
  ext <;> simp [curve, orig, variableChange_a₁, variableChange_a₂, variableChange_a₃,
    variableChange_a₄, variableChange_a₆] <;> norm_num

/-- Minimal discriminant. -/
theorem curve_Δ (R : Type*) [CommRing R] : (curve R).Δ = 16586638656786071143743744 := by
  simp only [curve, Δ, b₂, b₄, b₆, b₈]; norm_num

/-- `c₄` of the minimal model. -/
theorem curve_c₄ (R : Type*) [CommRing R] : (curve R).c₄ = 3169004368 := by
  simp only [curve, c₄, b₂, b₄]; norm_num

/-- Factorisation of the minimal discriminant:
`Δ = 2⁸ · 3² · 2243 · 4547³ · 5843²`. -/
theorem disc_factorization :
    (16586638656786071143743744 : ℤ) = 2 ^ 8 * 3 ^ 2 * 2243 * 4547 ^ 3 * 5843 ^ 2 := by
  norm_num

/-- The primes appearing in the discriminant (and the conductor) are prime. -/
theorem bad_primes_prime :
    Nat.Prime 2 ∧ Nat.Prime 3 ∧ Nat.Prime 2243 ∧ Nat.Prime 4547 ∧ Nat.Prime 5843 := by
  refine ⟨by norm_num, by norm_num, by norm_num, by norm_num, by norm_num⟩

/-- Over any field of characteristic zero the minimal model is an elliptic curve. -/
instance curve_isElliptic (K : Type*) [Field K] [CharZero K] : (curve K).IsElliptic :=
  ⟨by rw [curve_Δ]; exact isUnit_iff_ne_zero.mpr (by norm_num)⟩

/-- The retained basis point `P1 = (-3031, 327384)` lies on the minimal model. -/
theorem P1_nonsingular : (curve ℚ).toAffine.Nonsingular (-3031) 327384 := by
  rw [← Affine.equation_iff_nonsingular, Affine.equation_iff]; simp [curve]; norm_num

/-- The retained basis point `P2 = (-2394, 281520)` lies on the minimal model. -/
theorem P2_nonsingular : (curve ℚ).toAffine.Nonsingular (-2394) 281520 := by
  rw [← Affine.equation_iff_nonsingular, Affine.equation_iff]; simp [curve]; norm_num

/-- The rational `2`-torsion point `T = (-7578, 0)` lies on the minimal model. -/
theorem T_nonsingular : (curve ℚ).toAffine.Nonsingular (-7578) 0 := by
  rw [← Affine.equation_iff_nonsingular, Affine.equation_iff]; simp [curve]; norm_num

/-- `P1` as a point of `E(ℚ)`. -/
noncomputable def P1 : (curve ℚ).toAffine.Point := .some P1_nonsingular
/-- `P2` as a point of `E(ℚ)`. -/
noncomputable def P2 : (curve ℚ).toAffine.Point := .some P2_nonsingular
/-- `T` as a point of `E(ℚ)`. -/
noncomputable def T : (curve ℚ).toAffine.Point := .some T_nonsingular

/-- `T` has order exactly two. -/
theorem T_addOrderOf : addOrderOf T = 2 := by
  have hneg : -T = T := by
    simp [T, Affine.Point.neg_some, Affine.negY, curve]
  have h2 : (2 : ℕ) • T = 0 := by
    rw [two_nsmul, ← sub_neg_eq_add, hneg, sub_self]
  apply addOrderOf_eq_prime h2
  simp [T]

/-- The original-model coordinates of the same three points. -/
theorem orig_points :
    (orig ℚ).toAffine.Equation 4547 327384 ∧ (orig ℚ).toAffine.Equation 5184 281520 ∧
      (orig ℚ).toAffine.Equation 0 0 := by
  refine ⟨?_, ?_, ?_⟩ <;> rw [Affine.equation_iff] <;> simp [orig] <;> norm_num

end Seed
