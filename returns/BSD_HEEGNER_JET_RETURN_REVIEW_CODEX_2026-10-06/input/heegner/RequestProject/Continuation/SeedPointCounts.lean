module

public import Mathlib

/-!
# Point counts: three supersingular primes of the seed curve

New Lean source for the 2026-10-06 continuation run. For `ℓ = 281, 661, 839` the congruence
`y² ≡ x³ - 22735x² + 106272484x (mod ℓ)` has exactly `ℓ` solutions `(x, y) ∈ [0, ℓ)²`. With
the point at infinity, `#E(𝔽_ℓ) = ℓ + 1`, so `a_ℓ = 0`. All three primes are good for `E`.

This is the record's original model. It differs from the minimal model by `x ↦ x + 7578` with
`u = 1`, so `a_ℓ` is the same at every odd good prime. Each count is evaluated by the kernel
(`decide +kernel`) by enumerating all `ℓ²` pairs. It uses no `native_decide`.
-/

@[expose] public section

namespace Continuation.SeedFinite

/-- Number of affine solutions `(x, y) ∈ [0, ℓ)²` of `y² ≡ x³ - 22735x² + 106272484x (mod ℓ)`. -/
def affCount (l : ℕ) : ℕ :=
  ((List.range l).map fun x =>
    ((List.range l).filter fun y =>
      ((y : ℤ) * y - ((x : ℤ) ^ 3 - 22735 * x ^ 2 + 106272484 * x)) % l = 0).length).sum

set_option maxRecDepth 100000 in
/-- `a_281 = 0`: there are `281` affine points, hence `#E(𝔽_281) = 282`. -/
theorem affCount_281 : affCount 281 = 281 := by decide +kernel

set_option maxRecDepth 100000 in
/-- `a_661 = 0`: there are `661` affine points, hence `#E(𝔽_661) = 662`. -/
theorem affCount_661 : affCount 661 = 661 := by decide +kernel

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
/-- `a_839 = 0`: there are `839` affine points, hence `#E(𝔽_839) = 840`. -/
theorem affCount_839 : affCount 839 = 839 := by decide +kernel

end Continuation.SeedFinite
