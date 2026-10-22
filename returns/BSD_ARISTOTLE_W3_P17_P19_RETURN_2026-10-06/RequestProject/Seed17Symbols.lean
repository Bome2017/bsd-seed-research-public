import Mathlib

/-!
# Seed at `p = 17`: exact mod-17 arithmetic on the computed plus modular symbols

The tables below were produced by `w3_p17/msl_sq.c` and `w3_p17/analyze_p17.py`, in floating point:
* `sym17 a = [a/17]^+`, the plus modular symbols of the seed `[0,-22735,0,106272484,0]` at denominator
  `17`;
* `sym289 a = [a/289]^+`, the same at denominator `289`.

Each symbol is normalised by the receipt period `Ω^+`, rounded to the nearest integer, and
indexed by `a mod 17` (resp. `a mod 289`). Entries with `17 ∣ a` are set to `0` and never used.
The Lean statements check the **finite arithmetic** done on these integers. They do not check the
analytic computation that produced the integers. That computation is validated separately
(see `W3_P17_REPORT.md`).

The measure is the Mazur–Tate–Teitelbaum measure, with `α ≡ a_17 = -6 ≡ 11 (mod 17)` and
`[0]^+ = 0`:

  `μ(a + 289 ℤ_17) = α⁻² [a/289]^+ − α⁻³ [a/17]^+`.

Its low coefficients are `ℓ_i ≡ Σ_{a ∈ (ℤ/289)^×} μ(a) · binom(u(a), i) (mod 17)`, where
`u(a) = log⟨a⟩ / log(1+17) mod 17 = ((a^16 mod 289) − 1)/17 · 16⁻¹ (mod 17)`.
-/

namespace Seed17

/-- `[a/17]^+` for `a = 0, …, 16`; the entry at `a = 0` is unused. -/
def sym17 : List ℤ := [0, -84, 420, -154, -84, 10, 10, -154, 36, 36, -154, 10, 10, -84, -154, 420, -84]

/-- `[a/289]^+` for `a = 0, …, 288`; the entries with `17 ∣ a` are unused. -/
def sym289 : List ℤ := [0, 18, -43, -111, 239, -109, -240, 212, 70, 154, -222, 73, -114, 131, 156, 262, 239, 0, 44, -238, -39, -18, 77, 226, 67, 154, 70, 47, 84, 102, 228, 277, -43, 45, 0, -79, -226, 87, -20, 84, -45, 152, 70, 94, 308, -109, 128, -109, -77, -238, 156, 0, -18, -63, 308, -41, -30, 7, 277, 94, 115, -39, 102, 41, 18, 152, -226, -221, 0, -109, -103, 89, 45, 73, 128, -111, 115, 92, 156, 41, 7, -221, -82, -63, 131, 0, -91, -275, 47, -79, 105, -114, 87, 92, -298, -77, -15, -15, -33, 67, -103, -41, 0, 158, -307, -21, 158, -240, 77, 89, -298, -199, -82, -313, -45, -91, 81, -275, 97, 0, -20, -136, -222, 97, -37, -30, -21, -199, -171, 81, -37, -313, 44, 212, -307, -33, 0, 228, -136, 0, 156, 226, 105, 0, -171, -171, 0, 105, 226, 156, 0, -136, 228, 0, -33, -307, 212, 44, -313, -37, 81, -171, -199, -21, -30, -37, 97, -222, -136, -20, 0, 97, -275, 81, -91, -45, -313, -82, -199, -298, 89, 77, -240, 158, -21, -307, 158, 0, -41, -103, 67, -33, -15, -15, -77, -298, 92, 87, -114, 105, -79, 47, -275, -91, 0, 131, -63, -82, -221, 7, 41, 156, 92, 115, -111, 128, 73, 45, 89, -103, -109, 0, -221, -226, 152, 18, 41, 102, -39, 115, 94, 277, 7, -30, -41, 308, -63, -18, 0, 156, -238, -77, -109, 128, -109, 308, 94, 70, 152, -45, 84, -20, 87, -226, -79, 0, 45, -43, 277, 228, 102, 84, 47, 70, 154, 67, 226, 77, -18, -39, -238, 44, 0, 239, 262, 156, 131, -114, 73, -222, 154, 70, 212, -240, -109, 239, -111, -43, 18]

/-- Hecke `U_17` distribution relation: `Σ_j [(a+17j)/289]^+ = a_17 [a/17]^+ − [0]^+`, with
`a_17 = -6` and `[0]^+ = 0`. -/
def distributionHolds : Bool :=
  (List.range 16).all fun i =>
    let a := i + 1
    ((List.range 17).map fun j => sym289.getD (a + 17 * j) 0).sum == -6 * sym17.getD a 0

/-- `u(a) mod 17` for a unit `a mod 289`. -/
def uLog (a : ℕ) : ℕ := ((a ^ 16 % 289 - 1) / 17) * 16 % 17

/-- `ℓ_i mod 17`; `α⁻¹ ≡ 11⁻¹ ≡ 14 (mod 17)`. -/
def ellMod17 (i : ℕ) : ℤ :=
  let ai : ℤ := 14
  (((List.range 289).filter fun a => a % 17 != 0).map fun a =>
      (ai ^ 2 * sym289.getD a 0 - ai ^ 3 * sym17.getD (a % 17) 0) * (Nat.choose (uLog a) i : ℤ)).sum % 17

theorem alpha_inv : (11 * 14 : ℤ) % 17 = 1 := by decide
theorem distribution_relation : distributionHolds = true := by decide +kernel
theorem ell_low_mod17 :
    ellMod17 0 = 0 ∧ ellMod17 1 = 0 ∧ ellMod17 2 = 0 ∧ ellMod17 3 = 0 ∧ ellMod17 4 = 13 := by
  decide +kernel

end Seed17
