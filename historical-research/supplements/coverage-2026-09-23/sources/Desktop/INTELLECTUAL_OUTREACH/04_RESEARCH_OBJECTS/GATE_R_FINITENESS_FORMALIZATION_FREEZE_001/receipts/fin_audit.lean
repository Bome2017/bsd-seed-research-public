import RequestProject.GateRFinite.Finiteness

/- EXTERNAL AUDIT.  The example states the TARGET type verbatim as shipped and
   discharges it with the returned theorem.  Any added hypothesis, weakened
   conclusion, or substituted group makes this fail to typecheck. -/
example : ∀ (ε : ℤ) (m q : ℕ) [Fact (Nat.Prime q)]
    (_hP : SDyadic.Params ε m q) (_hH : SDyadic.H41 ε m),
    Finite ((P01.Ecurve ε m q).toAffine.Point) :=
  GateRFinite.h41_finite

set_option pp.explicit true in
set_option pp.universes true in
set_option pp.fullNames true in
#check @GateRFinite.h41_finite
#print axioms GateRFinite.h41_finite
