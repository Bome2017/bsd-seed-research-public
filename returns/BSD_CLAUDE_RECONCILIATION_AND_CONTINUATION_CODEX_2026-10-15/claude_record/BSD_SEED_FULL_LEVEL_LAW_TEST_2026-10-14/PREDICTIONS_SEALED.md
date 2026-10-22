# Sealed predictions: the seed's tame law beyond depth 1 and at the Ш-prime 3

Written 2026-10-14 by Claude (Opus 5.5), BEFORE any seed modular-symbol table exists at these auxiliary primes.
Status: **SEALED, NOT LAUNCHED.** No production computation has been run for this folder.

## What is tested, and why these rows

The 10-07 exactness test (`~/BSD_TAME_LAW_EXACTNESS_TEST_2026-10-07/REPORT.md`) found the depth-2 Mazur–Tate
coefficient equal to K_E·(a_ℓ−2)·R_ℓ exactly in I²/I³ (odd part) on six control curves. Its own scope line says the
cells still untested are "odd Ш (seed 9) … the seed beyond depth 1" (`~/BSD_BUILD_MAP/RUN_NOW_2026-09-29.md`, 10-07
entry "Tame-law exactness → RIGID"). Every existing seed tame table (ℓ = 47, 59, 83, 103, 149, 167, 173, 191, 233, 283,
311) has a squarefree odd part of ℓ−1, so no seed row has ever tested depth ≥ 2 or the 3-adic part of K = 288 = 2⁵·3².

The rows below are the auxiliary primes ℓ ≤ 167 (inside the existing coefficient prefix, T ≤ 57,378,078,719) with
9 | ℓ−1 or 25 | ℓ−1 and a defined regulator. ℓ = 151 is excluded: 5 divides M, so the regulator is undefined at 5.

## Conventions (must be matched exactly by the evaluator)

- Curve: minimal model [0,−1,0,−66020924,−65074271436]; basis P₁ = (−3031, 327384), P₂ = (−2394, 281520).
- g = least primitive root mod ℓ. x(a) = ind_g(a) ∈ Z/(ℓ−1).
- c_k = Σ_{a=1}^{ℓ−1} binom(x(a), k)·N_a, with N_a the record pipeline's plus-symbol numerators (lattice 1/1024,
  ω₁ convention), exactly as in the p = 83 certificate (`~/BSD_UNRESOLVED_SEED_PUSH_2026-10-13/REPORT.md`) and
  `~/BSD_K288_CUSTODY_AUDIT_2026-10-06/c2_from_symbols.py`. Reduce modulo m = odd part of ℓ−1.
- Tame regulator: the 10-06 audit convention (`~/BSD_K288_CUSTODY_AUDIT_2026-10-06/tamereg_audit.gp`), with discrete
  logs kept modulo m instead of modulo p: h(Q) = ind_g(−a/b mod ℓ) for Q = (a/d², b/d³), Q = M·P_i,
  M = cexp·exponent(E(F_ℓ)), b₁₂ = (h(Q₁+Q₂) − h₁ − h₂)/2, R_ℓ = det/M⁴ mod m.
- Law under test: c₀ ≡ c₁ ≡ 0 and c₂ ≡ 288·(a_ℓ−2)·R_ℓ (mod m).

## Predictions

| ℓ | m (odd part of ℓ−1) | a_ℓ | g | R_ℓ mod m | **predicted c₂ mod m** | what it tests |
|---:|---|---:|---:|---:|---:|---|
| 101 | 25 = 5² | −6 | 2 | 6 | **1** | depth 2 at p = 5 |
| 109 | 27 = 3³ | −2 | 6 | 4 | **9** (v₃ = 2) | the 3-part of 288 at depth 3 |
| 127 | 63 = 3²·7 | 22 | 3 | 19 | **9** (≡ 0 mod 9, ≡ 2 mod 7) | 3-part mod 9 and p = 7 |
| 163 | 81 = 3⁴ | −14 | 2 | 65 | **18** (v₃ = 2) | the 3-part of 288 at depth 4 |
| 19 | 9 | 4 | 2 | 8 | 0 | weak: 9 ∣ c₂ only |
| 37 | 9 | 10 | 2 | 1 | 0 | weak: 9 ∣ c₂ only |
| 73 | 9 | −6 | 5 | 7 | 0 | weak: 9 ∣ c₂ only |

Producer: `prescreen/fulllevel_prescreen.gp` (sha256 36554835df4350459b32d93d18fb38737cf1314fe9ba8868dd052e70080533b4),
output `prescreen/fulllevel_prescreen.out` (sha256 87b47bfe2388b1b91bd609aec96adacff12a61ea4bd9b7bdef0a4e247047ccd3).
The prescreen reproduces the record's p = 17, 83 rows with the same code family (R(17,103) = 6, R(83,167) = 42).

## Reading the outcome

- PASS on 101/109/127/163: the exact per-level identity holds on the seed beyond depth 1, and at p = 3 the MT
  leading coefficient carries exactly 3² — the 3-part of #Ш = 9 proved in claim S.3. Calibration only.
- FAIL at the 3-adic rows with v₃(c₂) ≠ 2: the exact law's constant at the Ш-prime differs from 288 on the seed; the
  target statement G1/MI-1 must be restated before anyone attacks it.
- FAIL at 101 (mod 25) or the mod-7 part of 127: the per-level identity fails beyond depth 1 on the seed; the record's
  "MI-1 is an integral per-level identity" reading would be withdrawn for the seed.
- Endpoint effect in every case: **none on FIN, ORDER9 or Q36.** No new prime is settled (ℓ = 101, 109, 127, 163 serve
  only p ∈ {3, 5, 7}, all already settled).
