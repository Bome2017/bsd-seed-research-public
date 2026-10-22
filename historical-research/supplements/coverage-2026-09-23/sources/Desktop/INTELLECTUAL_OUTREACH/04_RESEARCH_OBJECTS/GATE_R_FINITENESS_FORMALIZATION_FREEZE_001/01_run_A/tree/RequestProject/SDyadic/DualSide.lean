/-
Exhaustion on the dual side.

For `(dualA, dualB) = (A q, r² q²)` the parity obstruction confines a locally soluble squarefree
`e` to `±1, ±2, ±q, ±2q`; the condition at `q` (the discriminant `Δ = D` is a non-residue mod `q`,
and `2` is a non-residue because `q ≡ 5 mod 8`) leaves only `±1`; and the obstruction at a prime
`ℓ ≡ 3 (mod 4)` dividing `D` to an odd power removes `−1`.  Only the trivial class survives.
-/
import RequestProject.SDyadic.PhiSide
import RequestProject.SDyadic.LocalEll

namespace SDyadic

open Run013

/-- **Exhaustion on the dual side.**  On `H₄₁`, the only everywhere-locally-soluble square class
for `(dualA, dualB)` is the trivial one. -/
theorem dual_exhaustion {ε : ℤ} {m q : ℕ} [hqf : Fact (Nat.Prime q)] (hP : Params ε m q)
    (hH : (DD ε m < 0 ∧ sCount ε m = 1) ∨
      (0 < DD ε m ∧ sCount ε m = 2 ∧ ∀ ℓ ∈ ellSet ε m, ℓ % 4 = 3))
    {e : ℤ} (he : e ≠ 0) (hsf : Squarefree e)
    (hL : LocalKummerAll (dualA ε m q) (dualB ε m q) ((e : ℤ) : ℚ)) :
    SqEq ℚ ((e : ℤ) : ℚ) 1 := by
  classical
  have hqp : q.Prime := hqf.out
  have hq2 : q ≠ 2 := q_ne_two hP
  have hqpos : (0 : ℤ) < (q : ℤ) := by exact_mod_cast hqp.pos
  have hr0 : rr ε m ≠ 0 := by
    intro hc
    simp only [rr] at hc
    rcases hP.eps_unit with h | h <;> rw [h] at hc <;> simp at hc
  have hbI0 : (rr ε m) ^ 2 * (q : ℤ) ^ 2 ≠ 0 :=
    mul_ne_zero (pow_ne_zero 2 hr0) (pow_ne_zero 2 hqpos.ne')
  have hAeq : dualA ε m q = ((AA ε m * (q : ℤ) : ℤ) : ℚ) := rfl
  have hBeq : dualB ε m q = (((rr ε m) ^ 2 * (q : ℤ) ^ 2 : ℤ) : ℚ) := rfl
  have hbne : dualB ε m q ≠ 0 := by rw [hBeq]; exact_mod_cast hbI0
  have heQ : ((e : ℤ) : ℚ) ≠ 0 := by exact_mod_cast he
  rw [localKummerAll_iff_cov hbne heQ, hAeq, hBeq] at hL
  obtain ⟨-, hpad⟩ := hL
  have hcov : ∀ (P : ℕ) [Fact P.Prime],
      Cov ℚ_[P] ((AA ε m * (q : ℤ) : ℤ) : ℚ_[P]) (((rr ε m) ^ 2 * (q : ℤ) ^ 2 : ℤ) : ℚ_[P])
        ((e : ℤ) : ℚ_[P]) := by
    intro P _
    simpa only [Rat.cast_intCast] using hpad P
  have hΔ : (AA ε m) ^ 2 - 4 * (rr ε m) ^ 2 = DD ε m := A_sq_sub_four_B ε m
  have hqr : ¬ (q : ℤ) ∣ rr ε m := q_not_dvd_r hP
  -- confinement to divisors of `2q`
  have hMdvd : e.natAbs ∣ 2 * q := by
    refine natAbs_dvd_of_local hsf he (Nat.mul_ne_zero two_ne_zero hqp.pos.ne') ?_ hcov
    intro p hp hpb
    have hpZ : Prime ((p : ℤ)) := Nat.prime_iff_prime_int.mp hp
    have hcase : (p : ℤ) ∣ rr ε m ∨ (p : ℤ) ∣ (q : ℤ) := by
      rcases hpZ.dvd_mul.mp hpb with h | h
      · exact Or.inl (hpZ.dvd_of_dvd_pow h)
      · exact Or.inr (hpZ.dvd_of_dvd_pow h)
    rcases hcase with h | h
    · have h2 : (p : ℤ) ∣ 2 ^ m := by
        rcases hP.eps_unit with he' | he'
        · simpa [rr, he'] using h
        · exact dvd_neg.mp (by simpa [rr, he'] using h)
      have h2' : p ∣ 2 ^ m := by exact_mod_cast h2
      have : p = 2 := (Nat.prime_dvd_prime_iff_eq hp Nat.prime_two).mp (hp.dvd_of_dvd_pow h2')
      rw [this]
      exact Dvd.dvd.mul_right dvd_rfl q
    · have : p ∣ q := by exact_mod_cast h
      rw [(Nat.prime_dvd_prime_iff_eq hp hqp).mp this]
      exact Dvd.dvd.mul_left dvd_rfl 2
  -- residue facts at `q`
  have hns2 : ¬ IsSquare (((2 : ℤ)) : ZMod q) := by
    have hcast : (((2 : ℤ)) : ZMod q) = (2 : ZMod q) := by push_cast; ring
    rw [hcast, ZMod.exists_sq_eq_two_iff hq2]
    have := hP.q_mod_eight
    omega
  have hsqm1 : IsSquare ((-1 : ZMod q)) :=
    (ZMod.exists_sq_eq_neg_one_iff).mpr (by have := hP.q_mod_eight; omega)
  have hnsm2 : ¬ IsSquare (((-2 : ℤ)) : ZMod q) := by
    intro hc
    refine hns2 ?_
    have hrw : (((2 : ℤ)) : ZMod q) = (-1) * (((-2 : ℤ)) : ZMod q) := by push_cast; ring
    rw [hrw]
    exact hsqm1.mul hc
  have hqnd1 : ¬ (q : ℤ) ∣ (1 : ℤ) := by
    intro h
    have : (q : ℕ) ∣ 1 := by exact_mod_cast h
    exact hqp.one_lt.ne' (Nat.dvd_one.mp this)
  have hqnd2 : ¬ (q : ℤ) ∣ (2 : ℤ) := by
    intro h
    have : (q : ℕ) ∣ 2 := by exact_mod_cast h
    exact hq2 ((Nat.prime_dvd_prime_iff_eq hqp Nat.prime_two).mp this)
  -- the `ℓ`-adic data
  obtain ⟨ell, hellmem, hell4⟩ := exists_ell_mod_four_three hP hH
  have hellp : ell.Prime := ell_prime hellmem
  haveI : Fact ell.Prime := ⟨hellp⟩
  have hellq : ¬ (ell : ℤ) ∣ (q : ℤ) := by
    intro h
    have : ell ∣ q := by exact_mod_cast h
    exact ell_ne_q hP hellmem ((Nat.prime_dvd_prime_iff_eq hellp hqp).mp this)
  obtain ⟨k, w, hk, hw, hfac⟩ := D_ell_factor hP hellmem
  -- case analysis on the squarefree divisors of `2q`
  rcases nat_dvd_two_primes Nat.prime_two hqp hMdvd with hN | hN | hN | hN <;>
    rcases Int.natAbs_eq e with hE | hE <;> rw [hN] at hE <;> push_cast at hE
  · exact ⟨1, one_ne_zero, by rw [hE]; norm_num⟩
  · exfalso
    have hc := hcov ell
    rw [hE] at hc
    exact not_cov_ell_neg_one hell4 hΔ hk hellq hw hfac hc
  · exfalso
    have hsq := isSquare_of_cov_q hq2 hΔ (by rw [hE]; exact hqnd2) hqr (hcov q)
    rw [hE] at hsq
    exact hns2 hsq
  · exfalso
    have hsq := isSquare_of_cov_q hq2 hΔ (by rw [hE]; simpa using hqnd2) hqr (hcov q)
    rw [hE] at hsq
    exact hnsm2 hsq
  · exfalso
    have hc := hcov q
    have hee : e = (q : ℤ) * 1 := by rw [hE]; ring
    rw [hee] at hc
    exact not_cov_q_of_odd_val hq2 hΔ hqnd1 hP.legendre_D_q hc
  · exfalso
    have hc := hcov q
    have hee : e = (q : ℤ) * (-1) := by rw [hE]; ring
    rw [hee] at hc
    exact not_cov_q_of_odd_val hq2 hΔ (by simpa using hqnd1) hP.legendre_D_q hc
  · exfalso
    have hc := hcov q
    have hee : e = (q : ℤ) * 2 := by rw [hE]; ring
    rw [hee] at hc
    exact not_cov_q_of_odd_val hq2 hΔ hqnd2 hP.legendre_D_q hc
  · exfalso
    have hc := hcov q
    have hee : e = (q : ℤ) * (-2) := by rw [hE]; ring
    rw [hee] at hc
    exact not_cov_q_of_odd_val hq2 hΔ (by simpa using hqnd2) hP.legendre_D_q hc

end SDyadic
