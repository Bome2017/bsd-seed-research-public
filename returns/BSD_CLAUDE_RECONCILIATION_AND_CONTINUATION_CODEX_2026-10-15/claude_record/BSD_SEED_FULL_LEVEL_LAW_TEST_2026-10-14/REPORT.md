# The seed's exact tame law beyond depth 1 and at the Ш-prime 3: all seven sealed rows pass

2026-10-14. Claude (Opus 5.5), run at the user's request ("Sure do 1"). **Verdict: SEALED_PREDICTIONS_7_OF_7_PASS.**
Grade: computer-assisted numerical test of a conjectural identity, with sealed predictions and independent re-evaluation.
It is not a proof, not human review, not formal verification. **Endpoint effect: none. FIN, ORDER9 and Q36 are unchanged.**
No new coefficient prime is settled.

## 1. What was tested

The record's per-level reading of the tame law is: the depth-2 Mazur–Tate coefficient of θ_ℓ equals
288·(a_ℓ − 2)·R_ℓ in I²/I³, odd part of ℓ − 1, with 288 = 32·#Ш = 2⁵·3². It had been checked on the seed only modulo
single primes p ∥ ℓ − 1 (ten (p, ℓ) points), and exactly at full level only on six other curves. The 10-07 exactness test
listed two cells as untested: "odd Ш (seed 9)" and "the seed beyond depth 1". Every earlier seed tame table had a
squarefree odd part of ℓ − 1.

Seven new seed tables were computed at auxiliary primes with 9 | ℓ − 1 or 25 | ℓ − 1. Predictions were sealed before any
table existed (`PREDICTIONS_SEALED.md`, sha256 e91c74e3…, verified unchanged before and after the runs).

## 2. Results

c_k = Σ_a binom(ind_g(a), k)·[a/ℓ]⁺, g the least primitive root, symbols in the record's ω₁ convention; m = odd part of
ℓ − 1. "Law" = 288·(a_ℓ − 2)·R_ℓ mod m with R_ℓ from the independent GMP regulator code.

| ℓ | m | sealed c₂ | computed c₂ mod m | 2nd primitive root: c₂ vs law | c₀, c₁ mod m | what the row tests |
|---:|---:|---:|---:|---|---|---|
| 101 | 25 = 5² | 1 | **1** | 16 vs 16 | 0, 0 | depth 2 at p = 5 |
| 109 | 27 = 3³ | 9 | **9** | 9 vs 9 | 0, 0 | v₃ = 2 at depth 3 |
| 127 | 63 = 3²·7 | 9 | **9** | 36 vs 36 | 0, 0 | 3² and p = 7 |
| 163 | 81 = 3⁴ | 18 | **18** | 45 vs 45 | 0, 0 | v₃ = 2 at depth 4 |
| 19 | 9 | 0 | **0** | 0 vs 0 | 0, 0 | weak: 9 ∣ c₂ |
| 37 | 9 | 0 | **0** | 0 vs 0 | 0, 0 | weak: 9 ∣ c₂ |
| 73 | 9 | 0 | **0** | 0 vs 0 | 0, 0 | weak: 9 ∣ c₂ |

Exact coefficients at the decisive rows (GP cross-check): ℓ = 163: (c₀, c₁, c₂) = (0, −10044, −263718);
ℓ = 109: (0, −6912, −208080); ℓ = 101: (0, −44300, −1209274). c₁ is divisible by the full odd modulus in every row,
so θ_ℓ ∈ I² holds at full level, and c₂ mod m is the I²/I³ coefficient.

At ℓ = 127 the unchanged frozen checker, run with p = 7, returns NONZERO with c₂ ≡ 2 (mod 7): a second Ota certificate
for Ш[7^∞] = 0, which was already settled. Record only.

## 3. What the result means, and what it does not

- The exact per-level identity holds on the actual seed beyond depth 1: mod 5² at ℓ = 101.
- At the prime 3, where Ш[3^∞] ≅ (Z/3)² is proved in writing (claim S.3), the Mazur–Tate coefficient carries exactly 3²
  in the tested rows: c₂ ≡ 9 (mod 27) at ℓ = 109 and c₂ ≡ 18 (mod 81) at ℓ = 163, as the constant 288 = 32·9 requires.
  This is the first test of the seed's law where its #Ш factor is not a unit.
- Together with the earlier rows, every tested seed level is consistent with one integral identity per level with the
  single constant 288: the rank-two Mazur–Tate refined conjecture at prime level, with #Ш = 9. The target G1/MI-1 for the
  seed can be stated in that exact form, including the Ш-prime.
- Not shown: any proof of the identity, at any level not computed. The 3-adic rows sit at a bad prime (3 ∣ N), outside the
  domains of Ota's theorem and of the proved K288 facts; they are observations about θ_ℓ, not certificates. The three
  m = 9 rows only test 9 ∣ c₂. Agreement at finitely many levels gives no cofinite statement; FIN-tail still needs a
  proof valid at almost every level, and no method for that is known.

## 4. How it was run, and custody

- Engine: the frozen p83 package `~/BSD_UNRESOLVED_SEED_PUSH_2026-10-13/FROZEN_RUN_PACKAGE_p83_l167`, arbcore sha256
  47d07f2e…, unchanged checker, `run_chain.sh` here; 8 threads; coefficient prefix
  `~/BSD_P17_PREREQUISITES_2026-09-25/singleton_probe/corpus_ext_6445/view/ap`; receipts from the package.
- T per ℓ: the engine's own `tmin` mode at LATDEN 4096, aligned up to a segment boundary (`tmin/`).
- Checker outcome: every row's only failure reasons are the p-admissibility rules ("p must be a prime ≥ 5",
  "v_p(ℓ−1) > 1"), which these full-level rows violate by design; PARAMS, manifest, COUNT identity, receipt root and
  symbol identification all pass. No coefficient file was modified during the runs.
- New code: `eval/evaluate_full_level.py` re-identifies every symbol from its printed ball (exact decimal arithmetic) and
  computes c₀..c₃ at full level; it reproduces the certified p83 value c₂ ≡ 44 (mod 83) and the existing ℓ = 103 table
  at full level (mod 51). `eval/regulator_gmpy2.py` computes R_ℓ with GMP rationals and no PARI, for two multipliers M;
  it reproduces R(83,167) = 42 and all seven sealed regulators. `eval/gp_crosscheck/` recomputes the decisive rows in GP.
- Cost: 22.8 CPU-hours over 2 h 52 min wall, 16:25:48–19:17:30 UTC; peak memory 0.74 GB per run; 542 MB of outputs.

| ℓ | T | segments | wall s | msl.txt sha256 (prefix) | segment root (prefix) |
|---:|---:|---:|---:|---|---|
| 19 | 6,257,901,567 | 373 | 307 | 825b406968d5e78b | 6998bf6447af5c39 |
| 101 | 34,359,738,367 | 2048 | 1643 | 28926b21f894be08 | f9025fc6471fe407 |
| 109 | 37,144,756,223 | 2214 | 1822 | a4fed9a29598a822 | e87eea8a81aad4ab |
| 127 | 43,402,657,791 | 2587 | 2095 | b78a58485570fe82 | 9ca04490f29cbfac |
| 163 | 55,968,792,575 | 3336 | 2689 | abe9bb88835f65f1 | 9d6c8f74fe18d875 |
| 37 | 12,348,030,975 | 736 | 571 | d5153fd23318e2ec | 585f87ba270cf014 |
| 73 | 24,679,284,735 | 1471 | 1164 | 211121fb9624b6f9 | ef68cc042b84ac4e |

`PRE_RUN_CLARIFICATION.md` (written before any table existed) fixes that the symbols enter as their integer values
cand/1024, as in the 288 fit; the sealed file's word "numerators" was imprecise and no prediction depended on it.
Full outputs: `RESULTS.json`, `RESULTS.md`, `eval/`, `production/` (per-row `msl.txt`, `RUN_MANIFEST.json`,
`SINGLETON_REPORT.json`, logs), `MANIFEST.sha256`. Local only; nothing was pushed.
