import WitnessContent.Primary
import WitnessContent.GroupRing

/-!
# A1 — the Witness-Content implication

Proof of the abstract Theorem WC (T7) and of its group-ring instantiation (T8).

Every arithmetic input (Ota's theorems, the Selmer corank facts, torsion of Sha) and the open
antecedent `A ≠ 0 ∧ A ∈ J_E` are hypotheses; nothing here proves any of them.
-/

set_option synthInstance.maxHeartbeats 1000000
set_option maxHeartbeats 1000000

namespace WitnessContent

open scoped BigOperators

/-- T7: Theorem WC in abstract witness form. -/
theorem WC_abstract_proof : Spec.WC_abstract := by
  classical
  intro S0 Sha _ W M _ t r hexp htors hselmer hota517 hota15 A hA hAJ
  obtain ⟨hbound, hzero⟩ := JE_bounds_aux t (primesOutside S0) A hA hAJ
  -- conclusion (1): each good primary part is finite
  have h1 : ∀ p ∈ primesOutside S0, (primaryPart Sha p : Set Sha).Finite := by
    intro p hp
    by_contra hinf
    have hr3 : 3 ≤ r p := hselmer p hp hinf
    have hall : ∀ S, t p S = 0 := fun S => hota517 p hp S hr3
    have hlt : hInf t p < ⊤ :=
      lt_of_le_of_lt (hbound p hp) (ENat.coe_lt_top _)
    obtain ⟨S, hS⟩ := (hInf_lt_top_iff_aux t p).1 hlt
    exact hS (hall S)
  -- conclusion (2): the good primary parts vanish away from A
  have h2 : ∀ p ∈ primesOutside S0, ¬ (p : ℤ) ∣ A → primaryPart Sha p = ⊥ := by
    intro p hp hdvd
    have hp' : p.Prime := hp.1
    have h0 : hInf t p = 0 := hzero p hp hp' hdvd
    have hle : hInf t p ≤ ((0 : ℕ) : ℕ∞) := by rw [h0]; simp
    obtain ⟨S, hS⟩ := (hInf_le_iff_aux t p hp' (hexp p hp) 0).1 hle
    rw [zero_add] at hS
    exact primaryPart_eq_bot_of_ptorsion_trivial p (hota15 p hp S hS)
  refine ⟨h1, h2, ?_⟩
  -- conclusion (3): global finiteness, given finiteness at the exceptional primes
  intro hS0fin
  set T : Finset ℕ := (S0.filter Nat.Prime) ∪ A.natAbs.primeFactors with hT
  have hTprime : ∀ p ∈ T, p.Prime := by
    intro p hpT
    rcases Finset.mem_union.1 hpT with h | h
    · exact (Finset.mem_filter.1 h).2
    · exact Nat.prime_of_mem_primeFactors h
  have hTfin : ∀ p ∈ T, (primaryPart Sha p : Set Sha).Finite := by
    intro p hpT
    by_cases hpS0 : p ∈ S0
    · exact hS0fin p hpS0 (hTprime p hpT)
    · exact h1 p ⟨hTprime p hpT, hpS0⟩
  refine finite_of_covered_by_primary T hTfin ?_
  intro x
  -- x is torsion, so it decomposes over the prime factors of its order
  have hxfin : IsOfFinAddOrder x := htors x
  set n : ℕ := addOrderOf x with hn
  have hnpos : 0 < n := hxfin.addOrderOf_pos
  have hnx : n • x = 0 := addOrderOf_nsmul_eq_zero x
  obtain ⟨μ, hμmem, hμsum⟩ := exists_primary_decomposition x n (by omega) hnx
  -- components away from T vanish, by conclusion (2)
  have hvanish : ∀ q ∈ n.primeFactors, q ∉ T → μ q = 0 := by
    intro q hq hqT
    have hqp : q.Prime := Nat.prime_of_mem_primeFactors hq
    have hqS0 : q ∉ S0 := by
      intro hmem
      exact hqT (Finset.mem_union_left _ (Finset.mem_filter.2 ⟨hmem, hqp⟩))
    have hqA : ¬ (q : ℤ) ∣ A := by
      intro hdvd
      have hdvd' : q ∣ A.natAbs := by
        have : (q : ℤ) ∣ (A.natAbs : ℤ) := (Int.dvd_natAbs).2 hdvd
        exact_mod_cast this
      exact hqT (Finset.mem_union_right _
        (Nat.mem_primeFactors.2 ⟨hqp, hdvd', Int.natAbs_ne_zero.2 hA⟩))
    have hbot : primaryPart Sha q = ⊥ := h2 q ⟨hqp, hqS0⟩ hqA
    have := hμmem q hq
    rw [hbot] at this
    simpa using this
  refine ⟨fun q => if q ∈ n.primeFactors then μ q else 0, ?_, ?_⟩
  · intro q _
    by_cases hq : q ∈ n.primeFactors
    · simpa [hq] using hμmem q hq
    · simp [hq]
  · -- both sums reduce to the sum over `n.primeFactors ∩ T`
    have hsum1 : ∑ q ∈ T, (if q ∈ n.primeFactors then μ q else 0)
        = ∑ q ∈ T ∩ n.primeFactors, μ q := by
      rw [Finset.sum_ite_mem]
    have hsum2 : ∑ q ∈ n.primeFactors, μ q = ∑ q ∈ n.primeFactors ∩ T, μ q := by
      refine (Finset.sum_subset Finset.inter_subset_left ?_).symm
      intro q hq hnot
      exact hvanish q hq (fun hqT => hnot (Finset.mem_inter.2 ⟨hq, hqT⟩))
    rw [hsum1, Finset.inter_comm, ← hsum2, hμsum]

/-- T8: Theorem WC with Ota Thm 5.17 in its group-ring form. -/
theorem WC_groupRing_proof : Spec.WC_groupRing := by
  classical
  intro S0 Sha _ W Rp _ G _ e θ r h2S0 hG hunits htors hcorank hselmer hota517 hota15 A hA hAJ
  refine WC_abstract_proof S0 Sha W (fun p S => gr (Rp p) (G p S) 2)
    (fun p S => cls2 (θ p S)) r ?_ htors hselmer ?_ hota15 A hA hAJ
  · -- bounded p-power exponent, from T3
    intro p hp S
    obtain ⟨he0, he⟩ := hG p hp S
    refine ⟨(e p S).factorization p, fun y => ?_⟩
    exact gr_pow_factorization_smul_eq_zero p (e p S) hp.1 he0 he (hunits p hp) 2 (by norm_num) y
  · -- the witness form of Ota 5.17, from T4
    intro p hp S hr3
    have hp3 : 3 ≤ p := by
      have hpp : p.Prime := hp.1
      have hne2 : p ≠ 2 := by
        intro h
        exact hp.2 (h ▸ h2S0)
      have h2le := hpp.two_le
      omega
    exact (bridge_517_aux (θ p S) (r p) p (hcorank p hp) hp3 (hota517 p hp S)).2 hr3

end WitnessContent
