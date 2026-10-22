# Descent certificate for the seed: rank 2, Sha[2] = 0, index-one basis (2026-09-25)

**Curve.** `E : y² = x³ − 22735x² + 106272484x = x(x² + ax + b)`, with conductor
`N = 6503188012738584 = 2³·3·2243·4547²·5843`, `E(ℚ)_tors = ⟨T⟩ ≅ ℤ/2` and `T = (0,0)`. The 2-isogenous curve is
`E′ : y² = x(x² + 45470x + 91790289)`, with `T′ = (0,0)`.

## Statements certified here (exact computation; no preprint input)

1. `rank E(ℚ) = 2`.
2. `Sha(E/ℚ)[2] = 0`, hence `Sha(E/ℚ)[2^∞] = 0`: a nonzero 2-primary element has a nonzero multiple of order 2.
3. `E(ℚ) = ⟨T⟩ ⊕ ℤP₁ ⊕ ℤP₂`, with `P₁ = (4547, 327384)` and `P₂ = (5184, 281520)`. The basis has index one, not merely
   finite index.

These are the inputs that release claims R.1, R.4 and S.2 currently import from Zywina, arXiv:2502.01957v1, Thm 1.2 (a
2025 preprint). The results below agree with that theorem but do not use it.

## Why the descent is elementary here

`b = 106272484 = 2²·4547·5843` and `a² − 4b = 91790289 = 3²·2243·4547`. So both 2-isogeny descents are local at
`{2, 3, 2243, 4547, 5843, ∞}`. No class group or unit computation enters.

## Evidence

Two independent implementations, plus an exact lower bound.

| check | tool | result |
|---|---|---|
| 2-isogeny descent, first descent only (`-d`) | eclib `mwrank` 20250627 | first local descent gives rank bound 2; points found give rank 2. `Rank of S^2(E) = 3`. `III(E/Q)[2]`, `III(E/Q)[phi']`, `III(E'/Q)[2]` and `III(E'/Q)[phi]` are trivial |
| default run, with second descent | eclib `mwrank` | `Rank = 2`, `#III(E/Q)[2] = 1` |
| E′ | eclib `mwrank` | the same, from the isogenous side |
| full 2-descent | PARI 2.17.3 `ellrank`, computed **unconditionally** per its manual | `[r₁, r₂, s] = [2, 2, 0]` for both E and E′. This gives 2-Selmer rank C = r₂ + T + s = 3, and rank of `Sha[2]` S = C − T − R = 3 − 1 − 2 = 0 |
| exact lower bound: x-coordinate images mod squares | PARI, exact | `α(T) = 4547·5843` and `α(P₁) = 4547`, so `α(E(ℚ))` contains `{1, 4547, 5843, 4547·5843}` (order 4). `α′(T′) = 2243·4547` and `α′(Q′) = −2243`, so `α′(E′(ℚ))` contains `{1, 2243·4547, −2243, −4547}` (order 4). Then `|α(E(ℚ))|·|α′(E′(ℚ))| = 16 = 2^(r+2)` gives r ≥ 2, matching the Selmer upper bound |
| index one | eclib saturation via Sage 10.9 (`max_prime=−1`, i.e. an automatically computed, proven bound) | proven saturation index bound 2, Tamagawa prime 2; "Points were proved 2-saturated". Saturation index 1, input points unchanged; regulator 17.7965174724903, matching R.5 |

**Conclusion.** The Selmer upper bounds equal the explicit lower bounds on both sides of the isogeny. So the rank is
exactly 2 and the φ- and φ′-parts of Sha are trivial. Both implementations then give `Sha(E/ℚ)[2] = 0` directly: the
2-Selmer rank is 3 = 2 + dim E(ℚ)[2]. Saturation at the proven bound gives index one.

## Trust base and grade

- **Grade.** EXACT_COMPUTATION. It is a finite exact descent, cross-checked by two independent implementations (PARI's
  `ellrank` and Cremona's eclib), replayable in about 4 s with `bash verify_descent.sh`.
- **Residual trust.** The correctness of those two programs; no human review. The saturation step uses eclib only,
  through Sage. The older Lane 3 Silverman/ratpoints certificate is a second, earlier route to index one.
- **Zywina's preprint.** Becomes corroboration: its Thm 1.2 supplies the same rank and 2-primary statements for the
  whole family.

## Files

- `pari_descent.gp`, `pari_descent.out`
- `mwrank_E_2isogeny_only.log`, `mwrank_E_default.log`, `mwrank_Eprime_2isogeny_only.log`
- `saturation.sage`, `saturation.out`
- `verify_descent.sh`, whose replay prints `DESCENT_CERTIFICATE_REPLAY_PASS`
- `MANIFEST.sha256`
