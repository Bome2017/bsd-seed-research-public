/-
Non-vacuity witnesses for the hypotheses of the principal target.

This file adds nothing to the target statement.  It only exhibits explicit parameter tuples
`(ε, m, q)` satisfying both `SDyadic.Params ε m q` and the certified stratum `SDyadic.H41 ε m`,
one for each of the two `H₄₁` branches, so that `SDyadic.sdyadic_saturation` is demonstrably
not vacuous.

  * branch `D < 0`, `s = 1` :  `ε = 1`,  `m = 3`,  `q = 13`  (`D = -31`)
  * branch `D > 0`, `s = 2` :  `ε = -1`, `m = 3`,  `q = 5`   (`D = 33 = 3 · 11`)
-/
import RequestProject.SDyadic.Saturation

namespace SDyadic

open Run013

namespace Instances

/-! ## Branch 1 : `ε = 1`, `m = 3`, `q = 13`, `D = -31` -/

instance factPrime13 : Fact (Nat.Prime 13) := ⟨by norm_num⟩

theorem DD_one_three : DD 1 3 = -31 := by decide

theorem ellSet_one_three : ellSet 1 3 = {31} := by
  rw [ellSet, DD_one_three]
  show Nat.primeFactors 31 = {31}
  exact Nat.Prime.primeFactors (by norm_num)

theorem H41_one_three : H41 1 3 := by
  refine Or.inl ⟨by rw [DD_one_three]; norm_num, ?_⟩
  rw [sCount, ellSet_one_three]; rfl

theorem params_one_three_thirteen : Params 1 3 13 := by
  refine ⟨by norm_num, Or.inl rfl, ?_, by norm_num, ?_, ?_⟩
  · rw [DD_one_three]; decide
  · rw [DD_one_three]; decide
  · intro l hl
    rw [ellSet_one_three] at hl
    simp only [Finset.mem_singleton] at hl
    subst hl
    rw [padicValInt, DD_one_three]
    norm_num [padicValNat.self]

/-! ## Branch 2 : `ε = -1`, `m = 3`, `q = 5`, `D = 33` -/

instance factPrime5 : Fact (Nat.Prime 5) := ⟨by norm_num⟩

theorem DD_neg_one_three : DD (-1) 3 = 33 := by decide

theorem ellSet_neg_one_three : ellSet (-1) 3 = {3, 11} := by
  rw [ellSet, DD_neg_one_three]
  show Nat.primeFactors 33 = {3, 11}
  rw [show (33 : ℕ) = 3 * 11 by norm_num, Nat.primeFactors_mul (by norm_num) (by norm_num),
    Nat.Prime.primeFactors (by norm_num), Nat.Prime.primeFactors (by norm_num)]
  decide

theorem H41_neg_one_three : H41 (-1) 3 := by
  refine Or.inr ⟨by rw [DD_neg_one_three]; norm_num, ?_, ?_⟩
  · rw [sCount, ellSet_neg_one_three]; rfl
  · intro l hl
    rw [ellSet_neg_one_three] at hl
    simp only [Finset.mem_insert, Finset.mem_singleton] at hl
    rcases hl with rfl | rfl <;> rfl

theorem params_neg_one_three_five : Params (-1) 3 5 := by
  refine ⟨by norm_num, Or.inr rfl, ?_, by norm_num, ?_, ?_⟩
  · rw [DD_neg_one_three]; decide
  · rw [DD_neg_one_three]; decide
  · intro l hl
    rw [ellSet_neg_one_three] at hl
    simp only [Finset.mem_insert, Finset.mem_singleton] at hl
    rw [padicValInt, DD_neg_one_three]
    rcases hl with rfl | rfl
    · show Odd (padicValNat 3 (33 : ℤ).natAbs)
      haveI : Fact (Nat.Prime 3) := ⟨by norm_num⟩
      haveI : Fact (Nat.Prime 11) := ⟨by norm_num⟩
      rw [show ((33 : ℤ).natAbs) = 3 * 11 by norm_num,
        padicValNat.mul (by norm_num) (by norm_num), padicValNat.self (by norm_num),
        padicValNat.eq_zero_of_not_dvd (by decide)]
      decide
    · show Odd (padicValNat 11 (33 : ℤ).natAbs)
      haveI : Fact (Nat.Prime 3) := ⟨by norm_num⟩
      haveI : Fact (Nat.Prime 11) := ⟨by norm_num⟩
      rw [show ((33 : ℤ).natAbs) = 11 * 3 by norm_num,
        padicValNat.mul (by norm_num) (by norm_num), padicValNat.self (by norm_num),
        padicValNat.eq_zero_of_not_dvd (by decide)]
      decide

/-! ## The target applies to both witnesses -/

theorem saturation_one_three_thirteen :
    (∀ d : ℚ, d ≠ 0 →
        (LocalKummerAll (phiA 1 3 13) (phiB 1 3 13) d ↔ Cov ℚ (phiA 1 3 13) (phiB 1 3 13) d)) ∧
    (∀ d : ℚ, d ≠ 0 →
        (LocalKummerAll (dualA 1 3 13) (dualB 1 3 13) d ↔ Cov ℚ (dualA 1 3 13) (dualB 1 3 13) d)) ∧
    GlobalSet (phiA 1 3 13) (phiB 1 3 13) = SelmerSet (phiA 1 3 13) (phiB 1 3 13) ∧
    GlobalSet (dualA 1 3 13) (dualB 1 3 13) = SelmerSet (dualA 1 3 13) (dualB 1 3 13) ∧
    ((KExp 1 3).subgroupOf (GphiExp 1 3 13)).index = 2 :=
  sdyadic_saturation 1 3 13 params_one_three_thirteen H41_one_three

theorem saturation_neg_one_three_five :
    (∀ d : ℚ, d ≠ 0 →
        (LocalKummerAll (phiA (-1) 3 5) (phiB (-1) 3 5) d ↔
          Cov ℚ (phiA (-1) 3 5) (phiB (-1) 3 5) d)) ∧
    (∀ d : ℚ, d ≠ 0 →
        (LocalKummerAll (dualA (-1) 3 5) (dualB (-1) 3 5) d ↔
          Cov ℚ (dualA (-1) 3 5) (dualB (-1) 3 5) d)) ∧
    GlobalSet (phiA (-1) 3 5) (phiB (-1) 3 5) = SelmerSet (phiA (-1) 3 5) (phiB (-1) 3 5) ∧
    GlobalSet (dualA (-1) 3 5) (dualB (-1) 3 5) = SelmerSet (dualA (-1) 3 5) (dualB (-1) 3 5) ∧
    ((KExp (-1) 3).subgroupOf (GphiExp (-1) 3 5)).index = 2 :=
  sdyadic_saturation (-1) 3 5 params_neg_one_three_five H41_neg_one_three

end Instances

end SDyadic
