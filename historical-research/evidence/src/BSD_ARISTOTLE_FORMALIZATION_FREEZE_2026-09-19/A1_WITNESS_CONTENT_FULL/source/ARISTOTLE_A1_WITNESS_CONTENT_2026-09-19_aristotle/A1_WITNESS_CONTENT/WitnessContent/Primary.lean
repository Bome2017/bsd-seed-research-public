import WitnessContent.Depth

/-!
# A1 — primary parts and the assembly step

Helper lemmas for target T7 (`WC_abstract`): the passage from `Sha[p] = 0` to `Sha[p^∞] = 0`,
the primary decomposition of a torsion element, and finiteness of a group covered by finitely
many finite primary parts.
-/

namespace WitnessContent

open scoped BigOperators

section Primary

variable {Sha : Type*} [AddCommGroup Sha]

lemma mem_primaryPart_iff (x : Sha) (p : ℕ) :
    x ∈ primaryPart Sha p ↔ ∃ k : ℕ, p ^ k • x = 0 := Iff.rfl

/-- `Sha[p] = 0` implies `Sha[p^∞] = 0` (KNOWN_TRAPS 6: the implication only goes this way). -/
lemma primaryPart_eq_bot_of_ptorsion_trivial (p : ℕ) (h : ∀ x : Sha, p • x = 0 → x = 0) :
    primaryPart Sha p = ⊥ := by
  ext x
  simp only [AddSubgroup.mem_bot]
  constructor
  · rintro ⟨k, hk⟩
    induction k generalizing x with
    | zero => simpa using hk
    | succ k ih =>
        have hstep : p ^ k • (p • x) = 0 := by
          rw [smul_smul, ← pow_succ]
          exact hk
        exact h x (ih (p • x) hstep)
  · rintro rfl
    exact ⟨0, by simp⟩

/-- Primary decomposition of an element killed by `n ≠ 0`. -/
lemma exists_primary_decomposition (x : Sha) (n : ℕ) (hn : n ≠ 0) (hx : n • x = 0) :
    ∃ μ : ℕ → Sha, (∀ q ∈ n.primeFactors, μ q ∈ primaryPart Sha q) ∧
      ∑ q ∈ n.primeFactors, μ q = x := by
  classical
  set S : Finset ℕ := n.primeFactors with hS
  set q : ℕ → ℤ := fun i => (i : ℤ) ^ (n.factorization i) with hq
  have hcop : (S : Set ℕ).Pairwise (Function.onFun IsCoprime q) := by
    intro i hi j hj hij
    have hip : i.Prime := Nat.prime_of_mem_primeFactors hi
    have hjp : j.Prime := Nat.prime_of_mem_primeFactors hj
    have hcopn : Nat.Coprime (i ^ (n.factorization i)) (j ^ (n.factorization j)) :=
      Nat.Coprime.pow _ _ ((Nat.coprime_primes hip hjp).mpr hij)
    have : IsCoprime ((i ^ (n.factorization i) : ℕ) : ℤ) ((j ^ (n.factorization j) : ℕ) : ℤ) :=
      Int.isCoprime_iff_gcd_eq_one.mpr (by simpa using hcopn)
    simpa [Function.onFun, hq] using this
  have hprod : ∏ i ∈ S, q i = (n : ℤ) := by
    have hnat : ∏ i ∈ S, i ^ (n.factorization i) = n := by
      rw [hS, ← Nat.support_factorization]
      exact Nat.factorization_prod_pow_eq_self hn
    calc ∏ i ∈ S, q i = ((∏ i ∈ S, i ^ (n.factorization i) : ℕ) : ℤ) := by push_cast [hq]; ring
      _ = (n : ℤ) := by rw [hnat]
  have hxmem : x ∈ Submodule.torsionBy ℤ Sha ((n : ℤ)) := by
    rw [Submodule.mem_torsionBy_iff]
    rw [← hx]
    exact natCast_zsmul x n
  rw [← hprod, ← Submodule.iSup_torsionBy_eq_torsionBy_prod hcop] at hxmem
  obtain ⟨μ', hμ'⟩ := (Submodule.mem_iSup_finset_iff_exists_sum _ x).1 hxmem
  refine ⟨fun i => (μ' i : Sha), fun i hi => ?_, hμ'⟩
  have hkill : q i • ((μ' i : Sha)) = 0 := (Submodule.mem_torsionBy_iff _ _).1 (μ' i).2
  refine ⟨n.factorization i, ?_⟩
  have : ((i ^ (n.factorization i) : ℕ) : ℤ) • ((μ' i : Sha)) = 0 := by
    simp [hq] at hkill ⊢
  rw [natCast_zsmul] at this
  exact this

/-- If finitely many finite primary parts cover the group, the group is finite. -/
lemma finite_of_covered_by_primary (T : Finset ℕ)
    (hfin : ∀ p ∈ T, (primaryPart Sha p : Set Sha).Finite)
    (hcover : ∀ x : Sha, ∃ μ : ℕ → Sha, (∀ q ∈ T, μ q ∈ primaryPart Sha q) ∧
      ∑ q ∈ T, μ q = x) : Finite Sha := by
  classical
  haveI : ∀ p : {x // x ∈ T}, Finite ↥(primaryPart Sha (p : ℕ)) := by
    intro p
    exact (hfin (p : ℕ) p.2).to_subtype
  refine Finite.of_surjective
    (f := fun v : (∀ p : {x // x ∈ T}, ↥(primaryPart Sha (p : ℕ))) =>
      ∑ p ∈ T.attach, ((v p : Sha))) ?_
  intro x
  obtain ⟨μ, hμmem, hμsum⟩ := hcover x
  refine ⟨fun p => ⟨μ (p : ℕ), hμmem (p : ℕ) p.2⟩, ?_⟩
  simpa using hμsum ▸ Finset.sum_attach T μ

end Primary

end WitnessContent
