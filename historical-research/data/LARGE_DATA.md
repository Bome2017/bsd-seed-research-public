# Large data: what is not in Git, how it is pinned, and how to regenerate it

The certificates in this release consume two kinds of bulk data that are **not** in the repository:
* **the Fourier-coefficient corpus.** Prime coefficients a_q are stored in segments of 2^24 integers, each checked by an independent integer verifier.
* **the per-run work units and logs.**

**A hash identifies these data; it does not supply them.** Independent replay of a large certificate needs either the data or a regeneration run. Both options, and their limits, are stated below.

## 1. Where the data are

All locations are on the originating machine (local disk). No copy exists in any cloud service or public archive.

| corpus / run | location on the originating machine | size | used by | pinned in this repository by |
|---|---|---|---|---|
| p = 3 rigorous run: 663,685,727 verified a_q; segment root `5f9994d9…` | `BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/run/` | 20 GB, 12,957 files | S.3 | `evidence/src/BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/P3_MANIFEST.sha256` (every file's sha256) |
| p = 5 rigorous upgrade: 360,542,141 verified a_q; root `fcd02437…` (byte-identical to the p = 3 corpus on the shared range) | `BSD_SEED_2243_12_P5_RIGOROUS_UPGRADE_2026-09-19/run/` | 11 GB, 6,538 files | S.5 | `evidence/src/BSD_SEED_2243_12_P5_RIGOROUS_UPGRADE_2026-09-19/P5_MANIFEST.sha256` |
| C7 / C11 corpus: 2,333 segments, T up to 39,141,244,927 (reused by C13, D=-23, D=-7) | `BSD_CODEX6_MASTER_HANDOFF_2026-09-19/_work/active_full_bsd/p11/run/` | 29 GB, 24,856 files | S.7, S.11, S.13, K.1, K.2 | `evidence/src/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/_work/active_full_bsd/p11/CERTIFICATE_BINDINGS.json`, `.../p7/CERTIFICATE_BINDINGS.json` |
| C13 external run: 948 new segments (total 3,281, T = 55,046,045,695) plus 17,605 Arb work units | `BSD_SEED_P13_RUN_2026-09-21/run/` | 19 GB, 27,583 files | S.13 | `evidence/src/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/_work/active_full_bsd/p13/CERTIFICATE_BINDINGS.json`, `COMPLETION_REVIEW.json` |
| seed 150M segments: T = 1.5·10⁸ | `BSD_RIGOROUS_STREAM_CORE_2026-09-19/runs/seed150M/` | 286 MB (all runs) | R.3, X.6 | `evidence/src/BSD_RIGOROUS_STREAM_CORE_2026-09-19/runs/seed150M/logs/ap_files.sha256` (bound by the master) |
| 2243 pilot preparation: 30 verified top segments near T_run | `BSD_2243_PILOT_PREP_2026-09-22/S3_bench/conc/ap/` | about 0.1 GB | benchmarks only | `evidence/src/BSD_2243_PILOT_PREP_2026-09-22/MANIFEST.sha256` |

The corpus roots consumed by each certificate are printed in its theorem record:
* C7: m49 `0db19ef8…`, m7 `006f8521…`
* C11: m121 `01dd1087…`, m11 `c219a9b3…`
* D=-7: AP_SEGROOT `99b47995…`
* C13: the segment roots in the external run record.

## 2. How to regenerate

**First-review correction:** do not use the legacy coefficient verifier unmodified for a new certificate. `review/repairs/wverify_distinct.c` repairs its repeated-prime-factor and pre-multiplication-bound checks; the adjacent patch shows the exact changes. `tools/replay/coefficient_verifier_regression.py --compile` exercises the real old/new C programs on macOS. The read-only supplemental check of the retained six certificate corpora passed these missing conditions (`review/replay_logs/witness_structure_summary.json`). It did not redo their group arithmetic. `review/repairs/run_witness_scan.py` can repeat that supplemental scan with explicit external-data and fresh-output paths.


The coefficient pipeline has three parts:
* an untrusted fast producer;
* an independent integer verifier (legacy source retained in `evidence/src/BSD_RIGOROUS_STREAM_CORE_2026-09-19/verifier/`; use the repair above), which checks every a_q by an integer group-order witness or by exhaustive counting for small q;
* the Arb engine (`arbcore.c`, `evidence/src/BSD_RIGOROUS_STREAM_CORE_2026-09-19/src/`).

Build instructions and toolchain versions are in `BSD_RIGOROUS_STREAM_CORE_2026-09-19/{build.sh,TOOLCHAIN.txt}`.

Measured costs on the originating host (16 GiB, 20 cores):

| target | cutoff | wall time (measured) |
|---|---|---|
| C13 (m = 169) | 5.5·10¹⁰ | about 2.5 h, including 948 new segments |
| C11 (m = 121) | 3.9·10¹⁰ | about 3 h 10 min |
| D=-7 central value | 2.0·10⁹ | about 4.5 min (reused corpus) |
| 2243 certificate (not run) | 3.9·10¹³ | about 1.1·10⁵ core-hours, i.e. about a year on this host |

## 3. Availability limits

* The corpora exist only on the originating machine. They are not uploaded to GitHub (the file-size and repository-size limits exclude them), to cloud storage, or to any archive.
* Availability to reviewers is therefore **by arrangement with the author**, or by regeneration. A regeneration of the C11/C13 corpus to T = 5.5·10¹⁰ is on the order of a day on a 20-core machine.
* The 2243 and 5843 certificates were never computed, so no corpus exists at their cutoffs (3.9·10¹³ and 1.7·10¹⁴).

## 4. Other excluded bulk and binaries

`evidence/EXCLUDED.tsv` lists every excluded file with its reason and the sha256 of the original:
* third-party publications (cited, not redistributed);
* compiled executables (sources are included);
* archives that embed private correspondence metadata;
* host telemetry.
