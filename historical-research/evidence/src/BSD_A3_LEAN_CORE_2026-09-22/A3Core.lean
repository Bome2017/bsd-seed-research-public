import Mathlib

/-!
# A3 signed minimal-λ bridge — algebraic core (§§2–4 of `SIGNED_MINIMAL_LAMBDA_BRIDGE.md`)

Only the algebraic implications are formalized. BLV, Gross points, signed Selmer theory and the
witness are NOT formalized. The four source-checked arithmetic inputs enter as explicit hypotheses:

* (I1) exact control: `X/uX ≅ Sel_{p^∞}(E/K)^∨`, τ-compatibly
       (`c`, `hc`, `hker`, `hcσ`; BLV Prop 5.9, Prop 5.3, Cor 5.5).
* (I2) exact specialization length at one `χ : T ↦ a`, `a ∈ pℤ_p`
       (`hexact`; BLV Thm 7.1 equality + Prop 5.9, Prop 5.15, Rem 5.16).
* (I3) τ-equivariant free presentation of `X/pX` and base-layer kernel/cokernel eigenspace equality,
       in ±-graded form (`iA iB πA πB u1 u0`, `harith`; BLV Prop 5.10, 5.13, Poitou–Tate).
* (I4) `rank E(Q) = 2`: Kummer surjection `Sel(E/Q)^∨ ↠ ℤ_p²` whose kernel is `Ш(E/Q)[p^∞]^∨`
       (`κ`, `hκ`), with restriction/corestriction `Sel(E/K)^∨⁺ ≅ Sel(E/Q)^∨` (`ρ`, p odd).

Standard Λ-module structure (not arithmetic) also enters as hypotheses:
* `X` finitely generated over `ℤ_p` (μ = 0); `rank (X/tors) = 2d` (λ(char X) = 2λ(F⁻) = 2d);
* `(T−a)` topologically nilpotent: `(T−a)^n X ⊆ pX` (`hnil`);
* `(I2')` characteristic ideal at `a`: `T−a` injective on `Y = X/tors` and `#(Y/(T−a)Y) = p^e`,
  the same exponent `e = v(F(a)) + v(F(ιa))` as in (I2) (`hinj`, `hchar`; BLV Thm 7.3 + det/index).

The ±-graded form of (I3) is justified by `SignBookkeeping`: the `(-1)`-eigenspace of the involution
induced on `F ⧸ uF` is `F⁻ ⧸ u(F⁺)` (the sign twist of the bridge's §3).
-/

open Submodule LinearMap
open scoped Pointwise TensorProduct

namespace A3Core

/-! ## §2 — elimination of finite `ℤ_p`-torsion -/
section TorsionElimination

variable {p : ℕ} [hp : Fact p.Prime]
variable {X : Type*} [AddCommGroup X] [Module ℤ_[p] X]

lemma torsion_le_comap_torsion (φ : X →ₗ[ℤ_[p]] X) :
    torsion ℤ_[p] X ≤ (torsion ℤ_[p] X).comap φ := by
  intro x hx
  rw [mem_comap]
  obtain ⟨a, ha⟩ := (mem_torsion_iff x).1 hx
  refine (mem_torsion_iff (φ x)).2 ⟨a, ?_⟩
  have h := congrArg φ ha
  rwa [map_zero, Submonoid.smul_def, map_smul, ← Submonoid.smul_def] at h

/-- The endomorphism `φ_Y` of `Y = X ⧸ tors` induced by `φ = T − a`. -/
noncomputable abbrev phiY (φ : X →ₗ[ℤ_[p]] X) :
    (X ⧸ torsion ℤ_[p] X) →ₗ[ℤ_[p]] (X ⧸ torsion ℤ_[p] X) :=
  (torsion ℤ_[p] X).mapQ (torsion ℤ_[p] X) φ (torsion_le_comap_torsion φ)

/-- **§2.** If the exact specialization length of `X` at `T = a` equals the determinant length of
`Y = X/tors` at `T = a`, then `X` has no `ℤ_p`-torsion. -/
theorem torsion_eq_bot_of_exact_lengths [Module.Finite ℤ_[p] X]
    (φ : X →ₗ[ℤ_[p]] X)
    (hnil : ∃ n : ℕ, ∀ x : X, (φ ^ n) x ∈ (p : ℤ_[p]) • (⊤ : Submodule ℤ_[p] X))
    (hinj : Function.Injective (phiY φ))
    (e : ℕ)
    (hexact : Nat.card (X ⧸ LinearMap.range φ) = p ^ e)
    (hchar : Nat.card ((X ⧸ torsion ℤ_[p] X) ⧸ LinearMap.range (phiY φ)) = p ^ e) :
    torsion ℤ_[p] X = ⊥ := by
  set H := torsion ℤ_[p] X with hH
  have hle : LinearMap.range φ ≤ (LinearMap.range (phiY φ)).comap H.mkQ := by
    rintro _ ⟨x, rfl⟩
    exact ⟨H.mkQ x, by simp [phiY]⟩
  set q := (LinearMap.range φ).mapQ (LinearMap.range (phiY φ)) H.mkQ hle with hq_def
  have hq : Function.Surjective q := by
    intro y
    obtain ⟨y', rfl⟩ := Submodule.Quotient.mk_surjective _ y
    obtain ⟨x, rfl⟩ := Submodule.Quotient.mk_surjective _ y'
    exact ⟨Submodule.Quotient.mk x, rfl⟩
  have hcard := Submodule.card_eq_card_quotient_mul_card (LinearMap.ker q)
  have hiso : Nat.card ((X ⧸ LinearMap.range φ) ⧸ LinearMap.ker q) = p ^ e := by
    rw [← hchar]
    exact Nat.card_congr (q.quotKerEquivOfSurjective hq).toEquiv
  rw [hexact, hiso] at hcard
  have hp0 : 0 < p ^ e := pow_pos hp.out.pos e
  have hker1 : Nat.card (LinearMap.ker q) = 1 :=
    Nat.eq_of_mul_eq_mul_right hp0 (by rw [one_mul]; exact hcard.symm)
  have hkerbot : LinearMap.ker q = ⊥ := by
    haveI : Subsingleton (LinearMap.ker q) := (Nat.card_eq_one_iff_unique.mp hker1).1
    exact Submodule.eq_bot_of_subsingleton
  -- torsion ⊆ range φ
  have hH_le_range : H ≤ LinearMap.range φ := by
    intro h hh
    have hmem : (Submodule.Quotient.mk h : X ⧸ LinearMap.range φ) ∈ LinearMap.ker q := by
      rw [LinearMap.mem_ker, hq_def, Submodule.mapQ_apply, Submodule.mkQ_apply,
        (Submodule.Quotient.mk_eq_zero _).2 hh]
      rfl
    rw [hkerbot] at hmem
    exact (Submodule.Quotient.mk_eq_zero _).1 ((Submodule.mem_bot _).1 hmem)
  -- torsion ⊆ φ(torsion), using injectivity of φ on Y
  have hH_le_map : H ≤ H.map φ := by
    intro h hh
    obtain ⟨x, rfl⟩ := hH_le_range hh
    have h0 : phiY φ (H.mkQ x) = 0 := by
      rw [phiY, Submodule.mkQ_apply, Submodule.mapQ_apply]
      exact (Submodule.Quotient.mk_eq_zero _).2 hh
    have hx : H.mkQ x = 0 := hinj (h0.trans (map_zero _).symm)
    exact ⟨x, (Submodule.Quotient.mk_eq_zero _).1 hx, rfl⟩
  have hpow : ∀ n : ℕ, H ≤ H.map (φ ^ n) := by
    intro n
    induction n with
    | zero => simp only [pow_zero, Module.End.one_eq_id, Submodule.map_id, le_refl]
    | succ n ih =>
      rw [pow_succ, Module.End.mul_eq_comp, Submodule.map_comp]
      exact ih.trans (Submodule.map_mono hH_le_map)
  obtain ⟨n, hn⟩ := hnil
  -- torsion ⊆ p · torsion, using that Y is torsion-free
  have hH_le_smul : H ≤ (Ideal.span {(p : ℤ_[p])}) • H := by
    rw [Submodule.ideal_span_singleton_smul]
    intro h hh
    obtain ⟨x, -, rfl⟩ := hpow n hh
    obtain ⟨y, -, hy⟩ := (Submodule.mem_smul_pointwise_iff_exists _ _ _).1 (hn x)
    have hyH : y ∈ H := by
      have hp0' : (p : ℤ_[p]) ≠ 0 := by exact_mod_cast hp.out.ne_zero
      have htors : H.mkQ y ∈ torsion ℤ_[p] (X ⧸ H) := by
        refine (mem_torsion_iff _).2 ⟨⟨(p : ℤ_[p]), mem_nonZeroDivisors_of_ne_zero hp0'⟩, ?_⟩
        rw [Submonoid.smul_def, ← map_smul, hy]
        exact (Submodule.Quotient.mk_eq_zero _).2 hh
      rw [hH, Submodule.QuotientTorsion.torsion_eq_bot] at htors
      exact (Submodule.Quotient.mk_eq_zero _).1 ((Submodule.mem_bot _).1 htors)
    exact (Submodule.mem_smul_pointwise_iff_exists _ _ _).2 ⟨y, hyH, hy⟩
  -- Nakayama over the local ring ℤ_p
  have hfg : H.FG := IsNoetherian.noetherian H
  have hjac : Ideal.span {(p : ℤ_[p])} ≤ (⊥ : Ideal ℤ_[p]).jacobson := by
    rw [IsLocalRing.jacobson_eq_maximalIdeal ⊥ bot_ne_top, PadicInt.maximalIdeal_eq_span_p]
  exact Submodule.eq_bot_of_le_smul_of_le_jacobson_bot _ _ hfg hH_le_smul hjac

/-- **§2, conclusion.** `μ = 0`, `λ(F⁻) = d` and the exact length at one character give
`X ≅ ℤ_p^{2d}`. -/
theorem free_of_rank_of_exact_lengths [Module.Finite ℤ_[p] X]
    (φ : X →ₗ[ℤ_[p]] X)
    (hnil : ∃ n : ℕ, ∀ x : X, (φ ^ n) x ∈ (p : ℤ_[p]) • (⊤ : Submodule ℤ_[p] X))
    (hinj : Function.Injective (phiY φ))
    (e : ℕ)
    (hexact : Nat.card (X ⧸ LinearMap.range φ) = p ^ e)
    (hchar : Nat.card ((X ⧸ torsion ℤ_[p] X) ⧸ LinearMap.range (phiY φ)) = p ^ e)
    (d : ℕ) (hrank : Module.finrank ℤ_[p] (X ⧸ torsion ℤ_[p] X) = 2 * d) :
    Module.Free ℤ_[p] X ∧ Module.finrank ℤ_[p] X = 2 * d := by
  have h := torsion_eq_bot_of_exact_lengths φ hnil hinj e hexact hchar
  haveI : Module.IsTorsionFree ℤ_[p] X := Submodule.isTorsionFree_iff_torsion_eq_bot.mpr h
  refine ⟨Module.free_of_finite_type_torsion_free', ?_⟩
  rw [← hrank]
  exact (LinearEquiv.finrank_eq (Submodule.quotEquivOfEqBot _ h)).symm

end TorsionElimination

/-! ## §3 — balanced τ-eigenspace dimensions, via the graded snake lemma -/
section Balance

variable {k : Type*} [Field k]
variable {A1 B1 A0 B0 P Q : Type*}
  [AddCommGroup A1] [Module k A1] [AddCommGroup B1] [Module k B1]
  [AddCommGroup A0] [Module k A0] [AddCommGroup B0] [Module k B0]
  [AddCommGroup P] [Module k P] [AddCommGroup Q] [Module k Q]

/-- The minus component `B1/u(A1) → B0/u(A0)` of the base-layer map `F1/uF1 → F0/uF0`
(`A = +` parts, `B = −` parts; `u` is odd). -/
noncomputable def ibar (iA : A1 →ₗ[k] A0) (iB : B1 →ₗ[k] B0) (u1 : A1 →ₗ[k] B1)
    (u0 : A0 →ₗ[k] B0) (h1 : u0 ∘ₗ iA = iB ∘ₗ u1) :
    (B1 ⧸ LinearMap.range u1) →ₗ[k] (B0 ⧸ LinearMap.range u0) :=
  (LinearMap.range u1).mapQ (LinearMap.range u0) iB (by
    rintro _ ⟨a, rfl⟩
    exact ⟨iA a, by simpa using congrArg (fun f => f a) h1⟩)

/-- Snake lemma, cokernel end: `coker(ī⁻) ≅ W⁻/U(W⁺)`. -/
theorem finrank_coker_ibar
    (iA : A1 →ₗ[k] A0) (iB : B1 →ₗ[k] B0) (πA : A0 →ₗ[k] P) (πB : B0 →ₗ[k] Q)
    (u1 : A1 →ₗ[k] B1) (u0 : A0 →ₗ[k] B0) (U : P →ₗ[k] Q)
    (hexB : LinearMap.ker πB = LinearMap.range iB)
    (hπA : Function.Surjective πA) (hπB : Function.Surjective πB)
    (h1 : u0 ∘ₗ iA = iB ∘ₗ u1) (h2 : U ∘ₗ πA = πB ∘ₗ u0) :
    Module.finrank k ((B0 ⧸ LinearMap.range u0) ⧸ LinearMap.range (ibar iA iB u1 u0 h1)) =
      Module.finrank k (Q ⧸ LinearMap.range U) := by
  have hc : (ibar iA iB u1 u0 h1) ∘ₗ (LinearMap.range u1).mkQ =
      (LinearMap.range u0).mkQ ∘ₗ iB := Submodule.mapQ_mkQ _ _ _
  have hr : LinearMap.range (ibar iA iB u1 u0 h1) =
      (LinearMap.range iB).map (LinearMap.range u0).mkQ := by
    rw [← LinearMap.range_comp, ← hc,
      LinearMap.range_comp_of_range_eq_top _ (Submodule.range_mkQ _)]
  set Φ : B0 →ₗ[k] Q ⧸ LinearMap.range U := (LinearMap.range U).mkQ ∘ₗ πB with hΦ
  have hΦs : Function.Surjective Φ := (Submodule.mkQ_surjective _).comp hπB
  have hkerΦ : LinearMap.ker Φ = LinearMap.range u0 ⊔ LinearMap.range iB := by
    ext x
    simp only [LinearMap.mem_ker, hΦ, LinearMap.comp_apply, Submodule.mkQ_apply,
      Submodule.Quotient.mk_eq_zero, LinearMap.mem_range, Submodule.mem_sup]
    constructor
    · rintro ⟨w, hw⟩
      obtain ⟨a, rfl⟩ := hπA w
      have h2a : U (πA a) = πB (u0 a) := by simpa using congrArg (fun f => f a) h2
      have hx : x - u0 a ∈ LinearMap.ker πB := by
        rw [LinearMap.mem_ker, map_sub, ← hw, h2a, sub_self]
      rw [hexB] at hx
      obtain ⟨b, hb⟩ := hx
      exact ⟨u0 a, ⟨a, rfl⟩, iB b, ⟨b, rfl⟩, by rw [hb]; abel⟩
    · rintro ⟨y, ⟨a, rfl⟩, z, ⟨b, rfl⟩, rfl⟩
      refine ⟨πA a, ?_⟩
      have h2a : U (πA a) = πB (u0 a) := by simpa using congrArg (fun f => f a) h2
      have hb0 : πB (iB b) = 0 := by
        have hmem : iB b ∈ LinearMap.ker πB := by rw [hexB]; exact ⟨b, rfl⟩
        simpa using hmem
      rw [map_add, hb0, add_zero, h2a]
  have e1 : ((B0 ⧸ LinearMap.range u0) ⧸ LinearMap.range (ibar iA iB u1 u0 h1)) ≃ₗ[k]
      (B0 ⧸ (LinearMap.range u0 ⊔ LinearMap.range iB)) :=
    (Submodule.quotEquivOfEq _ _ hr) ≪≫ₗ Submodule.quotientQuotientEquivQuotientSup _ _
  have e2 : (B0 ⧸ (LinearMap.range u0 ⊔ LinearMap.range iB)) ≃ₗ[k] (Q ⧸ LinearMap.range U) :=
    (Submodule.quotEquivOfEq _ _ hkerΦ.symm) ≪≫ₗ Φ.quotKerEquivOfSurjective hΦs
  exact (e1 ≪≫ₗ e2).finrank_eq

/-- Snake lemma, kernel end: `ker(ī⁻) ≅ W[U]⁺` — the sign twist: the MINUS component of the reduced
presentation sees the PLUS part of `W[U]`. -/
theorem finrank_ker_ibar
    (iA : A1 →ₗ[k] A0) (iB : B1 →ₗ[k] B0) (πA : A0 →ₗ[k] P) (πB : B0 →ₗ[k] Q)
    (u1 : A1 →ₗ[k] B1) (u0 : A0 →ₗ[k] B0) (U : P →ₗ[k] Q)
    (hexA : LinearMap.ker πA = LinearMap.range iA)
    (hexB : LinearMap.ker πB = LinearMap.range iB)
    (hπA : Function.Surjective πA)
    (hiB : Function.Injective iB) (hu0 : Function.Injective u0)
    (h1 : u0 ∘ₗ iA = iB ∘ₗ u1) (h2 : U ∘ₗ πA = πB ∘ₗ u0) :
    Module.finrank k (LinearMap.ker (ibar iA iB u1 u0 h1)) =
      Module.finrank k (LinearMap.ker U) := by
  set S : Submodule k B1 := (LinearMap.range u0).comap iB with hS
  have hc : (ibar iA iB u1 u0 h1) ∘ₗ (LinearMap.range u1).mkQ =
      (LinearMap.range u0).mkQ ∘ₗ iB := Submodule.mapQ_mkQ _ _ _
  have hK : LinearMap.ker (ibar iA iB u1 u0 h1) = S.map (LinearMap.range u1).mkQ := by
    rw [← Submodule.map_comap_eq_of_surjective
      (Submodule.mkQ_surjective (LinearMap.range u1)) (LinearMap.ker (ibar iA iB u1 u0 h1))]
    congr 1
    rw [← LinearMap.ker_comp, hc, LinearMap.ker_comp, Submodule.ker_mkQ]
  set f : S →ₗ[k] (B1 ⧸ LinearMap.range u1) := (LinearMap.range u1).mkQ ∘ₗ S.subtype with hf
  have hrf : LinearMap.range f = LinearMap.ker (ibar iA iB u1 u0 h1) := by
    rw [hK, hf, LinearMap.range_comp, Submodule.range_subtype]
  have hkf : LinearMap.ker f = (LinearMap.range u1).comap S.subtype := by
    rw [hf, LinearMap.ker_comp, Submodule.ker_mkQ]
  -- Ψ₀ : S → A0, b ↦ u0⁻¹(iB b)
  let e0 := LinearEquiv.ofInjective u0 hu0
  let j : S →ₗ[k] LinearMap.range u0 :=
    LinearMap.codRestrict (LinearMap.range u0) (iB ∘ₗ S.subtype) (fun s => s.2)
  let Ψ0 : S →ₗ[k] A0 := e0.symm.toLinearMap ∘ₗ j
  have hΨ0 : ∀ s : S, u0 (Ψ0 s) = iB s := by
    intro s
    have h := LinearEquiv.ofInjective_apply (f := u0) (h := hu0) (e0.symm (j s))
    rw [LinearEquiv.apply_symm_apply] at h
    simpa [Ψ0, j] using h.symm
  have hΨmem : ∀ s : S, (πA ∘ₗ Ψ0) s ∈ LinearMap.ker U := by
    intro s
    rw [LinearMap.mem_ker, LinearMap.comp_apply]
    have h2a : U (πA (Ψ0 s)) = πB (u0 (Ψ0 s)) := by
      simpa using congrArg (fun g => g (Ψ0 s)) h2
    rw [h2a, hΨ0]
    have hmem : iB (s : B1) ∈ LinearMap.ker πB := by rw [hexB]; exact ⟨s, rfl⟩
    exact hmem
  let Ψ : S →ₗ[k] LinearMap.ker U := LinearMap.codRestrict (LinearMap.ker U) (πA ∘ₗ Ψ0) hΨmem
  have hΨs : Function.Surjective Ψ := by
    rintro ⟨w, hw⟩
    obtain ⟨a, rfl⟩ := hπA w
    have h2a : U (πA a) = πB (u0 a) := by simpa using congrArg (fun g => g a) h2
    have hmem : u0 a ∈ LinearMap.ker πB := by
      rw [LinearMap.mem_ker, ← h2a]; exact hw
    rw [hexB] at hmem
    obtain ⟨b, hb⟩ := hmem
    have hbS : b ∈ S := ⟨a, hb.symm⟩
    refine ⟨⟨b, hbS⟩, ?_⟩
    have hΨ0b : Ψ0 ⟨b, hbS⟩ = a := hu0 (by rw [hΨ0]; exact hb)
    apply Subtype.ext
    simp [Ψ, hΨ0b]
  have hkΨ : LinearMap.ker Ψ = LinearMap.ker f := by
    rw [hkf]
    ext s
    simp only [LinearMap.mem_ker, Submodule.mem_comap, Submodule.coe_subtype, LinearMap.mem_range]
    constructor
    · intro hs
      have h0 : πA (Ψ0 s) = 0 := by
        have := congrArg Subtype.val hs
        simpa [Ψ] using this
      have hmem : Ψ0 s ∈ LinearMap.ker πA := h0
      rw [hexA] at hmem
      obtain ⟨a1, ha1⟩ := hmem
      have h1a : u0 (iA a1) = iB (u1 a1) := by simpa using congrArg (fun g => g a1) h1
      refine ⟨a1, hiB ?_⟩
      rw [← h1a, ha1, hΨ0]
    · rintro ⟨a1, ha1⟩
      have h1a : u0 (iA a1) = iB (u1 a1) := by simpa using congrArg (fun g => g a1) h1
      have hΨ0s : Ψ0 s = iA a1 := hu0 (by rw [hΨ0, h1a, ha1])
      apply Subtype.ext
      have hmem : iA a1 ∈ LinearMap.ker πA := by rw [hexA]; exact ⟨a1, rfl⟩
      simpa [Ψ, hΨ0s] using hmem
  calc Module.finrank k (LinearMap.ker (ibar iA iB u1 u0 h1))
      = Module.finrank k (LinearMap.range f) := (LinearEquiv.ofEq _ _ hrf).finrank_eq.symm
    _ = Module.finrank k (S ⧸ LinearMap.ker f) := (f.quotKerEquivRange).finrank_eq.symm
    _ = Module.finrank k (S ⧸ LinearMap.ker Ψ) :=
        (Submodule.quotEquivOfEq _ _ hkΨ.symm).finrank_eq
    _ = Module.finrank k (LinearMap.ker U) := (Ψ.quotKerEquivOfSurjective hΨs).finrank_eq

/-- **§3.** Given the ±-graded free presentation `F1 → F0 → W → 0` (with `u` odd and `u` injective
on `F0`), if the minus component of the base-layer map has kernel and cokernel of equal dimension
(input I3), then `dim W⁺ = dim W⁻`. -/
theorem finrank_eq_of_graded_presentation [FiniteDimensional k P] [FiniteDimensional k Q]
    (iA : A1 →ₗ[k] A0) (iB : B1 →ₗ[k] B0) (πA : A0 →ₗ[k] P) (πB : B0 →ₗ[k] Q)
    (u1 : A1 →ₗ[k] B1) (u0 : A0 →ₗ[k] B0) (U : P →ₗ[k] Q)
    (hexA : LinearMap.ker πA = LinearMap.range iA)
    (hexB : LinearMap.ker πB = LinearMap.range iB)
    (hπA : Function.Surjective πA) (hπB : Function.Surjective πB)
    (hiB : Function.Injective iB) (hu0 : Function.Injective u0)
    (h1 : u0 ∘ₗ iA = iB ∘ₗ u1) (h2 : U ∘ₗ πA = πB ∘ₗ u0)
    (harith : Module.finrank k (LinearMap.ker (ibar iA iB u1 u0 h1)) =
      Module.finrank k ((B0 ⧸ LinearMap.range u0) ⧸ LinearMap.range (ibar iA iB u1 u0 h1))) :
    Module.finrank k P = Module.finrank k Q := by
  have hK := finrank_ker_ibar iA iB πA πB u1 u0 U hexA hexB hπA hiB hu0 h1 h2
  have hC := finrank_coker_ibar iA iB πA πB u1 u0 U hexB hπA hπB h1 h2
  have hU := LinearMap.finrank_range_add_finrank_ker U
  have hQ := Submodule.finrank_quotient_add_finrank (LinearMap.range U)
  omega

end Balance

/-! ## Sign bookkeeping: `(F ⧸ uF)⁻ ≅ F⁻ ⧸ u(F⁺)` -/
section SignBookkeeping

variable {k : Type*} [Field k]
variable {F : Type*} [AddCommGroup F] [Module k F]

/-- `range u ∩ F⁻ = u(F⁺)` when `t` is an involution anticommuting with `u` and `2 ≠ 0`. -/
theorem range_inf_minus_eq_map_plus (h2 : (2 : k) ≠ 0) (t u : F →ₗ[k] F)
    (ht : t ∘ₗ t = LinearMap.id) (htu : t ∘ₗ u = -(u ∘ₗ t)) :
    LinearMap.range u ⊓ LinearMap.ker (t + LinearMap.id) =
      (LinearMap.ker (t - LinearMap.id)).map u := by
  have htt : ∀ x, t (t x) = x := fun x => by simpa using congrArg (fun g => g x) ht
  have htux : ∀ x, t (u x) = -(u (t x)) := fun x => by simpa using congrArg (fun g => g x) htu
  ext y
  simp only [Submodule.mem_inf, LinearMap.mem_range, LinearMap.mem_ker, Submodule.mem_map,
    LinearMap.add_apply, LinearMap.sub_apply, LinearMap.id_apply]
  constructor
  · rintro ⟨⟨x, rfl⟩, hy⟩
    -- x⁺ = (x + t x)/2 ; u x = u x⁺ because u x⁻ ∈ F⁺ ∩ F⁻ = 0
    refine ⟨(2 : k)⁻¹ • (x + t x), ?_, ?_⟩
    · rw [map_smul, map_add, htt, add_comm (t x) x, sub_self]
    · -- hy : t (u x) + u x = 0
      have hux : u (t x) = u x := by
        have := htux x
        rw [this] at hy
        exact neg_add_eq_zero.mp hy
      rw [map_smul, map_add, hux, ← two_smul k (u x), smul_smul, inv_mul_cancel₀ h2, one_smul]
  · rintro ⟨x, hx, rfl⟩
    have hx' : t x = x := sub_eq_zero.mp hx
    exact ⟨⟨x, rfl⟩, by rw [htux, hx', neg_add_cancel]⟩

/-- The involution induced by `t` on `F ⧸ uF`. -/
noncomputable def tbar (t u : F →ₗ[k] F) (htu : t ∘ₗ u = -(u ∘ₗ t)) :
    (F ⧸ LinearMap.range u) →ₗ[k] (F ⧸ LinearMap.range u) :=
  (LinearMap.range u).mapQ (LinearMap.range u) t (by
    rintro _ ⟨x, rfl⟩
    refine ⟨-(t x), ?_⟩
    have := congrArg (fun g => g x) htu
    simp only [LinearMap.comp_apply, LinearMap.neg_apply] at this
    rw [map_neg, this] )

/-- **Sign bookkeeping.** The `(-1)`-eigenspace of the involution induced on `F ⧸ uF` is
`F⁻ ⧸ (range u ∩ F⁻)`, i.e. `F⁻ ⧸ u(F⁺)` by `range_inf_minus_eq_map_plus`. -/
noncomputable def minusOfQuotientEquiv (h2 : (2 : k) ≠ 0) (t u : F →ₗ[k] F)
    (ht : t ∘ₗ t = LinearMap.id) (htu : t ∘ₗ u = -(u ∘ₗ t)) :
    (LinearMap.ker (t + LinearMap.id) ⧸
        (LinearMap.range u).comap (LinearMap.ker (t + LinearMap.id)).subtype) ≃ₗ[k]
      LinearMap.ker (tbar t u htu + LinearMap.id) := by
  have htt : ∀ x, t (t x) = x := fun x => by simpa using congrArg (fun g => g x) ht
  let Fm := LinearMap.ker (t + LinearMap.id)
  have hmaps : ∀ x : Fm, (LinearMap.range u).mkQ (x : F) ∈
      LinearMap.ker (tbar t u htu + LinearMap.id) := by
    intro x
    have hx : t x + x = 0 := x.2
    rw [LinearMap.mem_ker, LinearMap.add_apply, LinearMap.id_apply, Submodule.mkQ_apply, tbar,
      Submodule.mapQ_apply, ← Submodule.Quotient.mk_add, hx, Submodule.Quotient.mk_zero]
  let g : Fm →ₗ[k] LinearMap.ker (tbar t u htu + LinearMap.id) :=
    LinearMap.codRestrict _ ((LinearMap.range u).mkQ ∘ₗ Fm.subtype) hmaps
  have hg : Function.Surjective g := by
    rintro ⟨ybar, hy⟩
    obtain ⟨y, rfl⟩ := Submodule.Quotient.mk_surjective _ ybar
    have hy' : Submodule.Quotient.mk (t y + y) = (0 : F ⧸ LinearMap.range u) := by
      have := hy
      rw [LinearMap.mem_ker, LinearMap.add_apply, LinearMap.id_apply, tbar,
        Submodule.mapQ_apply] at this
      rw [Submodule.Quotient.mk_add]; exact this
    -- v = (y - t y)/2 ∈ F⁻ and mk v = mk y
    let v : F := (2 : k)⁻¹ • (y - t y)
    have hv : v ∈ Fm := by
      show t v + v = 0
      simp only [v, map_smul, map_sub, htt]
      rw [← smul_add]; simp
    refine ⟨⟨v, hv⟩, ?_⟩
    apply Subtype.ext
    simp only [g, LinearMap.codRestrict_apply, LinearMap.comp_apply, Submodule.coe_subtype,
      Submodule.mkQ_apply]
    -- mk v = mk y  ⟸  y - v = (t y + y)/2 ∈ range u
    rw [eq_comm, ← sub_eq_zero, ← Submodule.Quotient.mk_sub, Submodule.Quotient.mk_eq_zero]
    have hmem : t y + y ∈ LinearMap.range u := (Submodule.Quotient.mk_eq_zero _).1 hy'
    have : y - v = (2 : k)⁻¹ • (t y + y) := by
      have key : (2 : k) • (y - v) = (2 : k) • ((2 : k)⁻¹ • (t y + y)) := by
        rw [smul_smul, mul_inv_cancel₀ h2, one_smul]
        simp only [v]
        rw [smul_sub, smul_smul, mul_inv_cancel₀ h2, one_smul, two_smul]
        abel
      exact smul_right_injective F h2 key
    rw [this]
    exact Submodule.smul_mem _ _ hmem
  have hkg : LinearMap.ker g = (LinearMap.range u).comap Fm.subtype := by
    ext x
    simp only [LinearMap.mem_ker, Submodule.mem_comap, Submodule.coe_subtype]
    constructor
    · intro hx
      have := congrArg Subtype.val hx
      simpa [g] using this
    · intro hx
      apply Subtype.ext
      simpa [g] using hx
  exact (Submodule.quotEquivOfEq _ _ hkg.symm) ≪≫ₗ g.quotKerEquivOfSurjective hg

/-- `u` restricted `F⁺ → F⁻`. -/
noncomputable def uPlusK (t u : F →ₗ[k] F) (htu : t ∘ₗ u = -(u ∘ₗ t)) :
    LinearMap.ker (t - LinearMap.id) →ₗ[k] LinearMap.ker (t + LinearMap.id) :=
  LinearMap.codRestrict _ (u ∘ₗ (LinearMap.ker (t - LinearMap.id)).subtype) (fun x => by
    have hx : t x - x = 0 := x.2
    have h := congrArg (fun g => g (x : F)) htu
    simp only [LinearMap.comp_apply, LinearMap.neg_apply] at h
    rw [LinearMap.mem_ker, LinearMap.add_apply, LinearMap.id_apply, LinearMap.comp_apply,
      Submodule.coe_subtype, h, sub_eq_zero.mp hx, neg_add_cancel])

/-- Inside `F⁻`, the submodule killed in `F⁻ → (F ⧸ uF)⁻` is exactly `u(F⁺)`. -/
theorem range_uPlusK (h2 : (2 : k) ≠ 0) (t u : F →ₗ[k] F)
    (ht : t ∘ₗ t = LinearMap.id) (htu : t ∘ₗ u = -(u ∘ₗ t)) :
    LinearMap.range (uPlusK t u htu) =
      (LinearMap.range u).comap (LinearMap.ker (t + LinearMap.id)).subtype := by
  have hrm := range_inf_minus_eq_map_plus h2 t u ht htu
  ext y
  simp only [Submodule.mem_comap, Submodule.coe_subtype]
  constructor
  · rintro ⟨x, rfl⟩
    exact ⟨x, rfl⟩
  · intro hy
    have hy' : (y : F) ∈ LinearMap.range u ⊓ LinearMap.ker (t + LinearMap.id) := ⟨hy, y.2⟩
    rw [hrm] at hy'
    obtain ⟨x, hx, hxy⟩ := hy'
    exact ⟨⟨x, hx⟩, Subtype.ext hxy⟩

/-- **Sign bookkeeping, final form.** `(F ⧸ uF)⁻ ≅ F⁻ ⧸ u(F⁺)`: the minus eigenspace of the
reduction mod `u` is the MINUS part modulo `u` applied to the PLUS part. This is the source/target
of `ibar` in the graded presentation. -/
noncomputable def minusOfQuotientEquiv' (h2 : (2 : k) ≠ 0) (t u : F →ₗ[k] F)
    (ht : t ∘ₗ t = LinearMap.id) (htu : t ∘ₗ u = -(u ∘ₗ t)) :
    (LinearMap.ker (t + LinearMap.id) ⧸ LinearMap.range (uPlusK t u htu)) ≃ₗ[k]
      LinearMap.ker (tbar t u htu + LinearMap.id) :=
  (Submodule.quotEquivOfEq _ _ (range_uPlusK h2 t u ht htu)) ≪≫ₗ
    minusOfQuotientEquiv h2 t u ht htu

end SignBookkeeping

/-! ## §4 — rank two forces `Ш(E/Q)[p^∞] = 0`; and `d ≥ 2` -/
section RankTwo

variable {p : ℕ} [hp : Fact p.Prime]
variable {X SK SQ : Type*} [AddCommGroup X] [Module ℤ_[p] X]
  [AddCommGroup SK] [Module ℤ_[p] SK] [AddCommGroup SQ] [Module ℤ_[p] SQ]

/-- `X⁺`, the `τ = +1` eigenspace. -/
noncomputable abbrev plusPart (τ : X →ₗ[ℤ_[p]] X) : Submodule ℤ_[p] X := LinearMap.ker (τ - LinearMap.id)

/-- The composite `X⁺ → (X/uX)⁺ ≅ (Sel(E/K)^∨)⁺ ≅ Sel(E/Q)^∨`. -/
noncomputable def plusToSelQ (τ : X →ₗ[ℤ_[p]] X) (c : X →ₗ[ℤ_[p]] SK) (σ : SK →ₗ[ℤ_[p]] SK)
    (hcσ : c ∘ₗ τ = σ ∘ₗ c) (ρ : LinearMap.ker (σ - LinearMap.id) ≃ₗ[ℤ_[p]] SQ) :
    plusPart τ →ₗ[ℤ_[p]] SQ :=
  ρ.toLinearMap ∘ₗ LinearMap.codRestrict (LinearMap.ker (σ - LinearMap.id))
    (c ∘ₗ (plusPart τ).subtype) (fun x => by
      have hx : τ x - x = 0 := x.2
      rw [LinearMap.mem_ker, LinearMap.sub_apply, LinearMap.id_apply, LinearMap.comp_apply,
        Submodule.coe_subtype]
      have h := congrArg (fun g => g (x : X)) hcσ
      simp only [LinearMap.comp_apply] at h
      rw [← h, sub_eq_zero.mp hx, sub_self])

theorem plusToSelQ_surjective (h2 : IsUnit (2 : ℤ_[p]))
    (τ : X →ₗ[ℤ_[p]] X) (hτ : τ ∘ₗ τ = LinearMap.id)
    (c : X →ₗ[ℤ_[p]] SK) (hc : Function.Surjective c)
    (σ : SK →ₗ[ℤ_[p]] SK) (hcσ : c ∘ₗ τ = σ ∘ₗ c)
    (ρ : LinearMap.ker (σ - LinearMap.id) ≃ₗ[ℤ_[p]] SQ) :
    Function.Surjective (plusToSelQ τ c σ hcσ ρ) := by
  have hττ : ∀ x, τ (τ x) = x := fun x => by simpa using congrArg (fun g => g x) hτ
  intro s
  obtain ⟨⟨y, hy⟩, rfl⟩ := ρ.surjective s
  have hy' : σ y = y := sub_eq_zero.mp hy
  obtain ⟨x, rfl⟩ := hc y
  obtain ⟨v, hv⟩ := h2
  let x' : X := ((v⁻¹ : ℤ_[p]ˣ) : ℤ_[p]) • (x + τ x)
  have hx' : x' ∈ plusPart τ := by
    show τ x' - x' = 0
    simp only [x', map_smul, map_add, hττ]
    rw [add_comm (τ x) x, sub_self]
  refine ⟨⟨x', hx'⟩, congrArg ρ (Subtype.ext ?_)⟩
  show c x' = c x
  have hcτ : c (τ x) = σ (c x) := by simpa using congrArg (fun g => g x) hcσ
  simp only [x']
  rw [map_smul, map_add, hcτ, hy', ← two_smul ℤ_[p] (c x), ← hv, smul_smul, Units.inv_mul,
    one_smul]

/-- **§4, `d ≥ 2`.** -/
theorem two_le_finrank_plus [Module.Finite ℤ_[p] X] (h2 : IsUnit (2 : ℤ_[p]))
    (τ : X →ₗ[ℤ_[p]] X) (hτ : τ ∘ₗ τ = LinearMap.id)
    (c : X →ₗ[ℤ_[p]] SK) (hc : Function.Surjective c)
    (σ : SK →ₗ[ℤ_[p]] SK) (hcσ : c ∘ₗ τ = σ ∘ₗ c)
    (ρ : LinearMap.ker (σ - LinearMap.id) ≃ₗ[ℤ_[p]] SQ)
    (κ : SQ →ₗ[ℤ_[p]] (Fin 2 → ℤ_[p])) (hκ : Function.Surjective κ) :
    2 ≤ Module.finrank ℤ_[p] (plusPart τ) := by
  have hg : Function.Surjective (κ ∘ₗ plusToSelQ τ c σ hcσ ρ) :=
    hκ.comp (plusToSelQ_surjective h2 τ hτ c hc σ hcσ ρ)
  have h := LinearMap.finrank_le_finrank_of_surjective hg
  simpa using h

/-- **§4, `d = 2 ⇒ Ш(E/Q)[p^∞]^∨ = 0`** (and the kernel of `X⁺ → Sel(E/Q)^∨` vanishes). -/
theorem sha_dual_eq_bot_of_finrank_plus_eq_two [Module.Finite ℤ_[p] X]
    (h2 : IsUnit (2 : ℤ_[p]))
    (τ : X →ₗ[ℤ_[p]] X) [Module.Free ℤ_[p] (plusPart τ)] (hτ : τ ∘ₗ τ = LinearMap.id)
    (c : X →ₗ[ℤ_[p]] SK) (hc : Function.Surjective c)
    (σ : SK →ₗ[ℤ_[p]] SK) (hcσ : c ∘ₗ τ = σ ∘ₗ c)
    (ρ : LinearMap.ker (σ - LinearMap.id) ≃ₗ[ℤ_[p]] SQ)
    (κ : SQ →ₗ[ℤ_[p]] (Fin 2 → ℤ_[p])) (hκ : Function.Surjective κ)
    (hd : Module.finrank ℤ_[p] (plusPart τ) = 2) :
    LinearMap.ker κ = ⊥ := by
  set f := plusToSelQ τ c σ hcσ ρ with hf
  have hfs : Function.Surjective f := plusToSelQ_surjective h2 τ hτ c hc σ hcσ ρ
  set g := κ ∘ₗ f with hg_def
  have hg : Function.Surjective g := hκ.comp hfs
  let b := Module.finBasisOfFinrankEq ℤ_[p] (plusPart τ) hd
  let e := b.equivFun
  have hinj : Function.Injective g := by
    have hs : Function.Surjective (g ∘ₗ e.symm.toLinearMap) := hg.comp e.symm.surjective
    have hi := OrzechProperty.injective_of_surjective_endomorphism _ hs
    intro x y hxy
    have : (g ∘ₗ e.symm.toLinearMap) (e x) = (g ∘ₗ e.symm.toLinearMap) (e y) := by
      simpa using hxy
    exact e.injective (hi this)
  rw [eq_bot_iff]
  intro s hs
  obtain ⟨x, rfl⟩ := hfs s
  have hgx : g x = g 0 := by
    rw [map_zero, hg_def, LinearMap.comp_apply]; exact hs
  rw [hinj hgx, map_zero]
  exact Submodule.zero_mem _

end RankTwo

/-! ## `d ≥ 2 ⇒ b̄₁ = 0 ⇒ M₁ = 0` -/
section LinearCoefficient

variable {k : Type*} [Field k]

theorem coeff_one_eq_zero_of_two_le_order (F : PowerSeries k)
    (h : F ≠ 0 → (2 : ℕ∞) ≤ F.order) : PowerSeries.coeff 1 F = 0 := by
  by_cases hF : F = 0
  · simp [hF]
  · exact PowerSeries.coeff_of_lt_order 1 (lt_of_lt_of_le (by norm_num) (h hF))

/-- With the first-layer normalization `b̄₁ = Σ_j j·v_j` (BLV §4.3 at `n = 1`; handled elsewhere),
`d ≥ 2` gives `M₁ = 0`. -/
theorem M1_eq_zero (F : PowerSeries k) (p : ℕ) (v : ℕ → k)
    (hnorm : PowerSeries.coeff 1 F = ∑ j ∈ Finset.range p, (j : k) * v j)
    (h : F ≠ 0 → (2 : ℕ∞) ≤ F.order) :
    ∑ j ∈ Finset.range p, (j : k) * v j = 0 := by
  rw [← hnorm]; exact coeff_one_eq_zero_of_two_le_order F h

/-- `b̄₀ = b̄₁ = 0` and `b̄₂ ≠ 0` give `ord_T F̄ = 2`. -/
theorem order_eq_two (F : PowerSeries k) (h0 : PowerSeries.coeff 0 F = 0)
    (h1 : PowerSeries.coeff 1 F = 0) (h2 : PowerSeries.coeff 2 F ≠ 0) : F.order = 2 := by
  have := (PowerSeries.order_eq_nat (φ := F) (n := 2)).2 ⟨h2, fun i hi => by
    interval_cases i <;> assumption⟩
  exact_mod_cast this

end LinearCoefficient

/-! ## Capstone — the chain §2 → §3 → §4, with `rank X⁺ = rank X⁻ = d` over `ℤ_p` -/
section Capstone

variable {p : ℕ} [hp : Fact p.Prime]
variable {X SK SQ : Type*} [AddCommGroup X] [Module ℤ_[p] X]
  [AddCommGroup SK] [Module ℤ_[p] SK] [AddCommGroup SQ] [Module ℤ_[p] SQ]

/-- `X⁻`, the `τ = −1` eigenspace. -/
noncomputable abbrev minusPart (τ : X →ₗ[ℤ_[p]] X) : Submodule ℤ_[p] X :=
  LinearMap.ker (τ + LinearMap.id)

/-- `u` restricted `X⁺ → X⁻` (u is odd: `τu = −uτ`). -/
noncomputable def uPlus (τ u : X →ₗ[ℤ_[p]] X) (hτu : τ ∘ₗ u = -(u ∘ₗ τ)) :
    plusPart τ →ₗ[ℤ_[p]] minusPart τ :=
  LinearMap.codRestrict (minusPart τ) (u ∘ₗ (plusPart τ).subtype) (fun x => by
    have hx : τ x - x = 0 := x.2
    have h := congrArg (fun g => g (x : X)) hτu
    simp only [LinearMap.comp_apply, LinearMap.neg_apply] at h
    rw [LinearMap.mem_ker, LinearMap.add_apply, LinearMap.id_apply, LinearMap.comp_apply,
      Submodule.coe_subtype, h, sub_eq_zero.mp hx, neg_add_cancel])

lemma torsion_submodule_eq_bot {R M : Type*} [CommRing R] [AddCommGroup M] [Module R M]
    (h : torsion R M = ⊥) (N : Submodule R M) : torsion R N = ⊥ := by
  rw [eq_bot_iff]
  intro x hx
  obtain ⟨a, ha⟩ := (mem_torsion_iff x).1 hx
  have hmem : (x : M) ∈ torsion R M := (mem_torsion_iff _).2 ⟨a, by
    have := congrArg Subtype.val ha
    simpa using this⟩
  rw [h] at hmem
  rw [Submodule.mem_bot] at hmem ⊢
  exact Subtype.ext hmem

lemma free_of_submodule [Module.Finite ℤ_[p] X] (htf : torsion ℤ_[p] X = ⊥)
    (N : Submodule ℤ_[p] X) : Module.Free ℤ_[p] N := by
  haveI : Module.IsTorsionFree ℤ_[p] N :=
    Submodule.isTorsionFree_iff_torsion_eq_bot.mpr (torsion_submodule_eq_bot htf N)
  exact Module.free_of_finite_type_torsion_free'

lemma isCompl_plus_minus (h2 : IsUnit (2 : ℤ_[p])) (τ : X →ₗ[ℤ_[p]] X)
    (hτ : τ ∘ₗ τ = LinearMap.id) : IsCompl (plusPart τ) (minusPart τ) := by
  have hττ : ∀ x, τ (τ x) = x := fun x => by simpa using congrArg (fun g => g x) hτ
  obtain ⟨v, hv⟩ := h2
  constructor
  · rw [Submodule.disjoint_def]
    intro x hx1 hx2
    have e1 : τ x - x = 0 := hx1
    have e2 : τ x + x = 0 := hx2
    have h2x : (2 : ℤ_[p]) • x = 0 := by
      rw [two_smul]; rw [sub_eq_zero.mp e1] at e2; exact e2
    rw [← hv] at h2x
    have := congrArg (fun y => ((v⁻¹ : ℤ_[p]ˣ) : ℤ_[p]) • y) h2x
    simpa [smul_smul] using this
  · rw [codisjoint_iff, eq_top_iff]
    intro x _
    have hx : x = ((v⁻¹ : ℤ_[p]ˣ) : ℤ_[p]) • (x + τ x) + ((v⁻¹ : ℤ_[p]ˣ) : ℤ_[p]) • (x - τ x) := by
      rw [← smul_add, show x + τ x + (x - τ x) = (2 : ℤ_[p]) • x by rw [two_smul]; abel, ← hv,
        smul_smul, Units.inv_mul, one_smul]
    rw [hx]
    apply Submodule.add_mem_sup
    · rw [LinearMap.mem_ker, LinearMap.sub_apply, map_smul, map_add, hττ, LinearMap.id_apply,
        add_comm (τ x) x, sub_self]
    · rw [LinearMap.mem_ker, LinearMap.add_apply, map_smul, map_sub, hττ, LinearMap.id_apply,
        ← smul_add, show τ x - x + (x - τ x) = 0 by abel, smul_zero]

lemma finrank_plus_add_minus [Module.Finite ℤ_[p] X] (htf : torsion ℤ_[p] X = ⊥)
    (h2 : IsUnit (2 : ℤ_[p])) (τ : X →ₗ[ℤ_[p]] X) (hτ : τ ∘ₗ τ = LinearMap.id) :
    Module.finrank ℤ_[p] (plusPart τ) + Module.finrank ℤ_[p] (minusPart τ) =
      Module.finrank ℤ_[p] X := by
  haveI := free_of_submodule htf (plusPart τ)
  haveI := free_of_submodule htf (minusPart τ)
  rw [← Module.finrank_prod]
  exact (Submodule.prodEquivOfIsCompl _ _ (isCompl_plus_minus h2 τ hτ)).finrank_eq

local notation "𝕜" => IsLocalRing.ResidueField ℤ_[p]

/-- **§3 over `ℤ_p`.** The graded presentation of `X/pX = 𝕜 ⊗ X = (𝕜 ⊗ X⁺) ⊕ (𝕜 ⊗ X⁻)` with the
arithmetic eigenspace equality gives `rank X⁺ = rank X⁻`. -/
theorem finrank_plus_eq_minus_of_presentation [Module.Finite ℤ_[p] X]
    (htf : torsion ℤ_[p] X = ⊥)
    (τ u : X →ₗ[ℤ_[p]] X) (hτu : τ ∘ₗ u = -(u ∘ₗ τ))
    {A1 B1 A0 B0 : Type*}
    [AddCommGroup A1] [Module 𝕜 A1] [AddCommGroup B1] [Module 𝕜 B1]
    [AddCommGroup A0] [Module 𝕜 A0] [AddCommGroup B0] [Module 𝕜 B0]
    (iA : A1 →ₗ[𝕜] A0) (iB : B1 →ₗ[𝕜] B0)
    (πA : A0 →ₗ[𝕜] 𝕜 ⊗[ℤ_[p]] plusPart τ) (πB : B0 →ₗ[𝕜] 𝕜 ⊗[ℤ_[p]] minusPart τ)
    (u1 : A1 →ₗ[𝕜] B1) (u0 : A0 →ₗ[𝕜] B0)
    (hexA : LinearMap.ker πA = LinearMap.range iA)
    (hexB : LinearMap.ker πB = LinearMap.range iB)
    (hπA : Function.Surjective πA) (hπB : Function.Surjective πB)
    (hiB : Function.Injective iB) (hu0 : Function.Injective u0)
    (h1 : u0 ∘ₗ iA = iB ∘ₗ u1)
    (hcomm2 : ((uPlus τ u hτu).baseChange 𝕜) ∘ₗ πA = πB ∘ₗ u0)
    (harith : Module.finrank 𝕜 (LinearMap.ker (ibar iA iB u1 u0 h1)) =
      Module.finrank 𝕜 ((B0 ⧸ LinearMap.range u0) ⧸ LinearMap.range (ibar iA iB u1 u0 h1))) :
    Module.finrank ℤ_[p] (plusPart τ) = Module.finrank ℤ_[p] (minusPart τ) := by
  haveI := free_of_submodule htf (plusPart τ)
  haveI := free_of_submodule htf (minusPart τ)
  have h := finrank_eq_of_graded_presentation iA iB πA πB u1 u0 ((uPlus τ u hτu).baseChange 𝕜)
    hexA hexB hπA hπB hiB hu0 h1 hcomm2 harith
  rwa [Module.finrank_baseChange, Module.finrank_baseChange] at h

/-- **The A3 bridge, algebraic core.** From the four arithmetic inputs (as hypotheses) and the
standard Λ-module structure: `X ≅ ℤ_p^{2d}`; `rank X⁺ = rank X⁻ = d`; `d ≥ 2`;
`d = 2 ⇒ Ш(E/Q)[p^∞]^∨ = 0`; `b̄₁ = 0`; and `b̄₂ ≠ 0 ⇒ Ш(E/Q)[p^∞]^∨ = 0`. -/
theorem A3_bridge_core (hp2 : p ≠ 2) [Module.Finite ℤ_[p] X]
    -- §2: φ = T − a
    (φ : X →ₗ[ℤ_[p]] X)
    (hnil : ∃ n : ℕ, ∀ x : X, (φ ^ n) x ∈ (p : ℤ_[p]) • (⊤ : Submodule ℤ_[p] X))
    (hinj : Function.Injective (phiY φ)) (e : ℕ)
    (hexact : Nat.card (X ⧸ LinearMap.range φ) = p ^ e)
    (hchar : Nat.card ((X ⧸ torsion ℤ_[p] X) ⧸ LinearMap.range (phiY φ)) = p ^ e)
    (d : ℕ) (hrank : Module.finrank ℤ_[p] (X ⧸ torsion ℤ_[p] X) = 2 * d)
    -- complex conjugation and u = γ − γ⁻¹
    (τ u : X →ₗ[ℤ_[p]] X) (hτ : τ ∘ₗ τ = LinearMap.id) (hτu : τ ∘ₗ u = -(u ∘ₗ τ))
    -- §3: graded presentation (I3)
    {A1 B1 A0 B0 : Type*}
    [AddCommGroup A1] [Module 𝕜 A1] [AddCommGroup B1] [Module 𝕜 B1]
    [AddCommGroup A0] [Module 𝕜 A0] [AddCommGroup B0] [Module 𝕜 B0]
    (iA : A1 →ₗ[𝕜] A0) (iB : B1 →ₗ[𝕜] B0)
    (πA : A0 →ₗ[𝕜] 𝕜 ⊗[ℤ_[p]] plusPart τ) (πB : B0 →ₗ[𝕜] 𝕜 ⊗[ℤ_[p]] minusPart τ)
    (u1 : A1 →ₗ[𝕜] B1) (u0 : A0 →ₗ[𝕜] B0)
    (hexA : LinearMap.ker πA = LinearMap.range iA)
    (hexB : LinearMap.ker πB = LinearMap.range iB)
    (hπA : Function.Surjective πA) (hπB : Function.Surjective πB)
    (hiB : Function.Injective iB) (hu0 : Function.Injective u0)
    (h1 : u0 ∘ₗ iA = iB ∘ₗ u1)
    (hcomm2 : ((uPlus τ u hτu).baseChange 𝕜) ∘ₗ πA = πB ∘ₗ u0)
    (harith : Module.finrank 𝕜 (LinearMap.ker (ibar iA iB u1 u0 h1)) =
      Module.finrank 𝕜 ((B0 ⧸ LinearMap.range u0) ⧸ LinearMap.range (ibar iA iB u1 u0 h1)))
    -- §4: control (I1), restriction/corestriction, Kummer with rank E(Q) = 2 (I4)
    (c : X →ₗ[ℤ_[p]] SK) (hc : Function.Surjective c)
    (σ : SK →ₗ[ℤ_[p]] SK) (hcσ : c ∘ₗ τ = σ ∘ₗ c)
    (ρ : LinearMap.ker (σ - LinearMap.id) ≃ₗ[ℤ_[p]] SQ)
    (κ : SQ →ₗ[ℤ_[p]] (Fin 2 → ℤ_[p])) (hκ : Function.Surjective κ)
    -- the minus square-root series mod p: `order = d < ∞` encodes μ = 0 and λ = d
    (Fbar : PowerSeries (ZMod p)) (hlam : Fbar.order = d) :
    (Module.Free ℤ_[p] X ∧ Module.finrank ℤ_[p] X = 2 * d) ∧
    (Module.finrank ℤ_[p] (plusPart τ) = d ∧ Module.finrank ℤ_[p] (minusPart τ) = d) ∧
    2 ≤ d ∧
    (d = 2 → LinearMap.ker κ = ⊥) ∧
    PowerSeries.coeff 1 Fbar = 0 ∧
    (∀ v : ℕ → ZMod p, PowerSeries.coeff 1 Fbar = ∑ j ∈ Finset.range p, (j : ZMod p) * v j →
      ∑ j ∈ Finset.range p, (j : ZMod p) * v j = 0) ∧
    (PowerSeries.coeff 2 Fbar ≠ 0 → LinearMap.ker κ = ⊥) := by
  have h2unit : IsUnit (2 : ℤ_[p]) := by
    rw [PadicInt.isUnit_iff]
    have := (PadicInt.norm_natCast_eq_one_iff (p := p) (n := 2)).mpr
      ((Nat.coprime_primes hp.out Nat.prime_two).mpr hp2)
    simpa using this
  have hA := free_of_rank_of_exact_lengths φ hnil hinj e hexact hchar d hrank
  have htf := torsion_eq_bot_of_exact_lengths φ hnil hinj e hexact hchar
  have hbal := finrank_plus_eq_minus_of_presentation htf τ u hτu iA iB πA πB u1 u0
    hexA hexB hπA hπB hiB hu0 h1 hcomm2 harith
  have hsum := finrank_plus_add_minus htf h2unit τ hτ
  have hplus : Module.finrank ℤ_[p] (plusPart τ) = d := by omega
  have hminus : Module.finrank ℤ_[p] (minusPart τ) = d := by omega
  have hd2 : 2 ≤ d := hplus ▸ two_le_finrank_plus h2unit τ hτ c hc σ hcσ ρ κ hκ
  have hsha : d = 2 → LinearMap.ker κ = ⊥ := by
    intro hd
    haveI := free_of_submodule htf (plusPart τ)
    exact sha_dual_eq_bot_of_finrank_plus_eq_two h2unit τ hτ c hc σ hcσ ρ κ hκ (by omega)
  have hord : (2 : ℕ∞) ≤ Fbar.order := by rw [hlam]; exact_mod_cast hd2
  have hb1 : PowerSeries.coeff 1 Fbar = 0 := coeff_one_eq_zero_of_two_le_order Fbar (fun _ => hord)
  refine ⟨hA, ⟨hplus, hminus⟩, hd2, hsha, hb1,
    fun v hnorm => M1_eq_zero Fbar p v hnorm (fun _ => hord), fun hb2 => hsha ?_⟩
  have hb0 : PowerSeries.coeff 0 Fbar = 0 :=
    PowerSeries.coeff_of_lt_order 0 (lt_of_lt_of_le (by norm_num) hord)
  have h2ord := order_eq_two Fbar hb0 hb1 hb2
  rw [hlam] at h2ord
  exact_mod_cast h2ord

end Capstone

end A3Core

#print axioms A3Core.free_of_rank_of_exact_lengths
#print axioms A3Core.finrank_eq_of_graded_presentation
#print axioms A3Core.minusOfQuotientEquiv
#print axioms A3Core.minusOfQuotientEquiv'
#print axioms A3Core.range_inf_minus_eq_map_plus
#print axioms A3Core.two_le_finrank_plus
#print axioms A3Core.sha_dual_eq_bot_of_finrank_plus_eq_two
#print axioms A3Core.M1_eq_zero
#print axioms A3Core.order_eq_two
#print axioms A3Core.finrank_plus_eq_minus_of_presentation
#print axioms A3Core.A3_bridge_core
