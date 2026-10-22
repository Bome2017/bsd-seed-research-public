# A3 capstone signature and input correspondence

The following is copied verbatim from the retained Lean source (SHA-256 `f7a3c861c998f99630a46a9c988e41554ef630d46fdfbbe7f90383a4bf7f24ca`). Its imported types and definitions are in that file; the four arithmetic and four structural input groups are mapped in the signed-bridge appendix, and in the retained REPORT.md. No input is promoted by this transcription.

```lean
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
    (PowerSeries.coeff 2 Fbar ≠ 0 → LinearMap.ker κ = ⊥)
```
