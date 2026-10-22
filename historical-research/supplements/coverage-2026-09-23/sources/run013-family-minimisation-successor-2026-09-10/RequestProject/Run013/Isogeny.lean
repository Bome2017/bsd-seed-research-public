/-
Run013 — `Isogeny.lean`

The exact frozen degree-two isogeny and its normalized dual (`TARGET.md` §1):

    phi_q(x,y)      = ( y^2 / x^2 ,  y (64 q^2 - x^2) / x^2 )        : E_q  → E'_q,
    hat phi_q(x,y)  = ( y^2 / (4 x^2) , y (-31 q^2 - x^2) / (8 x^2) ) : E'_q → E_q,

together with

* the verification that each map really lands on the stated target curve;
* the kernels;
* `hat phi_q ∘ phi_q = [2]` on `x`-coordinates, checked against mathlib's own
  duplication formula `addX x x (slope x x y y)` for `E_q`;
* the fact that the coefficient pairs used by the two descents are exactly the
  coefficient pairs of the *targets* `E'_q` and `E_q`, which is what fixes the
  orientation and prevents `phi` and `hat phi` from being interchanged;
* the images of the rational two-torsion of `E'_q` under the descent map, which are
  exactly the four classes `1, -31, q, -31 q`.
-/
import RequestProject.Run013.Curves
import RequestProject.Run013.PhiSelmer
import RequestProject.Run013.DualPhiSelmer

namespace Run013

open WeierstrassCurve

/-! ## Orientation: which coefficients drive which descent -/

/-- The `phi_q`-descent uses the coefficients of the **target** curve `E'_q`. -/
theorem phi_coeffs (q : ℕ) :
    phiA q = (EqPrimeCurve (q : ℚ)).a₂ ∧ phiB q = (EqPrimeCurve (q : ℚ)).a₄ := by
  constructor <;> simp [phiA, phiB, EqPrimeCurve]

/-- The `hat phi_q`-descent uses the coefficients of the **target** curve `E_q`. -/
theorem dual_coeffs (q : ℕ) :
    dualA q = (EqCurve (q : ℚ)).a₂ ∧ dualB q = (EqCurve (q : ℚ)).a₄ := by
  constructor <;> simp [dualA, dualB, EqCurve]

/-! ## The isogeny -/

/-- `x`-coordinate of `phi_q`. -/
def phiX (x y : ℚ) : ℚ := y ^ 2 / x ^ 2

/-- `y`-coordinate of `phi_q`. -/
def phiY (q x y : ℚ) : ℚ := y * (64 * q ^ 2 - x ^ 2) / x ^ 2

/-- `x`-coordinate of the normalized dual `hat phi_q`. -/
def dualPhiX (x y : ℚ) : ℚ := y ^ 2 / (4 * x ^ 2)

/-- `y`-coordinate of the normalized dual `hat phi_q`. -/
def dualPhiY (q x y : ℚ) : ℚ := y * (-31 * q ^ 2 - x ^ 2) / (8 * x ^ 2)

/-- `phi_q` maps `E_q` to `E'_q`. -/
theorem phi_maps_to (q x y : ℚ) (hx : x ≠ 0)
    (h : y ^ 2 = x ^ 3 - 15 * q * x ^ 2 + 64 * q ^ 2 * x) :
    phiY q x y ^ 2 =
      phiX x y ^ 3 + 30 * q * phiX x y ^ 2 - 31 * q ^ 2 * phiX x y := by
  have key : y ^ 2 * (64 * q ^ 2 - x ^ 2) ^ 2 * x ^ 2
      = y ^ 6 + 30 * q * y ^ 4 * x ^ 2 - 31 * q ^ 2 * y ^ 2 * x ^ 4 := by
    have h6 : y ^ 6 = (y ^ 2) ^ 3 := by ring
    have h4 : y ^ 4 = (y ^ 2) ^ 2 := by ring
    rw [h6, h4, h]
    ring
  simp only [phiX, phiY]
  field_simp
  linear_combination key

/-- `hat phi_q` maps `E'_q` to `E_q`. -/
theorem dual_phi_maps_to (q x y : ℚ) (hx : x ≠ 0)
    (h : y ^ 2 = x ^ 3 + 30 * q * x ^ 2 - 31 * q ^ 2 * x) :
    dualPhiY q x y ^ 2 =
      dualPhiX x y ^ 3 - 15 * q * dualPhiX x y ^ 2 + 64 * q ^ 2 * dualPhiX x y := by
  have key : y ^ 2 * (-31 * q ^ 2 - x ^ 2) ^ 2 * x ^ 2
      = y ^ 6 - 60 * q * y ^ 4 * x ^ 2 + 1024 * q ^ 2 * y ^ 2 * x ^ 4 := by
    have h6 : y ^ 6 = (y ^ 2) ^ 3 := by ring
    have h4 : y ^ 4 = (y ^ 2) ^ 2 := by ring
    rw [h6, h4, h]
    ring
  simp only [dualPhiX, dualPhiY]
  field_simp
  linear_combination 64 * key

/-! ## Kernels -/

/-- The only affine rational point of `E_q` with `y = 0` is `(0,0)`: the kernel of `phi_q`
is `{O, (0,0)}` and this is all of `E_q(Q)[2]`. -/
theorem phi_kernel (q x y : ℚ) (hq : 0 < q)
    (h : y ^ 2 = x ^ 3 - 15 * q * x ^ 2 + 64 * q ^ 2 * x) (hy : y = 0) :
    x = 0 := by
  subst hy
  exact (Eq_two_torsion q x hq).mp (by linarith)

/-- The full rational two-torsion of `E'_q` is `{O, (0,0), (q,0), (-31q,0)}`, and the kernel
of `hat phi_q` is the subgroup `{O, (0,0)}`. -/
theorem dual_phi_two_torsion (q x : ℚ) (hq : q ≠ 0) :
    x ^ 3 + 30 * q * x ^ 2 - 31 * q ^ 2 * x = 0 ↔ x = 0 ∨ x = q ∨ x = -(31 * q) :=
  EqPrime_two_torsion q x hq

/-! ## `hat phi ∘ phi = [2]` -/

open scoped Classical in
/-- Mathlib's duplication formula for `E_q` in closed form. -/
theorem EqCurve_double_x (q x y : ℚ) (hy : y ≠ 0)
    (h : y ^ 2 = x ^ 3 - 15 * q * x ^ 2 + 64 * q ^ 2 * x) :
    (EqCurve q).toAffine.addX x x ((EqCurve q).toAffine.slope x x y y)
      = ((x ^ 2 - 64 * q ^ 2) / (2 * y)) ^ 2 := by
  simp only [WeierstrassCurve.Affine.addX, WeierstrassCurve.Affine.slope,
    WeierstrassCurve.Affine.negY, EqCurve, WeierstrassCurve.toAffine, if_true,
    zero_mul, sub_zero, add_zero]
  rw [if_neg (show ¬ (y = -y) by intro hc; apply hy; linarith),
    show y - -y = 2 * y from by ring]
  field_simp
  linear_combination (4 * (15 * q - 2 * x)) * h

open scoped Classical in
/-- The composite `hat phi_q ∘ phi_q` has the `x`-coordinate of `[2]` on `E_q`;
this is the frozen relation `hat phi_q ∘ phi_q = [2]`. -/
theorem dual_comp_phi_eq_double (q x y : ℚ) (hx : x ≠ 0) (hy : y ≠ 0)
    (h : y ^ 2 = x ^ 3 - 15 * q * x ^ 2 + 64 * q ^ 2 * x) :
    dualPhiX (phiX x y) (phiY q x y)
      = (EqCurve q).toAffine.addX x x ((EqCurve q).toAffine.slope x x y y) := by
  rw [EqCurve_double_x q x y hy h]
  simp only [dualPhiX, phiX, phiY]
  have hy2 : y ^ 2 ≠ 0 := pow_ne_zero 2 hy
  field_simp
  ring

/-! ## The descent map on the rational two-torsion of `E'_q` -/

/-- The four rational two-torsion points of `E'_q` land in the Kummer image at `Q`:
`O ↦ 1`, `(0,0) ↦ b = -31 q^2`, `(q,0) ↦ q`, `(-31q,0) ↦ -31 q`. -/
theorem torsion_in_kummer (q : ℕ) (hq : 0 < q) :
    (1 : ℚ) ∈ KummerImage ℚ (phiA q) (phiB q) ∧
    phiB q ∈ KummerImage ℚ (phiA q) (phiB q) ∧
    ((q : ℚ)) ∈ KummerImage ℚ (phiA q) (phiB q) ∧
    (-(31 * (q : ℚ))) ∈ KummerImage ℚ (phiA q) (phiB q) := by
  have hq0 : (q : ℚ) ≠ 0 := Nat.cast_ne_zero.mpr hq.ne'
  refine ⟨Or.inl rfl, Or.inr (Or.inl rfl), Or.inr (Or.inr ⟨hq0, 0, ?_⟩),
    Or.inr (Or.inr ⟨by simpa using hq0, 0, ?_⟩)⟩
  · simp only [phiA, phiB]; ring
  · simp only [phiA, phiB]; ring

/-- The class of `b = -31 q^2` is the class of `-31`. -/
theorem cls_phiB (q : ℕ) (hq : 0 < q) : cls (phiB q) = cls (-31 : ℚ) := by
  have hq0 : (q : ℚ) ≠ 0 := Nat.cast_ne_zero.mpr hq.ne'
  have hb : phiB q ≠ 0 := phiB_ne_zero hq
  rw [cls_of_ne hb, cls_of_ne (show (-31 : ℚ) ≠ 0 by norm_num)]
  exact qcl_eq_of_sqEq ⟨(q : ℚ), hq0, by simp only [phiB, Units.val_mk0]⟩

/-- **The `phi_q`-Selmer group is exactly the image of the rational two-torsion of `E'_q`.**

Combined with `phi_selmer_eq` this says that the descent map
`E'_q(Q)/phi(E_q(Q)) → Sel^{phi_q}` is surjective, i.e. the `phi_q`-part of Sha vanishes. -/
theorem phi_selmer_eq_torsion_image_min (q : ℕ) (hq : F62min q) :
    SelmerSet (phiA q) (phiB q)
      = {cls 1, cls (phiB q), cls ((q : ℚ)), cls (-(31 * (q : ℚ)))} := by
  rw [phi_selmer_eq_min hq, cls_phiB q hq.pos]

/-- The audited statement, preserved verbatim on the six-field family. -/
theorem phi_selmer_eq_torsion_image (q : ℕ) (hq : F62 q) :
    SelmerSet (phiA q) (phiB q)
      = {cls 1, cls (phiB q), cls ((q : ℚ)), cls (-(31 * (q : ℚ)))} :=
  phi_selmer_eq_torsion_image_min q hq.toMin

end Run013
