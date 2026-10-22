/-
Run013 successor — `Descent/Delta.lean`

The actual coordinate descent homomorphism on the genuine mathlib rational point group.

Everything the certified development says about descent so far is stated about
`Run013.KummerImage`, which is a **coordinate-defined set**: the class of `1`, the class of
`b`, and the `x`-coordinates of the remaining affine solutions.  Nothing so far connects it
to an elliptic-curve group.  This file states the theorem that makes that connection:
`KummerImage` is exactly the image of a genuine group homomorphism out of
`WeierstrassCurve.Affine.Point`, mathlib's actual group of nonsingular rational points.

The scaffolding below is proved, and the single target `delta_descent` is now proved as well:
its placeholder has been replaced by a complete proof, together with the auxiliary lemmas it
uses, all of which are proved.

NOT proved, NOT assumed, and explicitly out of scope here:
  * `ker δ_{E'} = φ(E(ℚ))` and `ker δ_E = ψ(E'(ℚ))`,
  * any identification of `Point ⧸ ker δ` with an isogeny cokernel or with `E/2E`,
  * anything named Sel₂, Sha, rank, or BSD.
-/
import RequestProject.Run013.Selmer

namespace Descent

open Run013 WeierstrassCurve

/-! ## The curve -/

/-- The Weierstrass model `y² = x³ + a x² + b x`, as an actual `WeierstrassCurve ℚ`. -/
def Wab (a b : ℚ) : WeierstrassCurve ℚ :=
  { a₁ := 0, a₂ := a, a₃ := 0, a₄ := b, a₆ := 0 }

/-- The discriminant of `Wab a b`.  Proved, not assumed. -/
theorem Wab_Δ (a b : ℚ) : (Wab a b).Δ = 16 * b ^ 2 * (a ^ 2 - 4 * b) := by
  simp [Wab, WeierstrassCurve.Δ, WeierstrassCurve.b₂, WeierstrassCurve.b₄,
    WeierstrassCurve.b₆, WeierstrassCurve.b₈]
  ring

/-- Under the two standing hypotheses the model is nonsingular. -/
theorem Wab_Δ_ne_zero {a b : ℚ} (hb : b ≠ 0) (hΔ : a ^ 2 - 4 * b ≠ 0) : (Wab a b).Δ ≠ 0 := by
  rw [Wab_Δ]
  exact mul_ne_zero (mul_ne_zero (by norm_num) (pow_ne_zero 2 hb)) hΔ

/-- The affine equation of `Wab a b` is literally `y² = x³ + a x² + b x`. -/
theorem Wab_equation_iff (a b x y : ℚ) :
    (Wab a b).toAffine.Equation x y ↔ y ^ 2 = x ^ 3 + a * x ^ 2 + b * x := by
  rw [Affine.equation_iff]
  simp [Wab]

/-- An affine point of `Wab a b` with `x = 0` has `y = 0`.  This is what makes the three
cases of `delta` exhaustive, and it is why the value at `(0,0)` has to be supplied
separately. -/
theorem Wab_x_eq_zero {a b y : ℚ} (h : (Wab a b).toAffine.Equation 0 y) : y = 0 := by
  rw [Wab_equation_iff] at h
  simpa using pow_eq_zero_iff (n := 2) (by norm_num) |>.mp (by simpa using h)

/-! ## The descent map -/

/--
The coordinate descent map on the **actual** mathlib point group.

    δ(O)      = 1
    δ((0,0))  = [b]
    δ((x,y))  = [x]      for x ≠ 0

The value at `(0,0)` is `cls b`, **not** `cls 0`.  `Run013.cls` is defined with
`cls 0 = 1` as an irrelevant default (`Selmer.lean`), and using that default here would
silently delete the exceptional case and make the homomorphism property false on every
line through `(0,0)`.
-/
noncomputable def delta (a b : ℚ) : (Wab a b).toAffine.Point → Qsq
  | .zero => 1
  | @Affine.Point.some _ _ _ x _ _ => if x = 0 then cls b else cls x

@[simp] theorem delta_zero (a b : ℚ) : delta a b 0 = 1 := rfl

@[simp] theorem delta_some_of_ne {a b x y : ℚ} (h : (Wab a b).toAffine.Nonsingular x y)
    (hx : x ≠ 0) : delta a b (Affine.Point.some h) = cls x := by
  simp [delta, hx]

@[simp] theorem delta_some_of_eq {a b y : ℚ} (h : (Wab a b).toAffine.Nonsingular 0 y) :
    delta a b (Affine.Point.some h) = cls b := by
  simp [delta]

/-- The two-torsion point `(0,0)` really is a point of the group, under the standing
hypotheses.  Proved, so the exceptional case of `delta` is not vacuous. -/
theorem two_torsion_mem {a b : ℚ} (hb : b ≠ 0) (hΔ : a ^ 2 - 4 * b ≠ 0) :
    (Wab a b).toAffine.Nonsingular 0 0 := by
  refine (Affine.equation_iff_nonsingular_of_Δ_ne_zero ?_).mp ?_
  · exact Wab_Δ_ne_zero hb hΔ
  · rw [Wab_equation_iff]; ring

/-! ## Square classes: the multiplicative bookkeeping

`Qsq` is an elementary abelian `2`-group, and `cls` is multiplicative on nonzero rationals.
Both facts are proved here from the existing `Run013` definitions; nothing in
`RequestProject/Run013/` is changed.
-/

/-- `cls` is multiplicative on nonzero rationals. -/
theorem cls_mul {u v : ℚ} (hu : u ≠ 0) (hv : v ≠ 0) : cls (u * v) = cls u * cls v := by
  rw [cls_of_ne (mul_ne_zero hu hv), cls_of_ne hu, cls_of_ne hv, qcl, qcl, qcl,
    ← QuotientGroup.mk_mul]
  congr 1
  ext
  simp

/-- Every square class is its own inverse. -/
theorem Qsq_mul_self (c : Qsq) : c * c = 1 := by
  obtain ⟨u, rfl⟩ := qcl_surjective c
  rw [qcl, ← QuotientGroup.mk_mul, QuotientGroup.eq_one_iff, mem_sqSubgroup]
  exact ⟨u, (sq u).symm⟩

theorem Qsq_inv_self (c : Qsq) : c⁻¹ = c := inv_eq_of_mul_eq_one_right (Qsq_mul_self c)

/-- The class of a nonzero square is trivial. -/
theorem cls_sq {t : ℚ} (ht : t ≠ 0) : cls (t ^ 2) = 1 := by
  rw [sq, cls_mul ht ht]
  exact Qsq_mul_self _

/-- If the product of three nonzero rationals is a nonzero square, then the class of the third
is the product of the classes of the first two. -/
theorem cls_eq_mul_of_prod_sq {u v w : ℚ} (hu : u ≠ 0) (hv : v ≠ 0) (hw : w ≠ 0)
    (h : ∃ t : ℚ, t ≠ 0 ∧ u * v * w = t ^ 2) : cls w = cls u * cls v := by
  obtain ⟨t, ht, htt⟩ := h
  have h1 : cls u * cls v * cls w = 1 := by
    rw [← cls_mul hu hv, ← cls_mul (mul_ne_zero hu hv) hw, htt, cls_sq ht]
  rw [← Qsq_inv_self (cls u * cls v)]
  exact eq_inv_of_mul_eq_one_right h1

/-! ## The coefficients of `Wab` -/

@[simp] theorem Wab_a₁ (a b : ℚ) : (Wab a b).toAffine.a₁ = 0 := rfl
@[simp] theorem Wab_a₂ (a b : ℚ) : (Wab a b).toAffine.a₂ = a := rfl
@[simp] theorem Wab_a₃ (a b : ℚ) : (Wab a b).toAffine.a₃ = 0 := rfl
@[simp] theorem Wab_a₄ (a b : ℚ) : (Wab a b).toAffine.a₄ = b := rfl
@[simp] theorem Wab_a₆ (a b : ℚ) : (Wab a b).toAffine.a₆ = 0 := rfl

/-! ## The value attached to an `x`-coordinate -/

/-- The rational number whose square class `delta` records: the `x`-coordinate itself, except at
the two-torsion point `(0,0)`, where it is `b`. -/
def dval (b x : ℚ) : ℚ := if x = 0 then b else x

@[simp] theorem dval_zero (b : ℚ) : dval b 0 = b := if_pos rfl

theorem dval_of_ne (b : ℚ) {x : ℚ} (hx : x ≠ 0) : dval b x = x := if_neg hx

theorem dval_ne_zero {b : ℚ} (hb : b ≠ 0) (x : ℚ) : dval b x ≠ 0 := by
  rw [dval]
  split <;> assumption

theorem delta_some_eq_cls_dval {a b x y : ℚ} (h : (Wab a b).toAffine.Nonsingular x y) :
    delta a b (Affine.Point.some h) = cls (dval b x) := by
  by_cases hx : x = 0
  · subst hx; rw [dval_zero, delta_some_of_eq]
  · rw [dval_of_ne b hx, delta_some_of_ne h hx]

/-! ## The intersection cubic

A line `y = ℓ x + ν` meets `Wab a b` in `x³ + (a − ℓ²)x² + (b − 2ℓν)x − ν²`.  Mathlib's
`addPolynomial_slope` already factors this cubic as `(X − x₁)(X − x₂)(X − x₃)` in every case
covered by the group law — chords, tangents and all — so the two symmetric functions below are
obtained by comparing coefficients, with no case split.
-/

/-- Product and second symmetric function of the three intersection abscissae.  The first
component says the three `x`-coordinates multiply to the square `ν²`; the second is what forces
the value `b` at the exceptional point. -/
theorem root_relations {a b x₁ x₂ y₁ y₂ : ℚ}
    (h₁ : (Wab a b).toAffine.Equation x₁ y₁) (h₂ : (Wab a b).toAffine.Equation x₂ y₂)
    (hxy : ¬(x₁ = x₂ ∧ y₁ = (Wab a b).toAffine.negY x₂ y₂)) :
    x₁ * x₂ * (Wab a b).toAffine.addX x₁ x₂ ((Wab a b).toAffine.slope x₁ x₂ y₁ y₂)
        = (y₁ - (Wab a b).toAffine.slope x₁ x₂ y₁ y₂ * x₁) ^ 2
      ∧ x₁ * x₂ + x₁ * (Wab a b).toAffine.addX x₁ x₂ ((Wab a b).toAffine.slope x₁ x₂ y₁ y₂)
            + x₂ * (Wab a b).toAffine.addX x₁ x₂ ((Wab a b).toAffine.slope x₁ x₂ y₁ y₂)
        = b - 2 * (Wab a b).toAffine.slope x₁ x₂ y₁ y₂
            * (y₁ - (Wab a b).toAffine.slope x₁ x₂ y₁ y₂ * x₁) := by
  have h := Affine.addPolynomial_slope h₁ h₂ hxy
  rw [Affine.addPolynomial_eq, Cubic.prod_X_sub_C_eq, neg_inj, Cubic.toPoly_injective] at h
  have hc := congrArg Cubic.c h
  have hd := congrArg Cubic.d h
  simp only [Wab_a₁, Wab_a₃, Wab_a₄, Wab_a₆] at hc hd
  exact ⟨by linear_combination hd, by linear_combination -hc⟩

/-- The descent values of the three intersection abscissae multiply to a nonzero square.

If none of the three abscissae vanishes the product is `ν²`.  If one of them vanishes then `ν = 0`
— the line passes through `(0,0)` — the other two multiply to `b`, and the product of the three
descent values is `b²`.  Two of them cannot vanish at once, since `b ≠ 0`. -/
theorem dval_prod_sq {b x₁ x₂ x₃ nu L : ℚ} (hb : b ≠ 0)
    (h1 : x₁ * x₂ * x₃ = nu ^ 2)
    (h2 : x₁ * x₂ + x₁ * x₃ + x₂ * x₃ = b - 2 * L * nu) :
    ∃ t : ℚ, t ≠ 0 ∧ dval b x₁ * dval b x₂ * dval b x₃ = t ^ 2 := by
  have hnu_of : x₁ * x₂ * x₃ = 0 → nu = 0 := by
    intro h0
    have : nu ^ 2 = 0 := by rw [← h1, h0]
    exact pow_eq_zero_iff (n := 2) (by norm_num) |>.mp this
  by_cases hx1 : x₁ = 0
  · subst hx1
    have hnu : nu = 0 := hnu_of (by ring)
    subst hnu
    have h23 : x₂ * x₃ = b := by linear_combination h2
    have hx2 : x₂ ≠ 0 := by
      rintro rfl
      exact hb (by linear_combination -h23)
    have hx3 : x₃ ≠ 0 := by
      rintro rfl
      exact hb (by linear_combination -h23)
    exact ⟨b, hb, by rw [dval_zero, dval_of_ne b hx2, dval_of_ne b hx3]; linear_combination b * h23⟩
  · by_cases hx2 : x₂ = 0
    · subst hx2
      have hnu : nu = 0 := hnu_of (by ring)
      subst hnu
      have h13 : x₁ * x₃ = b := by linear_combination h2
      have hx3 : x₃ ≠ 0 := by
        rintro rfl
        exact hb (by linear_combination -h13)
      exact ⟨b, hb, by
        rw [dval_zero, dval_of_ne b hx1, dval_of_ne b hx3]; linear_combination b * h13⟩
    · by_cases hx3 : x₃ = 0
      · subst hx3
        have hnu : nu = 0 := hnu_of (by ring)
        subst hnu
        have h12 : x₁ * x₂ = b := by linear_combination h2
        exact ⟨b, hb, by
          rw [dval_zero, dval_of_ne b hx1, dval_of_ne b hx2]; linear_combination b * h12⟩
      · refine ⟨nu, ?_, by rw [dval_of_ne b hx1, dval_of_ne b hx2, dval_of_ne b hx3]; exact h1⟩
        intro h0
        exact (mul_ne_zero (mul_ne_zero hx1 hx2) hx3) (by rw [h1, h0]; ring)

/-! ## Conclusion 1: `delta` is a homomorphism -/

/-- The descent map respects the elliptic group law.  All cases of mathlib's addition are
covered: either summand at infinity, inverse pairs (vertical lines), doubling, the exceptional
point `(0,0)`, and ordinary chords. -/
theorem delta_add {a b : ℚ} (hb : b ≠ 0) (P Q : (Wab a b).toAffine.Point) :
    delta a b (P + Q) = delta a b P * delta a b Q := by
  rcases P with _ | @⟨x₁, y₁, h₁⟩
  · rw [show (Affine.Point.zero : (Wab a b).toAffine.Point) = 0 from rfl, zero_add, delta_zero,
      one_mul]
  · rcases Q with _ | @⟨x₂, y₂, h₂⟩
    · rw [show (Affine.Point.zero : (Wab a b).toAffine.Point) = 0 from rfl, add_zero, delta_zero,
        mul_one]
    · by_cases hxy : x₁ = x₂ ∧ y₁ = (Wab a b).toAffine.negY x₂ y₂
      · obtain ⟨hx, hy⟩ := hxy
        subst hx
        rw [Affine.Point.add_of_Y_eq rfl hy, delta_zero, delta_some_eq_cls_dval,
          delta_some_eq_cls_dval]
        exact (Qsq_mul_self _).symm
      · rw [Affine.Point.add_some hxy, delta_some_eq_cls_dval, delta_some_eq_cls_dval,
          delta_some_eq_cls_dval]
        obtain ⟨hr1, hr2⟩ := root_relations h₁.left h₂.left hxy
        exact cls_eq_mul_of_prod_sq (dval_ne_zero hb _) (dval_ne_zero hb _) (dval_ne_zero hb _)
          (dval_prod_sq hb hr1 hr2)

/-! ## Conclusion 2: the image of `delta` -/

/-- The covering is soluble for `d = 1`: the class of the point at infinity. -/
theorem cov_one (a b : ℚ) : Cov ℚ a b 1 := ⟨1, 0, 1, by simp, by norm_num⟩

/-- The covering is soluble for `d = b`: the class of the two-torsion point `(0,0)`. -/
theorem cov_b {a b : ℚ} (hb : b ≠ 0) : Cov ℚ a b b :=
  ⟨0, 1, 1, by simp, by rw [div_self hb]; ring⟩

/-- The covering is soluble for the abscissa of any affine point with `x ≠ 0`.  This uses the
already-certified `Run013.cov_iff_inKummer`. -/
theorem cov_of_point {a b x y : ℚ} (hb : b ≠ 0) (hx : x ≠ 0)
    (hy : y ^ 2 = x ^ 3 + a * x ^ 2 + b * x) : Cov ℚ a b x :=
  (cov_iff_inKummer hb hx).mpr ⟨x, Or.inr (Or.inr ⟨hx, y, hy⟩), SqEq.rfl' x⟩

/-- The image of `delta` is exactly the set of classes represented by a `d` for which the quartic
covering `Cov ℚ a b d` is soluble. -/
theorem delta_image {a b : ℚ} (hb : b ≠ 0) (hΔ : a ^ 2 - 4 * b ≠ 0) (c : Qsq) :
    (∃ P : (Wab a b).toAffine.Point, delta a b P = c)
      ↔ ∃ d : ℚˣ, qcl d = c ∧ Cov ℚ a b (d : ℚ) := by
  constructor
  · rintro ⟨P, rfl⟩
    rcases P with _ | @⟨x, y, h⟩
    · exact ⟨1, rfl, by simpa using cov_one a b⟩
    · by_cases hx : x = 0
      · subst hx
        refine ⟨Units.mk0 b hb, ?_, ?_⟩
        · rw [delta_some_of_eq h, cls_of_ne hb]
        · simpa using cov_b hb
      · refine ⟨Units.mk0 x hx, ?_, ?_⟩
        · rw [delta_some_of_ne h hx, cls_of_ne hx]
        · have hy : y ^ 2 = x ^ 3 + a * x ^ 2 + b * x := (Wab_equation_iff a b x y).mp h.left
          simpa using cov_of_point hb hx hy
  · rintro ⟨d, rfl, hcov⟩
    obtain ⟨c₀, hmem, hsq⟩ := (cov_iff_inKummer hb d.ne_zero).mp hcov
    rcases hmem with rfl | rfl | ⟨hx, y, hy⟩
    · refine ⟨0, ?_⟩
      rw [delta_zero, qcl_eq_of_sqEq (b := 1) (by simpa using hsq)]
      rfl
    · refine ⟨Affine.Point.some (two_torsion_mem hb hΔ), ?_⟩
      rw [delta_some_of_eq (two_torsion_mem hb hΔ), cls_of_ne hb]
      exact (qcl_eq_of_sqEq (a := d) (b := Units.mk0 c₀ hb) (by simpa using hsq)).symm
    · have hns : (Wab a b).toAffine.Nonsingular c₀ y :=
        (Affine.equation_iff_nonsingular_of_Δ_ne_zero (Wab_Δ_ne_zero hb hΔ)).mp
          ((Wab_equation_iff a b c₀ y).mpr hy)
      refine ⟨Affine.Point.some hns, ?_⟩
      rw [delta_some_of_ne hns hx, cls_of_ne hx]
      exact (qcl_eq_of_sqEq (a := d) (b := Units.mk0 c₀ hx) (by simpa using hsq)).symm

/-! ## The target -/

/--
**Target.**  `δ` is a homomorphism out of the actual point group, its image is exactly the
certified global solubility set, and the induced first-isomorphism quotient exists.

Conclusion 1 is the homomorphism law.  It is a conclusion, never a hypothesis.

Conclusion 2 identifies the image with `∃ d, qcl d = c ∧ Cov ℚ a b d`, which is exactly
`SDyadic.GlobalSet a b` written with the existing `Run013.Cov`.  The intended route is the
already-certified `Run013.cov_iff_inKummer`; that equivalence is to be **used**, never
reproved or replaced.

Conclusion 3 is the existing first isomorphism theorem applied to the bundled map, with the
quotient taken over the honest kernel.  It is not a cardinality claim.

The mechanism of conclusion 1: a line `y = λx + ν` meets `Wab a b` in
`x³ + (a − λ²)x² + (b − 2λν)x − ν²`, whose three roots multiply to `ν²` — a square, hence
trivial in `Qsq`.  When the line passes through `(0,0)` we have `ν = 0`, the cubic factors as
`x·(x² + (a − λ²)x + b)`, and the two remaining roots multiply to `b` — which is exactly why
`δ((0,0)) = [b]`.  Vertical lines, tangents and the `(0,0)` translations are separate cases
and none may be omitted.
-/
theorem delta_descent (a b : ℚ) (hb : b ≠ 0) (hΔ : a ^ 2 - 4 * b ≠ 0) :
    (∀ P Q : (Wab a b).toAffine.Point,
        delta a b (P + Q) = delta a b P * delta a b Q)
    ∧ (∀ c : Qsq,
        (∃ P : (Wab a b).toAffine.Point, delta a b P = c)
          ↔ ∃ d : ℚˣ, qcl d = c ∧ Cov ℚ a b (d : ℚ))
    ∧ (∃ φ : Multiplicative ((Wab a b).toAffine.Point) →* Qsq,
        (∀ P : (Wab a b).toAffine.Point, φ (Multiplicative.ofAdd P) = delta a b P)
          ∧ Nonempty ((Multiplicative ((Wab a b).toAffine.Point) ⧸ φ.ker) ≃* φ.range)) := by
  refine ⟨delta_add hb, delta_image hb hΔ, ?_⟩
  refine ⟨{ toFun := fun P => delta a b (Multiplicative.toAdd P)
            map_one' := delta_zero a b
            map_mul' := fun P Q => delta_add hb _ _ }, fun _ => rfl,
    ⟨QuotientGroup.quotientKerEquivRange _⟩⟩

end Descent
