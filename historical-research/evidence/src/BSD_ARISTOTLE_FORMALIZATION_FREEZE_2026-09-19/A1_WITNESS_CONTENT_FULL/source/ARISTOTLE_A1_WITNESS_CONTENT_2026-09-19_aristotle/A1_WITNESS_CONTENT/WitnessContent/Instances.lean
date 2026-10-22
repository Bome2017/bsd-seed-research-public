import WitnessContent.Spec

/-!
# A1 — instantiation checks (T10, T11)

The two abstractions used by T8 are satisfied by the intended arithmetic objects:
`ℤ_[p]` has all prime-to-`p` naturals invertible, and `(ZMod S)ˣ` is a finite group.
-/

namespace WitnessContent

/-- T10. -/
theorem padicInt_units_proof : Spec.PadicInt_units := by
  intro p _ u hu
  rw [PadicInt.isUnit_iff]
  have h1 : ‖(u : ℤ_[p])‖ ≤ 1 := PadicInt.norm_le_one _
  have h2 : ¬ ‖(u : ℤ_[p])‖ < 1 := by
    intro h
    have hcast : ((u : ℤ) : ℤ_[p]) = (u : ℤ_[p]) := by push_cast; ring
    rw [← hcast, PadicInt.norm_int_lt_one_iff_dvd] at h
    exact hu (by exact_mod_cast h)
  exact le_antisymm h1 (not_lt.mp h2)

/-- T11. -/
theorem units_exponent_proof : Spec.Units_exponent := by
  intro S _
  exact ⟨Nat.card_pos, fun g => pow_card_eq_one'⟩

end WitnessContent
