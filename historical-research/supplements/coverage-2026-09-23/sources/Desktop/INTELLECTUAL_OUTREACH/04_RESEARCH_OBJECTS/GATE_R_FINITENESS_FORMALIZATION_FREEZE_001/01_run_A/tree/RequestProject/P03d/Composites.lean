import RequestProject.P03c.Kernels

namespace P03d

open Run013 SDyadic Descent P01 P03a P03b P03c WeierstrassCurve

/-! # P03d — the two composites are doubling

The point-level package so far, all double-run Lean certified:

    P01   E_q(ℚ)[2] = {O,T},  E'_q(ℚ)[2] = {O,T',Q,R}
    P03a  φ, φ̂ as total maps on mathlib's actual point types, landing on the opposite curve
    P03b  both maps are additive
    P03c  both bundled as AddMonoidHom, with ker φ = {O,T} and ker φ̂ = {O,T'}

This file states the last point-level ingredient of the classical degree-2 pair: that the two
composites are multiplication by two.

## Why the statement is written this way

The right-hand side is **`P + P`**, using mathlib's own `AddCommGroup` structure on
`WeierstrassCurve.Affine.Point`. No `[2]`, no `zsmul`, no new abstraction is introduced. The
theorem therefore says exactly what it looks like it says, in the group law that is already
there.

The left-hand side composes the **bundled** homomorphisms from P03c. `P03c.phiHom_apply` and
`dualPhiHom_apply` are `rfl`, so this is interchangeable with the `phiPoint`/`dualPhiPoint`
form if that is more convenient in the proof.

## The likely shape of the proof

Both P03b runs independently discovered that φ and φ̂ are the `c = 1` and `c = 2` instances of
a single scaled coordinate map

    (x, y)  ↦  ( y² / (c²x²) ,  y(b − x²) / (c³x²) )

That observation was not supplied to them; it came out of both searches. P03d literally
composes the `c = 1` and `c = 2` instances, so whichever generic layer the chosen base
provides — `P03b.gen_additive` and its `core_*` lemmas here — is likely the right tool, and
`P03a.isogeny_core` is the division-free identity underneath it.

Case structure, as in P03b: `P = O`; `P` in the exceptional fibre (`x = 0`, which P01
identifies as `T` on `E_q` and `T'` on `E'_q`); and the ordinary case. Note that on the
exceptional fibre both sides are `O` — `φ(T) = O` by P03a, and `T + T = O` because `T` is
2-torsion by P01 — so those branches close from certified facts rather than computation.

## Boundary

NOT in this file, and not to be added:
`ker δ = im φ`, quotient equivalences of any kind, `E(ℚ)/2E(ℚ)`, `Sel₂`, Ш, rank, BSD.
-/

/-! ## Auxiliary lemmas

All proved.  Three ingredients, and nothing else:

* `double_of_coords` — the doubling side.  On `Wab a b` with `x ≠ 0` and `y ≠ 0`, mathlib's
  `Affine.Point.add` at `P = P` is the tangent branch, and `P03b.addX_eq_of_tangent` /
  `addY_eq_of_tangent` reduce it to two cleared polynomial identities in the coordinates.
  Those two identities are discharged from the source equation alone, division-free, exactly
  as `P03a.isogeny_core` is.
* the four coordinate lemmas — the composite side.  These are pure rational-function algebra
  in the P03a coordinate functions: composing the `c = 1` and `c = 2` instances of the scaled
  map produces `(b − x²)²/(4y²)` and `(b − x²)((a² − 4b)x⁴ − y⁴)/(8y³x²)`, in the cleared
  form `double_of_coords` consumes.  No curve equation is needed for them.

Nothing here is a kernel, a quotient, an image, or a descent statement. -/

/-- **The doubling side.**  On `Wab a b`, an affine point with `x ≠ 0` and `y ≠ 0` doubles to
the point whose coordinates satisfy the two cleared identities

    X₃ · 4y²    = (b − x²)²,
    Y₃ · 8y³x²  = (b − x²)((a² − 4b)x⁴ − y⁴).

The `y ≠ 0` hypothesis puts `Affine.Point.add` in its tangent branch, and the two identities
are then exactly the hypotheses of `P03b.addX_eq_of_tangent` and `addY_eq_of_tangent` after
substituting the source equation `y² = x³ + ax² + bx`. -/
theorem double_of_coords {a b x y X₃ Y₃ : ℚ}
    (h : (Wab a b).toAffine.Nonsingular x y) (h₃ : (Wab a b).toAffine.Nonsingular X₃ Y₃)
    (hx : x ≠ 0) (hy : y ≠ 0)
    (hX₃ : X₃ * (4 * y ^ 2) = (b - x ^ 2) ^ 2)
    (hY₃ : Y₃ * (8 * y ^ 3 * x ^ 2) = (b - x ^ 2) * ((a ^ 2 - 4 * b) * x ^ 4 - y ^ 4)) :
    Affine.Point.some h + Affine.Point.some h = Affine.Point.some h₃ := by
  have heq : y ^ 2 = x ^ 3 + a * x ^ 2 + b * x := (Wab_equation_iff a b x y).mp h.left
  have hYne : y ≠ (Wab a b).toAffine.negY x y := by
    rw [Wab_negY_eq]
    intro hc
    exact hy (by linarith)
  have hne : ¬(x = x ∧ y = (Wab a b).toAffine.negY x y) := fun hc => hYne hc.2
  have keyX : (X₃ + a + x + x) * (2 * y) ^ 2 = (3 * x ^ 2 + 2 * a * x + b) ^ 2 := by
    linear_combination hX₃ + (4 * a + 8 * x) * heq
  have keyY : (Y₃ + y) * (2 * y) = -(3 * x ^ 2 + 2 * a * x + b) * (X₃ - x) := by
    have hz : ((Y₃ + y) * (2 * y) - (-(3 * x ^ 2 + 2 * a * x + b) * (X₃ - x)))
        * (4 * y ^ 2 * x ^ 2) = 0 := by
      linear_combination hY₃ + (x ^ 2 * (3 * x ^ 2 + 2 * a * x + b)) * hX₃ +
        ((9 * x ^ 2 - b) * (y ^ 2 + x ^ 3 + a * x ^ 2 + b * x)
          - 4 * x ^ 3 * (3 * x ^ 2 + 2 * a * x + b)) * heq
    have hne0 : (4 : ℚ) * y ^ 2 * x ^ 2 ≠ 0 :=
      mul_ne_zero (mul_ne_zero (by norm_num) (pow_ne_zero 2 hy)) (pow_ne_zero 2 hx)
    linarith [sub_eq_zero.mp ((mul_eq_zero.mp hz).resolve_right hne0)]
  rw [Affine.Point.add_some hne]
  exact Wab_pt_eq _ _ (addX_eq_of_tangent rfl hYne hy keyX)
    (addY_eq_of_tangent rfl hYne hy keyX keyY)

/-- **Composite abscissa, `φ̂ ∘ φ`.**  The `c = 2` map applied to the `c = 1` image returns
`(b − x²)²/(4y²)`, in cleared form. -/
theorem comp_phi_X (b x y : ℚ) (hx : x ≠ 0) (hy : y ≠ 0) :
    dualPhiX (phiX x y) (phiY b x y) * (4 * y ^ 2) = (b - x ^ 2) ^ 2 := by
  simp only [dualPhiX, phiX, phiY]
  field_simp

/-- **Composite ordinate, `φ̂ ∘ φ`.**  Here `B = a² − 4b` is the `b`-coefficient of the
intermediate curve, which for the family is `P03a.family_phiB_eq`. -/
theorem comp_phi_Y (a b B x y : ℚ) (hx : x ≠ 0) (hy : y ≠ 0) (hB : B = a ^ 2 - 4 * b) :
    dualPhiY B (phiX x y) (phiY b x y) * (8 * y ^ 3 * x ^ 2)
      = (b - x ^ 2) * ((a ^ 2 - 4 * b) * x ^ 4 - y ^ 4) := by
  subst hB
  simp only [dualPhiY, phiX, phiY]
  field_simp

/-- **Composite abscissa, `φ ∘ φ̂`.**  The `c = 1` map applied to the `c = 2` image returns the
same shape, with the roles of the two models exchanged. -/
theorem comp_dual_X (B X Y : ℚ) (hX : X ≠ 0) (hY : Y ≠ 0) :
    phiX (dualPhiX X Y) (dualPhiY B X Y) * (4 * Y ^ 2) = (B - X ^ 2) ^ 2 := by
  simp only [dualPhiX, dualPhiY, phiX]
  field_simp
  ring

/-- **Composite ordinate, `φ ∘ φ̂`.**  Here `16b = A² − 4B`, which for the family is
`P03a.family_dualB_eq`. -/
theorem comp_dual_Y (b A B X Y : ℚ) (hX : X ≠ 0) (hY : Y ≠ 0) (hb : 16 * b = A ^ 2 - 4 * B) :
    phiY b (dualPhiX X Y) (dualPhiY B X Y) * (8 * Y ^ 3 * X ^ 2)
      = (B - X ^ 2) * ((A ^ 2 - 4 * B) * X ^ 4 - Y ^ 4) := by
  have hb' : b = (A ^ 2 - 4 * B) / 16 := by linarith
  subst hb'
  simp only [dualPhiX, dualPhiY, phiY]
  field_simp
  ring

/--
**Target.**  The two composites are doubling.

`φ̂ ∘ φ = [2]` on `E_q(ℚ)` and `φ ∘ φ̂ = [2]` on `E'_q(ℚ)`, stated pointwise against mathlib's
own group law.

After this, the point-level classical 2-isogeny package is complete: actual maps, additivity,
exact kernels, dual composites. It is still **not** `ker δ = im φ`, which is P03e, and it says
nothing about `E(ℚ)/2E(ℚ)`, `Sel₂`, Ш or rank. -/
theorem isogeny_composites_eq_double
    (ε : ℤ) (m q : ℕ) [Fact (Nat.Prime q)] (hP : Params ε m q) :
    (∀ P : (Ecurve ε m q).toAffine.Point,
        dualPhiHom hP (phiHom hP P) = P + P)
  ∧ (∀ P : (E'curve ε m q).toAffine.Point,
        phiHom hP (dualPhiHom hP P) = P + P) := by
  constructor
  · intro P
    cases P with
    | zero =>
      rw [show (Affine.Point.zero : (Ecurve ε m q).toAffine.Point) = 0 from rfl,
        map_zero, map_zero, add_zero]
    | some h =>
      rename_i x y
      rw [phiHom_apply]
      by_cases hx : x = 0
      · -- the exceptional fibre on `E_q`: the point is `T`, so both sides are `O`
        subst hx
        have hy : y = 0 := Wab_x_eq_zero (a := dualA ε m q) (b := dualB ε m q) h.left
        subst hy
        rw [phiPoint_some_of_x_eq_zero hP h, map_zero]
        exact ((Wab_two_torsion_some h).mpr rfl).symm
      · rw [phiPoint_some_of_ne hP h hx]
        by_cases hy : y = 0
        · -- `P` is 2-torsion, and its image is `T'`, so both sides are `O`
          subst hy
          have hX0 : phiX x 0 = 0 := by simp [phiX]
          have hY0 : phiY (dualB ε m q) x 0 = 0 := by simp [phiY]
          rw [show Affine.Point.some ((isogeny_coords_nonsingular ε m q hP).1 x 0 h hx)
              = T'pt hP from Wab_pt_eq _ (T'_mem hP) hX0 hY0, dualPhiHom_apply,
            dualPhiPoint_T'pt]
          exact ((Wab_two_torsion_some h).mpr rfl).symm
        · -- the ordinary branch
          have hX0 : phiX x y ≠ 0 := by
            simp only [phiX]
            exact div_ne_zero (pow_ne_zero 2 hy) (pow_ne_zero 2 hx)
          rw [dualPhiHom_apply, dualPhiPoint_some_of_ne hP _ hX0]
          exact (double_of_coords h _ hx hy (comp_phi_X _ _ _ hx hy)
            (comp_phi_Y (dualA ε m q) _ _ _ _ hx hy (family_phiB_eq ε m q))).symm
  · intro P
    cases P with
    | zero =>
      rw [show (Affine.Point.zero : (E'curve ε m q).toAffine.Point) = 0 from rfl,
        map_zero, map_zero, add_zero]
    | some h =>
      rename_i X Y
      rw [dualPhiHom_apply]
      by_cases hX : X = 0
      · -- the exceptional fibre on `E'_q`: the point is `T'`, so both sides are `O`
        subst hX
        have hY : Y = 0 := Wab_x_eq_zero (a := phiA ε m q) (b := phiB ε m q) h.left
        subst hY
        rw [dualPhiPoint_some_of_X_eq_zero hP h, map_zero]
        exact ((Wab_two_torsion_some h).mpr rfl).symm
      · rw [dualPhiPoint_some_of_ne hP h hX]
        by_cases hY : Y = 0
        · -- `P` is 2-torsion, and its image is `T`, so both sides are `O`
          subst hY
          have hx0 : dualPhiX X 0 = 0 := by simp [dualPhiX]
          have hy0 : dualPhiY (phiB ε m q) X 0 = 0 := by simp [dualPhiY]
          rw [show Affine.Point.some ((isogeny_coords_nonsingular ε m q hP).2 X 0 h hX)
              = Tpt hP from Wab_pt_eq _ (T_mem hP) hx0 hy0, phiHom_apply, phiPoint_Tpt]
          exact ((Wab_two_torsion_some h).mpr rfl).symm
        · -- the ordinary branch
          have hx0 : dualPhiX X Y ≠ 0 := by
            simp only [dualPhiX]
            exact div_ne_zero (pow_ne_zero 2 hY)
              (mul_ne_zero (by norm_num) (pow_ne_zero 2 hX))
          rw [phiHom_apply, phiPoint_some_of_ne hP _ hx0]
          exact (double_of_coords h _ hX hY (comp_dual_X _ _ _ hX hY)
            (comp_dual_Y _ (phiA ε m q) _ _ _ hX hY (family_dualB_eq ε m q))).symm

end P03d
