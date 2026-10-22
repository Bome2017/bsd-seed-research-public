# Source register

## The single shared input

| copy | sha256 |
|---|---|
| as built | `632f8f93eb02dfe34a1a6885ed9f36a6b3f4a9d7f26785de73e8fce6fe3fde23` |
| returned by Run A | `632f8f93eb02dfe34a1a6885ed9f36a6b3f4a9d7f26785de73e8fce6fe3fde23` |
| returned by Run B | `632f8f93eb02dfe34a1a6885ed9f36a6b3f4a9d7f26785de73e8fce6fe3fde23` |

## Carried trees

| directory | files | failures |
|---|---|---|
| `00_v1_handoff/` | 29 | 0 |
| `01_run_A/tree/` | 31 | 0 |
| `02_run_B/tree/` | 31 | 0 |

## The changed file

| | sha256 | lines | declarations |
|---|---|---|---|
| handoff | `479397064afd98ea11059e39b1550b498e5ad9e53905dc2f726e621417aed48a` | 72 | 1 |
| Run A | `444b1c02e2b495a49505dd0057e3e30b0c4e3ee4d0d41db50920ebc98504448e` | 532 | 13 |
| Run B | `68d2dfcc0dcbb9d43f5e0e6e73ea683b38c6f4958e404a5fb3f2135e54206116` | 610 | 18 |

## The ten inherited Lean sources — untouched by both runs

| file | sha256 | provenance |
|---|---|---|
| `Run013/Basic.lean` | `4f085a8c7f3cb0621af4341a87a8aed26bde2cee5f0d9148a58a4c3332115947` | audited 62a1 |
| `Run013/Selmer.lean` | `4dda4069454b2dd02a7c1a821d0a7e7cf7ecae775147f6e38f9e877f57fa3a0b` | audited 62a1 |
| `SDyadic/Family.lean` | `a866211d79a65fdf030e53f0ed9519ecf86bbc80c1fca2c778d3ba8f2499f2c3` | frozen family |
| `Descent/Delta.lean` | `b1d5625d1a7c8651777c4ab4f149deda26b4ba2cb01dced12ccf839492af17f7` | Delta Run B |
| `Descent/Ported.lean` | `938750075fbfa5ea71df6bd8d1063d1a9ec27b6b93005061cb741ee7b50c91ef` | 3 Delta Run A lemmas |
| `P01/TwoTorsion.lean` | `1d2941e00a8b2a32c01fde83d053e210fd5214ba50154f4c532bd3eba53b39e8` | P01 Run A |
| `P01/PortedRunB.lean` | `37e80ea675ccbe353f4e23f9ba8a529bf34ff3f28e4c5332cd7db1369d460f21` | 2 P01 Run B lemmas |
| `P01/Instances.lean` | `157d05af9edec15260fd0156540a3317204edf98cb0d6c28eae44ac295822b92` | saturation Run B witnesses |
| `P03a/PointMaps.lean` | `bd3fe49394d08e46d6cf6205760648fc50d5ef4fb23942c641381286d4a66b03` | **P03a Run B** |
| `Main.lean` | `01fdd181e862049ce6f713077eff359703ff9daddf41edbe4652fce1eb97f0e2` | project root |

## Archives

| file | sha256 | bytes |
|---|---|---|
| `_external/originals/ARISTOTLE_P03B_ISOGENY_ADDITIVITY_V1.tar.gz` | `632f8f93eb02dfe34a1a6885ed9f36a6b3f4a9d7f26785de73e8fce6fe3fde23` | 43154 |
| `_external/originals/RUN_A_8a3aac10-aristotle.tar.gz` | `f7bc1ad39a59a84e29534fad8eb1f73e650be54395e7e3e84b15778369893975` | 93090 |
| `_external/originals/RUN_B_b1563310-aristotle.tar.gz` | `9cc82611a9373f495fb1f46a2f5a8ed2a12cc1dd759b79e034897aeb2c69ce8b` | 93024 |

## Files written by this object

| file | role |
|---|---|
| `README.md`, `STATUS.md` | what this is; tiers; the boundary |
| `AB_ARCHITECTURE_COMPARISON.md` | zero shared names; the convergent scaled-map finding |
| `CONTINUATION_BASE_ASSESSMENT.md` | Run B weakly; why the choice matters less here |
| `SOURCE_REGISTER.md`, `ERRATA.md` | this file; E1–E4 |
| `0N_run_*/STALE_METADATA_NOTICE.md` | a notice per run |
| `receipts/RUN_{A,B}_INDEPENDENT_VERIFICATION.txt` | custody, rebuild, constructs, boundary, axioms |
| `receipts/TARGET_STATEMENT_COMPARISON.txt` | the target diffed three ways; source-counted declarations |
| `receipts/CROSS_RUN_SEMANTIC_CHECK.txt` | one probe, both developments, law instantiated |
| `receipts/semantic_probe.lean` | that probe, replayable, no `sorry` |

## Manifest coverage

The root manifest excludes only itself; all three nested manifests are covered:

    00_v1_handoff/MANIFEST.sha256    c797996c6d017cfc…
    01_run_A/tree/MANIFEST.sha256    c797996c6d017cfc…
    02_run_B/tree/MANIFEST.sha256    c797996c6d017cfc…

All three equal — the evidence for `ERRATA.md` E2.

## Read-only sources touched

| path | access |
|---|---|
| `~/Downloads/8a3aac10-…`, `~/Downloads/b1563310-…` | read; copied, never moved |
| `ARISTOTLE_P03B_ISOGENY_ADDITIVITY_V1` | read; **not modified** |
| `~/k33-successor-base-v6-2026-08-29/.lake/packages` | cloned copy-on-write into scratch build trees |

No source object was modified.
