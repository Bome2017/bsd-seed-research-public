# Handoff — K288 raw custody audit (Claude, Opus 5.5, 2026-10-06)

**Verdict: K288_CUSTODY_CONFIRMED.** This was step 1 of Pro's 10-06 re-prioritization. It cost $0 and involved no new L-value computation.

- **Rebuilt inputs.**
  - All nine c₂ values were rebuilt with fresh code from the raw certified `XB` symbol lines. Hashes and pinned corpus roots are bound for all 9 runs, and all 1,564 symbol identifications are unique.
  - All nine tame regulators were recomputed with fresh GP code. This uses a different multiplier M from `tame_reg.gp`, so the M⁴ scaling is checked as well.
- **Result.** w = c₂ / ((a_ℓ − 2)·R) ≡ 288 (mod p) at p = 17, 19, 23, 29, 31, 37, 41, 43, 47.
  - The value is unchanged under the second primitive root.
  - CRT gives exactly 288 modulo 20,475,850,236,047.
  - Rational reconstruction returns 288/1.
- **Convention.** Symbols are Re λ/ω₁, g is the least primitive root, b₁₂ = (h(Q₁+Q₂) − h₁ − h₂)/2, and R = det/M⁴. Under it the unit is u = 1 at every residue.
- **Provenance of 288.**
  - It was fitted at 17 and 23, as the least CRT lift mod 391.
  - At 19 it was evaluated after the result.
  - Six pre-result forecasts matched.
- **Sealed extra checks (`PREDICTION_EXTRA.md`, sha 9791e0aa…).**
  - p = 5 at ℓ = 191 and at ℓ = 311 both match.
  - p = 3 at ℓ = 103 matches, but that check does not discriminate.
- **Independent corroboration.** Aristotle eb3e82a5 -6 recomputed R by two Python routes and agrees at 9/9.
- **Scope.**
  - The symbol values themselves are taken as certified by the run pipeline.
  - 17, 19, 23 and 29 carry the record's "outside artifact-level review outstanding" qualifier.

FIN, ORDER9 and Q36 are unchanged.
