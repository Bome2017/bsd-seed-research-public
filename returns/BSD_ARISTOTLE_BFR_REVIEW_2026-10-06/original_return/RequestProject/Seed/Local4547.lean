module

public import Mathlib

/-!
# Exact local data at the bad coefficient primes `2243`, `4547`, `5843`

## Index data

For a prime `q` of bad reduction, `[E(ℚ_q) : E₁(ℚ_q)] = c_q · #Ẽ_ns(𝔽_q)`.  With the retained
reduction types (release claim A.1: `2243` split `I₁`, `c = 1`; `4547` type `III`, `c = 2`;
`5843` non-split `I₂`, `c = 2`) these indices are `2242`, `2 · 4547`, `2 · 5844`.  The lemma
`index_coprime` records the elementary divisibility facts that decide whether a primitive point
of `E₁(ℚ_p)` (such as the receiver point `R_p`) generates `E(ℚ_p)/p`.

## A kernel-evaluated certificate at `p = 4547`

At the additive prime `4547` the index is divisible by `p`.  The research return shows that the
correct local generator there is the rational basis point `P2 = (-2394, 281520)`: it has
non-singular reduction and `v_p(x((p-1)P2) - x(P2)) = 1`, equivalently `v_p(t(p P2)) = 1`.

`chainCert` recomputes `(p-1)·P2` by an *independent* method (homogeneous projective
coordinates, no division, exact arithmetic modulo `p³`) from the Python producer
`research_return/checks/local_kummer_4547.py` (affine coordinates modulo `p⁸`).  It also checks
at every step that the chord denominator is a `p`-adic unit, so that no precision is lost.
The kernel evaluates it by `decide`.

Scope: the identification of this finite computation with the group law of `E(ℚ_p)`, and the
formal-group consequences drawn from it, are standard facts that are *not* formalized here
(Mathlib has no formal group / Néron model API); they are listed as imports in
`research_return/ASSUMPTIONS.json`.
-/

@[expose] public section

namespace Seed.Local

/-- `[E(ℚ_q) : E₁(ℚ_q)] = c_q · #Ẽ_ns(𝔽_q)` at the three bad coefficient primes (retained types):
it is prime to `q` at `2243` and `5843` and divisible by `q` at `4547`. -/
theorem index_coprime :
    ¬ (2243 ∣ 1 * 2242) ∧ ¬ (5843 ∣ 2 * 5844) ∧ (4547 ∣ 2 * 4547) := by
  decide

/-- The odd primes dividing the bad-place reduction indices `4, 8, 2242, 9094, 11688`
(the origin of `19, 59, 487` in the record's exceptional set `B*`). -/
theorem reduction_quotient_factorizations :
    2242 = 2 * 19 * 59 ∧ 9094 = 2 * 4547 ∧ 11688 = 2 ^ 3 * 3 * 487 := by
  decide

/-- The prime. -/
def p : ℕ := 4547
/-- Working modulus `p³`: the projective formulas involve no division, so residues modulo
`p³` are exact. -/
def M : ℕ := 4547 ^ 3

/-- Reduction modulo `M` of an integer given as a pair of naturals (positive, negative). -/
def red (a : ℤ) : ℕ := (a % (M : ℤ)).toNat

/-- Minimal model coefficients modulo `M` (`a₂ = -1`, `a₄ = -66020924`). -/
def a2 : ℕ := red (-1)
def a4 : ℕ := red (-66020924)

/-- Modular arithmetic helpers on `ℕ` (all results reduced modulo `M`). -/
def ad (x y : ℕ) : ℕ := (x + y) % M
def sb (x y : ℕ) : ℕ := (x + (M - y % M)) % M
def ml (x y : ℕ) : ℕ := (x * y) % M

/-- A projective point `(X : Y : Z)` modulo `M`, together with a flag recording that every chord
denominator encountered so far was a unit modulo `p`. -/
structure St where
  X : ℕ
  Y : ℕ
  Z : ℕ
  ok : Bool

/-- `P2 = (-2394, 281520)` modulo `M`. -/
def xP : ℕ := red (-2394)
def yP : ℕ := red 281520

/-- `2·P2` by the tangent formula, written projectively:
`N = 3x² + 2a₂x + a₄`, `D = 2y`, `X₃ = D(N² - a₂D² - 2xD²)`,
`Y₃ = -(yD³ + N(N² - a₂D² - 3xD²))`, `Z₃ = D³`. -/
def dbl : St :=
  let N := ad (ad (ml 3 (ml xP xP)) (ml 2 (ml a2 xP))) a4
  let D := ml 2 yP
  let D2 := ml D D
  let B := sb (sb (ml N N) (ml a2 D2)) (ml 2 (ml xP D2))
  let X3 := ml D B
  let Y3 := sb 0 (ad (ml yP (ml D2 D)) (ml N (sb B (ml xP D2))))
  let Z3 := ml D2 D
  ⟨X3, Y3, Z3, D % p != 0⟩

/-- Chord addition `Q + P2` projectively (`P2` has `Z = 1`):
`u = y_P Z - Y`, `v = x_P Z - X`, `A = u² Z - a₂ v² Z - v²(X + x_P Z)`,
`X₃ = vA`, `Y₃ = -(Y v³ + u(A - v² X))`, `Z₃ = v³ Z`. -/
def addP (s : St) : St :=
  let u := sb (ml yP s.Z) s.Y
  let v := sb (ml xP s.Z) s.X
  let v2 := ml v v
  let A := sb (sb (ml (ml u u) s.Z) (ml a2 (ml v2 s.Z))) (ml v2 (ad s.X (ml xP s.Z)))
  let X3 := ml v A
  let Y3 := sb 0 (ad (ml s.Y (ml v2 v)) (ml u (sb A (ml v2 s.X))))
  let Z3 := ml (ml v2 v) s.Z
  ⟨X3, Y3, Z3, s.ok && (v % p != 0)⟩

/-- `k ↦ (k+2)·P2` by repeated chord addition. -/
def chain : ℕ → St
  | 0 => dbl
  | n + 1 => addP (chain n)

/-- `(p-1)·P2 = chain (p-3)`. -/
def Apm1 : St := chain (4547 - 3)

/-- The certificate: every chord denominator was a unit mod `p`; `(p-1)P2` has unit `Z`
(so it lies in `E₀ \ E₁`); and `X - x(P2) Z` is divisible by `p` but not by `p²`, i.e.
`v_p(x((p-1)P2) - x(P2)) = 1`. Also `P2` has non-singular reduction mod `p` (`2y ≢ 0`). -/
def chainCert : Bool :=
  let A := Apm1
  A.ok && (A.Z % p != 0) && ((sb A.X (ml xP A.Z)) % p == 0) &&
    ((sb A.X (ml xP A.Z)) % (p * p) != 0) && ((2 * yP) % p != 0)

theorem chainCert_true : chainCert = true := by
  decide +kernel

end Seed.Local
