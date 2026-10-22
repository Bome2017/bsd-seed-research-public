# Source register

Provenance of every file in this freeze. Digests were computed here from the
delivered bytes, not transcribed from any report.

## Inputs — the two Pro returns, verbatim

Both runs were given the same immutable input:
`POST_SATURATION_SEL2_BRIDGE_PACKET_001`, archive
`16abdee1a9e39a44f5ada81fe267b016f95fb74fa8de1290a41614596dd7e4db`,
root manifest `24cb2797f754655d8ce01c32127fc4c648d04c0c9449e1fdb90c7a5870462df5`,
21 entries. PRO_1 recomputed and reported both digests; PRO_2 reported 21/21 match.

| file in this freeze | sha256 | bytes | origin |
|---|---|---|---|
| `01_pro_1/DEPENDENCY_GRAPH.json` | `3f55c7bc55389f41459a65df09cb6db7dbf109b073d85b931dcecd6353e3e739` | 9646 | PRO_1 return |
| `01_pro_1/FINAL_REFEREE_REPORT.md` | `f0553ea5d11852e2713b80992d13331ca437559ee1b76e12f656f8eb5dc55189` | 41086 | PRO_1 return |
| `01_pro_1/PRE_COMPARISON_RECONSTRUCTION.md` | `711278fc2cfc3322423279c15340c17b7b28a38b2fe85c114f31d9a1f3283600` | 34005 | PRO_1 return |
| `01_pro_1/STAGE_II_COMPARISON.md` | `2ea6a4d49b8f4e1b96332cbcc8942932a07a9760ab80345eba0e28c451a2d4c1` | 5517 | PRO_1 return |
| `02_pro_2/ARISTOTLE_TASK.md` | `91b011943e2a12137ad93aa6c3a4e32f282b0397d22557fada4b493fe70675f1` | 4940 | PRO_2 return |
| `02_pro_2/DEPENDENCY_GRAPH.json` | `4159d496e7cd1567f51070e7b5716451bf6dd842ba7f6e32bd5179ee31ab4cb6` | 13805 | PRO_2 return |
| `02_pro_2/DEPENDENCY_GRAPH.md` | `66bd47be488c84d51cfc6493b8c99cb2454cbf99e4cf03e460501ac94080ba80` | 12914 | PRO_2 return |
| `02_pro_2/MATHLIB_SURVEY.md` | `e9292f77e26872c47bbf969efbdcfca50c243c511ee48b81b3867d2b5c72c465` | 14645 | PRO_2 return |
| `02_pro_2/PRE_COMPARISON_RECONSTRUCTION.md` | `24527fb717de2daeaa9873f8b13f49b23503faa1dcf1f47fc816fdc9d98b6881` | 21291 | PRO_2 return |
| `02_pro_2/REFEREE_REPORT.md` | `9640e2a9e4942c81f7d67c36df74a587192b5b6a7e02c71a74fb55de4eeecf68` | 12841 | PRO_2 return |
| `02_pro_2/STAGE_II_COMPARISON.md` | `85801077f7a74b40a2d230fd57d0ed9356b7915f7cb0fc3da2f0f139c36010ff` | 4555 | PRO_2 return |

11/11 byte-identical to the delivered files. No return file was edited, reformatted,
renamed in content, or harmonised with the other run.

## The two frozen Stage-I reconstructions

| run | frozen Stage-I sha256 | claimed by the run | |
|---|---|---|---|
| PRO_1 | `711278fc2cfc3322423279c15340c17b7b28a38b2fe85c114f31d9a1f3283600` | `711278fc2cfc3322423279c15340c17b7b28a38b2fe85c114f31d9a1f3283600` | MATCH |
| PRO_2 | `24527fb717de2daeaa9873f8b13f49b23503faa1dcf1f47fc816fdc9d98b6881` | `24527fb717de2daeaa9873f8b13f49b23503faa1dcf1f47fc816fdc9d98b6881` | MATCH |

## Files written by this freeze

| file | role |
|---|---|
| `README.md` | what this object is, and how to replay it |
| `STATUS.md` | operator headline verbatim, plus the rows this freeze adds |
| `RECONCILIATION.md` | convergence and the four real differences, unharmonised |
| `NEXT_ARISTOTLE_TARGET.md` | the exact next theorem, PRO_2 primary |
| `SURVEY_EVIDENCE_BOUNDARY.md` | what ABSENT does and does not mean |
| `ERRATA.md` | E1 carried forward; E2, E3, E4 new |
| `SOURCE_REGISTER.md` | this file |
| `MANIFEST.sha256` | every entry |
| `receipts/STAGE_I_INDEPENDENCE.txt` | both Stage-I digests recomputed; embedded-vs-standalone diff |
| `receipts/HEADLINE_DIFF.txt` | mechanical key-by-key headline comparison |
| `receipts/DEPENDENCY_GRAPH_AUDIT.txt` | both graphs parsed, acyclicity, blocked-list comparison |
| `receipts/INDEPENDENT_MATH_CHECKS.txt` | 16 checks of the reports' own algebra |
| `receipts/math_checks.py` | the script behind that receipt, for replay |
| `receipts/PINNED_MATHLIB_LOCAL_VERIFICATION.txt` | local exhaustive re-run of both surveys |
| `receipts/FROZEN_OBJECT_VERIFICATION.txt` | contributing frozen objects re-verified |

## Read-only sources touched

| path | access |
|---|---|
| `~/Downloads/untitled folder 5`, `untitled folder 6` | read; copied, never moved |
| `~/k33-successor-base-v6-2026-08-29/.lake/packages/mathlib` | read-only grep at rev `8f9d9cff…`; no build, no execution |
| `POST_SATURATION_SEL2_BRIDGE_PACKET_001` | manifest re-verified only |
| `S_DYADIC_SATURATION_FORMALIZATION_FREEZE_001` | manifest re-verified only |

No source object was modified. No frozen 62a1, 66b1, two-curve, hostile-review,
finite-field, S_dyadic or saturation object was altered.
