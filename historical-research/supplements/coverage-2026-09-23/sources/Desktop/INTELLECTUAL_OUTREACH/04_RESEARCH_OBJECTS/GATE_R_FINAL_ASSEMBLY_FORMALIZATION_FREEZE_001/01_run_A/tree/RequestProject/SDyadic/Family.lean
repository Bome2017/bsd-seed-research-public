/-
`S_dyadic` — the parameter family and the two curve models.

Nothing here mentions the *answer*.  This file fixes only:
  * the dyadic normalisation `r = ε·2^m`, `A = 1−2r`, `B = r²`, `D = 1−4r`;
  * the coefficient pairs of the two curves, in the orientation of the reviewed theorem;
  * the hypotheses on `q` and on the valuations of `D`.

The Selmer *objects* come from the vendored `Run013.Selmer`, which defines them by genuine
local solubility at ℝ and at every ℚ_p.  See `FORMALIZATION_BOUNDARY.md`.
-/
import RequestProject.Run013.Selmer

namespace SDyadic

open Run013

/-! ## The dyadic parameters -/

/-- `r = ε · 2^m`. -/
def rr (ε : ℤ) (m : ℕ) : ℤ := ε * 2 ^ m

/-- `A = 1 − 2r`. -/
def AA (ε : ℤ) (m : ℕ) : ℤ := 1 - 2 * rr ε m

/-- `B = r²`. -/
def BB (ε : ℤ) (m : ℕ) : ℤ := (rr ε m) ^ 2

/-- `D = 1 − 4r`. -/
def DD (ε : ℤ) (m : ℕ) : ℤ := 1 - 4 * rr ε m

/-- The distinct positive odd prime divisors `ℓ₁,…,ℓ_s` of `|D|`.
`D = 1 − 4r` is odd, so every element here is odd. -/
def ellSet (ε : ℤ) (m : ℕ) : Finset ℕ := (DD ε m).natAbs.primeFactors

/-- `s`, the number of those primes. -/
def sCount (ε : ℤ) (m : ℕ) : ℕ := (ellSet ε m).card

/-! ## The two curves, in the orientation of the reviewed theorem

`E_q : y² = x(x² + A q x + r² q²)` and `E'_q : Y² = X(X − q)(X − D q)`.

Expanding the quotient, `X(X−q)(X−Dq) = X(X² − (1+D)q X + D q²)`, and `1 + D = 2A`, so its
coefficient pair is `(−2Aq, Dq²)`.

`SelmerSet a b` from `Run013.Selmer` is the Selmer group of the 2-isogeny with kernel `⟨(0,0)⟩`
**onto** `y² = x(x² + a x + b)`.  Hence:
  * `Sel^φ` is evaluated on `E'_q`  →  `SelmerSet (phiA …) (phiB …)`;
  * `Sel^φ̂` is evaluated on `E_q`  →  `SelmerSet (dualA …) (dualB …)`.
Do not reverse these. -/

/-- First coefficient of `E'_q`, i.e. `−2Aq`. -/
def phiA (ε : ℤ) (m : ℕ) (q : ℕ) : ℚ := ((-2 * AA ε m * q : ℤ) : ℚ)

/-- Second coefficient of `E'_q`, i.e. `D q²`. -/
def phiB (ε : ℤ) (m : ℕ) (q : ℕ) : ℚ := ((DD ε m * (q : ℤ) ^ 2 : ℤ) : ℚ)

/-- First coefficient of `E_q`, i.e. `A q`. -/
def dualA (ε : ℤ) (m : ℕ) (q : ℕ) : ℚ := ((AA ε m * q : ℤ) : ℚ)

/-- Second coefficient of `E_q`, i.e. `r² q²`. -/
def dualB (ε : ℤ) (m : ℕ) (q : ℕ) : ℚ := ((BB ε m * (q : ℤ) ^ 2 : ℤ) : ℚ)

/-! ## The hypotheses -/

/-- The exact hypotheses of the reviewed theorem.  No conclusion is encoded here.

`q`'s primality is carried by the instance argument `[Fact (Nat.Prime q)]`, which is what
`legendreSym q` requires; `q : ℕ` together with primality gives `q > 0`. -/
structure Params (ε : ℤ) (m : ℕ) (q : ℕ) [Fact (Nat.Prime q)] : Prop where
  /-- `m ≥ 3`.  Retained exactly; sharpening to `m ≥ 1` is out of scope for V1. -/
  m_ge_three : 3 ≤ m
  /-- `ε ∈ {1, −1}`. -/
  eps_unit : ε = 1 ∨ ε = -1
  /-- `q ∤ 2D`. -/
  q_not_dvd_twoD : ¬ ((q : ℤ) ∣ 2 * DD ε m)
  /-- `q ≡ 5 (mod 8)`. -/
  q_mod_eight : q % 8 = 5
  /-- `(D/q) = −1`. -/
  legendre_D_q : legendreSym q (DD ε m) = -1
  /-- every `v_{ℓ}(D)` is odd, for `ℓ` an odd prime divisor of `|D|`. -/
  odd_valuations : ∀ ℓ ∈ ellSet ε m, Odd (padicValInt ℓ (DD ε m))

/-- `q` is prime, extracted from the instance. -/
lemma Params.q_prime {ε : ℤ} {m q : ℕ} [hq : Fact (Nat.Prime q)] (_ : Params ε m q) :
    Nat.Prime q := hq.out

/-- `q > 0`. -/
lemma Params.q_pos {ε : ℤ} {m q : ℕ} [Fact (Nat.Prime q)] (h : Params ε m q) : 0 < q :=
  h.q_prime.pos

/-! ## Elementary identities of the normalisation (proved, not assumed) -/

theorem A_sq_sub_four_B (ε : ℤ) (m : ℕ) : (AA ε m) ^ 2 - 4 * BB ε m = DD ε m := by
  simp only [AA, BB, DD]; ring

theorem one_add_D (ε : ℤ) (m : ℕ) : 1 + DD ε m = 2 * AA ε m := by
  simp only [AA, DD]; ring

/-- The quotient model expands with coefficient pair `(−2Aq, Dq²)`:
`X(X−q)(X−Dq) = X(X² + (−2Aq)X + Dq²)`. -/
theorem quotient_model_expand (ε : ℤ) (m : ℕ) (q : ℤ) (X : ℤ) :
    X * (X - q) * (X - DD ε m * q)
      = X * (X ^ 2 + (-2 * AA ε m * q) * X + DD ε m * q ^ 2) := by
  have h : (1 : ℤ) + DD ε m = 2 * AA ε m := one_add_D ε m
  linear_combination (-(X ^ 2 * q)) * h

/-- `D` is odd. -/
theorem D_odd (ε : ℤ) (m : ℕ) : Odd (DD ε m) := ⟨-2 * rr ε m, by simp only [DD]; ring⟩

end SDyadic
