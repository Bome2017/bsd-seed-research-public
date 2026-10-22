import RequestProject.P04c.TwoDescent
import RequestProject.R1.Duplication

namespace R1

open Run013 SDyadic Descent P01 P03a P03c P04c WeierstrassCurve

/-! # TARGET R1 — `H41_MULTIPLICATIVE_DUPLICATION_HEIGHT`

**PRIMARY target of this packet.**  The actual arithmetic gate for Gate R.

    ∃ C ≥ 1, ∀ P : E_q(ℚ),   H(P)^4 ≤ C * H(P + P)

on `(P01.Ecurve ε m q).toAffine.Point` — mathlib's own rational point group — with `H` the
integer multiplicative height of the reduced `x`-coordinate.

## Why this and not an abstract lemma

This inequality is the missing arithmetic premise.  Nothing in the completed H¹-free programme
supplies it, and no abstract height/descent lemma can: an abstract theorem assuming bounded
halving does not establish bounded halving for these curves.  That is the whole point of making
this the primary target.

## The mathematical interface

Put `a = A·q` and `b = r²q²`.  For `y² = x(x² + a x + b)` the duplication of the `x`-coordinate
is given by the degree-four homogeneous pair

    F(X,Z) = (X² − b Z²)²
    G(X,Z) = 4 X Z (X² + a X Z + b Z²)

so that `x(2P) = F(x,1) / G(x,1)`.  This identity was checked symbolically against the
chord-tangent law before this handoff was written; it is **not** supplied as a proved lemma here,
and tying it to mathlib's `P + P` is part of the work.

`b ≠ 0` and `a² − 4b ≠ 0` hold by `P01.dualB_ne_zero` and `P01.dualA_disc_ne_zero`.  Their use
must stay visible: they are what makes `Res(F,G) ≠ 0`.

## The two distinct estimate obligations

1. **Before reduction.**  A lower bound on the size of `(F(u,v), G(u,v))` in terms of
   `max(|u|,v)^4`.
2. **Cancellation after reduction.**  A curve-dependent bound on `gcd(F(u,v), G(u,v))` when the
   pair is reduced to coprime projective coordinates.

**A no-common-projective-zero argument alone is insufficient**, and both design audits say so
independently.  Obligation 2 is the hard one.  A resultant/Bézout certificate is one possible
implementation, not an assumed theorem.  For orientation only, the exact resultants at the two
certified instances are `9.61…e25` (ε=1,m=3,q=13) and `1.14…e21` (ε=−1,m=3,q=5), and the largest
cancellation observed in a bounded sweep was `2.79e8` resp. `8.45e7` — so `C` is genuinely large
and genuinely curve-dependent.

## Boundary

`C` may depend on `ε, m, q`.  A single constant uniform over all `H₄₁` parameters is **not**
requested and must not be claimed.

**This theorem does not prove rank zero, and does not prove `E_q(ℚ)` finite or finitely
generated.**  It is one of several premises a later rank argument would need; the others are
finite height sublevels, a torsion coset representative, and translation by `T`.  None of those
is in scope here.
-/

variable {ε : ℤ} {m q : ℕ}

/-! ## The height

`ℚ` in mathlib is stored in reduced form with positive denominator — `Rat.num` and `Rat.den` are
coprime and `0 < den` — so `heightQ` is literally the `max(|u|, v)` of the specification, with no
reduction step to justify. -/

/-- `H_ℚ(u/v) = max(|u|, v)` on the reduced representation. -/
def heightQ (x : ℚ) : ℕ := max x.num.natAbs x.den

@[simp] theorem heightQ_zero : heightQ 0 = 1 := by simp [heightQ]

theorem one_le_heightQ (x : ℚ) : 1 ≤ heightQ x :=
  le_trans x.den_pos (le_max_right _ _)

/-- The multiplicative height on the **actual** point group: `H(O) = 1`, and `H((x,y)) = H_ℚ(x)`.
Defined by pattern matching on mathlib's own `Affine.Point`, not on any surrogate. -/
noncomputable def height : (Ecurve ε m q).toAffine.Point → ℕ
  | .zero => 1
  | @Affine.Point.some _ _ _ x _ _ => heightQ x

@[simp] theorem height_zero : height (0 : (Ecurve ε m q).toAffine.Point) = 1 := rfl

@[simp] theorem height_some {x y : ℚ} (h : (Ecurve ε m q).toAffine.Nonsingular x y) :
    height (Affine.Point.some h) = heightQ x := rfl

theorem one_le_height (P : (Ecurve ε m q).toAffine.Point) : 1 ≤ height P := by
  cases P with
  | zero => exact height_zero.ge
  | some h => exact one_le_heightQ _

/-! ## The R1 target -/

/--
**TARGET R1 — `H41_MULTIPLICATIVE_DUPLICATION_HEIGHT`.  PRIMARY.**

Quantifier order is exactly: parameters → `∃ C` → `∀ P`.

Handle explicitly:
* `P = O`, where `H(O) = 1` and `O + O = O`;
* points killed by doubling (`P + P = O`), including `T = (0,0)` and the points of `E_q(ℚ)[2]`;
* the vanishing loci of `F` and of `G`, i.e. `x² = b` and `x(x² + ax + b) = 0`.

Forbidden as premise or conclusion: finite generation, `Finite`/`Fintype` on the point group,
Mordell–Weil, any canonical-height assumption, rank, `Sel₂`, Ш, BSD, and any assumed
rational-map height inequality equivalent to this statement. -/
theorem h41_multiplicative_duplication_height
    (ε : ℤ) (m q : ℕ) [Fact (Nat.Prime q)] (hP : Params ε m q) (hH : H41 ε m) :
    ∃ C : ℕ, 1 ≤ C ∧
      ∀ P : (Ecurve ε m q).toAffine.Point, height P ^ 4 ≤ C * height (P + P) := by
  -- the integral coefficients of `E_q : y² = x(x² + A q x + r² q²)`
  set aZ : ℤ := AA ε m * (q : ℤ) with haZ
  set bZ : ℤ := BB ε m * (q : ℤ) ^ 2 with hbZ
  have hdualA : dualA ε m q = ((aZ : ℤ) : ℚ) := rfl
  have hdualB : dualB ε m q = ((bZ : ℤ) : ℚ) := rfl
  -- the two certified side conditions: they are exactly what makes the resultant nonzero
  have hbQ : dualB ε m q ≠ 0 := dualB_ne_zero hP
  have hdQ : dualA ε m q ^ 2 - 4 * dualB ε m q ≠ 0 := dualA_disc_ne_zero hP
  have hb0 : bZ ≠ 0 := by
    intro h
    exact hbQ (by rw [hdualB, h]; simp)
  have hd0 : aZ ^ 2 - 4 * bZ ≠ 0 := by
    intro h
    refine hdQ ?_
    have hc : ((aZ ^ 2 - 4 * bZ : ℤ) : ℚ) = 0 := by rw [h]; simp
    rw [hdualA, hdualB]
    push_cast at hc
    linear_combination hc
  obtain ⟨C₀, hC₀, hcore⟩ := duplication_height_core aZ bZ hb0 hd0
  refine ⟨max C₀ ((bZ.natAbs + 1) ^ 4), le_trans hC₀ (le_max_left _ _), ?_⟩
  intro P
  cases P with
  | zero =>
      rw [show (Affine.Point.zero : (Ecurve ε m q).toAffine.Point) = 0 from rfl, add_zero,
        height_zero]
      simpa using le_trans hC₀ (le_max_left _ _)
  | @some x y h =>
      have heq : y ^ 2 = x ^ 3 + dualA ε m q * x ^ 2 + dualB ε m q * x :=
        (Wab_equation_iff _ _ x y).mp h.left
      by_cases hy : y = 0
      · -- points killed by doubling: `T = (0,0)` and all of `E_q(ℚ)[2]`
        have hyy : y = (Ecurve ε m q).toAffine.negY x y := by
          rw [show (Ecurve ε m q).toAffine.negY x y = -y from Wab_negY _ _ x y, hy]; ring
        rw [WeierstrassCurve.Affine.Point.add_self_of_Y_eq hyy, height_zero, mul_one,
          height_some h]
        have hroot : x * (x ^ 2 + (aZ : ℚ) * x + (bZ : ℚ)) = 0 := by
          rw [← hdualA, ← hdualB]
          rw [hy] at heq
          linear_combination -heq
        have hbnd : hgt x ≤ bZ.natAbs + 1 := hgt_le_of_two_torsion hb0 hroot
        calc heightQ x ^ 4 = hgt x ^ 4 := rfl
          _ ≤ (bZ.natAbs + 1) ^ 4 := Nat.pow_le_pow_left hbnd 4
          _ ≤ max C₀ ((bZ.natAbs + 1) ^ 4) := le_max_right _ _
      · -- the generic case: mathlib's tangent law computes `x(2P) = F/G`
        have hne : y ≠ (Ecurve ε m q).toAffine.negY x y := by
          rw [show (Ecurve ε m q).toAffine.negY x y = -y from Wab_negY _ _ x y]
          intro hcon
          exact hy (by linarith)
        rw [WeierstrassCurve.Affine.Point.add_self_of_Y_ne hne, height_some h, height_some _]
        have hdup : (Ecurve ε m q).toAffine.addX x x ((Ecurve ε m q).toAffine.slope x x y y)
            * ((4 : ℚ) * x * (x ^ 2 + (aZ : ℚ) * x + (bZ : ℚ))) = (x ^ 2 - (bZ : ℚ)) ^ 2 := by
          rw [← hdualA, ← hdualB]
          exact Wab_addX_self heq hy
        have hres := hcore x
          ((Ecurve ε m q).toAffine.addX x x ((Ecurve ε m q).toAffine.slope x x y y)) hdup
        calc heightQ x ^ 4 = hgt x ^ 4 := rfl
          _ ≤ C₀ * hgt ((Ecurve ε m q).toAffine.addX x x
                ((Ecurve ε m q).toAffine.slope x x y y)) := hres
          _ ≤ max C₀ ((bZ.natAbs + 1) ^ 4) * hgt ((Ecurve ε m q).toAffine.addX x x
                ((Ecurve ε m q).toAffine.slope x x y y)) :=
              Nat.mul_le_mul_right _ (le_max_left _ _)

end R1
