import PrimarySupport.Primary

/-!
# A2 — the torsion countermodels CM1 and CM1′

* CM1: `⨁_p ZMod p` has every primary part finite, infinitely many nonzero primary parts, and is
  infinite.  So "every primary part finite" does not imply finiteness.
* CM1′: `ℕ →₀ ZMod 2` is torsion with finite prime support but infinite.  So finite prime support
  does not imply finiteness.
-/

namespace PrimarySupport

/-! ### CM1 -/

/-- The direct sum `⨁_p ZMod p` over the primes. -/
abbrev DSum : Type := Π₀ p : Nat.Primes, ZMod (p : ℕ)

lemma dsum_isTorsion : AddMonoid.IsTorsion DSum := by
  intro x
  rw [isOfFinAddOrder_iff_nsmul_eq_zero]
  refine ⟨∏ q ∈ x.support, (q : ℕ), ?_, ?_⟩
  · exact Finset.prod_pos fun q _ => (q : Nat.Primes).2.pos
  · ext q
    rw [DFinsupp.smul_apply, DFinsupp.zero_apply]
    by_cases hq : q ∈ x.support
    · have hdvd : ((q : ℕ)) ∣ ∏ r ∈ x.support, (r : ℕ) :=
        Finset.dvd_prod_of_mem (fun r : Nat.Primes => (r : ℕ)) hq
      obtain ⟨c, hc⟩ := hdvd
      rw [hc, mul_comm, mul_nsmul]
      have hz : ((q : ℕ)) • (c • x q) = 0 := by
        rw [nsmul_eq_mul, ZMod.natCast_self, zero_mul]
      exact hz
    · rw [DFinsupp.notMem_support_iff.mp hq, smul_zero]

/-- Off the prime `p` itself, an element of the `p`-primary part of `⨁_q ZMod q` vanishes. -/
lemma dsum_primary_apply_eq_zero {p : ℕ} (hp : p.Prime) {x : DSum}
    (hx : x ∈ primaryPart DSum p) (q : Nat.Primes) (hq : (q : ℕ) ≠ p) : x q = 0 := by
  obtain ⟨k, hk⟩ := hx
  have hkq : (p ^ k) • (x q) = 0 := by
    have := congrArg (fun y : DSum => y q) hk
    simpa using this
  haveI : Fact ((q : ℕ)).Prime := ⟨(q : Nat.Primes).2⟩
  have hne : ((p ^ k : ℕ) : ZMod (q : ℕ)) ≠ 0 := by
    rw [Ne, ZMod.natCast_eq_zero_iff]
    intro hdvd
    have := Nat.Prime.dvd_of_dvd_pow (q : Nat.Primes).2 hdvd
    exact hq (((Nat.prime_dvd_prime_iff_eq (q : Nat.Primes).2 hp).mp this))
  have : ((p ^ k : ℕ) : ZMod (q : ℕ)) * (x q) = 0 := by rw [← nsmul_eq_mul]; exact hkq
  rcases mul_eq_zero.mp this with h | h
  · exact absurd h hne
  · exact h

lemma dsum_primary_finite {p : ℕ} (hp : p.Prime) :
    (primaryPart DSum p : Set DSum).Finite := by
  haveI : Fact p.Prime := ⟨hp⟩
  have hsub : (primaryPart DSum p : Set DSum) ⊆
      Set.range (fun a : ZMod p => DFinsupp.single (⟨p, hp⟩ : Nat.Primes) a) := by
    intro x hx
    refine ⟨x ⟨p, hp⟩, ?_⟩
    ext q
    by_cases hq : q = (⟨p, hp⟩ : Nat.Primes)
    · subst hq; simp
    · have hqp : (q : ℕ) ≠ p := fun h => hq (Subtype.ext h)
      rw [DFinsupp.single_eq_of_ne hq, dsum_primary_apply_eq_zero hp hx q hqp]
  exact Set.Finite.subset (Set.finite_range _) hsub

lemma dsum_single_mem_primary {p : ℕ} (hp : p.Prime) (a : ZMod p) :
    (DFinsupp.single (⟨p, hp⟩ : Nat.Primes) a : DSum) ∈ primaryPart DSum p := by
  refine ⟨1, ?_⟩
  ext q
  rw [DFinsupp.smul_apply, DFinsupp.zero_apply, pow_one]
  by_cases hq : q = (⟨p, hp⟩ : Nat.Primes)
  · subst hq
    rw [DFinsupp.single_eq_same, nsmul_eq_mul, ZMod.natCast_self, zero_mul]
  · rw [DFinsupp.single_eq_of_ne hq, smul_zero]

lemma dsum_primary_ne_bot {p : ℕ} (hp : p.Prime) : primaryPart DSum p ≠ ⊥ := by
  haveI : Fact p.Prime := ⟨hp⟩
  intro hbot
  have hmem := dsum_single_mem_primary hp (1 : ZMod p)
  rw [hbot] at hmem
  have h0 : (DFinsupp.single (⟨p, hp⟩ : Nat.Primes) (1 : ZMod p) : DSum) = 0 := hmem
  have := congrArg (fun y : DSum => y (⟨p, hp⟩ : Nat.Primes)) h0
  simp at this

lemma dsum_support_infinite : {p : ℕ | p.Prime ∧ primaryPart DSum p ≠ ⊥}.Infinite := by
  have heq : {p : ℕ | p.Prime ∧ primaryPart DSum p ≠ ⊥} = {p : ℕ | p.Prime} := by
    ext p
    exact ⟨fun h => h.1, fun h => ⟨h, dsum_primary_ne_bot h⟩⟩
  rw [heq]
  exact Nat.infinite_setOf_prime

lemma dsum_not_finite : ¬ Finite DSum := by
  have hinj : Function.Injective
      (fun p : Nat.Primes => (DFinsupp.single p (1 : ZMod (p : ℕ)) : DSum)) := by
    intro p q hpq
    by_contra hne
    haveI : Fact ((p : ℕ)).Prime := ⟨p.2⟩
    have h := congrArg (fun y : DSum => y p) hpq
    simp only [DFinsupp.single_eq_same, DFinsupp.single_eq_of_ne hne] at h
    exact one_ne_zero h
  intro hfin
  exact (Infinite.of_injective _ hinj).not_finite hfin

/-! ### CM1′ -/

lemma finsupp_zmod2_isTorsion : AddMonoid.IsTorsion (ℕ →₀ ZMod 2) := by
  intro x
  rw [isOfFinAddOrder_iff_nsmul_eq_zero]
  refine ⟨2, by norm_num, ?_⟩
  ext n
  rw [Finsupp.smul_apply, Finsupp.zero_apply, nsmul_eq_mul]
  have : ((2 : ℕ) : ZMod 2) = 0 := ZMod.natCast_self 2
  rw [this, zero_mul]

lemma finsupp_zmod2_primary_eq_bot {p : ℕ} (hp : p.Prime) (hp2 : p ≠ 2) :
    primaryPart (ℕ →₀ ZMod 2) p = ⊥ := by
  refine primaryPart_eq_bot_of_torsionfree p ?_
  intro x hx
  have hodd : p % 2 = 1 := by
    rcases hp.eq_two_or_odd with h | h
    · exact absurd h hp2
    · exact h
  obtain ⟨m, hm⟩ : ∃ m, p = 2 * m + 1 := ⟨p / 2, by omega⟩
  have h2 : (2 : ℕ) • x = 0 := by
    ext n
    rw [Finsupp.smul_apply, Finsupp.zero_apply, nsmul_eq_mul]
    have : ((2 : ℕ) : ZMod 2) = 0 := ZMod.natCast_self 2
    rw [this, zero_mul]
  have : x = 0 := by
    have hpx : ((2 * m + 1 : ℕ)) • x = 0 := by rw [← hm]; exact hx
    rw [add_smul, one_smul, mul_comm, mul_smul, h2, smul_zero, zero_add] at hpx
    exact hpx
  exact this

lemma finsupp_zmod2_support_finite :
    {p : ℕ | p.Prime ∧ primaryPart (ℕ →₀ ZMod 2) p ≠ ⊥}.Finite := by
  refine Set.Finite.subset (Set.finite_singleton 2) ?_
  rintro p ⟨hp, hne⟩
  by_contra hp2
  exact hne (finsupp_zmod2_primary_eq_bot hp hp2)

lemma finsupp_zmod2_not_finite : ¬ Finite (ℕ →₀ ZMod 2) := by
  have hinj : Function.Injective (fun n : ℕ => (Finsupp.single n (1 : ZMod 2))) := by
    intro n m hnm
    by_contra hne
    have := congrFun (congrArg (fun y : ℕ →₀ ZMod 2 => (y : ℕ → ZMod 2)) hnm) n
    simp [hne] at this
  intro hfin
  exact (Infinite.of_injective _ hinj).not_finite hfin

end PrimarySupport
