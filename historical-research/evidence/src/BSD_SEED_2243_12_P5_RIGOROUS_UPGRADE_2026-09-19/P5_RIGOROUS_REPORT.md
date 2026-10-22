# P5_RIGOROUS_REPORT: proof-grade upgrade of the seed's p = 5 numerical node (N7)

## RETURN: **P5_RIGOROUS_SHA5_ZERO_CONFIRMED**

- The rigorous Arb pipeline with independently verified coefficients reproduces all 20 symbols [b/25]⁺ exactly, and they **agree with the historical LP5 values**.
- Two independent evaluations give a₂ ≡ 2 (mod 5) in the ω₁ normalisation (1 in the Néron normalisation), so **ord₅(a₂) = 0**.
- With the unchanged, already-audited Kato / Stein–Wuthrich chain this gives **Sha(E/Q)[5^∞] = 0**, now with node N7 at proof grade (`SHA5_RIGOROUS_THEOREM.md`).
- The frozen master certificate and the LP5 / SW-gate directories are unchanged. Nothing is merged.

**Curve.** E : y² = x³ − 22735x² + 106272484x, with N = 2³·3·2243·4547²·5843, w = +1 and a₅ = −2.

## 1. Result

| quantity | value |
|---|---|
| [b/25]⁺ (b = 1..24, 5 ∤ b), exact | −54, 16, 90, −52, −76, 16, 76, −52, −54, 90, 90, −54, −52, 76, 16, −76, −52, 90, 16, −54 |
| six-symbol value (audited N6 formula) | 3(16 + 90 − 52 − 54) + 4(−52 + 90) = **152 ≡ 2 (mod 5)** |
| independent exact evaluator | a_{2,0} = 0 exactly; a_{2,1} ≡ 0 (mod 5); **a_{2,2} ≡ 2 (mod 5)** (α ≡ 13 mod 25; the α⁻³[b/5]⁺ term included and ≡ 0 mod 5) |
| SW normalisation | Néron period with λ_f: a_{2,2} ≡ 1 (mod 5). With the curve's parametrisation (factor c_E/2, c_E = 2^k ∣ 512): residue in {1, 2, 3, 4}, never 0 |
| **ord₅(a₂)** | **0** |
| historical LP5 (consistency only) | 20/20 symbols identical; 152 = 152: **no disagreement** |

## 2. How it was obtained

**Pre-launch gate: 7/7 pass** (`prelaunch/PRELAUNCH_GATE.md`).
- The core MANIFEST verified 1718/1718.
- The rebuilt binaries are byte-identical to the MANIFEST.
- 11/11 stored validation artifacts were reproduced: 389a1 msl and ms at m = 25; 37a1 msl at m = 25 with s = −1; 446d1 msl at m = 5; the 24a1 pipeline.
- No stale processes.
- **T_min(m = 25, LATDEN 1024) = 7 825 119 335 recomputed** (T_min − 1 fails), which is the recorded value. Operational T = 7 834 959 871 = 467·2²⁴ − 1. For m = 5: T_min 1 511 545 536, T = 1 526 726 655.
- Lattice: (1/1024)Z ⊇ (1/(2c_E))Z ⊇ (1/c_E)Z with c_E ∣ 512, as the audited gate authorizes.
- Resources recorded.

**Launch** 06:28:48 at J = W = 16, through the existing `run_p3.sh` with TARGETS="25:1:1 5:1:1", LATDEN = 1024. The guard variable P3_AUTHORIZED=yes was set under the operator's p = 5 authorization; no guard code was modified.

**Stage W** (32.6 min):
- 467/467 segments; **360 542 141 primes** (= PARI `primepi`); 360 541 575 witnesses verified independently, 566 by exhaustive count.
- **0 failures.**
- Aggregate a_q root `fcd024375b54642344d03502caf0c53882190973ab2683239011f813ca2848d4`.
- **Byte-identical to the independent p = 3 run's coefficient files for all 467 segments.**

**Stage A** (7.1 min): m = 25 gives 20 + 20 symbols, and m = 5 gives 4 + 4. Each is in an Arb ball (tail included) and uniquely identified in (1/1024)Z. **All 48 values are integers.**

**Checks — every mandatory check passed:**

| check | where | result |
|---|---|---|
| coefficient roots (verifier = engine) | P3_CHECK, INTEGRITY | PASS (m = 25: 467 segments; m = 5: 91) |
| count identities | P3_CHECK, INTEGRITY | PASS |
| lattice uniqueness (plus and minus) | P3_CHECK | PASS (48/48) |
| Hecke consistency: T₅ between the independent m = 25 and m = 5 runs, both signs; Σ[c/5]⁺ = 0 | P3_CHECK (8), P5_DOWNSTREAM | PASS |
| checkpoint / self-hash integrity; PARAMS; no missing segment | INTEGRITY (2 790 unit self-hashes) | PASS |
| forced values a_{2,0} = 0, a_{2,1} ≡ 0 (mod 5); route A = route B | P5_DOWNSTREAM 21/21 | PASS |

**Replays** (`P5_REPLAY.md`):
- the cross-run comparison: 467/467 byte-identical;
- the Stage W sample: 32/32 byte-identical;
- the full Stage A re-execution at a different thread count in fresh directories: both outputs byte-identical.

## 3. Summary numbers

| item | value |
|---|---|
| exact identified symbols | the 20 + 20 [b/25]^± and 4 + 4 [c/5]^± of `P5_CERTIFICATE.md` §3 |
| coefficient residue | a_{2,2} ≡ 2 (mod 5) in ω₁ normalisation (≡ 1 Néron) |
| ord₅(a₂) | **0** |
| theorem | **Sha(E/Q)[5^∞] = 0**, node N7 now proof-grade |
| CPU time | pipeline ≈ **10.1 CPU-h**: producer 6.22 (exact), verifier ≈ 2.07 (sampled), arbcore 1.83 (exact). Replays and audits ≈ 1.8 CPU-h |
| wall time | pipeline **39.7 min** (06:28:48 → 07:08:29); gate to final report ≈ 1 h 15 min |
| peak RAM | **1.42 GB** (arbcore m = 25) |
| swap | **+0 MB** |
| disk used | **11 GB** (witnesses 9.4 GB kept, a_q 1.4 GB) |
| replay status | **PASS** |
| manifest status | `P5_MANIFEST.sha256` (every file of this directory), verified after writing |

## 4. Scope and caveats (wording discipline)

1. **What changed.**
   - N7's evidence moved from CERT-NUM (LP5 double stream, with BBR/Deligne tail and floating-point model) to proof-grade computer-assisted: Arb enclosures with the elementary Hasse/divisor tail, a_q proved by the independent verifier, and the trust base listed in `P5_CERTIFICATE.md` §6.
   - **Every other node and label of the master certificate is unchanged.** N8's 2-part stays DER and N1 stays a preprint plus replay; see `SHA5_RIGOROUS_THEOREM.md` §3.
2. **The lattice is a theorem input.** (1/1024)Z needs c_E ∣ 512 (N8). The run does not prove it. All values are integers, which is consistent with the sharper lattice.
3. **Normalisation.** The residue depends on the normalisation: 2 for ω₁, 1 for Néron, and 1–4 with an unknown c_E. The **valuation does not**, because 5 ∤ c_E. The audited chain uses only ord₅(a₂) = 0.
4. **Successor, not an edit.** The master certificate (`~/SEED_2243_12_MASTER_CERTIFICATE_2026-09-18/`), the SW gate, LP5 and the ledger are unchanged. This directory is a successor record for the operator to merge or link.
5. **Related (not part of this certificate).**
   - The p = 3 corollary #Sha[30^∞] = 9 (`SHA3_THEOREM.md`) no longer carries the CERT-NUM qualifier for its p = 5 input; that file is not edited.
   - The master certificate's non-claim "analytic rank exactly 2 is not certified" is superseded by the core's `ANALYTIC_RANK_CERTIFICATE.md`.
6. **Optional R2 reading.** It was done during the Stage W wait, as source reading only. The result is `~/BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/addenda/P3_R2_PERIOD_PROVENANCE_AUDIT.md` (hash in `addenda/ADDENDA_MANIFEST.sha256`).
   - **R2 remains OPEN, now sharpened.** Kim–Ota 2023 removes PW's squarefree-N restriction but needs p ≥ 5 and (N, p) = 1. Pollack–Weston 2011 §6, Chida–Hsieh Prop. 6.1 and Skinner–Zhang also need p ≥ 5 and/or p ∤ N. So the residual gap is exactly "p = 3 ∣ N".
   - It has no bearing on the p = 5 certificate.
7. **Not done:** no p = 7, no depth > 2, and nothing merged.

## 5. Files

Everything below lives in this directory, `~/BSD_SEED_2243_12_P5_RIGOROUS_UPGRADE_2026-09-19/`.

- **Reports:**
  - `P5_RIGOROUS_REPORT.md` (this file)
  - `P5_CERTIFICATE.md`
  - `SHA5_RIGOROUS_THEOREM.md`
  - `P5_REPLAY.md`
  - `P5_RESOURCE_LOG.md`
  - `P5_MANIFEST.sha256`
  - `STATE.json`, `RESUME.md`
- **`prelaunch/`:** the gate record, hashes, reproduction checks, tmin output, launch command.
- **`run/`:** the pipeline output:
  - `wit/`, `ap/` (467 each)
  - `seg/`, `logs/`
  - `units_m25/`, `units_m5/`
  - `msl_m25.txt`, `msl_m5.txt`
  - `SYMBOLS_m25.txt`, `SYMBOLS_m5.txt`
  - `P3_CHECK.txt`, `targets.txt`
- **`downstream/`:**
  - `p5_downstream.py` + `P5_DOWNSTREAM.txt`
  - `p5_integrity.py` + `INTEGRITY.txt`
  - `cross_run_p3.py` + `CROSS_RUN_P3.txt`
  - `PRIMEPI.txt`
- **`replay/`:** the two replay scripts and their outputs.
- **`logs/`:** monitor TSV, governor log, stage W summary, resource summary; `monitor.sh`.
