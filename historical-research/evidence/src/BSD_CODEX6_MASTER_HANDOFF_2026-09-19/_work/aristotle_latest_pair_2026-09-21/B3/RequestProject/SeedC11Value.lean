import RequestProject.SeedC11Assembly

/-!
# The computed value: `C₁₁ = 8` for the seed curve

This file records the numerical certificate produced in this session and evaluates the assembly of
`RequestProject/SeedC11Assembly.lean` on it.

The plus modular symbols of

    E : y² = x³ − 22735x² + 106272484x,   N = 6503188012738584,   ω₁ = 0.02804490151943640444830940180793…

at denominators `49` and `121` were computed from

    [a/m]⁺ = −(Re λ(a/m))/ω₁,   Re λ(a/m) = −c_a − w·c_B,   B ≡ −(aN)^{−1} (mod m),   w = +1,
    c_a = Σ_{n ≤ X} (a_n/n) cos(2πna/m) e^{−2πn/(m√N)},   X = 4·10^{10},

using `a_p` for all `1 711 955 433` primes `p < 4·10^{10}` (PARI 2.17.2 `Fl_elltrace` on the short
model, bad primes `2, 3, 2243, 4547, 5843` special-cased), multiplicative reconstruction of `a_n`,
and Kahan-summed bucket sums; see `scripts/c11/` and `ARISTOTLE_B_C11_SPEC.md`. The truncation
satisfies the a-priori tail bound `2·tail/ω₁ < 1/2048`, and every computed value came out within
`8.2·10^{−11}` of an **integer** (identification window `1/2048 ≈ 4.9·10^{−4}`; the values are also
unchanged when the truncation is lowered to `2.28·10^{10}`). The sign convention is the retained
project's, i.e. `[0]⁺ = +L(E,1)/ω₁`; this is the convention in which the retained `p = 5` and
`p = 7` certificates are stated, and both were reproduced by the same run.

The numbers below are therefore an *input* to Lean: they are the output of a floating-point
computation with an explicit error budget, not of a formal proof. What Lean checks here is the
exact finite arithmetic downstream of them.
-/

set_option maxRecDepth 100000

namespace SeedC11

/-- Look a value up in a table of modular symbols. -/
def ofTable (t : List (ℕ × ℤ)) (b : ℕ) : ℤ := (t.lookup b).getD 0

/-! ## `p = 7`: the retained certificate, reproduced value by value -/

/-- `[b/49]⁺` for the 15 `b` that carry a nonzero weight, in the retained sign convention. -/
def sym49 : List (ℕ × ℤ) :=
  [(2, 36), (4, 7), (6, -130), (9, 7), (10, -84), (11, -50), (12, 70), (13, 63), (15, -158),
   (16, -84), (17, 102), (20, 142), (22, -158), (23, -63), (24, -63)]

/-- The three group sums of the retained 7-primary certificate, recovered from the recomputed
symbols. -/
theorem sym49_group_sums :
    (ofTable sym49 2 + ofTable sym49 4 + ofTable sym49 11 + ofTable sym49 13 + ofTable sym49 22
        + ofTable sym49 23 = -165)
  ∧ (ofTable sym49 6 + ofTable sym49 9 + ofTable sym49 10 + ofTable sym49 15 + ofTable sym49 16
        + ofTable sym49 24 = -512)
  ∧ (ofTable sym49 12 + ofTable sym49 17 + ofTable sym49 20 = 314) := by
  refine ⟨by decide, by decide, by decide⟩

/-- `[T²]L₇ ≡ 1 (mod 7)`: the retained 7-primary premise, recomputed here end to end. -/
theorem C_seven_value : C 7 2 (ofTable sym49) = 1 := by decide

/-! ## `p = 11`: the 45 symbols at denominator 121 and the value of `C₁₁` -/

/-- `[b/121]⁺` for the 45 `b` that carry a nonzero weight, in the retained sign convention. -/
def sym121 : List (ℕ × ℤ) :=
  [(2, -133), (5, 134), (6, 110), (7, 142), (8, 47), (10, 134), (14, 83), (15, -40), (16, 85),
   (17, 52), (18, -121), (19, -13), (20, 44), (21, -149), (23, -59), (24, 47), (25, -133),
   (26, 160), (28, 45), (29, 20), (30, -182), (31, 83), (32, 110), (34, 80), (35, -97),
   (37, -40), (38, -32), (41, -18), (42, -182), (43, -73), (45, 45), (46, -18), (47, -123),
   (48, -5), (49, -73), (50, -129), (51, -121), (52, 138), (53, -123), (54, 52), (56, -32),
   (57, 114), (58, 44), (59, 142), (60, -149)]

/-- The five weight-class sums of the 45 symbols. -/
theorem sym121_group_sums :
    (ofTable sym121 2 + ofTable sym121 6 + ofTable sym121 18 + ofTable sym121 41
        + ofTable sym121 54 = -110)
  ∧ (ofTable sym121 5 + ofTable sym121 14 + ofTable sym121 15 + ofTable sym121 17
        + ofTable sym121 25 + ofTable sym121 32 + ofTable sym121 42 + ofTable sym121 45
        + ofTable sym121 46 + ofTable sym121 51 = -70)
  ∧ (ofTable sym121 8 + ofTable sym121 20 + ofTable sym121 24 + ofTable sym121 26
        + ofTable sym121 43 + ofTable sym121 47 + ofTable sym121 49 + ofTable sym121 56
        + ofTable sym121 59 + ofTable sym121 60 = -10)
  ∧ (ofTable sym121 10 + ofTable sym121 16 + ofTable sym121 23 + ofTable sym121 28
        + ofTable sym121 30 + ofTable sym121 31 + ofTable sym121 35 + ofTable sym121 37
        + ofTable sym121 48 + ofTable sym121 52 = 102)
  ∧ (ofTable sym121 7 + ofTable sym121 19 + ofTable sym121 21 + ofTable sym121 29
        + ofTable sym121 34 + ofTable sym121 38 + ofTable sym121 50 + ofTable sym121 53
        + ofTable sym121 57 + ofTable sym121 58 = -46) := by
  refine ⟨by decide, by decide, by decide, by decide, by decide⟩

/-- **The value.** `C₁₁ = [T²]L₁₁(E,T) ≡ 8 (mod 11)` in the `ω₁` normalisation. -/
theorem C_eleven_value : C 11 3 (ofTable sym121) = 8 := by decide

/-- **`C₁₁ ≠ 0`.** -/
theorem C_eleven_ne_zero : C 11 3 (ofTable sym121) ≠ 0 := by decide

/-- In the retained Néron / full-real-period normalisation the symbols are halved, so the value is
`8/2 = 4` — also nonzero. -/
theorem C_eleven_value_neron : (8 : ZMod 11) * 2⁻¹ = 4 := by decide

end SeedC11
