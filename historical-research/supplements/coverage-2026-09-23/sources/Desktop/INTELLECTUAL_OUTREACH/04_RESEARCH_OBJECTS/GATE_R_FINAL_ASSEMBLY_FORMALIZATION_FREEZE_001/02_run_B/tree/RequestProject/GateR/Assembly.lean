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

/-! ### Private support for OUTPUT 1 -/

/-- Rationals of bounded height form a finite set: both numerator and denominator are
bounded, and a rational is determined by that pair. -/
private theorem finite_heightQ_le (n : ℕ) : {x : ℚ | R1.heightQ x ≤ n}.Finite := by
  refine Set.Finite.of_finite_image (f := fun x : ℚ => (x.num, x.den)) ?_ ?_
  · refine Set.Finite.subset
      (Set.Finite.prod (Set.finite_Icc (-(n : ℤ)) (n : ℤ)) (Set.finite_Iic n)) ?_
    rintro ⟨a, b⟩ ⟨x, hx, hxab⟩
    simp only [Set.mem_setOf_eq, R1.heightQ] at hx
    have h1 : x.num.natAbs ≤ n := le_trans (le_max_left _ _) hx
    have h2 : x.den ≤ n := le_trans (le_max_right _ _) hx
    obtain ⟨rfl, rfl⟩ : a = x.num ∧ b = x.den := by
      constructor
      · exact (congrArg Prod.fst hxab).symm
      · exact (congrArg Prod.snd hxab).symm
    refine Set.mem_prod.mpr ⟨?_, ?_⟩
    · simp only [Set.mem_Icc]
      omega
    · exact Set.mem_Iic.mpr h2
  · intro x _ y _ h
    exact Rat.ext (congrArg Prod.fst h) (congrArg Prod.snd h)

open WeierstrassCurve in
/-- A point of the affine model, coded by its `x`-coordinate together with the sign of its
`y`-coordinate.  The code determines the point. -/
private noncomputable def pcode {ε : ℤ} {m q : ℕ} :
    (P01.Ecurve ε m q).toAffine.Point → Option (ℚ × Bool)
  | .zero => none
  | @Affine.Point.some _ _ _ x y _ => some (x, decide (0 ≤ y))

open WeierstrassCurve in
private theorem pcode_injective {ε : ℤ} {m q : ℕ} :
    Function.Injective (@pcode ε m q) := by
  intro P₁ P₂ h
  cases P₁ with
  | zero =>
      cases P₂ with
      | zero => rfl
      | some h₂ => exact absurd h (by simp [pcode])
  | @some x₁ y₁ h₁ =>
      cases P₂ with
      | zero => exact absurd h (by simp [pcode])
      | @some x₂ y₂ h₂ =>
          simp only [pcode, Option.some.injEq, Prod.mk.injEq, decide_eq_decide] at h
          obtain ⟨hx, hsign⟩ := h
          subst hx
          have e₁ : y₁ ^ 2 = x₁ ^ 3 + dualA ε m q * x₁ ^ 2 + dualB ε m q * x₁ :=
            (Descent.Wab_equation_iff _ _ x₁ y₁).mp h₁.left
          have e₂ : y₂ ^ 2 = x₁ ^ 3 + dualA ε m q * x₁ ^ 2 + dualB ε m q * x₁ :=
            (Descent.Wab_equation_iff _ _ x₁ y₂).mp h₂.left
          have hfac : (y₁ - y₂) * (y₁ + y₂) = 0 := by linear_combination e₁ - e₂
          have hy : y₁ = y₂ := by
            rcases mul_eq_zero.mp hfac with h0 | h0
            · linarith
            · by_cases hp : (0 : ℚ) ≤ y₁
              · have : (0 : ℚ) ≤ y₂ := hsign.mp hp
                linarith
              · have : ¬ (0 : ℚ) ≤ y₂ := fun hc => hp (hsign.mpr hc)
                push_neg at hp this
                linarith
          exact Wab_pt_eq h₁ h₂ rfl hy

/-! ### OUTPUT 1 -/

/-- OUTPUT 1. -/
theorem height_sublevels (ε : ℤ) (m q n : ℕ) :
    {P : (P01.Ecurve ε m q).toAffine.Point | R1.height P ≤ n}.Finite := by
  refine Set.Finite.of_finite_image (f := @pcode ε m q) ?_
    (Function.Injective.injOn pcode_injective)
  refine Set.Finite.subset
    (Set.Finite.insert none
      (Set.Finite.image Option.some
        (Set.Finite.prod (finite_heightQ_le n) (Set.finite_univ (α := Bool))))) ?_
  rintro c ⟨P, hP, rfl⟩
  cases P with
  | zero => exact Set.mem_insert _ _
  | @some x y h =>
      refine Set.mem_insert_of_mem _ ⟨(x, decide (0 ≤ y)), ?_, rfl⟩
      refine Set.mem_prod.mpr ⟨?_, Set.mem_univ _⟩
      simpa [R1.height] using hP

/-! ### Private support for OUTPUT 2

The marked point `T = (0,0)` is not a double.  Under the certified identifications it is
`φ̂(Q)` with `Q = (q,0)`, so its class in `E_q(ℚ)/2E_q(ℚ)` is trivial exactly when the square
class of `q` lies in `KExp = ⟨[D]⟩`, which it does not. -/

private theorem cls_q_not_mem_KExp {ε : ℤ} {m q : ℕ} [Fact (Nat.Prime q)]
    (hP : Params ε m q) : Run013.cls ((q : ℕ) : ℚ) ∉ KExp ε m := by
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
    have hcc : DD ε m * (q : ℤ) = ((q : ℤ) * c) * (q : ℤ) := by rw [hc]; ring
    exact mul_right_cancel₀ hq0 hcc
  intro hmem
  rw [KExp] at hmem
  rcases mem_closure_singleton_of_sq_eq_one (qsq_sq_eq_one _) hmem with h1 | h1
  · exact cls_ne_one_of_not_isSquare hq0 hnsq_q (by rw [hqcast]; exact h1)
  · refine cls_ne_cls_of_not_isSquare_mul hq0 hD0 ?_ (by rw [hqcast]; exact h1)
    rw [mul_comm]
    exact hnsq_Dq

private theorem Tpt_add_self {ε : ℤ} {m q : ℕ} [Fact (Nat.Prime q)] (hP : Params ε m q) :
    Tpt hP + Tpt hP = 0 :=
  (Wab_two_torsion_some (T_mem hP)).mpr rfl

private theorem Tpt_not_mem_twoE {ε : ℤ} {m q : ℕ} [Fact (Nat.Prime q)]
    (hP : Params ε m q) (hH : H41 ε m) : Tpt hP ∉ P04c.twoE ε m q := by
  intro hmem
  have hq0 : ((q : ℕ) : ℚ) ≠ 0 := by
    have := hP.q_pos
    exact_mod_cast this.ne'
  have hdelta : Descent.delta (phiA ε m q) (phiB ε m q) (Qpt hP) = Run013.cls ((q : ℕ) : ℚ) :=
    Descent.delta_some_of_ne (Q_mem hP) hq0
  have h1 : P04c.dualQuotHom hP (Qpt hP) = 0 := by
    rw [P04c.dualQuotHom_apply, QuotientAddGroup.eq_zero_iff, P03c.dualPhiHom_apply,
      P03e.dualPhiPoint_Qpt]
    exact hmem
  have h2 : Qpt hP ∈ (P04c.gphiQuotHom hP hH).ker := by
    rw [← P04c.ker_dualQuotHom_eq_ker_gphiQuotHom hP hH]
    exact h1
  have h3 := (P04c.mem_ker_gphiQuotHom hP hH _).mp h2
  rw [hdelta] at h3
  exact cls_q_not_mem_KExp hP h3

/-! ### OUTPUT 2 -/

/-- OUTPUT 2. -/
theorem halving_representatives (ε : ℤ) (m q : ℕ) [Fact (Nat.Prime q)]
    (hP : SDyadic.Params ε m q) (hH : SDyadic.H41 ε m) :
    ∀ P : (P01.Ecurve ε m q).toAffine.Point,
      ∃ Q : (P01.Ecurve ε m q).toAffine.Point, ∃ e : ℕ,
        e ≤ 1 ∧ P = Q + Q + e • P01.Tpt hP := by
  intro P
  by_cases hmem : P ∈ P04c.twoE ε m q
  · obtain ⟨R, hR⟩ := P04c.mem_twoE.mp hmem
    exact ⟨R, 0, Nat.zero_le 1, by rw [zero_nsmul, add_zero, hR]⟩
  · -- `P` and `T` both have nontrivial class in a quotient of order two, hence equal classes
    obtain ⟨eqv⟩ := P04c.twoE_quotient_equiv_zmod hP hH
    have hPne : (QuotientAddGroup.mk P : (P01.Ecurve ε m q).toAffine.Point ⧸ P04c.twoE ε m q)
        ≠ 0 := by
      rw [Ne, QuotientAddGroup.eq_zero_iff]
      exact hmem
    have hTne : (QuotientAddGroup.mk (Tpt hP) :
        (P01.Ecurve ε m q).toAffine.Point ⧸ P04c.twoE ε m q) ≠ 0 := by
      rw [Ne, QuotientAddGroup.eq_zero_iff]
      exact Tpt_not_mem_twoE hP hH
    have hzmod : ∀ z : ZMod 2, z ≠ 0 → z = 1 := by decide
    have hP1 : eqv (QuotientAddGroup.mk P) = 1 :=
      hzmod _ (fun hc => hPne (eqv.injective (by rw [hc, map_zero])))
    have hT1 : eqv (QuotientAddGroup.mk (Tpt hP)) = 1 :=
      hzmod _ (fun hc => hTne (eqv.injective (by rw [hc, map_zero])))
    have heq : (QuotientAddGroup.mk P : (P01.Ecurve ε m q).toAffine.Point ⧸ P04c.twoE ε m q)
        = QuotientAddGroup.mk (Tpt hP) := eqv.injective (by rw [hP1, hT1])
    have hsub : P - Tpt hP ∈ P04c.twoE ε m q :=
      QuotientAddGroup.eq_iff_sub_mem.mp heq
    obtain ⟨R, hR⟩ := P04c.mem_twoE.mp hsub
    refine ⟨R, 1, le_refl 1, ?_⟩
    rw [one_nsmul, hR, sub_add_cancel]

/-! ### Private support for OUTPUT 3 -/

private theorem le_max_of_pow_four_le {h C M : ℕ} (hM : 1 ≤ M)
    (hle : h ^ 4 ≤ C * M) : h ≤ max M C := by
  by_contra hcon
  push_neg at hcon
  have h1 : C ≤ max M C := le_max_right _ _
  have h2 : M ≤ max M C := le_max_left _ _
  have hK1 : 1 ≤ max M C := le_trans hM h2
  have hCM : C * M ≤ max M C * max M C := Nat.mul_le_mul h1 h2
  have hlt : max M C * max M C < h * h := Nat.mul_lt_mul_of_lt_of_le hcon (le_of_lt hcon) (by omega)
  have hsq : h * h ≤ h ^ 4 := by
    have h4 : h ^ 2 ≤ h ^ 4 := Nat.pow_le_pow_right (by omega) (by norm_num)
    calc h * h = h ^ 2 := (sq h).symm
      _ ≤ h ^ 4 := h4
  omega

/-! ### OUTPUT 3 -/

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
  set T := Tpt hP with hT
  set M := translateMax T R1.height P with hM
  have hMP : R1.height P ≤ M := le_max_left _ _
  have hMPT : R1.height (P + T) ≤ M := le_max_right _ _
  have hM1 : 1 ≤ M := le_trans (R1.one_le_height P) hMP
  -- the double of `Q` is either `P` or `P + T`, so its height is at most `M`
  have hQQ : R1.height (Q + Q) ≤ M := by
    interval_cases e
    · rw [zero_nsmul, add_zero] at hPQ
      rw [← hPQ]
      exact hMP
    · have : Q + Q = P + T := by
        rw [hPQ, one_nsmul]
        rw [add_assoc, add_assoc, Tpt_add_self hP, add_zero]
      rw [this]
      exact hMPT
  -- `Q + T` halves the same point
  have hQT : (Q + T) + (Q + T) = Q + Q := by
    have : (Q + T) + (Q + T) = Q + Q + (T + T) := by abel
    rw [this, Tpt_add_self hP, add_zero]
  have hbQ : R1.height Q ≤ max M C :=
    le_max_of_pow_four_le hM1 (le_trans (hCdup Q) (Nat.mul_le_mul_left C hQQ))
  have hbQT : R1.height (Q + T) ≤ max M C := by
    refine le_max_of_pow_four_le hM1 (le_trans (hCdup (Q + T)) ?_)
    rw [hQT]
    exact Nat.mul_le_mul_left C hQQ
  exact ⟨Q, e, he, hPQ, max_le hbQ hbQT⟩

/-! ### OUTPUT 4 -/

/-- OUTPUT 4. -/
theorem every_point_torsion (ε : ℤ) (m q : ℕ) [Fact (Nat.Prime q)]
    (hP : SDyadic.Params ε m q) (hH : SDyadic.H41 ε m) :
    ∀ P : (P01.Ecurve ε m q).toAffine.Point, ∃ n : ℕ, 0 < n ∧ n • P = 0 := by
  obtain ⟨C, hC1, hhalve⟩ := bounded_halving ε m q hP hH
  refine R0.properHeightTwoDescentTorsion (Tpt hP) (Tpt_add_self hP)
    (translateMax (Tpt hP) R1.height) C ?_ ?_
  · intro n
    refine Set.Finite.subset (height_sublevels ε m q n) ?_
    intro P hPn
    simp only [Set.mem_setOf_eq, translateMax] at hPn ⊢
    exact le_trans (le_max_left _ _) hPn
  · intro P
    obtain ⟨Q, e, he, hPQ, hbound⟩ := hhalve P
    exact ⟨Q, e, he, hPQ, hbound⟩

/-! ### OUTPUT 5 -/

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
  rw [← Nat.cast_smul_eq_nsmul ℤ n P] at hnP
  exact hnP

end GateR
