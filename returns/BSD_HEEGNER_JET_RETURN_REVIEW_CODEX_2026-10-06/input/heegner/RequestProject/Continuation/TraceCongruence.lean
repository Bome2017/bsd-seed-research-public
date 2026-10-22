module

public import Mathlib
public import RequestProject.Continuation.CrossPrimeKolyvagin
public import RequestProject.Continuation.SeedPointCounts

/-!
# Derived-point invariance without `a_ℓ = 0`, and finite checks for the `p = 53` application

New Lean source for the second 2026-10-06 continuation (see `research_return/REVISION_2.md`).

* `derived_invariance_trace`: if `σ ^ m = 1` and `Tr y = a • y₁` (the Heegner norm relation
  `Tr_{H_ℓ/H_1} y_ℓ = a_ℓ y_1`), then `σ (D y) - D y = m • y - a • y₁`.
* `derived_invariance_mod_common`: hence, for every `d` dividing both `m = ℓ + 1` and `a = a_ℓ`,
  the difference lies in `d • M`. The divisor `M_ℓ = gcd(a_ℓ, ℓ + 1)` therefore works for all
  its prime factors at once; exact `a_ℓ = 0` is not needed.
* `reduced_target_iff`: the elementary bookkeeping `h = 2 + s - t`, `t ≤ 1`, `s` even, gives
  `h ≤ 2 ↔ s = 0`.
* Finite seed facts used in the concrete application at `p = 53`: `a_53 = -6` (so `53` is
  good ordinary), `a_29 = 0` (so `29` is supersingular and outside the authenticated domain),
  the minimal discriminant from `c₄, c₆`, and the residues of the multiplicative primes
  modulo `53`.
-/

@[expose] public section

namespace Continuation.TraceCongruence

open Finset Continuation.CrossPrime

/-- **Derived-point identity with a nonzero trace.** If `σ ^ m = 1` and the trace of `y` equals
`a • y₁`, then `σ (D y) - D y = m • y - a • y₁`. -/
theorem derived_invariance_trace {M : Type*} [AddCommGroup M] (σ : AddMonoid.End M) (m : ℕ)
    (hσ : σ ^ m = 1) (y y₁ : M) (a : ℤ) (htr : ∑ j ∈ range m, (σ ^ j) y = a • y₁) :
    σ (kolyvaginD σ m y) - kolyvaginD σ m y = (m : ℤ) • y - a • y₁ := by
  have h := congrArg (fun f : AddMonoid.End M => f y) (derivative_relation σ m hσ)
  have e1 : ((σ - 1) * kolyvaginD σ m) y = σ (kolyvaginD σ m y) - kolyvaginD σ m y := rfl
  have e2 : ((m : AddMonoid.End M) - ∑ j ∈ range m, σ ^ j) y
      = m • y - ∑ j ∈ range m, (σ ^ j) y := by
    rw [AddMonoidHom.sub_apply, AddMonoidHom.finset_sum_apply, AddMonoid.End.natCast_apply]
  simp only at h
  rw [← e1, h, e2, htr, natCast_zsmul]

/-- **Common-modulus invariance.** For every `d` dividing both `m` and `a`, `D y` is
`σ`-invariant modulo `d • M`. -/
theorem derived_invariance_mod_common {M : Type*} [AddCommGroup M] (σ : AddMonoid.End M)
    (m : ℕ) (hσ : σ ^ m = 1) (y y₁ : M) (a : ℤ)
    (htr : ∑ j ∈ range m, (σ ^ j) y = a • y₁) {d : ℤ} (hdm : d ∣ (m : ℤ)) (hda : d ∣ a) :
    ∃ z : M, σ (kolyvaginD σ m y) - kolyvaginD σ m y = d • z := by
  obtain ⟨k, hk⟩ := hdm
  obtain ⟨c, rfl⟩ := hda
  refine ⟨k • y - c • y₁, ?_⟩
  rw [derived_invariance_trace σ m hσ y y₁ _ htr, hk, smul_sub, mul_smul, mul_smul]

/-- The common modulus `gcd(a, m)` is admissible in `derived_invariance_mod_common`. -/
theorem derived_invariance_mod_gcd {M : Type*} [AddCommGroup M] (σ : AddMonoid.End M)
    (m : ℕ) (hσ : σ ^ m = 1) (y y₁ : M) (a : ℤ)
    (htr : ∑ j ∈ range m, (σ ^ j) y = a • y₁) :
    ∃ z : M, σ (kolyvaginD σ m y) - kolyvaginD σ m y = (Int.gcd a m : ℤ) • z :=
  derived_invariance_mod_common σ m hσ y y₁ a htr (Int.gcd_dvd_right a m)
    (Int.gcd_dvd_left a m)

/-- **Reduced-target bookkeeping.** If `h = 2 + s - t` with `t ≤ 1` and `s` even, then
`h ≤ 2 ↔ s = 0`. (Here `s = dim Sha[p]`, `t = dim loc_p Sel_p`.) -/
theorem reduced_target_iff (h s t : ℕ) (hh : h + t = 2 + s) (ht : t ≤ 1) (hs : Even s) :
    h ≤ 2 ↔ s = 0 := by
  obtain ⟨r, rfl⟩ := hs
  omega

/-! ### Finite seed facts for the application at `p = 53` -/

/-- `59` affine points mod `53`, so `#E(𝔽_53) = 60` and `a_53 = 54 - 60 = -6`. -/
theorem affCount_53 : Continuation.SeedFinite.affCount 53 = 59 := by decide +kernel

/-- `a_29 = 0`: `29` is a supersingular prime of the seed curve. -/
theorem affCount_29 : Continuation.SeedFinite.affCount 29 = 29 := by decide +kernel

/-- `53` is good ordinary: `a_53 = 53 + 1 - #E(𝔽_53) = -6 ≢ 0 (mod 53)`. -/
theorem ordinary_53 : ((53 + 1 : ℤ) - (Continuation.SeedFinite.affCount 53 + 1)) = -6 ∧
    ¬ ((53 : ℤ) ∣ -6) := by
  rw [affCount_53]; decide

/-- The minimal model's discriminant from `c₄ = 3169004368`, `c₆ = 56243184546880`:
`Δ = (c₄³ - c₆²)/1728 = 2⁸·3²·2243·4547³·5843²`. -/
theorem minimal_discriminant :
    (3169004368 : ℤ) ^ 3 - 56243184546880 ^ 2
      = 1728 * (2 ^ 8 * 3 ^ 2 * 2243 * 4547 ^ 3 * 5843 ^ 2) := by norm_num

/-- Residues of the multiplicative primes modulo `53`: none is `≡ ±1`. Also `53 ∣ 3392`. -/
theorem residues_mod_53 : 3 % 53 = 3 ∧ 2243 % 53 = 17 ∧ 5843 % 53 = 13 ∧ 3392 = 2 ^ 6 * 53 := by
  decide

/-! ### Inertness of the auxiliary primes used in the revised table -/

instance fact_prime_3391 : Fact (Nat.Prime 3391) := ⟨by norm_num⟩
instance fact_prime_21089 : Fact (Nat.Prime 21089) := ⟨by norm_num⟩

/-- `ℓ = 3391` (with `3392 = 2⁶·53`) is inert in `ℚ(√-23)`. -/
theorem inert_3391 : legendreSym 3391 (-23) = -1 := by norm_num

/-- `ℓ = 21089` (with `21090 = 2·3·5·19·37`, `a_ℓ = -74`) is inert in `ℚ(√-23)`. -/
theorem inert_21089 : legendreSym 21089 (-23) = -1 := by norm_num

/-- `gcd(a_ℓ, ℓ + 1) = gcd(-74, 21090) = 74 = 2·37`. -/
theorem common_modulus_21089 : Int.gcd (-74) 21090 = 74 ∧ 21090 = 2 * 3 * 5 * 19 * 37 := by
  decide

end Continuation.TraceCongruence
