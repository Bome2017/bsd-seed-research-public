/-
Run013 — `Selmer.lean`

The genuine isogeny-Selmer groups, as subsets of `ℚ*/ℚ*^2`.

For a curve `A_{a,b} : y^2 = x^3 + a x^2 + b x` over `ℚ` the descent map attached to the
two-isogeny with kernel `⟨(0,0)⟩` *onto* `A_{a,b}` has image, over a field `K`, equal to
`KummerImage K a b` (see `Basic.lean`).  The associated Selmer group is the set of
square classes lying in that local image at **every** place of `ℚ`:

    Sel = { d ∈ ℚ*/ℚ*^2 | d ∈ image of the local descent map at ℝ and at every ℚ_p }.

This file sets up `ℚ*/ℚ*^2` as an honest quotient group, defines the Selmer set, proves
that the defining condition only depends on the square class, and records the
translation into the language of the quartic coverings.

No finite test is built into the definition.
-/
import RequestProject.Run013.Basic

namespace Run013

/-! ## The group `ℚ*/ℚ*^2` -/

/-- The subgroup of squares in `ℚˣ`. -/
def sqSubgroup : Subgroup ℚˣ := MonoidHom.range (powMonoidHom 2 : ℚˣ →* ℚˣ)

/-- The square-class group `ℚ*/ℚ*^2`. -/
abbrev Qsq := ℚˣ ⧸ sqSubgroup

/-- The class of a rational unit in `ℚ*/ℚ*^2`. -/
def qcl (a : ℚˣ) : Qsq := QuotientGroup.mk a

lemma mem_sqSubgroup {x : ℚˣ} : x ∈ sqSubgroup ↔ ∃ t : ℚˣ, x = t ^ 2 := by
  simp [sqSubgroup, powMonoidHom, eq_comm]

lemma qcl_eq_qcl {a b : ℚˣ} : qcl a = qcl b ↔ ∃ t : ℚˣ, b = a * t ^ 2 := by
  rw [qcl, qcl, QuotientGroup.eq, mem_sqSubgroup]
  constructor
  · rintro ⟨t, ht⟩
    exact ⟨t, by rw [← ht, mul_inv_cancel_left]⟩
  · rintro ⟨t, ht⟩
    exact ⟨t, by rw [ht, inv_mul_cancel_left]⟩

lemma qcl_surjective : Function.Surjective qcl := Quot.mk_surjective

/-- The square class of a rational number.  On nonzero arguments this is the honest class in
`ℚ*/ℚ*^2`; the value at `0` is irrelevant and never used. -/
noncomputable def cls (d : ℚ) : Qsq := if h : d = 0 then 1 else qcl (Units.mk0 d h)

lemma cls_of_ne {d : ℚ} (h : d ≠ 0) : cls d = qcl (Units.mk0 d h) := dif_neg h

/-- Square-equivalence of rationals is exactly equality of classes in `ℚ*/ℚ*^2`. -/
lemma qcl_eq_of_sqEq {a b : ℚˣ} (h : SqEq ℚ (a : ℚ) (b : ℚ)) : qcl a = qcl b := by
  obtain ⟨t, ht, hab⟩ := h
  refine qcl_eq_qcl.mpr ⟨(Units.mk0 t ht)⁻¹, ?_⟩
  have hb' : (b : ℚ) = (a : ℚ) * (t⁻¹) ^ 2 := by field_simp; linear_combination -hab
  apply Units.ext
  push_cast [Units.val_inv_eq_inv_val]
  exact hb'

/-! ## Base change of coverings -/

/-- A rational point on a covering gives a point over any field of characteristic zero. -/
theorem cov_base_change {K : Type*} [Field K] [CharZero K] {a b d : ℚ} (h : Cov ℚ a b d) :
    Cov K (a : K) (b : K) (d : K) := by
  obtain ⟨u, v, n, huv, hn⟩ := h
  refine ⟨(u : K), (v : K), (n : K), ?_, ?_⟩
  · rintro ⟨hu, hv⟩
    exact huv ⟨by exact_mod_cast hu, by exact_mod_cast hv⟩
  · have := congrArg (fun x : ℚ => (x : K)) hn
    push_cast at this
    exact this

/-! ## Local conditions -/

/-- The local condition defining the Selmer group: the class of `d` lies in the image of the
local descent map at the archimedean place and at every finite place. -/
def LocalKummerAll (a b d : ℚ) : Prop :=
  InKummer ℝ (a : ℝ) (b : ℝ) (d : ℝ) ∧
    ∀ (p : ℕ) [Fact p.Prime], InKummer ℚ_[p] (a : ℚ_[p]) (b : ℚ_[p]) (d : ℚ_[p])

/-- Translation of the local conditions into solubility of the quartic coverings. -/
theorem localKummerAll_iff_cov {a b d : ℚ} (hb : b ≠ 0) (hd : d ≠ 0) :
    LocalKummerAll a b d ↔
      (Cov ℝ (a : ℝ) (b : ℝ) (d : ℝ) ∧
        ∀ (p : ℕ) [Fact p.Prime], Cov ℚ_[p] (a : ℚ_[p]) (b : ℚ_[p]) (d : ℚ_[p])) := by
  have hbR : (b : ℝ) ≠ 0 := Rat.cast_ne_zero.mpr hb
  have hdR : (d : ℝ) ≠ 0 := Rat.cast_ne_zero.mpr hd
  constructor
  · rintro ⟨hinf, hp⟩
    refine ⟨(cov_iff_inKummer hbR hdR).mpr hinf, fun p _ => ?_⟩
    exact (cov_iff_inKummer (Rat.cast_ne_zero.mpr hb) (Rat.cast_ne_zero.mpr hd)).mpr (hp p)
  · rintro ⟨hinf, hp⟩
    refine ⟨(cov_iff_inKummer hbR hdR).mp hinf, fun p _ => ?_⟩
    exact (cov_iff_inKummer (Rat.cast_ne_zero.mpr hb) (Rat.cast_ne_zero.mpr hd)).mp (hp p)

/-- The local conditions only depend on the square class of `d`. -/
theorem localKummerAll_sqEq {a b d c : ℚ} (hb : b ≠ 0) (hc : c ≠ 0) (h : SqEq ℚ d c)
    (hL : LocalKummerAll a b c) : LocalKummerAll a b d := by
  have hd : d ≠ 0 := h.ne_zero hc
  rw [localKummerAll_iff_cov hb hc] at hL
  rw [localKummerAll_iff_cov hb hd]
  obtain ⟨t, ht, hdc⟩ := h
  refine ⟨?_, fun p _ => ?_⟩
  · refine cov_sqEq (Rat.cast_ne_zero.mpr hc) ⟨(t : ℝ), Rat.cast_ne_zero.mpr ht, ?_⟩ hL.1
    exact_mod_cast congrArg (fun x : ℚ => (x : ℝ)) hdc
  · refine cov_sqEq (Rat.cast_ne_zero.mpr hc) ⟨(t : ℚ_[p]), Rat.cast_ne_zero.mpr ht, ?_⟩ (hL.2 p)
    exact_mod_cast congrArg (fun x : ℚ => (x : ℚ_[p])) hdc

/-! ## The Selmer group -/

/-- The Selmer group of the two-isogeny with kernel `⟨(0,0)⟩` onto `A_{a,b} : y^2 = x^3+ax^2+bx`,
viewed inside `ℚ*/ℚ*^2`. -/
def SelmerSet (a b : ℚ) : Set Qsq :=
  {c | ∃ d : ℚˣ, qcl d = c ∧ LocalKummerAll a b (d : ℚ)}

/-- Membership in the Selmer group can be tested on any representative. -/
theorem mem_selmerSet_iff {a b : ℚ} (hb : b ≠ 0) (d : ℚˣ) :
    qcl d ∈ SelmerSet a b ↔ LocalKummerAll a b (d : ℚ) := by
  constructor
  · rintro ⟨e, he, hL⟩
    obtain ⟨t, ht⟩ := qcl_eq_qcl.mp he
    refine localKummerAll_sqEq hb e.ne_zero ⟨(t : ℚ), t.ne_zero, ?_⟩ hL
    exact_mod_cast congrArg (fun x : ℚˣ => (x : ℚ)) ht
  · intro hL; exact ⟨d, rfl, hL⟩

/-- Everywhere-locally-soluble classes given by an honest rational point are Selmer. -/
theorem mem_selmerSet_of_global {a b : ℚ} (hb : b ≠ 0) (d : ℚˣ) (h : Cov ℚ a b (d : ℚ)) :
    qcl d ∈ SelmerSet a b := by
  refine (mem_selmerSet_iff hb d).mpr ?_
  rw [localKummerAll_iff_cov hb d.ne_zero]
  exact ⟨cov_base_change h, fun p _ => cov_base_change h⟩

/-- Membership of a square class, tested on a nonzero rational representative. -/
theorem mem_selmerSet_cls_iff {a b : ℚ} (hb : b ≠ 0) {d : ℚ} (hd : d ≠ 0) :
    cls d ∈ SelmerSet a b ↔ LocalKummerAll a b d := by
  rw [cls_of_ne hd, mem_selmerSet_iff hb]
  rfl

/-- A rational point on the covering puts the class of `d` into the Selmer group. -/
theorem mem_selmerSet_cls_of_global {a b : ℚ} (hb : b ≠ 0) {d : ℚ} (hd : d ≠ 0)
    (h : Cov ℚ a b d) : cls d ∈ SelmerSet a b := by
  rw [cls_of_ne hd]
  exact mem_selmerSet_of_global hb _ h

end Run013
