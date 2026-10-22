module

public import Mathlib

/-!
# The tightened admission threshold for `DERIVED_GROSS_IDENTITY`

Lean companion of `THRESHOLD_REGRADE.md`. It formalizes the logic of the compatibility square

```
  Θ⁽²⁾      =   m_E · det h(P₁,P₂)
   ↓ φ               ↓ φ
  C₂(p,ℓ)   =   m_E · (a_ℓ − 2) · R_{p,ℓ}     (mod p)
```

and of the unit ambiguities in it. All arithmetic inputs (the characteristic-zero identity, the
reduction map, G2, the detector) are explicit hypotheses. Nothing here is a statement about `Ш`
of the seed.

* `finite_support_of_square`: the four interfaces give `Ш[p] ≠ 0 → p ∣ num(m_E)` outside an
  explicit finite set, and hence finite support.
* `bottom_row_is_exact_law`: the bottom row of the square is Theorem W's scalar
  `s_p = C₂/((a_ℓ−2)R)` being congruent to `m_E`, i.e. the exact Law (G1).
* `single_unit_preserves_zero`, `proved_units_preserve_zero`: a discrepancy factor that is a
  proved nonzero residue does not affect zero/nonzero detection, whether it is one unit or a
  quotient of two.
* `uncontrolled_factor_no_detection`: if the discrepancy factor is not proved to be a unit, the
  bottom row gives no detection at all.
-/

@[expose] public section

namespace DerivedGross.Threshold

/-- **One proved unit on the final congruence is harmless for zero detection.** -/
theorem single_unit_preserves_zero {F : Type*} [Field F] (s u m : F) (hu : u ≠ 0)
    (h : s = u * m) : s = 0 ↔ m = 0 := by
  subst h; simp [hu]

/-- **Two separately proved units are also harmless for zero detection.** If the left vertical
map sends `Θ⁽²⁾` to `u·C₂`, the right one sends `det h` to `v·X` with `X = (a_ℓ−2)R`, the
characteristic-zero identity transports to `u·C₂ = m·(v·X)`, and both `u` and `v` are proved
nonzero, then `C₂ = 0 ↔ m = 0` whenever `X ≠ 0`. What matters is that the total discrepancy
`v/u` is a proved unit, not how many unit factors appear. -/
theorem proved_units_preserve_zero {F : Type*} [Field F] (C₂ X m u v : F) (hu : u ≠ 0)
    (hv : v ≠ 0) (hX : X ≠ 0) (h : u * C₂ = m * (v * X)) : C₂ = 0 ↔ m = 0 := by
  constructor
  · intro hC
    rw [hC, mul_zero] at h
    rcases mul_eq_zero.mp h.symm with hm | hvX
    · exact hm
    · exact absurd hvX (mul_ne_zero hv hX)
  · intro hm
    rw [hm, zero_mul] at h
    rcases mul_eq_zero.mp h with hu0 | hC
    · exact absurd hu0 hu
    · exact hC

/-- **An uncontrolled discrepancy factor kills detection.** For any `m ≠ 0` and `X ≠ 0` and any
`u`, the factor `v = 0` (a scalar not proved to be a unit) is consistent with the transported
identity `u·C₂ = m·(v·X)` together with `C₂ = 0`. So the bottom row then says nothing about
`m mod p`. -/
theorem uncontrolled_factor_no_detection {F : Type*} [Field F] (m X u : F) :
    ∃ C₂ v : F, u * C₂ = m * (v * X) ∧ C₂ = 0 := ⟨0, 0, by simp, rfl⟩

/-- **The bottom row is the exact Law.** If `b·C₂ = a·X` in `ZMod p` with `p ∤ b` and `X ≠ 0`,
then Theorem W's scalar `s_p = C₂/X` equals `a/b = m_E mod p`. -/
theorem bottom_row_is_exact_law (p : ℕ) [Fact p.Prime] (a b : ℤ) (C₂ X : ZMod p)
    (hb : (b : ZMod p) ≠ 0) (hX : X ≠ 0) (h : (b : ZMod p) * C₂ = (a : ZMod p) * X) :
    C₂ / X = (a : ZMod p) / (b : ZMod p) := by
  rw [div_eq_div_iff hX hb]
  linear_combination h

/-- **The finite-support theorem from the four interfaces.**

* Interface 1 (characteristic-zero identity): `Θ, D : V` with `b • Θ = a • D`, i.e.
  `Θ⁽²⁾ = m_E · det h` with `m_E = a/b`.
* Interface 2 (the constant): `a ≠ 0`, `b ≠ 0` (Ш/FIN/Q36/BSD-freeness of `a, b` is a property
  of their definition and is not expressible here).
* Interface 3 (compatible reduction): for `p ∉ S` and admissible `ℓ`, one additive map
  `φ p ℓ : V → ZMod p` with `φ Θ = C₂(p,ℓ)` and `φ D = w·(a_ℓ − 2)R_{p,ℓ}`, with the discrepancy
  `w(p,ℓ)` proved nonzero (`w = 1` in the exact case).
* G2: for `p ∉ S` some admissible `ℓ` has `(a_ℓ − 2)R_{p,ℓ} ≠ 0` in `ZMod p`.
* Detector: for `p ∉ S` and admissible `ℓ`, `C₂(p,ℓ) ≠ 0` forces `Ш[p] = 0`.

Then interface 4: for every prime `p ∉ S` with `p ∤ b`, `Ш[p] ≠ 0 → p ∣ a`; so the primes with
`Ш[p] ≠ 0` lie in `S ∪ {p ∣ b} ∪ {p ∣ a}`, a finite set. -/
theorem finite_support_of_square {V : Type*} [AddCommGroup V] (S : Finset ℕ) (a b : ℤ)
    (ha : a ≠ 0) (hb : b ≠ 0) (Θ D : V) (hid : b • Θ = a • D)
    (Adm : ℕ → ℕ → Prop) (ShaZero : ℕ → Prop)
    (φ : (p : ℕ) → ℕ → V →+ ZMod p) (C₂ X w : (p : ℕ) → ℕ → ZMod p)
    (hφΘ : ∀ p, p.Prime → p ∉ S → ∀ ℓ, Adm p ℓ → φ p ℓ Θ = C₂ p ℓ)
    (hφD : ∀ p, p.Prime → p ∉ S → ∀ ℓ, Adm p ℓ → φ p ℓ D = w p ℓ * X p ℓ)
    (hw : ∀ p, p.Prime → p ∉ S → ∀ ℓ, Adm p ℓ → w p ℓ ≠ 0)
    (hG2 : ∀ p, p.Prime → p ∉ S → ∃ ℓ, Adm p ℓ ∧ X p ℓ ≠ 0)
    (hdet : ∀ p, p.Prime → p ∉ S → ∀ ℓ, Adm p ℓ → C₂ p ℓ ≠ 0 → ShaZero p) :
    (∀ p, p.Prime → p ∉ S → ¬ (p : ℤ) ∣ b → ¬ ShaZero p → (p : ℤ) ∣ a) ∧
    {p | p.Prime ∧ ¬ ShaZero p} ⊆
      (S : Set ℕ) ∪ (b.natAbs.primeFactors : Set ℕ) ∪ (a.natAbs.primeFactors : Set ℕ) ∧
    {p | p.Prime ∧ ¬ ShaZero p}.Finite := by
  have key : ∀ p, p.Prime → p ∉ S → ¬ (p : ℤ) ∣ b → ¬ ShaZero p → (p : ℤ) ∣ a := by
    intro p hp hS hpb hbad
    haveI := Fact.mk hp
    by_contra hpa
    have haz : (a : ZMod p) ≠ 0 := by
      rw [Ne, ZMod.intCast_zmod_eq_zero_iff_dvd]; exact hpa
    have hbz : (b : ZMod p) ≠ 0 := by
      rw [Ne, ZMod.intCast_zmod_eq_zero_iff_dvd]; exact hpb
    obtain ⟨ℓ, hadm, hX⟩ := hG2 p hp hS
    have hrow : (b : ZMod p) * C₂ p ℓ = (a : ZMod p) * (w p ℓ * X p ℓ) := by
      have := congrArg (φ p ℓ) hid
      rw [map_zsmul, map_zsmul, hφΘ p hp hS ℓ hadm, hφD p hp hS ℓ hadm] at this
      simpa [zsmul_eq_mul] using this
    have hC : C₂ p ℓ ≠ 0 := by
      intro h0
      rw [h0, mul_zero] at hrow
      exact mul_ne_zero haz (mul_ne_zero (hw p hp hS ℓ hadm) hX) hrow.symm
    exact hbad (hdet p hp hS ℓ hadm hC)
  have hsub : {p | p.Prime ∧ ¬ ShaZero p} ⊆
      (S : Set ℕ) ∪ (b.natAbs.primeFactors : Set ℕ) ∪ (a.natAbs.primeFactors : Set ℕ) := by
    rintro p ⟨hp, hbad⟩
    by_cases hS : p ∈ S
    · exact Or.inl (Or.inl hS)
    by_cases hpb : (p : ℤ) ∣ b
    · refine Or.inl (Or.inr ?_)
      simp only [Finset.mem_coe, Nat.mem_primeFactors]
      exact ⟨hp, Int.natCast_dvd.mp hpb, Int.natAbs_ne_zero.mpr hb⟩
    · right
      simp only [Finset.mem_coe, Nat.mem_primeFactors]
      exact ⟨hp, Int.natCast_dvd.mp (key p hp hS hpb hbad), Int.natAbs_ne_zero.mpr ha⟩
  exact ⟨key, hsub,
    (((Finset.finite_toSet _).union (Finset.finite_toSet _)).union (Finset.finite_toSet _)).subset
      hsub⟩

end DerivedGross.Threshold
