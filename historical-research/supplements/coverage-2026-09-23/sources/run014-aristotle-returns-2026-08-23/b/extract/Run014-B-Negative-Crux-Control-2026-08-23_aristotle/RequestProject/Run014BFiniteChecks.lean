import Mathlib

/-!
# Run014-B audit: machine-checked finite facts

This file certifies, in Lean, exactly those statements of the Run014-B archive that are
*finite* and therefore genuinely machine-checkable, plus one elementary group-theoretic
lemma used in the audit of the archive's `Sha[2^∞] = 0` step.

Nothing here certifies a uniform (in `q`) statement, and nothing here concerns the
`L`-function of any elliptic curve.  See `ARISTOTLE_RESULT.md` for the audit itself.
-/

namespace Run014B

/-! ## 1. The `q = 13` family-signature witness of the frozen family `F_62`

The base curve is Cremona `62a1`: `v^2 + u*v + v = u^3 - u^2 - u + 1`.
-/

/-- The affine `F_13`-points of the minimal model of `62a1`. -/
def affinePointsF13 : Finset (ZMod 13 × ZMod 13) :=
  Finset.univ.filter fun p =>
    p.2 ^ 2 + p.1 * p.2 + p.2 = p.1 ^ 3 - p.1 ^ 2 - p.1 + 1

/-- `#E(F_13) = 12` for `62a1` (affine points plus the point at infinity). -/
theorem card_points_62a1_F13 : affinePointsF13.card + 1 = 12 := by decide

/-- The Frobenius trace at `13` is `a_13 = 13 + 1 - 12 = 2`; in particular `a_13 ≠ 0`,
which is one of the literal defining conditions of `F_62`. -/
theorem trace_62a1_at_13 : (13 : ℤ) + 1 - 12 = 2 ∧ (2 : ℤ) ≠ 0 := by norm_num

/-- `v_2(#E(F_13)) = 2`, another literal defining condition of `F_62`. -/
theorem two_adic_valuation_point_count : 2 ^ 2 ∣ 12 ∧ ¬ (2 ^ 3 ∣ 12) := by decide

/-- `13 ≡ 5 (mod 8)`. -/
theorem thirteen_mod_eight : 13 % 8 = 5 := by decide

/-- `13` does not divide `372 = 4 * 3 * 31`. -/
theorem thirteen_not_dvd_372 : ¬ ((13 : ℕ) ∣ 372) := by decide

/-- `13` is a quadratic nonresidue mod `31`, i.e. the Legendre symbol `(13/31) = -1`. -/
theorem thirteen_nonresidue_mod_31 : ¬ ∃ x : ZMod 31, x ^ 2 = 13 := by decide

/-! ## 2. The `2`-primary triviality step

The archive deduces `Ш[2^∞] = 0` from `Ш[2] = 0` while also invoking finiteness of `Ш`
(an external analytic input).  The deduction needs no finiteness: in any abelian group,
vanishing of the `2`-torsion already kills the whole `2`-primary part.  This lemma is
recorded because it isolates which parts of the archive's chain are *not* load-bearing on
external theorems.
-/

/-- In an additive commutative group with no `2`-torsion, there is no `2`-power torsion. -/
theorem no_two_power_torsion_of_no_two_torsion
    {A : Type*} [AddCommGroup A] (h2 : ∀ a : A, (2 : ℕ) • a = 0 → a = 0) :
    ∀ (n : ℕ) (a : A), (2 ^ n : ℕ) • a = 0 → a = 0 := by
  intro n
  induction n with
  | zero => intro a ha; simpa using ha
  | succ k ih =>
      intro a ha
      refine ih a (h2 ((2 ^ k : ℕ) • a) ?_)
      simpa [pow_succ, mul_comm, mul_smul] using ha

end Run014B
