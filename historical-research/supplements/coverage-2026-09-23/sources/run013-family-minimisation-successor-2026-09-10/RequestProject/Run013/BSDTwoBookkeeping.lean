/-
Run013 — `BSDTwoBookkeeping.lean`

**LEVEL C.**  The elementary/exact arithmetic layer of `BSD_CHAIN.md` §§3–5.

Three genuinely unconditional pieces are proved here:

* the arithmetic reason for `c_q(E_q) = 2`: the normalized `I_0^*` component polynomial
  `T (T^2 - 15 T + 64)` has exactly one root modulo `q`, because the discriminant of the
  quadratic factor is `-31` and `(-31/q) = -1`;
* the arithmetic reason for `E_q(Q)_tors ≃ Z/2Z` at the prime `2`: the only rational
  two-torsion is `(0,0)` and there is no rational point of order `4` above it;
* the **period normalization**: the invariant differential of the nonminimal short
  descent model is exactly one half of the Néron differential of the minimal `62a1`
  model.  This factor of two is kept explicit and is never silently discarded.

The final `2`-adic valuation identity is stated with the analytic input, the Tamagawa
input and the torsion input as ordinary theorem hypotheses.  It is labelled

    CONDITIONAL_ON_EXTERNAL_INPUT

because `v_2(L(E_q,1)/Omega(E_q)) = 0` rests on Zhai's non-vanishing theorem and the
Tamagawa numbers rest on Tate's algorithm, neither of which is available in mathlib.
No axiom is introduced: the hypotheses are ordinary binders.
-/
import RequestProject.Run013.Family
import RequestProject.Run013.Curves
import RequestProject.Run013.FullTwoSelmer

namespace Run013

/-! ## `c_q(E_q) = 2`: the component polynomial has exactly one root -/

/-- The quadratic factor `T^2 - 15 T + 64` of the normalized `I_0^*` component polynomial
has **no** root modulo `q`, because `(2T - 15)^2 = -31` would then be a square. -/
theorem cq_component_quadratic_no_root {q : ℕ} [Fact q.Prime]
    (hns : ¬ IsSquare ((-31 : ℤ) : ZMod q)) (T : ZMod q) :
    T ^ 2 - 15 * T + 64 ≠ 0 := by
  intro h
  refine hns ⟨2 * T - 15, ?_⟩
  push_cast
  linear_combination -4 * h

/-- Hence `T (T^2 - 15 T + 64)` has exactly one root modulo `q`, namely `T = 0`;
this is the exact reason the handoff gives for `c_q(E_q) = 2`. -/
theorem cq_component_root_iff {q : ℕ} [Fact q.Prime]
    (hns : ¬ IsSquare ((-31 : ℤ) : ZMod q)) (T : ZMod q) :
    T * (T ^ 2 - 15 * T + 64) = 0 ↔ T = 0 := by
  constructor
  · intro h
    rcases mul_eq_zero.mp h with h1 | h1
    · exact h1
    · exact absurd h1 (cq_component_quadratic_no_root hns T)
  · rintro rfl; ring

/-! ## `E_q(Q)_tors` at the prime `2` -/

/-- There is no rational point of order `4` above `(0,0)` on `E_q`:
a halving of `(0,0)` would need `x^2 = 64 q^2`, and neither `x = 8q` nor `x = -8q` gives a
rational `y`. -/
theorem no_rational_four_torsion {q : ℕ} (hq : q.Prime) (x y : ℚ)
    (hx : x ^ 2 = 64 * (q : ℚ) ^ 2)
    (h : y ^ 2 = x ^ 3 - 15 * q * x ^ 2 + 64 * (q : ℚ) ^ 2 * x) : False := by
  have hqpos : (0 : ℚ) < q := by exact_mod_cast hq.pos
  have hq0 : (q : ℚ) ≠ 0 := ne_of_gt hqpos
  have hcases : x = 8 * q ∨ x = -(8 * q) := by
    have : (x - 8 * q) * (x + 8 * q) = 0 := by linear_combination hx
    rcases mul_eq_zero.mp this with h1 | h1
    · exact Or.inl (by linarith)
    · exact Or.inr (by linarith)
  rcases hcases with rfl | rfl
  · -- `y^2 = 64 q^3`, so `q` would be a rational square
    have hy : y ^ 2 = 64 * (q : ℚ) ^ 3 := by linear_combination h
    refine not_isSquare_prime_rat hq ⟨y / (8 * q), ?_⟩
    field_simp
    linear_combination -hy
  · -- `y^2 < 0`
    have hy : y ^ 2 = -(1984 * (q : ℚ) ^ 3) := by linear_combination h
    nlinarith [sq_nonneg y, pow_pos hqpos 3]

/-- The only rational two-torsion point of `E_q` is `(0,0)`; combined with
`no_rational_four_torsion` this is the `2`-primary part of
`E_q(Q)_tors ≃ Z/2Z`, i.e. `v_2(# E_q(Q)_tors) = 1`. -/
theorem Eq_two_torsion_unique {q : ℕ} (hq : 0 < q) (x : ℚ) :
    x ^ 3 - 15 * (q : ℚ) * x ^ 2 + 64 * (q : ℚ) ^ 2 * x = 0 ↔ x = 0 :=
  Eq_two_torsion (q : ℚ) x (by exact_mod_cast hq)

/-! ## Period normalization: the factor of two in the differential -/

/-- **The descent-model differential is one half of the Néron differential.**

On the minimal model `E : v^2 + u v + v = u^3 - u^2 - u + 1` the Néron differential is
`omega = du / (2v + u + 1)`.  Under the frozen change of variables `X = 4(u+1)`,
`Y = 8v + 4u + 4` one has `dX = 4 du` and `2Y = 8 (2v + u + 1)`, hence

    dX / (2Y) = (1/2) * omega.

The nonminimal short model must therefore never be used as if it carried the Néron
differential. -/
theorem descent_differential_is_half_neron (u v Y : ℚ)
    (hY : Y = 8 * v + 4 * u + 4)
    (hs : 2 * v + u + 1 ≠ 0) :
    (4 : ℚ) / (2 * Y) = (1 / 2) * (1 / (2 * v + u + 1)) := by
  subst hY
  have h8 : (8 : ℚ) * (2 * v + u + 1) ≠ 0 := by
    simpa using hs
  rw [show 2 * (8 * v + 4 * u + 4) = 8 * (2 * v + u + 1) from by ring]
  field_simp
  norm_num

/-! ## The `2`-adic Tamagawa product -/

/-- `c_2 = 2`, `c_31 = 1`, `c_q = 2`, hence `v_2(∏_p c_p(E_q)) = 2`. -/
theorem tamagawa_product_valuation : padicValNat 2 (2 * 1 * 2) = 2 := by
  show padicValNat 2 (2 ^ 2) = 2
  exact padicValNat.prime_pow 2

/-! ## The BSD-at-2 valuation identity -/

/-- **`CONDITIONAL_ON_EXTERNAL_INPUT`.**

The exact `2`-adic bookkeeping of `BSD_CHAIN.md` §5.  In analytic rank zero the regulator
is `1` and

    # Sha(E_q)_an = (L(E_q,1)/Omega(E_q)) * (# E_q(Q)_tors)^2 / ∏_p c_p(E_q),

so its `2`-adic valuation is `vL + 2 * vTors - vTam`.

The three inputs are hypotheses, not axioms:

* `hL`  : `v_2(L(E_q,1)/Omega(E_q)) = 0`   — Zhai, *Non-vanishing theorems for quadratic
  twists of elliptic curves*, Asian J. Math. 20 (2016), Theorem 1.5.  Not formalized.
* `hTam`: `v_2(∏_p c_p(E_q)) = 2`          — Tate's algorithm; the arithmetic reason at the
  prime `q` is proved above in `cq_component_root_iff`.  Not formalized in full.
* `hTors`: `v_2(# E_q(Q)_tors) = 1`        — the `2`-primary part is proved above; the
  absence of odd torsion is external.

Given them, the `2`-adic valuation of the analytic order of Sha is `0`. -/
theorem sha_analytic_two_valuation (vL vTors vTam : ℤ)
    (hL : vL = 0) (hTors : vTors = 1) (hTam : vTam = 2) :
    vL + 2 * vTors - vTam = 0 := by
  subst hL; subst hTors; subst hTam; ring

end Run013
