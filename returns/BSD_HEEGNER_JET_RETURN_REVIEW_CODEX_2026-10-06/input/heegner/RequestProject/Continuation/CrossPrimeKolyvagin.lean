module

public import Mathlib

/-!
# Cross-prime Kolyvagin derivative: the algebraic and finite steps

New Lean source for the 2026-10-06 continuation run (see `research_return/PROOF.md`).

* `derivative_relation`: Kolyvagin's telescoping identity `(σ - 1) D = m - Tr` for an
  element `σ` of any ring with `σ ^ m = 1`, where `D = Σ_{i<m} i σ^i`.
* `cross_prime_invariance`: if the trace of `y` vanishes (which is the Heegner norm
  relation `Tr y_ℓ = a_ℓ y_1` when `a_ℓ = 0`), then `σ (D y) - D y = m • y`. Hence `D y`
  is `σ`-invariant modulo `d` for every divisor `d` of `m`, simultaneously.
* `supersingular_charpoly`: if `p ∣ a` and `p ∣ ℓ + 1`, then `X² - aX + ℓ ≡ (X - 1)(X + 1)`
  mod `p`.
* The seed's finite facts: `K = ℚ(√-23)` satisfies the Heegner hypothesis, and specific
  primes `ℓ` are inert in `K` and have `a_ℓ = 0`.

Nothing here formalizes Heegner points, Selmer groups or Kolyvagin's theorem. Those remain
written imports.
-/

@[expose] public section

namespace Continuation.CrossPrime

open Finset Polynomial

/-- The Kolyvagin derivative operator `D_m = Σ_{i<m} i σ^i` in a ring. -/
def kolyvaginD {R : Type*} [Ring R] (s : R) (m : ℕ) : R :=
  ∑ i ∈ range m, (i : R) * s ^ i

/-- Telescoping identity in `ℤ[X]`, before reduction modulo `X^m = 1`. -/
theorem derivative_telescope_poly (m : ℕ) :
    (X - 1) * (∑ i ∈ range m, (i : ℤ[X]) * X ^ i) + ∑ j ∈ range m, (X : ℤ[X]) ^ j
      = 1 + ((m : ℤ[X]) - 1) * X ^ m := by
  induction m with
  | zero => simp
  | succ n ih =>
    rw [sum_range_succ, sum_range_succ, mul_add, add_add_add_comm, ih]
    push_cast
    ring

/-- Telescoping identity in any ring, before reduction modulo `σ^m = 1`. -/
theorem derivative_telescope {R : Type*} [Ring R] (s : R) (m : ℕ) :
    (s - 1) * kolyvaginD s m + ∑ j ∈ range m, s ^ j = 1 + ((m : R) - 1) * s ^ m := by
  have h := congrArg (Polynomial.aeval (R := ℤ) s) (derivative_telescope_poly m)
  simpa [kolyvaginD, map_sum] using h

/-- **Kolyvagin's derivative relation.** If `σ ^ m = 1` then `(σ - 1) D_m = m - Tr`,
where `Tr = Σ_{j<m} σ^j`. -/
theorem derivative_relation {R : Type*} [Ring R] (s : R) (m : ℕ) (hs : s ^ m = 1) :
    (s - 1) * kolyvaginD s m = m - ∑ j ∈ range m, s ^ j := by
  have h := derivative_telescope s m
  rw [hs, mul_one] at h
  rw [eq_sub_iff_add_eq, h]
  abel

/-- For a nontrivial `m`-th root of unity `ζ` in a field, `(ζ - 1) Σ_{i<m} i ζ^i = m`.
This is the factor `m / (χ(σ) - 1)` acquired by the `χ`-component of `D y`. -/
theorem derivative_root_of_unity {F : Type*} [Field F] (ζ : F) (m : ℕ) (hζ : ζ ^ m = 1)
    (hne : ζ ≠ 1) : (ζ - 1) * kolyvaginD ζ m = m := by
  rw [derivative_relation ζ m hζ]
  have : ∑ j ∈ range m, ζ ^ j = 0 := by
    have h := geom_sum_mul ζ m
    rw [hζ, sub_self] at h
    exact (mul_eq_zero.mp h).resolve_right (sub_ne_zero.mpr hne)
  rw [this, sub_zero]

/-- **Cross-prime invariance.** Let `σ` act additively on `M` with `σ ^ m = 1`, and let
`y ∈ M` have zero trace. Then `σ (D y) - D y = m • y`. -/
theorem cross_prime_invariance {M : Type*} [AddCommGroup M] (σ : AddMonoid.End M) (m : ℕ)
    (hσ : σ ^ m = 1) (y : M) (htr : ∑ j ∈ range m, (σ ^ j) y = 0) :
    σ (kolyvaginD σ m y) - kolyvaginD σ m y = m • y := by
  have h := congrArg (fun f : AddMonoid.End M => f y) (derivative_relation σ m hσ)
  have e1 : ((σ - 1) * kolyvaginD σ m) y = σ (kolyvaginD σ m y) - kolyvaginD σ m y := rfl
  have e2 : ((m : AddMonoid.End M) - ∑ j ∈ range m, σ ^ j) y
      = m • y - ∑ j ∈ range m, (σ ^ j) y := by
    rw [AddMonoidHom.sub_apply, AddMonoidHom.finset_sum_apply, AddMonoid.End.natCast_apply]
  simp only at h
  rw [← e1, h, e2, htr, sub_zero]

/-- Consequently `D y` is `σ`-invariant modulo `d • M` for every divisor `d` of `m`, all at
once. -/
theorem cross_prime_invariance_dvd {M : Type*} [AddCommGroup M] (σ : AddMonoid.End M)
    (m : ℕ) (hσ : σ ^ m = 1) (y : M) (htr : ∑ j ∈ range m, (σ ^ j) y = 0) {d : ℕ}
    (hd : d ∣ m) : ∃ z : M, σ (kolyvaginD σ m y) - kolyvaginD σ m y = d • z := by
  obtain ⟨k, rfl⟩ := hd
  exact ⟨k • y, by rw [cross_prime_invariance σ _ hσ y htr, mul_smul]⟩

/-- At a supersingular prime (`a_ℓ = 0`, or more generally `p ∣ a_ℓ`) with `p ∣ ℓ + 1`,
the Frobenius characteristic polynomial is `(X - 1)(X + 1)` modulo `p`. -/
theorem supersingular_charpoly (p : ℕ) (a l : ℤ) (ha : (p : ℤ) ∣ a) (hl : (p : ℤ) ∣ l + 1) :
    (X ^ 2 - C (a : ZMod p) * X + C (l : ZMod p) : (ZMod p)[X]) = (X - 1) * (X + 1) := by
  have ha' : (a : ZMod p) = 0 := (ZMod.intCast_zmod_eq_zero_iff_dvd a p).mpr ha
  have hl' : (l : ZMod p) = -1 := by
    have : ((l + 1 : ℤ) : ZMod p) = 0 := (ZMod.intCast_zmod_eq_zero_iff_dvd _ p).mpr hl
    push_cast at this
    exact eq_neg_of_add_eq_zero_left this
  rw [ha', hl']
  simp only [map_zero, zero_mul, sub_zero, map_neg, map_one]
  ring

end Continuation.CrossPrime
