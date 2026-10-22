import PrimarySupport.Depth

/-!
# A2 — helper lemmas: Lemma B in the valuation model, and the profinite countermodel CM3

`v p` records the valuation of the local datum at `p`.  All statements are elementary.
-/

namespace PrimarySupport

/-- B1. Some nonzero integer is divisible by `p ^ v p` at every prime iff `v` has finite support. -/
lemma exists_int_dvd_iff_finite_support (v : ℕ → ℕ) :
    (∃ A : ℤ, A ≠ 0 ∧ ∀ p : ℕ, p.Prime → (p : ℤ) ^ v p ∣ A) ↔ {p | p.Prime ∧ v p ≠ 0}.Finite := by
  constructor
  · rintro ⟨A, hA0, hA⟩
    refine Set.Finite.subset (finite_primes_dvd hA0) ?_
    rintro p ⟨hp, hv⟩
    exact dvd_trans (dvd_pow_self _ hv) (hA p hp)
  · intro hfin
    refine ⟨∏ p ∈ hfin.toFinset, (p : ℤ) ^ v p, ?_, ?_⟩
    · refine Finset.prod_ne_zero_iff.2 fun p hp => pow_ne_zero _ ?_
      exact_mod_cast (hfin.mem_toFinset.mp hp).1.pos.ne'
    · intro p hp
      by_cases hv : v p = 0
      · simp [hv]
      · exact Finset.dvd_prod_of_mem (fun q : ℕ => (q : ℤ) ^ v q)
          (hfin.mem_toFinset.mpr ⟨hp, hv⟩)

/-- The product of the local cokernels is infinite as soon as infinitely many are nontrivial. -/
lemma not_finite_pi_of_infinite_support {v : ℕ → ℕ} (hinf : {p : ℕ | p.Prime ∧ v p ≠ 0}.Infinite) :
    ¬ Finite (∀ p : Nat.Primes, ZMod ((p : ℕ) ^ v p)) := by
  intro hfin
  set S := {p : ℕ | p.Prime ∧ v p ≠ 0} with hS
  let ι : ℕ ↪ S := hinf.natEmbedding
  have key : ∀ n : ℕ, ((ι n : ℕ)).Prime ∧ v (ι n : ℕ) ≠ 0 := fun n => (ι n).2
  let e : ℕ → (∀ p : Nat.Primes, ZMod ((p : ℕ) ^ v p)) :=
    fun n q => if (q : ℕ) = ((ι n : S) : ℕ) then 1 else 0
  have hinj : Function.Injective e := by
    intro n m hnm
    by_contra hne
    have hprime : ((ι n : S) : ℕ).Prime := (key n).1
    let q : Nat.Primes := ⟨((ι n : S) : ℕ), hprime⟩
    have h1 : e n q = 1 := by simp [e, q]
    have h2 : e m q = 0 := by
      have hne' : ((ι n : S) : ℕ) ≠ ((ι m : S) : ℕ) := fun h => hne (ι.injective (Subtype.ext h))
      simp [e, q, hne']
    haveI : Fact (1 < ((q : ℕ)) ^ v (q : ℕ)) := by
      constructor
      have h2p : 2 ≤ (q : ℕ) := hprime.two_le
      have hv : 1 ≤ v (q : ℕ) := Nat.one_le_iff_ne_zero.mpr (key n).2
      calc 1 < (q : ℕ) ^ 1 := by simpa using h2p
        _ ≤ (q : ℕ) ^ v (q : ℕ) := Nat.pow_le_pow_right (by omega) hv
    have : (1 : ZMod ((q : ℕ) ^ v (q : ℕ))) = 0 := by rw [← h1, ← h2, hnm]
    exact one_ne_zero this
  exact (Infinite.of_injective e hinj).not_finite hfin

/-- The product of the local cokernels is finite as soon as only finitely many are nontrivial. -/
lemma finite_pi_of_finite_support {v : ℕ → ℕ} (hfin : {p : ℕ | p.Prime ∧ v p ≠ 0}.Finite) :
    Finite (∀ p : Nat.Primes, ZMod ((p : ℕ) ^ v p)) := by
  set T : Set Nat.Primes := {p : Nat.Primes | v (p : ℕ) ≠ 0} with hT
  have hTfin : T.Finite := by
    have hsub : T ⊆ Subtype.val ⁻¹' {p : ℕ | p.Prime ∧ v p ≠ 0} := fun p hp => ⟨p.2, hp⟩
    exact Set.Finite.subset (hfin.preimage (Set.injOn_of_injective Subtype.val_injective)) hsub
  haveI : Finite T := hTfin
  haveI : ∀ p : T, Finite (ZMod (((p : Nat.Primes) : ℕ) ^ v ((p : Nat.Primes) : ℕ))) := by
    intro p
    haveI : NeZero (((p : Nat.Primes) : ℕ) ^ v ((p : Nat.Primes) : ℕ)) :=
      ⟨pow_ne_zero _ (p : Nat.Primes).2.pos.ne'⟩
    infer_instance
  have hinj : Function.Injective
      (fun (f : ∀ p : Nat.Primes, ZMod ((p : ℕ) ^ v p)) => fun p : T => f (p : Nat.Primes)) := by
    intro f g hfg
    funext q
    by_cases hq : v (q : ℕ) = 0
    · haveI : Subsingleton (ZMod ((q : ℕ) ^ v (q : ℕ))) := by rw [hq, pow_zero]; infer_instance
      exact Subsingleton.elim _ _
    · exact congrFun hfg ⟨q, hq⟩
  exact Finite.of_injective _ hinj

/-- B2. -/
lemma finite_pi_iff_finite_support (v : ℕ → ℕ) :
    Finite (∀ p : Nat.Primes, ZMod ((p : ℕ) ^ v p)) ↔ {p | p.Prime ∧ v p ≠ 0}.Finite := by
  constructor
  · intro hfin
    by_contra hinf
    exact not_finite_pi_of_infinite_support (Set.not_finite.mp hinf) hfin
  · exact finite_pi_of_finite_support

/-! ### CM3: the profinite countermodel -/

/-- The valuation datum of CM3: `v = 0` at `2` and `5`, and `v = 2` at every other prime. -/
def cm3v : ℕ → ℕ := fun p => if p = 2 ∨ p = 5 then 0 else 2

lemma cm3_support : {p : ℕ | p.Prime ∧ cm3v p ≠ 0} = {p : ℕ | p.Prime} \ {2, 5} := by
  ext p
  simp only [Set.mem_setOf_eq, Set.mem_diff, Set.mem_insert_iff, Set.mem_singleton_iff, cm3v]
  constructor
  · rintro ⟨hp, hv⟩
    refine ⟨hp, ?_⟩
    intro hcon
    simp [hcon] at hv
  · rintro ⟨hp, hcon⟩
    refine ⟨hp, ?_⟩
    simp [hcon]

lemma cm3_support_infinite : {p : ℕ | p.Prime ∧ cm3v p ≠ 0}.Infinite := by
  rw [cm3_support]
  exact Set.Infinite.diff Nat.infinite_setOf_prime (Set.toFinite _)

end PrimarySupport
