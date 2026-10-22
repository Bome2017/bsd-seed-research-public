# Curve data and settled primes (extracted verbatim from the seed master map, 2026-10-01; §2 and §4.1–4.2)

Paths in the tables refer to the author's machine and are given only as provenance.

## §2 The curve

| Item | Value | Source |
|---|---|---|
| Model | y² = x³ − 22735x² + 106272484x | A.1 |
| Global minimal model | [0,−1,0,−66020924,−65074271436], via x = X + 7578, u = 1 (same invariant differential) | A.1, S.3L, B.16 |
| c₄, c₆ | 3169004368, 56243184546880 | paper 02_curve.tex |
| Δ_min | 2⁸·3²·2243·4547³·5843² = 16586638656786071143743744 > 0, so E(ℝ) has two components | A.1 |
| j | 1322372123614064/689197281363 ∉ ℤ, so E has no CM | A.2 |
| Origin | Zywina family (m,n) = (2243,12). m + 16n² = 4547 and m + 25n² = 5843; all three are ≡ 11 mod 24 | 03_rank.tex |
| 2-isogenous curve | E′: y² = x(x² + 45470x + 91790289) | 03_rank.tex |
| Conductor | N = 2³·3·2243·4547²·5843 = 6503188012738584 | A.1 |
| Tamagawa product | 16 | A.1 |
| Root number | +1; local factor −1 at 2243 and at ∞ | A.1, SPS |
| Torsion | ℤ/2 = ⟨T⟩, T = (0,0) | A.1, R.1 |
| Generators (basis of E(ℚ)/tors, index 1) | P₁ = (4547, 327384), P₂ = (5184, 281520). On the minimal model: (−3031, 327384) and (−2394, 281520). Alternative basis: P₂ and G = (5843, 210348) = −P₁ − P₂ + T | R.1 |
| 2-Selmer | rank 3 (including torsion); Ш[2] = 0 | R.1 |
| Image of Galois | mod-ℓ is GL₂(F_ℓ) for every odd ℓ; ℓ-adic surjective for ℓ ≥ 5 | A.3 |
| Manin constant | c₀ = 2^a with a ≤ 8, and 4547 ∤ c₀. c_E \| 2⁹, so symbols lie in (1/1024)ℤ at rational unitary cusps | A.4 |
| Good supersingular primes < 2000 | 23, 29, 131, 167, 281, 563, 661, 823, 839, 863, 887, 1013, 1471, 1511, 1823 | A.1 |
| Anomalous primes | none; #E(F₅) = 8 | A.1 |
| Exceptional good primes (BKS/class-group set) | a₁₉ = 4, a₅₉ = −4, a₄₈₇ = −28; 2242 = 2·19·59 and 5844 = 12·487 | B.20 |
| B* (Theorem W exclusions) | {2, 3, 19, 59, 487, 2243, 4547, 5843} | B.19 |
| ω₁ | 0.0280449015194364044483094018079 ± 3.04e−32; Ω_E = 2ω₁ | R.5 |
| Reg (BSD normalization) | 17.79651747249034020748 < Reg < 17.79651747249034039153 | R.5 |
| Ω_E·Reg | (0.99820315980984172437, 0.99820315980984173470) | R.5 |
| L(E,1), L′(E,1) | both 0 | R.2 |
| L″(E,1)/2 | [35.929604, 35.941023]: Arb partial sum to n ≤ 1.5e8 plus tail bound 5.709e−3 | R.3 |
| q | (35.99427, 36.00573). The float estimate 36 ± 3e−15 is evidence only, never a proof input | R.6 |
| Twist E^{−23} | rank 1; L′ ∈ [39.512236, 40.182321]; rank E(ℚ(√−23)) = 3 | K.1 |
| Twist E^{−7} | rank 0; L ∈ [9.054319, 9.054421]; rank E(ℚ(√−7)) = 2, with (r⁺, r⁻) = (2, 0) | K.2 |
| Ω⁻ | defined in A.4; no value in the release | — |

**Bad reduction**

| p | Kodaira | c_p | a_p | Type |
|---|---|---|---|---|
| 2 | I₁* | 2 | 0 | additive |
| 3 | I₂ | 2 | −1 | nonsplit multiplicative |
| 2243 | I₁ | 1 | +1 | split multiplicative |
| 4547 | III | 2 | 0 | additive, potentially good supersingular (j ≡ 1728; inertia of order 4) |
| 5843 | I₂ | 2 | −1 | nonsplit multiplicative |

**Certified witness coefficients**
- p = 3: a₄,₂ = 15480 ≡ 9 mod 27 (ω₁ normalization); a₄,₀ = 0; a₄,₁ = −54.
- p = 5: six-symbol value 152, so a₂,₂ ≡ 2 mod 5.
- p = 7, 11, 13: C₇ ≡ 1 mod 7; C₁₁ ≡ 8 mod 11; C₁₃ ≡ 2 mod 13.
- p = 17–47: singleton c₂ values, listed in §4.2.
- p = 2243: D5 gives Reg_γ ≡ 2181 and ℓ_γ ≡ 1799 mod 2243.

---


## §4 Per-prime ledger

**Path keys**
- `SP` = `~/BSD_P17_PREREQUISITES_2026-09-25/singleton_probe`
- `MH` = `~/BSD_CODEX6_MASTER_HANDOFF_2026-09-19`
- `ST` = `~/BSD_BAD_PRIME_STREAMING_RETURN_OPUS_2026-09-29`
- `P53` = `~/BSD_P53_L743_RUN_2026-10-01`

No prime has a human review.

### 4.1 Settled, p ≤ 13

| p | Ш[p^∞] | Method | Certificate | Grade | Cost | Date |
|---|---|---|---|---|---|---|
| 2 | 0 | 2-isogeny descent: PARI `ellrank` [2,2,0], eclib `mwrank -d` (rank S² = 3), Sage saturation (index 1) | `~/BSD_PERIMETER_Q36_2026-09-25/descent/` (CERTIFICATE.md, verify_descent.sh) | S.2 EXACT_COMPUTATION | replay 4–10 s | 09-25 |
| 3 | (ℤ/3)² | Four claims, listed below the table | `~/BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/`; `~/BSD_P3_LOWER_HALF_3DESCENT_RETURN_OPUS_2026-09-29/verify_certificate.gp`; `~/BSD_P3_UPPER_REPAIR_SCREEN_RETURN_OPUS_2026-09-29/`; `~/BSD_P3_MS_R24_COLEMAN_RETURN_OPUS_2026-09-29/`; Lean A5 `~/BSD_FINITE_PART_HARDENING_2026-09-24/A5_p3/` | S.3 PROVED_COMPUTER_ASSISTED + IMPORTED_PUBLISHED + PROVED_WRITTEN + LEAN_CHECKED (Skinner route only). S.3L EXACT. S.3K PROVED_WRITTEN (3 model readers + 1 Codex reading) | depth-4 run ≈21 CPU-h; 3-descent ≈2.5 CPU-h (verifier 0.2 s) | 09-19; S.3L/S.3K 09-29 |
| 5 | 0 | a₂,₂ ≡ 2 mod 5 (six-symbol value 152), then Kato + SW 6.1; uses v₂(c₀) ≤ 8 | `~/BSD_SEED_2243_12_P5_RIGOROUS_UPGRADE_2026-09-19/` | S.5 PROVED_COMPUTER_ASSISTED + IMPORTED_PUBLISHED + LEAN_CHECKED (A4) | ≈10 CPU-h | 09-18/19 |
| 7 | 0 | C₇ ≡ 1 mod 7 (weighted sum −1931), criterion B.1 | `MH`/audits/P7_PRIMARY_THEOREM.md | S.7 (same grades) | 18.5 min wall on 12 workers | 09-20 |
| 11 | 0 | C₁₁ ≡ 8 mod 11 (sum −190) | `MH`/audits/P11_PRIMARY_THEOREM.md | S.11 | 11,408 s wall | 09-21 |
| 13 | 0 | C₁₃ ≡ 2 mod 13 (sum −3950). The run's own 7/8 were misnormalized (W.3) | `MH`/audits/P13_PRIMARY_THEOREM.md | S.13, with the write-through-incident qualification | 2 h 35 min wall | 09-21/22 |

**The four claims behind p = 3:**
- **S.3:** a₄,₂ = 15480 ≡ 9 mod 27, then SW Prop 3.5, Skinner Thm A, Jones 3.1 and Cassels–Tate.
- **S.3L:** two explicit cubics give #Ш[3] ≥ 9 with no GRH and no SU.
- **S.3F:** finiteness from Kato 18.4.
- **S.3K (route K, primary since 09-29):** #Ш[3^∞] ≤ 9, via the integral Coleman map at nonsplit 3 and Kato 13.4(3)/13.14.

### 4.2 Settled, 17–47 (Ota singleton witness)

- **The test:** c₂ = Σ C(ind_g(a) mod p, 2)·[a/ℓ]⁺. The frozen checker returned NONZERO in every row.
- **Grade:** S.17-47 PROVED_COMPUTER_ASSISTED + PROVED_WRITTEN + IMPORTED_PREPRINT. Ota is published (Amer. J. Math. 140, 2018), but the theorem numbers were read from arXiv v1.
- **Files:** each package is `SP`/FROZEN_RUN_PACKAGE_<id>/; each result is `SP`/seed_runs/<id>/RESULT_P<p>.md.

| p | Type | ℓ (g) | T (segments) | c₂ ≡ (mod p) | Package / pinned root | CPU-h | Notes | Review |
|---|---|---|---|---|---|---|---|---|
| 17 | ord | 103 (5) | 33,218,887,679 (1,980) | 46298 ≡ 7 | 7248cf5 / 55095730… | 3.64 | depth-3 route (≈3,160 CPU-h) archived; **ball radius ≈ 99% of the half-spacing** | Fable PASS_AT_RETAINED_GRADE |
| 19 | ord | 191 (19) | 65,783,463,935 (3,921) | −30432 ≡ 6 | 2dd268d / 58d28b37… | 8.69 | run 1 INVALID (arb_div margin; 7.25 CPU-h) | Fable PASS |
| 23 | ss | 47 (5) | 14,914,945,023 (889) | 103854 ≡ 9 | 0f4683d / a83f42e3… | 1.67 | replaced Criterion SS (≈500 CPU-h); **margin ≈ 99%** | Fable PASS |
| 29 | ss | 233 (3) | 80,564,191,231 (4,802) | −98942 ≡ 6 | 29aabc1 / c329c118… | 9.30 | ℓ = 59 gave INCONCLUSIVE_ZERO (c₂ = 24360 ≡ 0) | Fable PASS |
| 31 | ord | 311 (17) | 108,129,157,119 (6,445) | 330990 ≡ 3 | f970040 / 92cd0222… | 12.82 | Stage W corpus_ext_6445: 38.0 CPU-h, shared with 47 | Codex Batch C PASS |
| 37 | ord | 149 (2) | 51,086,622,719 (3,045) | 762756 ≡ 1 | 49368cc / 7a174afd… | 5.50 | — | Codex + Pro |
| 41 | ord | 83 (2) | 28,135,391,231 (1,677) | −83420 ≡ 15 | 6c945e8 / e442e6c1… | 3.11 | — | Codex + Pro |
| 43 | ord | 173 (2) | 59,475,230,719 (3,545) | −227412 ≡ 15 | 1a4564d / 80b814ed… | 7.10 | — | Codex Batch C |
| 47 | ord | 283 (3) | 98,213,822,463 (5,854) | 596378 ≡ 42 | 0d4711e / 9fc6b8e8… | 11.51 | — | Codex Batch C |

**Review files:**
- Ota application: `~/BSD_BUILD_MAP/pro6/SINGLETON_AUDIT_REPORT_PRO.md` (SOUND_WITH_CORRECTIONS).
- 17–29: `~/BSD_CERT_17_29_AUDIT_RETURN_FABLE_2026-09-29/RETURN.md`.
- 31, 43, 47: `~/BSD_BATCH_C_AUDIT_CODEX_2026-09-27/REVIEW.md` (225/225 checks).
- 37, 41: `~/BSD_PRO_FOLLOWUP_LEAN_BATCH_C_AUDIT_CODEX_2026-09-27/AUDIT.md`.

**Totals:** Batch C used 69.61 CPU-h and 33 GB of new corpus; the 41 + 37 task used 8.61 CPU-h. **A zero at an auxiliary prime proves nothing.**

