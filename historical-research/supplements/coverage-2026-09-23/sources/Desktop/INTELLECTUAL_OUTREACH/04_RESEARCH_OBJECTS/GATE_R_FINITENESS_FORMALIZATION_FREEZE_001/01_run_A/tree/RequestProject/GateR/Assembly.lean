import RequestProject.Main
import Mathlib.LinearAlgebra.Dimension.Finite

/-
  GATE R — FINAL ASSEMBLY.

  Replace every `sorry` below.  Add nothing else to the public interface: private
  lemmas and local `have`s are unrestricted, but the five theorems below are the
  entire authorised output of this job, with exactly the signatures given.

  Do not modify any other file in this project.  Every other module is frozen and
  already certified; its bytes are part of the acceptance criteria.
-/

namespace GateR

open SDyadic P01 R1

/-- Auxiliary height used only inside this module.  `R1.height` itself is frozen
and must not be redefined. -/
def translateMax {G : Type*} [AddCommGroup G] (T : G) (H : G → ℕ) (P : G) : ℕ :=
  max (H P) (H (P + T))

/-! ### Private scaffolding: finiteness of height sublevels -/

section Finiteness

variable {ε : ℤ} {m q : ℕ}

/-- The coordinates of a point, as an `Option`: the point at infinity is `none`. -/
private def ptCoords : (Ecurve ε m q).toAffine.Point → Option (ℚ × ℚ)
  | .zero => none
  | @WeierstrassCurve.Affine.Point.some _ _ _ x y _ => some (x, y)

private theorem ptCoords_injective :
    Function.Injective (ptCoords (ε := ε) (m := m) (q := q)) := by
  intro P₁ P₂ h
  cases P₁ with
  | zero =>
      cases P₂ with
      | zero => rfl
      | some h₂ => exact absurd h (by simp [ptCoords])
  | @some x₁ y₁ h₁ =>
      cases P₂ with
      | zero => exact absurd h (by simp [ptCoords])
      | @some x₂ y₂ h₂ =>
          simp only [ptCoords, Option.some.injEq, Prod.mk.injEq] at h
          exact P01.Wab_pt_eq h₁ h₂ h.1 h.2

/-- The rationals of bounded height form a finite set. -/
private theorem finite_heightQ_le (n : ℕ) : {x : ℚ | R1.heightQ x ≤ n}.Finite := by
  refine Set.Finite.of_finite_image (f := fun x : ℚ => (x.num, x.den)) ?_ ?_
  · refine Set.Finite.subset
      ((Set.finite_Icc (-(n : ℤ)) (n : ℤ)).prod (Set.finite_Iic n)) ?_
    rintro ⟨a, d⟩ ⟨x, hx, hxe⟩
    have hx1 : x.num.natAbs ≤ n := le_trans (le_max_left _ _) hx
    have hx2 : x.den ≤ n := le_trans (le_max_right _ _) hx
    simp only [Prod.mk.injEq] at hxe
    obtain ⟨rfl, rfl⟩ := hxe
    exact ⟨⟨by omega, by omega⟩, hx2⟩
  · intro x _ y _ h
    simp only [Prod.mk.injEq] at h
    exact Rat.ext h.1 h.2

/-- For a fixed value, the rational square roots form a finite set. -/
private theorem finite_sq_eq (c : ℚ) : {y : ℚ | y ^ 2 = c}.Finite := by
  by_cases hc : ∃ y₀ : ℚ, y₀ ^ 2 = c
  · obtain ⟨y₀, hy₀⟩ := hc
    refine Set.Finite.subset ((Set.finite_singleton (-y₀)).insert y₀) ?_
    intro y hy
    have hy' : y ^ 2 = c := hy
    have : (y - y₀) * (y + y₀) = 0 := by linear_combination hy' - hy₀
    rcases mul_eq_zero.mp this with h | h
    · exact Or.inl (by linarith)
    · exact Or.inr (show y = -y₀ by linarith)
  · have : {y : ℚ | y ^ 2 = c} = ∅ := by
      ext y; simp only [Set.mem_setOf_eq, Set.mem_empty_iff_false, iff_false]
      exact fun hy => hc ⟨y, hy⟩
    rw [this]
    exact Set.finite_empty

end Finiteness

/-- OUTPUT 1. -/
theorem height_sublevels (ε : ℤ) (m q n : ℕ) :
    {P : (P01.Ecurve ε m q).toAffine.Point | R1.height P ≤ n}.Finite := by
  classical
  refine Set.Finite.of_finite_image (f := ptCoords) ?_ (ptCoords_injective.injOn)
  -- the image lies in `{none} ∪ some '' W`, with `W` the bounded coordinate pairs
  set W : Set (ℚ × ℚ) :=
    {p : ℚ × ℚ | R1.heightQ p.1 ≤ n ∧
      p.2 ^ 2 = p.1 ^ 3 + SDyadic.dualA ε m q * p.1 ^ 2 + SDyadic.dualB ε m q * p.1} with hW
  have hWfin : W.Finite := by
    have hsub : W ⊆ ⋃ x ∈ {x : ℚ | R1.heightQ x ≤ n},
        ({x} : Set ℚ) ×ˢ {y : ℚ | y ^ 2 = x ^ 3 + SDyadic.dualA ε m q * x ^ 2 +
          SDyadic.dualB ε m q * x} := by
      rintro ⟨x, y⟩ ⟨h1, h2⟩
      exact Set.mem_biUnion h1 ⟨rfl, h2⟩
    refine Set.Finite.subset (Set.Finite.biUnion (finite_heightQ_le n) ?_) hsub
    intro x _
    exact (Set.finite_singleton x).prod (finite_sq_eq _)
  refine Set.Finite.subset (Set.Finite.insert none (Set.Finite.image some hWfin)) ?_
  rintro v ⟨P, hP, rfl⟩
  cases P with
  | zero => exact Set.mem_insert _ _
  | @some x y h =>
      refine Set.mem_insert_of_mem _ ⟨(x, y), ⟨?_, ?_⟩, rfl⟩
      · exact hP
      · exact (Descent.Wab_equation_iff _ _ x y).mp h.left

/-! ### Private scaffolding: the marked point is not a double -/

section Descent

variable {ε : ℤ} {m q : ℕ} [Fact (Nat.Prime q)]

/-- `[q]` is not in `⟨[D]⟩`: `q` is not a square and `Dq` is not a square. -/
private theorem cls_q_not_mem_KExp (hP : Params ε m q) :
    Run013.cls ((q : ℚ)) ∉ SDyadic.KExp ε m := by
  have hqp : Nat.Prime q := hP.q_prime
  have hq0 : (q : ℤ) ≠ 0 := by exact_mod_cast hqp.ne_zero
  have hD0 : DD ε m ≠ 0 := D_ne_zero ε m
  have hqcast : ((q : ℤ) : ℚ) = ((q : ℕ) : ℚ) := by push_cast; ring
  have hqprime : Prime ((q : ℤ)) := Nat.prime_iff_prime_int.mp hqp
  have hnsq_q : ¬ IsSquare ((q : ℤ)) := by
    refine not_isSquare_of_prime_dvd_once hqprime dvd_rfl ?_
    intro hc
    have h2 : ((q : ℤ)) ^ 2 ≤ (q : ℤ) := Int.le_of_dvd (by positivity) hc
    have hq2 : (2 : ℤ) ≤ (q : ℤ) := by exact_mod_cast hqp.two_le
    nlinarith
  have hnsq_Dq : ¬ IsSquare (DD ε m * (q : ℤ)) := by
    refine not_isSquare_of_prime_dvd_once hqprime ⟨DD ε m, by ring⟩ ?_
    rintro ⟨c, hc⟩
    refine q_not_dvd_D hP ⟨c, ?_⟩
    have : DD ε m * (q : ℤ) = ((q : ℤ) * c) * (q : ℤ) := by rw [hc]; ring
    exact mul_right_cancel₀ hq0 this
  intro hmem
  rw [KExp] at hmem
  rcases mem_closure_singleton_of_sq_eq_one (qsq_sq_eq_one _) hmem with h1 | h1
  · exact cls_ne_one_of_not_isSquare hq0 hnsq_q (by rw [hqcast]; exact h1)
  · refine cls_ne_cls_of_not_isSquare_mul hq0 hD0 ?_ (by rw [hqcast]; exact h1)
    rw [mul_comm]
    exact hnsq_Dq

/-- The descent class of `Q = (q,0) ∈ E'_q(ℚ)` is `[q]`. -/
private theorem delta_Qpt (hP : Params ε m q) :
    Descent.delta (phiA ε m q) (phiB ε m q) (Qpt hP) = Run013.cls ((q : ℚ)) := by
  have hq0 : ((q : ℕ) : ℚ) ≠ 0 := by
    exact_mod_cast hP.q_prime.ne_zero
  exact Descent.delta_some_of_ne (P01.Q_mem hP) hq0

/-- **`T` is not a double.**  If it were, `[q]` would lie in `⟨[D]⟩`. -/
private theorem Tpt_not_mem_twoE (hP : Params ε m q) :
    Tpt hP ∉ P04c.twoE ε m q := by
  intro hmem
  have hT : P03c.dualPhiHom hP (Qpt hP) = Tpt hP := by
    rw [P03c.dualPhiHom_apply]
    exact P03e.dualPhiPoint_Qpt hP
  rw [← hT] at hmem
  obtain ⟨K, hK, hdiff⟩ := (P04c.dualPhi_mem_twoE_iff hP).mp hmem
  have hker : Qpt hP - K ∈ (P04a.deltaHomE' hP).ker := by
    rw [P04a.ker_deltaHomE'_eq_range_phiHom hP]
    exact hdiff
  have hval : P04a.deltaHomE' hP (Qpt hP) = P04a.deltaHomE' hP K := by
    have : P04a.deltaHomE' hP (Qpt hP - K) = 0 := hker
    rw [map_sub, sub_eq_zero] at this
    exact this
  have hQ : P04a.deltaHomE' hP (Qpt hP) = Additive.ofMul (Run013.cls ((q : ℚ))) := by
    rw [P04a.deltaHomE'_apply, delta_Qpt hP]
  refine cls_q_not_mem_KExp hP ?_
  rcases ((P03c.isogeny_kernels ε m q hP).2 K).mp hK with rfl | rfl
  · have h0 : Additive.ofMul (Run013.cls ((q : ℚ))) = (0 : Additive Run013.Qsq) := by
      rw [← hQ, hval, map_zero]
    have : Run013.cls ((q : ℚ)) = 1 := by
      simpa using congrArg Additive.toMul h0
    rw [this]
    exact one_mem _
  · have h1 : Additive.ofMul (Run013.cls ((q : ℚ)))
        = Additive.ofMul (Run013.cls ((DD ε m : ℤ) : ℚ)) := by
      rw [← hQ, hval, P04b.deltaHomE'_T'pt hP]
    have : Run013.cls ((q : ℚ)) = Run013.cls ((DD ε m : ℤ) : ℚ) :=
      Additive.ofMul.injective h1
    rw [this, KExp]
    exact Subgroup.subset_closure rfl

end Descent

/-- OUTPUT 2. -/
theorem halving_representatives (ε : ℤ) (m q : ℕ) [Fact (Nat.Prime q)]
    (hP : SDyadic.Params ε m q) (hH : SDyadic.H41 ε m) :
    ∀ P : (P01.Ecurve ε m q).toAffine.Point,
      ∃ Q : (P01.Ecurve ε m q).toAffine.Point, ∃ e : ℕ,
        e ≤ 1 ∧ P = Q + Q + e • P01.Tpt hP := by
  classical
  obtain ⟨eqv⟩ := P04c.twoE_quotient_equiv_zmod hP hH
  have hT : eqv (QuotientAddGroup.mk (P01.Tpt hP)) ≠ 0 := by
    intro h
    have : (QuotientAddGroup.mk (P01.Tpt hP) :
        (P01.Ecurve ε m q).toAffine.Point ⧸ P04c.twoE ε m q) = 0 := by
      have := congrArg eqv.symm h
      simpa using this
    exact Tpt_not_mem_twoE hP (QuotientAddGroup.eq_zero_iff _ |>.mp this)
  intro P
  by_cases hmem : QuotientAddGroup.mk P = (0 : (P01.Ecurve ε m q).toAffine.Point ⧸ P04c.twoE ε m q)
  · obtain ⟨R, hR⟩ := P04c.mem_twoE.mp ((QuotientAddGroup.eq_zero_iff _).mp hmem)
    exact ⟨R, 0, by norm_num, by rw [hR]; simp⟩
  · -- the quotient has exactly two elements, so `P` and `T` share a class
    have hcl : (QuotientAddGroup.mk P :
        (P01.Ecurve ε m q).toAffine.Point ⧸ P04c.twoE ε m q)
          = QuotientAddGroup.mk (P01.Tpt hP) := by
      have hPne : eqv (QuotientAddGroup.mk P) ≠ 0 := by
        intro h
        exact hmem (by simpa using congrArg eqv.symm h)
      have : eqv (QuotientAddGroup.mk P) = eqv (QuotientAddGroup.mk (P01.Tpt hP)) := by
        revert hPne hT
        generalize eqv (QuotientAddGroup.mk P) = u
        generalize eqv (QuotientAddGroup.mk (P01.Tpt hP)) = v
        revert u v
        decide
      exact eqv.injective this
    have hsub : P - P01.Tpt hP ∈ P04c.twoE ε m q := by
      rw [← QuotientAddGroup.eq_zero_iff]
      rw [show (QuotientAddGroup.mk (P - P01.Tpt hP) :
          (P01.Ecurve ε m q).toAffine.Point ⧸ P04c.twoE ε m q)
          = QuotientAddGroup.mk P - QuotientAddGroup.mk (P01.Tpt hP) from rfl, hcl, sub_self]
    obtain ⟨R, hR⟩ := P04c.mem_twoE.mp hsub
    refine ⟨R, 1, le_refl _, ?_⟩
    rw [hR, one_smul]
    abel

/-- OUTPUT 3. -/
theorem bounded_halving (ε : ℤ) (m q : ℕ) [Fact (Nat.Prime q)]
    (hP : SDyadic.Params ε m q) (hH : SDyadic.H41 ε m) :
    ∃ C : ℕ, 1 ≤ C ∧ ∀ P : (P01.Ecurve ε m q).toAffine.Point,
      ∃ Q : (P01.Ecurve ε m q).toAffine.Point, ∃ e : ℕ,
        e ≤ 1 ∧ P = Q + Q + e • P01.Tpt hP ∧
        translateMax (P01.Tpt hP) R1.height Q ≤
          max (translateMax (P01.Tpt hP) R1.height P) C := by
  obtain ⟨C, hC1, hCdup⟩ := R1.h41_multiplicative_duplication_height ε m q hP hH
  refine ⟨C, hC1, ?_⟩
  intro P
  obtain ⟨Q, e, he, hPQ⟩ := halving_representatives ε m q hP hH P
  refine ⟨Q, e, he, hPQ, ?_⟩
  have hTT : P01.Tpt hP + P01.Tpt hP = 0 :=
    (P01.Ecurve_two_torsion hP _).mpr (Or.inr rfl)
  -- the doubles of `Q` and of `Q + T` are `P` or `P + T`
  have hdouble : (Q + Q = P ∧ (Q + P01.Tpt hP) + (Q + P01.Tpt hP) = P) ∨
      (Q + Q = P + P01.Tpt hP ∧ (Q + P01.Tpt hP) + (Q + P01.Tpt hP) = P + P01.Tpt hP) := by
    interval_cases e
    · left
      constructor
      · rw [hPQ, zero_nsmul, add_zero]
      · rw [hPQ]; simp only [zero_nsmul, add_zero]
        rw [show Q + P01.Tpt hP + (Q + P01.Tpt hP)
          = Q + Q + (P01.Tpt hP + P01.Tpt hP) by abel, hTT, add_zero]
    · right
      constructor
      · rw [hPQ, one_nsmul]
        rw [show Q + Q + P01.Tpt hP + P01.Tpt hP
          = Q + Q + (P01.Tpt hP + P01.Tpt hP) by abel, hTT, add_zero]
      · rw [hPQ, one_nsmul]
        rw [show Q + P01.Tpt hP + (Q + P01.Tpt hP)
          = Q + Q + (P01.Tpt hP + P01.Tpt hP) by abel, hTT, add_zero,
          show Q + Q + P01.Tpt hP + P01.Tpt hP
          = Q + Q + (P01.Tpt hP + P01.Tpt hP) by abel, hTT, add_zero]
  -- hence `translateMax Q ^ 4 ≤ C * translateMax P`
  have hkey : translateMax (P01.Tpt hP) R1.height Q ^ 4
      ≤ C * translateMax (P01.Tpt hP) R1.height P := by
    have h1 := hCdup Q
    have h2 := hCdup (Q + P01.Tpt hP)
    rcases hdouble with ⟨hd1, hd2⟩ | ⟨hd1, hd2⟩
    · rw [hd1] at h1; rw [hd2] at h2
      have : max (R1.height Q) (R1.height (Q + P01.Tpt hP)) ^ 4 ≤ C * R1.height P := by
        rcases max_cases (R1.height Q) (R1.height (Q + P01.Tpt hP)) with ⟨hm, -⟩ | ⟨hm, -⟩ <;>
          rw [hm]
        · exact h1
        · exact h2
      refine le_trans this (Nat.mul_le_mul_left _ ?_)
      exact le_max_left _ _
    · rw [hd1] at h1; rw [hd2] at h2
      have : max (R1.height Q) (R1.height (Q + P01.Tpt hP)) ^ 4
          ≤ C * R1.height (P + P01.Tpt hP) := by
        rcases max_cases (R1.height Q) (R1.height (Q + P01.Tpt hP)) with ⟨hm, -⟩ | ⟨hm, -⟩ <;>
          rw [hm]
        · exact h1
        · exact h2
      refine le_trans this (Nat.mul_le_mul_left _ ?_)
      exact le_max_right _ _
  -- and `h^4 ≤ C * M` with `h ≥ 1` forces `h ≤ max M C`
  by_contra hcon
  push_neg at hcon
  have hMlt : translateMax (P01.Tpt hP) R1.height P < translateMax (P01.Tpt hP) R1.height Q :=
    lt_of_le_of_lt (le_max_left _ _) hcon
  have hClt : C < translateMax (P01.Tpt hP) R1.height Q :=
    lt_of_le_of_lt (le_max_right _ _) hcon
  have h1Q : 1 ≤ translateMax (P01.Tpt hP) R1.height Q :=
    le_trans (R1.one_le_height Q) (le_max_left _ _)
  set h := translateMax (P01.Tpt hP) R1.height Q
  set M := translateMax (P01.Tpt hP) R1.height P
  have hstep : h ^ 4 ≤ C * M := hkey
  have hsq : h ^ 2 ≤ h ^ 4 := Nat.pow_le_pow_right h1Q (by norm_num)
  have hsq' : h * h ≤ h ^ 4 := by rw [← sq]; exact hsq
  nlinarith [hstep, hsq', hClt, hMlt]

/-- OUTPUT 4. -/
theorem every_point_torsion (ε : ℤ) (m q : ℕ) [Fact (Nat.Prime q)]
    (hP : SDyadic.Params ε m q) (hH : SDyadic.H41 ε m) :
    ∀ P : (P01.Ecurve ε m q).toAffine.Point, ∃ n : ℕ, 0 < n ∧ n • P = 0 := by
  obtain ⟨C, -, hbd⟩ := bounded_halving ε m q hP hH
  have hTT : P01.Tpt hP + P01.Tpt hP = 0 :=
    (P01.Ecurve_two_torsion hP _).mpr (Or.inr rfl)
  refine R0.properHeightTwoDescentTorsion (P01.Tpt hP) hTT
    (translateMax (P01.Tpt hP) R1.height) C ?_ hbd
  intro n
  refine Set.Finite.subset (height_sublevels ε m q n) ?_
  intro P hp
  simp only [Set.mem_setOf_eq, translateMax] at hp ⊢
  exact le_trans (le_max_left _ _) hp

/-- OUTPUT 5.  The endpoint.  `Module.rank ℤ` is mathlib's cardinal-valued module
rank on the actual rational point group.  Do not weaken it to `Module.finrank`,
`Group.rank`, `AddGroup.rank`, or a statement about any other group. -/
theorem h41_rank_zero (ε : ℤ) (m q : ℕ) [Fact (Nat.Prime q)]
    (hP : SDyadic.Params ε m q) (hH : SDyadic.H41 ε m) :
    Module.rank ℤ (P01.Ecurve ε m q).toAffine.Point = (0 : Cardinal) := by
  rw [rank_eq_zero_iff]
  intro P
  obtain ⟨n, hn, hnP⟩ := every_point_torsion ε m q hP hH P
  refine ⟨(n : ℤ), by exact_mod_cast hn.ne', ?_⟩
  rw [← hnP, natCast_zsmul]

end GateR
