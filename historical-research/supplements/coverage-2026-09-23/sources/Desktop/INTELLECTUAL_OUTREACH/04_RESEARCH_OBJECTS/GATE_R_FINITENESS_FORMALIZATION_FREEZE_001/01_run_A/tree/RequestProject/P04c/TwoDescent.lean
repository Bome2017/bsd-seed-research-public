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

/-! ## Auxiliary construction

Everything below is proved, and uses nothing but the certified inputs listed at the head of
the file.  The plan:

* `range δ_E = ⊥` (P04b) and `ker δ_E = range φ̂` (P04a) give `φ̂` **surjective**;
* `dualQuotHom` is `P' ↦ ⟦φ̂ P'⟧ : E'_q(ℚ) →+ E_q(ℚ) ⧸ 2E_q(ℚ)`; it is surjective, and
  `P03d` makes it kill `range φ`, so it descends to the connecting map of conjunct 1;
* `gphiQuotHom` is `P' ↦ ⟦δ_{E'} P'⟧ : E'_q(ℚ) →+ Additive (GphiExp ⧸ KExp.subgroupOf GphiExp)`;
  it is surjective by P04b's `range δ_{E'} = GphiExp`;
* the two homomorphisms have the **same kernel** — both are `ker φ̂ + range φ`, the first by
  `P03d` and the second by P04b's `δ_{E'}(ker φ̂) = KExp` together with
  `ker δ_{E'} = range φ` — so the two quotients of `E'_q(ℚ)` agree, which is conjunct 2. -/

section Aux

variable [Fact (Nat.Prime q)]

/-- **`φ̂` is surjective.**  `P04b` gives `range δ_E = ⊥`, so every point of `E_q(ℚ)` lies in
`ker δ_E`, which `P04a` identifies with `range φ̂`. -/
theorem dualPhiHom_surjective (hP : Params ε m q) (hH : H41 ε m) :
    Function.Surjective (dualPhiHom hP) := by
  intro P
  have hmem : deltaHomE hP P ∈ (deltaHomE hP).range := ⟨P, rfl⟩
  rw [(saturation_reconnect ε m q hP hH).2.2.1, AddSubgroup.mem_bot] at hmem
  have hker : P ∈ (deltaHomE hP).ker := hmem
  rw [ker_deltaHomE_eq_range_dualPhiHom hP, AddMonoidHom.mem_range] at hker
  exact hker

/-- `P' ↦ ⟦φ̂ P'⟧`, before descending to the cokernel of `φ`. -/
noncomputable def dualQuotHom (hP : Params ε m q) :
    (E'curve ε m q).toAffine.Point →+ ((Ecurve ε m q).toAffine.Point ⧸ twoE ε m q) :=
  (QuotientAddGroup.mk' (twoE ε m q)).comp (dualPhiHom hP)

@[simp] theorem dualQuotHom_apply (hP : Params ε m q)
    (P' : (E'curve ε m q).toAffine.Point) :
    dualQuotHom hP P' = QuotientAddGroup.mk (dualPhiHom hP P') := rfl

theorem dualQuotHom_surjective (hP : Params ε m q) (hH : H41 ε m) :
    Function.Surjective (dualQuotHom hP) := by
  intro x
  obtain ⟨P, rfl⟩ := QuotientAddGroup.mk_surjective x
  obtain ⟨P', rfl⟩ := dualPhiHom_surjective hP hH P
  exact ⟨P', rfl⟩

/-- **The kernel of `P' ↦ ⟦φ̂ P'⟧`, pointwise.**  `φ̂ P'` is a double exactly when `P'` differs
from a point of `ker φ̂` by a `φ`-image.  Both directions are `P03d`'s `φ̂(φ R) = R + R`. -/
theorem dualPhi_mem_twoE_iff (hP : Params ε m q) {P' : (E'curve ε m q).toAffine.Point} :
    dualPhiHom hP P' ∈ twoE ε m q ↔
      ∃ Q ∈ (dualPhiHom hP).ker, P' - Q ∈ (phiHom hP).range := by
  constructor
  · intro h
    obtain ⟨R, hR⟩ := mem_twoE.mp h
    refine ⟨P' - phiHom hP R, ?_, ?_⟩
    · rw [AddMonoidHom.mem_ker, map_sub, (isogeny_composites_eq_double ε m q hP).1 R, hR,
        sub_self]
    · rw [sub_sub_cancel]
      exact ⟨R, rfl⟩
  · rintro ⟨Q, hQ, R, hR⟩
    rw [AddMonoidHom.mem_ker] at hQ
    have hP'eq : P' = phiHom hP R + Q := by rw [hR]; abel
    refine mem_twoE.mpr ⟨R, ?_⟩
    rw [hP'eq, map_add, hQ, add_zero, (isogeny_composites_eq_double ε m q hP).1 R]

/-- The connecting homomorphism of conjunct 1: `⟦P'⟧ ↦ ⟦φ̂ P'⟧`.  It is well defined because
`P03d` says `φ̂(φ R) = R + R ∈ 2E_q(ℚ)`. -/
noncomputable def connectingHom (hP : Params ε m q) :
    ((E'curve ε m q).toAffine.Point ⧸ (phiHom hP).range) →+
      ((Ecurve ε m q).toAffine.Point ⧸ twoE ε m q) :=
  QuotientAddGroup.lift _ (dualQuotHom hP) (by
    rintro _ ⟨R, rfl⟩
    rw [AddMonoidHom.mem_ker, dualQuotHom_apply, QuotientAddGroup.eq_zero_iff,
      (isogeny_composites_eq_double ε m q hP).1 R]
    exact mem_twoE.mpr ⟨R, rfl⟩)

@[simp] theorem connectingHom_mk (hP : Params ε m q)
    (P' : (E'curve ε m q).toAffine.Point) :
    connectingHom hP (QuotientAddGroup.mk P') = QuotientAddGroup.mk (dualPhiHom hP P') := rfl

theorem connectingHom_surjective (hP : Params ε m q) (hH : H41 ε m) :
    Function.Surjective (connectingHom hP) := by
  intro x
  obtain ⟨P', hP'⟩ := dualQuotHom_surjective hP hH x
  exact ⟨QuotientAddGroup.mk P', hP'⟩

theorem ker_connectingHom (hP : Params ε m q) :
    (connectingHom hP).ker =
      AddSubgroup.map (QuotientAddGroup.mk' ((phiHom hP).range)) (dualPhiHom hP).ker := by
  ext x
  obtain ⟨P', rfl⟩ := QuotientAddGroup.mk_surjective x
  constructor
  · intro hx
    rw [AddMonoidHom.mem_ker, connectingHom_mk, QuotientAddGroup.eq_zero_iff] at hx
    obtain ⟨Q, hQ, hR⟩ := (dualPhi_mem_twoE_iff hP).mp hx
    refine AddSubgroup.mem_map.mpr ⟨Q, hQ, ?_⟩
    rw [QuotientAddGroup.mk'_apply, QuotientAddGroup.eq_iff_sub_mem]
    have hneg := neg_mem hR
    rwa [neg_sub] at hneg
  · intro hx
    obtain ⟨Q, hQ, hEq⟩ := AddSubgroup.mem_map.mp hx
    rw [AddMonoidHom.mem_ker, ← hEq, QuotientAddGroup.mk'_apply, connectingHom_mk,
      AddMonoidHom.mem_ker.mp hQ]
    simp

/-! ### The square-class side -/

/-- The descent class of a rational point of `E'_q` lies in `GphiExp`: P04b's first conjunct. -/
theorem delta_mem_GphiExp (hP : Params ε m q) (hH : H41 ε m)
    (P' : (E'curve ε m q).toAffine.Point) :
    delta (phiA ε m q) (phiB ε m q) P' ∈ GphiExp ε m q :=
  ((saturation_reconnect ε m q hP hH).1 _).mp ⟨P', rfl⟩

/-- `P' ↦ ⟦δ_{E'} P'⟧`, valued in `Additive (GphiExp ⧸ KExp.subgroupOf GphiExp)`. -/
noncomputable def gphiQuotHom (hP : Params ε m q) (hH : H41 ε m) :
    (E'curve ε m q).toAffine.Point →+
      Additive (↥(GphiExp ε m q) ⧸ (KExp ε m).subgroupOf (GphiExp ε m q)) where
  toFun P' := Additive.ofMul (QuotientGroup.mk
    (⟨delta (phiA ε m q) (phiB ε m q) P', delta_mem_GphiExp hP hH P'⟩ : ↥(GphiExp ε m q)))
  map_zero' := by
    have h0 : (⟨delta (phiA ε m q) (phiB ε m q) 0, delta_mem_GphiExp hP hH 0⟩ :
        ↥(GphiExp ε m q)) = 1 :=
      Subtype.ext (congrArg Additive.toMul (deltaHomE' hP).map_zero)
    rw [h0]
    rfl
  map_add' P R := by
    have hmul : (⟨delta (phiA ε m q) (phiB ε m q) (P + R), delta_mem_GphiExp hP hH (P + R)⟩ :
        ↥(GphiExp ε m q))
        = ((⟨delta (phiA ε m q) (phiB ε m q) P, delta_mem_GphiExp hP hH P⟩ :
            ↥(GphiExp ε m q))
          * ((⟨delta (phiA ε m q) (phiB ε m q) R, delta_mem_GphiExp hP hH R⟩ :
            ↥(GphiExp ε m q)))) :=
      Subtype.ext (congrArg Additive.toMul ((deltaHomE' hP).map_add P R))
    rw [hmul]
    rfl

@[simp] theorem gphiQuotHom_apply (hP : Params ε m q) (hH : H41 ε m)
    (P' : (E'curve ε m q).toAffine.Point) :
    gphiQuotHom hP hH P' = Additive.ofMul (QuotientGroup.mk
      (⟨delta (phiA ε m q) (phiB ε m q) P', delta_mem_GphiExp hP hH P'⟩ :
        ↥(GphiExp ε m q))) := rfl

theorem gphiQuotHom_surjective (hP : Params ε m q) (hH : H41 ε m) :
    Function.Surjective (gphiQuotHom hP hH) := by
  intro z
  obtain ⟨c, hc⟩ := QuotientGroup.mk_surjective (Additive.toMul z)
  obtain ⟨P', hP'⟩ := ((saturation_reconnect ε m q hP hH).1 (c : Qsq)).mpr c.2
  have hval : delta (phiA ε m q) (phiB ε m q) P' = (c : Qsq) := congrArg Additive.toMul hP'
  refine ⟨P', ?_⟩
  rw [gphiQuotHom_apply]
  have : (⟨delta (phiA ε m q) (phiB ε m q) P', delta_mem_GphiExp hP hH P'⟩ :
      ↥(GphiExp ε m q)) = c := Subtype.ext hval
  rw [this, hc]
  rfl

theorem mem_ker_gphiQuotHom (hP : Params ε m q) (hH : H41 ε m)
    (P' : (E'curve ε m q).toAffine.Point) :
    P' ∈ (gphiQuotHom hP hH).ker ↔ delta (phiA ε m q) (phiB ε m q) P' ∈ KExp ε m := by
  rw [AddMonoidHom.mem_ker, gphiQuotHom_apply]
  rw [show ((0 : Additive (↥(GphiExp ε m q) ⧸ (KExp ε m).subgroupOf (GphiExp ε m q))))
      = Additive.ofMul 1 from rfl]
  rw [Additive.ofMul.apply_eq_iff_eq, QuotientGroup.eq_one_iff]
  exact Subgroup.mem_subgroupOf

/-- **The two homomorphisms out of `E'_q(ℚ)` have the same kernel.**  On the left the condition
is `φ̂ P' ∈ 2E_q(ℚ)`, i.e. `P' ∈ ker φ̂ + range φ` by `P03d`; on the right it is
`δ_{E'} P' ∈ KExp`, i.e. `δ_{E'} P' ∈ δ_{E'}(ker φ̂)` by P04b, i.e. again
`P' ∈ ker φ̂ + ker δ_{E'} = ker φ̂ + range φ`. -/
theorem ker_dualQuotHom_eq_ker_gphiQuotHom (hP : Params ε m q) (hH : H41 ε m) :
    (dualQuotHom hP).ker = (gphiQuotHom hP hH).ker := by
  ext P'
  rw [AddMonoidHom.mem_ker, dualQuotHom_apply, QuotientAddGroup.eq_zero_iff,
    dualPhi_mem_twoE_iff hP, mem_ker_gphiQuotHom hP hH,
    ← (saturation_reconnect ε m q hP hH).2.2.2 (delta (phiA ε m q) (phiB ε m q) P')]
  constructor
  · rintro ⟨Q, hQ, hR⟩
    refine AddSubgroup.mem_map.mpr ⟨Q, hQ, ?_⟩
    have hz : deltaHomE' hP (P' - Q) = 0 := by
      rw [← AddMonoidHom.mem_ker, ker_deltaHomE'_eq_range_phiHom hP]
      exact hR
    rw [map_sub, sub_eq_zero] at hz
    exact hz.symm
  · intro h
    obtain ⟨Q, hQ, hval⟩ := AddSubgroup.mem_map.mp h
    refine ⟨Q, hQ, ?_⟩
    rw [← ker_deltaHomE'_eq_range_phiHom hP, AddMonoidHom.mem_ker, map_sub, sub_eq_zero]
    exact hval.symm

/-! ### Transport

The two `first isomorphism theorem` steps and the cardinality are routed through the three
general lemmas below.  Stating them for an abstract `Additive (B ⧸ K)` keeps the elaborator
from unfolding the concrete square-class quotient. -/

section GeneralTransport

variable {A : Type*} [AddCommGroup A] {B : Type*} [CommGroup B] {K : Subgroup B}

/-- The first isomorphism theorem, for a surjection onto `Additive (B ⧸ K)`. -/
noncomputable def genQuotKerEquiv (f : A →+ Additive (B ⧸ K)) (hf : Function.Surjective f) :
    (A ⧸ f.ker) ≃+ Additive (B ⧸ K) :=
  QuotientAddGroup.quotientKerEquivOfSurjective f hf

/-- `Nat.card (Additive (B ⧸ K))` is the index of `K`. -/
theorem genCardAdditiveQuot : Nat.card (Additive (B ⧸ K)) = K.index :=
  (Nat.card_congr Additive.toMul).trans (Subgroup.index_eq_card K).symm

end GeneralTransport

/-- **Conjunct 2.**  `E_q(ℚ) ⧸ 2E_q(ℚ) ≃+ Additive (GphiExp ⧸ KExp.subgroupOf GphiExp)`, as the
two quotients of `E'_q(ℚ)` by the one common kernel. -/
noncomputable def twoEQuotEquivGphiQuot (hP : Params ε m q) (hH : H41 ε m) :
    ((Ecurve ε m q).toAffine.Point ⧸ twoE ε m q) ≃+
      Additive (↥(GphiExp ε m q) ⧸ (KExp ε m).subgroupOf (GphiExp ε m q)) :=
  (QuotientAddGroup.quotientKerEquivOfSurjective (dualQuotHom hP)
      (dualQuotHom_surjective hP hH)).symm.trans
    ((QuotientAddGroup.quotientAddEquivOfEq
        (ker_dualQuotHom_eq_ker_gphiQuotHom hP hH)).trans
      (genQuotKerEquiv (gphiQuotHom hP hH) (gphiQuotHom_surjective hP hH)))

/-- **Conjunct 3.**  The certified index `((KExp ε m).subgroupOf (GphiExp ε m q)).index = 2`,
transported along conjunct 2.  No finiteness is assumed anywhere: `Nat.card` of the quotient
is computed, and nothing is claimed about `E_q(ℚ)`. -/
theorem card_twoE_quotient (hP : Params ε m q) (hH : H41 ε m) :
    Nat.card ((Ecurve ε m q).toAffine.Point ⧸ twoE ε m q) = 2 := by
  rw [Nat.card_congr (twoEQuotEquivGphiQuot hP hH).toEquiv, genCardAdditiveQuot]
  exact (sdyadic_saturation ε m q hP hH).2.2.2.2

/-- **Conjunct 4.**  A group with `Nat.card = 2` is `C₂`. -/
theorem twoE_quotient_equiv_zmod (hP : Params ε m q) (hH : H41 ε m) :
    Nonempty (((Ecurve ε m q).toAffine.Point ⧸ twoE ε m q) ≃+ ZMod 2) := by
  have hcard := card_twoE_quotient hP hH
  have hcyc : IsAddCyclic ((Ecurve ε m q).toAffine.Point ⧸ twoE ε m q) :=
    isAddCyclic_of_prime_card (p := 2) hcard
  have e := zmodAddCyclicAddEquiv hcyc
  rw [hcard] at e
  exact ⟨e.symm⟩

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
  exact ⟨⟨connectingHom hP, fun P' => rfl, connectingHom_surjective hP hH,
      ker_connectingHom hP⟩,
    ⟨twoEQuotEquivGphiQuot hP hH⟩,
    card_twoE_quotient hP hH,
    twoE_quotient_equiv_zmod hP hH⟩

end P04c
