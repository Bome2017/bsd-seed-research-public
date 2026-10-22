import RequestProject.Descent.Ported
import RequestProject.SDyadic.Family

namespace P01

open Run013 SDyadic Descent WeierstrassCurve

/-! ## Integer identities of the normalisation (proved, not assumed) -/

theorem A_sq_sub_D (ε : ℤ) (m : ℕ) : (AA ε m) ^ 2 - DD ε m = 4 * (rr ε m) ^ 2 := by
  simp only [AA, DD]; ring

theorem dualA_disc_int (ε : ℤ) (m : ℕ) (q : ℕ) :
    (AA ε m * q) ^ 2 - 4 * (BB ε m * (q : ℤ) ^ 2) = DD ε m * (q : ℤ) ^ 2 := by
  linear_combination ((q : ℤ) ^ 2) * A_sq_sub_four_B ε m

theorem phiA_disc_int (ε : ℤ) (m : ℕ) (q : ℕ) :
    (-2 * AA ε m * q) ^ 2 - 4 * (DD ε m * (q : ℤ) ^ 2) = 16 * (rr ε m) ^ 2 * (q : ℤ) ^ 2 := by
  linear_combination (4 * (q : ℤ) ^ 2) * A_sq_sub_D ε m

theorem E'_root_q_int (ε : ℤ) (m : ℕ) (q : ℕ) :
    (0 : ℤ) ^ 2 = (q : ℤ) ^ 3 + (-2 * AA ε m * q) * (q : ℤ) ^ 2
      + (DD ε m * (q : ℤ) ^ 2) * (q : ℤ) := by
  linear_combination (-((q : ℤ) ^ 3)) * one_add_D ε m

theorem E'_root_Dq_int (ε : ℤ) (m : ℕ) (q : ℕ) :
    (0 : ℤ) ^ 2 = (DD ε m * q) ^ 3 + (-2 * AA ε m * q) * (DD ε m * (q : ℤ)) ^ 2
      + (DD ε m * (q : ℤ) ^ 2) * (DD ε m * q) := by
  linear_combination (-((DD ε m) ^ 2 * (q : ℤ) ^ 3)) * one_add_D ε m

/-! ## The two family curves as actual mathlib objects -/

variable (ε : ℤ) (m q : ℕ)

/-- `E_q : y² = x(x² + A q x + r² q²)`, an actual `WeierstrassCurve ℚ`. -/
def Ecurve : WeierstrassCurve ℚ := Wab (dualA ε m q) (dualB ε m q)

/-- `E'_q : Y² = X(X − q)(X − D q)`, an actual `WeierstrassCurve ℚ`.
The expansion `X(X−q)(X−Dq) = X(X² − 2AqX + Dq²)` is `SDyadic.quotient_model_expand`. -/
def E'curve : WeierstrassCurve ℚ := Wab (phiA ε m q) (phiB ε m q)

/-! ## Arithmetic facts from `Params` -/

variable {ε m q}

theorem rr_ne_zero (ε : ℤ) (m : ℕ) [Fact (Nat.Prime q)] (hP : Params ε m q) :
    rr ε m ≠ 0 := by
  rcases hP.eps_unit with h | h <;> simp [rr, h]

/-- `D ≠ 0`.  Unconditional: `D` is odd, so it is not zero. -/
theorem DD_ne_zero (ε : ℤ) (m : ℕ) : DD ε m ≠ 0 := by
  intro h
  obtain ⟨k, hk⟩ := D_odd ε m
  omega

theorem q_ne_zero' [Fact (Nat.Prime q)] (hP : Params ε m q) : (q : ℚ) ≠ 0 := by
  have := hP.q_pos
  exact_mod_cast this.ne'

/-- `D ≠ 1`.  `D = 1 − 4r` and `r ≠ 0`. -/
theorem DD_ne_one [Fact (Nat.Prime q)] (hP : Params ε m q) : DD ε m ≠ 1 := by
  intro h
  exact rr_ne_zero ε m hP (by simp only [DD] at h; omega)

/-! ## Nonsingularity of both models -/

theorem dualB_ne_zero [Fact (Nat.Prime q)] (hP : Params ε m q) : dualB ε m q ≠ 0 := by
  rw [dualB]
  have h1 : (BB ε m) ≠ 0 := by
    simpa [BB] using pow_ne_zero 2 (rr_ne_zero ε m hP)
  have h2 : (q : ℤ) ≠ 0 := by exact_mod_cast hP.q_pos.ne'
  exact_mod_cast mul_ne_zero h1 (pow_ne_zero 2 h2)

theorem phiB_ne_zero [Fact (Nat.Prime q)] (hP : Params ε m q) : phiB ε m q ≠ 0 := by
  rw [phiB]
  have h2 : (q : ℤ) ≠ 0 := by exact_mod_cast hP.q_pos.ne'
  exact_mod_cast mul_ne_zero (DD_ne_zero ε m) (pow_ne_zero 2 h2)

theorem dualA_disc_ne_zero [Fact (Nat.Prime q)] (hP : Params ε m q) :
    dualA ε m q ^ 2 - 4 * dualB ε m q ≠ 0 := by
  have hz : (AA ε m * q) ^ 2 - 4 * (BB ε m * (q : ℤ) ^ 2) ≠ 0 := by
    rw [dualA_disc_int]
    have h2 : (q : ℤ) ≠ 0 := by exact_mod_cast hP.q_pos.ne'
    exact mul_ne_zero (DD_ne_zero ε m) (pow_ne_zero 2 h2)
  rw [dualA, dualB]
  exact_mod_cast hz

theorem phiA_disc_ne_zero [Fact (Nat.Prime q)] (hP : Params ε m q) :
    phiA ε m q ^ 2 - 4 * phiB ε m q ≠ 0 := by
  have hz : (-2 * AA ε m * q) ^ 2 - 4 * (DD ε m * (q : ℤ) ^ 2) ≠ 0 := by
    rw [phiA_disc_int]
    have h2 : (q : ℤ) ≠ 0 := by exact_mod_cast hP.q_pos.ne'
    exact mul_ne_zero (mul_ne_zero (by norm_num) (pow_ne_zero 2 (rr_ne_zero ε m hP)))
      (pow_ne_zero 2 h2)
  rw [phiA, phiB]
  exact_mod_cast hz

theorem Ecurve_Δ_ne_zero [Fact (Nat.Prime q)] (hP : Params ε m q) : (Ecurve ε m q).Δ ≠ 0 :=
  Wab_Δ_ne_zero (dualB_ne_zero hP) (dualA_disc_ne_zero hP)

theorem E'curve_Δ_ne_zero [Fact (Nat.Prime q)] (hP : Params ε m q) : (E'curve ε m q).Δ ≠ 0 :=
  Wab_Δ_ne_zero (phiB_ne_zero hP) (phiA_disc_ne_zero hP)

/-! ## The marked rational points

`T = (0,0)` on `E_q`;  `T' = (0,0)`, `Q = (q,0)`, `R = (Dq,0)` on `E'_q`.

These are actual `WeierstrassCurve.Affine.Nonsingular` witnesses on the actual mathlib
models.  **Nothing here calls any of them a kernel.**  `φ` and `φ̂` do not exist yet; the
kernel statements belong to P03c. -/

theorem T_mem [Fact (Nat.Prime q)] (hP : Params ε m q) :
    (Ecurve ε m q).toAffine.Nonsingular 0 0 :=
  two_torsion_mem (dualB_ne_zero hP) (dualA_disc_ne_zero hP)

theorem T'_mem [Fact (Nat.Prime q)] (hP : Params ε m q) :
    (E'curve ε m q).toAffine.Nonsingular 0 0 :=
  two_torsion_mem (phiB_ne_zero hP) (phiA_disc_ne_zero hP)

theorem Q_mem [Fact (Nat.Prime q)] (hP : Params ε m q) :
    (E'curve ε m q).toAffine.Nonsingular (q : ℚ) 0 := by
  refine (Affine.equation_iff_nonsingular_of_Δ_ne_zero (E'curve_Δ_ne_zero hP)).mp ?_
  rw [E'curve, Wab_equation_iff, phiA, phiB]
  exact_mod_cast E'_root_q_int ε m q

theorem R_mem [Fact (Nat.Prime q)] (hP : Params ε m q) :
    (E'curve ε m q).toAffine.Nonsingular (((DD ε m : ℚ)) * (q : ℚ)) 0 := by
  refine (Affine.equation_iff_nonsingular_of_Δ_ne_zero (E'curve_Δ_ne_zero hP)).mp ?_
  rw [E'curve, Wab_equation_iff, phiA, phiB]
  exact_mod_cast E'_root_Dq_int ε m q

/-! ## The marked points as actual group elements

Named so that P03 can refer to them.  They depend on `hP` only through the nonsingularity
witness, and `Params` is a `Prop`, so any two proofs give the same point. -/

/-- `T = (0,0) ∈ E_q(ℚ)`. -/
noncomputable def Tpt [Fact (Nat.Prime q)] (hP : Params ε m q) :
    (Ecurve ε m q).toAffine.Point := Affine.Point.some (T_mem hP)

/-- `T' = (0,0) ∈ E'_q(ℚ)`. -/
noncomputable def T'pt [Fact (Nat.Prime q)] (hP : Params ε m q) :
    (E'curve ε m q).toAffine.Point := Affine.Point.some (T'_mem hP)

/-- `Q = (q,0) ∈ E'_q(ℚ)`. -/
noncomputable def Qpt [Fact (Nat.Prime q)] (hP : Params ε m q) :
    (E'curve ε m q).toAffine.Point := Affine.Point.some (Q_mem hP)

/-- `R = (Dq,0) ∈ E'_q(ℚ)`. -/
noncomputable def Rpt [Fact (Nat.Prime q)] (hP : Params ε m q) :
    (E'curve ε m q).toAffine.Point := Affine.Point.some (R_mem hP)

/-! ## Auxiliary lemmas for the classifications

All proved.  Nothing here is an isogeny, a kernel, or a descent map: these are statements
about negation, point equality, and roots of the defining cubic on the shape `Wab a b`. -/

/-- On a model with `a₁ = a₃ = 0`, negation on `y`-coordinates is `y ↦ -y`. -/
theorem Wab_negY_eq (a b x y : ℚ) : (Wab a b).toAffine.negY x y = -y := by
  simp [Affine.negY, Wab]

/-- An affine point of `Wab a b` is `2`-torsion exactly when its `y`-coordinate vanishes. -/
theorem Wab_two_torsion_some {a b x y : ℚ} (h : (Wab a b).toAffine.Nonsingular x y) :
    Affine.Point.some h + Affine.Point.some h = 0 ↔ y = 0 := by
  rw [add_eq_zero_iff_eq_neg, Affine.Point.neg_some, Affine.Point.some.injEq]
  constructor
  · rintro ⟨-, hy⟩
    rw [Wab_negY_eq] at hy
    linarith
  · rintro rfl
    exact ⟨rfl, by rw [Wab_negY_eq]; ring⟩

/-- Two affine points with the same coordinates are equal (`Nonsingular` is a `Prop`). -/
theorem Wab_pt_eq {a b x₁ y₁ x₂ y₂ : ℚ} (h₁ : (Wab a b).toAffine.Nonsingular x₁ y₁)
    (h₂ : (Wab a b).toAffine.Nonsingular x₂ y₂) (hx : x₁ = x₂) (hy : y₁ = y₂) :
    Affine.Point.some h₁ = Affine.Point.some h₂ := by
  subst hx; subst hy; rfl

/-- An affine point of `Wab a b` with `y = 0` has `x` a root of `x(x² + a x + b)`. -/
theorem Wab_root_of_y_zero {a b x : ℚ} (h : (Wab a b).toAffine.Nonsingular x 0) :
    x * (x ^ 2 + a * x + b) = 0 := by
  have := (Wab_equation_iff a b x 0).mp h.left
  linarith [this]

/-- `D` is not the square of a rational number: it is an integer, so a rational square root
would make it an integer square, hence a square in `ZMod q`, contradicting
`Params.legendre_D_q`. -/
theorem DD_not_rat_sq [Fact (Nat.Prime q)] (hP : Params ε m q) (u : ℚ) :
    u ^ 2 ≠ ((DD ε m : ℤ) : ℚ) := by
  intro hu
  have hsqQ : IsSquare (((DD ε m : ℤ) : ℚ)) := ⟨u, by rw [← hu]; ring⟩
  obtain ⟨n, hn⟩ := Rat.isSquare_intCast_iff.mp hsqQ
  have hsq : IsSquare ((DD ε m : ℤ) : ZMod q) := ⟨(n : ZMod q), by rw [hn]; push_cast; ring⟩
  exact ((legendreSym.eq_neg_one_iff q).mp hP.legendre_D_q) hsq

/-- The discriminant of the quadratic factor of `E_q`, over `ℚ`. -/
theorem dualA_disc_rat :
    (dualA ε m q) ^ 2 - 4 * dualB ε m q = ((DD ε m : ℤ) : ℚ) * (q : ℚ) ^ 2 := by
  rw [dualA, dualB]
  exact_mod_cast dualA_disc_int ε m q

/-- The cubic of `E'_q` factors over `ℚ` as `X(X − q)(X − Dq)`. -/
theorem E'curve_cubic_factor (x : ℚ) :
    x * (x - (q : ℚ)) * (x - ((DD ε m : ℤ) : ℚ) * (q : ℚ))
      = x * (x ^ 2 + phiA ε m q * x + phiB ε m q) := by
  have h1 : (1 : ℚ) + ((DD ε m : ℤ) : ℚ) = 2 * ((AA ε m : ℤ) : ℚ) := by
    exact_mod_cast one_add_D ε m
  rw [phiA, phiB]
  push_cast
  linear_combination (-(x ^ 2 * (q : ℚ))) * h1

/-! ## The exact rational 2-torsion sets

`{O, T}` and `{O, T', Q, R}` are **2-torsion sets**.  They are not kernels; no isogeny is
defined or referred to here. -/

/-- **Exact rational 2-torsion of `E_q`**: `E_q(ℚ)[2] = {O, T}`. -/
theorem Ecurve_two_torsion [Fact (Nat.Prime q)] (hP : Params ε m q)
    (P : (Ecurve ε m q).toAffine.Point) : P + P = 0 ↔ P = 0 ∨ P = Tpt hP := by
  constructor
  · intro hPP
    cases P with
    | zero => exact Or.inl rfl
    | @some x y h =>
        have hy : y = 0 := (Wab_two_torsion_some h).mp hPP
        subst hy
        have hroot : x * (x ^ 2 + dualA ε m q * x + dualB ε m q) = 0 := Wab_root_of_y_zero h
        by_cases hx : x = 0
        · subst hx
          exact Or.inr (Wab_pt_eq h (T_mem hP) rfl rfl)
        · exfalso
          have hquad : x ^ 2 + dualA ε m q * x + dualB ε m q = 0 :=
            (mul_eq_zero.mp hroot).resolve_left hx
          have hq : (q : ℚ) ≠ 0 := q_ne_zero' hP
          have hsq : (2 * x + dualA ε m q) ^ 2 = ((DD ε m : ℤ) : ℚ) * (q : ℚ) ^ 2 := by
            rw [← dualA_disc_rat (ε := ε) (m := m) (q := q)]
            linear_combination 4 * hquad
          refine DD_not_rat_sq hP ((2 * x + dualA ε m q) / (q : ℚ)) ?_
          field_simp
          linear_combination hsq
  · rintro (rfl | rfl)
    · simp
    · exact (Wab_two_torsion_some (T_mem hP)).mpr rfl

/-- **Exact rational 2-torsion of `E'_q`**: `E'_q(ℚ)[2] = {O, T', Q, R}`. -/
theorem E'curve_two_torsion [Fact (Nat.Prime q)] (hP : Params ε m q)
    (P : (E'curve ε m q).toAffine.Point) :
    P + P = 0 ↔ P = 0 ∨ P = T'pt hP ∨ P = Qpt hP ∨ P = Rpt hP := by
  constructor
  · intro hPP
    cases P with
    | zero => exact Or.inl rfl
    | @some x y h =>
        have hy : y = 0 := (Wab_two_torsion_some h).mp hPP
        subst hy
        have hfac : x * (x - (q : ℚ)) * (x - ((DD ε m : ℤ) : ℚ) * (q : ℚ)) = 0 := by
          rw [E'curve_cubic_factor (ε := ε) (m := m) (q := q) x]
          exact Wab_root_of_y_zero h
        rcases mul_eq_zero.mp hfac with h0 | h0
        · rcases mul_eq_zero.mp h0 with h1 | h1
          · exact Or.inr (Or.inl (Wab_pt_eq h (T'_mem hP) h1 rfl))
          · exact Or.inr (Or.inr (Or.inl (Wab_pt_eq h (Q_mem hP) (by linarith) rfl)))
        · exact Or.inr (Or.inr (Or.inr (Wab_pt_eq h (R_mem hP) (by linarith) rfl)))
  · rintro (rfl | rfl | rfl | rfl)
    · simp
    · exact (Wab_two_torsion_some (T'_mem hP)).mpr rfl
    · exact (Wab_two_torsion_some (Q_mem hP)).mpr rfl
    · exact (Wab_two_torsion_some (R_mem hP)).mpr rfl

/-! ## The marked points are nonzero and pairwise distinct -/

theorem Tpt_ne_zero [Fact (Nat.Prime q)] (hP : Params ε m q) : Tpt hP ≠ 0 := by
  simp [Tpt]

theorem T'pt_ne_zero [Fact (Nat.Prime q)] (hP : Params ε m q) : T'pt hP ≠ 0 := by
  simp [T'pt]

theorem Qpt_ne_zero [Fact (Nat.Prime q)] (hP : Params ε m q) : Qpt hP ≠ 0 := by
  simp [Qpt]

theorem Rpt_ne_zero [Fact (Nat.Prime q)] (hP : Params ε m q) : Rpt hP ≠ 0 := by
  simp [Rpt]

theorem T'pt_ne_Qpt [Fact (Nat.Prime q)] (hP : Params ε m q) : T'pt hP ≠ Qpt hP := by
  intro hEq
  rw [T'pt, Qpt, Affine.Point.some.injEq] at hEq
  exact q_ne_zero' hP hEq.1.symm

theorem T'pt_ne_Rpt [Fact (Nat.Prime q)] (hP : Params ε m q) : T'pt hP ≠ Rpt hP := by
  intro hEq
  rw [T'pt, Rpt, Affine.Point.some.injEq] at hEq
  rcases mul_eq_zero.mp hEq.1.symm with h | h
  · exact DD_ne_zero ε m (by exact_mod_cast h)
  · exact q_ne_zero' hP h

theorem Qpt_ne_Rpt [Fact (Nat.Prime q)] (hP : Params ε m q) : Qpt hP ≠ Rpt hP := by
  intro hEq
  rw [Qpt, Rpt, Affine.Point.some.injEq] at hEq
  have h2 : (((DD ε m : ℤ) : ℚ) - 1) * (q : ℚ) = 0 := by linear_combination -hEq.1
  rcases mul_eq_zero.mp h2 with h | h
  · exact DD_ne_one hP (by exact_mod_cast (by linarith : ((DD ε m : ℤ) : ℚ) = 1))
  · exact q_ne_zero' hP h

/-! ## The P01 target

One theorem.  Its first nine conjuncts are discharged by the proved lemmas above; the real
content is the last two, the **exact** rational 2-torsion classifications.

For `E_q` the obstruction is the one already sitting in `Params`.  A rational 2-torsion point
other than `O` and `T` would give a rational root of `x² + A q x + r² q²`, hence make its
discriminant `(Aq)² − 4r²q² = q²·D` a rational square, hence make `D` a rational square,
hence a square mod `q`.  But `Params.legendre_D_q` says `legendreSym q D = -1`, and
`Params.q_not_dvd_twoD` gives `q ∤ D`.  Contradiction.  `dualA_disc_int` above is exactly
that discriminant identity.

For `E'_q` all three roots `0, q, Dq` of the cubic are already rational, already marked, and
pairwise distinct, so the work is the exhaustive classification, not an obstruction.

In both cases a point of the actual group is 2-torsion iff it equals its own negation, and on
a model with `a₁ = a₃ = 0` that is exactly `y = 0`.

NOT in this theorem, and not to be added: `φ`, `φ̂`, any isogeny, any kernel claim about
`{O,T}` or `{O,T'}`, any descent-map kernel, `E(ℚ)/2E(ℚ)`, `Sel₂`, Ш, rank, BSD. -/
theorem p01_family_two_torsion (ε : ℤ) (m q : ℕ) [Fact (Nat.Prime q)] (hP : Params ε m q) :
    -- (1) both models are nonsingular
    (Ecurve ε m q).Δ ≠ 0
  ∧ (E'curve ε m q).Δ ≠ 0
    -- (2) the four marked points are genuine nonzero elements of the actual groups
  ∧ Tpt hP ≠ 0
  ∧ T'pt hP ≠ 0
  ∧ Qpt hP ≠ 0
  ∧ Rpt hP ≠ 0
    -- (3) the three marked points on E'_q are pairwise distinct
  ∧ T'pt hP ≠ Qpt hP
  ∧ T'pt hP ≠ Rpt hP
  ∧ Qpt hP ≠ Rpt hP
    -- (4) EXACT rational 2-torsion of E_q :  { O , T }
  ∧ (∀ P : (Ecurve ε m q).toAffine.Point, P + P = 0 ↔ P = 0 ∨ P = Tpt hP)
    -- (5) EXACT rational 2-torsion of E'_q :  { O , T' , Q , R }
  ∧ (∀ P : (E'curve ε m q).toAffine.Point,
        P + P = 0 ↔ P = 0 ∨ P = T'pt hP ∨ P = Qpt hP ∨ P = Rpt hP) := by
  refine ⟨Ecurve_Δ_ne_zero hP, E'curve_Δ_ne_zero hP, Tpt_ne_zero hP, T'pt_ne_zero hP,
    Qpt_ne_zero hP, Rpt_ne_zero hP, T'pt_ne_Qpt hP, T'pt_ne_Rpt hP, Qpt_ne_Rpt hP,
    Ecurve_two_torsion hP, E'curve_two_torsion hP⟩

end P01
