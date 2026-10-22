import RequestProject.P04a.Cokernels
import RequestProject.SDyadic.Saturation

namespace P04b

open Run013 SDyadic Descent P01 P03a P03b P03c P03e P04a WeierstrassCurve

/-! # P04b — reconnecting the cokernels to the saturation theorem

This is the first file in the development that imports **both** certified branches at once:
the H₄₁ saturation theorem (`SDyadic/Saturation.lean`) and the point-level isogeny package
(`P03a`–`P04a`).  Until now they were separate Lean projects that had never been compiled
together.

P04a produced two actual quotient groups and identified them with the ranges of the two
descent maps.  Saturation, proved much earlier and entirely in the language of square classes,
determined exactly which square classes are soluble.  This file says they are talking about
the same subgroups of `ℚ*/ℚ*²`.

## The three facts

    range δ_{E'}  =  GphiExp  =  ⟨[D],[q]⟩
    range δ_E     =  {1}
    δ_{E'}(ker φ̂) =  KExp     =  ⟨[D]⟩

The third is where `KExp` belongs.  **`KExp` is not `range δ_E`.**  It is the image of the
φ̂-kernel under the descent map on `E'_q`, and the saturation object never claims otherwise:
`KExp` occurs there only inside `((KExp ε m).subgroupOf (GphiExp ε m q)).index = 2`.

## Orientation, read off the frozen sources rather than the notation

* `SDyadic.GlobalSet a b = {c | ∃ d : ℚˣ, qcl d = c ∧ Cov ℚ a b d}` is **literally** the
  right-hand side of `P04a.isogeny_cokernels`'s sixth conjunct, so `range δ` and `GlobalSet`
  are the same set by construction, on both sides;
* on the φ side `SDyadic.phi_exhaustion` allows exactly the four classes `1, D, q, Dq`, and
  `SDyadic.cov_phi_one/D/q/Dq` exhibit rational points for each — that is `GphiExp`;
* on the dual side `SDyadic.dual_exhaustion` concludes `SqEq ℚ e 1` for every squarefree
  locally-soluble `e`, and `SDyadic.cov_dual_one` is the only dual witness.  The dual side
  therefore collapses to the trivial class.  This is why conjunct 2 reads `{1}` and not
  `⟨[D]⟩`.

## What must NOT appear

Do not form `GphiExp / KExp`, do not mention `E(ℚ)/2E(ℚ)`, and do not state any index,
order or cardinality — `((KExp ε m).subgroupOf (GphiExp ε m q)).index = 2` is already
certified and belongs to the **next** stage, not this one.  No `Sel₂`, Ш, rank or BSD.
Do not redo any local `p`-adic analysis: every local statement this file needs is already
certified inside `SDyadic/`.
-/

variable {ε : ℤ} {m q : ℕ}

/-! ## The elementary bridge

`phiB = D q²`, so its square class is the class of `D`.  This is the one small arithmetic fact
the reconnection needs that no earlier stage stated, and it is supplied here, proved, rather
than left to the target. -/

theorem cls_phiB_eq_cls_DD [Fact (Nat.Prime q)] (hP : Params ε m q) :
    cls (phiB ε m q) = cls ((DD ε m : ℤ) : ℚ) := by
  have hq : ((q : ℚ)) ≠ 0 := q_ne_zero' hP
  have hD : ((DD ε m : ℤ) : ℚ) ≠ 0 := Int.cast_ne_zero.mpr (DD_ne_zero ε m)
  have hfac : phiB ε m q = ((DD ε m : ℤ) : ℚ) * ((q : ℚ)) ^ 2 := by
    simp only [phiB]
    push_cast
    ring
  rw [hfac, cls_mul hD (pow_ne_zero 2 hq), cls_sq hq, mul_one]

/-! ## Auxiliary lemmas for the reconnection

All proved.  Nothing below introduces a quotient, an index, a cardinality, or a new local
statement: the square-class transport is `Descent.qcl_eq_cls_of_sqEq`, the two "which classes"
lemmas apply the **certified** exhaustion theorems of `SDyadic/` to the **certified** squarefree
representative, and the range of `δ_E` is read off `Descent.delta_descent` exactly as `P04a`
reads off the range of `δ_{E'}`. -/

/-- Square-class transport between two nonzero rationals in the same square class. -/
theorem cls_eq_cls_of_sqEq {d k : ℚ} (hd : d ≠ 0) (hk : k ≠ 0) (h : SqEq ℚ d k) :
    cls d = cls k := by
  rw [cls_of_ne hd]
  exact qcl_eq_cls_of_sqEq hk h

/-- The two casts of `q` into `ℚ` agree. -/
theorem qZ_eq_qN (q : ℕ) : ((q : ℤ) : ℚ) = ((q : ℕ) : ℚ) := by push_cast; ring

/-- `[D] ∈ ⟨[D],[q]⟩`. -/
theorem cls_DD_mem_GphiExp (ε : ℤ) (m q : ℕ) : cls ((DD ε m : ℤ) : ℚ) ∈ GphiExp ε m q :=
  Subgroup.subset_closure (Set.mem_insert _ _)

/-- `[q] ∈ ⟨[D],[q]⟩`. -/
theorem cls_q_mem_GphiExp (ε : ℤ) (m q : ℕ) : cls ((q : ℕ) : ℚ) ∈ GphiExp ε m q :=
  Subgroup.subset_closure (Set.mem_insert_of_mem _ rfl)

/-- **φ side.**  A square class carrying a rational point on the φ covering lies in
`⟨[D],[q]⟩`.  Rational solubility base-changes to everywhere-local solubility
(`Run013.cov_base_change`, `Run013.localKummerAll_iff_cov`); the certified squarefree
representative `SDyadic.exists_squarefree_rep` and the certified `SDyadic.phi_exhaustion` then
allow only the four classes `1, D, q, Dq`.  No local analysis is redone here. -/
theorem cls_mem_GphiExp_of_cov [Fact (Nat.Prime q)] (hP : Params ε m q) (hH : H41 ε m)
    {d : ℚ} (hd : d ≠ 0) (hcov : Cov ℚ (phiA ε m q) (phiB ε m q) d) :
    cls d ∈ GphiExp ε m q := by
  have hH' : (DD ε m < 0 ∧ sCount ε m = 1) ∨
      (0 < DD ε m ∧ sCount ε m = 2 ∧ ∀ ℓ ∈ ellSet ε m, ℓ % 4 = 3) := hH
  have hb : phiB ε m q ≠ 0 := phiB_ne_zero hP
  have hD : ((DD ε m : ℤ) : ℚ) ≠ 0 := Int.cast_ne_zero.mpr (DD_ne_zero ε m)
  have hqQ : ((q : ℤ) : ℚ) ≠ 0 := by rw [qZ_eq_qN]; exact q_ne_zero' hP
  have hL : LocalKummerAll (phiA ε m q) (phiB ε m q) d := by
    rw [localKummerAll_iff_cov hb hd]
    exact ⟨cov_base_change hcov, fun p _ => cov_base_change hcov⟩
  obtain ⟨e, he, hsf, hsq⟩ := exists_squarefree_rep d hd
  have heQ : ((e : ℤ) : ℚ) ≠ 0 := Int.cast_ne_zero.mpr he
  have hLe : LocalKummerAll (phiA ε m q) (phiB ε m q) ((e : ℤ) : ℚ) :=
    localKummerAll_sqEq hb hd (hsq.symm heQ) hL
  have hDq : ((DD ε m * (q : ℤ) : ℤ) : ℚ) = ((DD ε m : ℤ) : ℚ) * ((q : ℤ) : ℚ) := by
    push_cast; ring
  rw [cls_eq_cls_of_sqEq hd heQ hsq]
  rcases phi_exhaustion hP hH' he hsf hLe with h | h | h | h
  · rw [cls_eq_cls_of_sqEq heQ one_ne_zero h, cls_one]
    exact one_mem _
  · rw [cls_eq_cls_of_sqEq heQ hD h]
    exact cls_DD_mem_GphiExp ε m q
  · rw [cls_eq_cls_of_sqEq heQ hqQ h, qZ_eq_qN]
    exact cls_q_mem_GphiExp ε m q
  · rw [cls_eq_cls_of_sqEq heQ (by rw [hDq]; exact mul_ne_zero hD hqQ) h, hDq,
      cls_mul hD hqQ, qZ_eq_qN]
    exact mul_mem (cls_DD_mem_GphiExp ε m q) (cls_q_mem_GphiExp ε m q)

/-- **Dual side.**  A square class carrying a rational point on the dual covering is trivial.
Same route, with the certified `SDyadic.dual_exhaustion`, which allows only the class `1`. -/
theorem cls_eq_one_of_cov_dual [Fact (Nat.Prime q)] (hP : Params ε m q) (hH : H41 ε m)
    {d : ℚ} (hd : d ≠ 0) (hcov : Cov ℚ (dualA ε m q) (dualB ε m q) d) : cls d = 1 := by
  have hH' : (DD ε m < 0 ∧ sCount ε m = 1) ∨
      (0 < DD ε m ∧ sCount ε m = 2 ∧ ∀ ℓ ∈ ellSet ε m, ℓ % 4 = 3) := hH
  have hb : dualB ε m q ≠ 0 := dualB_ne_zero hP
  have hL : LocalKummerAll (dualA ε m q) (dualB ε m q) d := by
    rw [localKummerAll_iff_cov hb hd]
    exact ⟨cov_base_change hcov, fun p _ => cov_base_change hcov⟩
  obtain ⟨e, he, hsf, hsq⟩ := exists_squarefree_rep d hd
  have heQ : ((e : ℤ) : ℚ) ≠ 0 := Int.cast_ne_zero.mpr he
  have hLe : LocalKummerAll (dualA ε m q) (dualB ε m q) ((e : ℤ) : ℚ) :=
    localKummerAll_sqEq hb hd (hsq.symm heQ) hL
  rw [cls_eq_cls_of_sqEq hd heQ hsq,
    cls_eq_cls_of_sqEq heQ one_ne_zero (dual_exhaustion hP hH' he hsf hLe), cls_one]

/-- The coordinate description of `range δ_E`, the dual-side analogue of
`P04a.mem_range_deltaHomE'`.  Second component of `Descent.delta_descent`. -/
theorem mem_range_deltaHomE [Fact (Nat.Prime q)] (hP : Params ε m q) (c : Additive Qsq) :
    c ∈ (deltaHomE hP).range
      ↔ ∃ d : ℚˣ, qcl d = Additive.toMul c ∧ Cov ℚ (dualA ε m q) (dualB ε m q) (d : ℚ) := by
  rw [AddMonoidHom.mem_range]
  refine Iff.trans ?_
    ((delta_descent (dualA ε m q) (dualB ε m q) (dualB_ne_zero hP)
      (dualA_disc_ne_zero hP)).2.1 (Additive.toMul c))
  exact ⟨fun ⟨P, h⟩ => ⟨P, congrArg Additive.toMul h⟩,
    fun ⟨P, h⟩ => ⟨P, congrArg Additive.ofMul h⟩⟩

/-- `δ_{E'}(T') = [D]`: the descent class of the exceptional point, via `cls_phiB_eq_cls_DD`. -/
theorem deltaHomE'_T'pt [Fact (Nat.Prime q)] (hP : Params ε m q) :
    deltaHomE' hP (T'pt hP) = Additive.ofMul (cls ((DD ε m : ℤ) : ℚ)) := by
  rw [deltaHomE'_apply, delta_T'pt, cls_phiB_eq_cls_DD hP]

/-- `[D]` is in the range of `δ_{E'}`: the witness is `SDyadic.cov_phi_D`. -/
theorem ofMul_cls_DD_mem_range [Fact (Nat.Prime q)] (hP : Params ε m q) :
    Additive.ofMul (cls ((DD ε m : ℤ) : ℚ)) ∈ (deltaHomE' hP).range := by
  have hD : ((DD ε m : ℤ) : ℚ) ≠ 0 := Int.cast_ne_zero.mpr (DD_ne_zero ε m)
  exact (mem_range_deltaHomE' hP _).mpr
    ⟨Units.mk0 _ hD, (cls_of_ne hD).symm, cov_phi_D ε m q⟩

/-- `[q]` is in the range of `δ_{E'}`: the witness is `SDyadic.cov_phi_q`. -/
theorem ofMul_cls_q_mem_range [Fact (Nat.Prime q)] (hP : Params ε m q) :
    Additive.ofMul (cls ((q : ℕ) : ℚ)) ∈ (deltaHomE' hP).range := by
  have hq : ((q : ℕ) : ℚ) ≠ 0 := q_ne_zero' hP
  have hcov : Cov ℚ (phiA ε m q) (phiB ε m q) ((q : ℕ) : ℚ) := by
    have h := cov_phi_q ε m q
    rwa [qZ_eq_qN] at h
  exact (mem_range_deltaHomE' hP _).mpr ⟨Units.mk0 _ hq, (cls_of_ne hq).symm, hcov⟩

/-- Every class in `⟨[D],[q]⟩` is in the range of `δ_{E'}`.  The range is a subgroup and both
generators are hit, so this is closure induction. -/
theorem ofMul_mem_range_of_mem_GphiExp [Fact (Nat.Prime q)] (hP : Params ε m q) {c : Qsq}
    (hc : c ∈ GphiExp ε m q) : Additive.ofMul c ∈ (deltaHomE' hP).range := by
  rw [GphiExp] at hc
  induction hc using Subgroup.closure_induction with
  | mem x hx =>
      rcases hx with rfl | rfl
      · exact ofMul_cls_DD_mem_range hP
      · exact ofMul_cls_q_mem_range hP
  | one =>
      rw [_root_.ofMul_one]
      exact AddSubgroup.zero_mem _
  | mul x y _ _ hx hy => exact (deltaHomE' hP).range.add_mem hx hy
  | inv x _ hx => exact (deltaHomE' hP).range.neg_mem hx

/-! ## The four conjuncts -/

/-- **Conjunct 1.**  `range δ_{E'} = GphiExp = ⟨[D],[q]⟩`. -/
theorem range_deltaHomE'_iff_GphiExp [Fact (Nat.Prime q)] (hP : Params ε m q) (hH : H41 ε m)
    (c : Qsq) : Additive.ofMul c ∈ (deltaHomE' hP).range ↔ c ∈ GphiExp ε m q := by
  constructor
  · intro hc
    obtain ⟨d, hd, hcov⟩ := (mem_range_deltaHomE' hP (Additive.ofMul c)).mp hc
    have hd' : qcl d = c := hd
    rw [← hd', qcl_eq_cls_of_sqEq d.ne_zero (SqEq.rfl' _)]
    exact cls_mem_GphiExp_of_cov hP hH d.ne_zero hcov
  · exact fun hc => ofMul_mem_range_of_mem_GphiExp hP hc

/-- **Conjunct 2.**  `range δ_E = {1}`, elementwise. -/
theorem range_deltaHomE_iff_one [Fact (Nat.Prime q)] (hP : Params ε m q) (hH : H41 ε m)
    (c : Qsq) : Additive.ofMul c ∈ (deltaHomE hP).range ↔ c = 1 := by
  constructor
  · intro hc
    obtain ⟨d, hd, hcov⟩ := (mem_range_deltaHomE hP (Additive.ofMul c)).mp hc
    have hd' : qcl d = c := hd
    rw [← hd', qcl_eq_cls_of_sqEq d.ne_zero (SqEq.rfl' _)]
    exact cls_eq_one_of_cov_dual hP hH d.ne_zero hcov
  · rintro rfl
    rw [_root_.ofMul_one]
    exact AddSubgroup.zero_mem _

/-- **Conjunct 3.**  The same as an `AddSubgroup` identity. -/
theorem range_deltaHomE_eq_bot [Fact (Nat.Prime q)] (hP : Params ε m q) (hH : H41 ε m) :
    (deltaHomE hP).range = ⊥ := by
  refine le_antisymm (fun x hx => ?_) bot_le
  rw [AddSubgroup.mem_bot]
  exact (_root_.ofMul_eq_zero (A := Qsq) (x := Additive.toMul x)).mpr
    ((range_deltaHomE_iff_one hP hH (Additive.toMul x)).mp hx)

/-- **Conjunct 4.**  `δ_{E'}(ker φ̂) = KExp = ⟨[D]⟩`.  `P03c.isogeny_kernels` gives
`ker φ̂ = {O, T'}`, `δ_{E'}(O) = 1` and `δ_{E'}(T') = [D]`, and `⟨[D]⟩ = {1, [D]}` because every
square class is an involution. -/
theorem mem_map_ker_dualPhiHom_iff_KExp [Fact (Nat.Prime q)] (hP : Params ε m q) (c : Qsq) :
    Additive.ofMul c ∈ AddSubgroup.map (deltaHomE' hP) (dualPhiHom hP).ker
      ↔ c ∈ KExp ε m := by
  constructor
  · intro hc
    obtain ⟨P', hker, hval⟩ := AddSubgroup.mem_map.mp hc
    rcases ((isogeny_kernels ε m q hP).2 P').mp hker with rfl | rfl
    · rw [map_zero] at hval
      rw [_root_.ofMul_eq_zero.mp hval.symm]
      exact one_mem _
    · rw [deltaHomE'_T'pt hP] at hval
      rw [(Additive.ofMul.injective hval).symm, KExp]
      exact Subgroup.subset_closure rfl
  · intro hc
    rw [KExp] at hc
    rcases mem_closure_singleton_of_sq_eq_one (qsq_sq_eq_one _) hc with rfl | rfl
    · exact AddSubgroup.mem_map.mpr ⟨0, AddSubgroup.zero_mem _, by simp⟩
    · exact AddSubgroup.mem_map.mpr
        ⟨T'pt hP, ((isogeny_kernels ε m q hP).2 _).mpr (Or.inr rfl), deltaHomE'_T'pt hP⟩

/-! ## The P04b target -/

/--
**Target.**  The two descent ranges, and the image of the φ̂-kernel.

1. `range δ_{E'} = GphiExp ε m q = ⟨[D],[q]⟩`.
2. `range δ_E = {1}`, elementwise.
3. the same as an `AddSubgroup` identity, `range δ_E = ⊥`.
4. `δ_{E'}(ker φ̂) = KExp ε m = ⟨[D]⟩`.

Conjuncts 1, 2 and 3 are the reconnection: `range δ` is `GlobalSet` by `P04a`'s sixth
conjunct and `Descent.delta_descent`, `GlobalSet = SelmerSet` is `SDyadic.sdyadic_saturation`,
and the two exhaustion theorems say which classes those are.

Conjunct 4 is not about saturation at all.  `P03c.isogeny_kernels` gives `ker φ̂ = {O, T'}`,
`Descent.delta` gives `δ_{E'}(O) = 1` and `δ_{E'}(T') = [phiB]`, and `cls_phiB_eq_cls_DD`
above turns `[phiB]` into `[D]`.  Every element of `Qsq` is its own inverse
(`Descent.Qsq_mul_self`), so `{1, [D]}` is already the subgroup `⟨[D]⟩`.

Stated elementwise on `Qsq` throughout, so that no `Additive`/`Multiplicative` coercion has to
be trusted: `Additive.ofMul` is the identity function. -/
theorem saturation_reconnect (ε : ℤ) (m q : ℕ) [Fact (Nat.Prime q)]
    (hP : Params ε m q) (hH : H41 ε m) :
    (∀ c : Qsq, Additive.ofMul c ∈ (deltaHomE' hP).range ↔ c ∈ GphiExp ε m q)
  ∧ (∀ c : Qsq, Additive.ofMul c ∈ (deltaHomE hP).range ↔ c = 1)
  ∧ (deltaHomE hP).range = ⊥
  ∧ (∀ c : Qsq,
        Additive.ofMul c ∈ AddSubgroup.map (deltaHomE' hP) (dualPhiHom hP).ker
          ↔ c ∈ KExp ε m) := by
  exact ⟨range_deltaHomE'_iff_GphiExp hP hH,
    range_deltaHomE_iff_one hP hH,
    range_deltaHomE_eq_bot hP hH,
    mem_map_ker_dualPhiHom_iff_KExp hP⟩

end P04b
