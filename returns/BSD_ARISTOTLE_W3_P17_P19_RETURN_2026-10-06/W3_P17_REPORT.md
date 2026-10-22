# W3 on the actual seed at p = 17: weight-two data at denominator 17² = 289

**Status: COMPLETED EXPERIMENT. The calibration came back NEGATIVE.**

I computed the seed's weight-two plus modular symbols `[a/289]^+` and `[a/17]^+` and evaluated `ℓ_2 mod 17`. The result is `ℓ_2 ≡ 0 (mod 17)`. So the quadratic forcing criterion "`ℓ_2 ≢ 0 mod p`" **fails at p = 17**, even though `Ш(E/ℚ)[17] = 0` is already settled by the retained Ota receipt. The first nonzero coefficient is `ℓ_4`, so the 17-adic L-function has `μ = 0` and `λ = 4`, larger than the rank (2).

**Grades**
- **COMPUTED**: produced by code in `w3_p17/`. Floating point; validated as described below, but not interval-certified.
- **LEAN**: machine-checked, no `sorry`.
- **IMPORTED**: depends on a cited theorem or retained input.

## 1. The evaluator

The retained `arbcore msl` executable is not part of this project. I therefore wrote an evaluator, `w3_p17/msl_sq.c`, that implements the same computation for any modulus `m` with `gcd(m, N) = 1`, including composite `m = p^2`.

**Formula (validated).** With root number `+1`, write `a' = (N a)^{-1} mod m`. Then

```
[a/m]^+ · Ω^+ = Σ_b S_b ( cos(2π a b/m) + cos(2π a' b/m) ),
S_b = Σ_{n ≤ T, n ≡ b (m)} a_n/n · exp(−2π n/(m √N)).
```

`w3_p17/validate_formula.py` compares this formula with exact Manin-relation plus symbols (`w3_source/modsym2.py`):
- curves 11a1, 37a1 (root number −1) and 389a1;
- denominators `m = 5, 7, 9, 25, 49`, both prime and prime-square;
- agreement is `≤ 3·10^{-14}` with a single constant `Ω` for all `a` and all `m` (`FORMULA_VALIDATION.json`).

**Coefficients.** Write `P0 = ⌊√T⌋`.
- `n` that are `P0`-smooth are enumerated depth-first, using multiplicativity.
- Every other `n` is `k·q` with `q > P0` prime and `k < P0`.
- `a_q` for `q > P0` comes from Shanks–Mestre baby-step/giant-step in Montgomery arithmetic (`w3_p17/ap.h`). Each value is accepted only if it is the unique group order in the Hasse interval consistent with every tested point, on `E` and on random quadratic twists. Each accepted order is re-verified by an explicit scalar multiplication. The number of failures was 0 in every run.
- At the bad primes: `2` and `4547` are additive (`a = 0`); `3`, `2243`, `5843` are multiplicative, with `a = −1, +1, −1`.

**Engine checks.**
- BSGS `a_p` agrees with naive point counting for all primes `37 ≤ p < 3·10^5`.
- The full engine agrees with an independent brute-force summation (`ref_brute.c`) to `10^{-15}` at `m = 17, 289, 361`.

**External authentication against your receipt.** In the same pass as `m = 289`, I computed `[a/103]^+` (with `T = 2.08·10^{10}`). All **102** values equal the integers in the retained receipt `retained/P17_MSL.txt` (`XB … plus`). The worst distance to an integer was `1.2·10^{-6}`. That receipt was produced by the frozen `arbcore msl` with arb balls. So this evaluator reproduces the authenticated pipeline exactly, including the normalisation `Ω^+ = 0.02804490151943640…`.

**Cost.** The `m = 289` pass used `T = 2.5·289·√N = 5.83·10^{10}`. That meant `2 454 030 900` BSGS point counts, taking 6890 s on 8 cores. This matches your estimate of roughly 5,600 segments, i.e. about 3× the singleton `ℓ = 103` run.

## 2. Results at p = 17 (`w3_p17/P17_RESULTS.json`)

The basic data are `a_17 = −6` (ordinary, not anomalous) and `α ≡ 11 (mod 17)`.

**Level-17 symbols `[a/17]^+`, for `a = 1, …, 16`:**
`−84, 420, −154, −84, 10, 10, −154, 36, 36, −154, 10, 10, −84, −154, 420, −84`. The largest distance to an integer was `3·10^{-8}`.

**Level-289 symbols.** All 272 values `[a/289]^+` lie within `1.04·10^{-6}` of integers. The gcd of all 288 symbols is 1, so the normalisation is primitive at 17.

**Consistency checks, all passed:**
- `[0]^+ = L(E,1)/Ω^+`: numerically `1.4·10^{-8}`, i.e. 0.
- `Σ_{a=1}^{16} [a/17]^+ = (a_17 − 2)[0]^+ = 0`.
- Hecke `U_17`: `Σ_j [(a+17j)/289]^+ = a_17 [a/17]^+ − [0]^+` holds in all 16 classes. This identity links two independent sums (`m = 289` and `m = 17`, which use different kernels and cut-offs).

**Low coefficients mod 17.** The Mazur–Tate–Teitelbaum measure at level `17²` determines `L_p mod (17, T^{17})`, using the formula in `w3_source/weight2_jet.py`:

| i | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| `ℓ_i mod 17` | 0 | 0 | **0** | 0 | **13** | 11 | 12 |

The full list for `i ≤ 16` is in the JSON. `ℓ_0 ≡ ℓ_1 ≡ 0` is the forced rank-two vanishing; random data would give `ℓ_1 ≡ 0` with probability 1/17, so this is a real check.

**(LEAN)** `RequestProject/Seed17Symbols.lean` contains the 288 integers and checks two things by kernel evaluation:
- `Seed17.distribution_relation`: the `U_17` relation;
- `Seed17.ell_low_mod17`: `ℓ_0 ≡ ℓ_1 ≡ ℓ_2 ≡ ℓ_3 ≡ 0` and `ℓ_4 ≡ 13 (mod 17)`.

Lean checks the finite arithmetic only, not the analytic computation of the integers.

## 3. What the negative calibration means

1. **The weight-two quadratic criterion is strictly stronger than `Ш[p] = 0`.**
   - At `p = 17`, `Ш(E/ℚ)[17] = 0` is known (retained Ota receipt), yet `ℓ_2 ≡ 0`.
   - The local factors are all 17-units: `1 − α^{-1} ≡ −13`, the Tamagawa numbers have no factor 17, and the torsion is 2-power.
   - So, through the p-adic BSD leading-term relation `ℓ_2 ≐ (1−α^{-1})^2 · Reg_17/17^2 · #Ш · ∏c_v / #E(ℚ)_tors^2` (IMPORTED: Schneider / Perrin-Riou, plus the main-conjecture identification), `ℓ_2 ≡ 0` says **the normalised 17-adic regulator of the seed is divisible by 17**.
   - `λ = 4` with `μ = 0` is the Iwasawa-theoretic form of the same statement.

2. **W3 at 17 is undecided by weight-two data alone.**
   - `W3.quadratic_jet_forcing` needs one of the coefficients `a, b, c` of the quadratic jet to be a unit.
   - `c = unit·ℓ_2 ≡ 0`, and `b = −c ≡ 0` by the retained functional equation.
   - So the only remaining coefficient is `a`, which is tied to the one-divisor quantity `Λ_2`. That is still unknown here.

3. **Warning for the cofinite programme (heuristic, not proved).**
   - A cofinite W3 bound through `ℓ_2` amounts to "the normalised `p`-adic regulator is a `p`-unit for all but finitely many ordinary `p`".
   - If `ℓ_2 mod p` behaves like a random residue, the expected number of exceptional `p` is `Σ 1/p = ∞`.
   - The first seed data point (17) is exceptional.
   - So `ℓ_2 ≢ 0` should not be expected to hold cofinitely. Any FIN mechanism must tolerate `λ > 2` at infinitely many primes, i.e. it must see `#Ш` separately from the regulator.

## 4. Next prime and costs

`p = 19` has now been run; see §5.

Running time scales roughly like `(p^2)^{1.25}` from the measured 1.9 h at `p = 17`, on 8 cores:

| p | 19 | 31 | 37 | 43 | 53 |
|---|---|---|---|---|---|
| estimated hours | 2.5 | 9 | 13 | 18 | 29 |

`p = 23` and `p = 29` are supersingular (`a_p = 0`), so this ordinary formula does not apply to them.

## 5. p = 19: positive result on the seed (`w3_p17/P19_RESULTS.json`)

The basic data are `a_19 = 4` (ordinary, not anomalous) and `α ≡ 4 (mod 19)`.

**Run.** One pass computed `m = 361` (with `T = 7.28·10^{10}`) and `m = 19`. It made `3 036 899 844` BSGS point counts in 8507 s, with 0 failures.

**Checks, all passed:**
- All 342 values `[a/361]^+` and all 18 values `[a/19]^+` lie within `1.5·10^{-6}` of integers.
- The gcd of all symbols is 1.
- `Σ_a [a/19]^+ = (a_19 − 2)[0]^+ = 0`.
- The `U_19` distribution relation holds in all 18 classes.

**Low coefficients mod 19:**

| i | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| `ℓ_i mod 19` | 0 | 0 | **18** | 7 | 15 |

So `μ = 0` and `λ = 2 = rank`.

**(LEAN)** `RequestProject/Seed19Symbols.lean` checks two things:
- `Seed19.distribution_relation`;
- `Seed19.ell_low_mod19`: `ℓ_0 ≡ ℓ_1 ≡ 0` and `ℓ_2 ≡ 18 (mod 19)`.

**Domain conditions at 19 (COMPUTED, `w3_p17/surjectivity_check.py`).**
- **Surjectivity.** `ρ̄_19` is surjective by Serre's criterion (Prop. 19 of *Propriétés galoisiennes…*, 1972). The Frobenius witnesses are at `ℓ = 11, 5, 11`, and each has nonzero trace.
- **Tamagawa numbers** are prime to 19. The model gives `c_3 = c_5843 = 2` (non-split, `ord Δ = 2`) and `c_2243 = 1`; the additive primes have `c ≤ 4`.
- **Torsion** is 2-power.

The same check gives surjectivity at 17 and at 53.

**What `ℓ_2 ≢ 0 (mod 19)` gives.**
- **(IMPORTED: Kato's divisibility, the control theorem, the Schneider / Perrin-Riou leading term.)** It gives `Ш(E/ℚ)[19^∞] = 0`, and the normalised 19-adic regulator is a 19-adic unit. This is an independent weight-two certificate at 19. It does not use the Ota/Kurihara route.
- **(W3, IMPORTED_WITH_HYPOTHESES.)** Since `c = unit·ℓ_2 ≢ 0`, `W3.exists_node_ne_zero_of_not_dvd_c` makes some W3 node value nonzero mod `19^3`. This is under the W3 imports of `W3_SOURCE_REPORT.md` §5, which include the unverified Hida-domain condition at 19.

**Summary of the two calibrations on the actual seed.** The weight-two `ℓ_2` route certifies `p = 19` but not `p = 17`. At 17 the obstruction is a 17-divisible normalised regulator (`λ = 4`), not Ш.

## 6. L'(E^{(-23)}, 1), used by the Heegner note

See `w3_p17/TWIST23_RESULTS.json`. This is the same engine with the exponential-integral kernel, buckets mod 23 and conductor `23^2 N`. It is cross-checked by the functional-equation test with split parameter `t = 1.2`.
