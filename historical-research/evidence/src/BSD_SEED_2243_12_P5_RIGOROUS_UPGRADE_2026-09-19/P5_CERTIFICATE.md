# P5_CERTIFICATE: rigorous replacement of master-certificate node N7 (the p = 5 modular symbols)

**Curve.** E : y² = x³ − 22735x² + 106272484x, with N = 2³·3·2243·4547²·5843, w = +1, a₅ = −2 (good ordinary at 5) and Δ > 0.

**Run.** 2026-09-19 06:28:48 → 07:08:29 PDT, directory `~/BSD_SEED_2243_12_P5_RIGOROUS_UPGRADE_2026-09-19/`.
- Pipeline: `~/BSD_RIGOROUS_STREAM_CORE_2026-09-19/p3plan/run_p3.sh` (generic target list), with TARGETS="25:1:1 5:1:1", LATDEN = 1024 and J = W = 16.
- The guard variable P3_AUTHORIZED=yes was set under the operator's p = 5 authorization.

**Successor, not replacement of files.**
- This certificate supersedes the **evidence** for node N7 (CERT-NUM) of `~/SEED_2243_12_MASTER_CERTIFICATE_2026-09-18/00_CERTIFICATE.md`.
- That file, its addenda and bindings are **unchanged**, and nothing is merged.

## 0. Result

    the 20 symbols [b/25]⁺ are, exactly (b = 1..24, 5 ∤ b):
      −54, 16, 90, −52, −76, 16, 76, −52, −54, 90, 90, −54, −52, 76, 16, −76, −52, 90, 16, −54
    six-symbol value 3([2]+[3]+[4]+[11]) + 4([9]+[12]) = 3·0 + 4·38 = 152 ≡ 2 (mod 5)
    a_{2,2} ≡ 2 (mod 5) (ω₁ normalisation; Néron normalisation: 1), so ord₅(a₂) = 0

These values are identical to the historical LP5 output: node N7 is **confirmed**, now at proof grade.

## 1. Parameters (exact)

| item | value |
|---|---|
| targets | m = 25 (the 20 symbols of N6/N7) and m = 5 (the α⁻³[b/5]⁺ term of the exact measure and the T₅ Hecke check); M = gcd(m, N) = 1; Q = N; s = w = +1 |
| lattice (theorem input) | (1/1024)Z. The audited gate gives x_b ∈ (1/c_E)Z (N7), or conservatively (1/(2c_E))Z (gate addendum (iii)), with c_E \| 512 (N8). Both lie inside (1/1024)Z |
| truncation (`arbcore tmin`, exact) | m = 25: T_min = 7 825 119 335 (T_min − 1 fails), T = 7 834 959 871 = 467·2²⁴ − 1. m = 5: T_min = 1 511 545 536, T = 1 526 726 655 = 91·2²⁴ − 1 |
| rigorous error | 2·tail_MS(T) ≤ 1.327016732·10⁻⁵ (m = 25) and 1.081840123·10⁻⁵ (m = 5); divided by Ω⁺ both are < 1/2048 |
| periods (Arb, AGM) | Ω⁺ = ω₁ = [0.0280449015194364044483094018079 ± 3.04·10⁻³²]; Ω⁻ = [0.0305556264963434249561173450733 ± 1.88·10⁻³²] |

## 2. Coefficient certificate (Stage W)

- For every prime q ≤ 7 834 959 871:
  - **either** the untrusted producer (`apwit`) proposes a_q with a group-order witness, and the independent 145-line integer verifier (`wverify`) proves it;
  - **or** a_q is counted exhaustively, for q < 4096 or q ∣ Δ.
- Each `.done` marker was written only after verification. There were **0 failures**.

| quantity | value |
|---|---|
| segments (2²⁴ wide) | 467 of 467 |
| primes verified | **360 542 141** = PARI `primepi(7834959871)` (independent count) |
| by checked witness / by exhaustive count | 360 541 575 / 566 |
| **aggregate a_q root** (SHA-256 over the 467 verifier segment digests) | `fcd024375b54642344d03502caf0c53882190973ab2683239011f813ca2848d4` |
| a_q root over segments 0..90 (the m = 5 range) | `35a4745fbce663ec63475f573ca82376c8557ab51557a968d5c0d1b6c78157af` |
| **cross-run** | all 467 verifier records, verified a_q files and witness files are **byte-identical** to the independent p = 3 run's segments 0..466 (`downstream/CROSS_RUN_P3.txt`). The p = 3 run's root over the same segments is also `fcd02437…` |
| files kept | 467 witness files and 467 a_q files; hashes in `run/logs/`, re-verified by the integrity audit |

## 3. Symbol certificate (Stage A: `arbcore msl`, Arb ball arithmetic)

| target | wall / CPU (exact) | a_q root consumed | count identity | identified in (1/1024)Z |
|---|---|---|---|---|
| m = 25 | 352.6 s / 5 563 CPU-s (1.55 CPU-h); max RSS 1.42 GB | `fcd02437…` (= §2) | 2 559 233 045 smooth + 5 275 726 826 pairs = T | **20/20 plus, 20/20 minus** |
| m = 5 | 72.8 s / 1 016 CPU-s (0.28 CPU-h) | `35a4745f…` (= §2) | 501 449 581 + 1 025 277 074 = T | **4/4 plus, 4/4 minus** |

Every ball contains exactly one point of (1/1024)Z, and its radius is below 1/2048 with the tail included. **All 48 identified values are integers.**

| b (mod 25) | 1 | 2 | 3 | 4 | 6 | 7 | 8 | 9 | 11 | 12 | 13 | 14 | 16 | 17 | 18 | 19 | 21 | 22 | 23 | 24 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [b/25]⁺ | −54 | 16 | 90 | −52 | −76 | 16 | 76 | −52 | −54 | 90 | 90 | −54 | −52 | 76 | 16 | −76 | −52 | 90 | 16 | −54 |
| [b/25]⁻ | −27 | 65 | 124 | −36 | −2 | −65 | 0 | −36 | −27 | 124 | −124 | 27 | 36 | 0 | 65 | 2 | 36 | −124 | −65 | 27 |

[c/5]⁺ = (144, −144, −144, 144) and [c/5]⁻ = (−8, 0, 0, 8) for c = 1..4.

Machine-readable: `run/SYMBOLS_m25.txt` and `run/SYMBOLS_m5.txt`. Exact ball dumps: the `SDUMP` lines of `run/msl_m{25,5}.txt`.

## 4. Downstream: the depth-2 coefficient

**Specification** (SW gate Phase C; master N6):
- μ(b + 25Z₅) = α⁻²[b/25]⁺ − α⁻³[b/5]⁺, where α is the unit root of x² + 2x + 5 (a₅ = −2).
- P₂(T) = Σ_{a=1}^{4} Σ_{j=0}^{4} μ(ω(a)6ʲ)(1+T)ʲ.
- a₂ ≡ a_{2,2} (mod 5), by SW Prop. 3.5 with c = 0 (5 ∤ c_E).

| route | result |
|---|---|
| **A**: audited six-symbol formula 3([2]+[3]+[4]+[11]) + 4([9]+[12]) | 3(16 + 90 − 52 − 54) + 4(−52 + 90) = **152 ≡ 2 (mod 5)** |
| **B**: independent exact evaluator (α by Hensel lifting mod 5²⁰, α ≡ 13 mod 25 as in N6; Teichmüller lifts 1, 7, 18, 24 recomputed; all 20 + 4 symbols; the α⁻³ term included) | a_{2,0} = **0** exactly; a_{2,1} ≡ 0 (mod 5) with ord₅ = 1; **a_{2,2} ≡ 2 (mod 5), ord₅ = 0**. The α⁻³[b/5]⁺ part is ≡ 0 (mod 5), as the gate's addendum states |
| **C**: historical LP5 output (consistency only) | all 20 symbols equal, and the six-symbol value is 152 = 152: **no disagreement** |

Normalisation (gate addendum (ii): every normalisation in play differs by a 5-adic unit, since 5 ∤ c_E):

| normalisation | a_{2,2} mod 5 |
|---|---|
| ω₁ (x_b as computed; master N6/N9) | 2 |
| Néron period Ω_E⁺ = 2ω₁ with λ_f | 1 |
| Néron period with the curve's parametrisation (factor c_E/2; c_E = 2^k, k unknown) | 1, 2, 4 or 3: **never 0** |

**ord₅ a₂ = 0** in every normalisation.

## 5. Checks (all PASS)

**Stage C** (`run/P3_CHECK.txt`, 7/7):
- the segment roots equal the verifier roots (m = 25: 467 segments; m = 5: 91);
- the count identities hold;
- every plus and minus symbol is identified uniquely;
- the T₅ Hecke relation a₅[c/5] = Σ_{j<5}[(c+5j)/25] + [0] holds for all 8 (c, sign), exactly, with [0] = 0.

**Integrity** (`downstream/INTEGRITY.txt`, independent code, 19/19):
- done markers, tiling, and producer/verifier counts;
- every a_q and witness file matches its hash;
- PARAMS locks are correct;
- the unit sets are complete, with **2 335 + 455 unit self-hashes valid**;
- the Part-L a_q hashes equal the verifier's;
- the roots and count identities recompute.

**Downstream** (`downstream/P5_DOWNSTREAM.txt`, 21/21):
- a₅ = −2 is read from the verified file;
- the symbol sets are complete and the symmetries hold;
- the denominators are prime to 5, and the symbols lie in (1/512)Z;
- T₅ holds, and Σ_c[c/5]⁺ = 0;
- α ≡ 13 (mod 25); the Teichmüller lifts are correct; the residues run over all units;
- a_{2,0} = 0, and a_{2,1} ≡ 0 (mod 5);
- route A = route B, and the α⁻³ term vanishes mod 5;
- route C agrees (20/20 and 152).

**Independent counts:**
- PARI `primepi(7834959871)` = 360 542 141 = the verifier's total.
- The cross-run a_q root equals the p = 3 run's.

## 6. Engine identity

The engine is identical to the p = 3 run (`prelaunch/source_and_binary_hashes.txt`):
- arbcore.c `56a43aac…`, apwit.c `e6cca7ff…`, fastap.c `7d3f4d51…`, wverify.c `128e7960…`, run_p3.sh `6b7b071c…`, p3_check.py `1922291c…`;
- the binaries are byte-identical to the core MANIFEST (`f94c90c7…`, 1718/1718 verified).

**Trust base:**
- FLINT/Arb 3.3.1, GMP 6.3, MPFR 4.2.2;
- Apple clang 21;
- the verifier and the engine;
- the hardware and OS.

The producer, PARI, the Python comparators and the LP5 stream are **not** in the trust base.
