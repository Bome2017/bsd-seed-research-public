import RequestProject.GateR.Assembly

/-
  ONE TARGET.  Replace the single `sorry` below.

  Every other file in this project is frozen and already certified, INCLUDING
  `RequestProject/GateR/Assembly.lean`.  Do not modify any of them, and do not
  reprove anything they contain.

  The inputs you need are already theorems.  Find them and use them.
-/

namespace GateRFinite

open SDyadic P01 R1

/-! ### Private scaffolding

The certified inputs used below are, all of them already theorems of this tree:

* `R1.h41_multiplicative_duplication_height`  (the duplication height inequality),
* `GateR.height_sublevels`                    (finiteness of height sublevel sets),
* `GateR.halving_representatives`             (`P = Q + Q + e • T`, `e ≤ 1`),
* `GateR.every_point_torsion`                 (every rational point is torsion),
* `P01.Ecurve_two_torsion`, `R1.one_le_height`.

Nothing here is a restatement of a frozen theorem: the frozen statements are cited,
and the only new content is the strict height descent and the closure argument. -/

section Scaffolding

variable {ε : ℤ} {m q : ℕ} [Fact (Nat.Prime q)]

/-- The translate-max height of the frozen assembly, specialised to the marked point. -/
private noncomputable def hgt (hP : Params ε m q) :
    (Ecurve ε m q).toAffine.Point → ℕ :=
  GateR.translateMax (P01.Tpt hP) R1.height

private theorem hgt_eq (hP : Params ε m q) (P : (Ecurve ε m q).toAffine.Point) :
    hgt hP P = max (R1.height P) (R1.height (P + P01.Tpt hP)) := rfl

private theorem one_le_hgt (hP : Params ε m q) (P : (Ecurve ε m q).toAffine.Point) :
    1 ≤ hgt hP P :=
  le_trans (R1.one_le_height P) (le_max_left _ _)

/-- Sublevel sets of the translate-max height are finite, since they sit inside the
certified sublevel sets of `R1.height`. -/
private theorem hgt_sublevel_finite (hP : Params ε m q) (n : ℕ) :
    {P : (Ecurve ε m q).toAffine.Point | hgt hP P ≤ n}.Finite := by
  refine Set.Finite.subset (GateR.height_sublevels ε m q n) ?_
  intro P hp
  simp only [Set.mem_setOf_eq, hgt_eq] at hp ⊢
  exact le_trans (le_max_left _ _) hp

/-- The quartic duplication bound, transported to the translate-max height. -/
private theorem hgt_pow_four_le (hP : Params ε m q) (C : ℕ)
    (hC : ∀ P : (Ecurve ε m q).toAffine.Point, R1.height P ^ 4 ≤ C * R1.height (P + P))
    (P Q : (Ecurve ε m q).toAffine.Point) (e : ℕ) (he : e ≤ 1)
    (hPQ : P = Q + Q + e • P01.Tpt hP) :
    hgt hP Q ^ 4 ≤ C * hgt hP P := by
  have hTT : P01.Tpt hP + P01.Tpt hP = 0 :=
    (P01.Ecurve_two_torsion hP _).mpr (Or.inr rfl)
  have hdouble : (Q + Q = P ∧ (Q + P01.Tpt hP) + (Q + P01.Tpt hP) = P) ∨
      (Q + Q = P + P01.Tpt hP ∧
        (Q + P01.Tpt hP) + (Q + P01.Tpt hP) = P + P01.Tpt hP) := by
    interval_cases e
    · refine Or.inl ⟨by rw [hPQ, zero_nsmul, add_zero], ?_⟩
      rw [hPQ]
      simp only [zero_nsmul, add_zero]
      rw [show Q + P01.Tpt hP + (Q + P01.Tpt hP)
        = Q + Q + (P01.Tpt hP + P01.Tpt hP) by abel, hTT, add_zero]
    · refine Or.inr ⟨?_, ?_⟩
      · rw [hPQ, one_nsmul,
          show Q + Q + P01.Tpt hP + P01.Tpt hP
            = Q + Q + (P01.Tpt hP + P01.Tpt hP) by abel, hTT, add_zero]
      · rw [hPQ, one_nsmul,
          show Q + P01.Tpt hP + (Q + P01.Tpt hP)
            = Q + Q + (P01.Tpt hP + P01.Tpt hP) by abel, hTT, add_zero,
          show Q + Q + P01.Tpt hP + P01.Tpt hP
            = Q + Q + (P01.Tpt hP + P01.Tpt hP) by abel, hTT, add_zero]
  have h1 := hC Q
  have h2 := hC (Q + P01.Tpt hP)
  rw [hgt_eq, hgt_eq]
  rcases hdouble with ⟨hd1, hd2⟩ | ⟨hd1, hd2⟩
  · rw [hd1] at h1; rw [hd2] at h2
    have hmax : max (R1.height Q) (R1.height (Q + P01.Tpt hP)) ^ 4 ≤ C * R1.height P := by
      rcases max_cases (R1.height Q) (R1.height (Q + P01.Tpt hP)) with ⟨hm, -⟩ | ⟨hm, -⟩ <;>
        rw [hm]
      · exact h1
      · exact h2
    exact le_trans hmax (Nat.mul_le_mul_left _ (le_max_left _ _))
  · rw [hd1] at h1; rw [hd2] at h2
    have hmax : max (R1.height Q) (R1.height (Q + P01.Tpt hP)) ^ 4
        ≤ C * R1.height (P + P01.Tpt hP) := by
      rcases max_cases (R1.height Q) (R1.height (Q + P01.Tpt hP)) with ⟨hm, -⟩ | ⟨hm, -⟩ <;>
        rw [hm]
      · exact h1
      · exact h2
    exact le_trans hmax (Nat.mul_le_mul_left _ (le_max_right _ _))

/-- **Strict descent.**  Every point is `Q + Q + e • T` with `e ≤ 1` and with the height
of `Q` either bounded by the absolute constant `C`, or strictly smaller than that of `P`. -/
private theorem strict_descent (hP : Params ε m q) (hH : H41 ε m) :
    ∃ C : ℕ, 1 ≤ C ∧ ∀ P : (Ecurve ε m q).toAffine.Point,
      ∃ Q : (Ecurve ε m q).toAffine.Point, ∃ e : ℕ,
        e ≤ 1 ∧ P = Q + Q + e • P01.Tpt hP ∧
          (hgt hP Q ≤ C ∨ hgt hP Q < hgt hP P) := by
  obtain ⟨C, hC1, hCdup⟩ := R1.h41_multiplicative_duplication_height ε m q hP hH
  refine ⟨C, hC1, fun P => ?_⟩
  obtain ⟨Q, e, he, hPQ⟩ := GateR.halving_representatives ε m q hP hH P
  refine ⟨Q, e, he, hPQ, ?_⟩
  by_contra hcon
  push_neg at hcon
  obtain ⟨hCQ, hPQle⟩ := hcon
  have hkey : hgt hP Q ^ 4 ≤ C * hgt hP P := hgt_pow_four_le hP C hCdup P Q e he hPQ
  have h1Q : 1 ≤ hgt hP Q := one_le_hgt hP Q
  have hsq : hgt hP Q ^ 2 ≤ hgt hP Q ^ 4 := Nat.pow_le_pow_right h1Q (by norm_num)
  have hsq' : hgt hP Q * hgt hP Q ≤ hgt hP Q ^ 4 := by rw [← sq]; exact hsq
  nlinarith [hkey, hsq', hCQ, hPQle, h1Q, hC1]

/-- The whole point group is generated by a finite set: the bounded points together with
the marked point.  This is the classical descent, run on the certified inputs. -/
private theorem closure_eq_top (hP : Params ε m q) (hH : H41 ε m) :
    ∃ S : Set ((Ecurve ε m q).toAffine.Point),
      S.Finite ∧ AddSubgroup.closure S = ⊤ := by
  obtain ⟨C, -, hdesc⟩ := strict_descent hP hH
  refine ⟨{P : (Ecurve ε m q).toAffine.Point | hgt hP P ≤ C} ∪ {P01.Tpt hP},
    (hgt_sublevel_finite hP C).union (Set.finite_singleton _), ?_⟩
  set S : Set ((Ecurve ε m q).toAffine.Point) :=
    {P : (Ecurve ε m q).toAffine.Point | hgt hP P ≤ C} ∪ {P01.Tpt hP} with hS
  have hTmem : P01.Tpt hP ∈ AddSubgroup.closure S :=
    AddSubgroup.subset_closure (Or.inr rfl)
  have hbdd : ∀ R : (Ecurve ε m q).toAffine.Point, hgt hP R ≤ C →
      R ∈ AddSubgroup.closure S :=
    fun R hR => AddSubgroup.subset_closure (Or.inl hR)
  have key : ∀ n : ℕ, ∀ P : (Ecurve ε m q).toAffine.Point, hgt hP P = n →
      P ∈ AddSubgroup.closure S := by
    intro n
    induction n using Nat.strong_induction_on with
    | _ n ih =>
        intro P hPn
        by_cases hPC : hgt hP P ≤ C
        · exact hbdd P hPC
        · obtain ⟨Q, e, -, hPQ, hQ⟩ := hdesc P
          have hQmem : Q ∈ AddSubgroup.closure S := by
            rcases hQ with hQ | hQ
            · exact hbdd Q hQ
            · exact ih (hgt hP Q) (by omega) Q rfl
          rw [hPQ]
          exact AddSubgroup.add_mem _ (AddSubgroup.add_mem _ hQmem hQmem)
            (AddSubgroup.nsmul_mem _ hTmem e)
  refine eq_top_iff.mpr fun P _ => ?_
  exact key (hgt hP P) P rfl

end Scaffolding

/-- THE ONLY AUTHORISED OUTPUT.  `Finite` here is mathlib's finiteness of the actual
rational point group of the actual curve — not finiteness of a height sublevel set,
not a `Fintype` you construct by hand, and not a statement about any other group. -/
theorem h41_finite (ε : ℤ) (m q : ℕ) [Fact (Nat.Prime q)]
    (hP : SDyadic.Params ε m q) (hH : SDyadic.H41 ε m) :
    Finite ((P01.Ecurve ε m q).toAffine.Point) := by
  obtain ⟨S, hSfin, hStop⟩ := closure_eq_top hP hH
  haveI : AddGroup.FG ((P01.Ecurve ε m q).toAffine.Point) :=
    AddGroup.fg_iff.mpr ⟨S, hStop, hSfin⟩
  refine AddCommGroup.finite_of_fg_torsion _ ?_
  intro P
  exact isOfFinAddOrder_iff_nsmul_eq_zero.mpr (GateR.every_point_torsion ε m q hP hH P)

end GateRFinite
