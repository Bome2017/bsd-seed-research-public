module

public import Mathlib

/-!
# Excess obstruction (Stage A) and the rank-two switch test (Stage B): algebraic skeleton

Lean source for `research_return/EXCESS_OBSTRUCTION_RETURN.md`.

Nothing arithmetic is formalised here: Galois cohomology, Chebotarev and the OpenAI lift test are
used in the written return only, each one labelled IMPORTED or HEURISTIC there. This file checks the
linear algebra those arguments use.

* §1 `ker_restrictObs`: for any obstruction map `O : S → Hom(D, K)` and any finite-dimensional
  `W ≤ S`, put `D^W = {δ : O w δ = 0 for all w ∈ W}`. Then
  `ker (S → Hom(D^W, K)) = W ⊔ ker O`. So restricting to `D^W` never loses separation, (A1) on
  `D^W` holds by definition, and Stage A is exactly `ker O ≤ W` (`ker_restrictObs_eq_iff`).
* §2 the commutator change of `vertical:obstruction-span` at the trivial twist,
  `B(x,y) = -e(f x, g y) + e(g x, f y)` with `e` alternating, is **symmetric**
  (`commChange_symm`). So its span contains no non-symmetric form (`not_mem_span_of_not_symm`):
  the "every rectangular matrix" conclusion cannot come from this mechanism on a self-dual
  coefficient. On the diagonal, `B(x,x) = -2·e(f x, g x)` (`commChange_self`), which is enough to
  detect a class.
* §3 `stageA_kernel`: the abstract (A1)+(A2) assembly. If `f, g` vanish on `W` and the difference
  direction realises `B(·, x)`, then the kernel of the restricted map is exactly `W`.
* §4 `not_dvd_of_even_card`: a good odd prime `p ≥ 7` with `#E(𝔽_p)` even is non-anomalous
  (PRE-CHECK 2).
* §5 Stage B: a one-plane switch that keeps the generic `H¹ = W` forces `W ⊆ ker loc`
  (`preserve_forces_loc_zero`). Its special-fibre dimension change and determinant valuation
  shift are read off the Jordan exponents of the relaxed Lagrangian: a drop by two forces a
  valuation shift of at least two (`single_plane_drop_two`). The two-plane exponent vector
  `[1,1,1,-3]` shows the no-go is specific to one plane (`two_plane_escape`).
  `det_ratio` is the top-exterior-power comparison.
-/

@[expose] public section

namespace ExcessObstruction

open Module

/-! ## §1 The universal kernel of the restricted obstruction map -/

section Kernel

variable {K S D : Type*} [Field K] [AddCommGroup S] [Module K S] [AddCommGroup D] [Module K D]

/-- `D^W`: the directions along which every class in `W` is unobstructed. -/
def annW (O : S →ₗ[K] Dual K D) (W : Submodule K S) : Submodule K D :=
  (W.map O).dualCoannihilator

/-- The obstruction map restricted to the directions in `D^W`. -/
def restrictObs (O : S →ₗ[K] Dual K D) (W : Submodule K S) : S →ₗ[K] Dual K (annW O W) :=
  (annW O W).subtype.dualMap.comp O

theorem mem_annW {O : S →ₗ[K] Dual K D} {W : Submodule K S} {δ : D} :
    δ ∈ annW O W ↔ ∀ w ∈ W, O w δ = 0 := by
  simp [annW, Submodule.mem_dualCoannihilator]

/-- (A1) on `D^W` holds by definition. -/
theorem restrictObs_of_mem (O : S →ₗ[K] Dual K D) (W : Submodule K S) {w : S} (hw : w ∈ W) :
    restrictObs O W w = 0 := by
  ext ⟨δ, hδ⟩
  exact (mem_annW.1 hδ) w hw

/-- **Universal kernel theorem.** `ker (S → Hom(D^W, K)) = W ⊔ ker O`. -/
theorem ker_restrictObs (O : S →ₗ[K] Dual K D) (W : Submodule K S) [FiniteDimensional K W] :
    LinearMap.ker (restrictObs O W) = W ⊔ LinearMap.ker O := by
  haveI : FiniteDimensional K (W.map O) := Module.Finite.map W O
  rw [restrictObs, LinearMap.ker_comp, LinearMap.ker_dualMap_eq_dualAnnihilator_range,
    Submodule.range_subtype, annW, Subspace.dualCoannihilator_dualAnnihilator_eq,
    Submodule.comap_map_eq]

/-- Stage A holds iff the full obstruction map has kernel inside `W`. -/
theorem ker_restrictObs_eq_iff (O : S →ₗ[K] Dual K D) (W : Submodule K S)
    [FiniteDimensional K W] :
    LinearMap.ker (restrictObs O W) = W ↔ LinearMap.ker O ≤ W := by
  rw [ker_restrictObs]
  exact sup_eq_left

/-- (A2) in element form: every class outside `W` is obstructed along some direction of `D^W`
iff `ker O ≤ W`. -/
theorem a2_iff (O : S →ₗ[K] Dual K D) (W : Submodule K S) [FiniteDimensional K W] :
    (∀ x, x ∉ W → ∃ δ ∈ annW O W, O x δ ≠ 0) ↔ LinearMap.ker O ≤ W := by
  rw [← ker_restrictObs_eq_iff]
  constructor
  · intro h
    apply le_antisymm
    · intro x hx
      by_contra hxW
      obtain ⟨δ, hδ, hne⟩ := h x hxW
      apply hne
      have := LinearMap.congr_fun (LinearMap.mem_ker.1 hx) ⟨δ, hδ⟩
      simpa [restrictObs] using this
    · intro w hw
      exact LinearMap.mem_ker.2 (restrictObs_of_mem O W hw)
  · intro h x hx
    by_contra hcon
    push_neg at hcon
    apply hx
    rw [← h]
    refine LinearMap.mem_ker.2 ?_
    ext ⟨δ, hδ⟩
    simpa [restrictObs] using hcon δ hδ

end Kernel

/-! ## §2 The commutator change at the trivial twist is symmetric -/

section Commutator

variable {K S M : Type*} [Field K] [AddCommGroup S] [Module K S] [AddCommGroup M] [Module K M]

/-- The change in the lift test when a Frobenius is multiplied by the commutator `[v,w']`, with
`f = (evaluation at v)`, `g = (evaluation at w')`: `B(x,y) = -e(f x, g y) + e(g x, f y)`. -/
def commChange (e : M →ₗ[K] M →ₗ[K] K) (f g : S →ₗ[K] M) : S →ₗ[K] S →ₗ[K] K :=
  -(e.compl₁₂ f g) + e.compl₁₂ g f

@[simp] theorem commChange_apply (e : M →ₗ[K] M →ₗ[K] K) (f g : S →ₗ[K] M) (x y : S) :
    commChange e f g x y = -e (f x) (g y) + e (g x) (f y) := by
  simp [commChange]

theorem alt_antisymm {e : M →ₗ[K] M →ₗ[K] K} (he : ∀ m, e m m = 0) (a b : M) :
    e a b = -e b a := by
  have h := he (a + b)
  simp only [map_add, LinearMap.add_apply, he a, he b] at h
  linear_combination h

/-- With `e` alternating (the Weil pairing), the commutator change is symmetric. -/
theorem commChange_symm {e : M →ₗ[K] M →ₗ[K] K} (he : ∀ m, e m m = 0) (f g : S →ₗ[K] M)
    (x y : S) : commChange e f g x y = commChange e f g y x := by
  simp only [commChange_apply]
  rw [alt_antisymm he (f x) (g y), alt_antisymm he (g x) (f y)]
  ring

theorem commChange_self {e : M →ₗ[K] M →ₗ[K] K} (he : ∀ m, e m m = 0) (f g : S →ₗ[K] M)
    (x : S) : commChange e f g x x = -2 * e (f x) (g x) := by
  simp only [commChange_apply]
  rw [alt_antisymm he (g x) (f x)]
  ring

/-- The diagonal value detects `x` as soon as `e(f x, g x) ≠ 0` and `2 ≠ 0`. -/
theorem commChange_self_ne_zero {e : M →ₗ[K] M →ₗ[K] K} (he : ∀ m, e m m = 0)
    (h2 : (2 : K) ≠ 0) (f g : S →ₗ[K] M) {x : S} (hx : e (f x) (g x) ≠ 0) :
    commChange e f g x x ≠ 0 := by
  rw [commChange_self he]
  exact mul_ne_zero (neg_ne_zero.2 h2) hx

/-- Classes on which both evaluations vanish see no change: (A1) for the difference directions. -/
theorem commChange_eq_zero_of_left {e : M →ₗ[K] M →ₗ[K] K} (f g : S →ₗ[K] M) {w : S}
    (hf : f w = 0) (hg : g w = 0) (y : S) : commChange e f g w y = 0 := by
  simp [hf, hg]

/-- Symmetric bilinear forms on `S`. -/
def symmForms (K S : Type*) [Field K] [AddCommGroup S] [Module K S] :
    Submodule K (S →ₗ[K] S →ₗ[K] K) where
  carrier := {B | ∀ x y, B x y = B y x}
  add_mem' := by
    intro a b ha hb x y
    simp [ha x y, hb x y]
  zero_mem' := by intro x y; simp
  smul_mem' := by
    intro c B hB x y
    simp [hB x y]

/-- Every form in the span of the commutator changes is symmetric. -/
theorem span_commChange_le {e : M →ₗ[K] M →ₗ[K] K} (he : ∀ m, e m m = 0) :
    Submodule.span K {B | ∃ f g : S →ₗ[K] M, B = commChange e f g} ≤ symmForms K S := by
  rw [Submodule.span_le]
  rintro B ⟨f, g, rfl⟩ x y
  exact commChange_symm he f g x y

/-- Hence a non-symmetric form is never in that span: the full rectangular span asserted by
`vertical:obstruction-span` is not produced by this mechanism at the trivial twist. -/
theorem not_mem_span_of_not_symm {e : M →ₗ[K] M →ₗ[K] K} (he : ∀ m, e m m = 0)
    {B : S →ₗ[K] S →ₗ[K] K} {x y : S} (hB : B x y ≠ B y x) :
    B ∉ Submodule.span K {B | ∃ f g : S →ₗ[K] M, B = commChange e f g} := by
  intro hmem
  exact hB (span_commChange_le he hmem x y)

/-- An explicit non-symmetric form exists once `dim S ≥ 2` (elementary matrix `E₁₂`). -/
theorem exists_not_symm (φ ψ : Dual K S) {x y : S} (h1 : φ x = 1) (h2 : ψ x = 0)
    (h3 : ψ y = 1) (h4 : φ y = 0) :
    ∃ B : S →ₗ[K] S →ₗ[K] K, B x y ≠ B y x := by
  refine ⟨(LinearMap.mul K K).compl₁₂ φ ψ, ?_⟩
  simp [h1, h2, h3, h4]

end Commutator

/-! ## §3 The abstract Stage A assembly -/

section Assembly

variable {K S D M : Type*} [Field K] [AddCommGroup S] [Module K S] [AddCommGroup D] [Module K D]
  [AddCommGroup M] [Module K M]

/-- **Stage A, algebraic form.** Suppose that for every `x ∉ W` there are evaluations `f, g`
vanishing on `W` (the commutators fix `L_p`, so Kummer classes of points vanish on them) with
`e(f x, g x) ≠ 0` (the receiver kernel plus irreducibility of `E[p]`), and a direction `δ` whose
obstruction is the commutator change `B(·, x)` (Chebotarev plus the lift-test formula). Then the
kernel of the obstruction map restricted to `D^W` is exactly `W`. -/
theorem stageA_kernel (O : S →ₗ[K] Dual K D) (W : Submodule K S) [FiniteDimensional K W]
    (e : M →ₗ[K] M →ₗ[K] K) (he : ∀ m, e m m = 0) (h2 : (2 : K) ≠ 0)
    (hdir : ∀ x, x ∉ W → ∃ (f g : S →ₗ[K] M) (δ : D),
      (∀ w ∈ W, f w = 0 ∧ g w = 0) ∧ e (f x) (g x) ≠ 0 ∧
      ∀ y, O y δ = commChange e f g y x) :
    LinearMap.ker (restrictObs O W) = W := by
  rw [ker_restrictObs_eq_iff, ← a2_iff]
  intro x hx
  obtain ⟨f, g, δ, hW, hne, hO⟩ := hdir x hx
  refine ⟨δ, mem_annW.2 fun w hw => ?_, ?_⟩
  · rw [hO]
    exact commChange_eq_zero_of_left f g (hW w hw).1 (hW w hw).2 x
  · rw [hO]
    exact commChange_self_ne_zero he h2 f g hne

end Assembly

/-! ## §4 Non-anomaly from rational 2-torsion (PRE-CHECK 2) -/

/-- If `p ≥ 7` is an odd prime and `n = #E(𝔽_p)` is even, positive and within the Hasse bound
`(p + 1 - n)² ≤ 4p`, then `p ∤ n`. So `E(𝔽_p)[p] = 0`. -/
theorem not_dvd_of_even_card (p n : ℕ) (hp : 7 ≤ p) (hpodd : Odd p) (hn : Even n) (hpos : 0 < n)
    (hH : ((p : ℤ) + 1 - n) ^ 2 ≤ 4 * p) : ¬ p ∣ n := by
  rintro ⟨k, rfl⟩
  rcases Nat.lt_or_ge k 2 with hk | hk
  · interval_cases k
    · simp at hpos
    · simp only [mul_one] at hn
      exact (Nat.not_even_iff_odd.2 hpodd) hn
  · have hk' : (2 : ℤ) ≤ k := by exact_mod_cast hk
    have hp' : (7 : ℤ) ≤ p := by exact_mod_cast hp
    push_cast at hH
    have h1 : (p : ℤ) - 1 ≤ (p : ℤ) * k - p - 1 := by nlinarith
    have h2 : (0 : ℤ) ≤ (p : ℤ) - 1 := by omega
    have h3 : ((p : ℤ) - 1) ^ 2 ≤ ((p : ℤ) + 1 - p * k) ^ 2 := by nlinarith
    nlinarith

/-! ## §5 Stage B: the one-plane rank-two switch -/

section StageB

variable {K V P : Type*} [Field K] [AddCommGroup V] [Module K V] [AddCommGroup P] [Module K P]

/-- In the relaxed generic cohomology `V` with localisation `loc = (finite part, singular part)`,
the finite-condition and switched classes are the preimages of the two planes. If `W` lies in both
(the switch preserves the generic `H¹ = W`), then `W` is locally trivial at the switch prime. -/
theorem preserve_forces_loc_zero (locF locS : V →ₗ[K] P) (W : Submodule K V)
    (hF : W ≤ LinearMap.ker locS) (hS : W ≤ LinearMap.ker locF) :
    W ≤ LinearMap.ker (locF.prod locS) := by
  intro w hw
  simp [LinearMap.mem_ker.1 (hF hw), LinearMap.mem_ker.1 (hS hw)]

/-- Special-fibre change `dim H¹(C_{S,k}) - dim H¹(C_{F,k})` for a relaxed Lagrangian with Jordan
exponents `a`: `#{aᵢ < 0} - #{aᵢ > 0}`. -/
def dimChange (a : List ℤ) : ℤ :=
  (a.countP (fun t => decide (t < 0)) : ℤ) - (a.countP (fun t => decide (0 < t)) : ℤ)

/-- Valuation shift of the `Δ_W` coordinate across the switch: `v(det φ) = Σ aᵢ`. -/
def valShift (a : List ℤ) : ℤ := a.sum

/-- **One-plane no-go.** For a single switch plane (two exponents), a drop of the special-fibre
dimension by two forces the `Δ_W` valuation to move by at least two. -/
theorem single_plane_drop_two (a₁ a₂ : ℤ) (h : dimChange [a₁, a₂] = -2) :
    2 ≤ valShift [a₁, a₂] := by
  simp only [dimChange, valShift, List.countP_cons, List.countP_nil, List.sum_cons,
    List.sum_nil] at h ⊢
  by_cases h1 : a₁ < 0 <;> by_cases h2 : a₂ < 0 <;> by_cases h3 : 0 < a₁ <;>
    by_cases h4 : 0 < a₂ <;> simp_all
  all_goals omega

/-- Equivalently: a one-plane switch preserving the valuation of `Δ_W` does not change the
special-fibre dimension. -/
theorem single_plane_val_zero (a₁ a₂ : ℤ) (h : valShift [a₁, a₂] = 0) :
    dimChange [a₁, a₂] = 0 := by
  simp only [dimChange, valShift, List.countP_cons, List.countP_nil, List.sum_cons,
    List.sum_nil] at h ⊢
  by_cases h1 : a₁ < 0 <;> by_cases h2 : a₂ < 0 <;> by_cases h3 : 0 < a₁ <;>
    by_cases h4 : 0 < a₂ <;> simp_all
  all_goals omega

/-- With two switch planes at once the linear algebra allows a drop by two with no valuation
change; the no-go above is specific to one plane. -/
theorem two_plane_escape : dimChange [1, 1, 1, -3] = -2 ∧ valShift [1, 1, 1, -3] = 0 := by
  decide

/-- Top-exterior-power comparison: if the two boundary maps into the common dual line satisfy
`δ_F = δ_S · φ`, the two determinant coordinates differ by `det φ`. -/
theorem det_ratio {n : Type*} [Fintype n] [DecidableEq n] (δF δS φ : Matrix n n K)
    (h : δF = δS * φ) : δF.det = δS.det * φ.det := by
  rw [h, Matrix.det_mul]

end StageB

end ExcessObstruction

end
