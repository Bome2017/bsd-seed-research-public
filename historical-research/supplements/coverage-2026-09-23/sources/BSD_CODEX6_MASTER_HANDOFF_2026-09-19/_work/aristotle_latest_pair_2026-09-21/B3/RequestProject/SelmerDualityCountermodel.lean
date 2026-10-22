import Mathlib

/-!
# Self-duality degeneracy: the symplectic model (SUPERSEDED COMMENTARY)

**Correction notice.**  The linear algebra in this file is correct, but the arithmetic
interpretation attached to it below is not.  Two errors, identified in the review recorded
in `ARISTOTLE_B_CORRECTIONS.md`:

1. *The pairing is symmetric, not alternating.*  For odd `p` the local pairing on
   `H^1(Q_v, E[p])` induced by the Weil pairing and the cup product is symmetric — the
   degree-one cup-product sign cancels the alternating sign of the Weil pairing — so the
   arithmetic setting is quadratic, not symplectic (Poonen–Rains, §4.1).  The repaired
   quadratic version of the countermodel is `RequestProject/QuadraticSelmerModel.lean`, and
   that file supersedes the arithmetic commentary here.
2. *A finite intersection of local conditions computes the image of Selmer, not Selmer.*
   Localization at a finite set of places has a kernel; see
   `RequestProject/LocalizationKernel.lean`, where the kernel is shown to be nonzero for the
   seed curve at `p = 11`.  So `exists_config_with_known_plane` below should not be read as
   saying anything about how the Mordell–Weil plane sits inside a finite local
   intersection.

In addition, the "unboundedness" statement at the end should be read as: in *fixed* ambient
dimension `2N` the axioms give the bound `N` and nothing sharper (see
`QuadSelmer.finrank_inter_le`); unboundedness comes only from letting `N` grow.  The file is
retained unchanged apart from this notice, for the record; the statements it proves are
elementary linear algebra and remain valid as such.

The original commentary follows.

This file formalizes the abstract linear-algebra countermodel underlying the negative
verdict recorded in `ARISTOTLE_B_REPORT.md`.

## The arithmetic situation being modelled

For an elliptic curve `E/Q` and a prime `p`, the `p`-Selmer group is
`Sel_p(E) = G ⊓ L` computed inside the direct sum of the local cohomology groups
`H^1(Q_v, E[p])`:

* each local group `H^1(Q_v, E[p])` carries the local Tate-duality pairing, and
  `⨁_v H^1(Q_v, E[p])` is a symplectic space (the Weil pairing makes `E[p]` self-dual);
* the group of local conditions `L = ⨁_v im(E(Q_v)/p → H^1(Q_v, E[p]))` is **maximal
  isotropic** (the local Kummer image is its own annihilator);
* the image `G` of the global cohomology is **maximal isotropic** as well: that is exactly
  the global reciprocity law `∑_v inv_v(x ∪ y) = 0` of Poitou–Tate together with the
  Poitou-Tate exact sequence.

Everything a duality / reciprocity / "new bilinear pairing" argument can use about the
Selmer group is contained in that package: a nondegenerate alternating form on a
finite-dimensional space, and two maximal isotropic subspaces whose intersection is the
Selmer group.

## What is proved here

`SelmerDuality.exists_maximal_isotropic_pair_inter` : in the standard symplectic space
of dimension `2N` (modelled as `N` places, each contributing a `2`-dimensional local
symplectic space, with `L` the product of the local conditions), **every** intersection
dimension `k ≤ N` is realised by a pair of maximal isotropic subspaces.

Consequently (`SelmerDuality.inter_unbounded`) the intersection dimension is unbounded as
`N` grows, even after fixing any amount of information of this shape.  So no argument whose
inputs are only

* nondegeneracy and alternation of the global pairing,
* maximal isotropy of the local-condition subspace,
* maximal isotropy of the image of the global classes,
* the number of participating places,

can produce an upper bound for `dim Sel_p(E)`, hence none can produce an upper bound for
`Sha(E/Q)[p]`.

**Scope.**  The statement is about mechanisms whose *only* inputs are the four listed items.
It does not say that no upper bound exists, and it does not forbid a mechanism that supplies
further independently proved input — for instance a surjection onto `Sel_p(E)` from a source
of independently bounded dimension, a map out of `Sel_p(E)` with controlled kernel, an
annihilator theorem, or a lower bound on a dual Selmer group obtained by exhibiting global
classes with prescribed ramification.  Each of those adds a hypothesis this countermodel
does not satisfy.

This is a *structural* obstruction: it is the precise reason the
Greenberg–Wiles / Poitou–Tate formula for a self-dual module is an identity `0 = 0` rather
than an inequality, and it disposes uniformly of the mechanisms whose entire content is a
new pairing or a new global reciprocity identity on the local data.

The countermodel is faithful in a strong sense: `L` below is literally a product of local
conditions, one maximal isotropic line at each place, and only the global subspace `G`
varies.
-/

namespace SelmerDuality

open Module

variable {F : Type*} [Field F]

/-- The ambient space: `N` places, each contributing a two-dimensional local symplectic
space. -/
abbrev LocalSum (F : Type*) (N : ℕ) := Fin N → F × F

/-- The sum of the local Tate pairings. -/
def omega {N : ℕ} (v w : LocalSum F N) : F :=
  ∑ i, ((v i).1 * (w i).2 - (v i).2 * (w i).1)

lemma omega_self {N : ℕ} (v : LocalSum F N) : omega v v = 0 := by
  simp [omega, mul_comm]

lemma omega_skew {N : ℕ} (v w : LocalSum F N) : omega v w = -omega w v := by
  simp only [omega, ← Finset.sum_neg_distrib]
  refine Finset.sum_congr rfl fun i _ => by ring

/-- The pairing is nondegenerate. -/
lemma omega_nondegenerate {N : ℕ} {v : LocalSum F N} (h : ∀ w, omega v w = 0) : v = 0 := by
  funext i
  have h1 : (v i).1 = 0 := by
    have := h (fun j => if j = i then (0, 1) else 0)
    simpa [omega, apply_ite Prod.fst, apply_ite Prod.snd, Finset.sum_ite_eq'] using this
  have h2 : (v i).2 = 0 := by
    have := h (fun j => if j = i then (1, 0) else 0)
    simpa [omega, apply_ite Prod.fst, apply_ite Prod.snd, Finset.sum_ite_eq'] using this
  exact Prod.ext h1 h2

/-- A subspace is isotropic for `omega`. -/
def Isotropic {N : ℕ} (S : Submodule F (LocalSum F N)) : Prop :=
  ∀ v ∈ S, ∀ w ∈ S, omega v w = 0

/-- The product of the local conditions: at each place the line of "first coordinates".
This is a maximal isotropic subspace, and it is a genuine product over the places. -/
def Lcond (F : Type*) [Field F] (N : ℕ) : Submodule F (LocalSum F N) where
  carrier := {v | ∀ i, (v i).2 = 0}
  add_mem' := by intro a b ha hb i; simp [ha i, hb i]
  zero_mem' := by intro i; simp
  smul_mem' := by intro c a ha i; simp [ha i]

/-- The graph of the diagonal symmetric endomorphism with entries `d`; a maximal isotropic
subspace, playing the role of the image of the global cohomology. -/
def Gglob (F : Type*) [Field F] {N : ℕ} (d : Fin N → F) :
    Submodule F (LocalSum F N) where
  carrier := {v | ∀ i, (v i).2 = d i * (v i).1}
  add_mem' := by intro a b ha hb i; simp [ha i, hb i]; ring
  zero_mem' := by intro i; simp
  smul_mem' := by intro c a ha i; simp [ha i]; ring

lemma isotropic_Lcond {N : ℕ} : Isotropic (Lcond F N) := by
  intro v hv w hw
  have hv' : ∀ i, (v i).2 = 0 := hv
  have hw' : ∀ i, (w i).2 = 0 := hw
  simp [omega, hv', hw']

lemma isotropic_Gglob {N : ℕ} (d : Fin N → F) : Isotropic (Gglob F d) := by
  intro v hv w hw
  have hv' : ∀ i, (v i).2 = d i * (v i).1 := hv
  have hw' : ∀ i, (w i).2 = d i * (w i).1 := hw
  simp only [omega, hv', hw']
  refine Finset.sum_eq_zero fun i _ => by ring

/-- Coordinates for `Lcond`. -/
def lIso (F : Type*) [Field F] (N : ℕ) : (Fin N → F) →ₗ[F] LocalSum F N where
  toFun x := fun i => (x i, 0)
  map_add' := by intro x y; funext i; simp
  map_smul' := by intro c x; funext i; simp

/-- Coordinates for `Gglob d`. -/
def gIso (F : Type*) [Field F] {N : ℕ} (d : Fin N → F) :
    (Fin N → F) →ₗ[F] LocalSum F N where
  toFun x := fun i => (x i, d i * x i)
  map_add' := by intro x y; funext i; simp; ring
  map_smul' := by intro c x; funext i; simp [mul_left_comm]

lemma range_lIso {N : ℕ} : LinearMap.range (lIso F N) = Lcond F N := by
  ext v
  constructor
  · rintro ⟨x, rfl⟩ i; rfl
  · intro hv
    refine ⟨fun i => (v i).1, ?_⟩
    funext i
    exact Prod.ext rfl (hv i).symm

lemma range_gIso {N : ℕ} (d : Fin N → F) :
    LinearMap.range (gIso F d) = Gglob F d := by
  ext v
  constructor
  · rintro ⟨x, rfl⟩ i; rfl
  · intro hv
    refine ⟨fun i => (v i).1, ?_⟩
    funext i
    exact Prod.ext rfl (hv i).symm

lemma injective_lIso {N : ℕ} : Function.Injective (lIso F N) := by
  intro x y h
  funext i
  have := congrFun h i
  exact congrArg Prod.fst this

lemma injective_gIso {N : ℕ} (d : Fin N → F) : Function.Injective (gIso F d) := by
  intro x y h
  funext i
  have := congrFun h i
  exact congrArg Prod.fst this

lemma finrank_Lcond {N : ℕ} : finrank F (Lcond F N) = N := by
  rw [← range_lIso (F := F) (N := N),
    LinearMap.finrank_range_of_inj (injective_lIso (F := F) (N := N))]
  simp

lemma finrank_Gglob {N : ℕ} (d : Fin N → F) : finrank F (Gglob F d) = N := by
  rw [← range_gIso (F := F) d, LinearMap.finrank_range_of_inj (injective_gIso (F := F) d)]
  simp

/-- The specific "diagonal" used below: `0` on the first `k` places, `1` afterwards. -/
def dcut (F : Type*) [Field F] (N k : ℕ) : Fin N → F := fun i => if i.val < k then 0 else 1

/-- Coordinates for the intersection. -/
def kIso (F : Type*) [Field F] (N k : ℕ) : (Fin k → F) →ₗ[F] LocalSum F N where
  toFun y := fun i => (if h : i.val < k then y ⟨i.val, h⟩ else 0, 0)
  map_add' := by
    intro x y; funext i; by_cases h : i.val < k <;> simp [h]
  map_smul' := by
    intro c x; funext i; by_cases h : i.val < k <;> simp [h]

lemma injective_kIso {N k : ℕ} (hk : k ≤ N) : Function.Injective (kIso F N k) := by
  intro x y h
  funext j
  have hj : (j : ℕ) < N := lt_of_lt_of_le j.isLt hk
  have := congrFun h ⟨j.val, hj⟩
  have h2 : (j : ℕ) < k := j.isLt
  simp only [kIso, LinearMap.coe_mk, AddHom.coe_mk, h2, dif_pos] at this
  have := congrArg Prod.fst this
  simpa using this

lemma inter_eq_range {N k : ℕ} (hk : k ≤ N) :
    Gglob F (dcut F N k) ⊓ Lcond F N = LinearMap.range (kIso F N k) := by
  ext v
  constructor
  · rintro ⟨hg, hl⟩
    have hg' : ∀ i, (v i).2 = dcut F N k i * (v i).1 := hg
    have hl' : ∀ i, (v i).2 = 0 := hl
    refine ⟨fun j => (v ⟨j.val, lt_of_lt_of_le j.isLt hk⟩).1, ?_⟩
    funext i
    by_cases h : i.val < k
    · simp only [kIso, LinearMap.coe_mk, AddHom.coe_mk, h, dif_pos]
      refine Prod.ext ?_ (hl' i).symm
      simp
    · have hd : dcut F N k i = 1 := by simp [dcut, h]
      have hz : (v i).1 = 0 := by
        have h1 := hg' i
        rw [hd, one_mul, hl' i] at h1
        exact h1.symm
      simp only [kIso, LinearMap.coe_mk, AddHom.coe_mk, h, dif_neg, not_false_iff]
      exact Prod.ext hz.symm (hl' i).symm
  · rintro ⟨y, rfl⟩
    constructor
    · intro i
      by_cases h : i.val < k <;> simp [kIso, dcut, h]
    · intro i
      by_cases h : i.val < k <;> simp [kIso, h]

lemma finrank_inter {N k : ℕ} (hk : k ≤ N) :
    finrank F (Gglob F (dcut F N k) ⊓ Lcond F N : Submodule F (LocalSum F N)) = k := by
  rw [inter_eq_range hk, LinearMap.finrank_range_of_inj (injective_kIso (F := F) hk)]
  simp

/-- **Main countermodel.**  In the standard symplectic space attached to `N` places, with
`L` the fixed product of local conditions (one maximal isotropic line per place), every
value `k ≤ N` occurs as the dimension of `G ⊓ L` for a maximal isotropic `G`.

Read arithmetically: global duality (maximal isotropy of the image of global classes),
local duality (maximal isotropy of the local conditions), nondegeneracy of the pairing and
the number of places together put **no** upper bound on the Selmer group. -/
theorem exists_maximal_isotropic_pair_inter (F : Type*) [Field F] (N k : ℕ) (hk : k ≤ N) :
    ∃ G L : Submodule F (LocalSum F N),
      Isotropic G ∧ Isotropic L ∧
      finrank F G = N ∧ finrank F L = N ∧
      finrank F (G ⊓ L : Submodule F (LocalSum F N)) = k ∧
      L = Lcond F N := by
  refine ⟨Gglob F (dcut F N k), Lcond F N, isotropic_Gglob _, isotropic_Lcond,
    finrank_Gglob _, finrank_Lcond, finrank_inter hk, rfl⟩

lemma kIso_two_le {N k : ℕ} (h2 : 2 ≤ k) :
    LinearMap.range (kIso F N 2) ≤ Gglob F (dcut F N k) ⊓ Lcond F N := by
  rintro v ⟨y, rfl⟩
  constructor
  · intro i
    by_cases h : i.val < 2
    · have hk : ¬ (k ≤ i.val) := by omega
      simp [kIso, dcut, h, Nat.lt_of_lt_of_le h h2]
    · simp [kIso, h]
  · intro i
    by_cases h : i.val < 2 <;> simp [kIso, h]

/-- **The known Mordell–Weil plane does not help.**  The configuration can be chosen so that
`G ⊓ L` contains a fixed `2`-dimensional subspace — the image of `E(Q)/pE(Q)` — while the
total dimension of `G ⊓ L`, hence the dimension of the quotient modelling `Ш(E/Q)[p]`,
is an arbitrary `k ≥ 2`. -/
theorem exists_config_with_known_plane (F : Type*) [Field F] (N k : ℕ) (hk : k ≤ N)
    (h2 : 2 ≤ k) :
    ∃ (G L M : Submodule F (LocalSum F N)),
      Isotropic G ∧ Isotropic L ∧ L = Lcond F N ∧
      finrank F G = N ∧ finrank F L = N ∧
      M ≤ G ⊓ L ∧ finrank F M = 2 ∧
      finrank F (G ⊓ L : Submodule F (LocalSum F N)) = k := by
  refine ⟨Gglob F (dcut F N k), Lcond F N, LinearMap.range (kIso F N 2),
    isotropic_Gglob _, isotropic_Lcond, rfl, finrank_Gglob _, finrank_Lcond,
    kIso_two_le h2, ?_, finrank_inter hk⟩
  rw [LinearMap.finrank_range_of_inj (injective_kIso (F := F) (N := N) (k := 2) (by omega))]
  simp

/-- **Unboundedness.**  For every bound `B` there is such a configuration whose
"Selmer group" `G ⊓ L` has dimension exceeding `B`, while the pairing stays nondegenerate
and alternating and both subspaces stay maximal isotropic. -/
theorem inter_unbounded (F : Type*) [Field F] (B : ℕ) :
    ∃ (N : ℕ) (G L : Submodule F (LocalSum F N)),
      Isotropic G ∧ Isotropic L ∧
      finrank F G = N ∧ finrank F L = N ∧
      B < finrank F (G ⊓ L : Submodule F (LocalSum F N)) := by
  obtain ⟨G, L, hG, hL, hgr, hlr, hint, -⟩ :=
    exists_maximal_isotropic_pair_inter F (B + 1) (B + 1) le_rfl
  exact ⟨B + 1, G, L, hG, hL, hgr, hlr, by omega⟩

end SelmerDuality
