import Mathlib

namespace R0

/-! # TARGET R0 — `ProperHeightTwoDescentTorsion`

**SECONDARY / FALLBACK target of this packet.**  Purely abstract: no elliptic curve, no
`RequestProject` import, nothing from the frozen chain.  It is deliberately independent of R1 so
that it can be attempted whether R1 succeeds or blocks.

    G an additive commutative group,  T : G with T + T = 0,  h : G → ℕ,  B : ℕ
    (1) every sublevel set {P | h P ≤ n} is finite
    (2) every P is P = Q + Q + e • T with e ∈ {0,1} and h Q ≤ max (h P) B
    ⟹ every P : G has finite additive order.

## Boundary — read before starting

Hypothesis (2) is the arithmetic gate, and **this theorem does not establish it for anything.**
Proving R0 does **not** discharge the `H₄₁` height hypotheses and does **not** contribute a step
towards rank zero on its own. Any report that says otherwise is wrong. The companion target R1 is
where the actual arithmetic lives.

Forbidden as premises: `Finite G`, `Fintype G`, `AddGroup.FG G`, `Module.Finite ℤ G`, finite
rational rank, any existing rank-zero theorem, and any premise already asserting that elements are
torsion.

The torsion conclusion is **mandatory**. A bare natural-valued `finrank = 0` is not an acceptable
substitute, because it collapses infinite cardinal rank to zero. If `IsOfFinAddOrder` is the
cleanest API at this pin, use it — verify the exact spelling rather than assuming it.
-/

/--
**TARGET R0 — `ProperHeightTwoDescentTorsion`.  SECONDARY.**

Stated with the explicit `∃ n > 0, n • P = 0` conclusion. Restating it as `IsOfFinAddOrder P`, or
adding that as a corollary, is welcome provided this form is also proved. -/
theorem properHeightTwoDescentTorsion
    {G : Type*} [AddCommGroup G] (T : G) (hT : T + T = 0)
    (h : G → ℕ) (B : ℕ)
    (hfin : ∀ n : ℕ, {P : G | h P ≤ n}.Finite)
    (hhalve : ∀ P : G, ∃ Q : G, ∃ e : ℕ, e ≤ 1 ∧ P = Q + Q + e • T ∧ h Q ≤ max (h P) B) :
    ∀ P : G, ∃ n : ℕ, 0 < n ∧ n • P = 0 := by
  -- a choice of halving
  choose g e _he hstep hheight using hhalve
  have hT2 : ∀ c : ℕ, (2 * c) • T = 0 := by
    intro c
    rw [mul_comm, mul_smul, two_nsmul, hT, smul_zero]
  intro P
  -- iterate the halving; all iterates stay in one sublevel set
  set f : ℕ → G := fun n => g^[n] P with hf
  have hf0 : f 0 = P := rfl
  have hfsucc : ∀ n, f (n + 1) = g (f n) := by
    intro n
    simp [hf, Function.iterate_succ_apply']
  have hbound : ∀ n, h (f n) ≤ max (h P) B := by
    intro n
    induction n with
    | zero => exact le_max_left _ _
    | succ k ih =>
        rw [hfsucc]
        exact le_trans (hheight (f k)) (max_le ih (le_max_right _ _))
  -- finiteness of the sublevel set forces a repetition
  have hmaps : Set.MapsTo f Set.univ {Q : G | h Q ≤ max (h P) B} := fun n _ => hbound n
  obtain ⟨n, -, m, -, hnm, hfnm⟩ :=
    Set.infinite_univ.exists_ne_map_eq_of_mapsTo hmaps (hfin (max (h P) B))
  -- unwinding the halvings: `P = 2ᵏ • f k + c • T`
  have hdesc : ∀ k : ℕ, ∃ c : ℕ, P = (2 ^ k) • f k + c • T := by
    intro k
    induction k with
    | zero => exact ⟨0, by simp [hf0]⟩
    | succ j ih =>
        obtain ⟨c, hc⟩ := ih
        refine ⟨c + 2 ^ j * e (f j), ?_⟩
        set E : ℕ := e (f j) with hE
        have hfj : f j = f (j + 1) + f (j + 1) + E • T := by
          rw [hfsucc]
          exact hstep (f j)
        rw [hc, hfj]
        match_scalars <;> ring
  -- doubling annihilates the `T`-component
  have key : ∀ (k c : ℕ) (X : G), P = 2 ^ k • X + c • T → (2 : ℕ) • P = 2 ^ (k + 1) • X := by
    intro k c X hPk
    rw [hPk, smul_add, smul_smul, smul_smul, pow_succ, mul_comm (2 ^ k) 2, hT2 c, add_zero]
  obtain ⟨cn, hcn⟩ := hdesc n
  obtain ⟨cm, hcm⟩ := hdesc m
  have h2n : (2 : ℕ) • P = 2 ^ (n + 1) • f m := by
    rw [← hfnm]
    exact key n cn (f n) hcn
  have h2m : (2 : ℕ) • P = 2 ^ (m + 1) • f m := key m cm (f m) hcm
  -- hence two different powers of two annihilate the same multiple of `P`
  have e1 : 2 ^ (m + 1) • P = (2 ^ m * 2 ^ (n + 1)) • f m := by
    rw [pow_succ, mul_comm (2 ^ m) 2, mul_comm 2 (2 ^ m), mul_smul, h2n, smul_smul]
  have e2 : 2 ^ (n + 1) • P = (2 ^ n * 2 ^ (m + 1)) • f m := by
    rw [pow_succ, mul_comm (2 ^ n) 2, mul_comm 2 (2 ^ n), mul_smul, h2m, smul_smul]
  have hkey : 2 ^ (m + 1) • P = 2 ^ (n + 1) • P := by
    rw [e1, e2]
    congr 1
    ring
  -- cancel to produce a positive annihilator
  have cancel : ∀ a b : ℕ, b < a → a • P = b • P → ∃ k : ℕ, 0 < k ∧ k • P = 0 := by
    intro a b hba heq
    refine ⟨a - b, by omega, ?_⟩
    have h1 : b • P + (a - b) • P = b • P := by
      rw [← add_smul, show b + (a - b) = a by omega]
      exact heq
    exact left_eq_add.mp h1.symm
  rcases lt_or_gt_of_ne hnm with hlt | hlt
  · exact cancel (2 ^ (m + 1)) (2 ^ (n + 1))
      (Nat.pow_lt_pow_right one_lt_two (by omega)) hkey
  · exact cancel (2 ^ (n + 1)) (2 ^ (m + 1))
      (Nat.pow_lt_pow_right one_lt_two (by omega)) hkey.symm

/-- The same conclusion in mathlib's `IsOfFinAddOrder` form. -/
theorem isOfFinAddOrder_of_properHeightTwoDescent
    {G : Type*} [AddCommGroup G] (T : G) (hT : T + T = 0)
    (h : G → ℕ) (B : ℕ)
    (hfin : ∀ n : ℕ, {P : G | h P ≤ n}.Finite)
    (hhalve : ∀ P : G, ∃ Q : G, ∃ e : ℕ, e ≤ 1 ∧ P = Q + Q + e • T ∧ h Q ≤ max (h P) B) :
    ∀ P : G, IsOfFinAddOrder P := by
  intro P
  exact isOfFinAddOrder_iff_nsmul_eq_zero.mpr
    (properHeightTwoDescentTorsion T hT h B hfin hhalve P)

end R0
