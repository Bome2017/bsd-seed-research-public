import RequestProject.P03d.Composites

namespace P03e

open Run013 SDyadic Descent P01 P03a P03b P03c P03d WeierstrassCurve

/-! # P03e — the descent kernel is the isogeny image

This is the bridge the whole programme has been moving toward.

Two independently constructed things sit side by side in this project:

* **δ**, the coordinate descent homomorphism on the actual mathlib point group, certified in
  the Delta stage — `Descent.delta`, with `δ(O) = 1`, `δ((0,0)) = [b]`, `δ((x,y)) = [x]`;
* **φ, φ̂**, the degree-2 point-map pair with certified kernels and composites, built by hand
  across P03a–P03d because the pinned mathlib supplies no isogeny API.

Nothing so far connects them. This file states the identification.

## Orientation — get this right

`Descent.delta a b` is the descent map **on** `Wab a b`. `Ecurve = Wab dualA dualB` is `E_q`
and `E'curve = Wab phiA phiB` is `E'_q`. `φ : E_q → E'_q` and `φ̂ : E'_q → E_q`. So the
descent map on a curve is killed by the image of the isogeny landing **on that curve**:

    ker δ_E   = im φ̂        (φ̂ lands on E_q)
    ker δ_E'  = im φ         (φ  lands on E'_q)

Do not transpose these.

## Why the forward direction is transparent

For an ordinary point, the image coordinates are literal squares:

    x(φ̂(X,Y)) = Y²/(4X²) = (Y/(2X))²        x(φ(x,y)) = y²/x² = (y/x)²

so the square class is trivial. The `O` case is `δ(O) = 1` by `P03a.phiPoint_zero` and its
dual. The exceptional case needs care rather than computation: `φ̂(T') = O` and `φ(T) = O` by
P03a, and `δ(O) = 1`.

## Why the reverse direction is the real work

Given only that a coordinate has trivial square class, one must **construct** a rational
preimage. Writing `E : y² = x(x² + a x + b)` and `E' : Y² = X(X² + a'X + b')`, a point
`(X,Y)` on `E'` with `X ≠ 0` has `X = x + a + b/x` for any `φ`-preimage `(x,y)`, so `x`
satisfies

    x² + (a − X)·x + b = 0,     discriminant (X − a)² − 4b = Y²/X

which is a square exactly when `X` is. Take an actual square root, solve for `x`, recover
`y`, check the result really is a point and really maps back. That is a genuine existence
construction, not interface plumbing.

## What is already certified and available

P03d gives the composites, which is the standard way to get one inclusion cheaply: if
`δ_E(P) = 1` on the ordinary branch one can often exhibit the preimage directly, but
`φ̂(φ(P)) = P + P` is available if a doubling argument is preferred. P03c gives both kernels,
P03b additivity, P03a the branch equations, P01 the exact 2-torsion and the named points.

Note the two exceptional points behave **differently**, and both behaviours are already
certified consequences:

* on `E_q`: `δ_E(T) = [dualB] = [r²q²]`, a square, so `T` must lie in `im φ̂` — and it does,
  as `φ̂(Q)` where `Q = (q,0)` is one of the points P01 certified on `E'_q`;
* on `E'_q`: `δ_{E'}(T') = [phiB] = [D q²] = [D]`, which is **not** a square because
  `Params.legendre_D_q` says `legendreSym q D = -1` — and correspondingly `T'` is **not** in
  `im φ`, because `P01.Ecurve_two_torsion` says `E_q(ℚ)[2] = {O,T}` so no rational point of
  `E_q` has `y = 0, x ≠ 0`.

Those two are the sharpest self-consistency checks on the statement, and both were verified
numerically before this handoff was written (`receipts/verify_bridge.py`).

## Boundary

NOT in this file, and not to be added: any quotient object, `E'_q(ℚ)/φ(E_q(ℚ))`,
`E(ℚ)/2E(ℚ)`, `Sel₂`, Ш, rank, BSD. Forming the cokernel is the **next** step and is
legitimate only once this theorem exists.
-/

/-! ## Auxiliary lemmas

All proved.  Nothing below constructs a quotient, a subgroup, a range or an image object:
these are statements about square classes of rationals, about the two coordinate maps of
P03a, and about the marked points of P01.

The three groups are:

* **square classes** — `cls_eq_one_iff_sq` turns a trivial class into an actual rational
  square root, which is exactly the input the reverse direction needs, and `cls_dualB` /
  `cls_phiB_ne_one` settle the two exceptional fibres;
* **the algebraic cores** — `dual_preimage_core` and `phi_preimage_core`, the division-free
  identities behind the two preimage constructions;
* **the constructions themselves** — `exists_dualPhi_preimage` and `exists_phi_preimage`,
  which build an actual point of the opposite curve and prove it maps back.
-/

/-- A nonzero rational has trivial square class exactly when it is a rational square.  This
is the step that converts `δ(P) = 1` into an actual square root. -/
theorem cls_eq_one_iff_sq {u : ℚ} (hu : u ≠ 0) :
    cls u = 1 ↔ ∃ w : ℚ, w ≠ 0 ∧ u = w ^ 2 := by
  constructor
  · intro h
    have h1 : qcl (Units.mk0 u hu) = qcl (Units.mk0 1 one_ne_zero) := by
      rw [← cls_of_ne hu, ← cls_of_ne (one_ne_zero : (1 : ℚ) ≠ 0), h, cls_one]
    obtain ⟨t, ht⟩ := qcl_eq_qcl.mp h1
    have ht' : (1 : ℚ) = u * (t : ℚ) ^ 2 := by
      have h2 := congrArg (fun z : ℚˣ => (z : ℚ)) ht
      simpa using h2
    refine ⟨((t : ℚ))⁻¹, inv_ne_zero t.ne_zero, ?_⟩
    field_simp
    linear_combination -ht'
  · rintro ⟨w, hw, rfl⟩
    exact cls_sq hw

/-- `dualB = r²q²` is literally the square of `rq`. -/
theorem dualB_eq_sq (ε : ℤ) (m q : ℕ) :
    dualB ε m q = (((rr ε m * (q : ℤ) : ℤ) : ℚ)) ^ 2 := by
  simp only [dualB, BB]
  push_cast
  ring

/-- `δ_E(T) = [dualB] = 1`: the exceptional value on `E_q` is a square. -/
theorem cls_dualB {ε : ℤ} {m q : ℕ} [Fact (Nat.Prime q)] (hP : Params ε m q) :
    cls (dualB ε m q) = 1 := by
  refine (cls_eq_one_iff_sq (dualB_ne_zero hP)).mpr ⟨_, ?_, dualB_eq_sq ε m q⟩
  intro h0
  exact dualB_ne_zero hP (by rw [dualB_eq_sq, h0]; ring)

/-- `δ_{E'}(T') = [phiB] = [D q²] = [D] ≠ 1`: the exceptional value on `E'_q` is **not** a
square, because `Params.legendre_D_q` gives `legendreSym q D = -1` (`P01.DD_not_rat_sq`). -/
theorem cls_phiB_ne_one {ε : ℤ} {m q : ℕ} [Fact (Nat.Prime q)] (hP : Params ε m q) :
    cls (phiB ε m q) ≠ 1 := by
  intro h
  obtain ⟨w, hw, hEq⟩ := (cls_eq_one_iff_sq (phiB_ne_zero hP)).mp h
  refine DD_not_rat_sq hP (w / (q : ℚ)) ?_
  have hq : ((q : ℚ)) ≠ 0 := q_ne_zero' hP
  have hb : phiB ε m q = ((DD ε m : ℤ) : ℚ) * (q : ℚ) ^ 2 := by
    simp only [phiB]; push_cast; ring
  field_simp
  rw [← hEq, hb]; ring

/-- On `E_q` no rational point has `y = 0` and `x ≠ 0`: immediate from P01's exact rational
2-torsion `E_q(ℚ)[2] = {O, T}`.  This is what keeps `T'` out of the image of `φ`. -/
theorem Ecurve_y_zero_imp_x_zero {ε : ℤ} {m q : ℕ} [Fact (Nat.Prime q)] (hP : Params ε m q)
    {x : ℚ} (h : (Ecurve ε m q).toAffine.Nonsingular x 0) : x = 0 := by
  have hd : Affine.Point.some h + Affine.Point.some h = 0 :=
    (Wab_two_torsion_some (a := dualA ε m q) (b := dualB ε m q) h).mpr rfl
  rcases (Ecurve_two_torsion hP _).mp hd with h0 | h0
  · exact absurd h0 (Affine.Point.some_ne_zero _)
  · rw [Tpt, Affine.Point.some.injEq] at h0
    exact h0.1

/-! ### The algebraic cores of the two preimage constructions -/

/--
**Core of the `φ̂`-preimage.**  Let `x = w²` be a square abscissa on `E : y² = x(x²+ax+b)`,
and write `y = w·u`, so that `u² = w⁴ + a w² + b`.  Put

    X = 2w² + a + 2u,        Y = −2wX.

Then `b' − X² = −4uX` — which forces `X ≠ 0` once `b' ≠ 0` — and `(X,Y)` satisfies the
equation of `E' : Y² = X(X² + a'X + b')`.  Division free. -/
theorem dual_preimage_core {a b a' b' w u : ℚ}
    (ha' : a' = -2 * a) (hb' : b' = a ^ 2 - 4 * b)
    (hu : u ^ 2 = w ^ 4 + a * w ^ 2 + b) :
    b' - (2 * w ^ 2 + a + 2 * u) ^ 2 = -4 * u * (2 * w ^ 2 + a + 2 * u)
      ∧ (-2 * w * (2 * w ^ 2 + a + 2 * u)) ^ 2
          = (2 * w ^ 2 + a + 2 * u) ^ 3 + a' * (2 * w ^ 2 + a + 2 * u) ^ 2
            + b' * (2 * w ^ 2 + a + 2 * u) := by
  subst ha' hb'
  exact ⟨by linear_combination 4 * hu,
    by linear_combination (-4 * (2 * w ^ 2 + a + 2 * u)) * hu⟩

/--
**Core of the `φ`-preimage.**  Let `X = w²` be a square abscissa on `E'`, and write `Y = w·V`,
so that `V² = w⁴ + a'w² + b'`.  This `V` is precisely the square root of the discriminant
`(X − a)² − 4b` of `x² + (a − X)x + b`, so

    x = (w² − a + V)/2,        y = −w·x

is a root of that quadratic.  Then `b − x² = −Vx` — which forces `x ≠ 0` once `b ≠ 0` — and
`(x,y)` satisfies the equation of `E : y² = x(x² + ax + b)`. -/
theorem phi_preimage_core {a b a' b' w V : ℚ}
    (ha' : a' = -2 * a) (hb' : b' = a ^ 2 - 4 * b)
    (hV : V ^ 2 = w ^ 4 + a' * w ^ 2 + b') :
    b - ((w ^ 2 - a + V) / 2) ^ 2 = -V * ((w ^ 2 - a + V) / 2)
      ∧ (-w * ((w ^ 2 - a + V) / 2)) ^ 2
          = ((w ^ 2 - a + V) / 2) ^ 3 + a * ((w ^ 2 - a + V) / 2) ^ 2
            + b * ((w ^ 2 - a + V) / 2) := by
  subst ha' hb'
  exact ⟨by linear_combination (1/4 : ℚ) * hV,
    by linear_combination (-(w ^ 2 - a + V) / 8) * hV⟩

/-! ### The two constructions -/

/--
**The reverse direction on `E_q`, constructively.**  An affine point of `E_q` whose abscissa
is an actual rational square `w²` is `φ̂` of an actual rational point of `E'_q`, namely

    (X, Y) = (2w² + dualA + 2u,  −2wX),      y = w·u.

`X ≠ 0` because `b' − X² = −4uX` and `phiB ≠ 0`; the image coordinates are checked against
`P03a.dualPhiX` and `P03a.dualPhiY` directly. -/
theorem exists_dualPhi_preimage {ε : ℤ} {m q : ℕ} [Fact (Nat.Prime q)] (hP : Params ε m q)
    {x y : ℚ} (h : (Ecurve ε m q).toAffine.Nonsingular x y)
    {w : ℚ} (hw : w ≠ 0) (hxw : x = w ^ 2) :
    ∃ P' : (E'curve ε m q).toAffine.Point, dualPhiPoint hP P' = Affine.Point.some h := by
  obtain ⟨u, rfl⟩ : ∃ u : ℚ, y = w * u := ⟨y / w, by field_simp⟩
  have heq : (w * u) ^ 2 = x ^ 3 + dualA ε m q * x ^ 2 + dualB ε m q * x :=
    (Wab_equation_iff _ _ x _).mp h.left
  subst hxw
  have hu : u ^ 2 = w ^ 4 + dualA ε m q * w ^ 2 + dualB ε m q := by
    refine mul_left_cancel₀ (pow_ne_zero 2 hw) ?_
    linear_combination heq
  obtain ⟨k1, k2⟩ := dual_preimage_core (family_phiA_eq ε m q) (family_phiB_eq ε m q) hu
  set X : ℚ := 2 * w ^ 2 + dualA ε m q + 2 * u
  have hX : X ≠ 0 := by
    intro h0
    rw [h0] at k1
    exact phiB_ne_zero hP (by linarith [k1])
  have hns : (E'curve ε m q).toAffine.Nonsingular X (-2 * w * X) := by
    refine (Affine.equation_iff_nonsingular_of_Δ_ne_zero (E'curve_Δ_ne_zero hP)).mp ?_
    show (Wab (phiA ε m q) (phiB ε m q)).toAffine.Equation _ _
    rw [Wab_equation_iff]
    exact k2
  refine ⟨Affine.Point.some hns, ?_⟩
  rw [dualPhiPoint_some_of_ne hP hns hX]
  have h4 : (4 : ℚ) * X ^ 2 ≠ 0 := mul_ne_zero (by norm_num) (pow_ne_zero 2 hX)
  have h8 : (8 : ℚ) * X ^ 2 ≠ 0 := mul_ne_zero (by norm_num) (pow_ne_zero 2 hX)
  refine Wab_pt_eq _ h ?_ ?_
  · show dualPhiX X (-2 * w * X) = w ^ 2
    rw [dualPhiX, div_eq_iff h4]; ring
  · show dualPhiY (phiB ε m q) X (-2 * w * X) = w * u
    rw [dualPhiY, k1, div_eq_iff h8]; ring

/--
**The reverse direction on `E'_q`, constructively.**  An affine point of `E'_q` whose abscissa
is an actual rational square `w²` is `φ` of an actual rational point of `E_q`, namely

    (x, y) = ((w² − dualA + V)/2,  −w·x),      Y = w·V.

`x ≠ 0` because `b − x² = −Vx` and `dualB ≠ 0`; the image coordinates are checked against
`P03a.phiX` and `P03a.phiY` directly. -/
theorem exists_phi_preimage {ε : ℤ} {m q : ℕ} [Fact (Nat.Prime q)] (hP : Params ε m q)
    {X Y : ℚ} (h : (E'curve ε m q).toAffine.Nonsingular X Y)
    {w : ℚ} (hw : w ≠ 0) (hXw : X = w ^ 2) :
    ∃ P : (Ecurve ε m q).toAffine.Point, phiPoint hP P = Affine.Point.some h := by
  obtain ⟨V, rfl⟩ : ∃ V : ℚ, Y = w * V := ⟨Y / w, by field_simp⟩
  have heq : (w * V) ^ 2 = X ^ 3 + phiA ε m q * X ^ 2 + phiB ε m q * X :=
    (Wab_equation_iff _ _ X _).mp h.left
  subst hXw
  have hV : V ^ 2 = w ^ 4 + phiA ε m q * w ^ 2 + phiB ε m q := by
    refine mul_left_cancel₀ (pow_ne_zero 2 hw) ?_
    linear_combination heq
  obtain ⟨k1, k2⟩ := phi_preimage_core (family_phiA_eq ε m q) (family_phiB_eq ε m q) hV
  set x : ℚ := (w ^ 2 - dualA ε m q + V) / 2
  have hx : x ≠ 0 := by
    intro h0
    rw [h0] at k1
    exact dualB_ne_zero hP (by linarith [k1])
  have hns : (Ecurve ε m q).toAffine.Nonsingular x (-w * x) := by
    refine (Affine.equation_iff_nonsingular_of_Δ_ne_zero (Ecurve_Δ_ne_zero hP)).mp ?_
    show (Wab (dualA ε m q) (dualB ε m q)).toAffine.Equation _ _
    rw [Wab_equation_iff]
    exact k2
  refine ⟨Affine.Point.some hns, ?_⟩
  rw [phiPoint_some_of_ne hP hns hx]
  have h2 : x ^ 2 ≠ 0 := pow_ne_zero 2 hx
  refine Wab_pt_eq _ h ?_ ?_
  · show phiX x (-w * x) = w ^ 2
    rw [phiX, div_eq_iff h2]; ring
  · show phiY (dualB ε m q) x (-w * x) = w * V
    rw [phiY, k1, div_eq_iff h2]; ring

/-- `φ̂(Q) = T`, for P01's certified point `Q = (q,0)` on `E'_q`.  This is the exceptional
fibre of the forward direction on `E_q`: `δ_E(T) = [dualB]` is a square, and `T` really is in
the image of `φ̂`. -/
theorem dualPhiPoint_Qpt {ε : ℤ} {m q : ℕ} [Fact (Nat.Prime q)] (hP : Params ε m q) :
    dualPhiPoint hP (Qpt hP) = Tpt hP := by
  rw [Qpt, dualPhiPoint_some_of_ne hP (Q_mem hP) (q_ne_zero' hP)]
  refine Wab_pt_eq _ (T_mem hP) ?_ ?_
  · show dualPhiX (q : ℚ) 0 = 0
    simp [dualPhiX]
  · show dualPhiY (phiB ε m q) (q : ℚ) 0 = 0
    simp [dualPhiY]

/-! ### The forward direction: every image has trivial descent class -/

/-- **Forward on `E_q`.**  `δ_E(φ̂(P')) = 1` for every `P'`, including both exceptional
fibres.  On the ordinary branch the image abscissa is the literal square `(Y/(2X))²`; when
`Y = 0` the image abscissa is `0` and the recorded value is `dualB = (rq)²`, again a square;
and the two `O` branches are `δ(O) = 1`. -/
theorem delta_dualPhiPoint {ε : ℤ} {m q : ℕ} [Fact (Nat.Prime q)] (hP : Params ε m q)
    (P' : (E'curve ε m q).toAffine.Point) :
    delta (dualA ε m q) (dualB ε m q) (dualPhiPoint hP P') = 1 := by
  cases P' with
  | zero =>
    rw [show (Affine.Point.zero : (E'curve ε m q).toAffine.Point) = 0 from rfl,
      dualPhiPoint_zero]
    exact delta_zero _ _
  | @some X Y h =>
    by_cases hX : X = 0
    · subst hX
      rw [dualPhiPoint_some_of_X_eq_zero hP h]
      exact delta_zero _ _
    · rw [dualPhiPoint_some_of_ne hP h hX, delta_some_eq_cls_dval]
      by_cases hY : Y = 0
      · subst hY
        have h0 : dualPhiX X 0 = 0 := by simp [dualPhiX]
        rw [h0, dval_zero]
        exact cls_dualB hP
      · have hne : dualPhiX X Y ≠ 0 :=
          div_ne_zero (pow_ne_zero 2 hY) (mul_ne_zero (by norm_num) (pow_ne_zero 2 hX))
        have hsq : dualPhiX X Y = (Y / (2 * X)) ^ 2 := by
          rw [dualPhiX, div_pow]; ring_nf
        rw [dval_of_ne _ hne, hsq]
        exact cls_sq (div_ne_zero hY (mul_ne_zero two_ne_zero hX))

/-- **Forward on `E'_q`.**  `δ_{E'}(φ(P)) = 1` for every `P`.  On the ordinary branch the
image abscissa is the literal square `(y/x)²`.  The branch `y = 0, x ≠ 0` — which would land
on `T'`, whose class is **not** trivial — cannot occur, by P01's exact 2-torsion. -/
theorem delta_phiPoint {ε : ℤ} {m q : ℕ} [Fact (Nat.Prime q)] (hP : Params ε m q)
    (P : (Ecurve ε m q).toAffine.Point) :
    delta (phiA ε m q) (phiB ε m q) (phiPoint hP P) = 1 := by
  cases P with
  | zero =>
    rw [show (Affine.Point.zero : (Ecurve ε m q).toAffine.Point) = 0 from rfl, phiPoint_zero]
    exact delta_zero _ _
  | @some x y h =>
    by_cases hx : x = 0
    · subst hx
      rw [phiPoint_some_of_x_eq_zero hP h]
      exact delta_zero _ _
    · rw [phiPoint_some_of_ne hP h hx, delta_some_eq_cls_dval]
      have hy : y ≠ 0 := by
        rintro rfl
        exact hx (Ecurve_y_zero_imp_x_zero hP h)
      have hne : phiX x y ≠ 0 := div_ne_zero (pow_ne_zero 2 hy) (pow_ne_zero 2 hx)
      have hsq : phiX x y = (y / x) ^ 2 := by rw [phiX, div_pow]
      rw [dval_of_ne _ hne, hsq]
      exact cls_sq (div_ne_zero hy hx)

/--
**Target.**  The descent kernel is the isogeny image, on both sides, in membership form.

    δ_E(P)   = 1  ↔  ∃ P' ∈ E'_q(ℚ),  φ̂(P') = P
    δ_E'(P') = 1  ↔  ∃ P  ∈ E_q(ℚ),   φ(P)  = P'

Equivalently `ker δ_E = im φ̂` and `ker δ_{E'} = im φ`. Membership form is used because it is
what a cokernel construction will consume, and because it avoids introducing any quotient or
subgroup object here.

This theorem identifies the certified explicit descent map with the manually constructed
isogeny pair. It does **not** form a quotient, and says nothing about `E(ℚ)/2E(ℚ)`, `Sel₂`,
Ш or rank. -/
theorem descent_kernel_eq_isogeny_image
    (ε : ℤ) (m q : ℕ) [Fact (Nat.Prime q)] (hP : Params ε m q) :
    (∀ P : (Ecurve ε m q).toAffine.Point,
        delta (dualA ε m q) (dualB ε m q) P = 1
          ↔ ∃ P' : (E'curve ε m q).toAffine.Point, dualPhiHom hP P' = P)
  ∧ (∀ P' : (E'curve ε m q).toAffine.Point,
        delta (phiA ε m q) (phiB ε m q) P' = 1
          ↔ ∃ P : (Ecurve ε m q).toAffine.Point, phiHom hP P = P') := by
  constructor
  · intro P
    constructor
    · intro hδ
      cases P with
      | zero =>
        exact ⟨0, by rw [map_zero]; rfl⟩
      | @some x y h =>
        by_cases hx : x = 0
        · subst hx
          have hy : y = 0 := Wab_x_eq_zero (a := dualA ε m q) (b := dualB ε m q) h.left
          subst hy
          refine ⟨Qpt hP, ?_⟩
          rw [dualPhiHom_apply, dualPhiPoint_Qpt, Tpt]
        · rw [delta_some_of_ne h hx] at hδ
          obtain ⟨w, hw, hxw⟩ := (cls_eq_one_iff_sq hx).mp hδ
          obtain ⟨P', hP'⟩ := exists_dualPhi_preimage hP h hw hxw
          exact ⟨P', by rw [dualPhiHom_apply]; exact hP'⟩
    · rintro ⟨P', rfl⟩
      rw [dualPhiHom_apply]
      exact delta_dualPhiPoint hP P'
  · intro P'
    constructor
    · intro hδ
      cases P' with
      | zero =>
        exact ⟨0, by rw [map_zero]; rfl⟩
      | @some X Y h =>
        by_cases hX : X = 0
        · subst hX
          rw [delta_some_of_eq h] at hδ
          exact absurd hδ (cls_phiB_ne_one hP)
        · rw [delta_some_of_ne h hX] at hδ
          obtain ⟨w, hw, hXw⟩ := (cls_eq_one_iff_sq hX).mp hδ
          obtain ⟨P, hPP⟩ := exists_phi_preimage hP h hw hXw
          exact ⟨P, by rw [phiHom_apply]; exact hPP⟩
    · rintro ⟨P, rfl⟩
      rw [phiHom_apply]
      exact delta_phiPoint hP P

end P03e
