import RequestProject.R1.Bounds

/-!
# The degree-four duplication pair, its Bézout certificates, and the height estimate

For the family `y² = x (x² + a x + b)` with integer `a, b`, the duplication of the
`x`-coordinate is given by the degree-four homogeneous pair

    F(u,v) = (u² − b v²)²
    G(u,v) = 4 u v (u² + a u v + b v²)

so that `x(2P) = F(x,1) / G(x,1)`.

This file supplies, **for integer `a, b` with `b ≠ 0` and `a² − 4b ≠ 0`**, the two estimate
obligations of target R1:

* `bezout_v`, `bezout_u` — explicit Bézout certificates
  `4 b⁴ (a² − 4b)² · v¹²  =  cFv · F + cGv · G` and the same for `u¹²`, with **explicit**
  integer cofactors of degree eight.  The constant `4 b⁴ (a² − 4b)²` is nonzero exactly because
  `b ≠ 0` and `a² − 4b ≠ 0`; this is what replaces a bare "no common projective zero" argument.
* `bddBy_cFv` etc. — the cofactors are bounded by a curve-dependent constant times `M⁸`, where
  `M = max(|u|,|v|)`.  This is the quantitative content of obligation 1.
* `dvd_Rcon_of_reduce` — the cancellation bound of obligation 2: if the integer pair `(F, G)` is
  reduced to coprime projective coordinates by dividing out `k`, then `k ∣ 4 b⁴ (a² − 4b)²`, so
  the cancellation is bounded by a constant depending only on the curve.
* `duplication_height_core` — combining the two: `H(x)⁴ ≤ C · H(z)` whenever
  `z · 4x(x² + ax + b) = (x² − b)²` and `4x(x² + ax + b) ≠ 0`.

Nothing here mentions finiteness, finite generation, rank, Selmer groups or canonical heights.
-/

namespace R1

/-! ## The duplication pair and its Bézout certificates -/

/-- `F(u,v) = (u² − b v²)²`, the numerator form of the duplication map. -/
def Fpol (b u v : ℤ) : ℤ := (u ^ 2 - b * v ^ 2) ^ 2

/-- `G(u,v) = 4 u v (u² + a u v + b v²)`, the denominator form of the duplication map. -/
def Gpol (a b u v : ℤ) : ℤ := 4 * u * v * (u ^ 2 + a * u * v + b * v ^ 2)

/-- The nonzero constant of the Bézout certificates: `4 b⁴ (a² − 4b)²`. -/
def Rcon (a b : ℤ) : ℤ := 4 * b ^ 4 * (a ^ 2 - 4 * b) ^ 2

/-- Cofactor of `F` in the `v¹²` certificate. -/
def cFv (a b u v : ℤ) : ℤ :=
  4 * (u * ((2 * b - a ^ 2) * u * v ^ 2 - a * u ^ 2 * v) - b * (a ^ 2 - 4 * b) * v ^ 4) ^ 2

/-- Cofactor of `G` in the `v¹²` certificate. -/
def cGv (a b u v : ℤ) : ℤ :=
  (u * (a * u - 2 * b * v)) ^ 2 * (u * v * (u ^ 2 + a * u * v + b * v ^ 2))
    + 2 * (u * (a * u - 2 * b * v))
        * (u * ((2 * b - a ^ 2) * u * v ^ 2 - a * u ^ 2 * v) - b * (a ^ 2 - 4 * b) * v ^ 4)
        * (u ^ 2 - b * v ^ 2)

/-- Cofactor of `F` in the `u¹²` certificate. -/
def cFu (a b u v : ℤ) : ℤ :=
  4 * b ^ 2 * (u * (b ^ 2 * ((2 * b - a ^ 2) * u * v ^ 2 - a * u ^ 2 * v)
    + b * (a ^ 2 - 4 * b) * u * (2 * u ^ 2 - (u ^ 2 - b * v ^ 2)))) ^ 2

/-- Cofactor of `G` in the `u¹²` certificate. -/
def cGu (a b u v : ℤ) : ℤ :=
  b ^ 2 * ((b ^ 2 * u * (a * u - 2 * b * v)) ^ 2 * (u * v * (u ^ 2 + a * u * v + b * v ^ 2))
    + 2 * (b ^ 2 * u * (a * u - 2 * b * v))
        * (u * (b ^ 2 * ((2 * b - a ^ 2) * u * v ^ 2 - a * u ^ 2 * v)
            + b * (a ^ 2 - 4 * b) * u * (2 * u ^ 2 - (u ^ 2 - b * v ^ 2))))
        * (u ^ 2 - b * v ^ 2))

set_option maxHeartbeats 1000000 in
/-- **Bézout certificate, `v`-direction.** -/
theorem bezout_v (a b u v : ℤ) :
    Rcon a b * v ^ 12 = cFv a b u v * Fpol b u v + cGv a b u v * Gpol a b u v := by
  simp only [Rcon, cFv, cGv, Fpol, Gpol]
  ring

set_option maxHeartbeats 1000000 in
/-- **Bézout certificate, `u`-direction.** -/
theorem bezout_u (a b u v : ℤ) :
    Rcon a b * u ^ 12 = cFu a b u v * Fpol b u v + cGu a b u v * Gpol a b u v := by
  simp only [Rcon, cFu, cGu, Fpol, Gpol]
  ring

/-- The Bézout constant is nonzero precisely because `b ≠ 0` and `a² − 4b ≠ 0`; these are
`P01.dualB_ne_zero` and `P01.dualA_disc_ne_zero` for the `H₄₁` curves. -/
theorem Rcon_ne_zero {a b : ℤ} (hb : b ≠ 0) (hd : a ^ 2 - 4 * b ≠ 0) : Rcon a b ≠ 0 := by
  simp only [Rcon]
  exact mul_ne_zero (mul_ne_zero (by norm_num) (pow_ne_zero _ hb)) (pow_ne_zero _ hd)

/-! ## Size bounds for the cofactors -/

theorem bddBy_pow_fst (n : ℕ) : BddBy n (fun u _ => u ^ n) := by
  simpa using bddBy_pow n bddBy_fst

theorem bddBy_pow_snd (n : ℕ) : BddBy n (fun _ v => v ^ n) := by
  simpa using bddBy_pow n bddBy_snd

private theorem bddBy_A (a b : ℤ) : BddBy 2 (fun u v => u * (a * u - 2 * b * v)) := by
  have h₁ := bddBy_mul (bddBy_const a) bddBy_fst
  have h₂ := bddBy_mul (bddBy_const (2 * b)) bddBy_snd
  have h := bddBy_mul bddBy_fst (bddBy_sub h₁ h₂)
  exact bddBy_up (by norm_num) h

private theorem bddBy_S (b : ℤ) : BddBy 2 (fun u v => u ^ 2 - b * v ^ 2) := by
  have h := bddBy_sub (bddBy_pow_fst 2) (bddBy_mul (bddBy_const b) (bddBy_pow_snd 2))
  exact bddBy_up (by norm_num) h

private theorem bddBy_P (a b : ℤ) : BddBy 2 (fun u v => u ^ 2 + a * u * v + b * v ^ 2) := by
  have h₁ := bddBy_mul (bddBy_mul (bddBy_const a) bddBy_fst) bddBy_snd
  have h₂ := bddBy_mul (bddBy_const b) (bddBy_pow_snd 2)
  have h := bddBy_add (bddBy_add (bddBy_pow_fst 2) (bddBy_up (by norm_num) h₁))
    (bddBy_up (by norm_num) h₂)
  exact bddBy_up (by norm_num) h

private theorem bddBy_W (a b : ℤ) :
    BddBy 4 (fun u v => u * v * (u ^ 2 + a * u * v + b * v ^ 2)) := by
  have h := bddBy_mul (bddBy_mul bddBy_fst bddBy_snd) (bddBy_P a b)
  exact bddBy_up (by norm_num) h

private theorem bddBy_beta (a b : ℤ) :
    BddBy 3 (fun u v => (2 * b - a ^ 2) * u * v ^ 2 - a * u ^ 2 * v) := by
  have h₁ := bddBy_mul (bddBy_mul (bddBy_const (2 * b - a ^ 2)) bddBy_fst) (bddBy_pow_snd 2)
  have h₂ := bddBy_mul (bddBy_mul (bddBy_const a) (bddBy_pow_fst 2)) bddBy_snd
  have h := bddBy_sub (bddBy_up (by norm_num : (0 + 1 + 2 : ℕ) ≤ 3) h₁)
    (bddBy_up (by norm_num : (0 + 2 + 1 : ℕ) ≤ 3) h₂)
  exact h

private theorem bddBy_Bv (a b : ℤ) :
    BddBy 4 (fun u v => u * ((2 * b - a ^ 2) * u * v ^ 2 - a * u ^ 2 * v)
      - b * (a ^ 2 - 4 * b) * v ^ 4) := by
  have h₁ := bddBy_mul bddBy_fst (bddBy_beta a b)
  have h₂ := bddBy_mul (bddBy_const (b * (a ^ 2 - 4 * b))) (bddBy_pow_snd 4)
  have h := bddBy_sub (bddBy_up (by norm_num : (1 + 3 : ℕ) ≤ 4) h₁)
    (bddBy_up (by norm_num : (0 + 4 : ℕ) ≤ 4) h₂)
  exact h

private theorem bddBy_Bu (a b : ℤ) :
    BddBy 4 (fun u v => u * (b ^ 2 * ((2 * b - a ^ 2) * u * v ^ 2 - a * u ^ 2 * v)
      + b * (a ^ 2 - 4 * b) * u * (2 * u ^ 2 - (u ^ 2 - b * v ^ 2)))) := by
  have h₁ := bddBy_mul (bddBy_const (b ^ 2)) (bddBy_beta a b)
  have h₂ := bddBy_mul (bddBy_mul (bddBy_const (b * (a ^ 2 - 4 * b))) bddBy_fst)
    (bddBy_sub (bddBy_up (by norm_num : (0 + 2 : ℕ) ≤ 2) (bddBy_mul (bddBy_const 2)
      (bddBy_pow_fst 2))) (bddBy_S b))
  have h := bddBy_mul bddBy_fst
    (bddBy_add (bddBy_up (by norm_num : (0 + 3 : ℕ) ≤ 3) h₁)
      (bddBy_up (by norm_num : (0 + 1 + 2 : ℕ) ≤ 3) h₂))
  exact bddBy_up (by norm_num) h

theorem bddBy_cFv (a b : ℤ) : BddBy 8 (cFv a b) := by
  show BddBy 8 (fun u v => 4 * (u * ((2 * b - a ^ 2) * u * v ^ 2 - a * u ^ 2 * v)
    - b * (a ^ 2 - 4 * b) * v ^ 4) ^ 2)
  have h := bddBy_mul (bddBy_const 4) (bddBy_sq (bddBy_Bv a b))
  exact bddBy_up (by norm_num) h

theorem bddBy_cGv (a b : ℤ) : BddBy 8 (cGv a b) := by
  show BddBy 8 (fun u v => (u * (a * u - 2 * b * v)) ^ 2
      * (u * v * (u ^ 2 + a * u * v + b * v ^ 2))
    + 2 * (u * (a * u - 2 * b * v))
        * (u * ((2 * b - a ^ 2) * u * v ^ 2 - a * u ^ 2 * v) - b * (a ^ 2 - 4 * b) * v ^ 4)
        * (u ^ 2 - b * v ^ 2))
  have h₁ := bddBy_mul (bddBy_sq (bddBy_A a b)) (bddBy_W a b)
  have h₂ := bddBy_mul (bddBy_mul (bddBy_mul (bddBy_const 2) (bddBy_A a b)) (bddBy_Bv a b))
    (bddBy_S b)
  exact bddBy_add (bddBy_up (by norm_num : (2 + 2 + 4 : ℕ) ≤ 8) h₁)
    (bddBy_up (by norm_num : (0 + 2 + 4 + 2 : ℕ) ≤ 8) h₂)

theorem bddBy_cFu (a b : ℤ) : BddBy 8 (cFu a b) := by
  show BddBy 8 (fun u v => 4 * b ^ 2
    * (u * (b ^ 2 * ((2 * b - a ^ 2) * u * v ^ 2 - a * u ^ 2 * v)
        + b * (a ^ 2 - 4 * b) * u * (2 * u ^ 2 - (u ^ 2 - b * v ^ 2)))) ^ 2)
  have h := bddBy_mul (bddBy_const (4 * b ^ 2)) (bddBy_sq (bddBy_Bu a b))
  exact bddBy_up (by norm_num) h

theorem bddBy_cGu (a b : ℤ) : BddBy 8 (cGu a b) := by
  show BddBy 8 (fun u v => b ^ 2
    * ((b ^ 2 * u * (a * u - 2 * b * v)) ^ 2 * (u * v * (u ^ 2 + a * u * v + b * v ^ 2))
      + 2 * (b ^ 2 * u * (a * u - 2 * b * v))
          * (u * (b ^ 2 * ((2 * b - a ^ 2) * u * v ^ 2 - a * u ^ 2 * v)
              + b * (a ^ 2 - 4 * b) * u * (2 * u ^ 2 - (u ^ 2 - b * v ^ 2))))
          * (u ^ 2 - b * v ^ 2)))
  have hA2 : BddBy 2 (fun u v => b ^ 2 * u * (a * u - 2 * b * v)) := by
    have h := bddBy_mul (bddBy_mul (bddBy_const (b ^ 2)) bddBy_fst)
      (bddBy_sub (bddBy_mul (bddBy_const a) bddBy_fst)
        (bddBy_mul (bddBy_const (2 * b)) bddBy_snd))
    exact bddBy_up (by norm_num) h
  have h₁ := bddBy_mul (bddBy_sq hA2) (bddBy_W a b)
  have h₂ := bddBy_mul (bddBy_mul (bddBy_mul (bddBy_const 2) hA2) (bddBy_Bu a b)) (bddBy_S b)
  have h := bddBy_mul (bddBy_const (b ^ 2))
    (bddBy_add (bddBy_up (by norm_num : (2 + 2 + 4 : ℕ) ≤ 8) h₁)
      (bddBy_up (by norm_num : (0 + 2 + 4 + 2 : ℕ) ≤ 8) h₂))
  exact bddBy_up (by norm_num) h

/-! ## The reduced multiplicative height on `ℚ` -/

/-- `H(u/v) = max(|u|, v)` on the reduced representation.  `ℚ` in mathlib is stored reduced
with positive denominator, so no reduction step is needed. -/
def hgt (x : ℚ) : ℕ := max x.num.natAbs x.den

theorem one_le_hgt (x : ℚ) : 1 ≤ hgt x :=
  le_trans x.den_pos (le_max_right _ _)

theorem hgt_cast (x : ℚ) : (hgt x : ℤ) = max |x.num| (x.den : ℤ) := by
  rw [hgt, Nat.cast_max, Int.natCast_natAbs]

/-! ## Obligation 2: the cancellation bound -/

/-- **Cancellation bound.**  If `F` and `G` are the duplication values at a reduced fraction
`u/v` and `k` is the factor removed when `(F, G)` is reduced to coprime projective coordinates
— i.e. `F = N * k` and `G = D * k` — then `k` divides the curve constant `4 b⁴ (a² − 4b)²`. -/
theorem dvd_Rcon_of_reduce {a b u v N D k : ℤ} (hcop : IsCoprime u v)
    (hF : Fpol b u v = N * k) (hG : Gpol a b u v = D * k) : k ∣ Rcon a b := by
  have hkv : k ∣ Rcon a b * v ^ 12 := by
    refine ⟨cFv a b u v * N + cGv a b u v * D, ?_⟩
    rw [bezout_v a b u v, hF, hG]; ring
  have hku : k ∣ Rcon a b * u ^ 12 := by
    refine ⟨cFu a b u v * N + cGu a b u v * D, ?_⟩
    rw [bezout_u a b u v, hF, hG]; ring
  obtain ⟨s, t, hst⟩ := (hcop.pow (m := 12) (n := 12))
  have : Rcon a b = s * (Rcon a b * u ^ 12) + t * (Rcon a b * v ^ 12) := by
    calc Rcon a b = Rcon a b * (s * u ^ 12 + t * v ^ 12) := by rw [hst]; ring
      _ = s * (Rcon a b * u ^ 12) + t * (Rcon a b * v ^ 12) := by ring
  rw [this]
  exact dvd_add (Dvd.dvd.mul_left hku s) (Dvd.dvd.mul_left hkv t)

/-! ## The combined estimate -/

private theorem abs_mul_abs_le {k R x : ℤ} (hk : |k| ≤ |R|) (hx : 0 ≤ x) : |k| * x ≤ |R| * x :=
  mul_le_mul_of_nonneg_right hk hx

set_option maxHeartbeats 1000000 in
/--
**The height estimate for the duplication map.**

If `b ≠ 0` and `a² − 4b ≠ 0` then there is a constant `C ≥ 1`, depending only on `a` and `b`,
such that whenever `z` is the value of the duplication map at `x`, i.e.
`z · 4x(x² + ax + b) = (x² − b)²` with `4x(x² + ax + b) ≠ 0`, one has `H(x)⁴ ≤ C · H(z)`.
-/
theorem duplication_height_core (a b : ℤ) (hb : b ≠ 0) (hd : a ^ 2 - 4 * b ≠ 0) :
    ∃ C : ℕ, 1 ≤ C ∧ ∀ x z : ℚ,
      z * ((4 : ℚ) * x * (x ^ 2 + a * x + b)) = (x ^ 2 - b) ^ 2 →
      hgt x ^ 4 ≤ C * hgt z := by
  obtain ⟨K₁, hK₁, hb₁⟩ := bddBy_cFv a b
  obtain ⟨K₂, hK₂, hb₂⟩ := bddBy_cGv a b
  obtain ⟨K₃, hK₃, hb₃⟩ := bddBy_cFu a b
  obtain ⟨K₄, hK₄, hb₄⟩ := bddBy_cGu a b
  have hRne : Rcon a b ≠ 0 := Rcon_ne_zero hb hd
  set K : ℤ := K₁ + K₂ + K₃ + K₄ + 1 with hKdef
  have hK1 : (1 : ℤ) ≤ K := by omega
  have widen : ∀ (K' : ℤ), K' ≤ K → ∀ (c M : ℤ), 1 ≤ M → |c| ≤ K' * M ^ 8 →
      |c| ≤ K * M ^ 8 := by
    intro K' hK' c M hM hc
    refine le_trans hc (mul_le_mul_of_nonneg_right hK' ?_)
    have : (0 : ℤ) ≤ M := le_trans zero_le_one hM
    positivity
  -- ## The integral estimate
  have main : ∀ u v N D : ℤ, IsCoprime u v → 0 < v → 0 < D → IsCoprime N D →
      N * Gpol a b u v = Fpol b u v * D → (max |u| v) ^ 4 ≤ 2 * K * max |N| D := by
    intro u v N D hcop hv hD hcopND heq
    have hMu : |u| ≤ max |u| v := le_max_left _ _
    have hMv : |v| ≤ max |u| v := by rw [abs_of_pos hv]; exact le_max_right _ _
    have hM1 : 1 ≤ max |u| v := le_trans hv (le_max_right _ _)
    have hM0 : (0 : ℤ) < max |u| v := lt_of_lt_of_le zero_lt_one hM1
    -- reduce the duplication pair to coprime projective coordinates
    have hdvd : D ∣ Gpol a b u v :=
      hcopND.symm.dvd_of_dvd_mul_left ⟨Fpol b u v, by rw [heq]; ring⟩
    obtain ⟨k, hk⟩ := hdvd
    have hFk : Fpol b u v = N * k := by
      have h2 : Fpol b u v * D = N * k * D := by rw [← heq, hk]; ring
      exact mul_right_cancel₀ (by omega) h2
    -- obligation 2: the cancellation is bounded by the curve constant
    have hkR : k ∣ Rcon a b := dvd_Rcon_of_reduce hcop hFk hk
    have hkabs : |k| ≤ |Rcon a b| :=
      Int.le_of_dvd (abs_pos.mpr hRne) ((abs_dvd _ _).mpr ((dvd_abs _ _).mpr hkR))
    have hH0 : 0 ≤ max |N| D := le_trans (abs_nonneg N) (le_max_left _ _)
    -- obligation 1: the unreduced values are large
    have step : ∀ w cF cG : ℤ, Rcon a b * w = cF * Fpol b u v + cG * Gpol a b u v →
        |cF| ≤ K * (max |u| v) ^ 8 → |cG| ≤ K * (max |u| v) ^ 8 →
        |w| ≤ 2 * K * (max |u| v) ^ 8 * max |N| D := by
      intro w cF cG hid hcF hcG
      have hfac : Rcon a b * w = k * (cF * N + cG * D) := by
        rw [hid, hFk, hk]; ring
      have h1 : |Rcon a b| * |w| = |k| * |cF * N + cG * D| := by
        rw [← abs_mul, ← abs_mul, hfac]
      have e1 : |cF * N| ≤ K * (max |u| v) ^ 8 * max |N| D := by
        rw [abs_mul]
        exact mul_le_mul hcF (le_max_left _ _) (abs_nonneg _) (by positivity)
      have e2 : |cG * D| ≤ K * (max |u| v) ^ 8 * max |N| D := by
        rw [abs_mul, abs_of_pos hD]
        exact mul_le_mul hcG (le_max_right _ _) (le_of_lt hD) (by positivity)
      have h2 : |cF * N + cG * D| ≤ 2 * K * (max |u| v) ^ 8 * max |N| D :=
        calc |cF * N + cG * D| ≤ |cF * N| + |cG * D| := abs_add_le _ _
          _ ≤ K * (max |u| v) ^ 8 * max |N| D + K * (max |u| v) ^ 8 * max |N| D :=
              add_le_add e1 e2
          _ = 2 * K * (max |u| v) ^ 8 * max |N| D := by ring
      have h3 : |Rcon a b| * |w| ≤ |Rcon a b| * (2 * K * (max |u| v) ^ 8 * max |N| D) := by
        rw [h1]
        calc |k| * |cF * N + cG * D| ≤ |Rcon a b| * |cF * N + cG * D| :=
              mul_le_mul_of_nonneg_right hkabs (abs_nonneg _)
          _ ≤ |Rcon a b| * (2 * K * (max |u| v) ^ 8 * max |N| D) :=
              mul_le_mul_of_nonneg_left h2 (abs_nonneg _)
      exact le_of_mul_le_mul_left h3 (abs_pos.mpr hRne)
    have hvbound : v ^ 12 ≤ 2 * K * (max |u| v) ^ 8 * max |N| D := by
      have h := step (v ^ 12) (cFv a b u v) (cGv a b u v) (bezout_v a b u v)
        (widen K₁ (by omega) _ _ hM1 (hb₁ u v _ hM1 hMu hMv))
        (widen K₂ (by omega) _ _ hM1 (hb₂ u v _ hM1 hMu hMv))
      calc v ^ 12 = |v ^ 12| := (abs_of_nonneg (le_of_lt (pow_pos hv 12))).symm
        _ ≤ _ := h
    have hubound : |u| ^ 12 ≤ 2 * K * (max |u| v) ^ 8 * max |N| D := by
      have h := step (u ^ 12) (cFu a b u v) (cGu a b u v) (bezout_u a b u v)
        (widen K₃ (by omega) _ _ hM1 (hb₃ u v _ hM1 hMu hMv))
        (widen K₄ (by omega) _ _ hM1 (hb₄ u v _ hM1 hMu hMv))
      calc |u| ^ 12 = |u ^ 12| := (abs_pow u 12).symm
        _ ≤ _ := h
    have hM12 : (max |u| v) ^ 12 ≤ 2 * K * (max |u| v) ^ 8 * max |N| D := by
      rcases max_cases |u| v with ⟨he, _⟩ | ⟨he, _⟩
      · rw [show (max |u| v) ^ 12 = |u| ^ 12 by rw [he]]; exact hubound
      · rw [show (max |u| v) ^ 12 = v ^ 12 by rw [he]]; exact hvbound
    have hcancel : (max |u| v) ^ 8 * (max |u| v) ^ 4
        ≤ (max |u| v) ^ 8 * (2 * K * max |N| D) :=
      calc (max |u| v) ^ 8 * (max |u| v) ^ 4 = (max |u| v) ^ 12 := by ring
        _ ≤ 2 * K * (max |u| v) ^ 8 * max |N| D := hM12
        _ = (max |u| v) ^ 8 * (2 * K * max |N| D) := by ring
    exact le_of_mul_le_mul_left hcancel (pow_pos hM0 8)
  -- ## From the integral estimate to the height inequality
  refine ⟨(2 * K).toNat, ?_, ?_⟩
  · omega
  intro x z hdup
  have hvpos : (0 : ℤ) < (x.den : ℤ) := by exact_mod_cast x.pos
  have hDpos : (0 : ℤ) < (z.den : ℤ) := by exact_mod_cast z.pos
  have hcopx : IsCoprime x.num ((x.den : ℤ)) := by
    rw [Int.isCoprime_iff_gcd_eq_one]
    simpa [Int.gcd] using x.reduced
  have hcopz : IsCoprime z.num ((z.den : ℤ)) := by
    rw [Int.isCoprime_iff_gcd_eq_one]
    simpa [Int.gcd] using z.reduced
  have hxnum : (x.num : ℚ) = x * (x.den : ℚ) := (Rat.mul_den_eq_num x).symm
  have hznum : (z.num : ℚ) = z * (z.den : ℚ) := (Rat.mul_den_eq_num z).symm
  have hrel : z.num * Gpol a b x.num ((x.den : ℤ))
      = Fpol b x.num ((x.den : ℤ)) * ((z.den : ℤ)) := by
    have h : ((z.num * Gpol a b x.num ((x.den : ℤ)) : ℤ) : ℚ)
        = ((Fpol b x.num ((x.den : ℤ)) * ((z.den : ℤ)) : ℤ) : ℚ) := by
      simp only [Gpol, Fpol]
      push_cast
      rw [hxnum, hznum]
      linear_combination ((x.den : ℚ) ^ 4 * (z.den : ℚ)) * hdup
    exact_mod_cast h
  have hmain := main x.num ((x.den : ℤ)) z.num ((z.den : ℤ)) hcopx hvpos hDpos hcopz hrel
  have hfin : ((hgt x : ℤ)) ^ 4 ≤ (((2 * K).toNat : ℕ) : ℤ) * (hgt z : ℤ) := by
    rw [hgt_cast, hgt_cast, Int.toNat_of_nonneg (by omega)]
    calc (max |x.num| ((x.den : ℤ))) ^ 4 ≤ 2 * K * max |z.num| ((z.den : ℤ)) := hmain
      _ = 2 * K * max |z.num| ((z.den : ℤ)) := rfl
  exact_mod_cast hfin

end R1
