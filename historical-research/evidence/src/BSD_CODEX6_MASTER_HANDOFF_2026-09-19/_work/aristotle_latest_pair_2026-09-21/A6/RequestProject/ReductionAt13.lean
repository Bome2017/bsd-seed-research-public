import Mathlib
import RequestProject.SeedData

/-!
# Certified reduction data of the seed curve at the prime `13`

This file machine-checks, from the integral model recorded in `RequestProject/SeedData.lean`,
the *preliminary arithmetic input* needed before any `13`-primary computation is attempted:

* `13` is a prime of **good reduction**: `13 ∤ Δ` and `13 ∤ N`;
* the reduction of the seed model modulo `13` is the Weierstrass curve
  `W13 : y² = x³ + 2x² + 6x` over `𝔽₁₃` (`seed_reduction_at_13`), and it is nonsingular
  (`W13_Δ_ne_zero`);
* the **exact point count** `#E(𝔽₁₃) = 18` (`card_points_mod_13`), obtained by an exhaustive
  kernel evaluation over all `169` affine pairs together with the unique point at infinity —
  not by a numerical or table lookup;
* hence `a₁₃ = 13 + 1 - 18 = -4` (`a_thirteen_eq`), which satisfies the Hasse bound
  (`a_thirteen_hasse`);
* `13 ∤ a₁₃`, so `13` is a prime of **good ordinary reduction** (`ordinary_at_13`).

Everything here is an exact finite computation about the reduced curve.  **Nothing in this file
says anything about `Ш`**: it is exactly the independent verification of the preliminary data
`#E(𝔽₁₃) = 18`, `a₁₃ = -4`, `13 ∤ N`, and it is a *prerequisite* for — not a step of — any
`13`-primary argument.  No analytic input, no `L`-value, no coefficient corpus and no
finiteness assumption is used or implied.

The point count is taken in Mathlib's affine model `WeierstrassCurve.Affine.Point`, whose terms
are the point at infinity together with the nonsingular affine solutions; since `Δ ≠ 0` over
`𝔽₁₃`, *every* affine solution is nonsingular (`WeierstrassCurve.Affine.Point` is therefore in
bijection with `Option` of the solution set), which is the content of `pointEquiv13`.
-/

namespace SeedBSD

namespace ReductionAt13

/-! ## Good reduction at `13` -/

/-- `13` does not divide the discriminant of the seed model, so the reduction at `13` is good
(and the model is automatically `13`-minimal). -/
theorem thirteen_not_dvd_disc : ¬ ((13 : ℤ) ∣ Δ) := by decide

/-- `13` does not divide the conductor `N = 2³ · 3 · 2243 · 4547² · 5843`. -/
theorem thirteen_not_dvd_conductor : ¬ (13 ∣ N) := by decide

/-! ## The reduced curve over `𝔽₁₃` -/

/-- The seed model `y² = x³ + a₂x² + a₄x` as a Weierstrass curve over `ℤ`. -/
def Wseed : WeierstrassCurve ℤ := ⟨0, a₂, 0, a₄, 0⟩

/-- The reduction `y² = x³ + 2x² + 6x` of the seed model modulo `13`. -/
def W13 : WeierstrassCurve (ZMod 13) := ⟨0, 2, 0, 6, 0⟩

/-- The reduction of the seed model modulo `13` is `W13`: indeed `a₂ = -22735 ≡ 2` and
`a₄ = 106272484 ≡ 6 (mod 13)`. -/
theorem seed_reduction_at_13 : Wseed.map (Int.castRingHom (ZMod 13)) = W13 := by
  simp only [WeierstrassCurve.map, Wseed, W13, a₂, a₄, WeierstrassCurve.mk.injEq]
  refine ⟨by decide, by decide, by decide, by decide, by decide⟩

/-- The reduced curve is nonsingular: `Δ(W13) = 11 ≠ 0` in `𝔽₁₃`. -/
theorem W13_Δ_ne_zero : W13.Δ ≠ 0 := by decide

/-- The Weierstrass equation of `W13` in explicit form. -/
theorem W13_equation_iff (x y : ZMod 13) :
    W13.toAffine.Equation x y ↔ y ^ 2 = x ^ 3 + 2 * x ^ 2 + 6 * x := by
  rw [WeierstrassCurve.Affine.equation_iff]
  constructor <;> intro h <;> · simp only [W13] at *; linear_combination h

instance : DecidablePred fun p : ZMod 13 × ZMod 13 => W13.toAffine.Equation p.1 p.2 :=
  fun p => decidable_of_iff _ (W13_equation_iff p.1 p.2).symm

/-- The set of affine `𝔽₁₃`-solutions of `y² = x³ + 2x² + 6x`. -/
def affineSolutions : Finset (ZMod 13 × ZMod 13) :=
  Finset.univ.filter fun p => p.2 ^ 2 = p.1 ^ 3 + 2 * p.1 ^ 2 + 6 * p.1

/-- There are exactly `17` affine points: the `2`-torsion point `(0,0)` together with the
`8` values of `x` for which `x³ + 2x² + 6x` is a nonzero square, each contributing two points. -/
theorem card_affineSolutions : affineSolutions.card = 17 := by decide

/-- Since `Δ ≠ 0` over `𝔽₁₃`, the points of the affine model are the point at infinity together
with *all* affine solutions of the Weierstrass equation. -/
def pointEquiv13 :
    W13.toAffine.Point ≃ Option {p : ZMod 13 × ZMod 13 // W13.toAffine.Equation p.1 p.2} where
  toFun P := match P with
    | .zero => none
    | .some h => some ⟨(_, _), h.1⟩
  invFun o := match o with
    | none => .zero
    | some ⟨_, h⟩ =>
        .some ((WeierstrassCurve.Affine.equation_iff_nonsingular_of_Δ_ne_zero W13_Δ_ne_zero).mp h)
  left_inv P := by cases P <;> rfl
  right_inv o := by rcases o with _ | ⟨⟨x, y⟩, h⟩ <;> rfl

instance : Fintype W13.toAffine.Point := Fintype.ofEquiv _ pointEquiv13.symm

/-- **`#E(𝔽₁₃) = 18`.**  Exhaustive exact count: `17` affine points plus the point at infinity. -/
theorem card_points_mod_13 : Fintype.card W13.toAffine.Point = 18 := by
  rw [Fintype.card_congr pointEquiv13, Fintype.card_option, Fintype.card_subtype]
  decide

/-! ## The trace of Frobenius at `13` -/

/-- The trace of Frobenius at `13`, defined from the certified point count by
`a₁₃ = p + 1 - #E(𝔽ₚ)`. -/
def aThirteen : ℤ := (13 : ℤ) + 1 - (Fintype.card W13.toAffine.Point : ℤ)

/-- **`a₁₃ = -4`.** -/
theorem a_thirteen_eq : aThirteen = -4 := by
  rw [aThirteen, card_points_mod_13]; norm_num

/-- The Hasse bound `a₁₃² ≤ 4 · 13` is satisfied (`16 ≤ 52`), a consistency check on the count. -/
theorem a_thirteen_hasse : aThirteen ^ 2 ≤ 4 * 13 := by rw [a_thirteen_eq]; norm_num

/-- **`13` is a prime of good ordinary reduction**: the reduction is good
(`thirteen_not_dvd_disc`) and `13 ∤ a₁₃ = -4`. -/
theorem ordinary_at_13 : ¬ ((13 : ℤ) ∣ aThirteen) := by
  rw [a_thirteen_eq]; decide

end ReductionAt13

end SeedBSD
