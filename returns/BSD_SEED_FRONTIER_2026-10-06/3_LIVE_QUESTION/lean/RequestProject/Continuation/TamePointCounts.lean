module

public import Mathlib

/-!
# Point counts `#E(𝔽_ℓ)` at the nine K288 auxiliary primes

New Lean source (K288 custody audit). For the minimal model
`y² = x³ − x² − 66020924x − 65074271436` and each auxiliary prime `ℓ` used by the nine singleton
certificates `p = 17, …, 47`, the number of affine solutions `(x, y) ∈ [0, ℓ)²` plus the point at
infinity equals the recorded `#E(𝔽_ℓ)`. Each count is evaluated by the kernel
(`decide +kernel`), enumerating all `ℓ²` pairs; no `native_decide`.
-/

@[expose] public section

namespace TameScalar

/-- Number of affine solutions `(x, y) ∈ [0, ℓ)²` of
`y² ≡ x³ − x² − 66020924x − 65074271436 (mod ℓ)` (minimal model of the seed curve). -/
def affCountMin (l : ℕ) : ℕ :=
  ((List.range l).map fun x =>
    ((List.range l).filter fun y =>
      ((y : ℤ) * y - ((x : ℤ) ^ 3 - x ^ 2 - 66020924 * x - 65074271436)) % l = 0).length).sum

set_option maxHeartbeats 0 in
set_option maxRecDepth 200000 in
/-- `#E(𝔽_47) = 44`. -/
theorem card_47 : affCountMin 47 + 1 = 44 := by decide +kernel

set_option maxHeartbeats 0 in
set_option maxRecDepth 200000 in
/-- `#E(𝔽_83) = 92`. -/
theorem card_83 : affCountMin 83 + 1 = 92 := by decide +kernel

set_option maxHeartbeats 0 in
set_option maxRecDepth 200000 in
/-- `#E(𝔽_103) = 106`. -/
theorem card_103 : affCountMin 103 + 1 = 106 := by decide +kernel

set_option maxHeartbeats 0 in
set_option maxRecDepth 200000 in
/-- `#E(𝔽_149) = 160`. -/
theorem card_149 : affCountMin 149 + 1 = 160 := by decide +kernel

set_option maxHeartbeats 0 in
set_option maxRecDepth 200000 in
/-- `#E(𝔽_173) = 196`. -/
theorem card_173 : affCountMin 173 + 1 = 196 := by decide +kernel

set_option maxHeartbeats 0 in
set_option maxRecDepth 200000 in
/-- `#E(𝔽_191) = 202`. -/
theorem card_191 : affCountMin 191 + 1 = 202 := by decide +kernel

set_option maxHeartbeats 0 in
set_option maxRecDepth 200000 in
/-- `#E(𝔽_233) = 248`. -/
theorem card_233 : affCountMin 233 + 1 = 248 := by decide +kernel

set_option maxHeartbeats 0 in
set_option maxRecDepth 200000 in
/-- `#E(𝔽_283) = 288`. -/
theorem card_283 : affCountMin 283 + 1 = 288 := by decide +kernel

set_option maxHeartbeats 0 in
set_option maxRecDepth 200000 in
/-- `#E(𝔽_311) = 296`. -/
theorem card_311 : affCountMin 311 + 1 = 296 := by decide +kernel

end TameScalar
