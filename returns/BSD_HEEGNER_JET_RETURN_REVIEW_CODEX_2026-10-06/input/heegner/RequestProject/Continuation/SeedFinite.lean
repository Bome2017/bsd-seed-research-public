module

public import Mathlib

/-!
# Finite seed facts used by the cross-prime Kolyvagin construction

New Lean source for the 2026-10-06 continuation run.

* `K = ℚ(√-23)` satisfies the Heegner hypothesis for the conductor
  `N = 2^3 · 3 · 2243 · 4547^2 · 5843`: `-23 ≡ 1 (mod 8)`, so `2` splits, and `-23` is a
  nonzero square modulo `3, 2243, 4547, 5843`.
* The primes `ℓ = 281, 661, 839` are inert in `K` (`-23` is a non-square mod `ℓ`).

The point counts showing `a_ℓ = 0` at these primes are in `SeedPointCounts.lean`.
-/

@[expose] public section

namespace Continuation.SeedFinite

instance fact_prime_3 : Fact (Nat.Prime 3) := ⟨by norm_num⟩
instance fact_prime_2243 : Fact (Nat.Prime 2243) := ⟨by norm_num⟩
instance fact_prime_4547 : Fact (Nat.Prime 4547) := ⟨by norm_num⟩
instance fact_prime_5843 : Fact (Nat.Prime 5843) := ⟨by norm_num⟩
instance fact_prime_281 : Fact (Nat.Prime 281) := ⟨by norm_num⟩
instance fact_prime_661 : Fact (Nat.Prime 661) := ⟨by norm_num⟩
instance fact_prime_839 : Fact (Nat.Prime 839) := ⟨by norm_num⟩

/-! ### Heegner hypothesis for `K = ℚ(√-23)` -/

theorem two_splits : (-23 : ℤ) % 8 = 1 := by decide

theorem sq_mod_3 : ((1 : ZMod 3)) ^ 2 = -23 := by decide
theorem sq_mod_2243 : ((142 : ZMod 2243)) ^ 2 = -23 := by decide
theorem sq_mod_4547 : ((2063 : ZMod 4547)) ^ 2 = -23 := by decide
theorem sq_mod_5843 : ((1428 : ZMod 5843)) ^ 2 = -23 := by decide

private lemma legendre_one_of_sq (q : ℕ) [Fact q.Prime] (w : ZMod q) (hw : w ^ 2 = -23)
    (h0 : ((-23 : ℤ) : ZMod q) ≠ 0) : legendreSym q (-23) = 1 := by
  rw [legendreSym.eq_one_iff q h0]
  exact ⟨w, by push_cast; rw [← hw, sq]⟩

/-- Every odd prime dividing `N` splits in `ℚ(√-23)`. -/
theorem heegner_hypothesis_odd :
    legendreSym 3 (-23) = 1 ∧ legendreSym 2243 (-23) = 1 ∧
    legendreSym 4547 (-23) = 1 ∧ legendreSym 5843 (-23) = 1 := by
  exact ⟨legendre_one_of_sq 3 1 sq_mod_3 (by decide),
    legendre_one_of_sq 2243 142 sq_mod_2243 (by decide),
    legendre_one_of_sq 4547 2063 sq_mod_4547 (by decide),
    legendre_one_of_sq 5843 1428 sq_mod_5843 (by decide)⟩

/-! ### Supersingular primes inert in `K` -/

private lemma legendre_neg_one_of_euler (l : ℕ) [Fact l.Prime]
    (h0 : ((-23 : ℤ) : ZMod l) ≠ 0) (he : ((-23 : ℤ) : ZMod l) ^ (l / 2) ≠ 1) :
    legendreSym l (-23) = -1 := by
  rw [legendreSym.eq_neg_one_iff]
  intro hsq
  exact he ((ZMod.euler_criterion l h0).mp hsq)

theorem inert_281 : legendreSym 281 (-23) = -1 := by
  exact legendre_neg_one_of_euler 281 (by decide) (by decide +kernel)

theorem inert_661 : legendreSym 661 (-23) = -1 := by
  exact legendre_neg_one_of_euler 661 (by decide) (by decide +kernel)

theorem inert_839 : legendreSym 839 (-23) = -1 := by
  exact legendre_neg_one_of_euler 839 (by decide) (by decide +kernel)

/-- The primes `p ≥ 5` covered by these three supersingular inert primes: `p ∣ ℓ + 1`. -/
theorem covered_primes :
    282 = 2 * 3 * 47 ∧ 662 = 2 * 331 ∧ 840 = 2 ^ 3 * 3 * 5 * 7 ∧
    Nat.Prime 47 ∧ Nat.Prime 331 ∧ Nat.Prime 281 ∧ Nat.Prime 661 ∧ Nat.Prime 839 := by
  refine ⟨rfl, rfl, rfl, ?_, ?_, Fact.out, Fact.out, Fact.out⟩ <;> norm_num

end Continuation.SeedFinite
