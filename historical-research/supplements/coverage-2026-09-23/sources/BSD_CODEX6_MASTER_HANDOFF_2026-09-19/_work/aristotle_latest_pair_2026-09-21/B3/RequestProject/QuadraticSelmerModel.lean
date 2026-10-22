import Mathlib

/-!
# The intersection countermodel in the *quadratic* (symmetric) setting

This file replaces the symplectic countermodel of `SelmerDualityCountermodel.lean` by the
version appropriate to the arithmetic situation, and states carefully what it does and does
not show.

## Why symmetric rather than alternating

For an elliptic curve `E/Q` and an **odd** prime `p`, the local pairing on
`H^1(Q_v, E[p])` induced by the Weil pairing together with the cup product is
**symmetric**, not alternating: the sign coming from the degree-one cup product cancels the
sign of the alternating Weil pairing.  Sums of local invariants of cup products therefore
make `⨁_v H^1(Q_v, E[p])` a *quadratic* space, and the local conditions and the image of the
global classes are maximal isotropic for that quadratic structure (Poonen–Rains, §4.1).

The countermodel below is therefore carried out for the split quadratic form
`Q(v) = ∑_i x_i y_i` on `F^{2N}` (`N` places, each contributing a hyperbolic plane), with
isotropy meaning vanishing of `Q`, which in odd characteristic is the correct maximal
isotropic condition.

## What is proved

* `QuadSelmer.exists_maximal_isotropic_pair_inter` : for every `k ≤ N` there is a pair of
  `N`-dimensional totally isotropic subspaces `G, L` of the `2N`-dimensional split quadratic
  space with `finrank (G ⊓ L) = k`, where `L` is the *fixed* product of local conditions
  (one isotropic line per place).
* `QuadSelmer.exists_config_with_known_plane` : the same, with a fixed `2`-dimensional
  subspace (modelling the image of a rank-`2` Mordell–Weil group) contained in `G ⊓ L`.
* `QuadSelmer.finrank_inter_le` : conversely, in a fixed ambient dimension `2N` the
  intersection of two totally isotropic subspaces of dimension `N` always has dimension
  `≤ N`.

## Scope (deliberately narrow)

The pair of statements says exactly this: *within a fixed ambient dimension the axioms
"nondegenerate symmetric pairing, two maximal isotropic subspaces" give the bound `N` and
nothing better; the intersection is unbounded only because `N` is allowed to grow.*

It does **not** show that no upper bound for a Selmer group exists, and it does not exclude
arguments that supply further input: a bound on the number of participating places, an
annihilator or orthogonality statement about auxiliary classes, control on the kernel of
localization, or any independently proved estimate.  In particular `finrank_inter_le`
already *is* an upper bound in fixed ambient dimension.
-/

namespace QuadSelmer

open Module

variable {F : Type*} [Field F]

/-- The ambient space: `N` places, each contributing a hyperbolic plane. -/
abbrev LocalSum (F : Type*) (N : ℕ) := Fin N → F × F

/-- The split quadratic form `Q(v) = ∑_i x_i y_i`, the model of the sum of the local
invariants of the (symmetric, for odd `p`) local cup-product pairing. -/
def Q {N : ℕ} (v : LocalSum F N) : F := ∑ i, (v i).1 * (v i).2

/-- The associated symmetric bilinear form `B(v,w) = Q(v+w) - Q(v) - Q(w)`. -/
def B {N : ℕ} (v w : LocalSum F N) : F := ∑ i, ((v i).1 * (w i).2 + (v i).2 * (w i).1)

lemma B_symm {N : ℕ} (v w : LocalSum F N) : B v w = B w v := by
  refine Finset.sum_congr rfl fun i _ => by ring

lemma B_eq {N : ℕ} (v w : LocalSum F N) : B v w = Q (v + w) - Q v - Q w := by
  simp only [Q, B, Pi.add_apply, Prod.fst_add, Prod.snd_add, ← Finset.sum_sub_distrib]
  refine Finset.sum_congr rfl fun i _ => by ring

/-- The symmetric form is nondegenerate. -/
lemma B_nondegenerate {N : ℕ} {v : LocalSum F N} (h : ∀ w, B v w = 0) : v = 0 := by
  funext i
  have h1 : (v i).1 = 0 := by
    have := h (fun j => if j = i then (0, 1) else 0)
    simpa [B, apply_ite Prod.fst, apply_ite Prod.snd, Finset.sum_ite_eq'] using this
  have h2 : (v i).2 = 0 := by
    have := h (fun j => if j = i then (1, 0) else 0)
    simpa [B, apply_ite Prod.fst, apply_ite Prod.snd, Finset.sum_ite_eq'] using this
  exact Prod.ext h1 h2

/-- A subspace is totally isotropic when the quadratic form vanishes on it. -/
def Isotropic {N : ℕ} (S : Submodule F (LocalSum F N)) : Prop := ∀ v ∈ S, Q v = 0

/-- On a totally isotropic subspace the bilinear form vanishes as well. -/
lemma B_eq_zero_of_isotropic {N : ℕ} {S : Submodule F (LocalSum F N)} (hS : Isotropic S)
    {v w : LocalSum F N} (hv : v ∈ S) (hw : w ∈ S) : B v w = 0 := by
  rw [B_eq, hS _ (S.add_mem hv hw), hS _ hv, hS _ hw]; ring

/-- The product of the local conditions: at each place the isotropic line of "first
coordinates". -/
def Lcond (F : Type*) [Field F] (N : ℕ) : Submodule F (LocalSum F N) where
  carrier := {v | ∀ i, (v i).2 = 0}
  add_mem' := by intro a b ha hb i; simp [ha i, hb i]
  zero_mem' := by intro i; simp
  smul_mem' := by intro c a ha i; simp [ha i]

/-- The "global" maximal isotropic subspace: the first coordinate at the places `i < k`,
the second coordinate at the remaining places. -/
def Gglob (F : Type*) [Field F] (N k : ℕ) : Submodule F (LocalSum F N) where
  carrier := {v | (∀ i : Fin N, i.val < k → (v i).2 = 0) ∧
                  (∀ i : Fin N, ¬ i.val < k → (v i).1 = 0)}
  add_mem' := by
    rintro a b ⟨ha1, ha2⟩ ⟨hb1, hb2⟩
    exact ⟨fun i hi => by simp [ha1 i hi, hb1 i hi], fun i hi => by simp [ha2 i hi, hb2 i hi]⟩
  zero_mem' := ⟨fun i _ => rfl, fun i _ => rfl⟩
  smul_mem' := by
    rintro c a ⟨ha1, ha2⟩
    exact ⟨fun i hi => by simp [ha1 i hi], fun i hi => by simp [ha2 i hi]⟩

lemma isotropic_Lcond {N : ℕ} : Isotropic (Lcond F N) := by
  intro v hv
  have hv' : ∀ i, (v i).2 = 0 := hv
  simp [Q, hv']

lemma isotropic_Gglob {N k : ℕ} : Isotropic (Gglob F N k) := by
  rintro v ⟨h1, h2⟩
  refine Finset.sum_eq_zero fun i _ => ?_
  by_cases h : i.val < k
  · simp [h1 i h]
  · simp [h2 i h]

/-- Coordinates for `Lcond`. -/
def lIso (F : Type*) [Field F] (N : ℕ) : (Fin N → F) →ₗ[F] LocalSum F N where
  toFun x := fun i => (x i, 0)
  map_add' := by intro x y; funext i; simp
  map_smul' := by intro c x; funext i; simp

/-- Coordinates for `Gglob`. -/
def gIso (F : Type*) [Field F] (N k : ℕ) : (Fin N → F) →ₗ[F] LocalSum F N where
  toFun x := fun i => if i.val < k then (x i, 0) else (0, x i)
  map_add' := by intro x y; funext i; by_cases h : i.val < k <;> simp [h]
  map_smul' := by intro c x; funext i; by_cases h : i.val < k <;> simp [h]

/-- Coordinates for the intersection. -/
def kIso (F : Type*) [Field F] (N k : ℕ) : (Fin k → F) →ₗ[F] LocalSum F N where
  toFun y := fun i => (if h : i.val < k then y ⟨i.val, h⟩ else 0, 0)
  map_add' := by intro x y; funext i; by_cases h : i.val < k <;> simp [h]
  map_smul' := by intro c x; funext i; by_cases h : i.val < k <;> simp [h]

lemma range_lIso {N : ℕ} : LinearMap.range (lIso F N) = Lcond F N := by
  ext v
  constructor
  · rintro ⟨x, rfl⟩ i; rfl
  · intro hv
    exact ⟨fun i => (v i).1, funext fun i => Prod.ext rfl (hv i).symm⟩

lemma range_gIso {N k : ℕ} : LinearMap.range (gIso F N k) = Gglob F N k := by
  ext v
  constructor
  · rintro ⟨x, rfl⟩
    refine ⟨fun i hi => by simp [gIso, hi], fun i hi => by simp [gIso, hi]⟩
  · rintro ⟨h1, h2⟩
    refine ⟨fun i => if i.val < k then (v i).1 else (v i).2, funext fun i => ?_⟩
    by_cases h : i.val < k
    · simp only [gIso, LinearMap.coe_mk, AddHom.coe_mk, h, if_pos]
      exact Prod.ext rfl (h1 i h).symm
    · simp only [gIso, LinearMap.coe_mk, AddHom.coe_mk, h, if_neg, not_false_iff]
      exact Prod.ext (h2 i h).symm rfl

lemma injective_lIso {N : ℕ} : Function.Injective (lIso F N) := by
  intro x y h
  funext i
  exact congrArg Prod.fst (congrFun h i)

lemma injective_gIso {N k : ℕ} : Function.Injective (gIso F N k) := by
  intro x y h
  funext i
  have := congrFun h i
  by_cases hi : i.val < k
  · simpa [gIso, hi] using congrArg Prod.fst this
  · simpa [gIso, hi] using congrArg Prod.snd this

lemma injective_kIso {N k : ℕ} (hk : k ≤ N) : Function.Injective (kIso F N k) := by
  intro x y h
  funext j
  have hj : (j : ℕ) < N := lt_of_lt_of_le j.isLt hk
  have := congrFun h ⟨j.val, hj⟩
  have h2 : (j : ℕ) < k := j.isLt
  simp only [kIso, LinearMap.coe_mk, AddHom.coe_mk, h2, dif_pos] at this
  simpa using congrArg Prod.fst this

lemma finrank_Lcond {N : ℕ} : finrank F (Lcond F N) = N := by
  rw [← range_lIso (F := F) (N := N),
    LinearMap.finrank_range_of_inj (injective_lIso (F := F) (N := N))]
  simp

lemma finrank_Gglob {N k : ℕ} : finrank F (Gglob F N k) = N := by
  rw [← range_gIso (F := F) (N := N) (k := k),
    LinearMap.finrank_range_of_inj (injective_gIso (F := F) (N := N) (k := k))]
  simp

lemma inter_eq_range {N k : ℕ} (hk : k ≤ N) :
    Gglob F N k ⊓ Lcond F N = LinearMap.range (kIso F N k) := by
  ext v
  constructor
  · rintro ⟨⟨-, hg2⟩, hl⟩
    have hl' : ∀ i, (v i).2 = 0 := hl
    refine ⟨fun j => (v ⟨j.val, lt_of_lt_of_le j.isLt hk⟩).1, funext fun i => ?_⟩
    by_cases h : i.val < k
    · simp only [kIso, LinearMap.coe_mk, AddHom.coe_mk, h, dif_pos]
      exact Prod.ext (by simp) (hl' i).symm
    · simp only [kIso, LinearMap.coe_mk, AddHom.coe_mk, h, dif_neg, not_false_iff]
      exact Prod.ext (hg2 i h).symm (hl' i).symm
  · rintro ⟨y, rfl⟩
    refine ⟨⟨fun i _ => by by_cases h : i.val < k <;> simp [kIso, h], fun i hi => by
      simp [kIso, hi]⟩, fun i => by by_cases h : i.val < k <;> simp [kIso, h]⟩

lemma finrank_inter {N k : ℕ} (hk : k ≤ N) :
    finrank F (Gglob F N k ⊓ Lcond F N : Submodule F (LocalSum F N)) = k := by
  rw [inter_eq_range hk, LinearMap.finrank_range_of_inj (injective_kIso (F := F) hk)]
  simp

/-- **Every intersection dimension `k ≤ N` occurs**, for a pair of `N`-dimensional totally
isotropic subspaces of the split quadratic space of dimension `2N`, with `L` the fixed
product of local conditions.

Read arithmetically: symmetry and nondegeneracy of the global pairing, maximal isotropy of
the local conditions and of the image of the global classes, and the number of places, taken
*by themselves*, pin the intersection down no further than the trivial bound `N`. -/
theorem exists_maximal_isotropic_pair_inter (F : Type*) [Field F] (N k : ℕ) (hk : k ≤ N) :
    ∃ G L : Submodule F (LocalSum F N),
      Isotropic G ∧ Isotropic L ∧
      finrank F G = N ∧ finrank F L = N ∧
      finrank F (G ⊓ L : Submodule F (LocalSum F N)) = k ∧
      L = Lcond F N :=
  ⟨Gglob F N k, Lcond F N, isotropic_Gglob, isotropic_Lcond,
    finrank_Gglob, finrank_Lcond, finrank_inter hk, rfl⟩

/-- **The trivial bound really is a bound.**  In fixed ambient dimension `2N`, the
intersection of two totally isotropic subspaces of dimension `N` has dimension at most `N`.
(Together with the previous theorem: the axioms give exactly `N` and no more.) -/
theorem finrank_inter_le {N : ℕ} (G L : Submodule F (LocalSum F N)) (hG : finrank F G = N) :
    finrank F (G ⊓ L : Submodule F (LocalSum F N)) ≤ N := by
  have := Submodule.finrank_mono (inf_le_left : G ⊓ L ≤ G)
  omega

lemma kIso_two_le {N k : ℕ} (h2 : 2 ≤ k) :
    LinearMap.range (kIso F N 2) ≤ Gglob F N k ⊓ Lcond F N := by
  rintro v ⟨y, rfl⟩
  refine ⟨⟨fun i _ => by by_cases h : i.val < 2 <;> simp [kIso, h], fun i hi => ?_⟩,
    fun i => by by_cases h : i.val < 2 <;> simp [kIso, h]⟩
  have h : ¬ i.val < 2 := fun hlt => hi (lt_of_lt_of_le hlt h2)
  simp [kIso, h]

/-- **A fixed `2`-plane inside the intersection changes nothing.**  The configuration can be
chosen so that `G ⊓ L` contains a fixed `2`-dimensional subspace — the shape of the image of
a rank-`2` Mordell–Weil group — while `finrank (G ⊓ L)` is an arbitrary `k` with
`2 ≤ k ≤ N`.

Caveat, to be read with `RequestProject.LocalizationKernel`: in the arithmetic situation the
Selmer group maps to such an intersection with a kernel, so the Mordell–Weil plane need not
embed into the finite-place intersection at all. -/
theorem exists_config_with_known_plane (F : Type*) [Field F] (N k : ℕ) (hk : k ≤ N)
    (h2 : 2 ≤ k) :
    ∃ (G L M : Submodule F (LocalSum F N)),
      Isotropic G ∧ Isotropic L ∧ L = Lcond F N ∧
      finrank F G = N ∧ finrank F L = N ∧
      M ≤ G ⊓ L ∧ finrank F M = 2 ∧
      finrank F (G ⊓ L : Submodule F (LocalSum F N)) = k := by
  refine ⟨Gglob F N k, Lcond F N, LinearMap.range (kIso F N 2),
    isotropic_Gglob, isotropic_Lcond, rfl, finrank_Gglob, finrank_Lcond,
    kIso_two_le h2, ?_, finrank_inter hk⟩
  rw [LinearMap.finrank_range_of_inj (injective_kIso (F := F) (N := N) (k := 2) (by omega))]
  simp

/-- **Unboundedness comes only from growing the ambient dimension.**  For every bound `B`
there is a configuration, in ambient dimension `2(B+1)`, whose intersection has dimension
exceeding `B`. -/
theorem inter_unbounded (F : Type*) [Field F] (B : ℕ) :
    ∃ (N : ℕ) (G L : Submodule F (LocalSum F N)),
      Isotropic G ∧ Isotropic L ∧
      finrank F G = N ∧ finrank F L = N ∧
      B < finrank F (G ⊓ L : Submodule F (LocalSum F N)) := by
  obtain ⟨G, L, hG, hL, hgr, hlr, hint, -⟩ :=
    exists_maximal_isotropic_pair_inter F (B + 1) (B + 1) le_rfl
  exact ⟨B + 1, G, L, hG, hL, hgr, hlr, by omega⟩

end QuadSelmer
