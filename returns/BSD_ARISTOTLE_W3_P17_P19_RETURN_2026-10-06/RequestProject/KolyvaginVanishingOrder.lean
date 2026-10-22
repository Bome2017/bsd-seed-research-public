import Mathlib

/-!
# Zhang's vanishing order `ν_p` versus the Selmer ranks: exact bookkeeping

Fix the seed `E` (root number `ε(E/ℚ) = +1`, two independent rational points), an imaginary
quadratic field `K` satisfying the Heegner hypothesis, and a prime `p` to which Zhang's Kolyvagin
system results apply. Write

* `rp = dim_{𝔽_p} Sel_p(E/K)^+`. For odd `p` this is `dim Sel_p(E/ℚ)`.
* `rm = dim_{𝔽_p} Sel_p(E/K)^-`. This is `dim Sel_p(E^K/ℚ)`.
* `ν` is Zhang's vanishing order `ν_p = min {ω(n) : c(n) ≠ 0}` of the Kolyvagin system.

Zhang's Lemma 8.4 says `dim Sel^{ε_ν} = ν + 1` and `dim Sel^{-ε_ν} ≤ ν`, where
`ε_ν = ε(E/ℚ)·(-1)^{ν+1}`. With `ε(E/ℚ) = +1` we get `ε_ν = +` exactly when `ν` is odd. Its two
cases are the hypotheses `h_odd` and `h_even` below. The two rational points give `2 ≤ rp`.

The theorems are pure arithmetic consequences of those inputs. No parity hypothesis is needed.

* `nu_succ_eq_max`: `ν + 1 = max rp rm`, so `ν` is fixed by the two Selmer ranks.
* `nu_le_two_iff`: `ν ≤ 2 ↔ rp = 2 ∧ rm ≤ 3`.
* `nu_le_two_iff_of_rm_eq_one`: if `rm = 1`, then `ν ≤ 2 ↔ rp = 2`, and in that case `ν = 1`.

Hence, for every `p` with `dim Sel_p(E^K/ℚ) = 1`, the criterion "`ν_p ≤ 2`" is equivalent to
`Sel_p(E/ℚ)` having dimension `2`, i.e. to `Ш(E/ℚ)[p] = 0`. The `ν = 2` alternative can occur
only at primes where `dim Sel_p(E^K/ℚ) = 3`.
-/

namespace Heegner

/-- Zhang's vanishing order is one less than the larger of the two Selmer ranks. -/
theorem nu_succ_eq_max (rp rm ν : ℕ)
    (h_odd : Odd ν → rp = ν + 1 ∧ rm ≤ ν)
    (h_even : Even ν → rm = ν + 1 ∧ rp ≤ ν) :
    ν + 1 = max rp rm := by
  rcases Nat.even_or_odd ν with h | h
  · obtain ⟨h1, h2⟩ := h_even h; obtain ⟨k, hk⟩ := h; omega
  · obtain ⟨h1, h2⟩ := h_odd h; obtain ⟨k, hk⟩ := h; omega

/-- With two independent rational points (`2 ≤ rp`), the vanishing order is at least `1`. -/
theorem one_le_nu (rp rm ν : ℕ)
    (h_even : Even ν → rm = ν + 1 ∧ rp ≤ ν) (h_rank : 2 ≤ rp) : 1 ≤ ν := by
  by_contra h0
  have hν : ν = 0 := by omega
  obtain ⟨_, h2⟩ := h_even (by rw [hν]; exact ⟨0, rfl⟩)
  omega

/-- `ν ≤ 2` holds exactly when `Sel^+` has dimension `2` and `Sel^-` has dimension at most `3`. -/
theorem nu_le_two_iff (rp rm ν : ℕ)
    (h_odd : Odd ν → rp = ν + 1 ∧ rm ≤ ν)
    (h_even : Even ν → rm = ν + 1 ∧ rp ≤ ν) (h_rank : 2 ≤ rp) :
    ν ≤ 2 ↔ rp = 2 ∧ rm ≤ 3 := by
  rcases Nat.even_or_odd ν with h | h
  · obtain ⟨h1, h2⟩ := h_even h; obtain ⟨k, hk⟩ := h; omega
  · obtain ⟨h1, h2⟩ := h_odd h; obtain ⟨k, hk⟩ := h; omega

/-- If `dim Sel_p(E^K/ℚ) = 1`, then `ν ≤ 2` is equivalent to `dim Sel_p(E/ℚ) = 2`, and it forces
`ν = 1`. So the two-prime alternative (`ν = 2`) is impossible at such primes. -/
theorem nu_le_two_iff_of_rm_eq_one (rp rm ν : ℕ)
    (h_odd : Odd ν → rp = ν + 1 ∧ rm ≤ ν)
    (h_even : Even ν → rm = ν + 1 ∧ rp ≤ ν) (h_rank : 2 ≤ rp) (h_rm : rm = 1) :
    (ν ≤ 2 ↔ rp = 2) ∧ (ν ≤ 2 → ν = 1) := by
  rcases Nat.even_or_odd ν with h | h
  · obtain ⟨h1, h2⟩ := h_even h; obtain ⟨k, hk⟩ := h; omega
  · obtain ⟨h1, h2⟩ := h_odd h; obtain ⟨k, hk⟩ := h; omega

end Heegner
