import PrimarySupport.Defs

/-!
# A2 — helper lemmas: the extended valuation `vInf` and the depth ideal `JOf`

Supporting material for the packaged targets J1–J4 and the countermodel CM2.  Everything here is
elementary number theory over `ℤ`.
-/

namespace PrimarySupport

lemma vInf_zero (p : ℕ) : vInf p 0 = ⊤ := by simp [vInf]

lemma vInf_eq_top_iff (p : ℕ) (a : ℤ) : vInf p a = ⊤ ↔ a = 0 := by
  unfold vInf
  split <;> simp_all

/-- The basic translation: a finite depth bound is a prime-power divisibility. -/
lemma natCast_le_vInf_iff {p : ℕ} (hp : p.Prime) (n : ℕ) (a : ℤ) :
    ((n : ℕ∞) ≤ vInf p a) ↔ (p : ℤ) ^ n ∣ a := by
  haveI : Fact p.Prime := ⟨hp⟩
  unfold vInf
  by_cases ha : a = 0
  · simp [ha]
  · simp [ha, padicValInt_dvd_iff, Nat.cast_le]

/-- Depth bound at a prime where the depth is infinite. -/
lemma top_le_vInf_iff (p : ℕ) (a : ℤ) : (⊤ : ℕ∞) ≤ vInf p a ↔ a = 0 := by
  rw [top_le_iff, vInf_eq_top_iff]

/-- Membership in `JOf` at a single prime of finite depth. -/
lemma le_vInf_iff_of_ne_top {p : ℕ} (hp : p.Prime) {c : ℕ∞} (hc : c ≠ ⊤) (a : ℤ) :
    c ≤ vInf p a ↔ (p : ℤ) ^ c.toNat ∣ a := by
  rw [← natCast_le_vInf_iff hp c.toNat a, ENat.coe_toNat hc]

lemma mem_JOf_iff {P : Set ℕ} {h : ℕ → ℕ∞} {a : ℤ} : a ∈ JOf P h ↔ ∀ p ∈ P, h p ≤ vInf p a :=
  Iff.rfl

lemma zero_mem_JOf (P : Set ℕ) (h : ℕ → ℕ∞) : (0 : ℤ) ∈ JOf P h := by
  intro p _
  rw [vInf_zero]
  exact le_top

lemma add_mem_JOf {P : Set ℕ} {h : ℕ → ℕ∞} (hP : ∀ p ∈ P, p.Prime) {a b : ℤ}
    (ha : a ∈ JOf P h) (hb : b ∈ JOf P h) : a + b ∈ JOf P h := by
  intro p hpP
  rcases eq_or_ne (h p) ⊤ with hpt | hpt
  · have ha' := ha p hpP
    have hb' := hb p hpP
    rw [hpt, top_le_vInf_iff] at ha' hb'
    rw [hpt, top_le_vInf_iff, ha', hb', add_zero]
  · rw [le_vInf_iff_of_ne_top (hP p hpP) hpt]
    exact dvd_add ((le_vInf_iff_of_ne_top (hP p hpP) hpt _).1 (ha p hpP))
      ((le_vInf_iff_of_ne_top (hP p hpP) hpt _).1 (hb p hpP))

lemma mul_mem_JOf {P : Set ℕ} {h : ℕ → ℕ∞} (hP : ∀ p ∈ P, p.Prime) (c : ℤ) {a : ℤ}
    (ha : a ∈ JOf P h) : c * a ∈ JOf P h := by
  intro p hpP
  rcases eq_or_ne (h p) ⊤ with hpt | hpt
  · have ha' := ha p hpP
    rw [hpt, top_le_vInf_iff] at ha'
    rw [hpt, top_le_vInf_iff, ha', mul_zero]
  · rw [le_vInf_iff_of_ne_top (hP p hpP) hpt]
    exact Dvd.dvd.mul_left ((le_vInf_iff_of_ne_top (hP p hpP) hpt _).1 (ha p hpP)) c

/-- A prime of positive depth divides every nonzero element of `JOf`. -/
lemma dvd_of_mem_posSupport {P : Set ℕ} {h : ℕ → ℕ∞} (hP : ∀ p ∈ P, p.Prime) {a : ℤ}
    (ha : a ∈ JOf P h) (ha0 : a ≠ 0) {p : ℕ} (hp : p ∈ posSupport P h) : (p : ℤ) ∣ a := by
  obtain ⟨hpP, hpne⟩ := hp
  have hpt : h p ≠ ⊤ := by
    intro hpt
    exact ha0 ((top_le_vInf_iff p a).1 (hpt ▸ ha p hpP))
  have hdvd : (p : ℤ) ^ (h p).toNat ∣ a := (le_vInf_iff_of_ne_top (hP p hpP) hpt a).1 (ha p hpP)
  have h1 : 1 ≤ (h p).toNat := by
    rcases Nat.eq_zero_or_pos (h p).toNat with h0 | h0
    · exact absurd (by rw [← ENat.coe_toNat hpt, h0]; rfl) hpne
    · exact h0
  have hpow : (p : ℤ) ^ 1 ∣ (p : ℤ) ^ (h p).toNat := pow_dvd_pow _ h1
  exact dvd_trans (by simpa using hpow) hdvd

/-- The set of primes dividing a nonzero integer is finite. -/
lemma finite_primes_dvd {a : ℤ} (ha : a ≠ 0) : {p : ℕ | (p : ℤ) ∣ a}.Finite := by
  have hsub : {p : ℕ | (p : ℤ) ∣ a} ⊆ ↑(Finset.range (a.natAbs + 1)) := by
    intro p hp
    simp only [Set.mem_setOf_eq] at hp
    have hpa : p ∣ a.natAbs := Int.natCast_dvd_natCast.mp (Int.dvd_natAbs.mpr hp)
    have : p ≤ a.natAbs := Nat.le_of_dvd (Int.natAbs_pos.mpr ha) hpa
    simp only [Finset.coe_range, Set.mem_Iio]
    omega
  exact Set.Finite.subset (Finset.range (a.natAbs + 1)).finite_toSet hsub

/-- The generator attached to a finite positive support. -/
noncomputable def depthProd {P : Set ℕ} {h : ℕ → ℕ∞} (hfin : (posSupport P h).Finite) : ℤ :=
  ∏ p ∈ hfin.toFinset, (p : ℤ) ^ (h p).toNat

lemma depthProd_ne_zero {P : Set ℕ} {h : ℕ → ℕ∞} (hP : ∀ p ∈ P, p.Prime)
    (hfin : (posSupport P h).Finite) : depthProd hfin ≠ 0 := by
  refine Finset.prod_ne_zero_iff.2 fun p hp => ?_
  have hpP : p ∈ P := (hfin.mem_toFinset.mp hp).1
  exact pow_ne_zero _ (by exact_mod_cast (hP p hpP).pos.ne')

lemma depthProd_mem_JOf {P : Set ℕ} {h : ℕ → ℕ∞} (hP : ∀ p ∈ P, p.Prime)
    (htop : ∀ p ∈ P, h p ≠ ⊤) (hfin : (posSupport P h).Finite) : depthProd hfin ∈ JOf P h := by
  intro p hpP
  rcases eq_or_ne (h p) 0 with h0 | h0
  · rw [h0]; exact zero_le _
  · rw [le_vInf_iff_of_ne_top (hP p hpP) (htop p hpP)]
    exact Finset.dvd_prod_of_mem _ (hfin.mem_toFinset.mpr ⟨hpP, h0⟩)

/-- Coprimality of powers of distinct primes, over `ℤ`. -/
lemma isCoprime_prime_pow {p q : ℕ} (hp : p.Prime) (hq : q.Prime) (hne : p ≠ q) (m n : ℕ) :
    IsCoprime ((p : ℤ) ^ m) ((q : ℤ) ^ n) := by
  have hco : IsCoprime (p : ℤ) (q : ℤ) := by
    rw [Int.isCoprime_iff_gcd_eq_one]
    simpa using (Nat.coprime_primes hp hq).mpr hne
  exact hco.pow

/-- J2. `JOf P h` contains a nonzero integer iff all depths are finite and the positive support is
finite. -/
lemma exists_ne_zero_mem_JOf_iff {P : Set ℕ} {h : ℕ → ℕ∞} (hP : ∀ p ∈ P, p.Prime) :
    (∃ a ∈ JOf P h, a ≠ 0) ↔ (∀ p ∈ P, h p ≠ ⊤) ∧ (posSupport P h).Finite := by
  constructor
  · rintro ⟨a, ha, ha0⟩
    have htop : ∀ p ∈ P, h p ≠ ⊤ := by
      intro p hpP hpt
      have := ha p hpP
      rw [hpt, top_le_vInf_iff] at this
      exact ha0 this
    exact ⟨htop, Set.Finite.subset (finite_primes_dvd ha0)
      fun p hp => dvd_of_mem_posSupport hP ha ha0 hp⟩
  · rintro ⟨htop, hfin⟩
    exact ⟨depthProd hfin, depthProd_mem_JOf hP htop hfin, depthProd_ne_zero hP hfin⟩

/-- J3. In the nonzero case `JOf P h` is the set of multiples of `∏ p ^ h p`. -/
lemma JOf_eq_multiples {P : Set ℕ} {h : ℕ → ℕ∞} (hP : ∀ p ∈ P, p.Prime) (htop : ∀ p ∈ P, h p ≠ ⊤)
    (hfin : (posSupport P h).Finite) :
    JOf P h = {a | (∏ p ∈ hfin.toFinset, (p : ℤ) ^ (h p).toNat) ∣ a} := by
  ext a
  simp only [Set.mem_setOf_eq]
  constructor
  · intro ha
    refine Finset.prod_dvd_of_coprime ?_ ?_
    · intro p hp q hq hne
      have hpP : p ∈ P := (hfin.mem_toFinset.mp hp).1
      have hqP : q ∈ P := (hfin.mem_toFinset.mp hq).1
      exact isCoprime_prime_pow (hP p hpP) (hP q hqP) hne _ _
    · intro p hp
      have hpP : p ∈ P := (hfin.mem_toFinset.mp hp).1
      exact (le_vInf_iff_of_ne_top (hP p hpP) (htop p hpP) a).1 (ha p hpP)
  · intro ha p hpP
    rcases eq_or_ne (h p) 0 with h0 | h0
    · rw [h0]; exact zero_le _
    · rw [le_vInf_iff_of_ne_top (hP p hpP) (htop p hpP)]
      exact dvd_trans (Finset.dvd_prod_of_mem (fun q : ℕ => (q : ℤ) ^ (h q).toNat)
        (hfin.mem_toFinset.mpr ⟨hpP, h0⟩)) ha

/-- CM2 (second half). The constant depth function `2` cuts out the zero ideal. -/
lemma JOf_const_two : JOf {p : ℕ | p.Prime} (fun _ => (2 : ℕ∞)) = {0} := by
  ext a
  simp only [Set.mem_singleton_iff]
  constructor
  · intro ha
    by_contra ha0
    obtain ⟨p, hple, hp⟩ := Nat.exists_infinite_primes (a.natAbs + 1)
    have hmem : ((2 : ℕ) : ℕ∞) ≤ vInf p a := by
      have := ha p hp
      exact_mod_cast this
    have hsq : (p : ℤ) ^ 2 ∣ a := (natCast_le_vInf_iff hp 2 a).1 hmem
    have hpa : (p : ℤ) ∣ a := dvd_trans (dvd_pow_self _ two_ne_zero) hsq
    have hdvd : p ∣ a.natAbs := Int.natCast_dvd_natCast.mp (Int.dvd_natAbs.mpr hpa)
    have : p ≤ a.natAbs := Nat.le_of_dvd (Int.natAbs_pos.mpr ha0) hdvd
    omega
  · rintro rfl
    exact zero_mem_JOf _ _

/-- CM2 (first half). At every prime the class of `p ^ 2` in `ZMod (p ^ 3)` is nonzero and
divisible by `p`. -/
lemma zmod_p_sq_ne_zero {p : ℕ} (hp : p.Prime) :
    ((p : ZMod (p ^ 3)) ^ 2 ≠ 0 ∧ ∃ y : ZMod (p ^ 3), p • y = (p : ZMod (p ^ 3)) ^ 2) := by
  haveI : NeZero (p ^ 3) := ⟨pow_ne_zero _ hp.pos.ne'⟩
  constructor
  · intro hzero
    have hcast : (((p : ℤ) ^ 2 : ℤ) : ZMod (p ^ 3)) = 0 := by push_cast; exact hzero
    rw [ZMod.intCast_zmod_eq_zero_iff_dvd] at hcast
    have hdvd : p ^ 3 ∣ p ^ 2 := by exact_mod_cast hcast
    have hle : p ^ 3 ≤ p ^ 2 := Nat.le_of_dvd (Nat.pow_pos hp.pos) hdvd
    have h1 : 1 < p := hp.one_lt
    have : p ^ 2 < p ^ 3 := by
      have := Nat.pow_lt_pow_right h1 (show 2 < 3 by norm_num)
      exact this
    omega
  · exact ⟨(p : ZMod (p ^ 3)), by rw [nsmul_eq_mul, sq]⟩

end PrimarySupport
