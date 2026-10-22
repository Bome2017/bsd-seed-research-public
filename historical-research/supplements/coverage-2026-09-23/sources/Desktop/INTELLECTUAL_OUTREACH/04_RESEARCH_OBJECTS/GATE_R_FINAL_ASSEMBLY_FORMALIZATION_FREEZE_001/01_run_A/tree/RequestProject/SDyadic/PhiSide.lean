/-
Exhaustion on the `φ` side.

Combining
  * the parity obstruction (which confines `d` to the squarefree divisors of `D q`),
  * the dyadic condition `d ≡ 1 (mod 4)`, and
  * (when `D > 0`) positivity at the real place,
every everywhere-locally-soluble square class for the pair `(phiA, phiB)` is one of
`1`, `[D]`, `[q]`, `[D q]`.
-/
import RequestProject.SDyadic.Structure
import RequestProject.SDyadic.LocalTwo

namespace SDyadic

open Run013

/-! ## Two generic ingredients -/

/-- Solubility over `ℝ` fails when all three coefficients of the quartic are negative. -/
theorem not_cov_real_neg {a b d : ℝ} (ha : a < 0) (hb : 0 < b) (hd : d < 0) : ¬ Cov ℝ a b d := by
  rintro ⟨u, v, n, huv, hn⟩
  have hbd : b / d < 0 := div_neg_of_pos_of_neg hb hd
  have hu4 : (0 : ℝ) ≤ u ^ 4 := by positivity
  have hv4 : (0 : ℝ) ≤ v ^ 4 := by positivity
  have huv2 : (0 : ℝ) ≤ u ^ 2 * v ^ 2 := by positivity
  have h1 : d * u ^ 4 ≤ 0 := by nlinarith
  have h2 : a * u ^ 2 * v ^ 2 ≤ 0 := by nlinarith
  have h3 : b / d * v ^ 4 ≤ 0 := by nlinarith
  have hn2 : (0 : ℝ) ≤ n ^ 2 := sq_nonneg n
  have hz1 : d * u ^ 4 = 0 := by linarith
  have hz3 : b / d * v ^ 4 = 0 := by linarith
  have hu : u = 0 := by
    rcases mul_eq_zero.mp hz1 with h | h
    · exact absurd h hd.ne
    · exact pow_eq_zero_iff (n := 4) (by norm_num) |>.mp h
  have hv : v = 0 := by
    rcases mul_eq_zero.mp hz3 with h | h
    · exact absurd h hbd.ne
    · exact pow_eq_zero_iff (n := 4) (by norm_num) |>.mp h
  exact huv ⟨hu, hv⟩

/-- Every prime dividing a locally soluble squarefree `d` divides `b`. -/
theorem prime_dvd_b_of_local {a b e : ℤ} {p : ℕ} (hp : p.Prime) (hsf : Squarefree e)
    (hpe : (p : ℤ) ∣ e)
    (hcov : ∀ (P : ℕ) [Fact P.Prime], Cov ℚ_[P] ((a : ℤ) : ℚ_[P]) ((b : ℤ) : ℚ_[P])
      ((e : ℤ) : ℚ_[P])) :
    (p : ℤ) ∣ b := by
  by_contra hpb
  haveI : Fact p.Prime := ⟨hp⟩
  obtain ⟨d₀, hd₀eq, hd₀⟩ := exists_cofactor_of_squarefree hsf hp hpe
  have hc := hcov p
  rw [hd₀eq] at hc
  exact not_cov_padic_of_parity (a := a) hd₀ hpb hc

/-! ## Square-class bookkeeping -/

/-- Transport of square classes along the squarefree kernel. -/
theorem sqEq_kernel_gen {x y : ℤ} {b : ℕ} (hb : b ≠ 0) (h : y = x * (b : ℤ) ^ 2) :
    SqEq ℚ ((x : ℤ) : ℚ) ((y : ℤ) : ℚ) := by
  have hbQ : ((b : ℚ)) ≠ 0 := by exact_mod_cast hb
  refine ⟨((b : ℚ))⁻¹, inv_ne_zero hbQ, ?_⟩
  rw [h]
  push_cast
  field_simp

/-- A locally soluble squarefree `e` divides any `M` containing all primes of `b`. -/
theorem natAbs_dvd_of_local {a b e : ℤ} (hsf : Squarefree e) (he : e ≠ 0)
    {M : ℕ} (hM : M ≠ 0)
    (hrad : ∀ p : ℕ, p.Prime → (p : ℤ) ∣ b → p ∣ M)
    (hcov : ∀ (P : ℕ) [Fact P.Prime], Cov ℚ_[P] ((a : ℤ) : ℚ_[P]) ((b : ℤ) : ℚ_[P])
      ((e : ℤ) : ℚ_[P])) :
    e.natAbs ∣ M := by
  refine dvd_of_squarefree_of_primes (Int.natAbs_ne_zero.mpr he) hM
    (Int.squarefree_natAbs.mpr hsf) ?_
  intro p hp hpe
  exact hrad p hp (prime_dvd_b_of_local hp hsf
    (Int.dvd_natAbs.mp (Int.natCast_dvd_natCast.mpr hpe)) hcov)

theorem bad_class_absurd {e X : ℤ} (h : e = 4 * X + 3) (h4 : (4 : ℤ) ∣ e - 1) : False := by omega

/-! ## The `φ` exhaustion -/

/-- **Exhaustion on the `φ` side.**  On `H₄₁`, every everywhere-locally-soluble squarefree `e`
lies in one of the four square classes `1`, `[D]`, `[q]`, `[D q]`. -/
theorem phi_exhaustion {ε : ℤ} {m q : ℕ} [hqf : Fact (Nat.Prime q)] (hP : Params ε m q)
    (hH : (DD ε m < 0 ∧ sCount ε m = 1) ∨
      (0 < DD ε m ∧ sCount ε m = 2 ∧ ∀ ℓ ∈ ellSet ε m, ℓ % 4 = 3))
    {e : ℤ} (he : e ≠ 0) (hsf : Squarefree e)
    (hL : LocalKummerAll (phiA ε m q) (phiB ε m q) ((e : ℤ) : ℚ)) :
    SqEq ℚ ((e : ℤ) : ℚ) 1 ∨ SqEq ℚ ((e : ℤ) : ℚ) ((DD ε m : ℤ) : ℚ) ∨
      SqEq ℚ ((e : ℤ) : ℚ) (((q : ℤ)) : ℚ) ∨
      SqEq ℚ ((e : ℤ) : ℚ) ((DD ε m * (q : ℤ) : ℤ) : ℚ) := by
  classical
  have hqp : q.Prime := hqf.out
  have hqpos : (0 : ℤ) < (q : ℤ) := by exact_mod_cast hqp.pos
  have hD0 : DD ε m ≠ 0 := D_ne_zero ε m
  have hbI0 : DD ε m * (q : ℤ) ^ 2 ≠ 0 := mul_ne_zero hD0 (by positivity)
  have hAeq : phiA ε m q = ((-((q : ℤ) + DD ε m * (q : ℤ)) : ℤ) : ℚ) :=
    congrArg (fun z : ℤ => (z : ℚ)) (phiA_eq ε m q)
  have hBeq : phiB ε m q = ((DD ε m * (q : ℤ) ^ 2 : ℤ) : ℚ) := rfl
  have hbne : phiB ε m q ≠ 0 := by rw [hBeq]; exact_mod_cast hbI0
  have heQ : ((e : ℤ) : ℚ) ≠ 0 := by exact_mod_cast he
  rw [localKummerAll_iff_cov hbne heQ, hAeq, hBeq] at hL
  obtain ⟨hreal, hpad⟩ := hL
  simp only [Rat.cast_intCast] at hreal
  have hcov : ∀ (P : ℕ) [Fact P.Prime],
      Cov ℚ_[P] ((-((q : ℤ) + DD ε m * (q : ℤ)) : ℤ) : ℚ_[P])
        ((DD ε m * (q : ℤ) ^ 2 : ℤ) : ℚ_[P]) ((e : ℤ) : ℚ_[P]) := by
    intro P _
    simpa only [Rat.cast_intCast] using hpad P
  -- confinement to the divisors of the radical of `D q`
  have hprodpos : 0 < (∏ p ∈ ellSet ε m, p) * q :=
    Nat.mul_pos (Finset.prod_pos fun p hp => (ell_prime hp).pos) hqp.pos
  have hMdvd : e.natAbs ∣ (∏ p ∈ ellSet ε m, p) * q := by
    refine natAbs_dvd_of_local hsf he hprodpos.ne' ?_ hcov
    intro p hp hpb
    have hpZ : Prime ((p : ℤ)) := Nat.prime_iff_prime_int.mp hp
    rcases hpZ.dvd_mul.mp hpb with hpD | hpq
    · refine Dvd.dvd.mul_right (Finset.dvd_prod_of_mem _ ?_) q
      refine Nat.mem_primeFactors.mpr ⟨hp, ?_, Int.natAbs_ne_zero.mpr hD0⟩
      exact Int.natAbs_dvd_natAbs.mpr (by simpa using hpD)
    · have hpq' : (p : ℤ) ∣ (q : ℤ) := hpZ.dvd_of_dvd_pow hpq
      have : p ∣ q := by exact_mod_cast hpq'
      rw [(Nat.prime_dvd_prime_iff_eq hp hqp).mp this]
      exact Dvd.dvd.mul_left dvd_rfl _
  -- `e` is odd
  have hqodd : ¬ (2 : ℤ) ∣ (q : ℤ) := by
    have h8 := hP.q_mod_eight
    intro hc
    have : (2 : ℕ) ∣ q := by exact_mod_cast hc
    omega
  have h2e : ¬ (2 : ℤ) ∣ e := by
    intro h2
    have hb2 := prime_dvd_b_of_local Nat.prime_two hsf (by exact_mod_cast h2) hcov
    have hpZ2 : Prime ((2 : ℤ)) := Int.prime_two
    rcases hpZ2.dvd_mul.mp hb2 with h | h
    · exact D_not_two_dvd ε m h
    · exact hqodd (hpZ2.dvd_of_dvd_pow h)
  -- the dyadic condition
  have h4 : (4 : ℤ) ∣ (e - 1) :=
    four_dvd_sub_one_of_cov_two h2e (q_mod_four hP) (D_sub_one_dvd ε m hP.m_ge_three) (hcov 2)
  obtain ⟨t, ht4⟩ : ∃ t : ℕ, q = 4 * t + 1 := ⟨q / 4, by have := hP.q_mod_eight; omega⟩
  have htZ : (q : ℤ) = 4 * (t : ℤ) + 1 := by rw [ht4]; push_cast; ring
  obtain ⟨b, hb0, hbeq⟩ := D_kernel hP
  have hbodd : ¬ (2 : ℤ) ∣ (b : ℤ) := by
    rintro ⟨u, hu⟩
    refine D_not_two_dvd ε m ?_
    have hD : DD ε m = (if 0 < DD ε m then 1 else -1) * ((b : ℤ) ^ 2 * (∏ p ∈ ellSet ε m, p)) := by
      rcases Int.natAbs_eq (DD ε m) with h | h
      · have hpos : 0 < DD ε m := by
          rcases lt_trichotomy (DD ε m) 0 with hlt | h0 | hgt
          · exfalso; have : (0 : ℤ) ≤ DD ε m := h ▸ Int.natCast_nonneg _; omega
          · exact absurd h0 hD0
          · exact hgt
        rw [if_pos hpos, h, hbeq]; push_cast; ring
      · have hneg : DD ε m < 0 := by
          rcases lt_trichotomy (DD ε m) 0 with hlt | h0 | hgt
          · exact hlt
          · exact absurd h0 hD0
          · exfalso; have : DD ε m ≤ 0 := by rw [h]; simp
            omega
        rw [if_neg (by omega), h, hbeq]; push_cast; ring
    rw [hD, hu]
    exact ⟨(if 0 < DD ε m then 1 else -1) * (2 * u ^ 2 * (∏ p ∈ ellSet ε m, (p : ℤ))), by
      push_cast; ring⟩
  obtain ⟨c, hc⟩ : ∃ c : ℤ, (b : ℤ) = 2 * c + 1 := by
    rcases Int.even_or_odd ((b : ℤ)) with ⟨u, hu⟩ | ⟨u, hu⟩
    · exact absurd ⟨u, by omega⟩ hbodd
    · exact ⟨u, hu⟩
  have hD4 : (4 : ℤ) ∣ (DD ε m - 1) :=
    dvd_trans ⟨8, by norm_num⟩ (D_sub_one_dvd ε m hP.m_ge_three)
  rcases hH with ⟨hDneg, hs1⟩ | ⟨hDpos, hs2, hell34⟩
  · -- `D < 0`, one prime `ℓ`
    obtain ⟨ell, hEll⟩ := Finset.card_eq_one.mp hs1
    have hellmem : ell ∈ ellSet ε m := by rw [hEll]; exact Finset.mem_singleton_self ell
    have hellp : ell.Prime := ell_prime hellmem
    rw [hEll, Finset.prod_singleton] at hbeq hMdvd
    have hDfac : DD ε m = -(ell : ℤ) * (b : ℤ) ^ 2 := by
      rcases Int.natAbs_eq (DD ε m) with h | h
      · exfalso; have : (0 : ℤ) ≤ DD ε m := h ▸ Int.natCast_nonneg _; omega
      · rw [h, hbeq]; push_cast; ring
    have hell4 : ell % 4 = 3 := by
      have hexp : DD ε m = -(ell : ℤ) - 4 * ((ell : ℤ) * (c ^ 2 + c)) := by
        rw [hDfac, hc]; ring
      obtain ⟨k, hk⟩ := hD4
      rw [hexp] at hk
      have hdd : (4 : ℤ) ∣ ((ell : ℤ) + 1) := ⟨-(k + (ell : ℤ) * (c ^ 2 + c)), by linarith⟩
      omega
    obtain ⟨s, hs4⟩ : ∃ s : ℕ, ell = 4 * s + 3 := ⟨ell / 4, by omega⟩
    have hsZ : (ell : ℤ) = 4 * (s : ℤ) + 3 := by rw [hs4]; push_cast; ring
    rcases nat_dvd_two_primes hellp hqp hMdvd with hN | hN | hN | hN <;>
      rcases Int.natAbs_eq e with hE | hE <;> rw [hN] at hE <;> push_cast at hE
    · exact Or.inl ⟨1, one_ne_zero, by rw [hE]; norm_num⟩
    · exfalso; rw [hE] at h4; omega
    · exfalso; rw [hE, hsZ] at h4; omega
    · exact Or.inr (Or.inl (by rw [hE]; exact sqEq_kernel_gen hb0 hDfac))
    · exact Or.inr (Or.inr (Or.inl (by rw [hE]; exact SqEq.rfl' _)))
    · exfalso; rw [hE, htZ] at h4; omega
    · exfalso
      refine bad_class_absurd (X := 4 * (s : ℤ) * (t : ℤ) + (s : ℤ) + 3 * (t : ℤ)) ?_ h4
      rw [hE, hsZ, htZ]; ring
    · refine Or.inr (Or.inr (Or.inr ?_))
      rw [hE]
      exact sqEq_kernel_gen (x := -((ell : ℤ) * (q : ℤ))) (y := DD ε m * (q : ℤ)) hb0
        (by rw [hDfac]; ring)
  · -- `D > 0`, two primes `ℓ₁ ℓ₂ ≡ 3 (mod 4)`
    obtain ⟨l1, l2, h12, hEll⟩ := Finset.card_eq_two.mp hs2
    have h1mem : l1 ∈ ellSet ε m := by rw [hEll]; simp
    have h2mem : l2 ∈ ellSet ε m := by rw [hEll]; simp
    have h1p : l1.Prime := ell_prime h1mem
    have h2p : l2.Prime := ell_prime h2mem
    rw [hEll, Finset.prod_pair h12] at hbeq hMdvd
    have hDfac : DD ε m = ((l1 : ℤ) * (l2 : ℤ)) * (b : ℤ) ^ 2 := by
      rcases Int.natAbs_eq (DD ε m) with h | h
      · rw [h, hbeq]; push_cast; ring
      · exfalso
        have : DD ε m ≤ 0 := by rw [h]; simp
        omega
    -- positivity at the real place
    have hpos : 0 < e := by
      rcases lt_trichotomy e 0 with hlt | h0 | hgt
      · exfalso
        refine not_cov_real_neg (a := ((-((q : ℤ) + DD ε m * (q : ℤ)) : ℤ) : ℝ))
          (b := ((DD ε m * (q : ℤ) ^ 2 : ℤ) : ℝ)) (d := ((e : ℤ) : ℝ)) ?_ ?_ ?_ hreal
        · have : (0 : ℤ) < (q : ℤ) + DD ε m * (q : ℤ) := by nlinarith
          have h' : (-((q : ℤ) + DD ε m * (q : ℤ)) : ℤ) < 0 := by omega
          exact_mod_cast h'
        · have h' : (0 : ℤ) < DD ε m * (q : ℤ) ^ 2 := by positivity
          exact_mod_cast h'
        · exact_mod_cast hlt
      · exact absurd h0 he
      · exact hgt
    obtain ⟨s1, hs1'⟩ : ∃ s : ℕ, l1 = 4 * s + 3 := ⟨l1 / 4, by have := hell34 l1 h1mem; omega⟩
    obtain ⟨s2, hs2'⟩ : ∃ s : ℕ, l2 = 4 * s + 3 := ⟨l2 / 4, by have := hell34 l2 h2mem; omega⟩
    have h1Z : (l1 : ℤ) = 4 * (s1 : ℤ) + 3 := by rw [hs1']; push_cast; ring
    have h2Z : (l2 : ℤ) = 4 * (s2 : ℤ) + 3 := by rw [hs2']; push_cast; ring
    have heabs : e = (e.natAbs : ℤ) := by
      rcases Int.natAbs_eq e with h | h
      · exact h
      · exfalso
        have : (0 : ℤ) ≤ (e.natAbs : ℤ) := Int.natCast_nonneg _
        omega
    rcases nat_dvd_three_primes h1p h2p hqp hMdvd with hN | hN | hN | hN | hN | hN | hN | hN <;>
      rw [hN] at heabs <;> push_cast at heabs
    · exact Or.inl ⟨1, one_ne_zero, by rw [heabs]; norm_num⟩
    · exfalso; rw [heabs, h1Z] at h4; omega
    · exfalso; rw [heabs, h2Z] at h4; omega
    · exact Or.inr (Or.inl (by rw [heabs]; exact sqEq_kernel_gen hb0 hDfac))
    · exact Or.inr (Or.inr (Or.inl (by rw [heabs]; exact SqEq.rfl' _)))
    · exfalso
      refine bad_class_absurd (X := 4 * (s1 : ℤ) * (t : ℤ) + (s1 : ℤ) + 3 * (t : ℤ)) ?_ h4
      rw [heabs, h1Z, htZ]; ring
    · exfalso
      refine bad_class_absurd (X := 4 * (s2 : ℤ) * (t : ℤ) + (s2 : ℤ) + 3 * (t : ℤ)) ?_ h4
      rw [heabs, h2Z, htZ]; ring
    · refine Or.inr (Or.inr (Or.inr ?_))
      rw [heabs]
      exact sqEq_kernel_gen (x := (l1 : ℤ) * (l2 : ℤ) * (q : ℤ)) (y := DD ε m * (q : ℤ)) hb0
        (by rw [hDfac]; ring)

end SDyadic
