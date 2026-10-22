/-
`P01/Instances.lean` — non-vacuity witnesses for `Params`.

This file adds nothing to the P01 target.  It exhibits explicit parameter tuples `(ε, m, q)`
satisfying `SDyadic.Params`, so that `P01.p01_family_two_torsion` is demonstrably **not
vacuous**: its hypothesis really is satisfiable.

  * `ε = 1`,  `m = 3`, `q = 13`   (`D = −31`)
  * `ε = -1`, `m = 3`, `q = 5`    (`D =  33 = 3 · 11`)

PROVENANCE.  The two `Params` witnesses and their supporting facts are taken from the
**certified** saturation Run B development,
`S_DYADIC_SATURATION_FORMALIZATION_FREEZE_002/02_run_B/tree/RequestProject/SDyadic/Instances.lean`,
which carries axiom footprint `[propext, Classical.choice, Quot.sound]`.  Only the
`Params`-related declarations are carried here; the `H41` witnesses in that file need
`Saturation.lean`, which P01 does not import and does not need.

`decide` appearing below is Lean's **kernel-checked** decision procedure, not
`native_decide`.  It adds no axioms.
-/
import RequestProject.SDyadic.Family

namespace P01

open SDyadic

namespace Instances

/-! ## Branch 1 : `ε = 1`, `m = 3`, `q = 13`, `D = -31` -/

instance factPrime13 : Fact (Nat.Prime 13) := ⟨by norm_num⟩

theorem DD_one_three : DD 1 3 = -31 := by decide

theorem ellSet_one_three : ellSet 1 3 = {31} := by
  rw [ellSet, DD_one_three]
  show Nat.primeFactors 31 = {31}
  exact Nat.Prime.primeFactors (by norm_num)

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

end Instances

end P01
