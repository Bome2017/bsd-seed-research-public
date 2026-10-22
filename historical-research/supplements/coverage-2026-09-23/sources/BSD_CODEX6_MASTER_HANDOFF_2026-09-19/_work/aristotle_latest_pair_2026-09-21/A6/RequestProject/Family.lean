import Mathlib

/-!
# The seed is a family specialisation: every "coincidence" is a polynomial identity

The seed curve was offered together with an *uninterpreted datum*: `x(P₁) = 4547` while
`4547² ∣ N`, and with the suggestion that the conductor pattern
`N = 2³ · 3 · 2243 · 4547² · 5843` be treated as a distinguishing feature.

Both dissolve.  Write the two-integer family

  `A, s : ℤ`,  `B := A - 16s²`,  `C := A + 9s²`,
  `𝓔(A,s) : y² = x (x² - 5A x + 4AC)`,
  `Q₁ := (A, 6As)`,  `Q₂ := (36s², 12(A - 18s²)s)`.

(This is the review's family `y² = x(x² - 5tx + 4t(t+9))`, `P₁ = (t, 6t)`,
`P₂ = (36, 12(t-18))`, rescaled by `x ↦ s²x`, `y ↦ s³y` and written with `A = ts²`, so that
the parameters are integers.)

The seed is exactly `A = 4547`, `s = 12`, whence `B = 2243` and `C = 5843`.  This file
machine-checks the four identities that make the "coincidences" generic:

* `family_x_P1_eq` : `x(Q₁) = -a₂/5` **identically in `A, s`** — so `x(P₁) = 4547` is not a
  property of the seed at all, it is how the family is parametrised;
* `family_P1_on_curve`, `family_P2_on_curve` : the two points lie on `𝓔(A,s)` for all `A, s`;
* `family_disc` : `Δ = 2⁸ · 3² · A³ · B · C²` **identically** — so the exponent pattern
  `(3, 1, 2)` on the three "unusual" primes, and the constant `2⁸ · 3²`, are properties of the
  family, not of the seed;
* `seed_is_specialisation` : the seed's `a₂, a₄, Δ, P₁, P₂` are the values at `A = 4547, s = 12`,
  and `(A, B, C) = (4547, 2243, 5843)` are precisely the three odd "unusual" primes.

Conclusion: the *discriminant* of this model factors as `2⁸ · 3² · A³ · B · C²` identically, so
the three large primes occurring in it are `A`, `A - 16s²`, `A + 9s²`.

**Two qualifications, added after review.**

1. `family_disc` is an identity about the discriminant of the *given* model, not a conductor
   formula.  Passing from it to `N = 2³ · 3 · 2243 · 4547² · 5843` requires, at each prime,
   minimality of the model and the local valuations that feed Tate's algorithm — for the seed
   those are recorded separately in `RequestProject/SeedData.lean`.  Nothing here asserts a
   universal conductor formula for the family.
2. These identities show that the specific advertised features — the value `x(P₁) = 4547`, the
   divisibilities `A ∣ a₂, a₄`, the exponent pattern `(3, 1, 2)` and the constant `2⁸ · 3²` —
   are family-level, hence not seed-specific.  They do **not** show that the family carries no
   arithmetic usable against `Ш`; explaining the coordinates through a family is not a proof
   that the family is barren.
-/

namespace SeedBSD

namespace Family

variable (A s : ℤ)

/-- `B = A - 16s²`; for the seed, `B = 2243`. -/
def B : ℤ := A - 16 * s ^ 2

/-- `C = A + 9s²`; for the seed, `C = 5843`. -/
def C : ℤ := A + 9 * s ^ 2

/-- The `x²`-coefficient of the family model. -/
def a₂ : ℤ := -5 * A

/-- The `x`-coefficient of the family model. -/
def a₄ : ℤ := 4 * A * C A s

/-- The discriminant `16 a₄² (a₂² - 4a₄)` of `y² = x(x² + a₂x + a₄)`. -/
def disc : ℤ := 16 * (a₄ A s) ^ 2 * ((a₂ A) ^ 2 - 4 * a₄ A s)

/-- Membership in the family curve. -/
def OnCurve (x y : ℤ) : Prop := y ^ 2 = x ^ 3 + a₂ A * x ^ 2 + a₄ A s * x

/-- **The `x(P₁) = 4547` coincidence is a family identity.**
For every `A, s`, the first generator has `5 · x(Q₁) = -a₂`.  In particular `x(Q₁)` always
divides `a₂`, always divides `a₄`, and always reduces to the singular point of the fibre at any
prime dividing `A`.  No information specific to `4547` is involved. -/
theorem family_x_P1_eq : 5 * A = -a₂ A := by simp [a₂]

/-- `Q₁ = (A, 6As)` lies on `𝓔(A,s)` for all `A, s`. -/
theorem family_P1_on_curve : OnCurve A s A (6 * A * s) := by
  simp only [OnCurve, a₂, a₄, C]; ring

/-- `Q₂ = (36s², 12(A - 18s²)s)` lies on `𝓔(A,s)` for all `A, s`. -/
theorem family_P2_on_curve : OnCurve A s (36 * s ^ 2) (12 * (A - 18 * s ^ 2) * s) := by
  simp only [OnCurve, a₂, a₄, C]; ring

/-- **The discriminant pattern is a family identity.**
`Δ = 2⁸ · 3² · A³ · B · C²` for all `A, s`, where `Δ` is the discriminant of the model
`y² = x(x² + a₂x + a₄)` written above.  The constant `2⁸ · 3² = 2304` and the exponents
`(3, 1, 2)` are generic; the seed contributes only the *values* `A = 4547`, `B = 2243`,
`C = 5843`.

This is a statement about the discriminant of this model only.  It is not a conductor formula:
reading conductor exponents off it needs minimality and the local valuation data at each
prime. -/
theorem family_disc : disc A s = 2 ^ 8 * 3 ^ 2 * A ^ 3 * B A s * (C A s) ^ 2 := by
  simp only [disc, a₂, a₄, B, C]; ring

/-- The auxiliary identity behind `family_disc`: `a₂² - 4a₄ = 9 A B`. -/
theorem family_quadratic_disc : (a₂ A) ^ 2 - 4 * a₄ A s = 9 * A * B A s := by
  simp only [a₂, a₄, B, C]; ring

/-- `x(Q₂) = 36s²` is a perfect square times `36`; for the seed, `x(P₂) = 72²`. -/
theorem family_x_P2_sq : 36 * s ^ 2 = (6 * s) ^ 2 := by ring

end Family

/-! ## The seed is the specialisation `A = 4547`, `s = 12` -/

open Family

/-- `B(4547, 12) = 2243` and `C(4547, 12) = 5843`: the two remaining large conductor primes are
the family's `A - 16s²` and `A + 9s²`. -/
theorem seed_BC : B 4547 12 = 2243 ∧ C 4547 12 = 5843 := by
  constructor <;> norm_num [B, C]

/-- The seed's Weierstrass coefficients are the family values at `A = 4547`, `s = 12`. -/
theorem seed_coeffs : Family.a₂ 4547 = -22735 ∧ Family.a₄ 4547 12 = 106272484 := by
  constructor <;> norm_num [Family.a₂, Family.a₄, C]

/-- The seed's two generators are the family points at `A = 4547`, `s = 12`. -/
theorem seed_points :
    ((4547 : ℤ), (6 * 4547 * 12 : ℤ)) = (4547, 327384) ∧
    ((36 * 12 ^ 2 : ℤ), (12 * (4547 - 18 * 12 ^ 2) * 12 : ℤ)) = (5184, 281520) := by
  constructor <;> norm_num

/-- The seed's discriminant is the family value, with the three primes in the positions
`A³ · B · C²`. -/
theorem seed_disc :
    Family.disc 4547 12 = 2 ^ 8 * 3 ^ 2 * 4547 ^ 3 * 2243 * 5843 ^ 2 := by
  rw [family_disc]
  norm_num [B, C]

/-- **Summary.**  Every feature the record singled out as unusual — `x(P₁) = 4547`, the
divisibility `4547 ∣ a₂`, `4547 ∣ a₄`, the odd exponent `v_{4547}(Δ) = 3`, the squared prime
`5843²` in `Δ`, and the constant `2⁸ · 3²` — holds identically along the two-parameter family
and is therefore not seed-specific information. -/
theorem seed_coincidences_are_generic (A s : ℤ) :
    (5 * A = -Family.a₂ A) ∧
    (A ∣ Family.a₂ A) ∧ (A ∣ Family.a₄ A s) ∧
    Family.disc A s = 2 ^ 8 * 3 ^ 2 * A ^ 3 * Family.B A s * (Family.C A s) ^ 2 ∧
    Family.OnCurve A s A (6 * A * s) := by
  refine ⟨family_x_P1_eq A, ⟨-5, by simp [Family.a₂]; ring⟩,
    ⟨4 * Family.C A s, by simp [Family.a₄]; ring⟩, family_disc A s, family_P1_on_curve A s⟩

end SeedBSD
