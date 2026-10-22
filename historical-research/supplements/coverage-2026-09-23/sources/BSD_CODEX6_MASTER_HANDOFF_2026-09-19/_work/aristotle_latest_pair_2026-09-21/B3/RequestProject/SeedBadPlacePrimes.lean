import Mathlib

/-!
# Bad-place bookkeeping for the seed curve

For the seed curve

    E/Q :  y^2 = x^3 - 22735 x^2 + 106272484 x,   N = 2^3 * 3 * 2243 * 4547^2 * 5843,

Tate's algorithm gives the reduction data recorded in `ARISTOTLE_B_REPORT.md`:

| ℓ    | Kodaira | c_ℓ | #Ẽ_ns(F_ℓ)          | m_ℓ = c_ℓ · #Ẽ_ns(F_ℓ) |
|------|---------|-----|---------------------|------------------------|
| 2    | I₁*     | 2   | 2   (additive, G_a) | 4                      |
| 3    | I₂      | 2   | 4   (nonsplit)      | 8                      |
| 2243 | I₁      | 1   | 2242 (split)        | 2242                   |
| 4547 | III     | 2   | 4547 (additive)     | 9094                   |
| 5843 | I₂      | 2   | 5844 (nonsplit)     | 11688                  |

For ℓ ≠ p one has `E(Q_ℓ)[p] ↪ E(Q_ℓ)/E_1(Q_ℓ)`, a group of order `m_ℓ`, so
`E(Q_ℓ)[p] = 0` as soon as `p ∤ m_ℓ`; and then, by the local Euler-characteristic formula
together with local Tate duality and the Weil self-duality of `E[p]`,
`H^1(Q_ℓ, E[p]) = 0` outright.

The elliptic-curve content of that argument is written out in the report.  What is machine
checked **here** is only the resulting arithmetic bookkeeping: exactly which primes can
survive it.  The local-duality and Euler-characteristic steps, and the identification of the
integers `m_ℓ` with the curve's local data, are ordinary written mathematics *outside* the
formal statements below, which are divisibility facts about the five integers in the table.

## Scope of the corollary, corrected

The consequence one may draw is

    p ≥ 5,  p ∉ {19, 59, 487, 2243, 4547, 5843}  ⟹  H^1(Q_ℓ, E[p]) = 0 at every bad place ℓ.

The primes `19, 59, 487, 4547` are those dividing some `m_ℓ` (this is what is proved below);
the further exclusions `2243` and `5843` are the bad primes `ℓ` themselves, for which the
argument `ℓ ≠ p` used for the formal group is unavailable.  (`2` and `3` are excluded by
`p ≥ 5`.)

This simplifies the local conditions at the bad places: strict, unramified and Kummer
conditions coincide and vanish there.  It does **not** show that `Ш(E/Q)` is supported on
the exceptional set: a nonzero global class can restrict to zero in all of these (zero)
local groups, so vanishing of the bad-place cohomology is no obstruction to its existence.
Nor does it show that every global use of bad-reduction geometry is useless; it only kills
mechanisms whose output factors through those zero groups.
-/

namespace SeedBadPlace

/-- `m_ℓ = c_ℓ · #Ẽ_ns(F_ℓ)` for the five bad places `ℓ = 2, 3, 2243, 4547, 5843`. -/
def localOrder : Fin 5 → ℕ
  | 0 => 4
  | 1 => 8
  | 2 => 2242
  | 3 => 9094
  | 4 => 11688

private lemma prime_dvd_two_mul_two {p : ℕ} (hp : p.Prime) (h : p ∣ 4) : p = 2 := by
  have h' : p ∣ 2 * 2 := by norm_num at h ⊢; exact h
  rcases (Nat.Prime.dvd_mul hp).1 h' with h1 | h1 <;>
    exact (Nat.prime_dvd_prime_iff_eq hp (by norm_num)).1 h1

private lemma prime_dvd_eight {p : ℕ} (hp : p.Prime) (h : p ∣ 8) : p = 2 := by
  have h' : p ∣ 2 * 4 := by norm_num at h ⊢; exact h
  rcases (Nat.Prime.dvd_mul hp).1 h' with h1 | h1
  · exact (Nat.prime_dvd_prime_iff_eq hp (by norm_num)).1 h1
  · exact prime_dvd_two_mul_two hp h1

/-- The primes that can occur at a bad place of the seed curve are exactly
`2, 3, 19, 59, 487, 4547`. -/
theorem prime_dvd_localOrder_iff (p : ℕ) (hp : p.Prime) :
    (∃ i, p ∣ localOrder i) ↔ p = 2 ∨ p = 3 ∨ p = 19 ∨ p = 59 ∨ p = 487 ∨ p = 4547 := by
  constructor
  · rintro ⟨i, hi⟩
    fin_cases i
    · exact Or.inl (prime_dvd_two_mul_two hp hi)
    · exact Or.inl (prime_dvd_eight hp (by simpa [localOrder] using hi))
    · have h' : p ∣ 2 * (19 * 59) := by simpa [localOrder] using hi
      rcases (Nat.Prime.dvd_mul hp).1 h' with h1 | h1
      · exact Or.inl ((Nat.prime_dvd_prime_iff_eq hp (by norm_num)).1 h1)
      · rcases (Nat.Prime.dvd_mul hp).1 h1 with h2 | h2
        · exact Or.inr (Or.inr (Or.inl ((Nat.prime_dvd_prime_iff_eq hp (by norm_num)).1 h2)))
        · exact Or.inr (Or.inr (Or.inr (Or.inl
            ((Nat.prime_dvd_prime_iff_eq hp (by norm_num)).1 h2))))
    · have h' : p ∣ 2 * 4547 := by simpa [localOrder] using hi
      rcases (Nat.Prime.dvd_mul hp).1 h' with h1 | h1
      · exact Or.inl ((Nat.prime_dvd_prime_iff_eq hp (by norm_num)).1 h1)
      · exact Or.inr (Or.inr (Or.inr (Or.inr (Or.inr
          ((Nat.prime_dvd_prime_iff_eq hp (by norm_num)).1 h1)))))
    · have h' : p ∣ 8 * (3 * 487) := by simpa [localOrder] using hi
      rcases (Nat.Prime.dvd_mul hp).1 h' with h1 | h1
      · exact Or.inl (prime_dvd_eight hp h1)
      · rcases (Nat.Prime.dvd_mul hp).1 h1 with h2 | h2
        · exact Or.inr (Or.inl ((Nat.prime_dvd_prime_iff_eq hp (by norm_num)).1 h2))
        · exact Or.inr (Or.inr (Or.inr (Or.inr (Or.inl
            ((Nat.prime_dvd_prime_iff_eq hp (by norm_num)).1 h2)))))
  · rintro (rfl | rfl | rfl | rfl | rfl | rfl)
    · exact ⟨0, by norm_num [localOrder]⟩
    · exact ⟨4, by norm_num [localOrder]⟩
    · exact ⟨2, by norm_num [localOrder]⟩
    · exact ⟨2, by norm_num [localOrder]⟩
    · exact ⟨4, by norm_num [localOrder]⟩
    · exact ⟨3, by norm_num [localOrder]⟩

/-- **Exceptional-prime list.**  For every prime `p ≥ 5` other than `19, 59, 487` and the
bad prime `4547` itself, no bad place of the seed curve carries `p`-torsion:
`p ∤ c_ℓ · #Ẽ_ns(F_ℓ)` for all five bad places `ℓ`.  Combined with the local
Euler-characteristic argument written out in the report — and excluding in addition the
residue characteristics `p = 2243, 5843`, where the formal-group step does not apply — this
gives `H^1(Q_ℓ, E[p]) = 0` at every bad place.  See the module docstring for what that does
and does not imply about `Ш`. -/
theorem localOrder_coprime_of_generic (p : ℕ) (hp : p.Prime) (h5 : 5 ≤ p)
    (h19 : p ≠ 19) (h59 : p ≠ 59) (h487 : p ≠ 487) (h4547 : p ≠ 4547) :
    ∀ i, ¬ p ∣ localOrder i := by
  intro i hi
  rcases (prime_dvd_localOrder_iff p hp).1 ⟨i, hi⟩ with rfl | rfl | rfl | rfl | rfl | rfl <;>
    simp_all

end SeedBadPlace
