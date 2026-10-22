import RequestProject.P04b.Reconnect

namespace P04c

open Run013 SDyadic Descent P01 P03a P03b P03c P03d P03e P04a P04b WeierstrassCurve

/-! # P04c — `E_q(ℚ)/2E_q(ℚ)`

This is the last stage of the H¹-free bridge.  Everything it needs is certified, and all of it
now lives in one Lean project:

| | |
|---|---|
| `φ̂ ∘ φ = P + P` | `P03d.isogeny_composites_eq_double` |
| `ker φ̂ = {O, T'}` | `P03c.isogeny_kernels` |
| `ker δ_E = im φ̂`, `ker δ_{E'} = im φ` | `P03e.descent_kernel_eq_isogeny_image` |
| `E'_q(ℚ) ⧸ φ(E_q(ℚ)) ≃+ range δ_{E'}`, induced by `δ_{E'}` | `P04a.isogeny_cokernels` |
| `range δ_{E'} = GphiExp`, `range δ_E = ⊥`, `δ_{E'}(ker φ̂) = KExp` | `P04b.saturation_reconnect` |
| `((KExp ε m).subgroupOf (GphiExp ε m q)).index = 2` | `SDyadic.sdyadic_saturation` |

Two consequences are worth stating before the target, because they are what make the classical
argument collapse here rather than merely apply:

* `range δ_E = ⊥` says **every** rational point of `E_q` has trivial descent class, so by P03e
  every rational point of `E_q` is in `im φ̂` — the dual cokernel is the trivial group;
* `δ_{E'}(ker φ̂) = KExp` places `KExp` where it belongs. It is **not** `range δ_E`.

## Boundary

This file forms quotients and, for the first time in the development, states a **cardinality**:
`Nat.card (E_q(ℚ) ⧸ 2E_q(ℚ)) = 2`.  That is deliberate and is confined to `E_q(ℚ)/2E_q(ℚ)`.

Still absent, and not to be added: `Sel₂`, Ш, rank, `L(E,s)`, any statement about a
cohomological Selmer group, and any claim about the rank of `E_q(ℚ)` or about `E_q(ℚ)` itself
beyond this quotient.
-/

variable {ε : ℤ} {m q : ℕ}

/-! ## Doubling, and the subgroup `2E_q(ℚ)`

Supplied proved.  `P03d` deliberately states its composite identity with `P + P` on the right
rather than through any `[2]` abstraction; `dblHom` is the minimal device that turns that
identity into a subgroup, and nothing else about it is used. -/

/-- Doubling on an additive commutative group, bundled. -/
def dblHom (A : Type*) [AddCommGroup A] : A →+ A :=
  AddMonoidHom.mk' (fun a => a + a) (fun a b => add_add_add_comm a b a b)

@[simp] theorem dblHom_apply {A : Type*} [AddCommGroup A] (a : A) : dblHom A a = a + a := rfl

/-- `2E_q(ℚ)`, as an actual `AddSubgroup` of the rational point group. -/
noncomputable def twoE (ε : ℤ) (m q : ℕ) : AddSubgroup (Ecurve ε m q).toAffine.Point :=
  (dblHom _).range

theorem mem_twoE {P : (Ecurve ε m q).toAffine.Point} :
    P ∈ twoE ε m q ↔ ∃ R : (Ecurve ε m q).toAffine.Point, R + R = P := by
  simp [twoE, AddMonoidHom.mem_range]

/-! ## `KExp ≤ GphiExp`

Supplied proved, from the certified P04b target: the image of `ker φ̂` under `δ_{E'}` lies inside
the image of `δ_{E'}`, which is `GphiExp`.  It is what makes `(KExp ε m).subgroupOf
(GphiExp ε m q)` in the statement below the intended subgroup rather than an intersection. -/

theorem KExp_le_GphiExp [Fact (Nat.Prime q)] (hP : Params ε m q) (hH : H41 ε m) :
    KExp ε m ≤ GphiExp ε m q := by
  intro c hc
  obtain ⟨P', _, hval⟩ :=
    AddSubgroup.mem_map.mp (((saturation_reconnect ε m q hP hH).2.2.2 c).mpr hc)
  exact ((saturation_reconnect ε m q hP hH).1 c).mp ⟨P', hval⟩

/-! ## Auxiliary constructions

All proved.  Nothing below assumes finiteness, and nothing below adds arithmetic: the two
homomorphisms `uHom` and `vHom` out of `E'_q(ℚ)` are built from `dualPhiHom` and the certified
`deltaHomE'`, and their kernels are computed from `P03d`, `P03e`/`P04a` and `P04b` alone. -/

section Aux

variable [Fact (Nat.Prime q)]

/-- **`φ̂` is surjective.**  `P04b` gives `range δ_E = ⊥`, so every rational point of `E_q` lies
in `ker δ_E`, which `P04a` identifies with `range φ̂`. -/
theorem dualPhiHom_surjective (hP : Params ε m q) (hH : H41 ε m) :
    Function.Surjective (dualPhiHom hP) := by
  intro P
  have hmem : deltaHomE hP P ∈ (deltaHomE hP).range := ⟨P, rfl⟩
  rw [(saturation_reconnect ε m q hP hH).2.2.1, AddSubgroup.mem_bot] at hmem
  have hker : P ∈ (deltaHomE hP).ker := hmem
  rw [ker_deltaHomE_eq_range_dualPhiHom hP] at hker
  exact AddMonoidHom.mem_range.mp hker

/-- `P' ↦ ⟦φ̂ P'⟧`, the connecting map before it descends to the cokernel of `φ`. -/
noncomputable def uHom (hP : Params ε m q) :
    (E'curve ε m q).toAffine.Point →+ ((Ecurve ε m q).toAffine.Point ⧸ twoE ε m q) :=
  (QuotientAddGroup.mk' (twoE ε m q)).comp (dualPhiHom hP)

@[simp] theorem uHom_apply (hP : Params ε m q) (P' : (E'curve ε m q).toAffine.Point) :
    uHom hP P' = QuotientAddGroup.mk (dualPhiHom hP P') := rfl

theorem uHom_surjective (hP : Params ε m q) (hH : H41 ε m) :
    Function.Surjective (uHom hP) := by
  intro x
  obtain ⟨P, rfl⟩ := QuotientAddGroup.mk_surjective x
  obtain ⟨P', rfl⟩ := dualPhiHom_surjective hP hH P
  exact ⟨P', rfl⟩

/-- The kernel of `P' ↦ ⟦φ̂ P'⟧`: exactly the points congruent, modulo `φ(E_q(ℚ))`, to a point
of `ker φ̂`.  The forward direction is `P03d` (`φ̂ ∘ φ` is doubling); so is the converse. -/
theorem mem_ker_uHom_iff (hP : Params ε m q) (P' : (E'curve ε m q).toAffine.Point) :
    P' ∈ (uHom hP).ker ↔ ∃ R' ∈ (dualPhiHom hP).ker, P' - R' ∈ (phiHom hP).range := by
  constructor
  · intro h
    have h1 : dualPhiHom hP P' ∈ twoE ε m q :=
      (QuotientAddGroup.eq_zero_iff _).mp (AddMonoidHom.mem_ker.mp h)
    obtain ⟨R, hR⟩ := mem_twoE.mp h1
    refine ⟨P' - phiHom hP R, ?_, ?_⟩
    · rw [AddMonoidHom.mem_ker, map_sub, (isogeny_composites_eq_double ε m q hP).1 R, hR,
        sub_self]
    · have : P' - (P' - phiHom hP R) = phiHom hP R := by abel
      rw [this]
      exact AddMonoidHom.mem_range.mpr ⟨R, rfl⟩
  · rintro ⟨R', hR', hsub⟩
    obtain ⟨R, hR⟩ := AddMonoidHom.mem_range.mp hsub
    have hP'eq : P' = R' + phiHom hP R := by rw [hR]; abel
    have hval : dualPhiHom hP P' = R + R := by
      rw [hP'eq, map_add, AddMonoidHom.mem_ker.mp hR', zero_add,
        (isogeny_composites_eq_double ε m q hP).1 R]
    exact AddMonoidHom.mem_ker.mpr
      ((QuotientAddGroup.eq_zero_iff _).mpr (mem_twoE.mpr ⟨R, hval.symm⟩))

/-- Every descent class of a rational point of `E'_q` lies in `GphiExp` — the first component
of the certified `P04b.saturation_reconnect`. -/
theorem delta_mem_GphiExp (hP : Params ε m q) (hH : H41 ε m)
    (P' : (E'curve ε m q).toAffine.Point) :
    Additive.toMul (deltaHomE' hP P') ∈ GphiExp ε m q :=
  ((saturation_reconnect ε m q hP hH).1 (Additive.toMul (deltaHomE' hP P'))).mp ⟨P', rfl⟩

/-- The descent class of `P'`, as an element of `GphiExp`. -/
noncomputable def gClass (hP : Params ε m q) (hH : H41 ε m)
    (P' : (E'curve ε m q).toAffine.Point) : ↥(GphiExp ε m q) :=
  ⟨Additive.toMul (deltaHomE' hP P'), delta_mem_GphiExp hP hH P'⟩

theorem gClass_ofMul (hP : Params ε m q) (hH : H41 ε m)
    (P' : (E'curve ε m q).toAffine.Point) :
    Additive.ofMul ((gClass hP hH P' : Qsq)) = deltaHomE' hP P' := rfl

theorem gClass_add (hP : Params ε m q) (hH : H41 ε m)
    (P' Q' : (E'curve ε m q).toAffine.Point) :
    gClass hP hH (P' + Q') = gClass hP hH P' * gClass hP hH Q' :=
  Subtype.ext (congrArg Additive.toMul (map_add (deltaHomE' hP) P' Q'))

/-- `P' ↦ [δ_{E'} P']`, into the square-class quotient `GphiExp ⧸ KExp`. -/
noncomputable def vHom (hP : Params ε m q) (hH : H41 ε m) :
    (E'curve ε m q).toAffine.Point →+
      Additive (↥(GphiExp ε m q) ⧸ (KExp ε m).subgroupOf (GphiExp ε m q)) where
  toFun P' := Additive.ofMul (QuotientGroup.mk (gClass hP hH P'))
  map_zero' := by
    have h0 : gClass hP hH 0 = 1 :=
      Subtype.ext (congrArg Additive.toMul (map_zero (deltaHomE' hP)))
    simp only [h0, QuotientGroup.mk_one, ofMul_one]
  map_add' := by
    intro P' Q'
    simp only [gClass_add, QuotientGroup.mk_mul, ofMul_mul]

@[simp] theorem vHom_apply (hP : Params ε m q) (hH : H41 ε m)
    (P' : (E'curve ε m q).toAffine.Point) :
    vHom hP hH P' = Additive.ofMul (QuotientGroup.mk (gClass hP hH P')) := rfl

theorem vHom_surjective (hP : Params ε m q) (hH : H41 ε m) :
    Function.Surjective (vHom hP hH) := by
  intro x
  obtain ⟨c, hc⟩ := QuotientGroup.mk_surjective (Additive.toMul x)
  obtain ⟨P', hP'⟩ := ((saturation_reconnect ε m q hP hH).1 (c : Qsq)).mpr c.2
  refine ⟨P', ?_⟩
  rw [vHom_apply, show gClass hP hH P' = c from Subtype.ext (congrArg Additive.toMul hP'), hc]
  rfl

/-- The kernel of `vHom`, described exactly as the kernel of `uHom` was: this is the fourth
component of `P04b.saturation_reconnect`, which says `δ_{E'}(ker φ̂) = KExp`, together with
`ker δ_{E'} = range φ`. -/
theorem mem_ker_vHom_iff (hP : Params ε m q) (hH : H41 ε m)
    (P' : (E'curve ε m q).toAffine.Point) :
    P' ∈ (vHom hP hH).ker ↔ ∃ R' ∈ (dualPhiHom hP).ker, P' - R' ∈ (phiHom hP).range := by
  have hK : P' ∈ (vHom hP hH).ker ↔ (gClass hP hH P' : Qsq) ∈ KExp ε m := by
    rw [AddMonoidHom.mem_ker, vHom_apply,
      show (0 : Additive (↥(GphiExp ε m q) ⧸ (KExp ε m).subgroupOf (GphiExp ε m q)))
        = Additive.ofMul 1 from rfl,
      Additive.ofMul.injective.eq_iff, QuotientGroup.eq_one_iff, Subgroup.mem_subgroupOf]
  rw [hK, ← (saturation_reconnect ε m q hP hH).2.2.2 ((gClass hP hH P' : Qsq)),
    gClass_ofMul hP hH P']
  constructor
  · intro h
    obtain ⟨R', hR', hval⟩ := AddSubgroup.mem_map.mp h
    refine ⟨R', hR', ?_⟩
    have hker : P' - R' ∈ (deltaHomE' hP).ker :=
      AddMonoidHom.mem_ker.mpr (by rw [map_sub, hval, sub_self])
    rwa [ker_deltaHomE'_eq_range_phiHom hP] at hker
  · rintro ⟨R', hR', hsub⟩
    refine AddSubgroup.mem_map.mpr ⟨R', hR', ?_⟩
    have hker : P' - R' ∈ (deltaHomE' hP).ker := by
      rw [ker_deltaHomE'_eq_range_phiHom hP]; exact hsub
    have h0 : deltaHomE' hP P' - deltaHomE' hP R' = 0 := by
      rw [← map_sub]; exact AddMonoidHom.mem_ker.mp hker
    exact (sub_eq_zero.mp h0).symm

theorem ker_uHom_eq_ker_vHom (hP : Params ε m q) (hH : H41 ε m) :
    (uHom hP).ker = (vHom hP hH).ker := by
  ext P'
  rw [mem_ker_uHom_iff hP P', mem_ker_vHom_iff hP hH P']

/-- Two surjective homomorphisms out of the same group with the same kernel have isomorphic
targets.  Stated with the target of the second one displayed as `Additive (X ⧸ N)` for abstract
`X` and `N`, so that the concrete square-class subgroups never have to be unfolded. -/
noncomputable def equivAdditiveQuotientOfKerEq {A B : Type*} [AddCommGroup A] [AddCommGroup B]
    {X : Type*} [CommGroup X] {N : Subgroup X} [N.Normal] (f : A →+ B)
    (g : A →+ Additive (X ⧸ N)) (hf : Function.Surjective f) (hg : Function.Surjective g)
    (h : f.ker = g.ker) : B ≃+ Additive (X ⧸ N) :=
  ((QuotientAddGroup.quotientKerEquivOfSurjective f hf).symm.trans
      (QuotientAddGroup.quotientAddEquivOfEq h)).trans
    (QuotientAddGroup.quotientKerEquivOfSurjective g hg)

/-- `Nat.card` of an additive quotient is the index of the subgroup. -/
theorem card_additive_quotient {X : Type*} [CommGroup X] (N : Subgroup X) [N.Normal] :
    Nat.card (Additive (X ⧸ N)) = N.index := by
  rw [Subgroup.index_eq_card]
  exact Nat.card_congr Additive.toMul

/-- **`E_q(ℚ)/2E_q(ℚ) ≃+ GphiExp ⧸ KExp`.**  Both are the quotient of `E'_q(ℚ)` by one and the
same subgroup. -/
noncomputable def quotTwoEEquiv (hP : Params ε m q) (hH : H41 ε m) :
    ((Ecurve ε m q).toAffine.Point ⧸ twoE ε m q) ≃+
      Additive (↥(GphiExp ε m q) ⧸ (KExp ε m).subgroupOf (GphiExp ε m q)) :=
  equivAdditiveQuotientOfKerEq (f := uHom hP) (g := vHom hP hH) (uHom_surjective hP hH)
    (vHom_surjective hP hH) (ker_uHom_eq_ker_vHom hP hH)

end Aux

/-! ## The P04c target -/

/--
**Target.**  `E_q(ℚ)/2E_q(ℚ)`.

Four conjuncts.

1. **The connecting homomorphism.**  `φ̂` induces a map

       E'_q(ℚ) ⧸ φ(E_q(ℚ))   →+   E_q(ℚ) ⧸ 2E_q(ℚ)

   sending `⟦P'⟧` to `⟦φ̂(P')⟧` — pinned by the trailing `∀ P'` clause, so this is the actual
   map and not merely some homomorphism.  It is **surjective**, and its **kernel is exactly the
   image of `ker φ̂`**.  This is the point-cokernel exact sequence, in the only form it takes
   here; the fourth term vanishes because the dual cokernel is trivial.

2. **The square-class description.**

       E_q(ℚ) ⧸ 2E_q(ℚ)   ≃+   Additive (GphiExp ⧸ KExp.subgroupOf GphiExp)

   i.e. `E_q(ℚ)/2E_q(ℚ) ≅ G_{φ,exp}/K_{exp}` — the explicit descent quotient of square classes
   that the saturation theorem computed, now identified with an actual point quotient.

3. **`Nat.card (E_q(ℚ) ⧸ 2E_q(ℚ)) = 2`**, which is conjunct 2 together with the certified
   `((KExp ε m).subgroupOf (GphiExp ε m q)).index = 2`.

4. **`E_q(ℚ)/2E_q(ℚ) ≃+ ZMod 2`** — the group is `C₂`.

## Route

Deliberately not supplied.  No new arithmetic is needed: every ingredient is in the table at
the head of this file, and conjunct 1 needs nothing beyond `P03d`, `P03e` and `P04b`'s second
conjunct.  Conjuncts 2–4 are transport and bookkeeping over the certified identifications.

## What must NOT appear

`Sel₂`, Ш, `rank`, `L(E,s)`, `SelmerSet`, `LocalKummerAll`, any new local `p`-adic argument,
any statement about `E_q(ℚ)` other than this quotient, and any claim that `2E_q(ℚ)` or
`E_q(ℚ)` is finite.  `Nat.card` is permitted **only** for the quotient
`E_q(ℚ) ⧸ 2E_q(ℚ)` in conjunct 3. -/
theorem two_descent_quotient (ε : ℤ) (m q : ℕ) [Fact (Nat.Prime q)]
    (hP : Params ε m q) (hH : H41 ε m) :
    (∃ f : ((E'curve ε m q).toAffine.Point ⧸ (phiHom hP).range) →+
             ((Ecurve ε m q).toAffine.Point ⧸ twoE ε m q),
        (∀ P' : (E'curve ε m q).toAffine.Point,
            f (QuotientAddGroup.mk P') = QuotientAddGroup.mk (dualPhiHom hP P'))
      ∧ Function.Surjective f
      ∧ f.ker = AddSubgroup.map (QuotientAddGroup.mk' ((phiHom hP).range)) (dualPhiHom hP).ker)
  ∧ Nonempty (((Ecurve ε m q).toAffine.Point ⧸ twoE ε m q)
        ≃+ Additive (↥(GphiExp ε m q) ⧸ (KExp ε m).subgroupOf (GphiExp ε m q)))
  ∧ Nat.card ((Ecurve ε m q).toAffine.Point ⧸ twoE ε m q) = 2
  ∧ Nonempty (((Ecurve ε m q).toAffine.Point ⧸ twoE ε m q) ≃+ ZMod 2) := by
  -- The connecting homomorphism, as the descent of `uHom` to the cokernel of `φ`.
  have hle : (phiHom hP).range ≤ (uHom hP).ker := by
    rintro x hx
    obtain ⟨R, rfl⟩ := AddMonoidHom.mem_range.mp hx
    refine AddMonoidHom.mem_ker.mpr ((QuotientAddGroup.eq_zero_iff _).mpr ?_)
    rw [(isogeny_composites_eq_double ε m q hP).1 R]
    exact mem_twoE.mpr ⟨R, rfl⟩
  set f : ((E'curve ε m q).toAffine.Point ⧸ (phiHom hP).range) →+
      ((Ecurve ε m q).toAffine.Point ⧸ twoE ε m q) :=
    QuotientAddGroup.lift ((phiHom hP).range) (uHom hP) hle
  have hfmk : ∀ P' : (E'curve ε m q).toAffine.Point,
      f (QuotientAddGroup.mk P') = QuotientAddGroup.mk (dualPhiHom hP P') := fun P' => rfl
  have hfsurj : Function.Surjective f := by
    intro x
    obtain ⟨P', hP'⟩ := uHom_surjective hP hH x
    exact ⟨QuotientAddGroup.mk P', by rw [hfmk P']; exact hP'⟩
  have hfker : f.ker
      = AddSubgroup.map (QuotientAddGroup.mk' ((phiHom hP).range)) (dualPhiHom hP).ker := by
    ext x
    obtain ⟨P', rfl⟩ := QuotientAddGroup.mk_surjective x
    rw [AddMonoidHom.mem_ker, hfmk P']
    constructor
    · intro h
      have h1 : P' ∈ (uHom hP).ker := AddMonoidHom.mem_ker.mpr h
      obtain ⟨R', hR', hsub⟩ := (mem_ker_uHom_iff hP P').mp h1
      refine AddSubgroup.mem_map.mpr ⟨R', hR', ?_⟩
      exact QuotientAddGroup.eq_iff_sub_mem.mpr (by
        simpa using (AddSubgroup.neg_mem _ hsub))
    · intro h
      obtain ⟨R', hR', hval⟩ := AddSubgroup.mem_map.mp h
      have hsub : P' - R' ∈ (phiHom hP).range := by
        have : (QuotientAddGroup.mk P' : _ ⧸ (phiHom hP).range) = QuotientAddGroup.mk R' :=
          hval.symm
        exact QuotientAddGroup.eq_iff_sub_mem.mp this
      exact AddMonoidHom.mem_ker.mp ((mem_ker_uHom_iff hP P').mpr ⟨R', hR', hsub⟩)
  -- The square-class description.
  have hequiv := quotTwoEEquiv hP hH
  -- The cardinality.
  have hindex : ((KExp ε m).subgroupOf (GphiExp ε m q)).index = 2 :=
    (sdyadic_saturation ε m q hP hH).2.2.2.2
  have hcard : Nat.card ((Ecurve ε m q).toAffine.Point ⧸ twoE ε m q) = 2 := by
    rw [Nat.card_congr hequiv.toEquiv,
      card_additive_quotient ((KExp ε m).subgroupOf (GphiExp ε m q))]
    exact hindex
  -- `C₂`.
  have hzmod : Nonempty (((Ecurve ε m q).toAffine.Point ⧸ twoE ε m q) ≃+ ZMod 2) := by
    haveI : Fact (Nat.Prime 2) := ⟨Nat.prime_two⟩
    have hcyc : IsAddCyclic ((Ecurve ε m q).toAffine.Point ⧸ twoE ε m q) :=
      isAddCyclic_of_prime_card (p := 2) hcard
    have e := zmodAddCyclicAddEquiv hcyc
    rw [hcard] at e
    exact ⟨e.symm⟩
  exact ⟨⟨f, hfmk, hfsurj, hfker⟩, ⟨hequiv⟩, hcard, hzmod⟩

end P04c
