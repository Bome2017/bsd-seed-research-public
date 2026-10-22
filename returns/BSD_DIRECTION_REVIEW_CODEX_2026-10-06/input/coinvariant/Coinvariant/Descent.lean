import Mathlib

/-!
# Equivariant maps through coinvariants of a normal subgroup

Abstract algebraic core of the identification
`Hom_Γ(A, V) = Hom_{Γ/P}(A_P, V)` when the normal subgroup `P` acts trivially on `V`,
together with the linear-algebra step used to compute the cokernel of the norm pullback.
-/

namespace CoinvariantDescent

variable {k Γ A V : Type*} [CommRing k] [Group Γ]
  [AddCommGroup A] [Module k A] [AddCommGroup V] [Module k V]

/-- The space of `G`-equivariant `k`-linear maps between two representations. -/
def equivHom {G : Type*} [Group G] {M N : Type*} [AddCommGroup M] [Module k M]
    [AddCommGroup N] [Module k N] (ρ : Representation k G M) (τ : Representation k G N) :
    Submodule k (M →ₗ[k] N) where
  carrier := {f | ∀ g, f ∘ₗ ρ g = τ g ∘ₗ f}
  add_mem' {f f'} hf hf' g := by
    simp only [Set.mem_setOf_eq] at *
    rw [LinearMap.add_comp, LinearMap.comp_add, hf, hf']
  zero_mem' g := by simp
  smul_mem' c f hf g := by
    simp only [Set.mem_setOf_eq] at *
    rw [LinearMap.smul_comp, LinearMap.comp_smul, hf]

variable (ρ : Representation k Γ A) (τ : Representation k Γ V) (P : Subgroup Γ) [P.Normal]

/-- The augmentation submodule `I_P A`, spanned by `σ a - a` with `σ ∈ P`;
`A_P = A ⧸ I_P A` is the module of `P`-coinvariants. -/
def augP : Submodule k A :=
  Submodule.span k {x | ∃ σ ∈ P, ∃ a, x = ρ σ a - a}

lemma augP_le_comap (g : Γ) : augP ρ P ≤ (augP ρ P).comap (ρ g) := by
  rw [augP, Submodule.span_le]
  rintro _ ⟨σ, hσ, a, rfl⟩
  simp only [SetLike.mem_coe, Submodule.mem_comap, map_sub]
  apply Submodule.subset_span
  refine ⟨g * σ * g⁻¹, Subgroup.Normal.conj_mem inferInstance σ hσ g, ρ g a, ?_⟩
  rw [← Module.End.mul_apply, ← map_mul, ← Module.End.mul_apply, ← map_mul]
  simp [mul_assoc]

/-- The induced action of `Γ` on the coinvariants `A_P`. -/
noncomputable def coinvRep : Representation k Γ (A ⧸ augP ρ P) where
  toFun g := (augP ρ P).mapQ (augP ρ P) (ρ g) (augP_le_comap ρ P g)
  map_one' := by
    ext x
    simp
  map_mul' g h := by
    ext x
    simp

@[simp] lemma coinvRep_mk (g : Γ) (a : A) :
    coinvRep ρ P g (Submodule.Quotient.mk a) = Submodule.Quotient.mk (ρ g a) := rfl

/-- `P` acts trivially on its own coinvariants, so the action factors through `Γ/P`. -/
lemma coinvRep_trivial (σ : Γ) (hσ : σ ∈ P) : coinvRep ρ P σ = 1 := by
  ext a
  simp only [LinearMap.coe_comp, Function.comp_apply, Submodule.mkQ_apply, coinvRep_mk,
    Module.End.one_apply]
  rw [Submodule.Quotient.eq]
  exact Submodule.subset_span ⟨σ, hσ, a, rfl⟩

omit [P.Normal] in
/-- Any `Γ`-equivariant map to a module on which `P` acts trivially kills `I_P A`. -/
lemma augP_le_ker (hτ : ∀ σ ∈ P, τ σ = 1) (f : A →ₗ[k] V) (hf : f ∈ equivHom ρ τ) :
    augP ρ P ≤ LinearMap.ker f := by
  rw [augP, Submodule.span_le]
  rintro _ ⟨σ, hσ, a, rfl⟩
  have h := congrArg (fun F => F a) (hf σ)
  simp only [LinearMap.coe_comp, Function.comp_apply, hτ σ hσ, Module.End.one_apply] at h
  simp [h]

/-- **Coinvariant descent.** If `P ⊴ Γ` acts trivially on `V`, then restriction along
`A → A_P` is a linear isomorphism `Hom_Γ(A_P, V) ≃ Hom_Γ(A, V)`. -/
noncomputable def coinvEquiv (hτ : ∀ σ ∈ P, τ σ = 1) :
    equivHom (coinvRep ρ P) τ ≃ₗ[k] equivHom ρ τ where
  toFun g := ⟨g.1 ∘ₗ (augP ρ P).mkQ, fun h => by
    ext a
    have := congrArg (fun F => F (Submodule.Quotient.mk a)) (g.2 h)
    simpa using this⟩
  invFun f := ⟨(augP ρ P).liftQ f.1 (augP_le_ker ρ τ P hτ f.1 f.2), fun h => by
    ext a
    have := congrArg (fun F => F a) (f.2 h)
    simpa using this⟩
  map_add' _ _ := rfl
  map_smul' _ _ := rfl
  left_inv g := by
    ext a
    rfl
  right_inv f := by
    ext a
    rfl

/-- The action of `Γ/P = G₀` on the coinvariants `A_P`. -/
noncomputable def coinvRepQuot : Representation k (Γ ⧸ P) (A ⧸ augP ρ P) :=
  QuotientGroup.lift P (coinvRep ρ P) (fun σ hσ => by
    rw [MonoidHom.mem_ker]; exact coinvRep_trivial ρ P σ hσ)

/-- The action of `Γ/P = G₀` on `V`, when `P` acts trivially. -/
noncomputable def repQuot (hτ : ∀ σ ∈ P, τ σ = 1) : Representation k (Γ ⧸ P) V :=
  QuotientGroup.lift P τ (fun σ hσ => by rw [MonoidHom.mem_ker]; exact hτ σ hσ)

/-- `Γ`-equivariance and `Γ/P`-equivariance agree on maps out of the coinvariants. -/
lemma equivHom_quot_eq (hτ : ∀ σ ∈ P, τ σ = 1) :
    equivHom (coinvRepQuot ρ P) (repQuot τ P hτ) = equivHom (coinvRep ρ P) τ := by
  ext f
  constructor
  · intro hf g
    exact hf (QuotientGroup.mk g)
  · intro hf g
    induction g using QuotientGroup.induction_on with
    | H g => exact hf g

/-- **Main identification.** `B = Hom_Γ(A, V) ≅ Hom_{Γ/P}(A_P, V)`, canonically, via
composition with the projection `A → A_P`. -/
noncomputable def homEquivCoinvQuot (hτ : ∀ σ ∈ P, τ σ = 1) :
    equivHom (coinvRepQuot ρ P) (repQuot τ P hτ) ≃ₗ[k] equivHom ρ τ :=
  (LinearEquiv.ofEq _ _ (equivHom_quot_eq ρ τ P hτ)).trans (coinvEquiv ρ τ P hτ)

lemma homEquivCoinvQuot_apply (hτ : ∀ σ ∈ P, τ σ = 1)
    (g : equivHom (coinvRepQuot ρ P) (repQuot τ P hτ)) :
    (homEquivCoinvQuot ρ τ P hτ g : A →ₗ[k] V) = g.1 ∘ₗ (augP ρ P).mkQ := rfl

/-! ### The cokernel of the strict-at-`p` part

Linear-algebra step: for a space `S` with a subspace `W` and a localization map `loc`,
the image of `ker loc` in `S/W` has kernel `ker loc ⊓ W` and cokernel `loc(S)/loc(W)`. -/

section Strict

variable {K S F : Type*} [Field K] [AddCommGroup S] [Module K S] [AddCommGroup F] [Module K F]

/-- The kernel of `ker loc → S/W` is `ker loc ⊓ W`. -/
lemma strict_to_quot_ker (W : Submodule K S) (loc : S →ₗ[K] F) :
    LinearMap.ker (W.mkQ ∘ₗ (LinearMap.ker loc).subtype) =
      (W.comap (LinearMap.ker loc).subtype) := by
  ext x
  simp

/-- The cokernel of `ker loc → S/W` is `S/(ker loc ⊔ W) ≅ loc(S)/loc(W)`. -/
noncomputable def strict_coker_equiv (W : Submodule K S) (loc : S →ₗ[K] F) :
    (S ⧸ (LinearMap.ker loc ⊔ W)) ≃ₗ[K] (LinearMap.range loc ⧸ (W.map loc).comap
      (LinearMap.range loc).subtype) := by
  refine (Submodule.quotEquivOfEq _ _ ?_).trans
    (LinearMap.quotKerEquivOfSurjective
      (((W.map loc).comap (LinearMap.range loc).subtype).mkQ ∘ₗ loc.rangeRestrict) ?_)
  · ext x
    simp only [LinearMap.mem_ker, LinearMap.coe_comp, Function.comp_apply,
      Submodule.mkQ_apply, Submodule.Quotient.mk_eq_zero, Submodule.mem_comap,
      Submodule.coe_subtype, LinearMap.codRestrict_apply, Submodule.mem_map]
    constructor
    · intro hx
      obtain ⟨y, hy, z, hz, rfl⟩ := Submodule.mem_sup.1 hx
      exact ⟨z, hz, by rw [map_add, LinearMap.mem_ker.1 hy, zero_add]⟩
    · rintro ⟨z, hz, hzx⟩
      refine Submodule.mem_sup.2 ⟨x - z, ?_, z, hz, by abel⟩
      rw [LinearMap.mem_ker, map_sub, hzx, sub_self]
  · exact (Submodule.mkQ_surjective _).comp loc.surjective_rangeRestrict

/-- In particular, if `loc(W) = loc(S)`, then `ker loc` surjects onto `S/W`. -/
lemma strict_surj_of_loc_eq (W : Submodule K S) (loc : S →ₗ[K] F)
    (h : W.map loc = LinearMap.range loc) :
    Function.Surjective (W.mkQ ∘ₗ (LinearMap.ker loc).subtype) := by
  intro y
  obtain ⟨x, rfl⟩ := Submodule.mkQ_surjective W y
  have hx : loc x ∈ W.map loc := h ▸ LinearMap.mem_range_self loc x
  obtain ⟨z, hz, hzx⟩ := hx
  refine ⟨⟨x - z, by rw [LinearMap.mem_ker, map_sub, hzx, sub_self]⟩, ?_⟩
  simp only [LinearMap.coe_comp, Function.comp_apply, Submodule.coe_subtype,
    Submodule.mkQ_apply]
  rw [Submodule.Quotient.eq]
  simpa using hz

end Strict

/-! ### Central-sign vanishing

Used for the knot (`Λ²P`) contribution: if an element `z` acts by `+1` on `X` and by `-1`
on `V`, and `2` is invertible, there are no nonzero equivariant maps `X → V`. -/

lemma equivHom_eq_bot_of_sign {G X : Type*} [Group G] [AddCommGroup X] [Module k X]
    (σX : Representation k G X) (σV : Representation k G V) (z : G)
    (hX : σX z = 1) (hV : σV z = -1) (h2 : IsUnit (2 : k)) :
    equivHom σX σV = ⊥ := by
  rw [eq_bot_iff]
  intro f hf
  rw [Submodule.mem_bot]
  ext x
  have h := congrArg (fun F => F x) (hf z)
  simp only [LinearMap.coe_comp, Function.comp_apply, hX, hV, Module.End.one_apply,
    LinearMap.neg_apply] at h
  have h' : (2 : k) • f x = 0 := by
    rw [two_smul]; nth_rewrite 1 [h]; simp
  simpa [h2.smul_eq_zero] using h'

end CoinvariantDescent
