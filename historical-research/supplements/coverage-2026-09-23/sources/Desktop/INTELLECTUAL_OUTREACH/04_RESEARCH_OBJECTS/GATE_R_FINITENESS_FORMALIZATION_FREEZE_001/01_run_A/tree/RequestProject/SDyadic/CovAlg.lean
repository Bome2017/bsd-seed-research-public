/-
Generic algebra for the quartic coverings `Run013.Cov`.

Nothing here is specific to the `S_dyadic` family: these are field identities, a
denominator-cleared homogeneous form of the covering, its weighted scaling invariance, and the
discriminant (completed-square) identity

    `4 * d * n ^ 2 = (2 * d * u ^ 2 + a * v ^ 2) ^ 2 - (a ^ 2 - 4 * b) * v ^ 4`.
-/
import RequestProject.Run013.Selmer

namespace SDyadic

open Run013

variable {K : Type*} [Field K]

/-- The denominator-cleared, weighted-homogeneous form of the covering:
`d * n ^ 2 = d ^ 2 u ^ 4 + a d u ^ 2 v ^ 2 + b v ^ 4`. -/
def CovH (K : Type*) [Field K] (a b d : K) : Prop :=
  ∃ u v n : K, ¬(u = 0 ∧ v = 0) ∧
    d * n ^ 2 = d ^ 2 * u ^ 4 + a * d * u ^ 2 * v ^ 2 + b * v ^ 4

/-- For `d ≠ 0` the cleared form is equivalent to `Run013.Cov`. -/
theorem cov_iff_covH {a b d : K} (hd : d ≠ 0) : Cov K a b d ↔ CovH K a b d := by
  constructor
  · rintro ⟨u, v, n, huv, hn⟩
    refine ⟨u, v, n, huv, ?_⟩
    have hbd : b / d * d = b := div_mul_cancel₀ b hd
    calc d * n ^ 2 = d * (d * u ^ 4 + a * u ^ 2 * v ^ 2 + b / d * v ^ 4) := by rw [hn]
      _ = d ^ 2 * u ^ 4 + a * d * u ^ 2 * v ^ 2 + b * v ^ 4 := by
          linear_combination v ^ 4 * hbd
  · rintro ⟨u, v, n, huv, hn⟩
    refine ⟨u, v, n, huv, ?_⟩
    have hbd : b / d * d = b := div_mul_cancel₀ b hd
    have : d * n ^ 2 = d * (d * u ^ 4 + a * u ^ 2 * v ^ 2 + b / d * v ^ 4) := by
      rw [hn]; linear_combination -(v ^ 4) * hbd
    exact mul_left_cancel₀ hd this

/-- The cleared covering equation is invariant under the weighted scaling
`(u, v, n) ↦ (c u, c v, c² n)`. -/
theorem covH_scale {R : Type*} [CommRing R] {a b d u v n : R} (c : R)
    (h : d * n ^ 2 = d ^ 2 * u ^ 4 + a * d * u ^ 2 * v ^ 2 + b * v ^ 4) :
    d * (c ^ 2 * n) ^ 2 =
      d ^ 2 * (c * u) ^ 4 + a * d * (c * u) ^ 2 * (c * v) ^ 2 + b * (c * v) ^ 4 := by
  linear_combination c ^ 4 * h

/-- Completing the square: `4 d n² = (2 d u² + a v²)² − Δ v⁴` with `Δ = a² − 4b`. -/
theorem covH_disc {R : Type*} [CommRing R] {a b d u v n : R}
    (h : d * n ^ 2 = d ^ 2 * u ^ 4 + a * d * u ^ 2 * v ^ 2 + b * v ^ 4) :
    (2 * d * u ^ 2 + a * v ^ 2) ^ 2 - (a ^ 2 - 4 * b) * v ^ 4 = 4 * (d * n ^ 2) := by
  linear_combination -4 * h

/-- If the quartic factors as `(d u² − e₁ v²)(d u² − e₂ v²)` — which happens exactly when
`e₁ + e₂ = -a` and `e₁ e₂ = b` — the cleared covering equation reads `d n² = S · T`. -/
theorem covH_factor {R : Type*} [CommRing R] {a b d u v n e₁ e₂ : R}
    (hsum : e₁ + e₂ = -a) (hprod : e₁ * e₂ = b)
    (h : d * n ^ 2 = d ^ 2 * u ^ 4 + a * d * u ^ 2 * v ^ 2 + b * v ^ 4) :
    d * n ^ 2 = (d * u ^ 2 - e₁ * v ^ 2) * (d * u ^ 2 - e₂ * v ^ 2) := by
  linear_combination h + (d * u ^ 2 * v ^ 2) * hsum - v ^ 4 * hprod

end SDyadic
