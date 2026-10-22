/-
Elementary arithmetic support: squarefree representatives of rational square classes,
squarefree divisors of a product of distinct primes, and the squarefree kernel of an integer all
of whose prime multiplicities are odd.
-/
import RequestProject.SDyadic.LocalEll

namespace SDyadic

open Run013

/-! ## Squarefree representatives -/

theorem squarefree_neg' {x : ℤ} (h : Squarefree x) : Squarefree (-x) := fun y hy =>
  h y (dvd_neg.mp hy)

/-- Every nonzero rational is a squarefree integer times a rational square. -/
theorem exists_squarefree_rep (d : ℚ) (hd : d ≠ 0) :
    ∃ e : ℤ, e ≠ 0 ∧ Squarefree e ∧ SqEq ℚ d (e : ℚ) := by
  set N : ℤ := d.num * (d.den : ℤ) with hN
  have hden : (d.den : ℚ) ≠ 0 := by
    exact_mod_cast d.den_nz
  have hnum : (d.num : ℚ) ≠ 0 := by
    exact_mod_cast Rat.num_ne_zero.mpr hd
  have hN0 : N ≠ 0 := mul_ne_zero (Rat.num_ne_zero.mpr hd) (by exact_mod_cast d.den_nz)
  have hstep1 : SqEq ℚ d ((N : ℤ) : ℚ) := by
    refine ⟨((d.den : ℚ))⁻¹, inv_ne_zero hden, ?_⟩
    have h : ((N : ℤ) : ℚ) * (((d.den : ℚ))⁻¹) ^ 2 = (d.num : ℚ) / (d.den : ℚ) := by
      rw [hN]; push_cast; field_simp
    rw [h, Rat.num_div_den]
  obtain ⟨a, b, hab, hsf⟩ := Nat.sq_mul_squarefree N.natAbs
  have hNa : N.natAbs ≠ 0 := Int.natAbs_ne_zero.mpr hN0
  have hb0 : b ≠ 0 := by
    rintro rfl
    simp at hab
    exact hNa hab.symm
  have ha0 : a ≠ 0 := by
    rintro rfl
    simp at hab
    exact hNa hab.symm
  have hbQ : ((b : ℚ)) ≠ 0 := by exact_mod_cast hb0
  rcases Int.natAbs_eq N with hsign | hsign
  · refine ⟨(a : ℤ), by exact_mod_cast ha0, Int.squarefree_natCast.mpr hsf, ?_⟩
    refine hstep1.trans ⟨(b : ℚ), hbQ, ?_⟩
    rw [hsign, ← hab]
    push_cast
    ring
  · refine ⟨-(a : ℤ), by simpa using (by exact_mod_cast ha0 : (a : ℤ) ≠ 0),
      squarefree_neg' (Int.squarefree_natCast.mpr hsf), ?_⟩
    refine hstep1.trans ⟨(b : ℚ), hbQ, ?_⟩
    rw [hsign, ← hab]
    push_cast
    ring

/-- A prime dividing a squarefree integer divides it exactly once. -/
theorem exists_cofactor_of_squarefree {e : ℤ} (hsf : Squarefree e) {p : ℕ} (hp : p.Prime)
    (hdvd : (p : ℤ) ∣ e) : ∃ d₀ : ℤ, e = (p : ℤ) * d₀ ∧ ¬ (p : ℤ) ∣ d₀ := by
  obtain ⟨d₀, rfl⟩ := hdvd
  refine ⟨d₀, rfl, ?_⟩
  rintro ⟨t, rfl⟩
  have hunit := hsf (p : ℤ) ⟨t, by ring⟩
  have : ¬ IsUnit (p : ℤ) := by
    rw [Int.isUnit_iff]
    intro hc
    rcases hc with hc | hc
    · exact hp.one_lt.ne' (by exact_mod_cast hc)
    · have : (0 : ℤ) ≤ (p : ℤ) := Int.natCast_nonneg p
      omega
  exact this hunit

/-! ## Squarefree divisors of a product of distinct primes -/

theorem nat_dvd_prime_cases {p n : ℕ} (hp : p.Prime) (h : n ∣ p) : n = 1 ∨ n = p :=
  (Nat.Prime.eq_one_or_self_of_dvd hp n h)

theorem nat_dvd_two_primes {ℓ Q n : ℕ} (hℓ : ℓ.Prime) (hQ : Q.Prime) (h : n ∣ ℓ * Q) :
    n = 1 ∨ n = ℓ ∨ n = Q ∨ n = ℓ * Q := by
  obtain ⟨n₁, n₂, h₁, h₂, rfl⟩ := exists_dvd_and_dvd_of_dvd_mul h
  rcases nat_dvd_prime_cases hℓ h₁ with rfl | rfl <;>
    rcases nat_dvd_prime_cases hQ h₂ with rfl | rfl <;> simp

theorem nat_dvd_three_primes {ℓ₁ ℓ₂ Q n : ℕ} (hℓ₁ : ℓ₁.Prime) (hℓ₂ : ℓ₂.Prime) (hQ : Q.Prime)
    (h : n ∣ ℓ₁ * ℓ₂ * Q) :
    n = 1 ∨ n = ℓ₁ ∨ n = ℓ₂ ∨ n = ℓ₁ * ℓ₂ ∨ n = Q ∨ n = ℓ₁ * Q ∨ n = ℓ₂ * Q
      ∨ n = ℓ₁ * ℓ₂ * Q := by
  obtain ⟨n₁, n₂, h₁, h₂, rfl⟩ := exists_dvd_and_dvd_of_dvd_mul h
  rcases nat_dvd_two_primes hℓ₁ hℓ₂ h₁ with rfl | rfl | rfl | rfl <;>
    rcases nat_dvd_prime_cases hQ h₂ with rfl | rfl <;> simp

/-- A squarefree natural number all of whose prime factors divide `M` divides `M`. -/
theorem dvd_of_squarefree_of_primes {n M : ℕ} (hn : n ≠ 0) (hM : M ≠ 0) (hsf : Squarefree n)
    (h : ∀ p : ℕ, p.Prime → p ∣ n → p ∣ M) : n ∣ M := by
  rw [← Nat.factorization_le_iff_dvd hn hM, Finsupp.le_def]
  intro p
  by_cases hp : p.Prime
  · rcases Nat.eq_zero_or_pos (n.factorization p) with h0 | h0
    · simp [h0]
    · have hpn : p ∣ n := (Nat.Prime.dvd_iff_one_le_factorization hp hn).mpr h0
      have h1 : n.factorization p ≤ 1 := (Nat.squarefree_iff_factorization_le_one hn).mp hsf p
      have h2 : 1 ≤ M.factorization p :=
        (Nat.Prime.dvd_iff_one_le_factorization hp hM).mp (h p hp hpn)
      omega
  · simp [Nat.factorization_eq_zero_of_not_prime _ hp]

end SDyadic
