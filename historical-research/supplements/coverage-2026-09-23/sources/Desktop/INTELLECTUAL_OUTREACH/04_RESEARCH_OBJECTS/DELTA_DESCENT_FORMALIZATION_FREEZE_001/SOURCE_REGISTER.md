# Source register

## The handoff — carried forward byte-identically

Handoff archive: `b75ba34edce636035eb2d4c22b998d70ab51298434ffb0ae8558ab58c25052d3`
Handoff root manifest: `e02195eb7edaefafa01062fa4315f94059b5e55932e07f113c7ce88fee5222e8` (20 entries).

All 21 files under `00_v1_handoff/` were compared file-by-file against
`ARISTOTLE_DELTA_DESCENT_V1` as built: **21/21 byte-identical, 0 failures**.

## The return — carried forward byte-identically

All 24 files under `01_run_A/tree/` were compared against the extracted wrapper:
**24/24 byte-identical, 0 failures**. Nothing was edited, regenerated, or removed,
including the stale manifest and stale receipts (see `ERRATA.md` E2).

| file | sha256 | bytes |
|---|---|---|
| `01_run_A/tree/RequestProject/Descent/Delta.lean` | `ed971bde2b0e956a6d6efe4fe787ec4192dffc058d65f4c869466cc81afe8164` | 17072 |
| `01_run_A/tree/RequestProject/Run013/Basic.lean` | `4f085a8c7f3cb0621af4341a87a8aed26bde2cee5f0d9148a58a4c3332115947` | 5857 |
| `01_run_A/tree/RequestProject/Run013/Selmer.lean` | `4dda4069454b2dd02a7c1a821d0a7e7cf7ecae775147f6e38f9e877f57fa3a0b` | 6624 |
| `01_run_A/tree/RequestProject/Main.lean` | `2614ee24de7d0bf66a836e8d1c1818f06c172db94501ae387ec5d6cc92077218` | 142 |
| `01_run_A/tree/ARISTOTLE_SUMMARY.md` | `01a7fefbe4fb985896665f9d5083b710927caaa449ce892647ba6ecaa78f484b` | 3801 |
| `01_run_A/tree/MANIFEST.sha256` | `e02195eb7edaefafa01062fa4315f94059b5e55932e07f113c7ce88fee5222e8` | 1847 |

The two Run013 digests are the audited 62a1 development's:
`4f085a8c…115947` and `4dda4069…7fa3a0b`. They came back unchanged.

## Archives

| file | sha256 | bytes |
|---|---|---|
| `_external/originals/ARISTOTLE_DELTA_DESCENT_V1.tar.gz` | `b75ba34edce636035eb2d4c22b998d70ab51298434ffb0ae8558ab58c25052d3` | 45091 |
| `_external/originals/RUN_A_1738ee80-aristotle.tar.gz` | `87240251498c633bf16ce513d7984d587c03b7cf8f3faeab9322731e746f6232` | 95806 |

## Files written by this object

| file | role |
|---|---|
| `README.md` | what this object is; what will fail on replay and why |
| `STATUS.md` | certification tier and boundary |
| `PROOF_ARCHITECTURE.md` | the Vieta route; why `δ((0,0)) = [b]` |
| `SOURCE_REGISTER.md` | this file |
| `ERRATA.md` | E1 carried forward; E2 the packaging defect; E3 cross-reference |
| `01_run_A/STALE_METADATA_NOTICE.md` | warning beside the returned tree |
| `receipts/CUSTODY.txt` | input identity; what changed |
| `receipts/INDEPENDENT_REBUILD.txt` | 8030 jobs, no sorry warning |
| `receipts/INDEPENDENT_AXIOM_AUDIT.txt` | 15 objects |
| `receipts/INDEPENDENT_CONSTRUCT_SCAN.txt` | build source vs non-build files |
| `receipts/STATEMENT_PRESERVATION.txt` | statement, map, curve, declaration diff, route |
| `receipts/SEMANTIC_VERIFICATION.txt` | non-vacuity on a concrete curve |
| `receipts/semantic_probe.lean` | that probe, replayable, contains no `sorry` |
| `receipts/STALE_INPUT_METADATA.txt` | the defect, reproduced |

## Manifest coverage

The root `MANIFEST.sha256` excludes only itself. Both nested manifests are covered as
ordinary entries — deliberately, because the stale return manifest is evidence:

    00_v1_handoff/MANIFEST.sha256     e02195eb7edaefaf…
    01_run_A/tree/MANIFEST.sha256     e02195eb7edaefaf…

They are equal. That equality is the evidence for `ERRATA.md` E2.

## Read-only sources touched

| path | access |
|---|---|
| `~/Downloads/1738ee80-…-aristotle.tar.gz` | read; copied, never moved |
| `ARISTOTLE_DELTA_DESCENT_V1` | read; **not modified** |
| `~/k33-successor-base-v6-2026-08-29/.lake/packages` | cloned copy-on-write into a scratch build tree |

No source object was modified.
