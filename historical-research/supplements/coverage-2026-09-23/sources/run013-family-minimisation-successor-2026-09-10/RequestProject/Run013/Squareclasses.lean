/-
Run013 — `Squareclasses.lean`

Elementary facts about square classes of `ℚ` and about squarefree integers:

* every nonzero rational is square-equivalent to a squarefree integer;
* a squarefree number all of whose prime factors divide `m` divides `m`;
* the divisors of a product of two distinct primes.

These are the ingredients of the *structural* reduction to finitely many square
classes; no finite list is postulated.
-/
import RequestProject.Run013.Basic

namespace Run013

/-- Every nonzero rational is square-equivalent to a squarefree integer. -/
theorem exists_squarefree_rep (d : ℚ) (hd : d ≠ 0) :
    ∃ D : ℤ, Squarefree D ∧ SqEq ℚ d (D : ℚ) := by
  -- first: `d` is square-equivalent to the integer `num * den`
  have hden : (d.den : ℚ) ≠ 0 := Nat.cast_ne_zero.mpr d.den_nz
  have h1 : SqEq ℚ d ((d.num * (d.den : ℤ) : ℤ) : ℚ) := by
    refine ⟨1 / (d.den : ℚ), by positivity, ?_⟩
    push_cast
    field_simp
    exact Rat.mul_den_eq_num d
  set m : ℤ := d.num * (d.den : ℤ) with hm
  have hmne : m ≠ 0 := by
    have : d.num ≠ 0 := Rat.num_ne_zero.mpr hd
    exact mul_ne_zero this (Int.natCast_ne_zero.mpr d.den_nz)
  obtain ⟨A, B, hAB, hAsq⟩ := Nat.sq_mul_squarefree m.natAbs
  have hBne : B ≠ 0 := by
    rintro rfl
    simp at hAB
    exact hmne (Int.natAbs_eq_zero.mp hAB.symm)
  have hAne : A ≠ 0 := by
    rintro rfl
    simp at hAB
    exact hmne (Int.natAbs_eq_zero.mp hAB.symm)
  -- signed squarefree representative
  refine ⟨if 0 < m then (A : ℤ) else -(A : ℤ), ?_, ?_⟩
  · have : Squarefree ((A : ℤ)) := Int.squarefree_natAbs.mp (by simpa using hAsq)
    split
    · exact this
    · intro x hx
      exact this x (by simpa using hx.neg_right)
  · refine h1.trans ⟨(B : ℚ), by exact_mod_cast hBne, ?_⟩
    have habs : m.natAbs = B ^ 2 * A := hAB.symm
    split_ifs with hpos
    · have : m = (B : ℤ) ^ 2 * (A : ℤ) := by
        have := Int.natAbs_of_nonneg (le_of_lt hpos)
        rw [← this, habs]; push_cast; ring
      rw [this]; push_cast; ring
    · have hneg : m < 0 := lt_of_le_of_ne (not_lt.mp hpos) hmne
      have : m = -((B : ℤ) ^ 2 * (A : ℤ)) := by
        have h2 : (m.natAbs : ℤ) = -m := Int.ofNat_natAbs_of_nonpos (le_of_lt hneg)
        rw [habs] at h2
        push_cast at h2
        linarith
      rw [this]; push_cast; ring

/-- A squarefree number whose prime factors all divide `m` divides `m`. -/
theorem squarefree_dvd_of_primes {n m : ℕ} (hn : Squarefree n) (hm : m ≠ 0)
    (h : ∀ p, p.Prime → p ∣ n → p ∣ m) : n ∣ m := by
  have hn0 : n ≠ 0 := hn.ne_zero
  rw [← Nat.factorization_le_iff_dvd hn0 hm]
  intro p
  by_cases hp : p.Prime
  · by_cases hpn : p ∣ n
    · have h1 : n.factorization p ≤ 1 := (Nat.squarefree_iff_factorization_le_one hn0).mp hn p
      have h2 : 0 < m.factorization p := hp.factorization_pos_of_dvd hm (h p hp hpn)
      omega
    · simp [Nat.factorization_eq_zero_of_not_dvd hpn]
  · simp [Nat.factorization_eq_zero_of_not_prime _ hp]

/-- The divisors of a product of two distinct primes. -/
theorem dvd_two_primes {n r s : ℕ} (hr : r.Prime) (hs : s.Prime) (h : n ∣ r * s) :
    n = 1 ∨ n = r ∨ n = s ∨ n = r * s := by
  obtain ⟨k₁, k₂, h1, h2, rfl⟩ := Nat.dvd_mul.mp h
  rcases hr.eq_one_or_self_of_dvd k₁ h1 with rfl | rfl <;>
    rcases hs.eq_one_or_self_of_dvd k₂ h2 with rfl | rfl <;> simp

/-- From a squarefree integer to a signed product of allowed primes. -/
theorem squarefree_int_classify {D : ℤ} {r s : ℕ} (hD : Squarefree D)
    (hr : r.Prime) (hs : s.Prime)
    (h : ∀ p : ℕ, p.Prime → (p : ℤ) ∣ D → p = r ∨ p = s) :
    D = 1 ∨ D = -1 ∨ D = (r : ℤ) ∨ D = -(r : ℤ) ∨ D = (s : ℤ) ∨ D = -(s : ℤ)
      ∨ D = (r : ℤ) * s ∨ D = -((r : ℤ) * s) := by
  have hDne : D ≠ 0 := hD.ne_zero
  have hnat : Squarefree D.natAbs := Int.squarefree_natAbs.mpr hD
  have hdvd : D.natAbs ∣ r * s := by
    refine squarefree_dvd_of_primes hnat (Nat.mul_ne_zero hr.ne_zero hs.ne_zero) ?_
    intro p hp hpn
    have : (p : ℤ) ∣ D := Int.ofNat_dvd_left.mpr hpn
    rcases h p hp this with rfl | rfl
    · exact Dvd.intro s rfl
    · exact Dvd.intro_left r rfl
  have hcases := dvd_two_primes hr hs hdvd
  have habs : D = (D.natAbs : ℤ) ∨ D = -(D.natAbs : ℤ) := by
    rcases Int.natAbs_eq D with h | h
    · exact Or.inl h
    · exact Or.inr h
  rcases hcases with h1 | h1 | h1 | h1 <;> rw [h1] at habs <;>
    rcases habs with h2 | h2 <;> push_cast at h2 <;> simp [h2]

end Run013
