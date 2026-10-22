# Preliminary reduction data at 13 — independently certified

**Scope of this record.** This is *only* the independent verification of the preliminary
arithmetic quoted with the 13-primary plan. The 13-primary computation itself
(the depth-two symbol evaluation and the residue `C_13 = [T²]L_13(E,T) mod 13`) is **not**
attempted here and no claim about `Ш(E/ℚ)[13^∞]` is made.

## What was checked, and how

All statements below are machine-checked in `RequestProject/ReductionAt13.lean`, sorry-free,
with axioms limited to `propext`, `Classical.choice`, `Quot.sound`. The inputs are the exact
integral model already recorded in `RequestProject/SeedData.lean`:

```
E : y² = x³ + a₂x² + a₄x,  a₂ = -22735,  a₄ = 106272484
Δ = 2⁸·3²·2243·4547³·5843²,  N = 2³·3·2243·4547²·5843
```

| claim | theorem |
|---|---|
| `13 ∤ Δ` (good reduction, model automatically 13-minimal) | `thirteen_not_dvd_disc` |
| `13 ∤ N` | `thirteen_not_dvd_conductor` |
| reduction mod 13 is `W13 : y² = x³ + 2x² + 6x` over `𝔽₁₃` | `seed_reduction_at_13` |
| `Δ(W13) ≠ 0` in `𝔽₁₃` | `W13_Δ_ne_zero` |
| 17 affine `𝔽₁₃`-solutions | `card_affineSolutions` |
| **`#E(𝔽₁₃) = 18`** | `card_points_mod_13` |
| **`a₁₃ = 13 + 1 − 18 = −4`** | `a_thirteen_eq` |
| Hasse bound `a₁₃² ≤ 52` | `a_thirteen_hasse` |
| **`13 ∤ a₁₃`: good *ordinary* reduction** | `ordinary_at_13` |

Method: exhaustive kernel evaluation over all `169` pairs in `𝔽₁₃ × 𝔽₁₃`. Because `Δ ≠ 0`
over `𝔽₁₃`, every affine solution is nonsingular, so the point set of the affine model is in
bijection with the solution set plus the point at infinity (`pointEquiv13`); the count is
therefore of the actual group of points, not of an unqualified solution set. No table lookup,
no floating-point arithmetic, no external database, no coefficient corpus.

The 8 values of `x` with `x³+2x²+6x` a nonzero square are `x = 1,4,5,6,8,9,10,11`; together
with `x = 0` (the rational 2-torsion point `(0,0)`, which reduces to `(0,0)` here) this gives
`2·8 + 1 = 17` affine points.

## Consequence for the planned operation

The applicability condition of the fixed-prime method used at 7 and 11 — good **ordinary**
reduction at the prime — holds at 13, with unit root determined by `a₁₃ = −4 ≡ 9 (mod 13)`.
So the planned certified evaluation of `C_13` is not obstructed by the reduction type.

## Explicit non-claims

* No value of `C_13` is computed or estimated.
* `Ш(E/ℚ)[13^∞]` is untouched; the 11-primary input remains an imported computer-assisted
  result at the packet's declared grade, and the threshold record is unchanged.
* No uniform statement, no FIN, no order 9, no `q = 36`, no successor prime.
* Nothing here raises or lowers any order threshold, and no new global direction is proposed.
