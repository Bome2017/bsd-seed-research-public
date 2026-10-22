import RequestProject.P03e.Bridge

namespace P04a

open Run013 SDyadic Descent P01 P03a P03b P03c P03e WeierstrassCurve

/-! # P04a — the actual isogeny cokernels

Every stage so far produced maps and identities. This file produces, for the first time in
this development, an **actual quotient group** and identifies it.

P03e certified

    δ_E(P)     = 1  ↔  ∃ P', φ̂(P') = P
    δ_{E'}(P') = 1  ↔  ∃ P,  φ(P)  = P'

which is exactly the statement that `ker δ` and the image of the opposite isogeny are the same
set of points. Once the δ maps are bundled as honest homomorphisms — legitimate because
`Descent.delta_descent` certified multiplicativity — that set equality becomes an equality of
`AddSubgroup`s, and the quotients

    E'_q(ℚ) ⧸ φ(E_q(ℚ))      E_q(ℚ) ⧸ φ̂(E'_q(ℚ))

can be formed and identified with the ranges of the two descent maps.

## What is already proved and may be used freely

| fact | where | status |
|---|---|---|
| δ is multiplicative, and its image is the covering-soluble classes | `Descent.delta_descent` | certified, two runs |
| `φ`, `φ̂` bundled as `AddMonoidHom`s | `P03c.phiHom`, `P03c.dualPhiHom` | certified, two runs |
| `ker δ_E = im φ̂`, `ker δ_{E'} = im φ` | `P03e.descent_kernel_eq_isogeny_image` | certified, two runs |
| `cls (phiB ε m q) ≠ 1` | `P03e.cls_phiB_ne_one` | certified |
| the side conditions δ needs | `P01.dualB_ne_zero`, `P01.phiB_ne_zero`, `P01.dualA_disc_ne_zero`, `P01.phiA_disc_ne_zero` | certified, two runs |

## What must NOT appear

`Sel₂`, Ш, rank, BSD, `E(ℚ)/2E(ℚ)`, `Nat.card`, `Fintype`, `Finite`, `Nat.card`, any
finiteness or cardinality claim, any local condition, `SelmerSet`, or any statement about
2-descent beyond the single isogeny. This file forms two quotients and says what they are
isomorphic to. It says nothing about how big they are, and nothing about whether `range δ` is
contained in a Selmer group — that is a later stage.

## Honest note on the size of this task

The mathematics was done in P03e. What remains is assembly: bundling, one subgroup extension,
and Noether's first isomorphism theorem. The target below is expected to be short. It is
stated anyway, and stated in full, because the objects it names — the two quotient groups, the
induced isomorphisms, the range characterisation — are what every later stage consumes, and
this development does not use an object until it has been built and certified.
-/

variable {ε : ℤ} {m q : ℕ}

/-! ## The descent maps, bundled

`Qsq = ℚˣ ⧸ sqSubgroup` is a multiplicative group, so its additive copy `Additive Qsq` is the
target type that lets `δ` be an `AddMonoidHom` out of the additive point group. No content is
added by this translation; `Additive.ofMul` is the identity function. -/

/-- `δ_E` bundled as an additive homomorphism. `map_add` is the certified first component of
`Descent.delta_descent`; the two side conditions are P01's. -/
noncomputable def deltaHomE [Fact (Nat.Prime q)] (hP : Params ε m q) :
    (Ecurve ε m q).toAffine.Point →+ Additive Qsq :=
  AddMonoidHom.mk' (fun P => Additive.ofMul (delta (dualA ε m q) (dualB ε m q) P))
    (fun P Q =>
      (delta_descent (dualA ε m q) (dualB ε m q)
        (dualB_ne_zero hP) (dualA_disc_ne_zero hP)).1 P Q)

/-- `δ_{E'}` bundled as an additive homomorphism. -/
noncomputable def deltaHomE' [Fact (Nat.Prime q)] (hP : Params ε m q) :
    (E'curve ε m q).toAffine.Point →+ Additive Qsq :=
  AddMonoidHom.mk' (fun P => Additive.ofMul (delta (phiA ε m q) (phiB ε m q) P))
    (fun P Q =>
      (delta_descent (phiA ε m q) (phiB ε m q)
        (phiB_ne_zero hP) (phiA_disc_ne_zero hP)).1 P Q)

@[simp] theorem deltaHomE_apply [Fact (Nat.Prime q)] (hP : Params ε m q)
    (P : (Ecurve ε m q).toAffine.Point) :
    deltaHomE hP P = Additive.ofMul (delta (dualA ε m q) (dualB ε m q) P) := rfl

@[simp] theorem deltaHomE'_apply [Fact (Nat.Prime q)] (hP : Params ε m q)
    (P : (E'curve ε m q).toAffine.Point) :
    deltaHomE' hP P = Additive.ofMul (delta (phiA ε m q) (phiB ε m q) P) := rfl

/-! ## Auxiliary lemmas

All proved.  Nothing below uses finiteness, cardinality, a local condition, a Selmer set, or
any exact sequence: the two kernel identifications are `P03e.descent_kernel_eq_isogeny_image`
repackaged as `AddSubgroup` equalities, the two quotient isomorphisms are the first
isomorphism theorem transported along those equalities, the nontriviality is the certified
non-square obstruction `P03e.cls_phiB_ne_one`, and the range description is the second
component of `Descent.delta_descent`. -/

/-- `ker δ_{E'} = range φ`, as `AddSubgroup`s.  This is the membership-form P03e bridge
(`ker δ_{E'} = im φ`) turned into an equality of subgroup objects. -/
theorem ker_deltaHomE'_eq_range_phiHom [Fact (Nat.Prime q)] (hP : Params ε m q) :
    (deltaHomE' hP).ker = (phiHom hP).range := by
  ext P'
  rw [AddMonoidHom.mem_ker, AddMonoidHom.mem_range, deltaHomE'_apply,
    _root_.ofMul_eq_zero]
  exact (descent_kernel_eq_isogeny_image ε m q hP).2 P'

/-- `ker δ_E = range φ̂`, as `AddSubgroup`s. -/
theorem ker_deltaHomE_eq_range_dualPhiHom [Fact (Nat.Prime q)] (hP : Params ε m q) :
    (deltaHomE hP).ker = (dualPhiHom hP).range := by
  ext P
  rw [AddMonoidHom.mem_ker, AddMonoidHom.mem_range, deltaHomE_apply,
    _root_.ofMul_eq_zero]
  exact (descent_kernel_eq_isogeny_image ε m q hP).1 P

/-- The cokernel of `φ`, identified with the range of `δ_{E'}` by the map `δ_{E'}` induces. -/
noncomputable def cokerPhiEquiv [Fact (Nat.Prime q)] (hP : Params ε m q) :
    ((E'curve ε m q).toAffine.Point ⧸ (phiHom hP).range) ≃+ (deltaHomE' hP).range :=
  (QuotientAddGroup.quotientAddEquivOfEq
      (ker_deltaHomE'_eq_range_phiHom hP).symm).trans
    (QuotientAddGroup.quotientKerEquivRange (deltaHomE' hP))

/-- The cokernel of `φ̂`, identified with the range of `δ_E` by the map `δ_E` induces. -/
noncomputable def cokerDualPhiEquiv [Fact (Nat.Prime q)] (hP : Params ε m q) :
    ((Ecurve ε m q).toAffine.Point ⧸ (dualPhiHom hP).range) ≃+ (deltaHomE hP).range :=
  (QuotientAddGroup.quotientAddEquivOfEq
      (ker_deltaHomE_eq_range_dualPhiHom hP).symm).trans
    (QuotientAddGroup.quotientKerEquivRange (deltaHomE hP))

/-- The equivalence `cokerPhiEquiv` really is induced by `δ_{E'}`. -/
theorem cokerPhiEquiv_mk [Fact (Nat.Prime q)] (hP : Params ε m q)
    (P' : (E'curve ε m q).toAffine.Point) :
    (cokerPhiEquiv hP (QuotientAddGroup.mk P') : Additive Qsq)
      = Additive.ofMul (delta (phiA ε m q) (phiB ε m q) P') := rfl

/-- The equivalence `cokerDualPhiEquiv` really is induced by `δ_E`. -/
theorem cokerDualPhiEquiv_mk [Fact (Nat.Prime q)] (hP : Params ε m q)
    (P : (Ecurve ε m q).toAffine.Point) :
    (cokerDualPhiEquiv hP (QuotientAddGroup.mk P) : Additive Qsq)
      = Additive.ofMul (delta (dualA ε m q) (dualB ε m q) P) := rfl

/-- `δ_{E'}(T') = [phiB]`: the descent class of the exceptional point `T' = (0,0)`. -/
theorem delta_T'pt [Fact (Nat.Prime q)] (hP : Params ε m q) :
    delta (phiA ε m q) (phiB ε m q) (T'pt hP) = cls (phiB ε m q) := by
  rw [T'pt, delta_some_of_eq]

/-- **The cokernel of `φ` is not trivial.**  The class of `T'` is nonzero, because its descent
class is `[phiB] = [D q²] = [D]`, which `P03e.cls_phiB_ne_one` certifies is not a square. -/
theorem T'pt_class_ne_zero [Fact (Nat.Prime q)] (hP : Params ε m q) :
    (QuotientAddGroup.mk (T'pt hP)
      : (E'curve ε m q).toAffine.Point ⧸ (phiHom hP).range) ≠ 0 := by
  intro h
  rw [QuotientAddGroup.eq_zero_iff, ← ker_deltaHomE'_eq_range_phiHom hP,
    AddMonoidHom.mem_ker, deltaHomE'_apply, _root_.ofMul_eq_zero, delta_T'pt] at h
  exact cls_phiB_ne_one hP h

/-- The coordinate description of `range δ_{E'}`: the square classes carrying a rational point
on the corresponding quartic covering.  This is the second component of
`Descent.delta_descent`, attached to the honest subgroup. -/
theorem mem_range_deltaHomE' [Fact (Nat.Prime q)] (hP : Params ε m q) (c : Additive Qsq) :
    c ∈ (deltaHomE' hP).range
      ↔ ∃ d : ℚˣ, qcl d = Additive.toMul c ∧ Cov ℚ (phiA ε m q) (phiB ε m q) (d : ℚ) := by
  rw [AddMonoidHom.mem_range]
  refine Iff.trans ?_
    ((delta_descent (phiA ε m q) (phiB ε m q) (phiB_ne_zero hP)
      (phiA_disc_ne_zero hP)).2.1 (Additive.toMul c))
  exact ⟨fun ⟨P', hP'⟩ => ⟨P', congrArg Additive.toMul hP'⟩,
    fun ⟨P', hP'⟩ => ⟨P', congrArg Additive.ofMul hP'⟩⟩

/-! ## The P04a target -/

/--
**Target.**  The actual isogeny cokernels.

Six conjuncts.

1. `ker δ_{E'} = range φ` as `AddSubgroup`s of `E'_q(ℚ)`.
2. `ker δ_E = range φ̂` as `AddSubgroup`s of `E_q(ℚ)`.

3. An additive group isomorphism

       E'_q(ℚ) ⧸ range φ   ≃+   range δ_{E'}

   **induced by `δ_{E'}` itself**. That is what the trailing `∀ P'` clause pins down, and
   without it the conjunct would assert only that two groups happen to be abstractly
   isomorphic, which is much weaker and not what is wanted.

4. The same on the other side, for `E_q(ℚ) ⧸ range φ̂  ≃+  range δ_E`.

5. **The cokernel is not trivial**: the class of `T' = (0,0)` on `E'_q` is a nonzero element
   of `E'_q(ℚ) ⧸ range φ`. This is the group-quotient form of the certified Legendre
   obstruction — `T'` is the point whose descent class is `[D q²] = [D]`, and `Params` says
   `D` is not a square mod `q`.

6. The range of `δ_{E'}` is exactly the set of square classes carrying a rational point on the
   corresponding quartic covering — the coordinate description, now attached to the honest
   subgroup rather than to a bare image set.

This is a statement about honest point quotients. There is no Selmer group here, no local
condition, no finiteness, and no claim about the size of either quotient. -/
theorem isogeny_cokernels (ε : ℤ) (m q : ℕ) [Fact (Nat.Prime q)] (hP : Params ε m q) :
    (deltaHomE' hP).ker = (phiHom hP).range
  ∧ (deltaHomE hP).ker = (dualPhiHom hP).range
  ∧ (∃ e : ((E'curve ε m q).toAffine.Point ⧸ (phiHom hP).range) ≃+ (deltaHomE' hP).range,
        ∀ P' : (E'curve ε m q).toAffine.Point,
          (e (QuotientAddGroup.mk P') : Additive Qsq)
            = Additive.ofMul (delta (phiA ε m q) (phiB ε m q) P'))
  ∧ (∃ e : ((Ecurve ε m q).toAffine.Point ⧸ (dualPhiHom hP).range) ≃+ (deltaHomE hP).range,
        ∀ P : (Ecurve ε m q).toAffine.Point,
          (e (QuotientAddGroup.mk P) : Additive Qsq)
            = Additive.ofMul (delta (dualA ε m q) (dualB ε m q) P))
  ∧ (QuotientAddGroup.mk (T'pt hP)
        : (E'curve ε m q).toAffine.Point ⧸ (phiHom hP).range) ≠ 0
  ∧ (∀ c : Additive Qsq,
        c ∈ (deltaHomE' hP).range
          ↔ ∃ d : ℚˣ, qcl d = Additive.toMul c ∧ Cov ℚ (phiA ε m q) (phiB ε m q) (d : ℚ)) := by
  exact ⟨ker_deltaHomE'_eq_range_phiHom hP,
    ker_deltaHomE_eq_range_dualPhiHom hP,
    ⟨cokerPhiEquiv hP, cokerPhiEquiv_mk hP⟩,
    ⟨cokerDualPhiEquiv hP, cokerDualPhiEquiv_mk hP⟩,
    T'pt_class_ne_zero hP,
    mem_range_deltaHomE' hP⟩

end P04a
