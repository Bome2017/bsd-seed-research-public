# Source register

## The single shared input

| copy | sha256 |
|---|---|
| as built | `565d36342a8d4ccd17ecd05278252ddeea4a0d30846aa0763c80df795500ebba` |
| frozen here | `565d36342a8d4ccd17ecd05278252ddeea4a0d30846aa0763c80df795500ebba` |
| returned by Run A | `565d36342a8d4ccd17ecd05278252ddeea4a0d30846aa0763c80df795500ebba` |
| returned by Run B | `565d36342a8d4ccd17ecd05278252ddeea4a0d30846aa0763c80df795500ebba` |

All four agree. Both runs consumed byte-identical input.

## Carried trees

| directory | files | failures |
|---|---|---|
| `00_v1_handoff/` | 28 | 0 |
| `01_run_A/tree/` | 17 | 0 | (partial wrapper — see `ERRATA.md` E2) |
| `02_run_B/tree/` | 30 | 0 |

## The changed file

| | `P03a/PointMaps.lean` sha256 | lines | declarations |
|---|---|---|---|
| handoff | `e00f5a9626c69c3f0508b3c6cd2f17fa4d1cb65d8111aeb30f72ca99be320335` | 139 | 15 |
| Run A | `ebf31c30dae267805a64d4c27a61fd134495c32d3321387ffed3636a8717dfb1` | 212 | 21 |
| Run B | `bd3fe49394d08e46d6cf6205760648fc50d5ef4fb23942c641381286d4a66b03` | 216 | 22 |

## The nine inherited Lean sources — untouched by both runs

| file | sha256 | provenance |
|---|---|---|
| `Run013/Basic.lean` | `4f085a8c7f3cb0621af4341a87a8aed26bde2cee5f0d9148a58a4c3332115947` | audited 62a1 |
| `Run013/Selmer.lean` | `4dda4069454b2dd02a7c1a821d0a7e7cf7ecae775147f6e38f9e877f57fa3a0b` | audited 62a1 |
| `SDyadic/Family.lean` | `a866211d79a65fdf030e53f0ed9519ecf86bbc80c1fca2c778d3ba8f2499f2c3` | frozen family |
| `Descent/Delta.lean` | `b1d5625d1a7c8651777c4ab4f149deda26b4ba2cb01dced12ccf839492af17f7` | Delta Run B |
| `Descent/Ported.lean` | `938750075fbfa5ea71df6bd8d1063d1a9ec27b6b93005061cb741ee7b50c91ef` | 3 Delta Run A lemmas, rebased |
| `P01/TwoTorsion.lean` | `1d2941e00a8b2a32c01fde83d053e210fd5214ba50154f4c532bd3eba53b39e8` | P01 Run A |
| `P01/PortedRunB.lean` | `37e80ea675ccbe353f4e23f9ba8a529bf34ff3f28e4c5332cd7db1369d460f21` | 2 P01 Run B lemmas |
| `P01/Instances.lean` | `157d05af9edec15260fd0156540a3317204edf98cb0d6c28eae44ac295822b92` | Params witnesses, saturation Run B |
| `Main.lean` | `d65dec19487dd87f39f349cb28d6353b445f42f1735d5ae852ab8f41008631cf` | project root |

## Archives

| file | sha256 | bytes |
|---|---|---|
| `_external/originals/ARISTOTLE_P03A_ACTUAL_ISOGENY_POINT_MAPS_V1.tar.gz` | `565d36342a8d4ccd17ecd05278252ddeea4a0d30846aa0763c80df795500ebba` | 42530 |
| `_external/originals/RUN_A_d6494af0-aristotle.tar.gz` | `7fc203b5e295a0efe092c443011b437ae070ed5163a5dd2648d669f188c35fa5` | 66157 |
| `_external/originals/RUN_B_e9e4787d-aristotle.tar.gz` | `21c3035b778fe1e444dd792dab3d57ab696c44fff847b78058b416277ff3d427` | 86820 |

## Files written by this object

| file | role |
|---|---|
| `README.md`, `STATUS.md` | what this is; tiers; the boundary |
| `AB_ARCHITECTURE_COMPARISON.md` | the supplied route; `isogeny_core` vs the two cubic identities |
| `REUSABLE_LEMMA_CROSSWALK.md` | every added lemma, and what P03b will want |
| `CONTINUATION_BASE_ASSESSMENT.md` | Run B, nothing to port |
| `SOURCE_REGISTER.md`, `ERRATA.md` | this file; E1–E4 |
| `0N_run_*/STALE_METADATA_NOTICE.md` | a notice per run — the two defects differ |
| `receipts/RUN_{A,B}_*` | custody, rebuild, axioms, constructs |
| `receipts/TARGET_STATEMENT_COMPARISON.txt` | 15 declarations, 45 pairwise diffs, source-counted declarations |
| `receipts/CROSS_RUN_SEMANTIC_CHECK.txt` | one probe, both developments, maps evaluated |
| `receipts/semantic_probe.lean` | that probe, replayable, no `sorry` |

## Manifest coverage

The root manifest excludes only itself. Both nested manifests are covered:

    00_v1_handoff/MANIFEST.sha256    a176b197b8dc1c86…
    02_run_B/tree/MANIFEST.sha256    a176b197b8dc1c86…

They are equal — the evidence for `ERRATA.md` E2. Run A returned no manifest, which is
the other half of that entry.

## Read-only sources touched

| path | access |
|---|---|
| `~/Downloads/d6494af0-…`, `~/Downloads/e9e4787d-…` | read; copied, never moved |
| `ARISTOTLE_P03A_ACTUAL_ISOGENY_POINT_MAPS_V1` | read; **not modified** |
| `~/k33-successor-base-v6-2026-08-29/.lake/packages` | cloned copy-on-write into scratch build trees |

No source object was modified.
