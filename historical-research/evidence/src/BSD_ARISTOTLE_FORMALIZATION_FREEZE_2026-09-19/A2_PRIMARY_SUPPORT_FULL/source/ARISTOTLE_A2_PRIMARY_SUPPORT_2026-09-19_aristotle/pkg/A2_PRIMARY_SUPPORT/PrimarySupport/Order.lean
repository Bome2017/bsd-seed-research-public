import PrimarySupport.Primary

/-!
# A2 — helper lemmas: the order of a finite abelian group and its primary parts (H0, H2, CM4)

The square-order input of H2 is a hypothesis of the statement; nothing about elliptic curves or the
Cassels–Tate pairing is used or proved here.
-/

namespace PrimarySupport

variable {G : Type*} [AddCommGroup G]

/-- The order of the `p`-primary part of a finite abelian group is a power of `p`. -/
lemma card_primaryPart_eq_pow [Finite G] {p : ℕ} (hp : p.Prime) :
    ∃ a : ℕ, Nat.card (primaryPart G p) = p ^ a := by
  have hcard0 : Nat.card (primaryPart G p) ≠ 0 := Nat.card_pos.ne'
  refine ⟨(Nat.card (primaryPart G p)).primeFactorsList.length,
    Nat.eq_prime_pow_of_unique_prime_dvd hcard0 ?_⟩
  intro q hq hqdvd
  haveI : Fact q.Prime := ⟨hq⟩
  haveI : Fintype (primaryPart G p) := Fintype.ofFinite _
  have hcard : q ∣ Fintype.card (primaryPart G p) := by
    rwa [Nat.card_eq_fintype_card] at hqdvd
  obtain ⟨x, hx⟩ := exists_prime_addOrderOf_dvd_card q hcard
  obtain ⟨k, hk⟩ := x.2
  have hkx : (p ^ k) • x = 0 := Subtype.ext (by simpa using hk)
  have hdvd : addOrderOf x ∣ p ^ k := addOrderOf_dvd_of_nsmul_eq_zero hkx
  rw [hx] at hdvd
  exact ((Nat.prime_dvd_prime_iff_eq hq hp).mp (hq.dvd_of_dvd_pow hdvd))

/-- H0. The order of a finite abelian group is the product of the orders of its primary parts. -/
theorem card_eq_prod_primary_aux [Finite G] :
    Nat.card G = ∏ p ∈ (Nat.card G).primeFactors, Nat.card (primaryPart G p) := by
  have hN : Nat.card G ≠ 0 := Nat.card_pos.ne'
  -- the product divides the order
  have hdvd : (∏ p ∈ (Nat.card G).primeFactors, Nat.card (primaryPart G p)) ∣ Nat.card G := by
    have h1 : ∀ p ∈ (Nat.card G).primeFactors,
        Nat.card (primaryPart G p) ∣ p ^ (Nat.card G).factorization p := by
      intro p hp
      have hprime := Nat.prime_of_mem_primeFactors hp
      obtain ⟨a, ha⟩ := card_primaryPart_eq_pow (G := G) hprime
      rw [ha]
      refine pow_dvd_pow p ?_
      rw [← hprime.pow_dvd_iff_le_factorization hN, ← ha]
      exact AddSubgroup.card_addSubgroup_dvd_card _
    have h2 : (∏ p ∈ (Nat.card G).primeFactors, p ^ (Nat.card G).factorization p) = Nat.card G := by
      conv_rhs => rw [← Nat.factorization_prod_pow_eq_self hN]
      rw [Finsupp.prod, Nat.support_factorization]
    have h3 := Finset.prod_dvd_prod_of_dvd _ _ h1
    rwa [h2] at h3
  -- the order is at most the product
  have hle : Nat.card G ≤ ∏ p ∈ (Nat.card G).primeFactors, Nat.card (primaryPart G p) := by
    have hbot : ∀ p, p.Prime → p ∉ (Nat.card G).primeFactors → primaryPart G p = ⊥ := by
      intro p hp hpT
      by_contra hne
      exact hpT (Nat.mem_primeFactors.mpr
        ⟨hp, prime_dvd_card_of_primaryPart_ne_bot hp hne, hN⟩)
    haveI : Finite (∀ p : {p // p ∈ (Nat.card G).primeFactors}, primaryPart G (p : ℕ)) := Pi.finite
    have hsurj := sumMap_surjective (G := G) (Nat.card G).primeFactors is_add_torsion_of_finite hbot
    have hcard := Nat.card_le_card_of_surjective _ hsurj
    rw [Nat.card_pi] at hcard
    calc Nat.card G ≤ ∏ p : {p // p ∈ (Nat.card G).primeFactors}, Nat.card (primaryPart G (p : ℕ)) :=
          hcard
      _ = ∏ p ∈ (Nat.card G).primeFactors, Nat.card (primaryPart G p) :=
          Finset.prod_coe_sort _ (fun p : ℕ => Nat.card (primaryPart G p))
  exact le_antisymm hle (Nat.le_of_dvd Nat.card_pos hdvd)

/-- Cauchy: a prime dividing the order has a nontrivial primary part. -/
lemma primaryPart_ne_bot_of_dvd_card [Finite G] {p : ℕ} (hp : p.Prime) (hdvd : p ∣ Nat.card G) :
    primaryPart G p ≠ ⊥ := by
  haveI : Fact p.Prime := ⟨hp⟩
  haveI : Fintype G := Fintype.ofFinite G
  obtain ⟨x, hx⟩ := exists_prime_addOrderOf_dvd_card (G := G) p
    (by rwa [← Nat.card_eq_fintype_card])
  have hx0 : x ≠ 0 := by
    intro h
    rw [h, addOrderOf_zero] at hx
    exact hp.one_lt.ne hx
  have hmem : x ∈ primaryPart G p := ⟨1, by rw [pow_one, ← hx]; exact addOrderOf_nsmul_eq_zero x⟩
  intro hbot
  rw [hbot] at hmem
  exact hx0 (by simpa using hmem)

/-- If the `p`-primary part is trivial then `p` does not divide the order. -/
lemma not_dvd_card_of_card_primaryPart_eq_one [Finite G] {p : ℕ} (hp : p.Prime)
    (h : Nat.card (primaryPart G p) = 1) : ¬ p ∣ Nat.card G := by
  intro hdvd
  exact primaryPart_ne_bot_of_dvd_card hp hdvd (AddSubgroup.eq_bot_of_card_eq _ h)

/-- A prime dividing a product of primary-part orders is one of the indexing primes. -/
lemma eq_of_dvd_card_primaryPart [Finite G] {p q : ℕ} (hp : p.Prime) (hq : q.Prime)
    (hdvd : q ∣ Nat.card (primaryPart G p)) : q = p := by
  obtain ⟨a, ha⟩ := card_primaryPart_eq_pow (G := G) hp
  rw [ha] at hdvd
  exact (Nat.prime_dvd_prime_iff_eq hq hp).mp (hq.dvd_of_dvd_pow hdvd)

/-- H2. Under the stated hypotheses the order is `9 t ²` with `gcd (t, 30) = 1`. -/
theorem order_nine_t_sq_aux [Finite G] (h2 : Nat.card (primaryPart G 2) = 1)
    (h3 : Nat.card (primaryPart G 3) = 9) (h5 : Nat.card (primaryPart G 5) = 1)
    (hsq : ∀ p, p.Prime → p ≠ 2 → IsSquare (Nat.card (primaryPart G p))) :
    ∃ t : ℕ, Nat.card G = 9 * t ^ 2 ∧ Nat.Coprime t 30 := by
  classical
  have hN : Nat.card G ≠ 0 := Nat.card_pos.ne'
  have hprod := card_eq_prod_primary_aux (G := G)
  have h2not : ¬ (2 : ℕ) ∣ Nat.card G := not_dvd_card_of_card_primaryPart_eq_one Nat.prime_two h2
  have h5not : ¬ (5 : ℕ) ∣ Nat.card G :=
    not_dvd_card_of_card_primaryPart_eq_one (by norm_num) h5
  have h3mem : (3 : ℕ) ∈ (Nat.card G).primeFactors := by
    have h9 : (9 : ℕ) ∣ Nat.card G := by
      rw [← h3]; exact AddSubgroup.card_addSubgroup_dvd_card _
    exact Nat.mem_primeFactors.mpr ⟨by norm_num, dvd_trans (by norm_num) h9, hN⟩
  set S := (Nat.card G).primeFactors.erase 3 with hS
  have hsplit : Nat.card G = 9 * ∏ p ∈ S, Nat.card (primaryPart G p) := by
    rw [hprod, ← Finset.prod_erase_mul _ _ h3mem, h3, mul_comm]
  -- the remaining factor is a square
  have hsquare : IsSquare (∏ p ∈ S, Nat.card (primaryPart G p)) := by
    refine Finset.prod_induction _ IsSquare (fun a b ha hb => ha.mul hb) ⟨1, by ring⟩ ?_
    intro p hp
    have hpf : p ∈ (Nat.card G).primeFactors := Finset.mem_of_mem_erase hp
    have hprime : p.Prime := Nat.prime_of_mem_primeFactors hpf
    have hp2 : p ≠ 2 := by
      intro h
      exact h2not (h ▸ Nat.dvd_of_mem_primeFactors hpf)
    exact hsq p hprime hp2
  obtain ⟨t, ht⟩ := hsquare
  refine ⟨t, by rw [hsplit, ht, sq], ?_⟩
  -- coprimality of `t` with 2, 3 and 5
  have hdvd_t : ∀ q : ℕ, q.Prime → q ∣ t → ∃ p ∈ S, q = p := by
    intro q hq hqt
    have hqM : q ∣ ∏ p ∈ S, Nat.card (primaryPart G p) := by
      rw [ht]; exact hqt.mul_right t
    obtain ⟨p, hpS, hpq⟩ := (Prime.dvd_finset_prod_iff hq.prime _).mp hqM
    exact ⟨p, hpS, eq_of_dvd_card_primaryPart (Nat.prime_of_mem_primeFactors
      (Finset.mem_of_mem_erase hpS)) hq hpq⟩
  have hnot2 : ¬ (2 : ℕ) ∣ t := by
    intro h
    obtain ⟨p, hpS, hpq⟩ := hdvd_t 2 Nat.prime_two h
    subst hpq
    exact h2not (Nat.dvd_of_mem_primeFactors (Finset.mem_of_mem_erase hpS))
  have hnot3 : ¬ (3 : ℕ) ∣ t := by
    intro h
    obtain ⟨p, hpS, hpq⟩ := hdvd_t 3 (by norm_num) h
    subst hpq
    exact (Finset.mem_erase.mp hpS).1 rfl
  have hnot5 : ¬ (5 : ℕ) ∣ t := by
    intro h
    obtain ⟨p, hpS, hpq⟩ := hdvd_t 5 (by norm_num) h
    subst hpq
    exact h5not (Nat.dvd_of_mem_primeFactors (Finset.mem_of_mem_erase hpS))
  have c2 : Nat.Coprime t 2 :=
    Nat.coprime_comm.mp ((Nat.Prime.coprime_iff_not_dvd Nat.prime_two).mpr hnot2)
  have c3 : Nat.Coprime t 3 :=
    Nat.coprime_comm.mp ((Nat.Prime.coprime_iff_not_dvd (by norm_num)).mpr hnot3)
  have c5 : Nat.Coprime t 5 :=
    Nat.coprime_comm.mp ((Nat.Prime.coprime_iff_not_dvd (by norm_num)).mpr hnot5)
  have : Nat.Coprime t (2 * 3 * 5) := (c2.mul_right c3).mul_right c5
  simpa using this

/-! ### CM4: an order-441 group satisfying every hypothesis of H2 -/

/-- If the exponent `n` kills `G` and the prime `p` does not divide `n`, the `p`-part is trivial. -/
lemma primaryPart_eq_bot_of_exponent {n : ℕ} (hexp : ∀ x : G, n • x = 0) {p : ℕ} (hp : p.Prime)
    (hpn : ¬ p ∣ n) : primaryPart G p = ⊥ := by
  refine primaryPart_eq_bot_of_torsionfree p ?_
  intro x hx
  have hcop : Nat.Coprime p n := (Nat.Prime.coprime_iff_not_dvd hp).mpr hpn
  have hcopZ : IsCoprime (p : ℤ) (n : ℤ) := by
    rw [Int.isCoprime_iff_gcd_eq_one]; simpa using hcop
  obtain ⟨u, v, huv⟩ := hcopZ
  have hpz : ((p : ℤ)) • x = 0 := by rw [natCast_zsmul]; exact hx
  have hnz : ((n : ℤ)) • x = 0 := by rw [natCast_zsmul]; exact hexp x
  calc x = ((u * (p : ℤ) + v * (n : ℤ))) • x := by rw [huv, one_zsmul]
    _ = u • ((p : ℤ) • x) + v • ((n : ℤ) • x) := by rw [add_zsmul, smul_smul, smul_smul]
    _ = 0 := by rw [hpz, hnz, smul_zero, smul_zero, add_zero]

/-- If `p ^ k` kills `G`, the `p`-part is everything. -/
lemma primaryPart_eq_top_of_pow_exponent {p k : ℕ} (hexp : ∀ x : G, (p ^ k) • x = 0) :
    primaryPart G p = ⊤ :=
  eq_top_iff.mpr fun x _ => ⟨k, hexp x⟩

/-- The primary part of a product is the product of the primary parts. -/
lemma primaryPart_prod {A B : Type*} [AddCommGroup A] [AddCommGroup B] (p : ℕ) :
    primaryPart (A × B) p = (primaryPart A p).prod (primaryPart B p) := by
  ext x
  constructor
  · rintro ⟨k, hk⟩
    have h1 : (p ^ k) • x.1 = 0 := congrArg Prod.fst hk
    have h2 : (p ^ k) • x.2 = 0 := congrArg Prod.snd hk
    exact ⟨⟨k, h1⟩, ⟨k, h2⟩⟩
  · rintro ⟨⟨k, hk⟩, ⟨l, hl⟩⟩
    refine ⟨k + l, Prod.ext ?_ ?_⟩
    · show (p ^ (k + l)) • x.1 = 0
      rw [pow_add, mul_comm, mul_smul, hk, smul_zero]
    · show (p ^ (k + l)) • x.2 = 0
      rw [pow_add, mul_smul, hl, smul_zero]

lemma card_prod_subgroup {A B : Type*} [AddCommGroup A] [AddCommGroup B] (H : AddSubgroup A)
    (K : AddSubgroup B) : Nat.card (H.prod K) = Nat.card H * Nat.card K := by
  rw [Nat.card_congr (H.prodEquiv K).toEquiv, Nat.card_prod]

/-- The concrete countermodel of CM4. -/
abbrev G441 : Type := (ZMod 3 × ZMod 3) × (ZMod 7 × ZMod 7)

lemma zmod_nsmul_eq_zero {m n : ℕ} (h : m ∣ n) (a : ZMod m) : n • a = 0 := by
  obtain ⟨c, rfl⟩ := h
  rw [nsmul_eq_mul]
  push_cast
  rw [ZMod.natCast_self, zero_mul, zero_mul]

lemma exponent_three (x : ZMod 3 × ZMod 3) : (3 : ℕ) • x = 0 :=
  Prod.ext (zmod_nsmul_eq_zero dvd_rfl _) (zmod_nsmul_eq_zero dvd_rfl _)

lemma exponent_seven (x : ZMod 7 × ZMod 7) : (7 : ℕ) • x = 0 :=
  Prod.ext (zmod_nsmul_eq_zero dvd_rfl _) (zmod_nsmul_eq_zero dvd_rfl _)

lemma exponent_G441 (x : G441) : (21 : ℕ) • x = 0 :=
  Prod.ext (Prod.ext (zmod_nsmul_eq_zero (by norm_num) _) (zmod_nsmul_eq_zero (by norm_num) _))
    (Prod.ext (zmod_nsmul_eq_zero (by norm_num) _) (zmod_nsmul_eq_zero (by norm_num) _))

lemma primaryPart_G441_three : Nat.card (primaryPart G441 3) = 9 := by
  rw [primaryPart_prod,
    primaryPart_eq_top_of_pow_exponent (p := 3) (k := 1) (by simpa using exponent_three),
    primaryPart_eq_bot_of_exponent exponent_seven (by norm_num) (by norm_num),
    card_prod_subgroup, AddSubgroup.card_bot,
    Nat.card_congr (AddSubgroup.topEquiv (G := ZMod 3 × ZMod 3)).toEquiv]
  simp

lemma primaryPart_G441_seven : Nat.card (primaryPart G441 7) = 49 := by
  rw [primaryPart_prod,
    primaryPart_eq_bot_of_exponent exponent_three (by norm_num) (by norm_num),
    primaryPart_eq_top_of_pow_exponent (p := 7) (k := 1) (by simpa using exponent_seven),
    card_prod_subgroup, AddSubgroup.card_bot,
    Nat.card_congr (AddSubgroup.topEquiv (G := ZMod 7 × ZMod 7)).toEquiv]
  simp

lemma primaryPart_G441_other {p : ℕ} (hp : p.Prime) (h3 : p ≠ 3) (h7 : p ≠ 7) :
    Nat.card (primaryPart G441 p) = 1 := by
  have hpn : ¬ p ∣ 21 := by
    intro hdvd
    have h : p ∣ 3 * 7 := by norm_num; exact hdvd
    rcases (Nat.Prime.dvd_mul hp).mp h with h' | h'
    · exact h3 ((Nat.prime_dvd_prime_iff_eq hp (by norm_num)).mp h')
    · exact h7 ((Nat.prime_dvd_prime_iff_eq hp (by norm_num)).mp h')
  rw [primaryPart_eq_bot_of_exponent exponent_G441 hp hpn, AddSubgroup.card_bot]

end PrimarySupport
