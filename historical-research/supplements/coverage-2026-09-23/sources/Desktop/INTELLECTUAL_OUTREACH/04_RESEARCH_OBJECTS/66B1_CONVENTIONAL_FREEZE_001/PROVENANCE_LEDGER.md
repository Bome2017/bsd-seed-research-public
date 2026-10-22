# Provenance ledger

Every imported artifact: source path, SHA-256, byte size, and where it landed.  Originals were
**copied, never moved**; nothing in `~/Downloads` or any existing research directory was modified.

## Imported originals (byte-for-byte, `_external/originals/`)

| SHA-256 | bytes | source path | layer |
|---|---:|---|---|
| `ef2daae516a50cb70900dfb4e4707929ef7d18a3df4f287a3e9aa81557effdd1` | 19170 | `Desktop/.../RUN013_BANWAIT_CAPSULE_001/PK66B1_DESIGN_PACKET_2026-09-10.zip` | L0 |
| `082091dacebb31e9778f9b60eb4d49472a679ed7fde7a78f7f39a6c31686b672` | 130643 | `~/Downloads/PK66B1_INDEPENDENT_RECONSTRUCTION.zip` | L1 |
| `0f9468a2747c98794e3c7ff3991439cd8f2355095fd2b370b6c641daaca19050` | 12050 | `~/Downloads/PRE_COMPARISON_RECONSTRUCTION.md` | L1 |
| `03643caea88d63644ad563286e5732f72acd85ed876a3bb4d1c8a7b5fff3d73d` | 6543 | `~/Downloads/STAGE_II_LOCAL_DESCENT.md` | L2 |
| `580e3f4592d07ee19def6d729f4767d970ae891cc934ad1d1c2bcd41a5a403ea` | 137177 | `~/Downloads/PK66B1_CONTINUATION_RECEIPTS.zip` | L2 |
| `41e54692d9693737d72a68847571590ddee847930491f1c46efe8129b5fea661` | 23788 | `~/Downloads/66b1_stage_I_frozen_reconstruction.zip` | L3 |
| `2a627f6574cf20f2a9f63f42dc8b19c4173985d902fa0762df7c562b105a27a4` | 16898 | `~/Downloads/FROZEN_PRE_COMPARISON_RECONSTRUCTION.md` | L3 |
| `a1b603f2f2fb16397f228258b8f358bd7f8434c3dc95fcf0d00757d454bb3fca` | 229324 | `~/Downloads/66b1_hostile_comparison_audit.zip` | L4 |

Archive member inventories (name, size, SHA-256 for all 101 members across 5 archives):
`_receipts/archive_inventories/ARCHIVE_MEMBERS.json`.

## Duplicate basenames — resolved by hash, nothing overwritten

| pair | disposition |
|---|---|
| `PRE_COMPARISON_RECONSTRUCTION.md` and `PRE_COMPARISON_RECONSTRUCT(1)ION.md` (both 12050 B) | **byte-identical**, `0f9468a2…`. Browser-numbered duplicate. One canonical copy imported; both source paths recorded. |
| `FROZEN_PRE_COMPARISON_RECONSTRUCTION.md` and `(2) FROZEN_PRE_COMPARISON_RECONSTRUCTION.md` (both 16898 B) | **byte-identical**, `2a627f65…`. Same disposition. |

## Nested-copy cross-verification

Each document appears in several archives.  All copies verified byte-identical:

| document | standalone | in L1 zip | in L2 zip | in L3 zip | in L4 zip |
|---|---|---|---|---|---|
| `PRE_COMPARISON_RECONSTRUCTION.md` | `0f9468a2…` | same | same | — | same |
| `STAGE_II_LOCAL_DESCENT.md` | `03643cae…` | same | — | — | same |
| `FROZEN_PRE_COMPARISON_RECONSTRUCTION.md` | `2a627f65…` | — | — | same | same |

The design packet's members (`01_target`, `02_literature`, `04_62a1_reference_only`,
`05_prior_art_risk`) are echoed unchanged inside both models' retained trees — **MATCH** on all four.
Independently, the referee's own `CHECKSUMS.sha256` verifies **6/6** against the design packet frozen
here, confirming both models worked from the identical input.

## Explicitly excluded from this freeze

These are **62a1** artifacts that happen to sit in the same Downloads folder.  They belong to
`run013-family-minimisation-successor-2026-09-10` and were **not** swept in:

| file | SHA-256 | note |
|---|---|---|
| `independent_reconstruction_before_comparison.md` | `4109842e…` | 62a1 Proposition A referee |
| `independent_counts.csv` (501228 B) | `71387044…` | 62a1, and a **truncated prefix** of the complete 587596-byte copy inside the 62a1 referee bundle |
| `PROP_A_INDEPENDENT_REFEREE_RECEIPTS.zip` | `ba399317…` | 62a1 referee bundle |

No truncated or defective file was imported into this object.  The 66b1 chain contains no truncated
member: every archive member hash matches its counterpart everywhere it appears.

## Replay of supplied verification programs

| program | status |
|---|---|
| `verify_stage1.py` (L3) | exit 0 |
| `verify_audit.py` (L4) | exit 0 |
| `verify_continuation.py` (L2) | exit 0 **via wrapper** — the retained original hardcodes `/mnt/data/…`; see `04_reproducibility/REPRODUCTION.md` |
| referee `CHECKSUMS.sha256` (L3) | 6/6 OK once the design packet is supplied at the path it expects |

Outputs: `_receipts/replay/`.
