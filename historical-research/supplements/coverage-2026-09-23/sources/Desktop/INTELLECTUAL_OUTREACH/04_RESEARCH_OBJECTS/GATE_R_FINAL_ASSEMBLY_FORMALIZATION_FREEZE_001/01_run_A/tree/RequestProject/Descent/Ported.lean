/-
`Descent/Ported.lean`

Three helper lemmas carried over from the **Run A** Delta development into the **Run B**
base, as recommended by `CONTINUATION_BASE_ASSESSMENT.md` in
`DELTA_DESCENT_FORMALIZATION_FREEZE_002`.

Run B's `Delta.lean` is the successor base because its representative `dval` is
coordinate-level and its core lemma `dval_prod_sq` is stated on bare rationals, so both
re-instantiate on a second curve unchanged.  Run A nonetheless proved three things Run B
did not expose, and they are the pieces P03 will want:

  * `vieta_of_eval`        — curve-free monic-cubic coefficients ↔ root symmetric functions;
  * `qcl_eq_cls_of_sqEq`   — square-class transport between `ℚˣ` (`qcl`) and `ℚ` (`cls`);
  * `dval_mem_kummerImage` — the forward inclusion into the **certified** `KummerImage`,
    here restated for Run B's `dval` in place of Run A's point-indexed `dnum`.

The first two are Run A's text verbatim.  The third is the Run A statement rebased.

NOTHING here is used by the P01 target.  These are carried so that the successor base is
assembled once, and are proved here so that P03 does not have to re-derive them.
-/
import RequestProject.Descent.Delta

namespace Descent

open Run013 WeierstrassCurve

/-! ## Ported verbatim from Run A -/

/-- From the intersection identity holding for **all** `t`, both Vieta relations.
Curve-free: this is a statement about six rationals. -/
theorem vieta_of_eval {x₁ x₂ x₃ c₂ c₁ c₀ : ℚ}
    (h : ∀ t : ℚ, (t - x₁) * (t - x₂) * (t - x₃) = t ^ 3 + c₂ * t ^ 2 + c₁ * t + c₀) :
    x₁ * x₂ * x₃ = -c₀ ∧ x₁ * x₂ + x₁ * x₃ + x₂ * x₃ = c₁ :=
  ⟨by linear_combination -h 0, by linear_combination (h 1 - h (-1)) / 2⟩

/-- Square-class transport: a `ℚˣ`-indexed class agrees with the `ℚ`-valued one. -/
theorem qcl_eq_cls_of_sqEq {d : ℚˣ} {k : ℚ} (hk : k ≠ 0) (h : SqEq ℚ (d : ℚ) k) :
    qcl d = cls k := by
  rw [cls_of_ne hk]
  exact qcl_eq_of_sqEq (b := Units.mk0 k hk) h

/-! ## Rebased from Run A onto Run B's `dval` -/

/-- `cls 1 = 1`.  Run A had this; Run B did not. -/
theorem cls_one : cls (1 : ℚ) = 1 := by
  rw [cls_of_ne (one_ne_zero)]
  simp [qcl]

/-- The forward inclusion, coordinate level: the descent value of any affine point lies in
the certified `Run013.KummerImage`.  Run A's `dnum_mem_kummerImage`, rebased. -/
theorem dval_mem_kummerImage {a b x y : ℚ} (h : (Wab a b).toAffine.Nonsingular x y) :
    dval b x ∈ KummerImage ℚ a b := by
  by_cases hx : x = 0
  · rw [hx, dval_zero]; exact Or.inr (Or.inl rfl)
  · rw [dval_of_ne b hx]
    exact Or.inr (Or.inr ⟨hx, y, (Wab_equation_iff a b x y).mp h.left⟩)

/-- Point level: every point of the actual group has a nonzero representative in the
certified `KummerImage` whose class is its `delta` value. -/
theorem exists_kummer_rep {a b : ℚ} (hb : b ≠ 0) (P : (Wab a b).toAffine.Point) :
    ∃ k : ℚ, k ≠ 0 ∧ k ∈ KummerImage ℚ a b ∧ delta a b P = cls k := by
  cases P with
  | zero => exact ⟨1, one_ne_zero, Or.inl rfl, by
      show delta a b 0 = cls 1
      rw [delta_zero, cls_one]⟩
  | @some x y h =>
      exact ⟨dval b x, dval_ne_zero hb x, dval_mem_kummerImage h, delta_some_eq_cls_dval h⟩

end Descent
