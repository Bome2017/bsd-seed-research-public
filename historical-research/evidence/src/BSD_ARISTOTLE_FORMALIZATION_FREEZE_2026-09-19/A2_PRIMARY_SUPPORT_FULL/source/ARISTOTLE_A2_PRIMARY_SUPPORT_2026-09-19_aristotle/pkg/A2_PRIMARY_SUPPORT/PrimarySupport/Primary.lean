import PrimarySupport.Defs

/-!
# A2 — helper lemmas: primary parts, torsion decomposition and assembly

Supporting material for the packaged targets P1–P5 and H0/H2.  Everything is abstract abelian group
theory; no arithmetic input of any kind is used.
-/

namespace PrimarySupport

variable {G : Type*} [AddCommGroup G]

lemma mem_primaryPart_iff {p : ℕ} {x : G} : x ∈ primaryPart G p ↔ ∃ k : ℕ, p ^ k • x = 0 := Iff.rfl

/-- P1. Without `p`-torsion the `p`-primary part is trivial. -/
lemma primaryPart_eq_bot_of_torsionfree (p : ℕ) (hfree : ∀ x : G, p • x = 0 → x = 0) :
    primaryPart G p = ⊥ := by
  rw [AddSubgroup.eq_bot_iff_forall]
  rintro x ⟨k, hk⟩
  induction k generalizing x with
  | zero => simpa using hk
  | succ k ih =>
    refine hfree x (ih (p • x) ?_)
    rw [pow_succ, mul_smul] at hk
    exact hk

/-- P2 (core form). If `n • x = 0` with `n > 0`, then `x` is a sum of elements of the primary parts
at the prime factors of `n`. -/
lemma torsion_decomp :
    ∀ n : ℕ, ∀ x : G, 0 < n → n • x = 0 →
      ∃ f : ℕ → G, (∀ p ∈ n.primeFactors, f p ∈ primaryPart G p) ∧
        x = ∑ p ∈ n.primeFactors, f p := by
  intro n
  induction n using Nat.strong_induction_on with
  | _ n ih =>
    intro x hn hx
    by_cases h1 : n = 1
    · subst h1
      exact ⟨fun _ => 0, by simp, by simpa using hx⟩
    · have hn0 : n ≠ 0 := hn.ne'
      set q := n.minFac with hqdef
      have hq : q.Prime := Nat.minFac_prime h1
      have hqn : q ∣ n := Nat.minFac_dvd n
      set a := n.factorization q with ha
      set A := q ^ a with hA
      set m := n / A with hm
      have hAm : A * m = n := Nat.ordProj_mul_ordCompl_eq_self n q
      have hnd : ¬ q ∣ m := Nat.not_dvd_ordCompl hq hn0
      have hmpos : 0 < m := Nat.ordCompl_pos q hn0
      have ha1 : 1 ≤ a := Nat.Prime.factorization_pos_of_dvd hq hn0 hqn
      have hA2 : 2 ≤ A := by
        calc 2 ≤ q := hq.two_le
        _ = q ^ 1 := (pow_one q).symm
        _ ≤ q ^ a := Nat.pow_le_pow_right hq.pos ha1
      have hmlt : m < n := by nlinarith [hAm, hmpos]
      have hcop : Nat.Coprime A m :=
        Nat.Coprime.pow_left _ ((Nat.Prime.coprime_iff_not_dvd hq).mpr hnd)
      have hcopZ : IsCoprime (A : ℤ) (m : ℤ) := by
        rw [Int.isCoprime_iff_gcd_eq_one]; simpa using hcop
      obtain ⟨u, v, huv⟩ := hcopZ
      set x1 : G := (v * (m : ℤ)) • x with hx1
      set x2 : G := (u * (A : ℤ)) • x with hx2
      have hsplit : x = x1 + x2 := by
        calc x = ((u * (A : ℤ) + v * (m : ℤ))) • x := by rw [huv, one_zsmul]
        _ = x1 + x2 := by rw [add_zsmul, hx1, hx2]; abel
      have hnz : ((n : ℤ)) • x = 0 := by rw [natCast_zsmul]; exact hx
      have hx1mem : A • x1 = 0 := by
        have h : ((A : ℤ)) • x1 = 0 := by
          rw [hx1, smul_smul]
          have he : (A : ℤ) * (v * m) = v * (n : ℤ) := by push_cast [← hAm]; ring
          rw [he, ← smul_smul, hnz, smul_zero]
        rwa [natCast_zsmul] at h
      have hx2mem : m • x2 = 0 := by
        have h : ((m : ℤ)) • x2 = 0 := by
          rw [hx2, smul_smul]
          have he : (m : ℤ) * (u * A) = u * (n : ℤ) := by push_cast [← hAm]; ring
          rw [he, ← smul_smul, hnz, smul_zero]
        rwa [natCast_zsmul] at h
      obtain ⟨f', hf'mem, hf'sum⟩ := ih m hmlt x2 hmpos hx2mem
      have hqnotm : q ∉ m.primeFactors := fun hmem => hnd (Nat.dvd_of_mem_primeFactors hmem)
      have hne : ∀ p ∈ m.primeFactors, p ≠ q := fun p hp h => hqnotm (by rwa [h] at hp)
      have hpf : n.primeFactors = insert q m.primeFactors := by
        rw [← hAm, Nat.primeFactors_mul (by positivity) hmpos.ne', hA,
          Nat.primeFactors_pow q (by omega), hq.primeFactors]
        exact (Finset.insert_eq q _).symm
      refine ⟨fun p => if p = q then x1 else f' p, ?_, ?_⟩
      · intro p hp
        rw [hpf, Finset.mem_insert] at hp
        rcases hp with rfl | hp
        · exact ⟨a, by simpa [← hA] using hx1mem⟩
        · simpa only [if_neg (hne p hp)] using hf'mem p hp
      · rw [hpf, Finset.sum_insert hqnotm, if_pos rfl,
          Finset.sum_congr rfl (fun p hp => if_neg (hne p hp)), ← hf'sum]
        exact hsplit

/-- P2, in the packaged shape. -/
lemma torsion_decomposition_aux (htor : AddMonoid.IsTorsion G) (x : G) :
    ∃ (T : Finset ℕ) (f : ℕ → G),
      (∀ p ∈ T, p.Prime ∧ f p ∈ primaryPart G p) ∧ x = ∑ p ∈ T, f p := by
  obtain ⟨n, hnpos, hn⟩ := isOfFinAddOrder_iff_nsmul_eq_zero.mp (htor x)
  obtain ⟨f, hmem, hsum⟩ := torsion_decomp n x hnpos hn
  exact ⟨n.primeFactors, f, fun p hp => ⟨Nat.prime_of_mem_primeFactors hp, hmem p hp⟩, hsum⟩

/-! ### Assembly -/

/-- The summation map from the product of the primary parts indexed by a finite set of primes. -/
def sumMap (T : Finset ℕ) (g : ∀ p : {p // p ∈ T}, primaryPart G p) : G :=
  ∑ p ∈ T.attach, (g p : G)

/-- If all primary parts outside `T` vanish, the summation map is surjective. -/
lemma sumMap_surjective (T : Finset ℕ) (htor : AddMonoid.IsTorsion G)
    (hbot : ∀ p, p.Prime → p ∉ T → primaryPart G p = ⊥) :
    Function.Surjective (sumMap (G := G) T) := by
  intro x
  obtain ⟨S, f, hmem, hsum⟩ := torsion_decomposition_aux htor x
  classical
  refine ⟨fun p => ⟨if (p : ℕ) ∈ S then f (p : ℕ) else 0, ?_⟩, ?_⟩
  · by_cases hp : (p : ℕ) ∈ S
    · simpa [hp] using (hmem (p : ℕ) hp).2
    · simp [hp]
  · -- the sum over `T` recovers `x`
    have hzero : ∀ p ∈ S, p ∉ T → f p = 0 := by
      intro p hpS hpT
      have hprime : p.Prime := (hmem p hpS).1
      have : f p ∈ primaryPart G p := (hmem p hpS).2
      rw [hbot p hprime hpT] at this
      simpa using this
    have h1 : x = ∑ p ∈ S ∩ T, f p := by
      rw [hsum, ← Finset.sum_filter_add_sum_filter_not S (· ∈ T)]
      have h2 : ∑ p ∈ S.filter (fun p => p ∉ T), f p = 0 :=
        Finset.sum_eq_zero fun p hp => by
          rw [Finset.mem_filter] at hp
          exact hzero p hp.1 hp.2
      rw [h2, add_zero]
      congr 1
    have hfilter : T.filter (fun p => p ∈ S) = S ∩ T := by
      ext p
      simp only [Finset.mem_filter, Finset.mem_inter]
      tauto
    rw [sumMap, Finset.sum_attach T (fun p => if p ∈ S then f p else 0), ← Finset.sum_filter,
      hfilter]
    exact h1.symm

/-- P3. -/
lemma finite_of_primary (T : Finset ℕ) (htor : AddMonoid.IsTorsion G)
    (hbot : ∀ p, p.Prime → p ∉ T → primaryPart G p = ⊥)
    (hfin : ∀ p ∈ T, (primaryPart G p : Set G).Finite) : Finite G := by
  haveI : ∀ p : {p // p ∈ T}, Finite (primaryPart G (p : ℕ)) := by
    intro p
    exact (hfin (p : ℕ) p.2).to_subtype
  haveI : Finite (∀ p : {p // p ∈ T}, primaryPart G (p : ℕ)) := Pi.finite
  exact Finite.of_surjective _ (sumMap_surjective T htor hbot)

/-- P4. The assembly in the shape used downstream. -/
lemma finite_of_primary_WC_shape (S0 : Finset ℕ) (A : ℤ) (htor : AddMonoid.IsTorsion G)
    (hA : A ≠ 0) (hbot : ∀ p ∈ primesOutside S0, ¬ ((p : ℤ) ∣ A) → primaryPart G p = ⊥)
    (hfin : ∀ p ∈ primesOutside S0, (primaryPart G p : Set G).Finite)
    (hS0 : ∀ p ∈ S0, p.Prime → (primaryPart G p : Set G).Finite) : Finite G := by
  classical
  refine finite_of_primary ((S0 ∪ A.natAbs.primeFactors).filter Nat.Prime) htor ?_ ?_
  · intro p hp hpT
    have hpS0 : p ∉ S0 := by
      intro hmem
      exact hpT (Finset.mem_filter.mpr ⟨Finset.mem_union_left _ hmem, hp⟩)
    refine hbot p ⟨hp, hpS0⟩ ?_
    intro hdvd
    have hnat : p ∣ A.natAbs := Int.natCast_dvd_natCast.mp (Int.dvd_natAbs.mpr hdvd)
    have : p ∈ A.natAbs.primeFactors :=
      Nat.mem_primeFactors.mpr ⟨hp, hnat, Int.natAbs_ne_zero.mpr hA⟩
    exact hpT (Finset.mem_filter.mpr ⟨Finset.mem_union_right _ this, hp⟩)
  · intro p hpT
    have hp : p.Prime := (Finset.mem_filter.mp hpT).2
    by_cases hpS0 : p ∈ S0
    · exact hS0 p hpS0 hp
    · exact hfin p ⟨hp, hpS0⟩

/-- In a finite group, a prime with nontrivial primary part divides the order. -/
lemma prime_dvd_card_of_primaryPart_ne_bot [Finite G] {p : ℕ} (hp : p.Prime)
    (hne : primaryPart G p ≠ ⊥) : p ∣ Nat.card G := by
  obtain ⟨x, hxmem, hx0⟩ : ∃ x : G, x ∈ primaryPart G p ∧ x ≠ 0 := by
    by_contra hcon
    push_neg at hcon
    exact hne ((AddSubgroup.eq_bot_iff_forall _).2 fun x hx => hcon x hx)
  obtain ⟨k, hk⟩ := hxmem
  have hdvd : addOrderOf x ∣ p ^ k := addOrderOf_dvd_of_nsmul_eq_zero hk
  obtain ⟨i, _, hi⟩ := (Nat.dvd_prime_pow hp).1 hdvd
  have hi0 : i ≠ 0 := by
    intro h
    rw [h, pow_zero] at hi
    exact hx0 (AddMonoid.addOrderOf_eq_one_iff.mp hi)
  have hpx : p ∣ addOrderOf x := by
    rw [hi]
    exact dvd_pow_self p hi0
  exact hpx.trans (addOrderOf_dvd_natCard x)

/-- P5. For a torsion group, finiteness is exactly local finiteness plus finite prime support. -/
lemma finite_iff_local_and_support_aux (htor : AddMonoid.IsTorsion G) :
    Finite G ↔ (∀ p, p.Prime → (primaryPart G p : Set G).Finite) ∧
      {p | p.Prime ∧ primaryPart G p ≠ ⊥}.Finite := by
  constructor
  · intro hG
    refine ⟨fun p _ => Set.toFinite _, ?_⟩
    have hsub : {p : ℕ | p.Prime ∧ primaryPart G p ≠ ⊥} ⊆ (Nat.card G).primeFactors := by
      rintro p ⟨hp, hne⟩
      exact Nat.mem_primeFactors.mpr ⟨hp, prime_dvd_card_of_primaryPart_ne_bot hp hne,
        Nat.card_pos.ne'⟩
    exact Set.Finite.subset (Nat.card G).primeFactors.finite_toSet hsub
  · rintro ⟨hloc, hsupp⟩
    refine finite_of_primary hsupp.toFinset htor ?_ ?_
    · intro p hp hpT
      by_contra hne
      exact hpT (hsupp.mem_toFinset.mpr ⟨hp, hne⟩)
    · intro p hpT
      exact hloc p (hsupp.mem_toFinset.mp hpT).1

end PrimarySupport
