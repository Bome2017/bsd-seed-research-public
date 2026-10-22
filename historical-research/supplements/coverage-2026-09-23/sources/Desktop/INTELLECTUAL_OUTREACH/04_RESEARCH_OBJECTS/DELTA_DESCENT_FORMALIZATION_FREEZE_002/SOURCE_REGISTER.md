# Source register

## Carried forward from Freeze 001, byte-identical

Freeze 001 root manifest: `aabc880f5dd26df6b678093d7427055746099de6a13d25a27c65d175d74095e5` (61 entries).

All 46 files under `00_v1_handoff/` and `01_run_A/` were compared file-by-file:
**46/46 byte-identical, 0 failures**. Freeze 001's seven receipts are carried forward
under `receipts/RUN_A_*` (renamed only, contents unchanged).

## Run B — new in this object

All 25 files under `02_run_B/tree/` were compared against the extracted wrapper:
**25/25 byte-identical, 0 failures**.

| file | sha256 | bytes |
|---|---|---|
| `02_run_B/tree/RequestProject/Descent/Delta.lean` | `b1d5625d1a7c8651777c4ab4f149deda26b4ba2cb01dced12ccf839492af17f7` | 16631 |
| `02_run_B/tree/RequestProject/Run013/Basic.lean` | `4f085a8c7f3cb0621af4341a87a8aed26bde2cee5f0d9148a58a4c3332115947` | 5857 |
| `02_run_B/tree/RequestProject/Run013/Selmer.lean` | `4dda4069454b2dd02a7c1a821d0a7e7cf7ecae775147f6e38f9e877f57fa3a0b` | 6624 |
| `02_run_B/tree/VERIFICATION.md` | `f2e59cba7b97b88e544a6e4ba592dc9208b8de7e5f8f92c603cd1317614294b2` | 2641 |
| `02_run_B/tree/ARISTOTLE_SUMMARY.md` | `c3ff655292b4e3f158fdbf0a00853d66cacb5f124a5e6632c44f989e5d7ef949` | 2596 |
| `02_run_B/tree/MANIFEST.sha256` | `e02195eb7edaefafa01062fa4315f94059b5e55932e07f113c7ce88fee5222e8` | 1847 |

## The single shared input

| copy | sha256 |
|---|---|
| as built | `b75ba34edce636035eb2d4c22b998d70ab51298434ffb0ae8558ab58c25052d3` |
| frozen here | `b75ba34edce636035eb2d4c22b998d70ab51298434ffb0ae8558ab58c25052d3` |
| returned by Run A | `b75ba34edce636035eb2d4c22b998d70ab51298434ffb0ae8558ab58c25052d3` |
| returned by Run B | `b75ba34edce636035eb2d4c22b998d70ab51298434ffb0ae8558ab58c25052d3` |

All four agree. Both runs consumed byte-identical input.

## Archives

| file | sha256 | bytes |
|---|---|---|
| `_external/originals/ARISTOTLE_DELTA_DESCENT_V1.tar.gz` | `b75ba34edce636035eb2d4c22b998d70ab51298434ffb0ae8558ab58c25052d3` | 45091 |
| `_external/originals/RUN_A_1738ee80-aristotle.tar.gz` | `87240251498c633bf16ce513d7984d587c03b7cf8f3faeab9322731e746f6232` | 95806 |
| `_external/originals/RUN_B_ab937806-aristotle.tar.gz` | `a6b00c56164cf65840e6510a68b22597e74eab2210fa500eae29ce0294fc1a71` | 96153 |

## Files written by this object

| file | role |
|---|---|
| `README.md` | what this object is; the independence caveat |
| `STATUS.md` | certification tier, boundary, independence class |
| `AB_ARCHITECTURE_COMPARISON.md` | §1 the shared hint; then how the two differ |
| `REUSABLE_LEMMA_CROSSWALK.md` | every added lemma classified GENERIC/CURVE_BOUND/LOCAL |
| `CONTINUATION_BASE_ASSESSMENT.md` | Run B + 3 ported lemmas, with the counter-argument |
| `PROOF_ARCHITECTURE_RUN_A.md` | carried from Freeze 001, renamed to disambiguate |
| `ERRATA.md` | E1 carried; E2 now confirmed in both runs; E3 cross-reference |
| `SOURCE_REGISTER.md` | this file |
| `02_run_B/STALE_METADATA_NOTICE.md` | warning beside Run B's tree |
| `receipts/RUN_B_*` | custody, rebuild, axioms, constructs, stale metadata |
| `receipts/TARGET_STATEMENT_COMPARISON.txt` | three-way declaration diff |
| `receipts/CROSS_RUN_INTERFACE_CHECK.txt` | one probe, both developments |

## Manifest coverage

The root manifest excludes only itself. All three nested manifests are covered:

    00_v1_handoff/MANIFEST.sha256      e02195eb7edaefaf…
    01_run_A/tree/MANIFEST.sha256      e02195eb7edaefaf…
    02_run_B/tree/MANIFEST.sha256      e02195eb7edaefaf…

All three are equal — which is exactly the evidence for `ERRATA.md` E2.

## Read-only sources touched

| path | access |
|---|---|
| `~/Downloads/ab937806-…-aristotle.tar.gz` | read; copied, never moved |
| `DELTA_DESCENT_FORMALIZATION_FREEZE_001` | read; manifest re-verified; **not modified** |
| `ARISTOTLE_DELTA_DESCENT_V1` | read; **not modified** |
| `~/k33-successor-base-v6-2026-08-29/.lake/packages` | cloned copy-on-write into a scratch build tree |

No source object was modified.
