/-
Run013 — `Curves.lean`

The exact frozen models of `TARGET.md` §1:

* the base curve `E : v^2 + u v + v = u^3 - u^2 - u + 1` (Cremona `62a1`, LMFDB `62.a4`);
* the change of variables `X = 4(u+1)`, `Y = 8v + 4u + 4` identifying it with
  `E_1 : Y^2 = X^3 - 15 X^2 + 64 X`;
* the twisted models

      E_q  : y^2 = x^3 - 15 q x^2 + 64 q^2 x,
      E'_q : y^2 = x^3 + 30 q x^2 - 31 q^2 x = x (x - q) (x + 31 q);

* their discriminants, and their rational two-torsion.

Nothing here is a redefinition: the equations are copied literally from the handoff.
-/
import Mathlib

namespace Run013

open WeierstrassCurve

/-! ## Weierstrass models -/

/-- The base curve `62a1`: `v^2 + u v + v = u^3 - u^2 - u + 1`. -/
def E62Curve : WeierstrassCurve ℚ := ⟨1, -1, 1, -1, 1⟩

/-- The frozen model `E_q : y^2 = x^3 - 15 q x^2 + 64 q^2 x`. -/
def EqCurve (q : ℚ) : WeierstrassCurve ℚ := ⟨0, -15 * q, 0, 64 * q ^ 2, 0⟩

/-- The frozen model `E'_q : y^2 = x^3 + 30 q x^2 - 31 q^2 x`. -/
def EqPrimeCurve (q : ℚ) : WeierstrassCurve ℚ := ⟨0, 30 * q, 0, -31 * q ^ 2, 0⟩

/-! ## Discriminants -/

theorem E62Curve_Δ : E62Curve.Δ = -(2 ^ 4) * 31 := by
  simp [E62Curve, WeierstrassCurve.Δ, WeierstrassCurve.b₂, WeierstrassCurve.b₄,
    WeierstrassCurve.b₆, WeierstrassCurve.b₈]
  norm_num

theorem EqCurve_Δ (q : ℚ) : (EqCurve q).Δ = -(2 ^ 16) * 31 * q ^ 6 := by
  simp [EqCurve, WeierstrassCurve.Δ, WeierstrassCurve.b₂, WeierstrassCurve.b₄,
    WeierstrassCurve.b₆, WeierstrassCurve.b₈]
  ring

theorem EqPrimeCurve_Δ (q : ℚ) : (EqPrimeCurve q).Δ = 2 ^ 14 * 31 ^ 2 * q ^ 6 := by
  simp [EqPrimeCurve, WeierstrassCurve.Δ, WeierstrassCurve.b₂, WeierstrassCurve.b₄,
    WeierstrassCurve.b₆, WeierstrassCurve.b₈]
  ring

theorem EqCurve_nonsingular (q : ℚ) (hq : q ≠ 0) : (EqCurve q).Δ ≠ 0 := by
  rw [EqCurve_Δ]
  positivity

theorem EqPrimeCurve_nonsingular (q : ℚ) (hq : q ≠ 0) : (EqPrimeCurve q).Δ ≠ 0 := by
  rw [EqPrimeCurve_Δ]
  positivity

/-! ## The frozen change of variables -/

/-- `X = 4(u+1)`, `Y = 8v + 4u + 4` identifies `62a1` with `Y^2 = X^3 - 15 X^2 + 64 X`. -/
theorem model_62a1 (u v X Y : ℚ) (hX : X = 4 * (u + 1)) (hY : Y = 8 * v + 4 * u + 4) :
    (v ^ 2 + u * v + v = u ^ 3 - u ^ 2 - u + 1) ↔ (Y ^ 2 = X ^ 3 - 15 * X ^ 2 + 64 * X) := by
  subst hX hY
  constructor
  · intro h; linear_combination 64 * h
  · intro h; linear_combination h / 64

/-- `E_q` is the quadratic twist of `E_1` by `q`. -/
theorem twist_relation (q X Y : ℚ) (hq : q ≠ 0) :
    (q * Y ^ 2 = X ^ 3 - 15 * X ^ 2 + 64 * X) ↔
      ((q ^ 2 * Y) ^ 2 = (q * X) ^ 3 - 15 * q * (q * X) ^ 2 + 64 * q ^ 2 * (q * X)) := by
  constructor
  · intro h; linear_combination q ^ 3 * h
  · intro h
    have h3 : (q : ℚ) ^ 3 ≠ 0 := pow_ne_zero 3 hq
    apply mul_left_cancel₀ h3
    linear_combination h

/-! ## Rational two-torsion -/

/-- `E'_q` has full rational two-torsion: `x^3 + 30 q x^2 - 31 q^2 x = x (x - q) (x + 31 q)`. -/
theorem EqPrime_factor (q x : ℚ) :
    x ^ 3 + 30 * q * x ^ 2 - 31 * q ^ 2 * x = x * (x - q) * (x + 31 * q) := by ring

theorem EqPrime_two_torsion (q x : ℚ) (hq : q ≠ 0) :
    x ^ 3 + 30 * q * x ^ 2 - 31 * q ^ 2 * x = 0 ↔ x = 0 ∨ x = q ∨ x = -(31 * q) := by
  rw [EqPrime_factor]
  constructor
  · intro h
    rcases mul_eq_zero.mp h with h1 | h1
    · rcases mul_eq_zero.mp h1 with h2 | h2
      · exact Or.inl h2
      · exact Or.inr (Or.inl (by linarith))
    · exact Or.inr (Or.inr (by linarith))
  · rintro (rfl | rfl | rfl) <;> ring

/-- `E_q` has exactly one nontrivial rational two-torsion point, namely `(0,0)`:
the quadratic factor `x^2 - 15 q x + 64 q^2` has discriminant `-31 q^2 < 0`. -/
theorem Eq_two_torsion (q x : ℚ) (hq : 0 < q) :
    x ^ 3 - 15 * q * x ^ 2 + 64 * q ^ 2 * x = 0 ↔ x = 0 := by
  constructor
  · intro h
    by_contra hx
    have hfac : x * (x ^ 2 - 15 * q * x + 64 * q ^ 2) = 0 := by linear_combination h
    have hquad : x ^ 2 - 15 * q * x + 64 * q ^ 2 = 0 := by
      rcases mul_eq_zero.mp hfac with h1 | h1
      · exact absurd h1 hx
      · exact h1
    nlinarith [sq_nonneg (2 * x - 15 * q), sq_nonneg q, mul_pos hq hq]
  · rintro rfl; ring

end Run013
