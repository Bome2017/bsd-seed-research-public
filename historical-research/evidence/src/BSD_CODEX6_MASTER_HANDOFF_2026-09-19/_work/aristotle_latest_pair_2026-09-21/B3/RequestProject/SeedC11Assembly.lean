import Mathlib

/-!
# Exact assembly of the 11-primary test quantity `C₁₁` for the seed curve

For the seed curve

    E : y² = x³ - 22735 x² + 106272484 x,   N = 2³·3·2243·4547²·5843 = 6503188012738584,

the prime `11` is a prime of good ordinary reduction: `a₁₁ = -2` (so `#Ẽ(F₁₁) = 14`), and
`11 ∤ a₁₁`.  Write `L₁₁(E,T) ∈ Z₁₁[[T]]` for the Mazur–Swinnerton-Dyer `11`-adic `L`-function of
`E` in the `α`-ordinary normalisation, and

    C₁₁ := [T²] L₁₁(E,T)  (mod 11).

This file contains the **exact finite arithmetic** that turns modular-symbol values into `C₁₁`,
machine-checked.  It does *not* contain the modular symbols themselves: those are real numbers
produced by a numerical run, and they are the one missing input (see
`ARISTOTLE_B_C11_SPEC.md` in the project root).

## What is proved here

Let `p` be `7` or `11`, let `ω` be the Teichmüller lift modulo `p²`, and for `u` prime to `p`
let `j(u) ∈ Z/p` be defined by `u ≡ ω(u)·(1+p)^{j(u)} (mod p²)` (`jlog` below; `jlog_spec_*`).
With `S b := [b/p²]⁺` and `s a := [a/p]⁺` the plus modular symbols in the `ω₁` normalisation, the
depth-one Mazur–Tate approximation is

    P(T) = ∑_{u ∈ (Z/p²)ˣ} ( α^{-2} S u - α^{-3} s (u mod p) ) (1+T)^{j(u)},

and Stein–Wuthrich Prop. 3.5 gives `[T²]L_p ≡ [T²]P (mod p)`.  Three finite facts, all checked
by `decide` below, reduce `[T²]P mod p` to a short weighted sum of symbols at denominator `p²`:

* `level_drop_eleven` / `level_drop_seven`: for each residue `a` prime to `p`, the fibre sum
  `∑_{u ≡ a (p)} C(j(u),2)` vanishes mod `p` (it equals `C(p,3) = p·(p-1)(p-2)/6`).  Hence the
  lower-level symbols `s a` contribute `0`, whatever their values and whatever `α^{-3}` is.
* `jlog_neg_eleven` / `jlog_neg_seven`: `j(p² - b) = j(b)`.  Since the plus symbols satisfy
  `S (p² - b) = S b`, the sum folds onto `1 ≤ b ≤ (p²-1)/2`, doubling each coefficient
  (`fold_coeff_eleven`, `fold_coeff_seven`).
* the folded coefficient of `S b` is `α^{-2}·j(b)·(j(b)-1) mod p`, which vanishes exactly when
  `j(b) ∈ {0,1}`.  For `p = 11` this leaves **45** symbols (`supp_eleven_length`), for `p = 7`
  it leaves **15**.

For the seed curve `a_p = -2` at both `p = 7` and `p = 11`, so the unit root satisfies
`α ≡ -2 (mod p)` and `α^{-2} ≡ 2 (mod 7)`, `α^{-2} ≡ 3 (mod 11)` (`alphaInvSq_*`).

The resulting weighted sum is `C p c S` below (`c = α^{-2}`).  Two consequences are recorded:

* `C_seven_of_certificate`: fed with the three group sums `-165, -512, 314` of the retained
  7-primary run, the assembly returns `1`, i.e. it **reproduces** the retained premise
  `[T²]L₇ ≡ 1 (mod 7)` in the `ω₁` convention.  This is an independent check of the assembly,
  derived here from scratch and matching the retained certificate's weight pattern
  (`table_seven`: weights `5` on `{2,4,11,13,22,23}`, `4` on `{6,9,10,15,16,24}`, `3` on
  `{12,17,20}`).
* `table_eleven`: the corresponding 45 weighted symbols at denominator `121` for `p = 11`.
  `C 11 3 S` is the verifier: once the 45 numbers `S b = [b/121]⁺ ∈ (1/1024)Z` are certified,
  `C 11 3 S` *is* `C₁₁`, and `C₁₁ ≠ 0` is the retained sufficient test for `Ш(E/Q)[11^∞] = 0`.

Nothing here asserts a value of `C₁₁`, and nothing here proves the Iwasawa-theoretic implication
`C₁₁ ≠ 0 ⟹ Ш[11^∞] = 0`; that implication is the retained 7-primary argument specialised to 11
and is used only as context.
-/

set_option maxRecDepth 100000

namespace SeedC11

/-! ## Teichmüller lift and the `(1+p)`-logarithm modulo `p²` -/

/-- Teichmüller representative of `a` modulo `p²`: `ω(a) = a^p mod p²`. -/
def teich (p a : ℕ) : ℕ := a ^ p % (p * p)

/-- The unique `j < p` with `a ≡ ω(a)·(1+p)^j (mod p²)`, for `a` prime to `p`. -/
def jlog (p b : ℕ) : ℕ :=
  ((List.range p).find? fun j => (teich p b * (1 + p) ^ j) % (p * p) = b % (p * p)).getD 0

theorem teich_pow_eleven : ∀ b ∈ List.range 121, ¬ (11 ∣ b) → (teich 11 b) ^ 10 % 121 = 1 := by
  decide

theorem teich_mod_eleven : ∀ b ∈ List.range 121, ¬ (11 ∣ b) → (teich 11 b) % 11 = b % 11 := by
  decide

theorem jlog_spec_eleven :
    ∀ b ∈ List.range 121, ¬ (11 ∣ b) → (teich 11 b * 12 ^ jlog 11 b) % 121 = b % 121 := by
  decide

theorem jlog_lt_eleven : ∀ b ∈ List.range 121, ¬ (11 ∣ b) → jlog 11 b < 11 := by decide

theorem jlog_spec_seven :
    ∀ b ∈ List.range 49, ¬ (7 ∣ b) → (teich 7 b * 8 ^ jlog 7 b) % 49 = b % 49 := by decide

/-- `j` is invariant under `b ↦ p² - b`; this is what makes the plus symbols fold. -/
theorem jlog_neg_eleven :
    ∀ b ∈ List.range 121, 1 ≤ b → ¬ (11 ∣ b) → jlog 11 (121 - b) = jlog 11 b := by decide

theorem jlog_neg_seven :
    ∀ b ∈ List.range 49, 1 ≤ b → ¬ (7 ∣ b) → jlog 7 (49 - b) = jlog 7 b := by decide

/-! ## The lower-level term drops modulo `p` -/

/-- For each residue `a` prime to `11`, `∑_{u ≡ a (11)} C(j(u),2) ≡ 0 (mod 11)`.
Consequently the symbols at denominator `11` contribute nothing to `[T²]P mod 11`. -/
theorem level_drop_eleven : ∀ a ∈ List.range 11, ¬ (11 ∣ a) →
    (((List.range 121).filter fun u => decide (u % 11 = a)).map
      fun u => ((jlog 11 u).choose 2 : ZMod 11)).sum = 0 := by decide

theorem level_drop_seven : ∀ a ∈ List.range 7, ¬ (7 ∣ a) →
    (((List.range 49).filter fun u => decide (u % 7 = a)).map
      fun u => ((jlog 7 u).choose 2 : ZMod 7)).sum = 0 := by decide

/-! ## Unit root of the Hecke polynomial at `p` -/

/-- `a₁₁ = -2` for the seed curve, so the unit root is `α ≡ -2 (mod 11)` and `α^{-2} ≡ 3`. -/
theorem alphaInvSq_eleven : ((-2 : ZMod 11)) ^ 2 * 3 = 1 := by decide

/-- `a₇ = -2` for the seed curve, so `α^{-2} ≡ 2 (mod 7)`. -/
theorem alphaInvSq_seven : ((-2 : ZMod 7)) ^ 2 * 2 = 1 := by decide

/-- `α^{-1} ≡ 5 (mod 11)`. -/
theorem alphaInv_eleven : ((-2 : ZMod 11)) * 5 = 1 := by decide

/-- The interpolation factor `ε₁₁ = (1 - α^{-1})²` is an `11`-unit, as the retained leading-term
argument at `p = 7` requires of `ε₇`. -/
theorem epsilon_eleven_ne_zero : ((1 : ZMod 11) - 5) ^ 2 ≠ 0 := by decide

/-! ## The folded weights -/

/-- Folded coefficient of the symbol `[b/p²]⁺` in `[T²]P`, with `c = α^{-2}`. -/
def wtF (p : ℕ) (c : ZMod p) (b : ℕ) : ZMod p :=
  c * ((jlog p b : ZMod p) * ((jlog p b : ZMod p) - 1))

/-- Folding `u` and `p² - u` doubles `c·C(j,2)` into `c·j(j-1)`. -/
theorem fold_coeff_eleven : ∀ b ∈ List.range 61, 1 ≤ b → ¬ (11 ∣ b) →
    (3 : ZMod 11) * ((jlog 11 b).choose 2 : ZMod 11)
      + 3 * ((jlog 11 (121 - b)).choose 2 : ZMod 11) = wtF 11 3 b := by decide

theorem fold_coeff_seven : ∀ b ∈ List.range 25, 1 ≤ b → ¬ (7 ∣ b) →
    (2 : ZMod 7) * ((jlog 7 b).choose 2 : ZMod 7)
      + 2 * ((jlog 7 (49 - b)).choose 2 : ZMod 7) = wtF 7 2 b := by decide

/-- The symbols actually needed: `1 ≤ b ≤ (p²-1)/2`, `p ∤ b`, nonzero weight. -/
def suppF (p : ℕ) (c : ZMod p) : List ℕ :=
  (List.range (p * p / 2 + 1)).filter fun b =>
    decide (1 ≤ b) && decide (¬ p ∣ b) && decide (wtF p c b ≠ 0)

/-- The support with its weights. -/
def tableF (p : ℕ) (c : ZMod p) : List (ℕ × ZMod p) := (suppF p c).map fun b => (b, wtF p c b)

/-- The assembly: `C p c S` is `[T²]L_p mod p` computed from the symbols `S b = [b/p²]⁺`. -/
def C (p : ℕ) (c : ZMod p) (S : ℕ → ℤ) : ZMod p :=
  ((tableF p c).map fun q => q.2 * (S q.1 : ZMod p)).sum

/-! ## `p = 11`: the 45 symbols at denominator 121 and their weights -/

theorem supp_eleven_length : (suppF 11 3).length = 45 := by decide

theorem supp_eleven : suppF 11 3 =
    [2, 5, 6, 7, 8, 10, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 28, 29, 30, 31, 32, 34,
     35, 37, 38, 41, 42, 43, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 56, 57, 58, 59, 60] := by
  decide

theorem table_eleven : tableF 11 3 =
    [(2,2), (5,3), (6,2), (7,7), (8,5), (10,6), (14,3), (15,3), (16,6), (17,3), (18,2), (19,7),
     (20,5), (21,7), (23,6), (24,5), (25,3), (26,5), (28,6), (29,7), (30,6), (31,6), (32,3),
     (34,7), (35,6), (37,6), (38,7), (41,2), (42,3), (43,5), (45,3), (46,3), (47,5), (48,6),
     (49,5), (50,7), (51,3), (52,6), (53,7), (54,2), (56,5), (57,7), (58,7), (59,5), (60,5)] := by
  decide

/-- The weight of `[b/121]⁺` depends only on `j(b)`: the five classes are
`j ∈ {6}` ↦ `2`, `{5,7}` ↦ `5`, `{4,8}` ↦ `3`, `{3,9}` ↦ `7`, `{2,10}` ↦ `6`. -/
theorem weight_classes_eleven : ∀ b ∈ suppF 11 3,
    wtF 11 3 b = (if jlog 11 b = 6 then 2 else if jlog 11 b = 5 ∨ jlog 11 b = 7 then 5
      else if jlog 11 b = 4 ∨ jlog 11 b = 8 then 3
      else if jlog 11 b = 3 ∨ jlog 11 b = 9 then 7 else 6) := by decide

/-! ## `p = 7`: reproduction of the retained 7-primary certificate -/

theorem supp_seven_length : (suppF 7 2).length = 15 := by decide

theorem table_seven : tableF 7 2 =
    [(2,5), (4,5), (6,4), (9,4), (10,4), (11,5), (12,3), (13,5), (15,4), (16,4), (17,3), (20,3),
     (22,5), (23,5), (24,4)] := by decide

/-- **Reproduction of the retained 7-primary premise.**  The retained run reports the three group
sums of its certified symbols at denominator `49` as `-165`, `-512`, `314`.  Fed with those, the
assembly derived here independently returns `[T²]L₇ ≡ 1 (mod 7)`. -/
theorem C_seven_of_certificate (S : ℕ → ℤ)
    (h5 : S 2 + S 4 + S 11 + S 13 + S 22 + S 23 = -165)
    (h4 : S 6 + S 9 + S 10 + S 15 + S 16 + S 24 = -512)
    (h3 : S 12 + S 17 + S 20 = 314) :
    C 7 2 S = 1 := by
  have e5 : ((S 2 + S 4 + S 11 + S 13 + S 22 + S 23 : ℤ) : ZMod 7) = ((-165 : ℤ) : ZMod 7) := by
    rw [h5]
  have e4 : ((S 6 + S 9 + S 10 + S 15 + S 16 + S 24 : ℤ) : ZMod 7) = ((-512 : ℤ) : ZMod 7) := by
    rw [h4]
  have e3 : ((S 12 + S 17 + S 20 : ℤ) : ZMod 7) = ((314 : ℤ) : ZMod 7) := by rw [h3]
  push_cast at e5 e4 e3
  simp only [C, table_seven, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]
  linear_combination (norm := (ring_nf; decide)) (5 : ZMod 7) * e5 + 4 * e4 + 3 * e3

/-! ## The `p = 11` verifier, in grouped form -/

/-- `C 11 3 S` in the grouped form the numerical run should be checked against: the five weight
classes of `table_eleven`. -/
theorem C_eleven_grouped (S : ℕ → ℤ) :
    C 11 3 S =
      2 * ((S 2 + S 6 + S 18 + S 41 + S 54 : ℤ) : ZMod 11)
    + 3 * ((S 5 + S 14 + S 15 + S 17 + S 25 + S 32 + S 42 + S 45 + S 46 + S 51 : ℤ) : ZMod 11)
    + 5 * ((S 8 + S 20 + S 24 + S 26 + S 43 + S 47 + S 49 + S 56 + S 59 + S 60 : ℤ) : ZMod 11)
    + 6 * ((S 10 + S 16 + S 23 + S 28 + S 30 + S 31 + S 35 + S 37 + S 48 + S 52 : ℤ) : ZMod 11)
    + 7 * ((S 7 + S 19 + S 21 + S 29 + S 34 + S 38 + S 50 + S 53 + S 57 + S 58 : ℤ) : ZMod 11) := by
  simp only [C, table_eleven, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]
  push_cast
  ring

end SeedC11
