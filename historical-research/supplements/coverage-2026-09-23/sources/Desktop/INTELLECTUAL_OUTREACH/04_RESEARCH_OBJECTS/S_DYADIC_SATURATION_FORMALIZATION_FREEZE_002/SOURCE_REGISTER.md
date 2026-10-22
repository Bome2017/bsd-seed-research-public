# Source register

## Carried forward from Freeze 001, byte-identical

Freeze 001 root manifest: `518b740c48520467b552234ada2b6d079a6a12d299d903678bef819d380b1ce9` (65 entries).

All 58 files under `00_v1_handoff/` and `01_run_A/` were copied and then compared
file-by-file against Freeze 001: **58/58 byte-identical, 0 failures**. Freeze 001's
three receipts are carried forward under `receipts/RUN_A_*` (renamed only, contents
unchanged) so Run B's receipts can sit beside them without collision.

## Run B — new in this object

| file | sha256 | bytes |
|---|---|---|
| `_external/originals/RUN_B_e4d66a54-aristotle.tar.gz` | `f6f6890e0bd65908b1feab64ee97f4ee2b85aa9d8fc296757b4324bb0cbbe734` | 157322 |
| `_external/originals/RUN_B_ARISTOTLE_S_SATURATION_V2.tar.gz` | `8d17d0e677a56c2934114697de565b6132c7f1cca1a75b7d2a2b10a2b98756cf` | 58289 |
| `02_run_B/tree/MANIFEST.sha256` | `d7391faa0446462591e153910573f39ff00866c616e055761a42620a1263ea98` | 2872 |

Run B Lean sources:

| module | sha256 | lines |
|---|---|---|
| `Descent/LocalDual.lean` | `7ced8f9e2c8af1fdf7298ab0…` | 298 |
| `Descent/LocalGeneric.lean` | `e41384c4ff2baf2bb042260b…` | 81 |
| `Descent/LocalTwo.lean` | `d1fa4756363ba980071a457a…` | 134 |
| `Descent/PadicTools.lean` | `92ebe7dcbcaa24a2dd8df36c…` | 194 |
| `Descent/QsqQuotient.lean` | `a158f0f47b6c1f5874c27145…` | 116 |
| `Descent/SquareClass.lean` | `00ae49ca1e710be9a68ac497…` | 134 |
| `Main.lean` | `48c67767f6db931cd9418943…` | 9 |
| `Run013/Basic.lean` | `4f085a8c7f3cb0621af4341a…` | 143 |
| `Run013/Selmer.lean` | `4dda4069454b2dd02a7c1a82…` | 147 |
| `SDyadic/Arith.lean` | `6bc07659d62072b1b951b2bb…` | 208 |
| `SDyadic/Family.lean` | `a866211d79a65fdf030e53f0…` | 111 |
| `SDyadic/Instances.lean` | `95a3fe2e89ea1f2855d85eb6…` | 117 |
| `SDyadic/Saturation.lean` | `f9b940776c6ae4bf6bf06416…` | 590 |

## The single shared input

Both runs were given the same archive:

    ARISTOTLE_S_SATURATION_V1.tar.gz   aacd0de97688569f1214a013a62d8398c72cdd37105e35513a285051f5294b23

Run B's wrapper ships that archive back unmodified; its digest was recomputed here and
agrees with the copy frozen in Freeze 001.

## Files written by this object

| file | role |
|---|---|
| `README.md` | what this object is |
| `STATUS.md` | certification tier and boundary |
| `AB_ARCHITECTURE_COMPARISON.md` | how the two developments differ |
| `SOURCE_REGISTER.md` | this file |
| `ERRATA.md` | carried forward, plus anything new |
| `receipts/RUN_B_CUSTODY.txt` | reported hashes recomputed; input identity |
| `receipts/RUN_B_INDEPENDENT_REBUILD.txt` | build at the pin |
| `receipts/RUN_B_AXIOM_AUDIT.txt` | nine objects audited |
| `receipts/RUN_B_CONSTRUCT_SCAN.txt` | prohibited constructs + semantic traps |
| `receipts/TARGET_STATEMENT_COMPARISON.txt` | three-way declaration diff |
| `receipts/RUN_A_*` | Freeze 001's receipts, renamed only |

## Manifest coverage

This object's `MANIFEST.sha256` excludes only itself. The three nested manifests are covered
as ordinary entries:

    00_v1_handoff/MANIFEST.sha256        7166fb79…684340a4   (the V1 handoff manifest)
    01_run_A/tree/docs/MANIFEST.sha256   7166fb79…684340a4   (Run A returned it unchanged)
    02_run_B/tree/MANIFEST.sha256        d7391faa…1263ea98   (Run B's successor manifest)

That the first two are equal is the byte-level evidence that Run A consumed the exact
handoff. Freeze 001's root manifest omitted the first two; see `ERRATA.md` E3.

## Read-only sources touched

| path | access |
|---|---|
| `~/Downloads/e4d66a54-…-aristotle.tar.gz` | read; copied, never moved |
| `S_DYADIC_SATURATION_FORMALIZATION_FREEZE_001` | read; manifest re-verified; **not modified** |
| `~/k33-successor-base-v6-2026-08-29/.lake/packages` | cloned copy-on-write into a scratch build tree |

No source object was modified. Freeze 001 is intact.
