import Mathlib

/-!
# Sharpness of the duality bound for the *symmetric* local pairing

`RequestProject/IsotropicSharpness.lean` proves that two maximal isotropic subspaces of a
`2n`-dimensional **alternating** (symplectic) space can meet in any prescribed dimension `d ≤ n`.
That model is the wrong one for the arithmetic at hand: for odd `n` the local Tate pairing on
`H¹(ℚ_v, E[n])` induced by the Weil pairing and the cup product is **symmetric**, not
alternating (Poonen–Rains, "Random maximal isotropic subspaces and Selmer groups", §4.1): the
Weil pairing is antisymmetric and the cup product on degree-one classes is antisymmetric, and
the two signs cancel.

This file redoes the sharpness statement for a nondegenerate **symmetric** form, so that the
conclusion — that maximal isotropy alone constrains `dim(X ∩ L)` by nothing beyond
`0 ≤ dim(X ∩ L) ≤ ½ dim V` — is established for the pairing that actually occurs.

## Scope and the localisation kernel

What is formalised below is abstract linear algebra in one split symmetric space: two maximal
isotropic subspaces `X`, `L` of a `2n`-dimensional symmetric space, and the exact dimension of
`X ⊓ L`.  It is deliberately *not* an identification of `Sel_n(E)` with such an intersection, and
earlier prose in this development that read `dim Sel_n(E) = dim(X ∩ L)` was loose.  Two gaps
separate the model from the arithmetic:

* `Sel_n(E)` is by definition the **kernel** of the localisation map
  `H¹(ℚ, E[n]) → ∏_v H¹(ℚ_v, E[n]) / im(E(ℚ_v)/n)`.  Passing to the restricted product replaces
  it by the intersection of the image of global cohomology with the product of the local
  conditions; that intersection is a quotient of `Sel_n(E)` by the classes that are locally
  trivial everywhere, i.e. by `Ш¹(ℚ, E[n])`, the kernel of localisation.  Nothing in this file
  bounds or even mentions that kernel.
* The local conditions `im(E(ℚ_v)/n)` are maximal isotropic, and the image of the global
  cohomology is isotropic by global reciprocity; but a Poitou–Tate set-up realising both as
  maximal isotropic subspaces of a single nondegenerate space requires the restricted-product
  formalism, which is not developed here.

So the correct reading of the results below is one-directional: they show that *isotropy alone*
supplies no bound better than `½ dim V`, in a space of the right symmetry type.  They supply no
upper bound for `dim Sel_n(E)`, and they do not remove the localisation kernel.

The model is the split (hyperbolic) symmetric space `V = (Fin n → F) × (Fin n → F)` with

    ω x y = ∑ i, (x.1 i * y.2 i + x.2 i * y.1 i),

`X = (Fin n → F) × 0`, and `L d = {x | x.2 i = 0 for i < d, x.1 i = 0 for i ≥ d}`.  Both are
totally isotropic of dimension `n`, and `dim (X ⊓ L d) = d` exactly.  When `char F ≠ 2` the form
is genuinely non-alternating (`symForm_self_ne_zero`), which is the point of redoing the
computation.
-/

namespace SeedBSD.Symmetric

open Finset

variable {F : Type*} [Field F]

/-- The ambient `2n`-dimensional space carrying the split symmetric form. -/
abbrev Hyp (F : Type*) (n : ℕ) := (Fin n → F) × (Fin n → F)

/-- The split (hyperbolic) **symmetric** bilinear form. -/
def symForm {n : ℕ} (x y : Hyp F n) : F := ∑ i, (x.1 i * y.2 i + x.2 i * y.1 i)

theorem symForm_symm {n : ℕ} (x y : Hyp F n) : symForm x y = symForm y x :=
  Finset.sum_congr rfl fun i _ => by ring

/-- The form is **not** alternating when `char F ≠ 2` and `n ≥ 1`: on the vector `(e₀, e₀)` it
takes the value `2 ≠ 0`.  This is exactly the feature that distinguishes it from the symplectic
model, and it is the shape of the odd-residue-characteristic local Tate pairing. -/
theorem symForm_self_ne_zero {n : ℕ} (hn : 0 < n) (h2 : (2 : F) ≠ 0) :
    ∃ x : Hyp F n, symForm x x ≠ 0 := by
  classical
  refine ⟨(Pi.single ⟨0, hn⟩ 1, Pi.single ⟨0, hn⟩ 1), ?_⟩
  have : symForm ((Pi.single (⟨0, hn⟩ : Fin n) (1 : F)), Pi.single ⟨0, hn⟩ (1 : F))
      (Pi.single ⟨0, hn⟩ 1, Pi.single ⟨0, hn⟩ 1) = 2 := by
    simp only [symForm, Pi.single_apply]
    rw [Finset.sum_eq_single (⟨0, hn⟩ : Fin n)] <;> simp +contextual
    norm_num
  rw [this]
  exact h2

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

/-- `X = (Fin n → F) × 0`, the "global" maximal isotropic in the model. -/
def Xsub (F : Type*) [Field F] (n : ℕ) : Submodule F (Hyp F n) where
  carrier := {x | x.2 = 0}
  add_mem' := by intro a b ha hb; simp_all [Set.mem_setOf_eq]
  zero_mem' := by simp
  smul_mem' := by intro c a ha; simp_all [Set.mem_setOf_eq]

/-- `L d`, a second maximal isotropic subspace, meeting `X` in dimension `d`. -/
def Lsub (F : Type*) [Field F] (n d : ℕ) : Submodule F (Hyp F n) where
  carrier := {x | (∀ i : Fin n, (i : ℕ) < d → x.2 i = 0) ∧ (∀ i : Fin n, d ≤ (i : ℕ) → x.1 i = 0)}
  add_mem' := by
    rintro a b ⟨ha1, ha2⟩ ⟨hb1, hb2⟩
    exact ⟨fun i hi => by simp [ha1 i hi, hb1 i hi], fun i hi => by simp [ha2 i hi, hb2 i hi]⟩
  zero_mem' := by constructor <;> intro i _ <;> rfl
  smul_mem' := by
    rintro c a ⟨ha1, ha2⟩
    exact ⟨fun i hi => by simp [ha1 i hi], fun i hi => by simp [ha2 i hi]⟩

theorem Xsub_isotropic {n : ℕ} {x y : Hyp F n} (hx : x ∈ Xsub F n) (hy : y ∈ Xsub F n) :
    symForm x y = 0 := by
  have hx2 : x.2 = 0 := hx
  have hy2 : y.2 = 0 := hy
  simp [symForm, hx2, hy2]

theorem Lsub_isotropic {n d : ℕ} {x y : Hyp F n}
    (hx : x ∈ Lsub F n d) (hy : y ∈ Lsub F n d) : symForm x y = 0 := by
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

/-! ### The dimension computations -/

theorem finrank_hyp (F : Type*) [Field F] (n : ℕ) : Module.finrank F (Hyp F n) = 2 * n := by
  simp [Hyp, Module.finrank_prod]; ring

/-- The symmetric form is nondegenerate, so an isotropic subspace of dimension `n` is maximal
isotropic. -/
theorem symForm_nondegenerate {n : ℕ} {x : Hyp F n} (h : ∀ y, symForm x y = 0) : x = 0 := by
  classical
  have h1 : ∀ i, x.1 i = 0 := by
    intro i
    have := h (0, Pi.single i 1)
    simpa [symForm, Pi.single_apply, Finset.sum_ite_eq'] using this
  have h2 : ∀ i, x.2 i = 0 := by
    intro i
    have := h (Pi.single i 1, 0)
    simpa [symForm, Pi.single_apply, Finset.sum_ite_eq'] using this
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
    Module.finrank F ((Xsub F n) ⊓ (Lsub F n d) : Submodule F (Hyp F n)) = min d n := by
  have e : ((Xsub F n) ⊓ (Lsub F n d) : Submodule F (Hyp F n)) ≃ₗ[F] headSub F n d :=
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

/-- **Sharpness of the duality bound, symmetric case.**  In a `2n`-dimensional space carrying a
nondegenerate *symmetric* bilinear form — the shape of the local Tate pairing on
`H¹(ℚ_v, E[n])` for odd `n` — for every `d ≤ n` there are two totally isotropic subspaces of
dimension `n` (hence maximal isotropic) whose intersection has dimension exactly `d`.

So the correction that the arithmetic pairing is symmetric rather than alternating does not
rescue a duality-only bound: "`X` and `L` are maximal isotropic", which is the entire content of
Poitou–Tate here, constrains the dimension of the intersection of two such subspaces by nothing
beyond `0 ≤ dim(X ∩ L) ≤ n = ½ dim V`, and every value in that range occurs.

*Scope.*  The statement is abstract linear algebra about one split symmetric space.  It is a
no-go for extracting a bound from isotropy alone; it is **not** a statement about `Sel_n(E)`.
See the `Scope and the localisation kernel` section of the file header: `Sel_n(E)` is the kernel
of a global-to-local map, not literally an intersection of two maximal isotropic subspaces, and
nothing here controls the kernel of localisation. -/
theorem duality_bound_is_sharp_symmetric (F : Type*) [Field F] (n d : ℕ) (hd : d ≤ n) :
    Module.finrank F (Hyp F n) = 2 * n ∧
    (∀ x y : Hyp F n, symForm x y = symForm y x) ∧
    (∀ x : Hyp F n, (∀ y, symForm x y = 0) → x = 0) ∧
    (∀ x y, x ∈ Xsub F n → y ∈ Xsub F n → symForm x y = 0) ∧
    (∀ x y, x ∈ Lsub F n d → y ∈ Lsub F n d → symForm x y = 0) ∧
    Module.finrank F (Xsub F n) = n ∧
    Module.finrank F (Lsub F n d) = n ∧
    Module.finrank F ((Xsub F n) ⊓ (Lsub F n d) : Submodule F (Hyp F n)) = d := by
  refine ⟨finrank_hyp F n, fun x y => symForm_symm x y, fun _ h => symForm_nondegenerate h,
    fun x y hx hy => Xsub_isotropic hx hy, fun x y hx hy => Lsub_isotropic hx hy,
    finrank_Xsub F n, finrank_Lsub F n d, ?_⟩
  rw [finrank_inf]
  omega

/-- The same sharpness statement over `𝔽_p` for an odd prime `p`, where the form is genuinely
non-alternating. -/
theorem duality_bound_is_sharp_symmetric_oddPrime (p : ℕ) [Fact p.Prime] (hp : p ≠ 2)
    (n d : ℕ) (hn : 0 < n) (hd : d ≤ n) :
    (∃ x : Hyp (ZMod p) n, symForm x x ≠ 0) ∧
    Module.finrank (ZMod p) ((Xsub (ZMod p) n) ⊓ (Lsub (ZMod p) n d) :
      Submodule (ZMod p) (Hyp (ZMod p) n)) = d := by
  have h2 : (2 : ZMod p) ≠ 0 := by
    have hpp : p.Prime := Fact.out
    have h : ((2 : ℕ) : ZMod p) ≠ 0 := by
      rw [Ne, ZMod.natCast_eq_zero_iff]
      intro hdvd
      exact hp ((Nat.prime_dvd_prime_iff_eq hpp Nat.prime_two).1 hdvd)
    simpa using h
  exact ⟨symForm_self_ne_zero hn h2, (duality_bound_is_sharp_symmetric (ZMod p) n d hd).2.2.2.2.2.2.2⟩

end SeedBSD.Symmetric
