# Source register

| copy | sha256 |
|---|---|
| handoff as built | `03394e93fd7ec650b315dbbc0c80f906d4c2f7255587a52c6d180d64764a95c4` |
| returned by Run A | `03394e93fd7ec650b315dbbc0c80f906d4c2f7255587a52c6d180d64764a95c4` |
| returned by Run B | `03394e93fd7ec650b315dbbc0c80f906d4c2f7255587a52c6d180d64764a95c4` |

## Carried trees

| directory | files | manifest failures |
|---|---|---|
| `00_v1_handoff/` | 36 | 0 |
| `01_run_A/tree/` | 39 | 0 (36 handoff files + input tar + `ARISTOTLE_SUMMARY.md` + `P04A_COMPLETION_RECEIPT.md`) |
| `02_run_B/tree/` | 39 | 0 (36 handoff files + input tar + `ARISTOTLE_SUMMARY.md` + `P04A_COMPLETION_NOTES.md`) |

## The file the runs were asked to change

| copy | sha256 | lines | declarations |
|---|---|---|---|
| handoff `P04a/Cokernels.lean` | `f76083e1b68dbe0410f876f044eb49f5758931c375195fbd04edb80900e5b68a` | 135 | 3 |
| Run A `P04a/Cokernels.lean` | `1b91f7cf74ad2fd08811e7c560dc673a811ab4469a78c47568284e3473522798` | 224 | 13 |
| Run B `P04a/Cokernels.lean` | `82f3698942ac99d5336caed9a33be56fc5975f116240c9c9407dc78998cb6e70` | 220 | 12 |

The statement of `isogeny_cokernels` hashes to `9a660dd5819e4fa0fe3337d61a7bc54d7663c81370bd5be642111e7ca3b8e58b`
in **all three** copies.

## The fourteen inherited Lean sources — untouched by both runs

| file | sha256 |
|---|---|
| `Run013/Basic.lean` | `4f085a8c7f3cb0621af4341a87a8aed26bde2cee5f0d9148a58a4c3332115947` |
| `Run013/Selmer.lean` | `4dda4069454b2dd02a7c1a821d0a7e7cf7ecae775147f6e38f9e877f57fa3a0b` |
| `SDyadic/Family.lean` | `a866211d79a65fdf030e53f0ed9519ecf86bbc80c1fca2c778d3ba8f2499f2c3` |
| `Descent/Delta.lean` | `b1d5625d1a7c8651777c4ab4f149deda26b4ba2cb01dced12ccf839492af17f7` |
| `Descent/Ported.lean` | `938750075fbfa5ea71df6bd8d1063d1a9ec27b6b93005061cb741ee7b50c91ef` |
| `P01/TwoTorsion.lean` | `1d2941e00a8b2a32c01fde83d053e210fd5214ba50154f4c532bd3eba53b39e8` |
| `P01/PortedRunB.lean` | `37e80ea675ccbe353f4e23f9ba8a529bf34ff3f28e4c5332cd7db1369d460f21` |
| `P01/Instances.lean` | `157d05af9edec15260fd0156540a3317204edf98cb0d6c28eae44ac295822b92` |
| `P03a/PointMaps.lean` | `bd3fe49394d08e46d6cf6205760648fc50d5ef4fb23942c641381286d4a66b03` |
| `P03b/Additivity.lean` | `68d2dfcc0dcbb9d43f5e0e6e73ea683b38c6f4958e404a5fb3f2135e54206116` |
| `P03c/Kernels.lean` | `1f43cea283c93a3f19f09afbc432027a499c86eecd190b28446e2d73a477b53c` |
| `P03d/Composites.lean` | `959f5c7a951d6f04f2df04a8e64016b29650c4b6da4ca8e400629b20881b4c80` |
| `P03e/Bridge.lean` | `1d2ab5361e975cc26151c2ea0462909545c709c127abd9428ac201e764564f26` |
| `Main.lean` | `a1f8f015cc677acc0c449b074a1f5bc2712d9e7ce8f1f1eafbd7d0c5c32da2c4` |

## Archives

| file | sha256 | bytes |
|---|---|---|
| `_external/originals/ARISTOTLE_P04A_ISOGENY_COKERNELS_V1.tar.gz` | `03394e93fd7ec650b315dbbc0c80f906d4c2f7255587a52c6d180d64764a95c4` | 63372 |
| `_external/originals/RUN_A_da3311d7-aristotle.tar.gz` | `9c9f872296faad9411b55a783590edfa098ca4bbf21b17bdd2793f3111cf3bd7` | 133057 |
| `_external/originals/RUN_B_f8aa78cd-aristotle.tar.gz` | `237b49f63013b2a46133dc74530247bee7cc015069b44631908ec1aa31bab505` | 132348 |

## Probe

| file | sha256 |
|---|---|
| `receipts/semantic_probe.lean` | `78e6cb7238daed78ab6115423756d97703a0c0c344fcd7af62442b91f8fc43b9` |

Compiled unchanged against both developments. It names no run-specific helper.

## Toolchain

    leanprover/lean4:v4.28.0
    mathlib 8f9d9cff6bd728b17a24e163c9402775d9e6a365

## Archive recipe (this object)

Byte-reproducible; built twice and compared. Host extended attributes excluded, entry list
sorted (`ERRATA.md` E6 in the P03e freeze).

```bash
find "$N" -exec touch -t 202609110000 {} +
find "$N" | LC_ALL=C sort > list.txt
tar --uid 0 --gid 0 --numeric-owner --no-mac-metadata --no-xattrs --no-acls \
    -n -cf - -T list.txt | gzip -n > "$N.tar.gz"
```

No source object was modified.
