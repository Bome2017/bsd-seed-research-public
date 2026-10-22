module

public import Mathlib

/-!
# Algebraic skeleton for the fixed 1-motive `M_E = [ℤ² → E]` (2026-10-07)

Abstract algebra only; every arithmetic input is a named hypothesis. See
`RequestProject/OneMotive/RESULT.md` for the arithmetic and the labels.

* `sel_equiv_sha_of_H0_trivial` — the diagram chase `Sel(ℚ,M)(n) ≅ Ш¹(ℚ,M)[n]` when
  `H⁰(ℚ,M)/n = 0`: in `0 → H⁰/n → H¹(M[n]) → H¹(M)[n] → 0`, the Selmer group is the preimage
  of `Ш¹[n]`.
* `sha_equiv_of_sha2_trivial` — `Ш(E) ≅ Ш¹(M_E)`: injective comparison maps globally and
  locally, together with `Ш²(ℚ,ℤ²) = 0`.
* `two_torsion_div_odd` — `H⁰(ℚ,M_E) ≅ ℤ/2` gives `H⁰/p = 0` for odd `p`.
* `not_coinvariants_rank_one` — PRE-CHECK (d): if `G` acts trivially on a quotient `R²` of
  `T`, then `T/(1-τ)T` is never free of rank one.
* `two_le_finrank_ker_sub_one` — if `g` acts trivially on a quotient `K²` of a
  4-dimensional `V`, then `ker(g - 1)` has dimension at least 2. (For `q ≡ 1 (mod p)` this
  makes the singular quotient `H¹_{/f}(ℚ_q, M_E[p])` at least 2-dimensional.)
-/

@[expose] public section

namespace OneMotive

/-- **Diagram chase.** `ι : Q → H1n` is `H⁰(M)/n → H¹(M[n])`, `κ : H1n → H1` is
`H¹(M[n]) → H¹(M)`, exact at `H1n`, and `Sha ≤ range κ` (true for `Ш¹[n]`, since `κ` maps onto
`H¹(M)[n]`). If `Q = 0`, the Selmer group `κ⁻¹(Sha)` is isomorphic to `Sha`. -/
theorem sel_equiv_sha_of_H0_trivial {R Q H1n H1 : Type*} [Ring R]
    [AddCommGroup Q] [Module R Q] [AddCommGroup H1n] [Module R H1n]
    [AddCommGroup H1] [Module R H1] [Subsingleton Q]
    (ι : Q →ₗ[R] H1n) (κ : H1n →ₗ[R] H1) (hexact : LinearMap.ker κ = LinearMap.range ι)
    (Sha : Submodule R H1) (hsurj : Sha ≤ LinearMap.range κ) :
    Nonempty (Sha.comap κ ≃ₗ[R] Sha) := by
  have hinj : Function.Injective κ := by
    rw [← LinearMap.ker_eq_bot, hexact, eq_bot_iff]
    rintro x ⟨q, rfl⟩
    simp [Subsingleton.elim q 0]
  let f : Sha.comap κ →ₗ[R] Sha := κ.restrict (fun x hx => hx)
  refine ⟨LinearEquiv.ofBijective f ⟨?_, ?_⟩⟩
  · intro x y hxy
    apply Subtype.ext
    apply hinj
    simpa [f] using congrArg Subtype.val hxy
  · rintro ⟨y, hy⟩
    obtain ⟨x, rfl⟩ := hsurj hy
    exact ⟨⟨x, hy⟩, rfl⟩

/-- **`Ш(E) ≅ Ш¹(M_E)`.** `iE : H¹(E) → H¹(M)` injective, `j : H¹(M) → H²(ℤ²)` with
`ker j = range iE`; local versions `iP` (injective), `jP`; the squares commute; and the
localization `locZ` on `H²(ℚ,ℤ²)` is injective (`Ш²(ℚ,ℤ²) = 0`). Then `iE` restricts to an
isomorphism `ker locE ≃ ker locM`. -/
theorem sha_equiv_of_sha2_trivial {R E1 M1 Z2 PE PM PZ : Type*} [Ring R]
    [AddCommGroup E1] [Module R E1] [AddCommGroup M1] [Module R M1]
    [AddCommGroup Z2] [Module R Z2] [AddCommGroup PE] [Module R PE]
    [AddCommGroup PM] [Module R PM] [AddCommGroup PZ] [Module R PZ]
    (iE : E1 →ₗ[R] M1) (j : M1 →ₗ[R] Z2) (hiE : Function.Injective iE)
    (hexact : LinearMap.ker j = LinearMap.range iE)
    (locE : E1 →ₗ[R] PE) (locM : M1 →ₗ[R] PM) (locZ : Z2 →ₗ[R] PZ)
    (iP : PE →ₗ[R] PM) (jP : PM →ₗ[R] PZ) (hiP : Function.Injective iP)
    (hsq1 : locM ∘ₗ iE = iP ∘ₗ locE) (hsq2 : locZ ∘ₗ j = jP ∘ₗ locM)
    (hSha2 : Function.Injective locZ) :
    Nonempty (LinearMap.ker locE ≃ₗ[R] LinearMap.ker locM) := by
  have hmaps : ∀ y ∈ LinearMap.ker locE, iE y ∈ LinearMap.ker locM := by
    intro y hy
    have := LinearMap.congr_fun hsq1 y
    simp only [LinearMap.coe_comp, Function.comp_apply] at this
    rw [LinearMap.mem_ker] at hy ⊢
    rw [this, hy, map_zero]
  let f : LinearMap.ker locE →ₗ[R] LinearMap.ker locM := iE.restrict hmaps
  refine ⟨LinearEquiv.ofBijective f ⟨?_, ?_⟩⟩
  · intro x y hxy
    apply Subtype.ext
    apply hiE
    simpa [f] using congrArg Subtype.val hxy
  · rintro ⟨x, hx⟩
    rw [LinearMap.mem_ker] at hx
    have hj : j x = 0 := by
      apply hSha2
      have := LinearMap.congr_fun hsq2 x
      simp only [LinearMap.coe_comp, Function.comp_apply] at this
      rw [this, hx, map_zero, map_zero]
    have : x ∈ LinearMap.range iE := by rw [← hexact]; exact hj
    obtain ⟨y, rfl⟩ := this
    have hy : locE y = 0 := by
      apply hiP
      have := LinearMap.congr_fun hsq1 y
      simp only [LinearMap.coe_comp, Function.comp_apply] at this
      rw [← this, hx, map_zero]
    exact ⟨⟨y, hy⟩, rfl⟩

/-- **`H⁰(ℚ,M_E)/p = 0` for odd `p`.** `H⁰(ℚ,M_E) = E(ℚ)/⟨P₁,P₂⟩ ≅ E(ℚ)_tors ≅ ℤ/2` is killed by
2, so it is `p`-divisible for every odd `p`. -/
theorem two_torsion_div_odd {A : Type*} [AddCommGroup A] (h2 : ∀ a : A, (2 : ℕ) • a = 0)
    (p : ℕ) (hp : Odd p) (a : A) : ∃ b : A, p • b = a := by
  obtain ⟨k, rfl⟩ := hp
  refine ⟨a, ?_⟩
  rw [add_smul, one_smul, mul_comm, mul_smul, h2, smul_zero, zero_add]

/-- **PRE-CHECK (d), coinvariant lemma.** Let `π : T → R²` be surjective with `π ∘ τ = π`
(Galois acts trivially on the lattice quotient `ℤ_p²` of `T_pM_E`). Then
`T/(1-τ)T` is not free of rank one, for any `τ`. -/
theorem not_coinvariants_rank_one {R T : Type*} [CommRing R] [Nontrivial R]
    [AddCommGroup T] [Module R T] (τ : T →ₗ[R] T) (π : T →ₗ[R] (Fin 2 → R))
    (hπ : Function.Surjective π) (htriv : π ∘ₗ τ = π) :
    IsEmpty ((T ⧸ LinearMap.range (LinearMap.id - τ)) ≃ₗ[R] (Fin 1 → R)) := by
  constructor
  intro e
  have hle : LinearMap.range (LinearMap.id - τ) ≤ LinearMap.ker π := by
    rintro _ ⟨x, rfl⟩
    rw [LinearMap.mem_ker, LinearMap.sub_apply, map_sub, LinearMap.id_apply]
    have := LinearMap.congr_fun htriv x
    simp only [LinearMap.coe_comp, Function.comp_apply] at this
    rw [this, sub_self]
  let πbar := (LinearMap.range (LinearMap.id - τ)).liftQ π hle
  have hπbar : Function.Surjective πbar := by
    intro y
    obtain ⟨x, rfl⟩ := hπ y
    exact ⟨Submodule.Quotient.mk x, rfl⟩
  let g : (Fin 1 → R) →ₗ[R] (Fin 2 → R) := πbar ∘ₗ e.symm.toLinearMap
  have hg : Function.Surjective g := hπbar.comp e.symm.surjective
  have := le_of_fin_surjective R g hg
  omega

/-- **Rank of the singular quotient at `q ≡ 1 (mod p)`.** If `g` acts on a 4-dimensional
`V` (here `M_E[p]`) trivially on a quotient `K²` (the lattice quotient `𝔽_p²`), then
`ker(g - 1)` has dimension at least 2. -/
theorem two_le_finrank_ker_sub_one {K V : Type*} [Field K] [AddCommGroup V] [Module K V]
    [FiniteDimensional K V] (hV : Module.finrank K V = 4) (g : V →ₗ[K] V)
    (π : V →ₗ[K] (Fin 2 → K)) (hπ : Function.Surjective π) (htriv : π ∘ₗ g = π) :
    2 ≤ Module.finrank K (LinearMap.ker (g - LinearMap.id)) := by
  have hle : LinearMap.range (g - LinearMap.id) ≤ LinearMap.ker π := by
    rintro _ ⟨x, rfl⟩
    rw [LinearMap.mem_ker, LinearMap.sub_apply, map_sub, LinearMap.id_apply]
    have := LinearMap.congr_fun htriv x
    simp only [LinearMap.coe_comp, Function.comp_apply] at this
    rw [this, sub_self]
  have h1 := LinearMap.finrank_range_add_finrank_ker π
  have h2 := LinearMap.finrank_range_add_finrank_ker (g - LinearMap.id)
  rw [LinearMap.range_eq_top.mpr hπ, finrank_top, Module.finrank_fin_fun] at h1
  have h3 := Submodule.finrank_mono hle
  omega

end OneMotive
