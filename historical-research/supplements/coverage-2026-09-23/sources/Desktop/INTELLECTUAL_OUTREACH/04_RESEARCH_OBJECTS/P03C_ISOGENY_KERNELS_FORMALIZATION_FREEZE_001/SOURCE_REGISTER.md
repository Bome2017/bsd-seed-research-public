# Source register

## The single shared input

| copy | sha256 |
|---|---|
| as built | `bbd2f1f7a3f9e3d885b3fcfb14d34f9197bea1a5c4f7c6d240b6f7b7635919db` |
| returned by Run A | `bbd2f1f7a3f9e3d885b3fcfb14d34f9197bea1a5c4f7c6d240b6f7b7635919db` |
| returned by Run B | `bbd2f1f7a3f9e3d885b3fcfb14d34f9197bea1a5c4f7c6d240b6f7b7635919db` |

## Carried trees

| directory | files | failures |
|---|---|---|
| `00_v1_handoff/` | 30 | 0 |
| `01_run_A/tree/` | 32 | 0 |
| `02_run_B/tree/` | 32 | 0 |

## The changed file

| | sha256 | lines | declarations |
|---|---|---|---|
| handoff | `22e5bb5dab0ed337cb3403e0b3fc1a39b8f9a92b228b5ab60ef0c01c1fbb7e59` | 79 | 5 |
| Run A | `614062fbae6fe59c6181cb60fd9ff08f8ef65b35a1a92d3bb781af29569735fc` | 115 | 5 |
| Run B | `1f43cea283c93a3f19f09afbc432027a499c86eecd190b28446e2d73a477b53c` | 115 | 5 |

Same declaration count in all three: the runs added **no** auxiliary lemmas.

## The eleven inherited Lean sources — untouched by both runs

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
| `P03a/PointMaps.lean` | `bd3fe49394d08e46d6cf6205760648fc50d5ef4fb23942c641381286d4a66b03` | P03a Run B |
| `P03b/Additivity.lean` | `68d2dfcc0dcbb9d43f5e0e6e73ea683b38c6f4958e404a5fb3f2135e54206116` | P03b Run B |
| `Main.lean` | `73e004e4ceb388d8f962d03611506990fc5a83a4da149c7f3a9bec072d8191de` | project root |

## Archives

| file | sha256 | bytes |
|---|---|---|
| `_external/originals/ARISTOTLE_P03C_ISOGENY_KERNELS_V1.tar.gz` | `bbd2f1f7a3f9e3d885b3fcfb14d34f9197bea1a5c4f7c6d240b6f7b7635919db` | 48824 |
| `_external/originals/RUN_A_31dcd199-aristotle.tar.gz` | `657ba1b3f228fb85cf735f38ec91f824c9f36abd7fcd633f0feee76efe69c430` | 98134 |
| `_external/originals/RUN_B_f292098b-aristotle.tar.gz` | `de9976bbc9219635d44e1fd6ab3ed29c0016b309dfc520075d13c25de8a7ba48` | 99018 |

## Files written by this object

| file | role |
|---|---|
| `README.md`, `STATUS.md` | what this is; the confirmation-grade caveat |
| `receipts/PROOF_DIVERGENCE_MEASUREMENT.txt` | the two-line measurement, and the calibration table |
| `receipts/RUN_{A,B}_INDEPENDENT_VERIFICATION.txt` | custody, rebuild, constructs, boundary, axioms |
| `receipts/CROSS_RUN_SEMANTIC_CHECK.txt` | one probe, both runs, incl. the non-triviality check |
| `receipts/semantic_probe.lean` | that probe, replayable, no `sorry` |
| `SOURCE_REGISTER.md`, `ERRATA.md` | this file; E1–E4 |
| `0N_run_*/STALE_METADATA_NOTICE.md` | a notice per run |

## Manifest coverage

    00_v1_handoff/MANIFEST.sha256    0b0460ef7686ba2a…
    01_run_A/tree/MANIFEST.sha256    0b0460ef7686ba2a…
    02_run_B/tree/MANIFEST.sha256    0b0460ef7686ba2a…

All three equal — the evidence for `ERRATA.md` E2.

No source object was modified.
