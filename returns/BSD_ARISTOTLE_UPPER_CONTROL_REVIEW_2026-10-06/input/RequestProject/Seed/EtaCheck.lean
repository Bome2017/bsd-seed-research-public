module

public import Mathlib

/-!
# Local images of the Mordell–Weil basis at the auxiliary bad primes (kernel-evaluated)

At the exceptional coefficient primes `p ∈ {19, 59}` (auxiliary prime `q = 2243`, split `I₁`,
`c_q = 1`, `#Ẽ_ns(𝔽_q) = 2242`) and `p = 487` (auxiliary prime `q = 5843`, non-split `I₂`,
`c_q = 2`, `#Ẽ_ns(𝔽_q) = 5844`), the local Kummer group is `E(ℚ_q)/p ≅ Ẽ_ns(𝔽_q)/p`, which is
cyclic of order `p`. Here `p` divides the order of the cyclic group `Ẽ_ns(𝔽_q)` exactly once.

A point `P` of `E₀(ℚ_q)` has zero local class iff `(n/p)·P̃ = 0` in `Ẽ_ns(𝔽_q)`, where
`n = #Ẽ_ns(𝔽_q)`. The function `imgNonzero` computes `(n/p)·(c·P̃)` with exact affine
arithmetic modulo `q`. Inverses are computed by Fermat's little theorem. It also checks that the
reductions are nonsingular, i.e. not the node.

The kernel evaluates the results below by `decide +kernel`. They agree with
`research_return/checks/eta_exceptional.py`. Their use in `research_return/UPPER_CONTROL.md`
(§6) needs the standard identification of `E₀(ℚ_q)/E₁(ℚ_q)` with `Ẽ_ns(𝔽_q)` and the fact that
`E₁(ℚ_q)` is `p`-divisible for `q ≠ p`. These are imported, not formalized.
-/

@[expose] public section

namespace Seed.EtaCheck

/-- Modular exponentiation with structural fuel. -/
def mpow (q : ℕ) : ℕ → ℕ → ℕ → ℕ
  | 0, _, _ => 1
  | fuel + 1, b, e =>
    if e = 0 then 1 % q else
      let r := mpow q fuel (b * b % q) (e / 2)
      if e % 2 = 1 then r * b % q else r

def inv (q a : ℕ) : ℕ := mpow q 64 (a % q) (q - 2)

/-- Coefficients of the minimal model reduced into `[0, q)`. -/
def a2 (q : ℕ) : ℕ := (q - 1 % q) % q
def a4 (q : ℕ) : ℕ := (q - 66020924 % q) % q
def a6 (q : ℕ) : ℕ := (q - 65074271436 % q) % q

/-- Affine group law on the nonsingular part modulo `q`; `none` is the identity. -/
def add (q : ℕ) : Option (ℕ × ℕ) → Option (ℕ × ℕ) → Option (ℕ × ℕ)
  | none, Q => Q
  | P, none => P
  | some (x1, y1), some (x2, y2) =>
    if x1 % q = x2 % q then
      if (y1 + y2) % q = 0 then none else
        let lam := (3 * x1 * x1 + 2 * a2 q * x1 + a4 q) % q * inv q (2 * y1) % q
        let x3 := (lam * lam + (q - a2 q) + 2 * q - x1 - x2) % q
        let y3 := (q * q - (y1 + lam * ((x3 + q - x1) % q)) % q) % q
        some (x3, y3)
    else
      let lam := (y2 + q - y1) % q * inv q ((x2 + q - x1) % q) % q
      let x3 := (lam * lam + (q - a2 q) + 2 * q - x1 - x2) % q
      let y3 := (q * q - (y1 + lam * ((x3 + q - x1) % q)) % q) % q
      some (x3, y3)

/-- Double-and-add with fuel. -/
def smul (q : ℕ) : ℕ → ℕ → Option (ℕ × ℕ) → Option (ℕ × ℕ)
  | 0, _, _ => none
  | fuel + 1, n, P =>
    if n = 0 then none else
      let R := smul q fuel (n / 2) (add q P P)
      if n % 2 = 1 then add q R P else R

/-- `P1 = (-3031, 327384)` and `P2 = (-2394, 281520)` reduced modulo `q`. -/
def P1 (q : ℕ) : Option (ℕ × ℕ) := some ((q * 10000 - 3031) % q, 327384 % q)
def P2 (q : ℕ) : Option (ℕ × ℕ) := some ((q * 10000 - 2394) % q, 281520 % q)

/-- The point lies on the reduced curve and is not singular there. -/
def nonsingular (q : ℕ) : Option (ℕ × ℕ) → Bool
  | none => true
  | some (x, y) =>
    (y * y % q == (x * x * x + a2 q * x * x + a4 q * x + a6 q) % q) &&
      !((2 * y % q == 0) && ((3 * x * x + 2 * a2 q * x + a4 q) % q == 0))

/-- `(n/p)·(c·P̃) ≠ 0`: the local class of `P` in `E(ℚ_q)/p` is nonzero. -/
def imgNonzero (p q n c : ℕ) (P : Option (ℕ × ℕ)) : Bool :=
  nonsingular q P && (smul q 64 (n / p) (smul q 64 c P)).isSome

theorem eta_19 : imgNonzero 19 2243 2242 1 (P1 2243) = true ∧
    imgNonzero 19 2243 2242 1 (P2 2243) = true := by decide +kernel

theorem eta_59 : imgNonzero 59 2243 2242 1 (P1 2243) = true ∧
    imgNonzero 59 2243 2242 1 (P2 2243) = true := by decide +kernel

theorem eta_487 : imgNonzero 487 5843 5844 2 (P1 5843) = true ∧
    imgNonzero 487 5843 5844 2 (P2 5843) = true := by decide +kernel

/-- Sanity check of the implementation: the full group order kills the reductions. -/
theorem order_kills : smul 2243 64 2242 (P1 2243) = none ∧ smul 5843 64 5844 (P1 5843) = none ∧
    smul 2243 64 2242 (P2 2243) = none ∧ smul 5843 64 5844 (P2 5843) = none := by
  decide +kernel

end Seed.EtaCheck
