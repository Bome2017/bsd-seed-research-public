module

public import Mathlib

/-!
# Arithmetic behind the exceptional set `{19, 59, 487}` and the torus weight

These are the elementary arithmetic facts used in `research_return/UPPER_CONTROL.md`.

* At `q = 2243` (split `I₁`), `E[p]^{G_{ℚ_q}} ≠ 0` iff `μ_p ⊂ ℚ_q` iff `p ∣ q - 1 = 2242`.
* At `q = 5843` (non-split `I₂`), `E[p]^{G_{ℚ_q}} ≠ 0` iff `q ≡ -1 (mod p)` iff `p ∣ 5844`.
* At `q = 3` (non-split `I₂`), the same condition is `p ∣ 4`.

So for primes `p ≥ 5` the only cases are `p ∈ {19, 59}` (from `2243`) and `p = 487`
(from `5843`). `torus_weight_nontrivial` is the weight computation showing
`H¹(GL₂(𝔽_p), ad⁰) = 0` for every `p ≥ 5`: the character `diag(a, d) ↦ (d/a)²` is nontrivial.
-/

@[expose] public section

namespace Seed.Exceptional

theorem primeFactors_2242 : Nat.primeFactors 2242 = {2, 19, 59} := by
  rw [show (2242 : ℕ) = 2 * 19 * 59 by norm_num, Nat.primeFactors_mul (by norm_num) (by norm_num),
    Nat.primeFactors_mul (by norm_num) (by norm_num), Nat.Prime.primeFactors (by norm_num),
    Nat.Prime.primeFactors (by norm_num), Nat.Prime.primeFactors (by norm_num)]
  rfl

theorem primeFactors_5844 : Nat.primeFactors 5844 = {2, 3, 487} := by
  rw [show (5844 : ℕ) = 2 ^ 2 * 3 * 487 by norm_num,
    Nat.primeFactors_mul (by norm_num) (by norm_num),
    Nat.primeFactors_mul (by norm_num) (by norm_num), Nat.primeFactors_prime_pow (by norm_num)
      (by norm_num), Nat.Prime.primeFactors (by norm_num), Nat.Prime.primeFactors (by norm_num)]
  rfl

/-- The local invariants at `2243`, `5843` and `3` can be nonzero only for
`p ∈ {2, 3, 19, 59, 487}`. -/
theorem exceptional_local_primes (p : ℕ) (hp : p.Prime) (h : p ∣ 2242 ∨ p ∣ 5844 ∨ p ∣ 4) :
    p ∈ ({2, 3, 19, 59, 487} : Finset ℕ) := by
  rcases h with h | h | h
  · have : p ∈ Nat.primeFactors 2242 := Nat.mem_primeFactors.mpr ⟨hp, h, by norm_num⟩
    rw [primeFactors_2242] at this
    simp only [Finset.mem_insert, Finset.mem_singleton] at this ⊢
    omega
  · have : p ∈ Nat.primeFactors 5844 := Nat.mem_primeFactors.mpr ⟨hp, h, by norm_num⟩
    rw [primeFactors_5844] at this
    simp only [Finset.mem_insert, Finset.mem_singleton] at this ⊢
    omega
  · have h2 : p ∣ 2 ^ 2 := by simpa using h
    have := (Nat.prime_dvd_prime_iff_eq hp Nat.prime_two).mp (hp.dvd_of_dvd_pow h2)
    simp [this]

/-- For `p ≥ 5` the torus character `diag(a, d) ↦ (d / a)²` of `GL₂(𝔽_p)` is nontrivial:
take `a = 2`, `d = 1`. This kills `H¹(U, ad⁰)^T`, so `H¹(GL₂(𝔽_p), ad⁰) = 0`. For `SL₂`
(with `d = a⁻¹`) the character is `a⁻⁴`, which is trivial when `p = 5`. -/
theorem torus_weight_nontrivial (p : ℕ) [hp : Fact p.Prime] (h5 : 5 ≤ p) :
    ∃ a : ZMod p, a ≠ 0 ∧ (1 / a) ^ 2 ≠ 1 := by
  refine ⟨2, ?_, ?_⟩
  · intro h
    have : ((2 : ℕ) : ZMod p) = 0 := by exact_mod_cast h
    rw [ZMod.natCast_eq_zero_iff] at this
    have := Nat.le_of_dvd (by norm_num) this
    omega
  · intro h
    have h2 : (2 : ZMod p) ≠ 0 := by
      intro h'
      have : ((2 : ℕ) : ZMod p) = 0 := by exact_mod_cast h'
      rw [ZMod.natCast_eq_zero_iff] at this
      have := Nat.le_of_dvd (by norm_num) this
      omega
    have h4 : (4 : ZMod p) = 1 := by
      field_simp at h
      linear_combination -h
    have : ((3 : ℕ) : ZMod p) = 0 := by
      push_cast; linear_combination h4
    rw [ZMod.natCast_eq_zero_iff] at this
    have := Nat.le_of_dvd (by norm_num) this
    omega

end Seed.Exceptional
