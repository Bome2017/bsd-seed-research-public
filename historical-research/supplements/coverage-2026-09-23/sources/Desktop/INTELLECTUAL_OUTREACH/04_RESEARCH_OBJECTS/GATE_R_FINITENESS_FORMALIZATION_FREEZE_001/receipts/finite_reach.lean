import RequestProject.GateR.Assembly

/- CLAUDE-PRIVATE REACHABILITY CHECK for the Ultra finiteness consequence.
   Uses ONLY frozen/certified inputs: GateR.every_point_torsion, R1's duplication
   inequality, R1.one_le_height, GateR.height_sublevels.  Nothing is reproved. -/
namespace Reach
open SDyadic P01 R1

variable {ε : ℤ} {m q : ℕ}

/-- `n • P = 0` lets a multiple be reduced mod `n`. -/
private theorem smul_mod {G : Type*} [AddCommGroup G] (P : G) (n : ℕ) (hn : n • P = 0) (k : ℕ) :
    k • P = (k % n) • P := by
  conv_lhs => rw [← Nat.div_add_mod k n]
  rw [add_smul, mul_comm, mul_smul, hn, smul_zero, zero_add]

theorem height_cubed_le (ε : ℤ) (m q : ℕ) [Fact (Nat.Prime q)]
    (hP : Params ε m q) (hH : H41 ε m) (C : ℕ) (hC : 1 ≤ C)
    (hD : ∀ P : (Ecurve ε m q).toAffine.Point, height P ^ 4 ≤ C * height (P + P)) :
    ∀ P : (Ecurve ε m q).toAffine.Point, height P ^ 3 ≤ C := by
  classical
  intro P
  obtain ⟨n, hn, hnP⟩ := GateR.every_point_torsion ε m q hP hH P
  -- the finite set of multiples of P, which contains the whole doubling orbit
  set S : Finset ((Ecurve ε m q).toAffine.Point) :=
    (Finset.range n).image (fun k => k • P) with hS
  have hPS : P ∈ S := by
    refine Finset.mem_image.mpr ⟨1 % n, Finset.mem_range.mpr (Nat.mod_lt _ hn), ?_⟩
    rw [← smul_mod P n hnP 1, one_smul]
  have hdbl : ∀ R ∈ S, R + R ∈ S := by
    intro R hR
    obtain ⟨k, hk, rfl⟩ := Finset.mem_image.mp hR
    refine Finset.mem_image.mpr ⟨(2 * k) % n, Finset.mem_range.mpr (Nat.mod_lt _ hn), ?_⟩
    rw [← smul_mod P n hnP (2 * k), two_mul, add_smul]
  obtain ⟨Q, hQS, hQmax⟩ := S.exists_max_image height ⟨P, hPS⟩
  have h1 : height Q ^ 4 ≤ C * height Q :=
    le_trans (hD Q) (Nat.mul_le_mul_left C (hQmax _ (hdbl Q hQS)))
  have h3 : height Q ^ 3 ≤ C := by
    have hQ1 : 1 ≤ height Q := one_le_height Q
    have : height Q ^ 3 * height Q ≤ C * height Q := by
      calc height Q ^ 3 * height Q = height Q ^ 4 := by ring
        _ ≤ C * height Q := h1
    exact Nat.le_of_mul_le_mul_right this (lt_of_lt_of_le Nat.zero_lt_one hQ1)
  exact le_trans (Nat.pow_le_pow_left (hQmax _ hPS) 3) h3

/-- THE TARGET: the actual rational point group is finite. -/
theorem finite_points (ε : ℤ) (m q : ℕ) [Fact (Nat.Prime q)]
    (hP : Params ε m q) (hH : H41 ε m) :
    Finite ((Ecurve ε m q).toAffine.Point) := by
  classical
  obtain ⟨C, hC, hD⟩ := h41_multiplicative_duplication_height ε m q hP hH
  have hb : ∀ P : (Ecurve ε m q).toAffine.Point, height P ≤ C := by
    intro P
    have h3 := height_cubed_le ε m q hP hH C hC hD P
    exact le_trans (Nat.le_self_pow (by norm_num) _) h3
  have : (Set.univ : Set ((Ecurve ε m q).toAffine.Point)).Finite :=
    Set.Finite.subset (GateR.height_sublevels ε m q C) (fun P _ => hb P)
  exact Set.finite_univ_iff.mp this

end Reach

#print axioms Reach.finite_points
#print axioms Reach.height_cubed_le
