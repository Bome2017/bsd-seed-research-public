import RequestProject.P03a.PointMaps

namespace P03b

open Run013 SDyadic Descent P01 P03a WeierstrassCurve

/-! # P03b — the point maps respect the group law

P03a produced `P03a.phiPoint` and `P03a.dualPhiPoint` as **total functions** on mathlib's own
`WeierstrassCurve.Affine.Point`, with `O ↦ O`, the exceptional `x = 0` point `↦ O`, and the
classical coordinate formulas elsewhere.  Nothing was proved about how they interact with the
group law.

This file states exactly that, and nothing more.

**Everything P03a shipped is available and unchanged**, in particular the branch lemmas that
reduce the exceptional cases in one step:

    phiPoint_zero                  φ(O) = O
    dualPhiPoint_zero              φ̂(O) = O
    phiPoint_some_of_x_eq_zero     an affine point with x = 0 maps to O
    dualPhiPoint_some_of_X_eq_zero the same on the other side
    phiPoint_some_of_ne            the ordinary branch, as an explicit `Affine.Point.some`
    dualPhiPoint_some_of_ne        the same on the other side
    phiPoint_Tpt, dualPhiPoint_T'pt   the named exceptional fibres

and the division-free core from P03a Run B:

    isogeny_core (a b x y : ℚ) (hy : y ^ 2 = x ^ 3 + a * x ^ 2 + b * x) :
      y ^ 2 * (b - x ^ 2) ^ 2 * x ^ 2
        = (y ^ 2) ^ 3 - 2 * a * (y ^ 2) ^ 2 * x ^ 2 + (a ^ 2 - 4 * b) * y ^ 2 * x ^ 4

together with `phi_coords_equation`, `dualPhi_coords_equation`, the four family coefficient
bridges `family_phiA_eq`, `family_phiB_eq`, `family_dualA_eq`, `family_dualB_eq`, and from the
Delta layer `Descent.Wab_negY`, `Descent.vieta_of_eval`, `Descent.addPoly_eval`.

## The target

One theorem, two conjuncts.  After it, and only after it, the maps may legitimately be bundled
as group homomorphisms — that bundling is P03c's business, not this file's.

NOT in this theorem, and not to be added anywhere in this package:
`ker φ`, `ker φ̂`, `φ̂ ∘ φ = [2]`, `φ ∘ φ̂ = [2]`, `ker δ = im φ`, `E(ℚ)/2E(ℚ)`, `Sel₂`, Ш,
rank, BSD.  Do not construct a `MonoidHom`, `AddMonoidHom` or `MulHom` of either map here.

## The case structure

`Affine.Point.add` at the pin splits as: either argument `O`; an inverse/vertical pair
(`x₁ = x₂` with `y₁ = negY x₂ y₂`), which sums to `O`; doubling; and the ordinary chord case.
On top of that, each of `P`, `Q` may itself be the exceptional point (`x = 0`, which on these
models forces `y = 0`), and — the case that is easy to overlook — **the sum `P + Q` may land in
the exceptional fibre even when neither summand does**.

That last family is real: an exhaustive rational check over eight curves found 78 ordered
pairs of exactly that shape, and the identity holds in every one.  See
`receipts/verify_additivity.py`.
-/

/-! ## Auxiliary development

Everything below is **proved**, and everything below serves only the single target at the end
of the file.  No map is defined here, nothing is bundled, and nothing here is a kernel, a
composite, a base change or a `[2]`-statement.

The two P03a maps are the two instances `c = 1` and `c = 2` of one generic picture: for
`E : y² = x(x² + a x + b)` and a scaling parameter `c ≠ 0`, the coordinate formulas

    X = y² / (c² x²),        Y = y (b − x²) / (c³ x²)

carry `E` to `E' : Y² = X(X² + A X + B)` with `A = −2a/c²` and `B = (a² − 4b)/c⁴`.  Taking
`c = 1` gives `P03a.phiX`, `P03a.phiY`; taking `c = 2` gives `P03a.dualPhiX`, `P03a.dualPhiY`,
whose `4 = c²` and `8 = c³` are exactly the rescaling `(u,v) ↦ (u/4, v/8)` recorded in P03a.

### The shape of the algebra

`Affine.Point.add` produces the third intersection of the line `y = L x + ν` with the cubic,
and `Descent.root_relations` — the Delta-layer chord/tangent machinery — supplies two of the
three symmetric functions of the three abscissae; the third is `Affine.addX` itself.  So in the
non-vertical case the data `(x₁, x₂, x₃, L, ν)` satisfies full Vieta, and `a`, `b`, `x₃` may be
eliminated in favour of the four free parameters `x₁, x₂, L, ν`.  Each identity below is then a
rational-function identity, cleared with `field_simp`; `P03a.isogeny_core` supplies the
division-free core wherever the source equation is needed on its own.
-/

theorem core_vertical_image {x₁ x₂ L nu c x₃ b y₁ y₂ : ℚ}
    (hx1 : x₁ ≠ 0) (hx2 : x₂ ≠ 0) (hc : c ≠ 0)
    (hx3 : x₃ = nu ^ 2 / (x₁ * x₂))
    (hbv : b = x₁ * x₂ + x₁ * x₃ + x₂ * x₃ + 2 * L * nu)
    (hy1 : y₁ = L * x₁ + nu) (hy2 : y₂ = L * x₂ + nu)
    (hne : ¬(x₁ = x₂ ∧ y₁ = -y₂))
    (hX : y₁ ^ 2 / (c ^ 2 * x₁ ^ 2) = y₂ ^ 2 / (c ^ 2 * x₂ ^ 2))
    (hY : y₁ * (b - x₁ ^ 2) / (c ^ 3 * x₁ ^ 2) = -(y₂ * (b - x₂ ^ 2) / (c ^ 3 * x₂ ^ 2))) :
    nu = 0 := by
  by_contra hnu
  have hYsum : y₁ * (b - x₁ ^ 2) / (c ^ 3 * x₁ ^ 2) + y₂ * (b - x₂ ^ 2) / (c ^ 3 * x₂ ^ 2)
      = 0 := by linarith
  have h1 : y₁ ^ 2 * x₂ ^ 2 - y₂ ^ 2 * x₁ ^ 2 = 0 := by
    have h2 : y₁ ^ 2 * x₂ ^ 2 - y₂ ^ 2 * x₁ ^ 2
        = (y₁ ^ 2 / (c ^ 2 * x₁ ^ 2) - y₂ ^ 2 / (c ^ 2 * x₂ ^ 2)) * (c ^ 2 * x₁ ^ 2 * x₂ ^ 2) := by
      field_simp
    rw [h2, sub_eq_zero.mpr hX, zero_mul]
  have h1' : nu * ((x₂ - x₁) * (2 * L * (x₁ * x₂) + nu * (x₁ + x₂))) = 0 := by
    rw [hy1, hy2] at h1
    linear_combination h1
  rcases mul_eq_zero.mp h1' with h | h
  · exact hnu h
  rcases mul_eq_zero.mp h with h | h
  · -- the two summands coincide
    have hx12 : x₂ = x₁ := by linarith
    have hy12 : y₂ = y₁ := by rw [hy1, hy2, hx12]
    have hy0 : y₁ ≠ 0 := by
      intro h0
      exact hne ⟨hx12.symm, by rw [h0, hy12, h0]; ring⟩
    have hb2 : 2 * (y₁ * (b - x₁ ^ 2)) = 0 := by
      have h3 : 2 * (y₁ * (b - x₁ ^ 2))
          = (y₁ * (b - x₁ ^ 2) / (c ^ 3 * x₁ ^ 2) + y₂ * (b - x₂ ^ 2) / (c ^ 3 * x₂ ^ 2))
              * (c ^ 3 * x₁ ^ 2) := by
        rw [hx12, hy12]
        field_simp
        ring
      rw [h3, hYsum, zero_mul]
    have hbx : b = x₁ ^ 2 := by
      rcases mul_eq_zero.mp (by linarith : y₁ * (b - x₁ ^ 2) = 0) with h0 | h0
      · exact absurd h0 hy0
      · linarith
    have h4 : x₁ * (x₁ * x₃) = nu ^ 2 := by
      rw [hx3, hx12]
      field_simp
    have h5 : 2 * (x₁ * x₃) + 2 * L * nu = 0 := by
      rw [hbx, hx12] at hbv
      linear_combination -hbv
    have hkey : nu * (L * x₁ + nu) = 0 := by
      linear_combination (-1 : ℚ) * h4 + (x₁ / 2) * h5
    rcases mul_eq_zero.mp hkey with h0 | h0
    · exact hnu h0
    · exact hy0 (by rw [hy1]; linarith)
  · -- the two summands differ by the exceptional point
    have hbp : b = x₁ * x₂ := by
      have h8 : (b - x₁ * x₂) * (x₁ * x₂) = nu * (2 * L * (x₁ * x₂) + nu * (x₁ + x₂)) := by
        rw [hbv, hx3]
        field_simp
        ring
      have h9 : (b - x₁ * x₂) * (x₁ * x₂) = 0 := by rw [h8, h, mul_zero]
      rcases mul_eq_zero.mp h9 with h10 | h10
      · linarith
      · exact absurd h10 (mul_ne_zero hx1 hx2)
    have hzero : nu * (x₂ - x₁) ^ 2 = 0 := by
      have h3 : nu * (x₂ - x₁) ^ 2
          = (y₁ * (b - x₁ ^ 2) / (c ^ 3 * x₁ ^ 2) + y₂ * (b - x₂ ^ 2) / (c ^ 3 * x₂ ^ 2))
              * (c ^ 3 * x₁ * x₂) := by
        rw [hbp, hy1, hy2]
        field_simp
        ring
      rw [h3, hYsum, zero_mul]
    rcases mul_eq_zero.mp hzero with h0 | h0
    · exact hnu h0
    · have hx12 : x₂ = x₁ := by
        have h7 : x₂ - x₁ = 0 := pow_eq_zero_iff (n := 2) (by norm_num) |>.mp h0
        linarith
      have hy12 : y₂ = y₁ := by rw [hy1, hy2, hx12]
      have hy0 : y₁ = 0 := by
        rw [hx12] at h
        rcases mul_eq_zero.mp (by linarith : x₁ * (L * x₁ + nu) = 0) with h6 | h6
        · exact absurd h6 hx1
        · rw [hy1]; linarith
      exact hne ⟨hx12.symm, by rw [hy0, hy12, hy0]; ring⟩

/-- Ordinary chord on the image curve, `X`-coordinate, in cleared form:
`(X₃ + A + X₁ + X₂)(X₁ − X₂)² = (Y₁ − Y₂)²`. -/
theorem core_chord_X {x₁ x₂ L nu c x₃ a b A y₁ y₂ y₃ : ℚ}
    (hx1 : x₁ ≠ 0) (hx2 : x₂ ≠ 0) (hnu : nu ≠ 0) (hc : c ≠ 0)
    (hx3 : x₃ = nu ^ 2 / (x₁ * x₂)) (ha : a = L ^ 2 - x₁ - x₂ - x₃)
    (hbv : b = x₁ * x₂ + x₁ * x₃ + x₂ * x₃ + 2 * L * nu)
    (hA : A = -2 * a / c ^ 2)
    (hy1 : y₁ = L * x₁ + nu) (hy2 : y₂ = L * x₂ + nu) (hy3 : y₃ = -(L * x₃ + nu)) :
    (y₃ ^ 2 / (c ^ 2 * x₃ ^ 2) + A + y₁ ^ 2 / (c ^ 2 * x₁ ^ 2) + y₂ ^ 2 / (c ^ 2 * x₂ ^ 2))
        * (y₁ ^ 2 / (c ^ 2 * x₁ ^ 2) - y₂ ^ 2 / (c ^ 2 * x₂ ^ 2)) ^ 2
      = (y₁ * (b - x₁ ^ 2) / (c ^ 3 * x₁ ^ 2) - y₂ * (b - x₂ ^ 2) / (c ^ 3 * x₂ ^ 2)) ^ 2 := by
  subst hy1 hy2 hy3 hA hbv ha hx3
  field_simp
  ring

/-- Ordinary chord on the image curve, `Y`-coordinate, in cleared form. -/
theorem core_chord_Y {x₁ x₂ L nu c x₃ b y₁ y₂ y₃ : ℚ}
    (hx1 : x₁ ≠ 0) (hx2 : x₂ ≠ 0) (hnu : nu ≠ 0) (hc : c ≠ 0)
    (hx3 : x₃ = nu ^ 2 / (x₁ * x₂))
    (hbv : b = x₁ * x₂ + x₁ * x₃ + x₂ * x₃ + 2 * L * nu)
    (hy1 : y₁ = L * x₁ + nu) (hy2 : y₂ = L * x₂ + nu) (hy3 : y₃ = -(L * x₃ + nu)) :
    (y₃ * (b - x₃ ^ 2) / (c ^ 3 * x₃ ^ 2) + y₁ * (b - x₁ ^ 2) / (c ^ 3 * x₁ ^ 2))
        * (y₁ ^ 2 / (c ^ 2 * x₁ ^ 2) - y₂ ^ 2 / (c ^ 2 * x₂ ^ 2))
      = -(y₁ * (b - x₁ ^ 2) / (c ^ 3 * x₁ ^ 2) - y₂ * (b - x₂ ^ 2) / (c ^ 3 * x₂ ^ 2))
          * (y₃ ^ 2 / (c ^ 2 * x₃ ^ 2) - y₁ ^ 2 / (c ^ 2 * x₁ ^ 2)) := by
  subst hy1 hy2 hy3 hbv hx3
  field_simp
  ring

/-- The two images coincide, so the image side is a tangent: `X`-coordinate, cleared form.
This happens either when the two summands coincide (`x₂ = x₁`, honest doubling) or when they
differ by the exceptional point (`2 L x₁ x₂ + ν (x₁ + x₂) = 0`); `hflat` covers both. -/
theorem core_tangent_X {x₁ x₂ L nu c x₃ a b A B y₁ y₂ y₃ : ℚ}
    (hx1 : x₁ ≠ 0) (hx2 : x₂ ≠ 0) (hnu : nu ≠ 0) (hc : c ≠ 0)
    (hflat : (x₂ - x₁) * (2 * L * (x₁ * x₂) + nu * (x₁ + x₂)) = 0)
    (hx3 : x₃ = nu ^ 2 / (x₁ * x₂)) (ha : a = L ^ 2 - x₁ - x₂ - x₃)
    (hbv : b = x₁ * x₂ + x₁ * x₃ + x₂ * x₃ + 2 * L * nu)
    (hA : A = -2 * a / c ^ 2) (hB : B = (a ^ 2 - 4 * b) / c ^ 4)
    (hy1 : y₁ = L * x₁ + nu) (hy2 : y₂ = L * x₂ + nu) (hy3 : y₃ = -(L * x₃ + nu)) :
    (y₃ ^ 2 / (c ^ 2 * x₃ ^ 2) + A + y₁ ^ 2 / (c ^ 2 * x₁ ^ 2) + y₂ ^ 2 / (c ^ 2 * x₂ ^ 2))
        * (2 * (y₁ * (b - x₁ ^ 2) / (c ^ 3 * x₁ ^ 2))) ^ 2
      = (3 * (y₁ ^ 2 / (c ^ 2 * x₁ ^ 2)) ^ 2 + 2 * A * (y₁ ^ 2 / (c ^ 2 * x₁ ^ 2)) + B) ^ 2 := by
  rcases mul_eq_zero.mp hflat with h | h
  · have hxx : x₂ = x₁ := by linarith
    subst hxx
    subst hy1 hy2 hy3 hA hB hbv ha hx3
    field_simp
    ring
  · have hLv : L = -nu * (x₁ + x₂) / (2 * (x₁ * x₂)) := by
      field_simp
      linarith
    subst hy1 hy2 hy3 hA hB hbv ha hx3 hLv
    field_simp
    ring

/-- The two images coincide: `Y`-coordinate, cleared form. -/
theorem core_tangent_Y {x₁ x₂ L nu c x₃ a b A B y₁ y₃ : ℚ}
    (hx1 : x₁ ≠ 0) (hx2 : x₂ ≠ 0) (hnu : nu ≠ 0) (hc : c ≠ 0)
    (hflat : (x₂ - x₁) * (2 * L * (x₁ * x₂) + nu * (x₁ + x₂)) = 0)
    (hx3 : x₃ = nu ^ 2 / (x₁ * x₂)) (ha : a = L ^ 2 - x₁ - x₂ - x₃)
    (hbv : b = x₁ * x₂ + x₁ * x₃ + x₂ * x₃ + 2 * L * nu)
    (hA : A = -2 * a / c ^ 2) (hB : B = (a ^ 2 - 4 * b) / c ^ 4)
    (hy1 : y₁ = L * x₁ + nu) (hy3 : y₃ = -(L * x₃ + nu)) :
    (y₃ * (b - x₃ ^ 2) / (c ^ 3 * x₃ ^ 2) + y₁ * (b - x₁ ^ 2) / (c ^ 3 * x₁ ^ 2))
        * (2 * (y₁ * (b - x₁ ^ 2) / (c ^ 3 * x₁ ^ 2)))
      = -(3 * (y₁ ^ 2 / (c ^ 2 * x₁ ^ 2)) ^ 2 + 2 * A * (y₁ ^ 2 / (c ^ 2 * x₁ ^ 2)) + B)
          * (y₃ ^ 2 / (c ^ 2 * x₃ ^ 2) - y₁ ^ 2 / (c ^ 2 * x₁ ^ 2)) := by
  rcases mul_eq_zero.mp hflat with h | h
  · have hxx : x₂ = x₁ := by linarith
    subst hxx
    subst hy1 hy3 hA hB hbv ha hx3
    field_simp
    ring
  · have hLv : L = -nu * (x₁ + x₂) / (2 * (x₁ * x₂)) := by
      field_simp
      linarith
    subst hy1 hy3 hA hB hbv ha hx3 hLv
    field_simp
    ring

/-- When the line through the two summands passes through the exceptional point — that is,
`ν = 0`, which is exactly when the sum lands in the exceptional fibre — the two images have the
same `X`-coordinate. -/
theorem core_exceptional_X {x₁ x₂ L c y₁ y₂ : ℚ}
    (hx1 : x₁ ≠ 0) (hx2 : x₂ ≠ 0) (hc : c ≠ 0)
    (hy1 : y₁ = L * x₁) (hy2 : y₂ = L * x₂) :
    y₁ ^ 2 / (c ^ 2 * x₁ ^ 2) = y₂ ^ 2 / (c ^ 2 * x₂ ^ 2) := by
  subst hy1 hy2
  field_simp

/-- …and, since then `b = x₁x₂`, opposite `Y`-coordinates: the two images are inverse, so their
sum is `O`, which is the value the map takes at the exceptional point. -/
theorem core_exceptional_Y {x₁ x₂ L c b y₁ y₂ : ℚ}
    (hx1 : x₁ ≠ 0) (hx2 : x₂ ≠ 0) (hc : c ≠ 0) (hbv : b = x₁ * x₂)
    (hy1 : y₁ = L * x₁) (hy2 : y₂ = L * x₂) :
    y₁ * (b - x₁ ^ 2) / (c ^ 3 * x₁ ^ 2) = -(y₂ * (b - x₂ ^ 2) / (c ^ 3 * x₂ ^ 2)) := by
  subst hy1 hy2 hbv
  field_simp
  ring

/-- Bridge to `Affine.addX` on the target curve in the chord case: the cleared identity is
exactly `addX X₁ X₂ ((Y₁ − Y₂)/(X₁ − X₂)) = X₃`. -/
theorem addX_eq_of_chord {A B X₁ X₂ Y₁ Y₂ X₃ : ℚ} (hX : X₁ ≠ X₂)
    (key : (X₃ + A + X₁ + X₂) * (X₁ - X₂) ^ 2 = (Y₁ - Y₂) ^ 2) :
    (Wab A B).toAffine.addX X₁ X₂ ((Wab A B).toAffine.slope X₁ X₂ Y₁ Y₂) = X₃ := by
  have hd : X₁ - X₂ ≠ 0 := sub_ne_zero.mpr hX
  rw [Affine.slope_of_X_ne hX]
  simp only [Affine.addX, Wab_a₁, Wab_a₂]
  field_simp
  linear_combination -key

/-- Bridge to `Affine.addY` on the target curve in the chord case. -/
theorem addY_eq_of_chord {A B X₁ X₂ Y₁ Y₂ X₃ Y₃ : ℚ} (hX : X₁ ≠ X₂)
    (keyX : (X₃ + A + X₁ + X₂) * (X₁ - X₂) ^ 2 = (Y₁ - Y₂) ^ 2)
    (keyY : (Y₃ + Y₁) * (X₁ - X₂) = -(Y₁ - Y₂) * (X₃ - X₁)) :
    (Wab A B).toAffine.addY X₁ X₂ Y₁ ((Wab A B).toAffine.slope X₁ X₂ Y₁ Y₂) = Y₃ := by
  have hd : X₁ - X₂ ≠ 0 := sub_ne_zero.mpr hX
  simp only [Affine.addY, Affine.negAddY, Wab_negY_eq]
  rw [addX_eq_of_chord hX keyX, Affine.slope_of_X_ne hX]
  field_simp
  linear_combination -keyY

/-- Bridge to `Affine.addX` on the target curve in the tangent case, where mathlib's `slope`
is `(3X₁² + 2AX₁ + B)/(2Y₁)`. -/
theorem addX_eq_of_tangent {A B X₁ X₂ Y₁ Y₂ X₃ : ℚ} (hX : X₁ = X₂)
    (hY : Y₁ ≠ (Wab A B).toAffine.negY X₂ Y₂) (hY0 : Y₁ ≠ 0)
    (key : (X₃ + A + X₁ + X₂) * (2 * Y₁) ^ 2 = (3 * X₁ ^ 2 + 2 * A * X₁ + B) ^ 2) :
    (Wab A B).toAffine.addX X₁ X₂ ((Wab A B).toAffine.slope X₁ X₂ Y₁ Y₂) = X₃ := by
  rw [Affine.slope_of_Y_ne hX hY, Wab_negY_eq]
  simp only [Affine.addX, Wab_a₁, Wab_a₂, Wab_a₄]
  field_simp
  linear_combination -key

/-- Bridge to `Affine.addY` on the target curve in the tangent case. -/
theorem addY_eq_of_tangent {A B X₁ X₂ Y₁ Y₂ X₃ Y₃ : ℚ} (hX : X₁ = X₂)
    (hY : Y₁ ≠ (Wab A B).toAffine.negY X₂ Y₂) (hY0 : Y₁ ≠ 0)
    (keyX : (X₃ + A + X₁ + X₂) * (2 * Y₁) ^ 2 = (3 * X₁ ^ 2 + 2 * A * X₁ + B) ^ 2)
    (keyY : (Y₃ + Y₁) * (2 * Y₁) = -(3 * X₁ ^ 2 + 2 * A * X₁ + B) * (X₃ - X₁)) :
    (Wab A B).toAffine.addY X₁ X₂ Y₁ ((Wab A B).toAffine.slope X₁ X₂ Y₁ Y₂) = Y₃ := by
  simp only [Affine.addY, Affine.negAddY, Wab_negY_eq]
  rw [addX_eq_of_tangent hX hY hY0 keyX, Affine.slope_of_Y_ne hX hY, Wab_negY_eq]
  simp only [Wab_a₁, Wab_a₂, Wab_a₄]
  field_simp
  linear_combination -keyY

/-- The target model has nonzero `b`-coefficient. -/
theorem gen_B_ne_zero {a b c B : ℚ} (hΔ : a ^ 2 - 4 * b ≠ 0) (hc : c ≠ 0)
    (hB : B = (a ^ 2 - 4 * b) / c ^ 4) : B ≠ 0 := by
  rw [hB]
  exact div_ne_zero hΔ (pow_ne_zero 4 hc)

/-- The target model satisfies the second nonsingularity condition: `A² − 4B = 16b/c⁴`. -/
theorem gen_disc_ne_zero {a b c A B : ℚ} (hb : b ≠ 0) (hc : c ≠ 0) (hA : A = -2 * a / c ^ 2)
    (hB : B = (a ^ 2 - 4 * b) / c ^ 4) : A ^ 2 - 4 * B ≠ 0 := by
  have h : A ^ 2 - 4 * B = 16 * b / c ^ 4 := by
    rw [hA, hB]
    field_simp
    ring
  rw [h]
  exact div_ne_zero (mul_ne_zero (by norm_num) hb) (pow_ne_zero 4 hc)

/-- The image coordinates satisfy the target equation.  This is `P03a.isogeny_core` with the
scaling parameter carried through. -/
theorem gen_coords_equation {a b c A B : ℚ} (hc : c ≠ 0) (hA : A = -2 * a / c ^ 2)
    (hB : B = (a ^ 2 - 4 * b) / c ^ 4) {x y : ℚ} (hx : x ≠ 0)
    (hy : y ^ 2 = x ^ 3 + a * x ^ 2 + b * x) :
    (y * (b - x ^ 2) / (c ^ 3 * x ^ 2)) ^ 2
      = (y ^ 2 / (c ^ 2 * x ^ 2)) ^ 3 + A * (y ^ 2 / (c ^ 2 * x ^ 2)) ^ 2
        + B * (y ^ 2 / (c ^ 2 * x ^ 2)) := by
  subst hA hB
  have hx2 : x ^ 2 ≠ 0 := pow_ne_zero 2 hx
  field_simp
  linear_combination isogeny_core a b x y hy

/-- The image of a nonsingular affine point with `x ≠ 0` is a nonsingular point of the target
model. -/
theorem gen_image_nonsingular {a b c A B : ℚ} (hb : b ≠ 0) (hΔ : a ^ 2 - 4 * b ≠ 0) (hc : c ≠ 0)
    (hA : A = -2 * a / c ^ 2) (hB : B = (a ^ 2 - 4 * b) / c ^ 4)
    {x y : ℚ} (h : (Wab a b).toAffine.Nonsingular x y) (hx : x ≠ 0) :
    (Wab A B).toAffine.Nonsingular (y ^ 2 / (c ^ 2 * x ^ 2))
      (y * (b - x ^ 2) / (c ^ 3 * x ^ 2)) := by
  refine (Affine.equation_iff_nonsingular_of_Δ_ne_zero
    (Wab_Δ_ne_zero (gen_B_ne_zero hΔ hc hB) (gen_disc_ne_zero hb hc hA hB))).mp ?_
  rw [Wab_equation_iff]
  exact gen_coords_equation hc hA hB hx ((Wab_equation_iff a b x y).mp h.left)

/-- The heart of the case analysis: two ordinary summands, with the third intersection point
of the line through them supplied together with the Vieta relations that `Affine.addX` and
`Descent.root_relations` provide.  Covers the tangent case, the ordinary chord, the case where
the sum lands in the exceptional fibre, and the case where the two images are inverse. -/
theorem gen_add_ordinary {a b c A B : ℚ} (hb : b ≠ 0) (hΔ : a ^ 2 - 4 * b ≠ 0) (hc : c ≠ 0)
    (hA : A = -2 * a / c ^ 2) (hB : B = (a ^ 2 - 4 * b) / c ^ 4)
    (f : (Wab a b).toAffine.Point → (Wab A B).toAffine.Point)
    (hfz : ∀ {y : ℚ} (h : (Wab a b).toAffine.Nonsingular 0 y), f (Affine.Point.some h) = 0)
    (hfs : ∀ {x y : ℚ} (h : (Wab a b).toAffine.Nonsingular x y) (hx : x ≠ 0),
      f (Affine.Point.some h) = Affine.Point.some (gen_image_nonsingular hb hΔ hc hA hB h hx))
    {x₁ y₁ x₂ y₂ x₃ y₃ L nu : ℚ}
    (h₁ : (Wab a b).toAffine.Nonsingular x₁ y₁) (h₂ : (Wab a b).toAffine.Nonsingular x₂ y₂)
    (h₃ : (Wab a b).toAffine.Nonsingular x₃ y₃) (hx₁ : x₁ ≠ 0) (hx₂ : x₂ ≠ 0)
    (hne : ¬(x₁ = x₂ ∧ y₁ = -y₂))
    (hy1 : y₁ = L * x₁ + nu) (hy2 : y₂ = L * x₂ + nu) (hy3 : y₃ = -(L * x₃ + nu))
    (hsum : x₁ + x₂ + x₃ = L ^ 2 - a) (hprod : x₁ * x₂ * x₃ = nu ^ 2)
    (hsym : x₁ * x₂ + x₁ * x₃ + x₂ * x₃ = b - 2 * L * nu) :
    f (Affine.Point.some h₃) = f (Affine.Point.some h₁) + f (Affine.Point.some h₂) := by
  have hx3v : x₃ = nu ^ 2 / (x₁ * x₂) := by
    field_simp
    linear_combination hprod
  have hav : a = L ^ 2 - x₁ - x₂ - x₃ := by linarith
  have hbv : b = x₁ * x₂ + x₁ * x₃ + x₂ * x₃ + 2 * L * nu := by linarith
  by_cases hx₃ : x₃ = 0
  · -- the sum lands in the exceptional fibre, where the map takes the value `O`
    have hnu : nu = 0 := by
      have h0 : nu ^ 2 = 0 := by rw [← hprod, hx₃]; ring
      exact pow_eq_zero_iff (n := 2) (by norm_num) |>.mp h0
    have hbp : b = x₁ * x₂ := by rw [hbv, hx₃, hnu]; ring
    have hz : f (Affine.Point.some h₃) = 0 := by
      subst hx₃
      exact hfz h₃
    rw [hz, hfs h₁ hx₁, hfs h₂ hx₂]
    refine (Affine.Point.add_of_Y_eq ?_ ?_).symm
    · exact core_exceptional_X hx₁ hx₂ hc (by rw [hy1, hnu]; ring) (by rw [hy2, hnu]; ring)
    · rw [Wab_negY_eq]
      exact core_exceptional_Y hx₁ hx₂ hc hbp (by rw [hy1, hnu]; ring) (by rw [hy2, hnu]; ring)
  · -- the sum is an ordinary point
    have hnu : nu ≠ 0 := by
      intro h0
      exact hx₃ (by rw [hx3v, h0]; ring)
    rw [hfs h₃ hx₃, hfs h₁ hx₁, hfs h₂ hx₂]
    by_cases himg : y₁ ^ 2 / (c ^ 2 * x₁ ^ 2) = y₂ ^ 2 / (c ^ 2 * x₂ ^ 2) ∧
        y₁ * (b - x₁ ^ 2) / (c ^ 3 * x₁ ^ 2)
          = (Wab A B).toAffine.negY (y₂ ^ 2 / (c ^ 2 * x₂ ^ 2))
              (y₂ * (b - x₂ ^ 2) / (c ^ 3 * x₂ ^ 2))
    · -- impossible: inverse images force the sum into the exceptional fibre
      exfalso
      have h2 := himg.2
      rw [Wab_negY_eq] at h2
      exact hnu (core_vertical_image hx₁ hx₂ hc hx3v hbv hy1 hy2 hne himg.1 h2)
    · rw [Affine.Point.add_some himg]
      by_cases hXX : y₁ ^ 2 / (c ^ 2 * x₁ ^ 2) = y₂ ^ 2 / (c ^ 2 * x₂ ^ 2)
      · -- the two images coincide: the image side is a tangent
        have hYne : y₁ * (b - x₁ ^ 2) / (c ^ 3 * x₁ ^ 2)
            ≠ (Wab A B).toAffine.negY (y₂ ^ 2 / (c ^ 2 * x₂ ^ 2))
                (y₂ * (b - x₂ ^ 2) / (c ^ 3 * x₂ ^ 2)) := fun h => himg ⟨hXX, h⟩
        have hYY : y₁ * (b - x₁ ^ 2) / (c ^ 3 * x₁ ^ 2)
            = y₂ * (b - x₂ ^ 2) / (c ^ 3 * x₂ ^ 2) :=
          Affine.Y_eq_of_Y_ne (gen_image_nonsingular hb hΔ hc hA hB h₁ hx₁).left
            (gen_image_nonsingular hb hΔ hc hA hB h₂ hx₂).left hXX hYne
        have hY0 : y₁ * (b - x₁ ^ 2) / (c ^ 3 * x₁ ^ 2) ≠ 0 := by
          intro h0
          apply hYne
          rw [Wab_negY_eq, ← hYY, h0]
          ring
        have hflat : (x₂ - x₁) * (2 * L * (x₁ * x₂) + nu * (x₁ + x₂)) = 0 := by
          have h2 : y₁ ^ 2 * x₂ ^ 2 - y₂ ^ 2 * x₁ ^ 2
              = (y₁ ^ 2 / (c ^ 2 * x₁ ^ 2) - y₂ ^ 2 / (c ^ 2 * x₂ ^ 2))
                  * (c ^ 2 * x₁ ^ 2 * x₂ ^ 2) := by
            field_simp
          have h3 : y₁ ^ 2 * x₂ ^ 2 - y₂ ^ 2 * x₁ ^ 2 = 0 := by
            rw [h2, sub_eq_zero.mpr hXX, zero_mul]
          rw [hy1, hy2] at h3
          have h4 : nu * ((x₂ - x₁) * (2 * L * (x₁ * x₂) + nu * (x₁ + x₂))) = 0 := by
            linear_combination h3
          exact (mul_eq_zero.mp h4).resolve_left hnu
        refine Wab_pt_eq _ _ ?_ ?_
        · exact (addX_eq_of_tangent hXX hYne hY0
            (core_tangent_X hx₁ hx₂ hnu hc hflat hx3v hav hbv hA hB hy1 hy2 hy3)).symm
        · exact (addY_eq_of_tangent hXX hYne hY0
            (core_tangent_X hx₁ hx₂ hnu hc hflat hx3v hav hbv hA hB hy1 hy2 hy3)
            (core_tangent_Y hx₁ hx₂ hnu hc hflat hx3v hav hbv hA hB hy1 hy3)).symm
      · -- the ordinary chord on the image side
        refine Wab_pt_eq _ _ ?_ ?_
        · exact (addX_eq_of_chord hXX
            (core_chord_X hx₁ hx₂ hnu hc hx3v hav hbv hA hy1 hy2 hy3)).symm
        · exact (addY_eq_of_chord hXX
            (core_chord_X hx₁ hx₂ hnu hc hx3v hav hbv hA hy1 hy2 hy3)
            (core_chord_Y hx₁ hx₂ hnu hc hx3v hbv hy1 hy2 hy3)).symm

/-- **Generic additivity.**  Any map presented by the three branch equations of the P03a
construction respects the group law.  Every case of `Affine.Point.add` occurs: either argument
`O`; an inverse/vertical pair; a summand in the exceptional fibre `x = 0`; doubling; the
ordinary chord; and the sum landing in the exceptional fibre although neither summand does. -/
theorem gen_additive {a b c A B : ℚ} (hb : b ≠ 0) (hΔ : a ^ 2 - 4 * b ≠ 0) (hc : c ≠ 0)
    (hA : A = -2 * a / c ^ 2) (hB : B = (a ^ 2 - 4 * b) / c ^ 4)
    (f : (Wab a b).toAffine.Point → (Wab A B).toAffine.Point)
    (hf0 : f 0 = 0)
    (hfz : ∀ {y : ℚ} (h : (Wab a b).toAffine.Nonsingular 0 y), f (Affine.Point.some h) = 0)
    (hfs : ∀ {x y : ℚ} (h : (Wab a b).toAffine.Nonsingular x y) (hx : x ≠ 0),
      f (Affine.Point.some h) = Affine.Point.some (gen_image_nonsingular hb hΔ hc hA hB h hx))
    (P Q : (Wab a b).toAffine.Point) : f (P + Q) = f P + f Q := by
  have hfz' : ∀ {x y : ℚ} (h : (Wab a b).toAffine.Nonsingular x y), x = 0 →
      f (Affine.Point.some h) = 0 := by
    rintro x y h rfl
    exact hfz h
  have hfs' : ∀ {x y X Y : ℚ} (h : (Wab a b).toAffine.Nonsingular x y)
      (h' : (Wab A B).toAffine.Nonsingular X Y), x ≠ 0 →
      X = y ^ 2 / (c ^ 2 * x ^ 2) → Y = y * (b - x ^ 2) / (c ^ 3 * x ^ 2) →
      f (Affine.Point.some h) = Affine.Point.some h' := by
    intro x y X Y h h' hx hX hY
    rw [hfs h hx]
    exact Wab_pt_eq _ _ hX.symm hY.symm
  rcases P with _ | @⟨x₁, y₁, h₁⟩
  · rw [show (Affine.Point.zero : (Wab a b).toAffine.Point) = 0 from rfl, zero_add, hf0, zero_add]
  rcases Q with _ | @⟨x₂, y₂, h₂⟩
  · rw [show (Affine.Point.zero : (Wab a b).toAffine.Point) = 0 from rfl, add_zero, hf0, add_zero]
  have he₁ : y₁ ^ 2 = x₁ ^ 3 + a * x₁ ^ 2 + b * x₁ := (Wab_equation_iff a b x₁ y₁).mp h₁.left
  have he₂ : y₂ ^ 2 = x₂ ^ 3 + a * x₂ ^ 2 + b * x₂ := (Wab_equation_iff a b x₂ y₂).mp h₂.left
  by_cases hx₁ : x₁ = 0
  · -- the first summand lies in the exceptional fibre
    subst hx₁
    have hy₁ : y₁ = 0 := Wab_x_eq_zero h₁.left
    subst hy₁
    rw [hfz' h₁ rfl, zero_add]
    by_cases hx₂ : x₂ = 0
    · subst hx₂
      have hy₂ : y₂ = 0 := Wab_x_eq_zero h₂.left
      subst hy₂
      rw [Affine.Point.add_of_Y_eq rfl (by rw [Wab_negY_eq]; ring), hf0, hfz' h₂ rfl]
    · have hxne : (0 : ℚ) ≠ x₂ := fun h => hx₂ h.symm
      rw [Affine.Point.add_of_X_ne hxne, hfs h₂ hx₂]
      have hL : (Wab a b).toAffine.slope 0 x₂ 0 y₂ = y₂ / x₂ := by
        rw [Affine.slope_of_X_ne hxne, zero_sub, zero_sub, neg_div_neg_eq]
      have hX3 : (Wab a b).toAffine.addX 0 x₂ ((Wab a b).toAffine.slope 0 x₂ 0 y₂) = b / x₂ := by
        rw [hL]
        simp only [Affine.addX, Wab_a₁, Wab_a₂]
        field_simp
        linear_combination he₂
      have hY3 : (Wab a b).toAffine.addY 0 x₂ 0 ((Wab a b).toAffine.slope 0 x₂ 0 y₂)
          = -(b * y₂ / x₂ ^ 2) := by
        simp only [Affine.addY, Affine.negAddY, Wab_negY_eq]
        rw [hX3, hL]
        field_simp
        ring
      refine hfs' _ _ ?_ ?_ ?_
      · rw [hX3]
        exact div_ne_zero hb hx₂
      · rw [hX3, hY3]
        field_simp
      · rw [hX3, hY3]
        field_simp
        ring
  by_cases hx₂ : x₂ = 0
  · -- the second summand lies in the exceptional fibre
    subst hx₂
    have hy₂ : y₂ = 0 := Wab_x_eq_zero h₂.left
    subst hy₂
    rw [hfz' h₂ rfl, add_zero, Affine.Point.add_of_X_ne hx₁, hfs h₁ hx₁]
    have hL : (Wab a b).toAffine.slope x₁ 0 y₁ 0 = y₁ / x₁ := by
      rw [Affine.slope_of_X_ne hx₁, sub_zero, sub_zero]
    have hX3 : (Wab a b).toAffine.addX x₁ 0 ((Wab a b).toAffine.slope x₁ 0 y₁ 0) = b / x₁ := by
      rw [hL]
      simp only [Affine.addX, Wab_a₁, Wab_a₂]
      field_simp
      linear_combination he₁
    have hY3 : (Wab a b).toAffine.addY x₁ 0 y₁ ((Wab a b).toAffine.slope x₁ 0 y₁ 0)
        = -(b * y₁ / x₁ ^ 2) := by
      simp only [Affine.addY, Affine.negAddY, Wab_negY_eq]
      rw [hX3, hL]
      field_simp
      ring
    refine hfs' _ _ ?_ ?_ ?_
    · rw [hX3]
      exact div_ne_zero hb hx₁
    · rw [hX3, hY3]
      field_simp
    · rw [hX3, hY3]
      field_simp
      ring
  -- both summands are ordinary points
  by_cases hxy : x₁ = x₂ ∧ y₁ = (Wab a b).toAffine.negY x₂ y₂
  · -- an inverse pair: the line is vertical and the sum is `O`
    obtain ⟨hx, hy⟩ := hxy
    rw [Wab_negY_eq] at hy
    subst hx
    rw [Affine.Point.add_of_Y_eq rfl (by rw [Wab_negY_eq]; exact hy), hf0, hfs h₁ hx₁,
      hfs h₂ hx₂]
    refine (Affine.Point.add_of_Y_eq ?_ ?_).symm
    · rw [hy]; ring
    · rw [Wab_negY_eq, hy]; ring
  · -- the chord and tangent cases
    have hne : ¬(x₁ = x₂ ∧ y₁ = -y₂) := by
      intro h
      exact hxy ⟨h.1, by rw [Wab_negY_eq]; exact h.2⟩
    rw [Affine.Point.add_some hxy]
    obtain ⟨hr1, hr2⟩ := root_relations h₁.left h₂.left hxy
    have hy1 : y₁ = (Wab a b).toAffine.slope x₁ x₂ y₁ y₂ * x₁
        + (y₁ - (Wab a b).toAffine.slope x₁ x₂ y₁ y₂ * x₁) := by ring
    have hy2 : y₂ = (Wab a b).toAffine.slope x₁ x₂ y₁ y₂ * x₂
        + (y₁ - (Wab a b).toAffine.slope x₁ x₂ y₁ y₂ * x₁) := by
      by_cases hx : x₁ = x₂
      · have hyy : y₁ = y₂ := Affine.Y_eq_of_Y_ne h₁.left h₂.left hx (fun h => hxy ⟨hx, h⟩)
        rw [← hyy, ← hx]; ring
      · have hd : x₁ - x₂ ≠ 0 := sub_ne_zero.mpr hx
        rw [Affine.slope_of_X_ne hx]
        field_simp
        ring
    have hy3 : (Wab a b).toAffine.addY x₁ x₂ y₁ ((Wab a b).toAffine.slope x₁ x₂ y₁ y₂)
        = -((Wab a b).toAffine.slope x₁ x₂ y₁ y₂
              * (Wab a b).toAffine.addX x₁ x₂ ((Wab a b).toAffine.slope x₁ x₂ y₁ y₂)
            + (y₁ - (Wab a b).toAffine.slope x₁ x₂ y₁ y₂ * x₁)) := by
      simp only [Affine.addY, Affine.negAddY, Wab_negY_eq]
      ring
    have hsum : x₁ + x₂ + (Wab a b).toAffine.addX x₁ x₂ ((Wab a b).toAffine.slope x₁ x₂ y₁ y₂)
        = (Wab a b).toAffine.slope x₁ x₂ y₁ y₂ ^ 2 - a := by
      simp only [Affine.addX, Wab_a₁, Wab_a₂]
      ring
    exact gen_add_ordinary hb hΔ hc hA hB f hfz hfs h₁ h₂ _ hx₁ hx₂ hne hy1 hy2 hy3 hsum hr1 hr2

/-- **Target.**  Both P03a point maps are additive.

`phiPoint` and `dualPhiPoint` are the total functions built in P03a; `hP` is the frozen
`Params`.  Nothing else is asserted: this is additivity only, on the nose, for the maps
exactly as they were defined. -/
theorem isogeny_point_maps_additive
    (ε : ℤ) (m q : ℕ) [Fact (Nat.Prime q)] (hP : Params ε m q) :
    (∀ P Q : (Ecurve ε m q).toAffine.Point,
        phiPoint hP (P + Q) = phiPoint hP P + phiPoint hP Q)
  ∧ (∀ P Q : (E'curve ε m q).toAffine.Point,
        dualPhiPoint hP (P + Q) = dualPhiPoint hP P + dualPhiPoint hP Q) := by
  constructor
  · refine gen_additive (a := dualA ε m q) (b := dualB ε m q) (c := 1) (A := phiA ε m q)
      (B := phiB ε m q) (dualB_ne_zero hP) (dualA_disc_ne_zero hP) one_ne_zero ?_ ?_
      (phiPoint hP) (phiPoint_zero hP) (fun h => phiPoint_some_of_x_eq_zero hP h) ?_
    · rw [family_phiA_eq]; norm_num
    · rw [family_phiB_eq]; norm_num
    · intro x y h hx
      refine (phiPoint_some_of_ne hP h hx).trans (Wab_pt_eq _ _ ?_ ?_)
      · simp only [phiX]; norm_num
      · simp only [phiY]; norm_num
  · refine gen_additive (a := phiA ε m q) (b := phiB ε m q) (c := 2) (A := dualA ε m q)
      (B := dualB ε m q) (phiB_ne_zero hP) (phiA_disc_ne_zero hP) two_ne_zero ?_ ?_
      (dualPhiPoint hP) (dualPhiPoint_zero hP) (fun h => dualPhiPoint_some_of_X_eq_zero hP h) ?_
    · have h := family_dualA_eq ε m q
      field_simp
      linarith
    · have h := family_dualB_eq ε m q
      field_simp
      linarith
    · intro X Y h hX
      refine (dualPhiPoint_some_of_ne hP h hX).trans (Wab_pt_eq _ _ ?_ ?_)
      · simp only [dualPhiX]; norm_num
      · simp only [dualPhiY]; norm_num

end P03b
