import Mathlib

/-!
# Global duality determines only maximal isotropy, and that bounds nothing

**Correction (added after review).**  The model used below is an *alternating* (symplectic)
form.  That is not the shape of the arithmetic pairing for odd `n`: the local Tate pairing on
`H¹(ℚ_v, E[n])` induced by the Weil pairing and the cup product is **symmetric** (Poonen–Rains,
§4.1), the antisymmetry of the Weil pairing and of the cup product on degree-one classes
cancelling.  The statements below should therefore be read as linear algebra in the symplectic
model only.  The same sharpness conclusion for the correct symmetric pairing is proved in
`RequestProject/SymmetricIsotropySharpness.lean`
(`SeedBSD.Symmetric.duality_bound_is_sharp_symmetric`), so the conclusion survives the
correction; but the symplectic model alone does not establish it for the arithmetic pairing.

Poitou–Tate duality for the self-dual module `M = E[n]` says exactly two things about the
`n`-Selmer group, once one works inside the restricted product
`V = ⊕'_v H¹(ℚ_v, M)` with its perfect local-duality pairing:

* the image `X` of the global cohomology `H¹(ℚ, M)` is **maximal isotropic**;
* the Kummer local conditions `L = ∏_v L_v` are **maximal isotropic**;

and `X ∩ L` is the image of `Sel_n(E)` in the restricted product.  (This is the Poonen–Rains
picture.)  The identification is *not* an equality with `Sel_n(E)` itself: the localisation map
`H¹(ℚ, M) → V` has a kernel, `Ш¹(ℚ, E[n])`, and `X ∩ L` is the quotient of `Sel_n(E)` by that
kernel.  Nothing in this file controls it — see the `Scope and the localisation kernel` section
of `RequestProject/SymmetricIsotropySharpness.lean`.

This file machine-checks that those two facts are *exhausted* by the inequality
`dim(X ∩ L) ≤ ½ dim V`, and that **no better bound exists**: inside a `2n`-dimensional
symplectic space, for every `d ≤ n` there is a pair of maximal isotropic subspaces meeting in
dimension exactly `d`.

Consequently a purely duality-theoretic argument can never bound `dim(X ∩ L)` below
`½ dim V`, and `dim V` grows with the level and with the set of ramified places.  This is the
formal content of the obstruction "quantitative global duality does not bound `Ш[n]`".

The construction: `V = (Fin n → F) × (Fin n → F)` with the standard symplectic form
`B x y = ∑ i, (x.1 i * y.2 i - x.2 i * y.1 i)`, `X = (Fin n → F) × 0`, and
`L d = {x | x.2 i = 0 for i < d, x.1 i = 0 for i ≥ d}`.
-/

namespace SeedBSD

open Finset

variable {F : Type*} [Field F]

/-- The ambient `2n`-dimensional symplectic space. -/
abbrev Symp (F : Type*) (n : ℕ) := (Fin n → F) × (Fin n → F)

/-- The standard symplectic form. -/
def sympForm {n : ℕ} (x y : Symp F n) : F := ∑ i, (x.1 i * y.2 i - x.2 i * y.1 i)

theorem sympForm_self {n : ℕ} (x : Symp F n) : sympForm x x = 0 := by
  simp [sympForm, mul_comm]

/-- The number of indices of `Fin n` below `d`. -/
theorem card_lt_subtype (n d : ℕ) : Fintype.card {i : Fin n // (i : ℕ) < d} = min d n := by
  classical
  rw [Fintype.card_subtype]
  have himg : (Finset.univ.filter (fun x : Fin n => (x : ℕ) < d)).image Fin.val
      = Finset.range (min d n) := by
    ext m
    simp only [Finset.mem_image, Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_range,
      lt_min_iff]
    constructor
    · rintro ⟨i, hi, rfl⟩; exact ⟨hi, i.isLt⟩
    · rintro ⟨h1, h2⟩; exact ⟨⟨m, h2⟩, h1, rfl⟩
  rw [← Finset.card_image_of_injective _ Fin.val_injective, himg, Finset.card_range]

theorem sympForm_skew {n : ℕ} (x y : Symp F n) : sympForm x y = - sympForm y x := by
  simp only [sympForm, ← Finset.sum_neg_distrib]
  exact Finset.sum_congr rfl fun i _ => by ring

/-- `X = (Fin n → F) × 0`, the "global" maximal isotropic in the model. -/
def Xsub (F : Type*) [Field F] (n : ℕ) : Submodule F (Symp F n) where
  carrier := {x | x.2 = 0}
  add_mem' := by intro a b ha hb; simp_all [Set.mem_setOf_eq]
  zero_mem' := by simp
  smul_mem' := by intro c a ha; simp_all [Set.mem_setOf_eq]

/-- `L d`, a second maximal isotropic subspace, meeting `X` in dimension `d`. -/
def Lsub (F : Type*) [Field F] (n d : ℕ) : Submodule F (Symp F n) where
  carrier := {x | (∀ i : Fin n, (i : ℕ) < d → x.2 i = 0) ∧ (∀ i : Fin n, d ≤ (i : ℕ) → x.1 i = 0)}
  add_mem' := by
    rintro a b ⟨ha1, ha2⟩ ⟨hb1, hb2⟩
    exact ⟨fun i hi => by simp [ha1 i hi, hb1 i hi], fun i hi => by simp [ha2 i hi, hb2 i hi]⟩
  zero_mem' := by constructor <;> intro i _ <;> rfl
  smul_mem' := by
    rintro c a ⟨ha1, ha2⟩
    exact ⟨fun i hi => by simp [ha1 i hi], fun i hi => by simp [ha2 i hi]⟩

theorem Xsub_isotropic {n : ℕ} {x y : Symp F n} (hx : x ∈ Xsub F n) (hy : y ∈ Xsub F n) :
    sympForm x y = 0 := by
  have hx2 : x.2 = 0 := hx
  have hy2 : y.2 = 0 := hy
  simp [sympForm, hx2, hy2]

theorem Lsub_isotropic {n d : ℕ} {x y : Symp F n}
    (hx : x ∈ Lsub F n d) (hy : y ∈ Lsub F n d) : sympForm x y = 0 := by
  obtain ⟨hx1, hx2⟩ := hx
  obtain ⟨hy1, hy2⟩ := hy
  refine Finset.sum_eq_zero fun i _ => ?_
  by_cases hi : (i : ℕ) < d
  · rw [hx1 i hi, hy1 i hi]; ring
  · rw [hx2 i (by omega), hy2 i (by omega)]; ring

/-! ### Dimensions -/

/-- Vectors supported on the first `d` coordinates. -/
def headSub (F : Type*) [Field F] (n d : ℕ) : Submodule F (Fin n → F) where
  carrier := {a | ∀ i : Fin n, d ≤ (i : ℕ) → a i = 0}
  add_mem' := by intro a b ha hb i hi; simp [ha i hi, hb i hi]
  zero_mem' := by intro i _; rfl
  smul_mem' := by intro c a ha i hi; simp [ha i hi]

/-- Vectors supported on the last `n - d` coordinates. -/
def tailSub (F : Type*) [Field F] (n d : ℕ) : Submodule F (Fin n → F) where
  carrier := {a | ∀ i : Fin n, (i : ℕ) < d → a i = 0}
  add_mem' := by intro a b ha hb i hi; simp [ha i hi, hb i hi]
  zero_mem' := by intro i _; rfl
  smul_mem' := by intro c a ha i hi; simp [ha i hi]

theorem finrank_headSub (F : Type*) [Field F] (n d : ℕ) :
    Module.finrank F (headSub F n d) = min d n := by
  classical
  have e : (headSub F n d) ≃ₗ[F] ({i : Fin n // (i : ℕ) < d} → F) :=
    { toFun := fun a i => a.1 i.1
      map_add' := by intro a b; rfl
      map_smul' := by intro c a; rfl
      invFun := fun f => ⟨fun i => if h : (i : ℕ) < d then f ⟨i, h⟩ else 0, by
        intro i hi; simp [Nat.not_lt.mpr hi]⟩
      left_inv := by
        intro a
        ext i
        by_cases h : (i : ℕ) < d
        · simp [h]
        · simp [h, a.2 i (by omega)]
      right_inv := by intro f; ext i; simp [i.2] }
  rw [e.finrank_eq, Module.finrank_pi F, card_lt_subtype]

theorem finrank_tailSub (F : Type*) [Field F] (n d : ℕ) :
    Module.finrank F (tailSub F n d) = n - min d n := by
  classical
  have e : (tailSub F n d) ≃ₗ[F] ({i : Fin n // ¬ ((i : ℕ) < d)} → F) :=
    { toFun := fun a i => a.1 i.1
      map_add' := by intro a b; rfl
      map_smul' := by intro c a; rfl
      invFun := fun f => ⟨fun i => if h : (i : ℕ) < d then 0 else f ⟨i, h⟩, by
        intro i hi; simp [hi]⟩
      left_inv := by
        intro a
        ext i
        by_cases h : (i : ℕ) < d
        · simp [h, a.2 i h]
        · simp [h]
      right_inv := by intro f; ext i; simp [i.2] }
  rw [e.finrank_eq, Module.finrank_pi F, Fintype.card_subtype_compl, card_lt_subtype]
  simp

/-! ### The three dimension computations -/

theorem finrank_symp (F : Type*) [Field F] (n : ℕ) : Module.finrank F (Symp F n) = 2 * n := by
  simp [Symp, Module.finrank_prod]; ring

/-- The form is nondegenerate, so an isotropic subspace of dimension `n` is maximal isotropic. -/
theorem sympForm_nondegenerate {n : ℕ} {x : Symp F n} (h : ∀ y, sympForm x y = 0) : x = 0 := by
  classical
  have h1 : ∀ i, x.1 i = 0 := by
    intro i
    have := h (0, Pi.single i 1)
    simpa [sympForm, Pi.single_apply, Finset.sum_ite_eq'] using this
  have h2 : ∀ i, x.2 i = 0 := by
    intro i
    have := h (Pi.single i 1, 0)
    simp only [sympForm, Pi.single_apply] at this
    simpa [Finset.sum_ite_eq', neg_eq_zero] using this
  exact Prod.ext (funext h1) (funext h2)

theorem finrank_Xsub (F : Type*) [Field F] (n : ℕ) :
    Module.finrank F (Xsub F n) = n := by
  have e : (Xsub F n) ≃ₗ[F] (Fin n → F) :=
    { toFun := fun x => x.1.1
      map_add' := by intro a b; rfl
      map_smul' := by intro c a; rfl
      invFun := fun a => ⟨(a, 0), rfl⟩
      left_inv := by
        rintro ⟨⟨a, b⟩, hb⟩
        have : b = 0 := hb
        simp [this]
      right_inv := by intro a; rfl }
  rw [e.finrank_eq, Module.finrank_pi F]
  simp

theorem finrank_Lsub (F : Type*) [Field F] (n d : ℕ) :
    Module.finrank F (Lsub F n d) = n := by
  have e : (Lsub F n d) ≃ₗ[F] (headSub F n d × tailSub F n d) :=
    { toFun := fun x => (⟨x.1.1, x.2.2⟩, ⟨x.1.2, x.2.1⟩)
      map_add' := by intro a b; rfl
      map_smul' := by intro c a; rfl
      invFun := fun p => ⟨(p.1.1, p.2.1), p.2.2, p.1.2⟩
      left_inv := by rintro ⟨⟨a, b⟩, h⟩; rfl
      right_inv := by rintro ⟨⟨a, ha⟩, ⟨b, hb⟩⟩; rfl }
  rw [e.finrank_eq, Module.finrank_prod, finrank_headSub, finrank_tailSub]
  omega

/-- The intersection has dimension exactly `min d n`. -/
theorem finrank_inf (F : Type*) [Field F] (n d : ℕ) :
    Module.finrank F ((Xsub F n) ⊓ (Lsub F n d) : Submodule F (Symp F n)) = min d n := by
  have e : ((Xsub F n) ⊓ (Lsub F n d) : Submodule F (Symp F n)) ≃ₗ[F] headSub F n d :=
    { toFun := fun x => ⟨x.1.1, x.2.2.2⟩
      map_add' := by intro a b; rfl
      map_smul' := by intro c a; rfl
      invFun := fun a => ⟨(a.1, 0), rfl, by
        refine ⟨fun i _ => rfl, fun i hi => a.2 i hi⟩⟩
      left_inv := by
        rintro ⟨⟨a, b⟩, hX, hL⟩
        have hb : b = 0 := hX
        simp [hb]
      right_inv := by rintro ⟨a, ha⟩; rfl }
  rw [e.finrank_eq, finrank_headSub]

/-- **Sharpness of the duality bound.**  In a `2n`-dimensional symplectic space, for every
`d ≤ n` there are two isotropic subspaces of dimension `n` (hence maximal isotropic) whose
intersection has dimension exactly `d`.

Therefore "`X` and `L` are maximal isotropic" — which is *all* that Poitou–Tate global duality
asserts about `(H¹(ℚ, E[n]), ∏_v L_v)` — constrains `dim (X ∩ L)` by nothing beyond
`0 ≤ dim (X ∩ L) ≤ n = ½ dim V`, and that upper bound grows with the level and with the set of
ramified places.  No quantitative bound on `Ш[n]` can be extracted from duality alone.

*Scope.*  This is abstract linear algebra in one symplectic space; `X ∩ L` is the image of
`Sel_n(E)` in the restricted product, not `Sel_n(E)` itself, and the localisation kernel is not
addressed here.  The symmetric — i.e. arithmetically correct — version of the statement is
`SeedBSD.Symmetric.duality_bound_is_sharp_symmetric`. -/
theorem duality_bound_is_sharp (F : Type*) [Field F] (n d : ℕ) (hd : d ≤ n) :
    Module.finrank F (Symp F n) = 2 * n ∧
    (∀ x : Symp F n, (∀ y, sympForm x y = 0) → x = 0) ∧
    (∀ x y, x ∈ Xsub F n → y ∈ Xsub F n → sympForm x y = 0) ∧
    (∀ x y, x ∈ Lsub F n d → y ∈ Lsub F n d → sympForm x y = 0) ∧
    Module.finrank F (Xsub F n) = n ∧
    Module.finrank F (Lsub F n d) = n ∧
    Module.finrank F ((Xsub F n) ⊓ (Lsub F n d) : Submodule F (Symp F n)) = d := by
  refine ⟨finrank_symp F n, fun _ h => sympForm_nondegenerate h,
    fun x y hx hy => Xsub_isotropic hx hy, fun x y hx hy => Lsub_isotropic hx hy,
    finrank_Xsub F n, finrank_Lsub F n d, ?_⟩
  rw [finrank_inf]
  omega

end SeedBSD
