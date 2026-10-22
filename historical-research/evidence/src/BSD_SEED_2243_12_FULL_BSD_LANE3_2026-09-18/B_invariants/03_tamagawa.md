# B.3 — Tamagawa numbers and reduction types (Tate's algorithm)

Scripts: `scripts/s01_03_local.gp` (PARI `elllocalred`, `ellap`), `scripts/s01_03_sage.sage` (Sage `local_data(p, algorithm='generic')` =
Sage's own Python implementation of Tate's algorithm, and `local_data(p)` = PARI) → `out/`.

| p | v_p(Δ) | f_p | Kodaira (PARI code) | Sage generic Tate | c_p | a_p | reduction |
|---|---|---|---|---|---|---|---|
| 2 | 8 | 3 | I₁* (−5) | I1* | 2 | 0 | additive |
| 3 | 2 | 1 | I₂ (6) | I2 | 2 | −1 | **non-split** multiplicative |
| 2243 | 1 | 1 | I₁ (5) | I1 | 1 | +1 | **split** multiplicative |
| 4547 | 3 | 2 | III (3) | III | 2 | 0 | additive |
| 5843 | 2 | 1 | I₂ (6) | I2 | 2 | −1 | **non-split** multiplicative |

- All three implementations agree (PARI `elllocalred`, Sage generic Tate, Sage→PARI). **Label: PROVED** (Tate's algorithm is a
  finite exact computation; two independent implementations agree).
- Split/non-split from a_p = +1 / −1 at the multiplicative primes, and Sage's `has_split_multiplicative_reduction()` agrees.
- Consistency of c_p with the type: I_n split has c = n; I_n non-split has c = 1 if n is odd and 2 if n is even. So I₂ non-split
  gives c = 2 at 3 and at 5843, and I₁ split gives c = 1 at 2243. III always has c = 2. For I₁* (c ∈ {2, 4}), Tate's algorithm
  returns 2 in both implementations.
- **∏ c_p = 16 = 2⁴**, matching the brief. Root number w(E) = +1 (PARI `ellrootno`, Sage), matching the brief.
- The model is minimal at every p (u = 1 at each p in `elllocalred`), so these are the Tamagawa numbers of the Néron model.
