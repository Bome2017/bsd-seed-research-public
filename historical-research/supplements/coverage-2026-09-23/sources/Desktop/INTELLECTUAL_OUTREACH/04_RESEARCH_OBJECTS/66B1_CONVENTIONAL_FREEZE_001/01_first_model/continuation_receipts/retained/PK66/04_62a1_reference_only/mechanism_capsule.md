# 62a1 mechanism capsule — REFERENCE ONLY, DO NOT ASSUME PORTABILITY

A separate, finished piece of work established a finite-field statement for the curve 62a1. It is
summarised here **only** so that you can ask whether an analogue exists for 66b1. It is not evidence
about 66b1, and the fact that it worked once is not a reason to expect it to work again.

## The 62a1 statement

For the descent model `E₁ : Y² = X³ − 15X² + 64X` of 62a1 and a finite field `k` of characteristic
`∉ {2, 31}`, with `χ_k` the quadratic character:

    v₂(#E₁(k)) = 2   ⟺   χ_k(2) = χ_k(−31) = −1.

## The shape of the argument, in four moves

1. **Unique rational 2-torsion.** `X² − 15X + 64` has discriminant `−31`; when `χ_k(−31) = −1` it is
   irreducible, so `E₁(k)[2] ≅ Z/2` and the Sylow 2-subgroup is cyclic (via `|S[2]| = 2^r`).
2. **An explicit point of order 4** defined directly over `k`: `T = (8,8)`, with `2T = (0,0) ≠ O`.
3. **A halving obstruction.** For `Y² = X³ + aX² + bX`, `x(2P) = ((x(P)² − b)/(2y(P)))²`, so every
   doubled point has square abscissa. `x(T) = 8` is a nonsquare when `χ_k(2) = −1`, so `T ∉ 2E₁(k)`.
4. **Conclusion.** A cyclic 2-group containing an element of order 4 that is not a double has order
   exactly 4.

## Why you should not assume this transports

- 62a1 has `Δ < 0`; 66b1 has `Δ > 0`.
- 62a1's discriminant datum is the single prime 31; 66b1's is `33 = 3·11`, and the proposed family
  constrains `(q/3)` and `(q/11)` separately rather than their product.
- Step 2 depends on an explicit rational point whose x-coordinate happens to be a nonsquare in the
  relevant fields. Whether 66b1 has a point playing that role, and whether its x-coordinate has the
  needed character, is exactly what is open.

**Deliberately withheld:** any analysis of whether the analogue holds for 66b1, and any proposed
resolution of the period-normalization question in `TASK.md`. Derive both independently.
