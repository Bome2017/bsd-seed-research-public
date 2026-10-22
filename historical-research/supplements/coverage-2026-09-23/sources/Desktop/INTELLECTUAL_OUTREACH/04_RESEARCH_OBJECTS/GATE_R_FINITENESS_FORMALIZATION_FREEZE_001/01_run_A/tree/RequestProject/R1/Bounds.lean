import Mathlib

/-!
# A tiny toolkit for homogeneous size bounds on integer polynomial expressions

`BddBy d p` says that the two-variable integer expression `p` is bounded by a constant times
`M ^ d` whenever both arguments are bounded in absolute value by some `M ≥ 1`.  The constant is
existentially quantified, so that the composition lemmas below assemble the bounds for a compound
expression without any coefficient bookkeeping.

This is used in `RequestProject/R1/Bezout.lean` to bound the Bézout cofactors of the degree-four
duplication pair, which is the quantitative half of estimate obligation 1.
-/

namespace R1

/-- `BddBy d p`: some constant `K ≥ 0` bounds `|p u v|` by `K * M ^ d`, uniformly over all
`u, v` with `|u| ≤ M`, `|v| ≤ M` and `1 ≤ M`. -/
def BddBy (d : ℕ) (p : ℤ → ℤ → ℤ) : Prop :=
  ∃ K : ℤ, 0 ≤ K ∧ ∀ u v M : ℤ, 1 ≤ M → |u| ≤ M → |v| ≤ M → |p u v| ≤ K * M ^ d

theorem bddBy_const (c : ℤ) : BddBy 0 (fun _ _ => c) :=
  ⟨|c|, abs_nonneg c, fun _ _ _ _ _ _ => by simp⟩

theorem bddBy_fst : BddBy 1 (fun u _ => u) :=
  ⟨1, zero_le_one, fun _ _ _ _ hu _ => by simpa using hu⟩

theorem bddBy_snd : BddBy 1 (fun _ v => v) :=
  ⟨1, zero_le_one, fun _ _ _ _ _ hv => by simpa using hv⟩

theorem bddBy_add {d : ℕ} {p q : ℤ → ℤ → ℤ} (hp : BddBy d p) (hq : BddBy d q) :
    BddBy d (fun u v => p u v + q u v) := by
  obtain ⟨K₁, hK₁, h₁⟩ := hp
  obtain ⟨K₂, hK₂, h₂⟩ := hq
  refine ⟨K₁ + K₂, by positivity, fun u v M hM hu hv => ?_⟩
  calc |p u v + q u v| ≤ |p u v| + |q u v| := abs_add_le _ _
    _ ≤ K₁ * M ^ d + K₂ * M ^ d := add_le_add (h₁ u v M hM hu hv) (h₂ u v M hM hu hv)
    _ = (K₁ + K₂) * M ^ d := by ring

theorem bddBy_sub {d : ℕ} {p q : ℤ → ℤ → ℤ} (hp : BddBy d p) (hq : BddBy d q) :
    BddBy d (fun u v => p u v - q u v) := by
  obtain ⟨K₁, hK₁, h₁⟩ := hp
  obtain ⟨K₂, hK₂, h₂⟩ := hq
  refine ⟨K₁ + K₂, by positivity, fun u v M hM hu hv => ?_⟩
  calc |p u v - q u v| ≤ |p u v| + |q u v| := abs_sub _ _
    _ ≤ K₁ * M ^ d + K₂ * M ^ d := add_le_add (h₁ u v M hM hu hv) (h₂ u v M hM hu hv)
    _ = (K₁ + K₂) * M ^ d := by ring

theorem bddBy_mul {d e : ℕ} {p q : ℤ → ℤ → ℤ} (hp : BddBy d p) (hq : BddBy e q) :
    BddBy (d + e) (fun u v => p u v * q u v) := by
  obtain ⟨K₁, hK₁, h₁⟩ := hp
  obtain ⟨K₂, hK₂, h₂⟩ := hq
  refine ⟨K₁ * K₂, by positivity, fun u v M hM hu hv => ?_⟩
  have hM₀ : (0 : ℤ) ≤ M := le_trans zero_le_one hM
  have hb₁ := h₁ u v M hM hu hv
  have hb₂ := h₂ u v M hM hu hv
  calc |p u v * q u v| = |p u v| * |q u v| := abs_mul _ _
    _ ≤ (K₁ * M ^ d) * (K₂ * M ^ e) :=
        mul_le_mul hb₁ hb₂ (abs_nonneg _) (by positivity)
    _ = (K₁ * K₂) * M ^ (d + e) := by rw [pow_add]; ring

theorem bddBy_sq {d : ℕ} {p : ℤ → ℤ → ℤ} (hp : BddBy d p) :
    BddBy (d + d) (fun u v => p u v ^ 2) := by
  have h := bddBy_mul hp hp
  simpa [sq] using h

theorem bddBy_pow {d : ℕ} {p : ℤ → ℤ → ℤ} (n : ℕ) (hp : BddBy d p) :
    BddBy (n * d) (fun u v => p u v ^ n) := by
  induction n with
  | zero => simpa using bddBy_const 1
  | succ k ih =>
      have h := bddBy_mul ih hp
      simpa [pow_succ, Nat.succ_mul] using h

theorem bddBy_up {d e : ℕ} {p : ℤ → ℤ → ℤ} (hde : d ≤ e) (hp : BddBy d p) : BddBy e p := by
  obtain ⟨K, hK, h⟩ := hp
  refine ⟨K, hK, fun u v M hM hu hv => ?_⟩
  refine le_trans (h u v M hM hu hv) ?_
  exact mul_le_mul_of_nonneg_left (pow_le_pow_right₀ hM hde) hK

end R1
