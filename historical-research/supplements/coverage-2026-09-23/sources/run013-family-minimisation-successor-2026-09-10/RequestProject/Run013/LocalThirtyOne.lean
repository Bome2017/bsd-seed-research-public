/-
Run013 — `LocalThirtyOne.lean`

The local condition at `p = 31`, made explicit.

* On the **dual** side the coefficient is `b = 64 q^2`, which is prime to `31` (because
  `q ≠ 31`).  The support lemma therefore applies at `p = 31` and excludes every square
  class with `v_31 = 1`.  This is the reason `31` never appears in
  `Sel^{hat phi_q}(E'_q/Q)`.

* On the **`phi`** side the coefficient is `b = -31 q^2`, which *is* divisible by `31`.
  There the prime `31` is admitted into the support, and the classes `31`, `-31 q` etc.
  are separated instead by the `2`-adic condition of `LocalTwo.lean`
  (`D ≡ 1 (mod 4)`, and `31 ≡ 3 (mod 4)`).  This asymmetry is exactly the one recorded
  in the frozen proof.
-/
import RequestProject.Run013.Support

namespace Run013

instance : Fact (Nat.Prime 31) := ⟨by norm_num⟩

/-- **Local exclusion at `31` for the dual covering.** -/
theorem local31_dual (q D D₁ : ℤ) (hq : ¬ (31 : ℤ) ∣ q)
    (hD : D = 31 * D₁) (hD₁ : ¬ (31 : ℤ) ∣ D₁) :
    ¬ Cov ℚ_[31] ((-15 * q : ℤ) : ℚ_[31]) ((64 * q ^ 2 : ℤ) : ℚ_[31]) ((D : ℤ) : ℚ_[31]) := by
  have hb : ¬ ((31 : ℕ) : ℤ) ∣ (64 * q ^ 2 : ℤ) := by
    intro h
    have h31 : Prime (31 : ℤ) := by
      have : Nat.Prime 31 := by norm_num
      exact_mod_cast Nat.prime_iff_prime_int.mp this
    rcases h31.dvd_mul.mp (by exact_mod_cast h) with h1 | h1
    · norm_num at h1
    · exact hq (h31.dvd_of_dvd_pow h1)
  exact support_lemma (p := 31) (-15 * q) (64 * q ^ 2) D D₁ hb hD (by exact_mod_cast hD₁)

end Run013
