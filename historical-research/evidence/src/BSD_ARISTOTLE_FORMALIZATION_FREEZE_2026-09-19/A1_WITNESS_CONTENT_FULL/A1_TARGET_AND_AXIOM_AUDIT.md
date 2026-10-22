# A1_TARGET_AND_AXIOM_AUDIT — 20 targets, frozen types, axioms (fresh replay, 2026-09-19)

## 1. Frozen files vs the ORIGINAL package (byte comparison against the original tarball, `eba01658…`)
| file | sha256 | result |
|---|---|---|
| WitnessContent/Defs.lean | `14b61ab04f9b6353738c4fdf8674f80d1a16ef77cde390b4113497b210b5ca3b` | BYTE-IDENTICAL |
| WitnessContent/Spec.lean | `7ff05537d9f6852bf4cdd0e19fbb52800c44035dd6fbc2f4241f2c19217e8f40` | BYTE-IDENTICAL |
| WitnessContent/Acceptance.lean | `88ef61bd3a0915fdf239b02311121adab03b264bbeaaa0019102addd4a2fee70` | BYTE-IDENTICAL |
| lakefile.toml | `126c1c772c7b2a4a602818c96645a5d4dc4e58f5f0639ef300a671163d375d95` | BYTE-IDENTICAL |
| lean-toolchain | `db7bb24b756d745bbde83fe92718b51bd3625dae3701ba0f598d0eedcd3f3028` | BYTE-IDENTICAL |
| scripts/level.py | `e031a002523be22f6b167ecbd459c5dccf50f3b5f4f3939fe5e65ba35a9ef178` | BYTE-IDENTICAL |

Also unchanged: `scripts/acceptance.sh`, `scripts/FROZEN.sha256`, `lake-manifest.json`, the root `WitnessContent.lean`, and every
package document except `STATE.json` / `RESUME.md`.

- Changed: `Targets.lean`, `STATE.json`, `RESUME.md`.
- New: `Countermodels.lean`, `Depth.lean`, `GroupRing.lean`, `Instances.lean`, `Primary.lean`, `Stretch.lean`, `WC.lean`,
  `build.log`, `axioms.log`.
- Full table: `replay/frozen_and_file_comparison.txt`.

## 2. The 20 targets
Legend:
- **exact type**: the declared type is syntactically `WitnessContent.Spec.<Name>` (TypeIntegrity);
- **axioms**: from the fresh probe;
- **proof**: where the proof lives.

| # | level | theorem | exact type | axioms | status | proof |
|---|---|---|---|---|---|---|
| T1 | CORE | lemmaA_comm | ✓ | propext, choice, Quot.sound | CLEAN | GroupRing.nsmul_augIdeal_pow |
| T2 | CORE | gr_killed_by_exponent | ✓ | idem | CLEAN | GroupRing.gr_nsmul_exponent_eq_zero |
| T5 | CORE | depth_spec | ✓ | idem | CLEAN | Depth.depth_spec_aux |
| T5b | CORE | zero_infinitely_divisible | ✓ | propext | CLEAN | Depth.pdvd_zero |
| T6 | CORE | hInf_lt_top_iff | ✓ | idem | CLEAN | Depth.hInf_lt_top_iff_aux |
| T6b | CORE | hInf_le_iff | ✓ | idem | CLEAN | Depth.hInf_le_iff_aux |
| T6c | CORE | JE_bounds | ✓ | idem | CLEAN | Depth.JE_bounds_aux |
| T7 | CORE | **WC_abstract** | ✓ (+ kernel re-check) | idem | CLEAN | WC.WC_abstract_proof |
| T9a | CORE | **CM_uniform_denominator** | ✓ (+ kernel re-check) | idem | CLEAN | Countermodels |
| T9b | CORE | **CM_nonzero_everywhere** | ✓ (+ kernel re-check) | idem | CLEAN | Countermodels |
| T12 | CORE | **WC_abstract_nonvacuous** | ✓ (+ kernel re-check) | idem | CLEAN | Countermodels |
| T3 | FULL | gr_p_primary | ✓ | idem | CLEAN | GroupRing.gr_pow_factorization_smul_eq_zero |
| T4 | FULL | bridge_517 | ✓ | idem | CLEAN | GroupRing.bridge_517_aux |
| T4b | FULL | cls2_zero_iff | ✓ | idem | CLEAN | GroupRing.cls2_eq_zero_iff |
| T8 | FULL | **WC_groupRing** | ✓ (+ kernel re-check) | idem | CLEAN | WC.WC_groupRing_proof |
| T10 | FULL | padicInt_units | ✓ | idem | CLEAN | Instances |
| T11 | FULL | units_exponent | ✓ | idem | CLEAN | Instances |
| S1 | STRETCH | lemmaA_general | ✓ | idem | CLEAN | Stretch |
| S2 | STRETCH | gr_finite_Z | ✓ | idem | CLEAN | Stretch |
| S3 | STRETCH | gr_rational_trivial | ✓ | idem | CLEAN | Stretch |

- **Totals.** 20/20 CLEAN, so LEVEL = **A1_FULL**, FIRST_NOT_CLEAN_TARGET = None, and 3/3 stretch targets are clean.
- **Remaining `sorry`:** 0 (the fresh build has no `sorry` warning).
- **Axioms.** The fresh axiom set over all targets is ⊆ {propext, Classical.choice, Quot.sound}, with no `sorryAx`, no user
  axiom, and no `Lean.ofReduceBool`/`native_decide`.

## 3. The five sensitive targets, read against the frozen statements
- **WC_abstract.** The proof is `WC.WC_abstract_proof`. It `intro`s exactly the frozen binders and hypotheses, in this order:
  - `hexp`: bounded exponent;
  - `htors`: Sha torsion;
  - `hselmer`;
  - `hota517`: the witness form;
  - `hota15`;
  - `A hA hAJ`.
  It proves the three conclusions and discharges none of the hypotheses.
- **WC_groupRing.** The proof applies `WC_abstract_proof` to `M := gr (Rp p) (G p S) 2` and `t := cls2 ∘ θ`, and supplies two
  of its hypotheses:
  - the bounded exponent, from T3;
  - the 5.17 witness form, from T4 with `p ≥ 3` derived from `2 ∈ S0`.
  Every other hypothesis is passed through unchanged. The arithmetic boundary is still `A ≠ 0 ∧ A ∈ J_E` plus explicit
  Ota / Selmer / Sha hypotheses.
- **CM_uniform_denominator.** It computes `depth p (p²) = 2` in `ZMod(p³)` and `hInf = 2` at every prime, then shows `J = {0}`
  using a prime not dividing a given `a ≠ 0` (Euclid).
- **CM_nonzero_everywhere.** It instantiates the refuted shortcut with the T9a system (finite, bounded exponent, nonzero at every
  prime) and derives a contradiction from `J = {0}`.
- **WC_abstract_nonvacuous.** The witness is `S0 = ∅`, Sha = PUnit, M p _ = ZMod p, t = 1, r = 2. All seven conjuncts are
  proved, including `1 ∈ J_E`, so the T7 hypotheses are satisfiable (non-contradictory).

## 4. Result
**No target-integrity defect.** Every theorem proves exactly its frozen proposition, and no wrapper changes a meaning: the
types are literally the frozen constants.
