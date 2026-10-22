import Mathlib

/-!
# Seed at `p = 19`: exact mod-19 arithmetic on the computed plus modular symbols

This mirrors `RequestProject/Seed17Symbols.lean`, with `a_19 = 4`, so `α ≡ 4` and `α⁻¹ ≡ 5 (mod 19)`.
The tables `[a/19]^+` and `[a/361]^+` were computed by `w3_p17/msl_sq.c`, normalised by the
receipt period `Ω^+`, and rounded to integers (worst distance to an integer `1.5·10⁻⁶`). Lean
checks only the finite arithmetic on these integers:

* the Hecke `U_19` distribution relation `Σ_j [(a+19j)/361]^+ = a_19 [a/19]^+ − [0]^+`;
* the low coefficients `ℓ_0 ≡ ℓ_1 ≡ 0` and `ℓ_2 ≡ 18 ≢ 0 (mod 19)` of the weight-two
  Mazur–Tate–Teitelbaum 19-adic L-function.

Here `u(a) = ((a^18 mod 361) − 1)/19 · 18⁻¹ (mod 19)`.
-/

namespace Seed19

/-- `[a/19]^+` for `a = 0, …, 18`; the entry at `a = 0` is unused. -/
def sym19 : List ℤ := [0, -6, 72, 42, -6, 42, -34, -34, -38, -38, -38, -38, -34, -34, 42, -6, 42, 72, -6]

/-- `[a/361]^+` for `a = 0, …, 360`; the entries with `19 ∣ a` are unused. -/
def sym361 : List ℤ := [0, -8, -36, 0, -23, 36, 74, 84, 182, 60, 167, -22, -11, 84, 57, 61, 151, 44, 61, 0, 101, 51, 100, 0, 33, -1, 43, 167, 68, -40, 60, 66, 66, 45, 125, 53, 20, -50, 0, 117, 27, 45, -141, 45, 102, 74, 13, -135, -83, -13, -19, -143, 66, -27, 36, 154, -24, 0, -141, 73, 1, -50, 151, -18, -63, -48, -192, 58, 16, -143, 32, 67, 82, -35, -95, -171, 0, 125, 73, 33, -12, -153, -79, -1, -40, -76, -19, 68, 184, -19, 0, -8, 66, -13, 82, 0, -45, 27, 14, 1, -64, -114, -197, -76, 13, -13, -19, 32, 80, -107, -45, -64, -162, -23, 0, -12, 51, -153, 117, 100, 184, 102, -12, -22, 182, -15, -114, -137, 14, -90, -107, -13, -12, 0, 1, -36, 67, -24, -47, -19, -137, -83, 16, -48, -135, -19, -197, 53, -171, 45, -95, 92, 0, 0, 44, -47, 92, -35, -11, -18, -192, -15, -12, 58, -79, -63, -94, 101, -94, 154, -90, 0, -27, 20, 57, -12, 1, 43, 80, -61, -61, -61, -61, 80, 43, 1, -12, 57, 20, -27, 0, -90, 154, -94, 101, -94, -63, -79, 58, -12, -15, -192, -18, -11, -35, 92, -47, 44, 0, 0, 92, -95, 45, -171, 53, -197, -19, -135, -48, 16, -83, -137, -19, -47, -24, 67, -36, 1, 0, -12, -13, -107, -90, 14, -137, -114, -15, 182, -22, -12, 102, 184, 100, 117, -153, 51, -12, 0, -23, -162, -64, -45, -107, 80, 32, -19, -13, 13, -76, -197, -114, -64, 1, 14, 27, -45, 0, 82, -13, 66, -8, 0, -19, 184, 68, -19, -76, -40, -1, -79, -153, -12, 33, 73, 125, 0, -171, -95, -35, 82, 67, 32, -143, 16, 58, -192, -48, -63, -18, 151, -50, 1, 73, -141, 0, -24, 154, 36, -27, 66, -143, -19, -13, -83, -135, 13, 74, 102, 45, -141, 45, 27, 117, 0, -50, 20, 53, 125, 45, 66, 66, 60, -40, 68, 167, 43, -1, 33, 0, 100, 51, 101, 0, 61, 44, 151, 61, 57, 84, -11, -22, 167, 60, 182, 84, 74, 36, -23, 0, -36, -8]

/-- The Hecke `U_19` distribution relation, with `a_19 = 4` and `[0]^+ = 0`. -/
def distributionHolds : Bool :=
  (List.range 18).all fun i =>
    let a := i + 1
    ((List.range 19).map fun j => sym361.getD (a + 19 * j) 0).sum == 4 * sym19.getD a 0

/-- `u(a) mod 19` for a unit `a mod 361`. -/
def uLog (a : ℕ) : ℕ := ((a ^ 18 % 361 - 1) / 19) * 18 % 19

/-- `ℓ_i mod 19`, with `α⁻¹ ≡ 5 (mod 19)`. -/
def ellMod19 (i : ℕ) : ℤ :=
  let ai : ℤ := 5
  (((List.range 361).filter fun a => a % 19 != 0).map fun a =>
      (ai ^ 2 * sym361.getD a 0 - ai ^ 3 * sym19.getD (a % 19) 0) * (Nat.choose (uLog a) i : ℤ)).sum % 19

theorem alpha_inv : (4 * 5 : ℤ) % 19 = 1 := by decide
theorem distribution_relation : distributionHolds = true := by decide +kernel
theorem ell_low_mod19 : ellMod19 0 = 0 ∧ ellMod19 1 = 0 ∧ ellMod19 2 = 18 := by
  decide +kernel

end Seed19
