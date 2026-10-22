import Mathlib

/-!
# The seed curve has no rational `p`-isogeny for any prime `p ≥ 5`

This file records a *new* exact arithmetic fact about the seed curve

    E : y² = x³ - 22735 x² + 106272484 x,    N = 2³ · 3 · 2243 · 4547² · 5843,

namely that the mod-`p` Galois representation of `E` is irreducible for **every** prime
`p ≥ 5`, equivalently that `E` admits no rational isogeny of prime degree `p ≥ 5`.

It does not control any `Ш`-prime and gives no bound on `#Ш(E/Q)`; what it does is remove,
unconditionally and uniformly in `p`, the irreducibility hypothesis that is standing in
essentially every statement about `Sel_p(E)`.

## Shape of the argument

Two inputs from the literature are used, and neither is asserted here as a theorem: both are
carried as explicit hypotheses of the structure `SeedIrr.IsogenyInput`, so that the Lean
statement below is a genuine implication and no axiom is introduced.

* **Mazur's isogeny theorem** (rational isogenies of prime degree): if `E/Q` admits a rational
  `p`-isogeny with `p` prime, then `p ∈ {2, 3, 5, 7, 11, 13, 17, 19, 37, 43, 67, 163}`.
* **The Frobenius congruence**: if `E[p]` is reducible, it has a Galois-stable line, so for
  every prime `ℓ` of good reduction with `ℓ ≠ p` the characteristic polynomial
  `x² - a_ℓ x + ℓ` of `Frob_ℓ` acting on `E[p]` has a root in `F_p`.

Everything else is finite computation, and it is machine-checked here:

* `SeedIrr.cardE_5`, `SeedIrr.cardE_7`, `SeedIrr.cardE_17` : the reductions of `E` at the
  good primes `5, 7, 17` have `8, 10, 24` points, i.e. `a_5 = -2`, `a_7 = -2`, `a_17 = -6`;
* `SeedIrr.no_root_5_mod_*`, `SeedIrr.no_root_7_mod_*`, `SeedIrr.no_root_17_mod_5` : for each
  prime `p` on Mazur's list one of these characteristic polynomials has **no** root in
  `ZMod p`, which contradicts the Frobenius congruence.

Note that `IsogenyInput` is, as a bare structure, satisfiable by a trivial `Red`; its content
is the implication it yields when `Red` is instantiated by the actual reducibility predicate
of the seed curve, for which the two fields are the cited theorems.

The conclusion is `SeedIrr.IsogenyInput.not_reducible`: under the two hypotheses above,
`E[p]` is irreducible for every prime `p ≥ 5`.

## What this does not give

It gives no upper bound on `dim Sel_p(E)`, controls no further primary part of `Ш`, and says
nothing about `q = 36`. It is an input that other arguments habitually assume.
-/

namespace SeedIrr

open Finset

/-- Affine points of the reduction of `y² = x³ - 22735x² + 106272484x` modulo `l`. -/
def affinePoints (l : ℕ) [NeZero l] : Finset (ZMod l × ZMod l) :=
  Finset.univ.filter fun P => P.2 ^ 2 = P.1 ^ 3 - 22735 * P.1 ^ 2 + 106272484 * P.1

/-- Number of points of the reduction modulo `l`, including the point at infinity. -/
def cardE (l : ℕ) [NeZero l] : ℕ := (affinePoints l).card + 1

/-- The trace of Frobenius `a_l = l + 1 - #Ẽ(F_l)`. -/
def traceFrob (l : ℕ) [NeZero l] : ℤ := (l : ℤ) + 1 - (cardE l : ℤ)

/-! ### The point counts (machine-checked) -/

theorem cardE_5 : cardE 5 = 8 := by decide
theorem cardE_7 : cardE 7 = 10 := by decide
theorem cardE_11 : cardE 11 = 14 := by decide
theorem cardE_13 : cardE 13 = 18 := by decide
theorem cardE_17 : cardE 17 = 24 := by decide

theorem traceFrob_5 : traceFrob 5 = -2 := by
  simp [traceFrob, cardE_5]

theorem traceFrob_7 : traceFrob 7 = -2 := by
  simp [traceFrob, cardE_7]

theorem traceFrob_17 : traceFrob 17 = -6 := by
  simp [traceFrob, cardE_17]

/-! ### Torsion

For an odd prime `l` of good reduction the torsion subgroup of `E(Q)` injects into `Ẽ(F_l)`.
With `#Ẽ(F_11) = 14` and `#Ẽ(F_13) = 18` this forces the order of the torsion subgroup to
divide `gcd(14, 18) = 2`; since `(0,0)` is a rational point of order `2`, the torsion subgroup
is exactly `Z/2`. The injection itself is the cited input; the arithmetic is here. -/
theorem torsion_card_dvd_two (T : ℕ) (h11 : T ∣ cardE 11) (h13 : T ∣ cardE 13) : T ∣ 2 := by
  rw [cardE_11] at h11
  rw [cardE_13] at h13
  have : T ∣ Nat.gcd 14 18 := Nat.dvd_gcd h11 h13
  simpa using this

/-! ### No Frobenius eigenvalue

`x² - a_ℓ x + ℓ` for `(ℓ, a_ℓ) = (5, -2)`, `(7, -2)`, `(17, -6)` is `x² + 2x + 5`,
`x² + 2x + 7`, `x² + 6x + 17`. For each prime on Mazur's list one of them has no root. -/

theorem no_root_5_mod_7 : ∀ x : ZMod 7, x ^ 2 + 2 * x + 5 ≠ 0 := by decide
theorem no_root_5_mod_11 : ∀ x : ZMod 11, x ^ 2 + 2 * x + 5 ≠ 0 := by decide
theorem no_root_5_mod_19 : ∀ x : ZMod 19, x ^ 2 + 2 * x + 5 ≠ 0 := by decide
theorem no_root_5_mod_43 : ∀ x : ZMod 43, x ^ 2 + 2 * x + 5 ≠ 0 := by decide
theorem no_root_5_mod_67 : ∀ x : ZMod 67, x ^ 2 + 2 * x + 5 ≠ 0 := by decide
set_option maxRecDepth 8000 in
theorem no_root_5_mod_163 : ∀ x : ZMod 163, x ^ 2 + 2 * x + 5 ≠ 0 := by decide

theorem no_root_7_mod_13 : ∀ x : ZMod 13, x ^ 2 + 2 * x + 7 ≠ 0 := by decide
theorem no_root_7_mod_17 : ∀ x : ZMod 17, x ^ 2 + 2 * x + 7 ≠ 0 := by decide
theorem no_root_7_mod_37 : ∀ x : ZMod 37, x ^ 2 + 2 * x + 7 ≠ 0 := by decide

theorem no_root_17_mod_5 : ∀ x : ZMod 5, x ^ 2 + 6 * x + 17 ≠ 0 := by decide

/-! ### Assembling the two cited inputs with the computation -/

/-- The two inputs from the literature, as hypotheses.

`Red p` is to be read as "the `G_Q`-module `E[p]` of the seed curve is reducible", equivalently
"`E` admits a rational `p`-isogeny".

* `mazur` is Mazur's theorem on rational isogenies of prime degree;
* `frob5`, `frob7`, `frob17` are the standard consequence of a Galois-stable line: `Frob_ℓ`
  then has an eigenvalue in `F_p`, i.e. its characteristic polynomial `x² - a_ℓ x + ℓ` has a
  root there. Only the three good primes `ℓ ∈ {5, 7, 17}` are used, and the polynomials
  `x² + 2x + 5`, `x² + 2x + 7`, `x² + 6x + 17` are exactly the ones given by the traces
  `a_5 = -2`, `a_7 = -2`, `a_17 = -6` verified above. -/
structure IsogenyInput where
  Red : ℕ → Prop
  mazur : ∀ p : ℕ, p.Prime → Red p →
    p ∈ ({2, 3, 5, 7, 11, 13, 17, 19, 37, 43, 67, 163} : Finset ℕ)
  frob5 : ∀ p : ℕ, p.Prime → Red p → p ≠ 5 → ∃ x : ZMod p, x ^ 2 + 2 * x + 5 = 0
  frob7 : ∀ p : ℕ, p.Prime → Red p → p ≠ 7 → ∃ x : ZMod p, x ^ 2 + 2 * x + 7 = 0
  frob17 : ∀ p : ℕ, p.Prime → Red p → p ≠ 17 → ∃ x : ZMod p, x ^ 2 + 6 * x + 17 = 0

namespace IsogenyInput

variable (D : IsogenyInput)

/-- **Main statement.** Under Mazur's isogeny theorem and the Frobenius congruence, the seed
curve has no rational `p`-isogeny — equivalently `E[p]` is irreducible — for every prime
`p ≥ 5`. -/
theorem not_reducible (p : ℕ) (hp : p.Prime) (hp5 : 5 ≤ p) : ¬ D.Red p := by
  intro hred
  have hmem := D.mazur p hp hred
  fin_cases hmem
  · omega
  · omega
  · obtain ⟨x, hx⟩ := D.frob17 5 hp hred (by decide)
    exact no_root_17_mod_5 x hx
  · obtain ⟨x, hx⟩ := D.frob5 7 hp hred (by decide)
    exact no_root_5_mod_7 x hx
  · obtain ⟨x, hx⟩ := D.frob5 11 hp hred (by decide)
    exact no_root_5_mod_11 x hx
  · obtain ⟨x, hx⟩ := D.frob7 13 hp hred (by decide)
    exact no_root_7_mod_13 x hx
  · obtain ⟨x, hx⟩ := D.frob7 17 hp hred (by decide)
    exact no_root_7_mod_17 x hx
  · obtain ⟨x, hx⟩ := D.frob5 19 hp hred (by decide)
    exact no_root_5_mod_19 x hx
  · obtain ⟨x, hx⟩ := D.frob7 37 hp hred (by decide)
    exact no_root_7_mod_37 x hx
  · obtain ⟨x, hx⟩ := D.frob5 43 hp hred (by decide)
    exact no_root_5_mod_43 x hx
  · obtain ⟨x, hx⟩ := D.frob5 67 hp hred (by decide)
    exact no_root_5_mod_67 x hx
  · obtain ⟨x, hx⟩ := D.frob5 163 hp hred (by decide)
    exact no_root_5_mod_163 x hx

end IsogenyInput

end SeedIrr
