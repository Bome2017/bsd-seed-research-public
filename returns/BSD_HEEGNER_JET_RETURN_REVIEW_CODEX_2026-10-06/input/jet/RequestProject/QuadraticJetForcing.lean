import Mathlib

/-!
# Quadratic-jet forcing at the four W3 nodes

Let `F(T,S) = a T² + b T S + c S² + (terms of total degree ≥ 3)` be an integral two-variable
series (the retained low-jet input `F ∈ (T,S)²`).  At the four W3 nodes
`(w,s) ∈ {(3,2),(3,3),(4,3),(4,4)}` one evaluates at `T = t_w`, `S = t_s`, where
`t_n = (1+p)^n - 1 ≡ n p (mod p²)`.  Every term of total degree `≥ 3` then lies in `p³`.

The theorem below is the exact finite algebra of that evaluation, over an arbitrary integral
domain `R` and a nonzero element `π` (for the application `R = ℤ_[p]`, `π = p`): the hypotheses
`e₍ws₎` say that each node value differs from the quadratic part by a multiple of `π³`.

Conclusion: if all four node values vanish modulo `π³`, then `π` divides each of `a, b, c`.
The underlying `4 × 3` node matrix has rows `(9,6,4), (9,9,9), (16,12,9), (16,16,16)`; it contains
a `3 × 3` minor of determinant `1` after the unimodular row operation `4·r₄ − 7·r₂`, so no
condition on `p` is needed.

Consequently a unit coefficient `c` of `S²` forces one of the four node values to be nonzero
modulo `π³` (`exists_node_ne_zero_of_not_dvd_c`).
-/

namespace W3

variable {R : Type*} [CommRing R] [IsDomain R]

/-- Divisibility by `π³` of `π² x` forces divisibility of `x` by `π`. -/
lemma dvd_of_pow_three_dvd_sq_mul {π x : R} (hπ : π ≠ 0) (h : π ^ 3 ∣ π ^ 2 * x) : π ∣ x := by
  have h' : π ^ 2 * π ∣ π ^ 2 * x := by simpa [pow_succ] using h
  exact (mul_dvd_mul_iff_left (pow_ne_zero 2 hπ)).mp h'

omit [IsDomain R] in
/-- The quadratic part at a node equals `π²·(linear form) + π³·(something)`. -/
lemma quad_node_expansion (π a b c tw ts kw ks : R) (w s : R)
    (htw : tw = w * π + π ^ 2 * kw) (hts : ts = s * π + π ^ 2 * ks) :
    π ^ 3 ∣ (a * tw ^ 2 + b * tw * ts + c * ts ^ 2) - π ^ 2 * (a * w ^ 2 + b * w * s + c * s ^ 2) := by
  subst htw hts
  refine ⟨a * (2 * w * kw + π * kw ^ 2) + b * (w * ks + kw * s + π * kw * ks)
      + c * (2 * s * ks + π * ks ^ 2), ?_⟩
  ring

/-- **Quadratic-jet forcing lemma.**  If the four W3 node values all vanish modulo `π³`, then the
whole quadratic jet `(a, b, c)` vanishes modulo `π`. -/
theorem quadratic_jet_forcing {π : R} (hπ : π ≠ 0) (a b c t2 t3 t4 V32 V33 V43 V44 : R)
    (h2 : π ^ 2 ∣ t2 - 2 * π) (h3 : π ^ 2 ∣ t3 - 3 * π) (h4 : π ^ 2 ∣ t4 - 4 * π)
    (e32 : π ^ 3 ∣ V32 - (a * t3 ^ 2 + b * t3 * t2 + c * t2 ^ 2))
    (e33 : π ^ 3 ∣ V33 - (a * t3 ^ 2 + b * t3 * t3 + c * t3 ^ 2))
    (e43 : π ^ 3 ∣ V43 - (a * t4 ^ 2 + b * t4 * t3 + c * t3 ^ 2))
    (e44 : π ^ 3 ∣ V44 - (a * t4 ^ 2 + b * t4 * t4 + c * t4 ^ 2))
    (z32 : π ^ 3 ∣ V32) (z33 : π ^ 3 ∣ V33) (z43 : π ^ 3 ∣ V43) (z44 : π ^ 3 ∣ V44) :
    π ∣ a ∧ π ∣ b ∧ π ∣ c := by
  obtain ⟨k2, hk2⟩ := h2
  obtain ⟨k3, hk3⟩ := h3
  obtain ⟨k4, hk4⟩ := h4
  have ht2 : t2 = 2 * π + π ^ 2 * k2 := by linear_combination hk2
  have ht3 : t3 = 3 * π + π ^ 2 * k3 := by linear_combination hk3
  have ht4 : t4 = 4 * π + π ^ 2 * k4 := by linear_combination hk4
  -- the four linear forms are divisible by `π`
  have node : ∀ (V tw ts kw ks w s : R), tw = w * π + π ^ 2 * kw → ts = s * π + π ^ 2 * ks →
      π ^ 3 ∣ V - (a * tw ^ 2 + b * tw * ts + c * ts ^ 2) → π ^ 3 ∣ V →
      π ∣ a * w ^ 2 + b * w * s + c * s ^ 2 := by
    intro V tw ts kw ks w s htw hts e z
    apply dvd_of_pow_three_dvd_sq_mul hπ
    have hq := quad_node_expansion π a b c tw ts kw ks w s htw hts
    have : π ^ 2 * (a * w ^ 2 + b * w * s + c * s ^ 2) =
        V - (V - (a * tw ^ 2 + b * tw * ts + c * ts ^ 2))
          - ((a * tw ^ 2 + b * tw * ts + c * ts ^ 2)
              - π ^ 2 * (a * w ^ 2 + b * w * s + c * s ^ 2)) := by ring
    rw [this]
    exact dvd_sub (dvd_sub z e) hq
  have x32 := node V32 t3 t2 k3 k2 3 2 (by rw [ht3]) (by rw [ht2]) e32 z32
  have x33 := node V33 t3 t3 k3 k3 3 3 (by rw [ht3]) (by rw [ht3]) e33 z33
  have x43 := node V43 t4 t3 k4 k3 4 3 (by rw [ht4]) (by rw [ht3]) e43 z43
  have x44 := node V44 t4 t4 k4 k4 4 4 (by rw [ht4]) (by rw [ht4]) e44 z44
  obtain ⟨y32, hy32⟩ := x32
  obtain ⟨y33, hy33⟩ := x33
  obtain ⟨y43, hy43⟩ := x43
  obtain ⟨y44, hy44⟩ := x44
  -- `s = a + b + c = 4·X44 − 7·X33`, then invert the unimodular `3 × 3` system
  refine ⟨⟨6 * (4 * y44 - 7 * y33) + 3 * y32 - 2 * y43, ?_⟩,
    ⟨-17 * (4 * y44 - 7 * y33) - 7 * y32 + 5 * y43, ?_⟩,
    ⟨12 * (4 * y44 - 7 * y33) + 4 * y32 - 3 * y43, ?_⟩⟩
  · linear_combination 24 * hy44 - 42 * hy33 + 3 * hy32 - 2 * hy43
  · linear_combination (-68) * hy44 + 119 * hy33 - 7 * hy32 + 5 * hy43
  · linear_combination 48 * hy44 - 84 * hy33 + 4 * hy32 - 3 * hy43

/-- Contrapositive used for the weight-two half-test: if the `S²`-coefficient is `u · ℓ` with `u`
a unit and `π ∤ ℓ`, then at least one of the four node values is nonzero modulo `π³`. -/
theorem exists_node_ne_zero_of_not_dvd_c {π : R} (hπ : π ≠ 0)
    (a b c u ℓ t2 t3 t4 V32 V33 V43 V44 : R) (hu : IsUnit u) (hc : c = u * ℓ) (hℓ : ¬ π ∣ ℓ)
    (h2 : π ^ 2 ∣ t2 - 2 * π) (h3 : π ^ 2 ∣ t3 - 3 * π) (h4 : π ^ 2 ∣ t4 - 4 * π)
    (e32 : π ^ 3 ∣ V32 - (a * t3 ^ 2 + b * t3 * t2 + c * t2 ^ 2))
    (e33 : π ^ 3 ∣ V33 - (a * t3 ^ 2 + b * t3 * t3 + c * t3 ^ 2))
    (e43 : π ^ 3 ∣ V43 - (a * t4 ^ 2 + b * t4 * t3 + c * t3 ^ 2))
    (e44 : π ^ 3 ∣ V44 - (a * t4 ^ 2 + b * t4 * t4 + c * t4 ^ 2)) :
    ¬ π ^ 3 ∣ V32 ∨ ¬ π ^ 3 ∣ V33 ∨ ¬ π ^ 3 ∣ V43 ∨ ¬ π ^ 3 ∣ V44 := by
  by_contra hcon
  push_neg at hcon
  obtain ⟨z32, z33, z43, z44⟩ := hcon
  obtain ⟨-, -, hcd⟩ := quadratic_jet_forcing hπ a b c t2 t3 t4 V32 V33 V43 V44 h2 h3 h4
    e32 e33 e43 e44 z32 z33 z43 z44
  apply hℓ
  obtain ⟨v, hv⟩ := hu
  have : ℓ = ↑v⁻¹ * c := by rw [hc, ← hv, ← mul_assoc, Units.inv_mul, one_mul]
  rw [this]
  exact dvd_mul_of_dvd_right hcd _

/-- The nodes in `ℤ_[p]`: `t_n = (1+p)^n - 1` satisfies `p² ∣ t_n - n p`. -/
lemma padic_node_congr (p : ℕ) [Fact p.Prime] (n : ℕ) :
    (p : ℤ_[p]) ^ 2 ∣ ((1 + (p : ℤ_[p])) ^ n - 1) - n * p := by
  induction n with
  | zero => simp
  | succ n ih =>
    obtain ⟨k, hk⟩ := ih
    refine ⟨k * (1 + p) + n, ?_⟩
    have : (1 + (p : ℤ_[p])) ^ n = 1 + n * p + p ^ 2 * k := by linear_combination hk
    push_cast
    rw [pow_succ, this]
    ring

end W3
