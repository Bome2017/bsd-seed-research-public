/-
`P01/PortedRunB.lean`

Two generic lemmas carried from the **P01 Run B** development into the **P01 Run A** base,
as recommended by `CONTINUATION_BASE_ASSESSMENT.md` in
`P01_FAMILY_TWO_TORSION_FORMALIZATION_FREEZE_001`.

Run A is the base because it names its results — `Ecurve_two_torsion`, `E'curve_two_torsion`
and the seven nonzero/distinctness lemmas are standalone and citable, where Run B's are
reachable only as a nine-deep projection of the target conjunction.  Run B nonetheless proved
two lemmas that are strictly better than Run A's counterparts:

  * `Wab_two_torsion_iff` covers **all** points including `O`, where Run A's
    `Wab_two_torsion_some` covers only the affine case;
  * `int_isSquare_of_rat_sq` is curve-free and family-free, where Run A folds the same step
    into the family-specific `DD_not_rat_sq`.

Both are reproduced here **verbatim** from
`P01_FAMILY_TWO_TORSION_FORMALIZATION_FREEZE_001/02_run_B/tree/RequestProject/P01/TwoTorsion.lean`,
which rebuilds clean with axiom footprint `[propext, Classical.choice, Quot.sound]`.

Neither is used by the P03a target.  They are carried so the successor base is assembled
once, for P03b-e.
-/
import RequestProject.P01.TwoTorsion

namespace P01

open Run013 SDyadic Descent WeierstrassCurve

theorem Wab_two_torsion_iff {a b : ℚ} (P : (Wab a b).toAffine.Point) :
    P + P = 0 ↔ P = 0 ∨ ∃ (x : ℚ) (h : (Wab a b).toAffine.Nonsingular x 0),
      P = Affine.Point.some h := by
  rw [add_eq_zero_iff_eq_neg]
  cases P with
  | zero => exact ⟨fun _ => Or.inl rfl, fun _ => (neg_zero (G := (Wab a b).toAffine.Point)).symm⟩
  | @some x y h =>
      rw [Affine.Point.neg_some]
      constructor
      · intro hh
        have hy0 : y = (Wab a b).toAffine.negY x y := by simpa using hh
        rw [Wab_negY_eq] at hy0
        have hy : y = 0 := by linarith
        subst hy
        exact Or.inr ⟨x, h, rfl⟩
      · rintro (hh | ⟨x', h', hh⟩)
        · exact absurd hh (by simp)
        · have hxy : x = x' ∧ y = 0 := by simpa using hh
          obtain ⟨rfl, rfl⟩ := hxy
          simp

theorem int_isSquare_of_rat_sq {D : ℤ} {u : ℚ} (h : u ^ 2 = (D : ℚ)) : IsSquare D := by
  have hd : u.den = 1 := by
    have hden := Rat.den_pow u 2
    rw [h] at hden
    simp only [Rat.den_intCast] at hden
    nlinarith [hden]
  refine ⟨u.num, ?_⟩
  have hnum : (u.num : ℚ) = u := by rw [← Rat.num_div_den u, hd]; simp
  have h2 : ((u.num * u.num : ℤ) : ℚ) = (D : ℚ) := by push_cast [hnum]; linear_combination h
  exact_mod_cast h2.symm

end P01
