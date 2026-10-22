# P3_FINAL_REPORT: rigorous depth-4 p = 3 run for the seed (2243, 12)

## RETURN: **P3_PROVED_SHA3_ORDER_9**

- **Case A:** a_{4,2} = 15480 ≡ **9 (mod 27)**, and **ord₃(a_{4,2}) = 2**.
- Under F1's audited chain (`P3_CHAIN_PASS_WITH_CORRECTIONS`), this gives **Sha(E/Q)[3^∞] ≅ (Z/3Z)²**, as stated in `SHA3_THEOREM.md`.
- Two published-theorem provenance notes, R1 and R2, are carried and not closed.

**Curve.** E : y² = x³ − 22735x² + 106272484x, with N = 2³·3·2243·4547²·5843, w = +1 and a₃ = −1.

## 1. Result

| quantity | value |
|---|---|
| a_{4,2}, exact, symbols normalised by ω₁ | **15480 = 2³·3²·5·43** |
| a_{4,2} mod 27 | **9**. In the SW / Néron-period normalisation (x_b/2) the value is 7740 ≡ 18 (mod 27); the unit factor 2 leaves the valuation unchanged |
| ord₃ a_{4,2} | **2** |
| forced values | a_{4,0} = 0; a_{4,1} = −54 ≡ 0 (mod 27) |
| lower depths (consistency) | a_{3,·} = (0, 1260, 3186); a_{2,·} = (0, 378, 252); SW Prop 3.5 congruences hold between all depths |
| outcome | **CASE A** |

## 2. Theorem consequence

This follows F1's audited chain; the details are in `SHA3_THEOREM.md`.

1. a_{4,2} ≡ a₂ (mod 27): SW Prop. 3.5 with c = 0, and e_{3,2} = 3.
2. So ord₃ a₂ = 2. In particular a₂ ≠ 0.
3. Skinner 2016 Thm A gives Ch = (L₃). SW Thm 6.1 gives ord_T f_E ≥ 2. Hence ord_T L₃(E,T) = 2 = rank E(Q).
4. Therefore Sha(E/Q)[3^∞] is finite (Thm 6.1 equality).
5. The leading-term formula, with ε₃ = 2, ∏c_v = 16, ord₃ Reg_γ = 0 and #tors = 2, gives #Sha(E/Q)[3^∞] = 9.
6. Cassels–Tate gives **Sha(E/Q)[3^∞] ≅ (Z/3Z)²**.
7. Combined with the merged Sha[2^∞] = 0 and Sha[5^∞] = 0: **#Sha(E/Q)[30^∞] = 9**, matching Sha_an = 9.
   - Provenance: the p = 5 input's numeric node N7 is CERT-NUM from the pre-rigorous LP5 double-precision stream; see `SHA3_THEOREM.md`.

**Not claimed:** Sha(E/Q) finite; full BSD; SRAT; anything at p ∉ {2, 3, 5}.

## 3. How it was obtained

**Pre-launch gate: 8/8 pass** (`prelaunch/PRELAUNCH_GATE.md`).
- The core MANIFEST verified 1718/1718.
- One rebuild; the binaries came out byte-identical to the MANIFEST, and a 24a1 smoke test reproduced 8/8 artifacts.
- The guard refuses the seed without authorization (exit 2, both cases).
- Targets are m = 81 and 27 only.
- LATDEN = 1024; T_min(81) = 14 832 175 873; operational T = 14 847 836 159. Both are identical to P3_RUN_PLAN.
- No stale processes. Resources recorded.

**Launch** 23:07:11 at J = W = 16, through the existing guarded `run_p3.sh` with P3_AUTHORIZED=yes and the default p = 3 targets. No guard was bypassed.

**Stage W** (66.5 min):
- 885/885 segments; **663 685 727 primes** (= PARI `primepi`); 663 685 161 witnesses checked by the independent verifier, 566 by exhaustive count.
- **0 failures.**
- **Aggregate a_q root `5f9994d9…4713f`.**

**Stage A** (15 min):
- m = 81: 54 + 54 symbols; m = 27: 18 + 18 symbols. Each is enclosed in an Arb ball (tail included) and uniquely identified in (1/1024)Z.
- **All 144 values are integers.**
- The a_q roots consumed equal the verifier's.
- The count identities are exact.

**Stage C and audits.** Every mandatory check passed:

| check | where | result |
|---|---|---|
| 1. verifier segment root = arbcore segment root | P3_CHECK, INTEGRITY | PASS (m = 81: 885 segments; m = 27: 288) |
| 2. count identity | P3_CHECK, INTEGRITY | PASS (both targets) |
| 3. every plus/minus symbol uniquely identified | P3_CHECK | PASS (144/144) |
| 4. U₃ relations exact | P3_CHECK (36), DOWNSTREAM (81 → 27 → 9 → 3, [1/3]⁺ = [2/3]⁺ = 0) | PASS |
| 5. parameter / checkpoint integrity | INTEGRITY (PARAMS, unit sets, no .tmp) | PASS |
| 6. no missing segment | INTEGRITY (885 done markers, 885 verifier records, tiling) | PASS |
| 7. all self-hashes valid | INTEGRITY (5 865 units) | PASS |
| forced downstream values and consistency | DOWNSTREAM 20/20; Lane 3 `an2`; `primepi` | PASS |

**Downstream.** Lane 3's audited weight files, weights recomputed from scratch, and Lane 3's own `an2` evaluator (verbatim) all give the same a_{4,j}.

**Replays** (`P3_REPLAY.md`):
- Stage W sample: 32/32 byte-identical.
- Full Stage A re-execution in fresh directories with a different W: both outputs byte-identical.

## 4. Summary numbers

| item | value |
|---|---|
| exact a_{4,2} residue mod 27 | **9** (SW normalisation: 18) |
| ord₃ | **2** |
| theorem consequence | **Sha(E/Q)[3^∞] ≅ (Z/3Z)²; #Sha(E/Q)[30^∞] = 9** |
| CPU time | pipeline ≈ **21.1 CPU-h**: producer 12.81 (exact), verifier ≈ 4.3 (sampled), arbcore 3.93 (exact). Replays and audits ≈ 3.5 CPU-h. **Total ≈ 24.6 CPU-h** |
| wall time | pipeline **81.5 min** (23:07:12 → 00:28:40); including gate, audits, replays and reports ≈ 1 h 55 min |
| peak RAM | **1.35 GB (1.29 GiB)** project total, which is the arbcore msl max RSS. Well under the 12 GB authorization |
| swap | **+0 MB** growth (flat below the pre-launch baseline of 2.47 GB, which came from other apps) |
| disk used | **20 GB** (witnesses 17 GB kept, a_q 2.5 GB); 142 GB still free |
| workers | 16 throughout; governor never triggered; CPU_Speed_Limit ≥ 82 |
| replay status | **PASS** (32/32 Stage W sample; both Stage A outputs byte-identical; three downstream routes agree) |
| manifest status | `P3_MANIFEST.sha256` covers every file of this run directory; verified after writing (see §6) |

## 5. Provenance and caveats (wording discipline)

1. **R1 (F1):** Jones 1989, the multiplicative case of SW Thm 6.1, is unread (paywalled). **R2 (F1):** the Gross-versus-canonical period / freeness bridge behind SU Prop. 12.3.6 at p = 3 with 3 ∥ N and N non-squarefree is literature-internal; Pollack–Weston is unread. The label is F1's recommended one: "PROVED, citing Skinner (2016) Thm A as printed", with R1/R2 recorded. **Not closed tonight, as instructed.** R3–R7 are also listed in `SHA3_THEOREM.md` §4.
2. **R8 is discharged.** The run's floating-point certification was F1's precondition, and it is replaced by Arb enclosures with an independent coefficient verifier.
3. **The lattice is a theorem input.** (1/1024)Z depends on v₂(c₀) ≤ 8 and 4547 ∤ c₀ (merged, not re-audited by F1). The computation cannot detect a stray 4547 denominator (F1 Finding 8).
   - All 144 identified values are integers, so the sharper (1/512)Z lattice is also consistent.
   - A stray extra factor of 2 would have been detected.
4. **p = 5 input** to the 30^∞ corollary: CERT-NUM (floating-point model) in the master certificate. It was not re-run rigorously tonight.
5. **Erratum to the core report** (`~/BSD_RIGOROUS_STREAM_CORE_2026-09-19/00_REPORT.md`, caveat 6; that report is not rewritten). It said binary hashes change on every link because of the Mach-O LC_UUID. **That is wrong:** rebuilding with the same `build.sh` gives byte-identical binaries. The one earlier difference came from a different compile command. The memory note has been corrected.
6. **Scope of the claim.** Nothing is merged. The master ledger is not edited. No prior report is rewritten. No p = 7 or depth-5 run was launched.

## 6. Files

Everything below lives in this directory, `~/BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/`.

- **Reports:**
  - `P3_FINAL_REPORT.md` (this file)
  - `P3_CERTIFICATE.md`
  - `SHA3_THEOREM.md`
  - `P3_REPLAY.md`
  - `P3_RESOURCE_LOG.md`
  - `P3_MANIFEST.sha256`
  - `STATE.json`, `RESUME.md`
- **`prelaunch/`:** gate records, hashes, snapshots, launch command.
- **`run/`:** the pipeline output:
  - `wit/` (885 witness files)
  - `ap/` (885 verified a_q files)
  - `seg/`, `logs/`
  - `units_m81/`, `units_m27/`
  - `msl_m81.txt`, `msl_m27.txt`
  - `SYMBOLS_m81.txt`, `SYMBOLS_m27.txt`
  - `P3_CHECK.txt`, `targets.txt`
- **`downstream/`:**
  - `p3_downstream.py` + `P3_DOWNSTREAM.txt`
  - `p3_integrity.py` + `INTEGRITY.txt`
  - `lane3_an2_eval.gp` + `LANE3_AN2.txt`
  - `PRIMEPI.txt`, `symbol_tables.md`, `a42_folded_sum.txt`
  - `THEOREM_INPUTS_INVENTORY.md`, weight-file hashes
- **`replay/`:** the two replay scripts and their outputs.
- **`logs/`:** resource monitor TSV, governor log, stage W summary, resource summary; `monitor.sh`.
