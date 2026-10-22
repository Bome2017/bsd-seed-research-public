/-
Structure of the dyadic parameters: elementary congruences satisfied by `D` and `q`, and the
squarefree kernel of `D`.

Because every prime multiplicity of `D` is odd (a hypothesis of `Params`), the squarefree part of
`|D|` is exactly the product of its prime divisors; on the `H₄₁` stratum that product is `ℓ`
(one prime) or `ℓ₁ ℓ₂` (two primes).
-/
import RequestProject.SDyadic.Arith
import RequestProject.SDyadic.Family

namespace SDyadic

open Run013

/-! ## Congruences -/

theorem D_sub_one_dvd (ε : ℤ) (m : ℕ) (hm : 3 ≤ m) : (32 : ℤ) ∣ (DD ε m - 1) := by
  obtain ⟨t, rfl⟩ : ∃ t, m = 3 + t := ⟨m - 3, by omega⟩
  refine ⟨-(ε * 2 ^ t), ?_⟩
  simp only [DD, rr]
  rw [pow_add]
  ring

theorem D_not_two_dvd (ε : ℤ) (m : ℕ) : ¬ (2 : ℤ) ∣ DD ε m := by
  have h : DD ε m = 1 - 4 * rr ε m := rfl
  rw [h]
  rintro ⟨k, hk⟩
  omega

theorem D_ne_zero (ε : ℤ) (m : ℕ) : DD ε m ≠ 0 := by
  intro h
  exact D_not_two_dvd ε m (h ▸ dvd_zero 2)

/-- `1 − 2A + D = 0`, the identity behind the `q` and `Dq` covering witnesses. -/
theorem one_sub_two_A_add_D (ε : ℤ) (m : ℕ) : 1 - 2 * AA ε m + DD ε m = 0 := by
  simp only [AA, DD]; ring

/-- The `φ` first coefficient in the factored shape used by the dyadic analysis. -/
theorem phiA_eq (ε : ℤ) (m : ℕ) (q : ℕ) :
    (-2 * AA ε m * (q : ℤ) : ℤ) = -((q : ℤ) + DD ε m * (q : ℤ)) := by
  have h := one_sub_two_A_add_D ε m
  linear_combination (q : ℤ) * h

/-! ## The squarefree kernel of `D` -/

/-- If every prime multiplicity of `n` is odd, the squarefree part of `n` is the product of its
prime divisors. -/
theorem sq_mul_radical_of_odd_multiplicities {n : ℕ} (hn : n ≠ 0)
    (hodd : ∀ p ∈ n.primeFactors, Odd (n.factorization p)) :
    ∃ b : ℕ, b ≠ 0 ∧ n = b ^ 2 * (∏ p ∈ n.primeFactors, p) := by
  obtain ⟨a, b, hab, hsf⟩ := Nat.sq_mul_squarefree n
  have hb0 : b ≠ 0 := by rintro rfl; simp at hab; exact hn hab.symm
  have ha0 : a ≠ 0 := by rintro rfl; simp at hab; exact hn hab.symm
  have hfac : ∀ p : ℕ, p.Prime → n.factorization p = 2 * b.factorization p + a.factorization p := by
    intro p hp
    rw [← hab, Nat.factorization_mul (pow_ne_zero 2 hb0) ha0]
    simp [Nat.factorization_pow]
  have hprimes : a.primeFactors = n.primeFactors := by
    ext p
    simp only [Nat.mem_primeFactors]
    constructor
    · rintro ⟨hp, hpa, -⟩
      exact ⟨hp, dvd_trans hpa ⟨b ^ 2, by rw [← hab]; ring⟩, hn⟩
    · rintro ⟨hp, hpn, -⟩
      refine ⟨hp, ?_, ha0⟩
      have hodd' := hodd p (Nat.mem_primeFactors.mpr ⟨hp, hpn, hn⟩)
      rw [hfac p hp] at hodd'
      have : a.factorization p ≠ 0 := by
        rcases hodd' with ⟨t, ht⟩
        omega
      exact Nat.dvd_of_factorization_pos this
  refine ⟨b, hb0, ?_⟩
  rw [← hprimes, Nat.prod_primeFactors_of_squarefree hsf, ← hab]

/-- The squarefree kernel of `D`, under the odd-valuation hypothesis of `Params`. -/
theorem D_kernel {ε : ℤ} {m q : ℕ} [Fact (Nat.Prime q)] (hP : Params ε m q) :
    ∃ b : ℕ, b ≠ 0 ∧ (DD ε m).natAbs = b ^ 2 * (∏ p ∈ ellSet ε m, p) := by
  have hn : (DD ε m).natAbs ≠ 0 := Int.natAbs_ne_zero.mpr (D_ne_zero ε m)
  refine sq_mul_radical_of_odd_multiplicities hn ?_
  intro p hp
  have hpp : p.Prime := Nat.prime_of_mem_primeFactors hp
  have hmem : p ∈ ellSet ε m := hp
  have := hP.odd_valuations p hmem
  rwa [padicValInt, ← Nat.factorization_def _ hpp] at this

/-! ## Consequences of the `Params` hypotheses -/

variable {ε : ℤ} {m q : ℕ} [hqf : Fact (Nat.Prime q)]

theorem q_ne_two (hP : Params ε m q) : q ≠ 2 := by
  have := hP.q_mod_eight
  omega

theorem q_mod_four (hP : Params ε m q) : (4 : ℤ) ∣ ((q : ℤ) - 1) := by
  have h := hP.q_mod_eight
  have : q % 4 = 1 := by omega
  obtain ⟨s, hs⟩ : ∃ s, q = 4 * s + 1 := ⟨q / 4, by omega⟩
  exact ⟨(s : ℤ), by rw [hs]; push_cast; ring⟩

theorem q_not_dvd_D (hP : Params ε m q) : ¬ (q : ℤ) ∣ DD ε m := fun h =>
  hP.q_not_dvd_twoD (Dvd.dvd.mul_left h 2)

theorem q_not_dvd_r (hP : Params ε m q) : ¬ (q : ℤ) ∣ rr ε m := by
  intro h
  have hqp : q.Prime := hqf.out
  have h2 : (q : ℤ) ∣ 2 ^ m := by
    rcases hP.eps_unit with he | he
    · simpa [rr, he] using h
    · have hneg : (q : ℤ) ∣ -(2 ^ m) := by simpa [rr, he] using h
      exact dvd_neg.mp hneg
  have h2' : (q : ℕ) ∣ 2 ^ m := by exact_mod_cast h2
  exact q_ne_two hP ((Nat.prime_dvd_prime_iff_eq hqp Nat.prime_two).mp (hqp.dvd_of_dvd_pow h2'))

theorem ell_prime {ℓ : ℕ} (h : ℓ ∈ ellSet ε m) : ℓ.Prime := Nat.prime_of_mem_primeFactors h

theorem ell_dvd_D {ℓ : ℕ} (h : ℓ ∈ ellSet ε m) : (ℓ : ℤ) ∣ DD ε m := by
  have : ℓ ∣ (DD ε m).natAbs := Nat.dvd_of_mem_primeFactors h
  exact Int.dvd_natAbs.mp (Int.natCast_dvd_natCast.mpr this)

theorem ell_ne_q (hP : Params ε m q) {ℓ : ℕ} (h : ℓ ∈ ellSet ε m) : ℓ ≠ q := by
  rintro rfl
  exact q_not_dvd_D hP (ell_dvd_D h)

theorem ell_ne_two {ℓ : ℕ} (h : ℓ ∈ ellSet ε m) : ℓ ≠ 2 := by
  rintro rfl
  exact D_not_two_dvd ε m (ell_dvd_D h)

/-- The squarefree kernel of `D`, together with the oddness of its square factor. -/
theorem D_kernel_odd {ε : ℤ} {m q : ℕ} [Fact (Nat.Prime q)] (hP : Params ε m q) :
    ∃ b : ℕ, b ≠ 0 ∧ ¬ (2 : ℤ) ∣ (b : ℤ) ∧
      (DD ε m).natAbs = b ^ 2 * (∏ p ∈ ellSet ε m, p) := by
  obtain ⟨b, hb0, hbeq⟩ := D_kernel hP
  refine ⟨b, hb0, ?_, hbeq⟩
  rintro ⟨u, hu⟩
  refine D_not_two_dvd ε m (Int.dvd_natAbs.mp ?_)
  rw [hbeq]
  push_cast
  exact ⟨2 * u ^ 2 * (∏ p ∈ ellSet ε m, (p : ℤ)), by rw [hu]; ring⟩

/-- When `D < 0` has a single prime divisor, that prime is `3 mod 4`. -/
theorem ell_mod_four_three_of_D_neg {ε : ℤ} {m q : ℕ} [Fact (Nat.Prime q)] (hP : Params ε m q)
    (hDneg : DD ε m < 0) {ell : ℕ} (hEll : ellSet ε m = {ell}) : ell % 4 = 3 := by
  obtain ⟨b, hb0, hbodd, hbeq⟩ := D_kernel_odd hP
  rw [hEll, Finset.prod_singleton] at hbeq
  have hDfac : DD ε m = -(ell : ℤ) * (b : ℤ) ^ 2 := by
    rcases Int.natAbs_eq (DD ε m) with h | h
    · exfalso; have : (0 : ℤ) ≤ DD ε m := h ▸ Int.natCast_nonneg _; omega
    · rw [h, hbeq]; push_cast; ring
  obtain ⟨c, hc⟩ : ∃ c : ℤ, (b : ℤ) = 2 * c + 1 := by
    rcases Int.even_or_odd ((b : ℤ)) with ⟨u, hu⟩ | ⟨u, hu⟩
    · exact absurd ⟨u, by omega⟩ hbodd
    · exact ⟨u, hu⟩
  have hD4 : (4 : ℤ) ∣ (DD ε m - 1) :=
    dvd_trans ⟨8, by norm_num⟩ (D_sub_one_dvd ε m hP.m_ge_three)
  have hexp : DD ε m = -(ell : ℤ) - 4 * ((ell : ℤ) * (c ^ 2 + c)) := by rw [hDfac, hc]; ring
  obtain ⟨k, hk⟩ := hD4
  rw [hexp] at hk
  have hdd : (4 : ℤ) ∣ ((ell : ℤ) + 1) := ⟨-(k + (ell : ℤ) * (c ^ 2 + c)), by linarith⟩
  omega

/-- On the `H₄₁` stratum there is a prime divisor of `D` congruent to `3 mod 4`. -/
theorem exists_ell_mod_four_three {ε : ℤ} {m q : ℕ} [Fact (Nat.Prime q)] (hP : Params ε m q)
    (hH : (DD ε m < 0 ∧ sCount ε m = 1) ∨
      (0 < DD ε m ∧ sCount ε m = 2 ∧ ∀ ℓ ∈ ellSet ε m, ℓ % 4 = 3)) :
    ∃ ell ∈ ellSet ε m, ell % 4 = 3 := by
  rcases hH with ⟨hDneg, hs1⟩ | ⟨-, hs2, hell34⟩
  · obtain ⟨ell, hEll⟩ := Finset.card_eq_one.mp hs1
    exact ⟨ell, by rw [hEll]; simp, ell_mod_four_three_of_D_neg hP hDneg hEll⟩
  · obtain ⟨l1, l2, h12, hEll⟩ := Finset.card_eq_two.mp hs2
    have hm : l1 ∈ ellSet ε m := by rw [hEll]; simp
    exact ⟨l1, hm, hell34 l1 hm⟩

/-- The exact power of `ell` dividing `D`, with odd exponent. -/
theorem D_ell_factor {ε : ℤ} {m q : ℕ} [Fact (Nat.Prime q)] (hP : Params ε m q) {ell : ℕ}
    (hmem : ell ∈ ellSet ε m) :
    ∃ (k : ℕ) (w : ℤ), Odd k ∧ ¬ (ell : ℤ) ∣ w ∧ DD ε m = (ell : ℤ) ^ k * w := by
  have hp : ell.Prime := ell_prime hmem
  have hn : (DD ε m).natAbs ≠ 0 := Int.natAbs_ne_zero.mpr (D_ne_zero ε m)
  have hodd : Odd ((DD ε m).natAbs.factorization ell) := by
    have h := hP.odd_valuations ell hmem
    rwa [padicValInt, ← Nat.factorization_def _ hp] at h
  have hsplit :
      ell ^ ((DD ε m).natAbs.factorization ell) *
        ((DD ε m).natAbs / ell ^ ((DD ε m).natAbs.factorization ell)) = (DD ε m).natAbs :=
    Nat.ordProj_mul_ordCompl_eq_self _ ell
  have hnd : ¬ ell ∣ ((DD ε m).natAbs / ell ^ ((DD ε m).natAbs.factorization ell)) :=
    Nat.not_dvd_ordCompl hp hn
  have hcast : ((DD ε m).natAbs : ℤ)
      = (ell : ℤ) ^ ((DD ε m).natAbs.factorization ell)
        * (((DD ε m).natAbs / ell ^ ((DD ε m).natAbs.factorization ell) : ℕ) : ℤ) := by
    exact_mod_cast congrArg (fun n : ℕ => (n : ℤ)) hsplit.symm
  rcases Int.natAbs_eq (DD ε m) with h | h
  · refine ⟨_, (((DD ε m).natAbs / ell ^ ((DD ε m).natAbs.factorization ell) : ℕ) : ℤ), hodd,
      fun hc => hnd (by exact_mod_cast hc), ?_⟩
    exact h.trans hcast
  · refine ⟨_, -(((DD ε m).natAbs / ell ^ ((DD ε m).natAbs.factorization ell) : ℕ) : ℤ), hodd,
      fun hc => hnd (by exact_mod_cast (dvd_neg.mp hc)), ?_⟩
    exact h.trans (by rw [hcast]; ring)

end SDyadic
