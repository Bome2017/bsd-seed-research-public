import RequestProject.GateR.Assembly

/-  EXTERNAL AUDIT.  Each `example` below states the TARGET type verbatim from the
    shipped skeleton and discharges it with the returned theorem.  If a return
    added a hypothesis, weakened a conclusion, changed a quantifier or swapped the
    group, the corresponding example FAILS to typecheck.  Name agreement is not
    enough; this tests the proposition.                                        -/

-- translateMax must still be the shipped definition, checked by rfl.
example {G : Type*} [AddCommGroup G] (T : G) (H : G → ℕ) (P : G) :
    GateR.translateMax T H P = max (H P) (H (P + T)) := rfl

example : ∀ (ε : ℤ) (m q n : ℕ),
    {P : (P01.Ecurve ε m q).toAffine.Point | R1.height P ≤ n}.Finite :=
  GateR.height_sublevels

example : ∀ (ε : ℤ) (m q : ℕ) [Fact (Nat.Prime q)]
    (hP : SDyadic.Params ε m q) (_hH : SDyadic.H41 ε m),
    ∀ P : (P01.Ecurve ε m q).toAffine.Point,
      ∃ Q : (P01.Ecurve ε m q).toAffine.Point, ∃ e : ℕ,
        e ≤ 1 ∧ P = Q + Q + e • P01.Tpt hP :=
  GateR.halving_representatives

example : ∀ (ε : ℤ) (m q : ℕ) [Fact (Nat.Prime q)]
    (hP : SDyadic.Params ε m q) (_hH : SDyadic.H41 ε m),
    ∃ C : ℕ, 1 ≤ C ∧ ∀ P : (P01.Ecurve ε m q).toAffine.Point,
      ∃ Q : (P01.Ecurve ε m q).toAffine.Point, ∃ e : ℕ,
        e ≤ 1 ∧ P = Q + Q + e • P01.Tpt hP ∧
        GateR.translateMax (P01.Tpt hP) R1.height Q ≤
          max (GateR.translateMax (P01.Tpt hP) R1.height P) C :=
  GateR.bounded_halving

example : ∀ (ε : ℤ) (m q : ℕ) [Fact (Nat.Prime q)]
    (_hP : SDyadic.Params ε m q) (_hH : SDyadic.H41 ε m),
    ∀ P : (P01.Ecurve ε m q).toAffine.Point, ∃ n : ℕ, 0 < n ∧ n • P = 0 :=
  GateR.every_point_torsion

example : ∀ (ε : ℤ) (m q : ℕ) [Fact (Nat.Prime q)]
    (_hP : SDyadic.Params ε m q) (_hH : SDyadic.H41 ε m),
    Module.rank ℤ (P01.Ecurve ε m q).toAffine.Point = (0 : Cardinal) :=
  GateR.h41_rank_zero

set_option pp.explicit true in
set_option pp.universes true in
set_option pp.fullNames true in
#check @GateR.h41_rank_zero

#print axioms GateR.translateMax
#print axioms GateR.height_sublevels
#print axioms GateR.halving_representatives
#print axioms GateR.bounded_halving
#print axioms GateR.every_point_torsion
#print axioms GateR.h41_rank_zero
