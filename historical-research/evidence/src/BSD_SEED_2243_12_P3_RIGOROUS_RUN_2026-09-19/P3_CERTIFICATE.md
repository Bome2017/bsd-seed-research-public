# P3_CERTIFICATE: rigorous depth-4 p = 3 computation for the seed

**Curve.** E : y² = x³ − 22735x² + 106272484x, with N = 2³·3·2243·4547²·5843, w = +1 and a₃ = −1 (non-split multiplicative at 3).

**Run.** 2026-09-18 23:07:11 → 2026-09-19 00:28:40 PDT, directory `~/BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/`. The pipeline is `~/BSD_RIGOROUS_STREAM_CORE_2026-09-19/p3plan/run_p3.sh`, with P3_AUTHORIZED=yes, J = W = 16 and the default targets.

## 0. Result

    a_{4,2} = 15480 = 2³·3²·5·43     (exact; symbols normalised by ω₁)
    a_{4,2} ≡ 9 (mod 27)             (SW / Néron-period normalisation, x_b/2: a_{4,2} = 7740 ≡ 18 (mod 27))
    ord₃(a_{4,2}) = 2   ⇒ CASE A

The forced values also hold: a_{4,0} = 0 and a_{4,1} = −54 ≡ 0 (mod 27).

## 1. Parameters (exact)

| item | value |
|---|---|
| targets | m = 81 and m = 27 only; M = gcd(m,N) = 3; Q = N/3 = 2167729337579528; s = −w·a₃ = +1; κ = 2π/(m√Q) |
| lattice (theorem input) | (1/1024)Z (LATDEN = 1024) |
| truncation | m = 81: T_min = 14 832 175 873, T = 14 847 836 159 = 885·2²⁴ − 1. m = 27: T_min = 4 830 360 876, T = 4 831 838 207 = 288·2²⁴ − 1. Both are exact Arb minima (T_min − 1 fails) |
| rigorous error | 2·tail_MS(T) = 1.333053816·10⁻⁵ (m = 81) and 1.358052210·10⁻⁵ (m = 27), as upper bounds; divided by Ω⁺, both are < 1/2048 |
| periods (Arb, AGM) | Ω⁺ = ω₁ = [0.0280449015194364044483094018079 ± 3.04·10⁻³²]; Ω⁻ = [0.0305556264963434249561173450733 ± 1.88·10⁻³²] |

## 2. Coefficient certificate (Stage W)

- Every prime q ≤ 14 847 836 159 was handled in one of two ways:
  - **by checked witness:** the untrusted producer (`apwit`) proposes a_q with a group-order witness, and the independent 145-line integer verifier (`wverify`) re-proves it;
  - **by exhaustive count:** for q < 4096 or q ∣ Δ.
- Every segment was verified before its `.done` marker was written. No FATAL occurred anywhere.

| quantity | value |
|---|---|
| segments (2²⁴ wide) | 885 of 885 |
| primes verified | **663 685 727** = PARI `primepi(14847836159)` (independent count) |
| by checked witness / by exhaustive count | 663 685 161 / 566 |
| **aggregate a_q root** (SHA-256 over the 885 verifier segment digests) | `5f9994d95c31a49e7cbd91435fd33a9cbdadc81fcc4f47439fbbf2fa5bb4713f` |
| a_q root over segments 0..287 (the m = 27 range) | `ca234d65fa40332695f5f08675ade782c9a8439bee068b69ac9b64a470002084` |
| witness files kept | 885 files (17 GB); each SHA-256 in `run/logs/witsha_<s>.txt`, re-hashed by `downstream/p3_integrity.py` |
| verified a_q files | 885 files (2.5 GB); each SHA-256 = the verifier's `ap_sha256`, re-hashed |

## 3. Symbol certificate (Stage A, `arbcore msl`, Arb ball arithmetic)

| target | wall / CPU (exact) | a_q root consumed | count identity | identified |
|---|---|---|---|---|
| m = 81 | 687.6 s / 10 823 CPU-s (3.01 CPU-h); max RSS 1.35 GB (1.29 GiB) | `5f9994d9…` (= §2) | 4 841 666 641 smooth + 10 006 169 518 pairs = T | **54/54 plus, 54/54 minus** |
| m = 27 | 213.3 s / 3 305 CPU-s (0.92 CPU-h) | `ca234d65…` (= §2) | 1 580 993 508 + 3 250 844 699 = T | **18/18 plus, 18/18 minus** |

- Every ball contains exactly one point of (1/1024)Z; its radius is below 1/2048 and includes the rigorous tail.
- **All 144 identified values are integers.** So they also lie in (1/512)Z, the sharper lattice (F1 CP-F).
- Full tables: `downstream/symbol_tables.md`. Machine-readable: `run/SYMBOLS_m81.txt` and `run/SYMBOLS_m27.txt`. Exact ball dumps: the `SDUMP` lines of `run/msl_m81.txt` and `run/msl_m27.txt`.

**[b/81]⁺** for b = 1..40 (3 ∤ b), with [81−b]⁺ = [b]⁺:

| b | 1 | 2 | 4 | 5 | 7 | 8 | 10 | 11 | 13 | 14 | 16 | 17 | 19 | 20 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [b/81]⁺ | −101 | 63 | 88 | 76 | 14 | −36 | 76 | −89 | 93 | −36 | 14 | −60 | −13 | 108 |

| b | 22 | 23 | 25 | 26 | 28 | 29 | 31 | 32 | 34 | 35 | 37 | 38 | 40 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [b/81]⁺ | −60 | −57 | 63 | −57 | 88 | −66 | −101 | −53 | −89 | 93 | −53 | 108 | −13 |

## 4. Downstream evaluation (exact rational arithmetic)

- **Measure** (SW §3; F1 CP-F): μ(b + 3⁴Z₃) = α⁻⁴[b/81]⁺ with α = a₃ = −1. a₃ is read from the verified a_q file.
- **Approximation:** P₄(T) = Σ_{a∈{1,2}} Σ_{j<27} μ(ω(a)·4ʲ) (1+T)ʲ, with ω(2) = −1. So a_{4,j} = Σ_b w_{4,j}(b)[b/81]⁺.

The coefficients were computed three ways, all agreeing exactly:

| route | a_{4,0} | a_{4,1} | a_{4,2} |
|---|---|---|---|
| Lane 3 weight files `p3_weights_n4_j{0,1,2}.txt` (sha256 `23b8f7d5…`, `4204cfba…`, `e7341acb…`; AUDIT_D-recomputed) | 0 | −54 | 15480 |
| weights recomputed independently in `downstream/p3_downstream.py` (identical vectors) | 0 | −54 | 15480 |
| Lane 3 generic evaluator `an2` from `weights.gp` (sha256 `5c0476bd…`), copied verbatim | — | — | 3² + O(3³); mod 3⁶ = 3² + 2·3⁴ = 171 = 15480 mod 729 |

The folded sum is in `downstream/a42_folded_sum.txt`: 25 nonzero folded weights, total 15480.

**Lower depths** (independent m = 27 run, with U₃ for depth 2): a_{3,·} = (0, 1260, 3186) and a_{2,·} = (0, 378, 252). a_{2,2} = 2[2/9]⁺ = 252 ≡ 0 (mod 3), as Lane 3 predicted.

## 5. Checks (all PASS)

**Stage C** (`run/P3_CHECK.txt`, the existing checker, 7/7):
- the segment roots equal the verifier roots (m = 81, m = 27);
- the count identities hold;
- every plus and minus symbol is uniquely identified;
- U₃: a₃[b/27] = Σ_{j<3}[(b+27j)/81] holds for all 36 (b, sign), exactly.

**Integrity** (`downstream/INTEGRITY.txt`, independent code, 19/19):
- all 885 done markers are present, and each segment was logged once by the verifier with the correct tiling;
- producer and verifier witness counts are equal;
- every a_q file has the right size and hash, and every kept witness file matches its hash;
- PARAMS locks are correct;
- all unit sets are complete, with no `.tmp` left;
- **all 5 865 unit self-hashes are valid**, and every Part-L unit's a_q hash equals the verifier's;
- both AP_SEGROOTs and both count identities recompute.

**Downstream** (`downstream/P3_DOWNSTREAM.txt`, 20/20):
- a₃ = −1;
- the symbol sets are complete;
- the Teichmüller representatives are correct;
- Lane 3 weights = recomputed weights;
- U₃ 81 → 27 holds for both signs;
- **[1/3]⁺ = [2/3]⁺ = 0**;
- the symmetries hold;
- the symbols lie in (1/512)Z;
- file route = recomputed route;
- the depth-2 formula holds;
- the coefficients are 3-integral;
- **a_{n,0} = 0 for n = 2, 3, 4**;
- **a_{4,1} ≡ 0 (mod 27)**;
- the four SW Prop 3.5 congruences between depths 2, 3 and 4 hold.

**Independent counts:** PARI `primepi(14847836159)` = 663 685 727 = the verifier's total.

## 6. Engine identity

Source sha256 (the core MANIFEST f94c90c7… verified 1718/1718 before and after rebuilding):

| file | sha256 |
|---|---|
| arbcore.c | 56a43aac38161d48848df4ed5c2f931f1dc7d5db745600bd140e4be3cac67fd7 |
| apwit.c | e6cca7ffed1256b5cde682d48561805fc2111e97a0a4b08d438e593126af9d8b |
| fastap.c | 7d3f4d515aea25a10add93ef02b36b3e5da7ec409348a166e07d260df0b69526 |
| wverify.c | 128e7960f8efc0756557f2ee5619c1e80f7e9e0f69b6007f70cac63707abb596 |
| run_p3.sh | 6b7b071c19d472b8358ac904cb72c15585a260f9891504797053ff43fc1a55aa |
| p3_check.py | 1922291c13154d2abb484343108c122c71483f5bf68b18cb277a74e770d65566 |

The binaries (arbcore 47d07f2e…, apwit c21429cc…, wverify 9f4b136a…) are byte-identical to the MANIFEST entries.

**Trust base** (as in the core's `ANALYTIC_RANK_CERTIFICATE.md` §7):
- FLINT/Arb 3.3.1, GMP 6.3, MPFR 4.2.2;
- Apple clang 21;
- the verifier and the engine;
- the hardware and OS.

The producer, PARI, Sage and the Python comparators are **not** in the trust base; their outputs are either re-proved or only cross-checked.
