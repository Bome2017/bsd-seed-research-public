module

public import Mathlib

/-!
# The fixed 1-motive `M_E = [ℤ² → E]`: algebraic skeleton

Every arithmetic input is an explicit hypothesis. `ONE_MOTIVE_RESULT.md` (project root) states
the arithmetic results these lemmas encode.

* `OneMotive.KummerData`: the global and local Kummer sequences
  `0 → H⁰(F,M)/n → H¹(F,M[n]) → H¹(F,M)[n] → 0`, with localization maps.
  `KummerData.selEquivSha` is the diagram chase `Sel(ℚ,M)(n) ≅ Ш¹(ℚ,M)[n]` when `H⁰(ℚ,M)/n = 0`.
  The general case is the short exact sequence `0 → H⁰/n → Sel → Ш¹[n] → 0`
  (`i_mem_sel`, `j_mem_shaN`, `exists_sel_of_mem_shaN`, `mem_range_of_sel_of_j_eq_zero`).
* `OneMotive.quotient_trivial_of_coprime`: a finite group of order prime to `n` has `G/nG = 0`.
  It is used with `H⁰(ℚ,M_E) ≅ E(ℚ)_tors ≅ ℤ/2` and `n = p` odd.
* `OneMotive.ShaData` and `ShaData.shaEquiv`: the chase `Ш(E) ≅ Ш¹(M)`. Its inputs are the
  global and local injectivity of `H¹(E) → H¹(M)`, exactness at `H¹(M)`, and `Ш²(ℤ²) = 0`.
* `OneMotive.coinvariants_not_free_rank_one`: if `T` surjects equivariantly onto a trivial
  module `R²`, then no `T/(τ-1)T` is free of rank one. This is the failure of the
  Burns–Sakamoto–Sano / Sakamoto hypothesis for `T_pM_E`.
* `OneMotive.not_cyclic_of_two_dim_torsion`: a group isomorphic to `ℤ/p^n` has no subgroup
  `(ℤ/p)²`. This is why no prime `q ≡ 1 (mod p)` is a Stark-system prime for `M_E[p^n]`.
* `OneMotive.global_index_forces_finite`: suppose a fixed nonzero integer `A` controls `p ∣ z_p`
  outside a finite set, and `z_p = s_p·r_p`. Then only finitely many primes divide `r_p`, and
  only finitely many divide `s_p`.
-/

@[expose] public section

namespace OneMotive

open Function

/-! ## 1. The Kummer-sequence chase `Sel ≅ Ш¹[n]` -/

/-- The global and local Kummer sequences of a 1-motive `M` for the integer `n`, with
localization maps. `G0 = H⁰(ℚ,M)/n`, `G1 = H¹(ℚ,M[n])`, `G2 = H¹(ℚ,M)`, and `L0 v, L1 v, L2 v`
are the corresponding local groups at the place `v`. -/
structure KummerData (n : ℕ) {ι : Type*} (G0 G1 G2 : Type*) [AddCommGroup G0] [AddCommGroup G1]
    [AddCommGroup G2] (L0 L1 L2 : ι → Type*) [∀ v, AddCommGroup (L0 v)]
    [∀ v, AddCommGroup (L1 v)] [∀ v, AddCommGroup (L2 v)] where
  /-- `H⁰(ℚ,M)/n → H¹(ℚ,M[n])` -/
  i : G0 →+ G1
  /-- `H¹(ℚ,M[n]) → H¹(ℚ,M)` -/
  j : G1 →+ G2
  /-- local `H⁰(ℚ_v,M)/n → H¹(ℚ_v,M[n])` -/
  iv : ∀ v, L0 v →+ L1 v
  /-- local `H¹(ℚ_v,M[n]) → H¹(ℚ_v,M)` -/
  jv : ∀ v, L1 v →+ L2 v
  /-- localization on `H⁰/n` -/
  l0 : ∀ v, G0 →+ L0 v
  /-- localization on `H¹(M[n])` -/
  l1 : ∀ v, G1 →+ L1 v
  /-- localization on `H¹(M)` -/
  l2 : ∀ v, G2 →+ L2 v
  i_inj : Injective i
  exact : ∀ x, j x = 0 → x ∈ i.range
  ji : ∀ g, j (i g) = 0
  j_tors : ∀ x, n • j x = 0
  j_surj : ∀ y, n • y = 0 → ∃ x, j x = y
  exact_v : ∀ v x, jv v x = 0 ↔ x ∈ (iv v).range
  comm1 : ∀ v g, l1 v (i g) = iv v (l0 v g)
  comm2 : ∀ v x, l2 v (j x) = jv v (l1 v x)

namespace KummerData

variable {n : ℕ} {ι : Type*} {G0 G1 G2 : Type*} [AddCommGroup G0] [AddCommGroup G1]
  [AddCommGroup G2] {L0 L1 L2 : ι → Type*} [∀ v, AddCommGroup (L0 v)]
  [∀ v, AddCommGroup (L1 v)] [∀ v, AddCommGroup (L2 v)]
  (D : KummerData n G0 G1 G2 L0 L1 L2)

/-- The Selmer group: classes whose localization at every `v` comes from `H⁰(ℚ_v,M)/n`. -/
def sel : AddSubgroup G1 := ⨅ v, (D.iv v).range.comap (D.l1 v)

/-- `Ш¹(ℚ,M)`: classes that are locally trivial at every `v`. -/
def sha : AddSubgroup G2 := ⨅ v, (D.l2 v).ker

/-- `Ш¹(ℚ,M)[n]`. -/
def shaN : AddSubgroup G2 := D.sha ⊓ (nsmulAddMonoidHom n : G2 →+ G2).ker

lemma mem_sel {x : G1} : x ∈ D.sel ↔ ∀ v, D.l1 v x ∈ (D.iv v).range := by
  simp only [sel, AddSubgroup.mem_iInf, AddSubgroup.mem_comap]

lemma mem_shaN {y : G2} : y ∈ D.shaN ↔ (∀ v, D.l2 v y = 0) ∧ n • y = 0 := by
  simp only [shaN, sha, AddSubgroup.mem_inf, AddSubgroup.mem_iInf, AddMonoidHom.mem_ker,
    nsmulAddMonoidHom_apply]

/-- Global `H⁰/n` lands in the Selmer group. -/
theorem i_mem_sel (g : G0) : D.i g ∈ D.sel :=
  D.mem_sel.2 fun v => ⟨D.l0 v g, (D.comm1 v g).symm⟩

/-- Selmer classes map into `Ш¹[n]`. -/
theorem j_mem_shaN {x : G1} (hx : x ∈ D.sel) : D.j x ∈ D.shaN := by
  refine D.mem_shaN.2 ⟨fun v => ?_, D.j_tors x⟩
  rw [D.comm2]
  exact (D.exact_v v _).2 (D.mem_sel.1 hx v)

/-- Every element of `Ш¹[n]` comes from a Selmer class. -/
theorem exists_sel_of_mem_shaN {y : G2} (hy : y ∈ D.shaN) : ∃ x ∈ D.sel, D.j x = y := by
  obtain ⟨hloc, htors⟩ := D.mem_shaN.1 hy
  obtain ⟨x, rfl⟩ := D.j_surj y htors
  refine ⟨x, D.mem_sel.2 fun v => ?_, rfl⟩
  rw [← D.exact_v, ← D.comm2]
  exact hloc v

/-- The kernel of `Sel → Ш¹[n]` is the image of `H⁰/n`. -/
theorem mem_range_of_sel_of_j_eq_zero {x : G1} (hx0 : D.j x = 0) : x ∈ D.i.range :=
  D.exact x hx0

/-- The map `Sel → Ш¹[n]`. -/
def selToSha : D.sel →+ D.shaN :=
  AddMonoidHom.codRestrict (D.j.comp D.sel.subtype) D.shaN fun x => D.j_mem_shaN x.2

/-- **Fixed receiver, algebraic form.** If `H⁰(ℚ,M)/n = 0` then `Sel(ℚ,M)(n) ≅ Ш¹(ℚ,M)[n]`. -/
noncomputable def selEquivSha [Subsingleton G0] : D.sel ≃+ D.shaN :=
  AddEquiv.ofBijective D.selToSha
    ⟨by
      rw [injective_iff_map_eq_zero]
      intro x hx
      have hx0 : D.j x = 0 := congrArg Subtype.val hx
      obtain ⟨g, hg⟩ := D.exact x hx0
      have hg0 : g = 0 := Subsingleton.elim _ _
      apply Subtype.ext
      rw [← hg, hg0, map_zero]
      rfl,
     by
      rintro ⟨y, hy⟩
      obtain ⟨x, hx, rfl⟩ := D.exists_sel_of_mem_shaN hy
      exact ⟨⟨x, hx⟩, rfl⟩⟩

theorem selEquivSha_apply [Subsingleton G0] (x : D.sel) :
    (D.selEquivSha x : G2) = D.j x := rfl

end KummerData

/-- A finite abelian group of order prime to `n` is `n`-divisible, so `G/nG = 0`.
It is applied to `H⁰(ℚ,M_E) = E(ℚ)/⟨P₁,P₂⟩ ≅ ℤ/2` with `n = p` odd. -/
theorem quotient_trivial_of_coprime {G : Type*} [AddCommGroup G] [Finite G] {n : ℕ}
    (hn : Nat.Coprime (Nat.card G) n) (g : G) : ∃ h : G, n • h = g := by
  have hinj : Injective (fun h : G => n • h) := by
    intro a b hab
    have h0 : n • (a - b) = 0 := by
      simp only at hab
      rw [smul_sub, hab, sub_self]
    have h1 : addOrderOf (a - b) ∣ n := addOrderOf_dvd_of_nsmul_eq_zero h0
    have h2 : addOrderOf (a - b) ∣ Nat.card G := addOrderOf_dvd_natCard _
    have h3 : addOrderOf (a - b) = 1 := (Nat.Coprime.coprime_dvd_left h2 hn).eq_one_of_dvd h1
    have h4 := addOrderOf_nsmul_eq_zero (a - b)
    rw [h3, one_nsmul] at h4
    exact sub_eq_zero.1 h4
  exact (Finite.injective_iff_surjective.1 hinj) g

/-! ## 2. `Ш(E) ≅ Ш¹(M)` -/

/-- The piece `H¹(F,E) → H¹(F,M) → H²(F,ℤ²)` of the hypercohomology sequence of the triangle
`E → M → ℤ²[1]`, globally and locally, with localization maps. -/
structure ShaData {ι : Type*} (G1 G2 G3 : Type*) [AddCommGroup G1] [AddCommGroup G2]
    [AddCommGroup G3] (L1 L2 L3 : ι → Type*) [∀ v, AddCommGroup (L1 v)]
    [∀ v, AddCommGroup (L2 v)] [∀ v, AddCommGroup (L3 v)] where
  /-- `H¹(ℚ,E) → H¹(ℚ,M)` -/
  a : G1 →+ G2
  /-- `H¹(ℚ,M) → H²(ℚ,ℤ²)` -/
  b : G2 →+ G3
  /-- local `H¹(ℚ_v,E) → H¹(ℚ_v,M)` -/
  av : ∀ v, L1 v →+ L2 v
  /-- local `H¹(ℚ_v,M) → H²(ℚ_v,ℤ²)` -/
  bv : ∀ v, L2 v →+ L3 v
  /-- localization on `H¹(E)` -/
  l1 : ∀ v, G1 →+ L1 v
  /-- localization on `H¹(M)` -/
  l2 : ∀ v, G2 →+ L2 v
  /-- localization on `H²(ℤ²)` -/
  l3 : ∀ v, G3 →+ L3 v
  /-- global injectivity (from `H¹(ℚ,ℤ²) = 0`) -/
  a_inj : Injective a
  /-- local injectivity (from `H¹(ℚ_v,ℤ²) = 0`) -/
  av_inj : ∀ v, Injective (av v)
  exact : ∀ y, b y = 0 → y ∈ a.range
  comm_a : ∀ v x, l2 v (a x) = av v (l1 v x)
  comm_b : ∀ v y, l3 v (b y) = bv v (l2 v y)
  /-- `Ш²(ℚ,ℤ²) = Ш¹(ℚ,ℚ/ℤ)² = 0` (Chebotarev) -/
  sha2_zero : ∀ z, (∀ v, l3 v z = 0) → z = 0

namespace ShaData

variable {ι : Type*} {G1 G2 G3 : Type*} [AddCommGroup G1] [AddCommGroup G2] [AddCommGroup G3]
  {L1 L2 L3 : ι → Type*} [∀ v, AddCommGroup (L1 v)] [∀ v, AddCommGroup (L2 v)]
  [∀ v, AddCommGroup (L3 v)] (D : ShaData G1 G2 G3 L1 L2 L3)

/-- `Ш(E/ℚ)`. -/
def shaE : AddSubgroup G1 := ⨅ v, (D.l1 v).ker

/-- `Ш¹(ℚ,M)`. -/
def shaM : AddSubgroup G2 := ⨅ v, (D.l2 v).ker

lemma mem_shaE {x : G1} : x ∈ D.shaE ↔ ∀ v, D.l1 v x = 0 := by
  simp only [shaE, AddSubgroup.mem_iInf, AddMonoidHom.mem_ker]

lemma mem_shaM {y : G2} : y ∈ D.shaM ↔ ∀ v, D.l2 v y = 0 := by
  simp only [shaM, AddSubgroup.mem_iInf, AddMonoidHom.mem_ker]

theorem a_mem_shaM {x : G1} (hx : x ∈ D.shaE) : D.a x ∈ D.shaM :=
  D.mem_shaM.2 fun v => by rw [D.comm_a, D.mem_shaE.1 hx v, map_zero]

theorem exists_shaE_of_mem_shaM {y : G2} (hy : y ∈ D.shaM) : ∃ x ∈ D.shaE, D.a x = y := by
  have hb : D.b y = 0 := D.sha2_zero _ fun v => by rw [D.comm_b, D.mem_shaM.1 hy v, map_zero]
  obtain ⟨x, rfl⟩ := D.exact y hb
  refine ⟨x, D.mem_shaE.2 fun v => D.av_inj v ?_, rfl⟩
  rw [← D.comm_a, D.mem_shaM.1 hy v, map_zero]

/-- **`Ш¹(ℚ,M_E) ≅ Ш(E/ℚ)`, algebraic form.** -/
noncomputable def shaEquiv : D.shaE ≃+ D.shaM :=
  AddEquiv.ofBijective
    (AddMonoidHom.codRestrict (D.a.comp D.shaE.subtype) D.shaM fun x => D.a_mem_shaM x.2)
    ⟨fun x y h => Subtype.ext (D.a_inj (congrArg Subtype.val h)), by
      rintro ⟨y, hy⟩
      obtain ⟨x, hx, rfl⟩ := D.exists_shaE_of_mem_shaM hy
      exact ⟨⟨x, hx⟩, rfl⟩⟩

theorem shaEquiv_apply (x : D.shaE) : (D.shaEquiv x : G2) = D.a x := rfl

end ShaData

/-! ## 3. Coinvariants of `T_pM_E` are never free of rank one -/

/-- Suppose `T` surjects onto `R²` by a map that is invariant under `τ`. (The Galois action on
the lattice quotient `ℤ_p²` of `T_pM_E` is trivial.) Then `T/(τ-1)T` is not free of rank one. -/
theorem coinvariants_not_free_rank_one {R T : Type*} [CommRing R] [Nontrivial R]
    [AddCommGroup T] [Module R T] (τ : T →ₗ[R] T) (f : T →ₗ[R] (Fin 2 → R))
    (hf : Surjective f) (hfix : f ∘ₗ τ = f) :
    IsEmpty ((T ⧸ LinearMap.range (τ - LinearMap.id)) ≃ₗ[R] R) := by
  refine ⟨fun e => ?_⟩
  have hle : LinearMap.range (τ - LinearMap.id) ≤ LinearMap.ker f := by
    rintro _ ⟨x, rfl⟩
    simp only [LinearMap.mem_ker, LinearMap.sub_apply, LinearMap.id_apply, map_sub]
    rw [← LinearMap.comp_apply, hfix, sub_self]
  set g := (LinearMap.range (τ - LinearMap.id)).liftQ f hle
  have hg : Surjective g := by
    intro y
    obtain ⟨x, rfl⟩ := hf y
    exact ⟨Submodule.Quotient.mk x, rfl⟩
  let h : (Fin 1 → R) →ₗ[R] (Fin 2 → R) :=
    g ∘ₗ e.symm.toLinearMap ∘ₗ (LinearEquiv.funUnique (Fin 1) R R).toLinearMap
  have hh : Surjective h :=
    hg.comp (e.symm.surjective.comp (LinearEquiv.funUnique (Fin 1) R R).surjective)
  have := le_of_fin_surjective R h hh
  omega

/-! ## 4. Stark-system primes for `M_E[p^n]` satisfy `q ≢ 1 (mod p)` -/

/-- A group isomorphic to `ℤ/p^n` has no subgroup isomorphic to `(ℤ/p)²`. For `q ≡ 1 (mod p)`,
`H¹_{/f}(ℚ_q, M_E[p^n])[p] ≅ M_E[p](-1)^{Frob_q}` contains `(ℤ/p)²`, so `q` is not a
Stark-system prime. -/
theorem not_cyclic_of_two_dim_torsion (p n : ℕ) [hp : Fact p.Prime] {X : Type*}
    [AddCommGroup X] (e : X ≃+ ZMod (p ^ n)) (φ : ZMod p × ZMod p →+ X)
    (hφ : Injective φ) : False := by
  haveI : IsAddCyclic X := isAddCyclic_of_surjective e.symm.toAddMonoidHom e.symm.surjective
  let e2 : ZMod p × ZMod p ≃+ φ.range := AddMonoidHom.ofInjective hφ
  haveI : IsAddCyclic (ZMod p × ZMod p) :=
    isAddCyclic_of_surjective e2.symm.toAddMonoidHom e2.symm.surjective
  obtain ⟨g, hg⟩ := IsAddCyclic.exists_ofOrder_eq_natCard (α := ZMod p × ZMod p)
  have hcard : Nat.card (ZMod p × ZMod p) = p * p := by
    rw [Nat.card_prod, Nat.card_zmod]
  have hdvd : addOrderOf g ∣ p := by
    apply addOrderOf_dvd_of_nsmul_eq_zero
    rcases g with ⟨a, b⟩
    ext <;> simp [nsmul_eq_mul]
  rw [hg, hcard] at hdvd
  have := Nat.le_of_dvd hp.out.pos hdvd
  nlinarith [hp.out.two_le]

/-! ## 5. A fixed global index forces every factor to be a unit almost everywhere -/

/-- Suppose `p ∣ z_p ⟺ p ∣ A` for all primes `p ∉ S`, with `A ≠ 0`, and `z_p = s_p·r_p`. Then
only finitely many primes divide `r_p`, and only finitely many divide `s_p`. For the
Euler-characteristic element `z_p = #Ш[p^∞]·(p-adic regulator index)`, a global index therefore
needs both FIN-tail and the `p`-unit property of the normalized `p`-adic regulator for almost
all `p`. -/
theorem global_index_forces_finite (S : Finset ℕ) (A : ℤ) (hA : A ≠ 0) (z s r : ℕ → ℤ)
    (hz : ∀ p, z p = s p * r p)
    (hglob : ∀ p, p.Prime → p ∉ S → ((p : ℤ) ∣ z p ↔ (p : ℤ) ∣ A)) :
    {p : ℕ | p.Prime ∧ (p : ℤ) ∣ r p}.Finite ∧ {p : ℕ | p.Prime ∧ (p : ℤ) ∣ s p}.Finite := by
  have hfin : ((S ∪ A.natAbs.divisors : Finset ℕ) : Set ℕ).Finite := Finset.finite_toSet _
  have key : ∀ p : ℕ, p.Prime → (p : ℤ) ∣ z p → p ∈ (S ∪ A.natAbs.divisors : Finset ℕ) := by
    intro p hp hzp
    by_cases hS : p ∈ S
    · exact Finset.mem_union_left _ hS
    · have hpA := (hglob p hp hS).1 hzp
      apply Finset.mem_union_right
      rw [Nat.mem_divisors]
      exact ⟨Int.natCast_dvd.1 hpA, Int.natAbs_ne_zero.2 hA⟩
  refine ⟨hfin.subset fun p hp => key p hp.1 ?_, hfin.subset fun p hp => key p hp.1 ?_⟩
  · rw [hz]; exact dvd_mul_of_dvd_right hp.2 _
  · rw [hz]; exact dvd_mul_of_dvd_left hp.2 _

end OneMotive
