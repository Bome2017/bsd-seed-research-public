/-
# Machine-checked arithmetic input for the fixed twist `E^{-7}/Q`

The fixed curve of the audit is

    E' = E^{-7} :  y^2 = x^3 + 159145 x^2 + 5207351716 x .

This file certifies, by kernel/compiler evaluation, the finite arithmetic facts that the
Stage-I audit uses as inputs:

* the invariants `c4`, `c6`, `Delta` of the given model, and the factorisation of `Delta`
  (in particular `v_q(Delta) = 1` at `q = 2243`, which is what makes the image of every
  residual representation `rhobar_p` contain an element of order `p`);
* the non-integrality of `j`, hence that `E'` has no complex multiplication;
* the traces `a_l` at the small good primes `l = 5, 11, 13, 17, 19, 23`;
* for each prime `p` in Mazur's list of possible prime isogeny degrees of a non-CM elliptic
  curve over `Q`, an explicit good prime `l` with `a_l^2 - 4 l` a non-square modulo `p`.
  Since a reducible `rhobar_p` has both Frobenius eigenvalues in `F_p`, such a witness
  proves that `rhobar_p` is irreducible;
* `gcd(#E'(F_5), #E'(F_11)) = 2`, which bounds the torsion, and the non-squareness of the
  discriminant `4497724161` of the quadratic factor of the defining cubic, which shows the
  rational 2-torsion is exactly `Z/2`.

All statements here are finite computations about the explicit model; no arithmetic
geometry is assumed. `a_l` is *defined* here as `l + 1 - #E'(F_l)` with `#E'(F_l)` the
naive projective point count, which is the usual trace of Frobenius at a prime of good
reduction.
-/
import Mathlib

namespace TwistSha

/-- Right-hand side of the model `y^2 = x^3 + 159145 x^2 + 5207351716 x`, reduced mod `l`. -/
def rhs (l x : ℕ) : ℕ := (x ^ 3 + 159145 * x ^ 2 + 5207351716 * x) % l

/-- Number of affine points of the model over `F_l`. -/
def affineCount (l : ℕ) : ℕ :=
  ((List.range l).map fun x =>
    ((List.range l).filter fun y => (y * y) % l = rhs l x).length).sum

/-- `#E'(F_l)`, the affine points together with the point at infinity. -/
def cardE (l : ℕ) : ℕ := affineCount l + 1

/-- The trace of Frobenius `a_l = l + 1 - #E'(F_l)`. -/
def aL (l : ℕ) : ℤ := (l : ℤ) + 1 - (cardE l : ℤ)

/-- `c4` of the model. -/
def c4 : ℤ := (4 * 159145) ^ 2 - 24 * (2 * 5207351716)

/-- `c6` of the model. -/
def c6 : ℤ := -(4 * 159145) ^ 3 + 36 * (4 * 159145) * (2 * 5207351716)

/-- The discriminant of the model, as `(c4^3 - c6^2)/1728`. -/
def disc : ℤ := (c4 ^ 3 - c6 ^ 2) / 1728

/-- The invariants of the given model of `E^{-7}`, and the factorisation of its
discriminant.  The exponent `1` of `2243` is the input to the order-`p`-element argument. -/
theorem invariants :
    c4 = 155281214032 ∧ c6 = -19291412299579840 ∧
      disc = 1951401451332224483990307737856 ∧
      disc = 2 ^ 8 * 3 ^ 2 * 7 ^ 6 * 2243 ^ 1 * 4547 ^ 3 * 5843 ^ 2 := by
  refine ⟨by decide, by decide, by decide, by decide⟩

/-- `j = c4^3/Delta` is not an integer: `Delta` does not divide `c4^3`.  Hence `E^{-7}`
has potentially multiplicative reduction somewhere and in particular has no CM. -/
theorem j_not_integral : ¬ (disc ∣ c4 ^ 3) := by decide

/-- The traces of Frobenius of `E^{-7}` at the small good primes used as witnesses. -/
theorem aL_values :
    aL 5 = 2 ∧ aL 11 = -2 ∧ aL 13 = 4 ∧ aL 17 = 6 ∧ aL 19 = -4 ∧ aL 23 = 0 := by
  refine ⟨by native_decide, by native_decide, by native_decide, by native_decide,
    by native_decide, by native_decide⟩

/-- The traces at the three primes of multiplicative reduction (`v_q(c4) = 0`).  Here
`a_q = +1` means split and `a_q = -1` non-split multiplicative reduction.  So `E^{-7}` is
split multiplicative at 3 and 5843 and non-split multiplicative at 2243. -/
theorem aL_at_multiplicative_primes : aL 3 = 1 ∧ aL 2243 = -1 ∧ aL 5843 = 1 := by
  refine ⟨by native_decide, by native_decide, by native_decide⟩

/-- Mazur's list of the primes that can occur as the degree of a rational isogeny of a
non-CM elliptic curve over `Q` (extended by the CM degrees `43, 67, 163` for safety). -/
def mazurPrimes : List ℕ := [5, 7, 11, 13, 17, 19, 37, 43, 67, 163]

/-- The good auxiliary primes at which Frobenius is evaluated. -/
def witnessPrimes : List ℕ := [5, 11, 13, 17, 19, 23]

/-- Boolean square test modulo `p`. -/
def isSquareMod (a : ℤ) (p : ℕ) : Bool :=
  (List.range p).any fun r => (((r : ℤ) * (r : ℤ) - a) % (p : ℤ) = 0)

theorem not_isSquare_of_isSquareMod_false {p : ℕ} [NeZero p] {a : ℤ}
    (h : isSquareMod a p = false) : ¬ IsSquare ((a : ZMod p)) := by
  rintro ⟨r, hr⟩
  have hmem : r.val ∈ List.range p := List.mem_range.mpr (ZMod.val_lt r)
  have hz : ((((r.val : ℤ) * (r.val : ℤ) - a : ℤ)) : ZMod p) = 0 := by
    push_cast
    rw [ZMod.natCast_val, ZMod.cast_id, ← hr]
    ring
  have hdvd : ((p : ℤ)) ∣ ((r.val : ℤ) * (r.val : ℤ) - a) :=
    (ZMod.intCast_zmod_eq_zero_iff_dvd _ _).1 hz
  have : isSquareMod a p = true := by
    refine List.any_eq_true.2 ⟨r.val, hmem, ?_⟩
    simpa using Int.emod_eq_zero_of_dvd hdvd
  simp [this] at h

/-- **Residual irreducibility witnesses.**  For every prime `p` in Mazur's list there is a
good prime `l` such that the discriminant `a_l^2 - 4 l` of the Frobenius characteristic
polynomial is a non-square modulo `p`.  If `rhobar_p` were reducible its two Frobenius
eigenvalues would lie in `F_p`, forcing `a_l^2 - 4 l` to be a square mod `p` for every good
`l`.  Together with Mazur's theorem this rules out reducibility of `rhobar_p` for the fixed
curve `E^{-7}` at every prime `p >= 5`. -/
theorem irreducibility_witnesses :
    ∀ p ∈ mazurPrimes, ∃ l ∈ witnessPrimes,
      isSquareMod (aL l ^ 2 - 4 * (l : ℤ)) p = false := by
  native_decide

/-- The same witnesses, stated as genuine non-squareness in `ZMod p`. -/
theorem irreducibility_witnesses_zmod :
    ¬ IsSquare (((aL 17 ^ 2 - 4 * 17 : ℤ) : ZMod 5)) ∧
    ¬ IsSquare (((aL 5 ^ 2 - 4 * 5 : ℤ) : ZMod 7)) ∧
    ¬ IsSquare (((aL 5 ^ 2 - 4 * 5 : ℤ) : ZMod 11)) ∧
    ¬ IsSquare (((aL 17 ^ 2 - 4 * 17 : ℤ) : ZMod 13)) ∧
    ¬ IsSquare (((aL 11 ^ 2 - 4 * 11 : ℤ) : ZMod 17)) ∧
    ¬ IsSquare (((aL 5 ^ 2 - 4 * 5 : ℤ) : ZMod 19)) ∧
    ¬ IsSquare (((aL 17 ^ 2 - 4 * 17 : ℤ) : ZMod 37)) ∧
    ¬ IsSquare (((aL 5 ^ 2 - 4 * 5 : ℤ) : ZMod 43)) ∧
    ¬ IsSquare (((aL 5 ^ 2 - 4 * 5 : ℤ) : ZMod 67)) ∧
    ¬ IsSquare (((aL 5 ^ 2 - 4 * 5 : ℤ) : ZMod 163)) := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;>
    · apply not_isSquare_of_isSquareMod_false
      native_decide

/-- The point counts at 5 and 11 have gcd 2, so `#E^{-7}(Q)_tors` divides 2. -/
theorem torsion_gcd : Nat.gcd (cardE 5) (cardE 11) = 2 := by native_decide

/-- The discriminant `159145^2 - 4*5207351716 = 4497724161` of the quadratic factor of the
defining cubic is not a perfect square, so `E^{-7}(Q)[2] = Z/2` (not `(Z/2)^2`). -/
theorem quadratic_factor_disc_not_square : ¬ ∃ n : ℕ, n * n = 4497724161 := by
  rw [Nat.exists_mul_self]
  native_decide

end TwistSha
