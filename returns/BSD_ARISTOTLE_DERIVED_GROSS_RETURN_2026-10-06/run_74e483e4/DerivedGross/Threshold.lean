module

public import Mathlib

/-!
# The acceptance threshold for a derived Gross identity (addendum, 2026-10-07)

This file formalizes the logical part of the tightened acceptance test. All arithmetic inputs are
explicit hypotheses. Nothing here is a statement about `Ш` of the seed curve.

* `dvd_num_of_fixed_constant`, `support_finite_of_fixed_constant` : with **one** constant
  `m = a/b`, one exceptional set `S`, the per-prime congruence `b·C₂ ≡ a·D (mod p)`, the G2
  non-vanishing `D ≢ 0` and the detector `Ш[p] ≠ 0 ⇒ C₂ ≡ 0`, one gets
  `Ш[p] ≠ 0 ⇒ p ∣ a` outside `S`, and finite support when `a ≠ 0` and `S` is finite.
* `single_unit_zero_iff` : one unit on the final congruence does not change zero/non-zero.
* `two_units_detection` : two independent vertical units, both proved non-zero, still preserve
  zero/non-zero detection, but they change the value: `C·v = u·m·D`.
* `nonunit_vertical_breaks` : if a vertical "unit" is not proved non-zero mod `p`, the detector can
  fire although `m ≢ 0` and `D ≢ 0`.
* `level_dependent_no_bound` : with a level-dependent constant `m_{E,ℓ}`, every hypothesis of the
  support argument can hold while every prime is in the support.
-/

@[expose] public section

namespace DerivedGross.Threshold

/-- **The finite-support step with one fixed constant.**  `c p` is `C₂(p,ℓ_p)` mod `p` and `d p` is
`(a_ℓ − 2)·R_{p,ℓ_p}` mod `p` for an admissible `ℓ_p` supplied by G2. -/
theorem dvd_num_of_fixed_constant (S : Set ℕ) (ShaNZ : ℕ → Prop) (a b : ℤ)
    (c d : (p : ℕ) → ZMod p)
    (hident : ∀ p, p.Prime → p ∉ S → (b : ZMod p) * c p = (a : ZMod p) * d p)
    (hG2 : ∀ p, p.Prime → p ∉ S → d p ≠ 0)
    (hdet : ∀ p, p.Prime → p ∉ S → ShaNZ p → c p = 0) :
    ∀ p, p.Prime → p ∉ S → ShaNZ p → (p : ℤ) ∣ a := by
  intro p hp hS hsha
  haveI := Fact.mk hp
  have h := hident p hp hS
  rw [hdet p hp hS hsha, mul_zero] at h
  have ha : (a : ZMod p) = 0 := by
    rcases mul_eq_zero.1 h.symm with h1 | h1
    · exact h1
    · exact absurd h1 (hG2 p hp hS)
  exact (ZMod.intCast_zmod_eq_zero_iff_dvd a p).1 ha

/-- **Finite support from one fixed nonzero constant and a finite exceptional set.** -/
theorem support_finite_of_fixed_constant (S : Set ℕ) (hSfin : S.Finite) (ShaNZ : ℕ → Prop)
    (a b : ℤ) (ha0 : a ≠ 0) (c d : (p : ℕ) → ZMod p)
    (hident : ∀ p, p.Prime → p ∉ S → (b : ZMod p) * c p = (a : ZMod p) * d p)
    (hG2 : ∀ p, p.Prime → p ∉ S → d p ≠ 0)
    (hdet : ∀ p, p.Prime → p ∉ S → ShaNZ p → c p = 0) :
    {p : ℕ | p.Prime ∧ ShaNZ p}.Finite := by
  have hA : {p : ℕ | (p : ℤ) ∣ a}.Finite := by
    apply (Nat.divisors a.natAbs).finite_toSet.subset
    intro p hp
    simp only [Set.mem_setOf_eq] at hp
    simp only [Finset.mem_coe, Nat.mem_divisors]
    exact ⟨Int.natCast_dvd.1 hp, by simpa using ha0⟩
  apply (hSfin.union hA).subset
  rintro p ⟨hp, hsha⟩
  by_cases hS : p ∈ S
  · exact Or.inl hS
  · exact Or.inr (dvd_num_of_fixed_constant S ShaNZ a b c d hident hG2 hdet p hp hS hsha)

/-- **One unit on the final congruence is harmless for detection.** -/
theorem single_unit_zero_iff {F : Type*} [Field F] {s u m : F} (hu : u ≠ 0) (h : s = u * m) :
    s = 0 ↔ m = 0 := by
  rw [h, mul_eq_zero]; simp [hu]

/-- **Two independent vertical units, both non-zero.**  If `x = m·y` holds in the common target and
the two specialization maps give `C = u·x` and `D = v·y`, then zero/non-zero detection survives,
but the value seen on the specialized side is `u·m/v`, not `m`. -/
theorem two_units_detection {F : Type*} [Field F] {x y m u v C D : F} (hu : u ≠ 0) (hv : v ≠ 0)
    (hid : x = m * y) (hC : C = u * x) (hD : D = v * y) :
    (C = 0 ↔ m * D = 0) ∧ C * v = u * m * D := by
  subst hid hC hD
  refine ⟨?_, by ring⟩
  constructor
  · intro h
    have : u * (m * y) = 0 := h
    rcases mul_eq_zero.1 this with h1 | h1
    · exact absurd h1 hu
    · rw [show m * (v * y) = v * (m * y) by ring, h1, mul_zero]
  · intro h
    have : v * (m * y) = 0 := by rw [← h]; ring
    rcases mul_eq_zero.1 this with h1 | h1
    · exact absurd h1 hv
    · rw [h1, mul_zero]

/-- **A vertical factor not proved non-zero breaks the bridge.**  With `u = 0` the specialized
coefficient vanishes although `m ≠ 0` and `D ≠ 0`. -/
theorem nonunit_vertical_breaks {F : Type*} [Field F] (m y v : F) (hm : m ≠ 0) (hy : y ≠ 0)
    (hv : v ≠ 0) :
    (0 : F) * (m * y) = 0 ∧ m ≠ 0 ∧ v * y ≠ 0 :=
  ⟨zero_mul _, hm, mul_ne_zero hv hy⟩

/-- **A level-dependent constant gives no support bound.**  Take `m_{E,ℓ} = ℓ` (non-zero for
`ℓ ≠ 0`) and `ℓ_p = p`. Then the per-prime congruence, the G2 non-vanishing and the detector all hold
with the support predicate "`p` is prime", and the set of primes is infinite. -/
theorem level_dependent_no_bound :
    ∃ (aℓ : ℕ → ℤ) (ℓsel : ℕ → ℕ) (c d : (p : ℕ) → ZMod p),
      (∀ ℓ, ℓ ≠ 0 → aℓ ℓ ≠ 0) ∧
      (∀ p, p.Prime → (1 : ZMod p) * c p = (aℓ (ℓsel p) : ZMod p) * d p) ∧
      (∀ p, p.Prime → d p ≠ 0) ∧
      (∀ p, p.Prime → p.Prime → c p = 0) ∧
      {p : ℕ | p.Prime ∧ p.Prime}.Infinite := by
  refine ⟨fun ℓ => (ℓ : ℤ), fun p => p, fun _ => 0, fun _ => 1, ?_, ?_, ?_, ?_, ?_⟩
  · intro ℓ hℓ; exact Int.natCast_ne_zero.2 hℓ
  · intro p _; show (1 : ZMod p) * 0 = (((p : ℕ) : ℤ) : ZMod p) * 1
    rw [Int.cast_natCast, ZMod.natCast_self]; simp
  · intro p hp; haveI := Fact.mk hp; exact one_ne_zero
  · intro p _ _; rfl
  · simpa using Nat.infinite_setOf_prime

end DerivedGross.Threshold
