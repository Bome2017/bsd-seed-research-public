import RequestProject.P01.PortedRunB

namespace P03a

open Run013 SDyadic Descent P01 WeierstrassCurve

/-! ## The classical coordinate formulas

For `E : y² = x(x² + a x + b)` with the rational two-torsion point `T = (0,0)`, the 2-isogeny
with kernel `⟨T⟩` onto `E' : Y² = X(X² + a' X + b')`, where `a' = −2a` and `b' = a² − 4b`, is
given on affine points with `x ≠ 0` by

    X = y²/x²,        Y = y(b − x²)/x².

For the frozen family this is `E_q → E'_q`: with `(a,b) = (dualA, dualB)`,
`a' = −2·Aq = phiA` and `b' = (Aq)² − 4r²q² = D q² = phiB`, the last equality being the
shipped `P01.dualA_disc_int`.

The dual runs `E'_q → E_q`.  Applying the same construction to `E'` lands on
`y² = x(x² + 4a x + 16b)`, which is `E` after `(u,v) ↦ (u/4, v/8)`; composing gives

    x = Y²/(4X²),     y = Y(b' − X²)/(8X²).

Here `4·dualA = −2·phiA` and `16·dualB = phiA² − 4·phiB`, the latter being the shipped
`P01.phiA_disc_int`.

These are **coordinate** functions only.  Nothing here is a group homomorphism, a kernel, or
an isogeny in any formal sense — see `FORMALIZATION_BOUNDARY.md`. -/

/-- `X`-coordinate of `φ` at an affine point with `x ≠ 0`. -/
def phiX (x y : ℚ) : ℚ := y ^ 2 / x ^ 2

/-- `Y`-coordinate of `φ` at an affine point with `x ≠ 0`.  `b` is the source curve's `b`. -/
def phiY (b x y : ℚ) : ℚ := y * (b - x ^ 2) / x ^ 2

/-- `x`-coordinate of `φ̂` at an affine point with `X ≠ 0`. -/
def dualPhiX (X Y : ℚ) : ℚ := Y ^ 2 / (4 * X ^ 2)

/-- `y`-coordinate of `φ̂` at an affine point with `X ≠ 0`.  `b'` is the source curve's `b`. -/
def dualPhiY (b' X Y : ℚ) : ℚ := Y * (b' - X ^ 2) / (8 * X ^ 2)

/-! ## Auxiliary lemmas

The polynomial core of both coordinate formulas, and the two family parameter matchings.
All proved; nothing here is a homomorphism, a kernel, or a composite. -/

/-- The polynomial core, obtained from the source equation `y² = x³ + a x² + b x` together
with the pivotal identity `(x²+ax+b)² − 2ax(x²+ax+b) + (a²−4b)x² = (x²−b)²`. -/
theorem isogeny_core (a b x y : ℚ) (hy : y ^ 2 = x ^ 3 + a * x ^ 2 + b * x) :
    y ^ 2 * (b - x ^ 2) ^ 2 * x ^ 2
      = (y ^ 2) ^ 3 - 2 * a * (y ^ 2) ^ 2 * x ^ 2 + (a ^ 2 - 4 * b) * y ^ 2 * x ^ 4 := by
  linear_combination (-y ^ 4 + (2 * a * x ^ 2 - (x ^ 3 + a * x ^ 2 + b * x)) * y ^ 2) * hy

/-- Generic `φ`: the image coordinates satisfy `Y² = X³ + a'X² + b'X` whenever
`a' = −2a`, `b' = a² − 4b` and the source coordinates satisfy `y² = x³ + a x² + b x`. -/
theorem phi_coords_equation {a b a' b' x y : ℚ} (hx : x ≠ 0)
    (ha' : a' = -2 * a) (hb' : b' = a ^ 2 - 4 * b)
    (hy : y ^ 2 = x ^ 3 + a * x ^ 2 + b * x) :
    phiY b x y ^ 2 = phiX x y ^ 3 + a' * phiX x y ^ 2 + b' * phiX x y := by
  subst ha' hb'
  simp only [phiX, phiY]
  have hx2 : x ^ 2 ≠ 0 := pow_ne_zero 2 hx
  field_simp
  linear_combination isogeny_core a b x y hy

/-- Generic `φ̂`: the same construction on the target model, composed with the rescaling
`(u,v) ↦ (u/4, v/8)`, which is where the `4` and the `8` come from. -/
theorem dualPhi_coords_equation {a b a' b' X Y : ℚ} (hX : X ≠ 0)
    (ha : 4 * a = -2 * a') (hb : 16 * b = a' ^ 2 - 4 * b')
    (hY : Y ^ 2 = X ^ 3 + a' * X ^ 2 + b' * X) :
    dualPhiY b' X Y ^ 2
      = dualPhiX X Y ^ 3 + a * dualPhiX X Y ^ 2 + b * dualPhiX X Y := by
  simp only [dualPhiX, dualPhiY]
  have hX2 : X ^ 2 ≠ 0 := pow_ne_zero 2 hX
  have ha2 : a = -a' / 2 := by linarith
  have hb2 : b = (a' ^ 2 - 4 * b') / 16 := by linarith
  subst ha2 hb2
  field_simp
  linear_combination (2048 : ℚ) * isogeny_core a' b' X Y hY

/-- `phiA = −2·dualA` for the frozen family. -/
theorem family_phiA_eq (ε : ℤ) (m q : ℕ) : phiA ε m q = -2 * dualA ε m q := by
  simp only [phiA, dualA]; push_cast; ring

/-- `phiB = dualA² − 4·dualB` for the frozen family, by `P01.dualA_disc_int`. -/
theorem family_phiB_eq (ε : ℤ) (m q : ℕ) :
    phiB ε m q = dualA ε m q ^ 2 - 4 * dualB ε m q := by
  have h := dualA_disc_int ε m q
  simp only [phiB, dualA, dualB]
  exact_mod_cast h.symm

/-- `4·dualA = −2·phiA` for the frozen family. -/
theorem family_dualA_eq (ε : ℤ) (m q : ℕ) : 4 * dualA ε m q = -2 * phiA ε m q := by
  simp only [phiA, dualA]; push_cast; ring

/-- `16·dualB = phiA² − 4·phiB` for the frozen family, by `P01.phiA_disc_int`. -/
theorem family_dualB_eq (ε : ℤ) (m q : ℕ) :
    16 * dualB ε m q = phiA ε m q ^ 2 - 4 * phiB ε m q := by
  have hz : 16 * (BB ε m * (q : ℤ) ^ 2)
      = (-2 * AA ε m * q) ^ 2 - 4 * (DD ε m * (q : ℤ) ^ 2) := by
    rw [phiA_disc_int]; simp only [BB]; ring
  simp only [phiA, phiB, dualB]
  exact_mod_cast hz

/-! ## The P03a target

**One theorem.**  Both coordinate formulas send an actual nonsingular point of one family
curve to an actual nonsingular point of the other.

That is the whole of P03a: it is exactly what "every branch constructs a valid
`Affine.Point`" means, because `WeierstrassCurve.Affine.Point.some` takes precisely a
`Nonsingular` witness.  The total point maps below are wired from it, and their branch
lemmas follow by `rfl` / `dif_pos` / `dif_neg`.

**Intended route.**  Both models have nonzero discriminant (`P01.Ecurve_Δ_ne_zero`,
`P01.E'curve_Δ_ne_zero`), so `Affine.equation_iff_nonsingular_of_Δ_ne_zero` reduces each side
to `Equation`, and `Descent.Wab_equation_iff` unfolds that to the plain cubic.  The φ side is
then the identity

    (x² + a x + b)(x² − b)²  =  x³ · (X² + a' X + b')·X       with  X = (x²+ax+b)/x,

which reduces to `(x² + a x + b)² − 2a x (x² + a x + b) + (a² − 4b)x² = (x² − b)²`.  Substitute
the source equation `y² = x³ + a x² + b x` and clear denominators with `x ≠ 0`; `field_simp`
followed by `linear_combination` on the source equation is the expected shape.  The dual side
is the same computation on `E'` composed with the `(u,v) ↦ (u/4, v/8)` rescaling, which is
where the `4` and `8` come from.

**Not in this theorem, and not to be added:** `φ(P+Q) = φ(P)+φ(Q)`, any kernel claim,
`φ̂ ∘ φ = [2]`, `φ ∘ φ̂ = [2]`, base change, `ker δ = im φ`, `E(ℚ)/2E(ℚ)`, `Sel₂`, Ш, rank,
BSD.  Those are P03b–P03e and beyond. -/
theorem isogeny_coords_nonsingular (ε : ℤ) (m q : ℕ) [Fact (Nat.Prime q)] (hP : Params ε m q) :
    (∀ x y : ℚ, (Ecurve ε m q).toAffine.Nonsingular x y → x ≠ 0 →
        (E'curve ε m q).toAffine.Nonsingular (phiX x y) (phiY (dualB ε m q) x y))
  ∧ (∀ X Y : ℚ, (E'curve ε m q).toAffine.Nonsingular X Y → X ≠ 0 →
        (Ecurve ε m q).toAffine.Nonsingular (dualPhiX X Y) (dualPhiY (phiB ε m q) X Y)) := by
  refine ⟨fun x y h hx => ?_, fun X Y h hX => ?_⟩
  · have he : (Wab (dualA ε m q) (dualB ε m q)).toAffine.Equation x y :=
      (Affine.equation_iff_nonsingular_of_Δ_ne_zero (Ecurve_Δ_ne_zero hP)).mpr h
    rw [Wab_equation_iff] at he
    refine (Affine.equation_iff_nonsingular_of_Δ_ne_zero (E'curve_Δ_ne_zero hP)).mp ?_
    show (Wab (phiA ε m q) (phiB ε m q)).toAffine.Equation _ _
    rw [Wab_equation_iff]
    exact phi_coords_equation hx (family_phiA_eq ε m q) (family_phiB_eq ε m q) he
  · have he : (Wab (phiA ε m q) (phiB ε m q)).toAffine.Equation X Y :=
      (Affine.equation_iff_nonsingular_of_Δ_ne_zero (E'curve_Δ_ne_zero hP)).mpr h
    rw [Wab_equation_iff] at he
    refine (Affine.equation_iff_nonsingular_of_Δ_ne_zero (Ecurve_Δ_ne_zero hP)).mp ?_
    show (Wab (dualA ε m q) (dualB ε m q)).toAffine.Equation _ _
    rw [Wab_equation_iff]
    exact dualPhi_coords_equation hX (family_dualA_eq ε m q) (family_dualB_eq ε m q) he

/-! ## The total point maps

Defined on mathlib's own `WeierstrassCurve.Affine.Point`, so they are **total**: the point at
infinity and the exceptional affine point are real branches, not side conditions. -/

/-- `φ : E_q(ℚ) → E'_q(ℚ)` as a total function on the actual point types.
`O ↦ O`; the exceptional point `x = 0` (which is `T`, since `x = 0` forces `y = 0`) `↦ O`;
otherwise the classical coordinate formula. -/
noncomputable def phiPoint {ε : ℤ} {m q : ℕ} [Fact (Nat.Prime q)] (hP : Params ε m q) :
    (Ecurve ε m q).toAffine.Point → (E'curve ε m q).toAffine.Point
  | .zero => 0
  | @Affine.Point.some _ _ _ x y h =>
      if hx : x = 0 then 0
      else Affine.Point.some ((isogeny_coords_nonsingular ε m q hP).1 x y h hx)

/-- `φ̂ : E'_q(ℚ) → E_q(ℚ)` as a total function.  `O ↦ O`; `X = 0` (the point `T'`) `↦ O`;
otherwise the classical coordinate formula. -/
noncomputable def dualPhiPoint {ε : ℤ} {m q : ℕ} [Fact (Nat.Prime q)] (hP : Params ε m q) :
    (E'curve ε m q).toAffine.Point → (Ecurve ε m q).toAffine.Point
  | .zero => 0
  | @Affine.Point.some _ _ _ X Y h =>
      if hX : X = 0 then 0
      else Affine.Point.some ((isogeny_coords_nonsingular ε m q hP).2 X Y h hX)

/-! ## Branch lemmas -/

@[simp] theorem phiPoint_zero {ε : ℤ} {m q : ℕ} [Fact (Nat.Prime q)] (hP : Params ε m q) :
    phiPoint hP 0 = 0 := rfl

@[simp] theorem dualPhiPoint_zero {ε : ℤ} {m q : ℕ} [Fact (Nat.Prime q)] (hP : Params ε m q) :
    dualPhiPoint hP 0 = 0 := rfl

theorem phiPoint_some_of_x_eq_zero {ε : ℤ} {m q : ℕ} [Fact (Nat.Prime q)]
    (hP : Params ε m q) {y : ℚ} (h : (Ecurve ε m q).toAffine.Nonsingular 0 y) :
    phiPoint hP (Affine.Point.some h) = 0 := by
  simp [phiPoint]

theorem dualPhiPoint_some_of_X_eq_zero {ε : ℤ} {m q : ℕ} [Fact (Nat.Prime q)]
    (hP : Params ε m q) {Y : ℚ} (h : (E'curve ε m q).toAffine.Nonsingular 0 Y) :
    dualPhiPoint hP (Affine.Point.some h) = 0 := by
  simp [dualPhiPoint]

theorem phiPoint_some_of_ne {ε : ℤ} {m q : ℕ} [Fact (Nat.Prime q)] (hP : Params ε m q)
    {x y : ℚ} (h : (Ecurve ε m q).toAffine.Nonsingular x y) (hx : x ≠ 0) :
    phiPoint hP (Affine.Point.some h)
      = Affine.Point.some ((isogeny_coords_nonsingular ε m q hP).1 x y h hx) :=
  dif_neg hx

theorem dualPhiPoint_some_of_ne {ε : ℤ} {m q : ℕ} [Fact (Nat.Prime q)] (hP : Params ε m q)
    {X Y : ℚ} (h : (E'curve ε m q).toAffine.Nonsingular X Y) (hX : X ≠ 0) :
    dualPhiPoint hP (Affine.Point.some h)
      = Affine.Point.some ((isogeny_coords_nonsingular ε m q hP).2 X Y h hX) :=
  dif_neg hX

/-! ## The exceptional fibres, named -/

@[simp] theorem phiPoint_Tpt {ε : ℤ} {m q : ℕ} [Fact (Nat.Prime q)] (hP : Params ε m q) :
    phiPoint hP (Tpt hP) = 0 :=
  phiPoint_some_of_x_eq_zero hP (T_mem hP)

@[simp] theorem dualPhiPoint_T'pt {ε : ℤ} {m q : ℕ} [Fact (Nat.Prime q)] (hP : Params ε m q) :
    dualPhiPoint hP (T'pt hP) = 0 :=
  dualPhiPoint_some_of_X_eq_zero hP (T'_mem hP)

end P03a
