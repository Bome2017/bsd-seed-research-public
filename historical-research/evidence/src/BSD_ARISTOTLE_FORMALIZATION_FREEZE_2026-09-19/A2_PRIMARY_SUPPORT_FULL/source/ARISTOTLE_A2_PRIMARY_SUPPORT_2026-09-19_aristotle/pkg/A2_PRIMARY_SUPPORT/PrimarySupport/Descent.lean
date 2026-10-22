import PrimarySupport.Content
import PrimarySupport.Depth

/-!
# A2 — helper lemmas: descent to `ℤ` with a primitive comparison (target L7)

The comparison vector `z` is a *hypothesis*; nothing here constructs it.
-/

namespace PrimarySupport

/-- L7. If the depth is bounded by the content valuation of a fixed nonzero lattice vector outside
a finite set `B`, and is finite on `B`, then `JOf P h` contains a nonzero integer. -/
lemma exists_ne_zero_mem_JOf_of_content_bound {P : Set ℕ} {h : ℕ → ℕ∞} (B : Finset ℕ) {n : ℕ}
    (z : Fin n → ℤ) (hP : ∀ p ∈ P, p.Prime) (hz : z ≠ 0)
    (hout : ∀ p ∈ P, p ∉ B → h p ≤ (padicValInt p (content z) : ℕ))
    (hin : ∀ p ∈ P, p ∈ B → h p ≠ ⊤) :
    ∃ A : ℤ, A ≠ 0 ∧ A ∈ JOf P h := by
  have hc : content z ≠ 0 := content_ne_zero hz
  have htop : ∀ p ∈ P, h p ≠ ⊤ := by
    intro p hpP
    by_cases hpB : p ∈ B
    · exact hin p hpP hpB
    · intro hpt
      have := hout p hpP hpB
      rw [hpt] at this
      simp at this
  have hsupp : (posSupport P h).Finite := by
    refine Set.Finite.subset (Set.Finite.union (B : Set ℕ).toFinite (finite_primes_dvd hc)) ?_
    rintro p ⟨hpP, hpne⟩
    by_cases hpB : p ∈ B
    · exact Or.inl hpB
    · refine Or.inr ?_
      haveI : Fact (Nat.Prime p) := ⟨hP p hpP⟩
      have hle : h p ≤ ((padicValInt p (content z) : ℕ) : ℕ∞) := hout p hpP hpB
      have hpos : 1 ≤ padicValInt p (content z) := by
        by_contra hcon
        have h0 : padicValInt p (content z) = 0 := by omega
        rw [h0] at hle
        exact hpne (le_antisymm (by simpa using hle) (zero_le _))
      have : (p : ℤ) ^ 1 ∣ content z := (padicValInt_dvd_iff 1 (content z)).2 (Or.inr hpos)
      simpa using this
  obtain ⟨A, hA, hA0⟩ := (exists_ne_zero_mem_JOf_iff hP).2 ⟨htop, hsupp⟩
  exact ⟨A, hA0, hA⟩

end PrimarySupport
