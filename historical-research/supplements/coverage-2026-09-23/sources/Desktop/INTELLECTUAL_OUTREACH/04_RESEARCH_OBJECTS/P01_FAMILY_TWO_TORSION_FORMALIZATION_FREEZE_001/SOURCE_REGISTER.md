# Source register

## The single shared input

| copy | sha256 |
|---|---|
| as built | `fe8450464d877433888a34ef9403617f8e5feb1594d7be46090802de08d489e2` |
| frozen here | `fe8450464d877433888a34ef9403617f8e5feb1594d7be46090802de08d489e2` |
| returned by Run A | `fe8450464d877433888a34ef9403617f8e5feb1594d7be46090802de08d489e2` |
| returned by Run B | `fe8450464d877433888a34ef9403617f8e5feb1594d7be46090802de08d489e2` |

All four agree. Both runs consumed byte-identical input.

## Carried trees — byte-identical to their sources

| directory | files | failures |
|---|---|---|
| `00_v1_handoff/` | 24 | 0 |
| `01_run_A/tree/` | 27 | 0 |
| `02_run_B/tree/` | 27 | 0 |

## The changed file in each run

| run | `P01/TwoTorsion.lean` sha256 | lines | declarations |
|---|---|---|---|
| handoff | `20b8210ac36168a7ecb3dfb75e083796a8a70e80373509263dfd4ca8ae77bd42` | 193 | 26 |
| A | `1d2941e00a8b2a32c01fde83d053e210fd5214ba50154f4c532bd3eba53b39e8` | 346 | 42 |
| B | `98db822a09bbb260d40085778d6b7748dae0faddc0129755df724ba5ec0678de` | 329 | 31 |

## The seven certified inputs — untouched by both runs

| file | sha256 |
|---|---|
| `RequestProject/Run013/Basic.lean` | `4f085a8c7f3cb0621af4341a87a8aed26bde2cee5f0d9148a58a4c3332115947` |
| `RequestProject/Run013/Selmer.lean` | `4dda4069454b2dd02a7c1a821d0a7e7cf7ecae775147f6e38f9e877f57fa3a0b` |
| `RequestProject/SDyadic/Family.lean` | `a866211d79a65fdf030e53f0ed9519ecf86bbc80c1fca2c778d3ba8f2499f2c3` |
| `RequestProject/Descent/Delta.lean` | `b1d5625d1a7c8651777c4ab4f149deda26b4ba2cb01dced12ccf839492af17f7` |
| `RequestProject/Descent/Ported.lean` | `938750075fbfa5ea71df6bd8d1063d1a9ec27b6b93005061cb741ee7b50c91ef` |
| `RequestProject/P01/Instances.lean` | `157d05af9edec15260fd0156540a3317204edf98cb0d6c28eae44ac295822b92` |
| `RequestProject/Main.lean` | `eb09cc346e30c595ed174824f428b725ad27d908f6df6d710651620e21e6f338` |

`Descent/Delta.lean` is **Delta Run B**, and `Run013/Basic.lean` / `Selmer.lean` are the
audited 62a1 development. `P01/Instances.lean` carries the non-vacuity witnesses from
certified saturation Run B. None of them was modified by either P01 run.

## Archives

| file | sha256 | bytes |
|---|---|---|
| `_external/originals/ARISTOTLE_P01_FAMILY_TWO_TORSION_V1.tar.gz` | `fe8450464d877433888a34ef9403617f8e5feb1594d7be46090802de08d489e2` | 35554 |
| `_external/originals/RUN_A_8a3881a9-aristotle.tar.gz` | `9ae502039110c32cce48c801d7f792136bb01c6d3ae0cceb984130d25afa53b4` | 73707 |
| `_external/originals/RUN_B_b67dbb4e-aristotle.tar.gz` | `1964ac96e8d24678e7d34f9a9a5d1801f7b46f82fac03f68c73564927b91de52` | 73676 |

## Files written by this object

| file | role |
|---|---|
| `README.md`, `STATUS.md` | what this is; tiers; the independence caveat |
| `AB_ARCHITECTURE_COMPARISON.md` | §1 the supplied route; then how the two differ |
| `REUSABLE_LEMMA_CROSSWALK.md` | every added lemma classified for P03 reuse |
| `CONTINUATION_BASE_ASSESSMENT.md` | Run A + 2 ported lemmas, and why this flips Delta's call |
| `SOURCE_REGISTER.md`, `ERRATA.md` | this file; E1–E4 |
| `0N_run_*/STALE_METADATA_NOTICE.md` | warning beside each returned tree |
| `receipts/RUN_{A,B}_*` | custody, rebuild, axioms, constructs, stale metadata |
| `receipts/TARGET_STATEMENT_COMPARISON.txt` | 26 declarations, 78 pairwise diffs |
| `receipts/CROSS_RUN_SEMANTIC_CHECK.txt` | one probe, both developments |
| `receipts/semantic_probe.lean` | that probe, replayable, contains no `sorry` |

## Manifest coverage

The root manifest excludes only itself. All three nested manifests are covered:

    00_v1_handoff/MANIFEST.sha256    379d32f559df363c…
    01_run_A/tree/MANIFEST.sha256    379d32f559df363c…
    02_run_B/tree/MANIFEST.sha256    379d32f559df363c…

All three are equal — which is the evidence for `ERRATA.md` E2.

## Read-only sources touched

| path | access |
|---|---|
| `~/Downloads/8a3881a9-…`, `~/Downloads/b67dbb4e-…` | read; copied, never moved |
| `ARISTOTLE_P01_FAMILY_TWO_TORSION_V1` | read; **not modified** |
| `~/k33-successor-base-v6-2026-08-29/.lake/packages` | cloned copy-on-write into scratch build trees |

No source object was modified.
