# Source register

| copy | sha256 |
|---|---|
| handoff as built | `1daf41ef1b899fcaca08a9b2d58f77710385fb19cb11fdd0556f2dad70ae4f8a` |
| returned by Run A | `1daf41ef1b899fcaca08a9b2d58f77710385fb19cb11fdd0556f2dad70ae4f8a` |
| returned by Run B | `1daf41ef1b899fcaca08a9b2d58f77710385fb19cb11fdd0556f2dad70ae4f8a` |

## Carried trees

| directory | files | manifest failures |
|---|---|---|
| `00_v1_handoff/` | 33 | 0 |
| `01_run_A/tree/` | 21 | 0 (partial wrapper: 19 of 33 handoff files + 2 extras) |
| `02_run_B/tree/` | 36 | 0 (33 handoff files + 3 extras) |

## The file the runs were asked to change

| copy | sha256 | lines | declarations |
|---|---|---|---|
| handoff `P03e/Bridge.lean` | `f0306243550d100c36dcad81e86e64b51fa594bb0e5ac268eca4f6fb2429138a` | 104 | 1 |
| Run A `P03e/Bridge.lean` | `db0f41c2be74726c87ed2245a36cd8d791ffc46ae6249ed3f7074db1d8a7dfcb` | 386 | 12 |
| Run B `P03e/Bridge.lean` | `1d2ab5361e975cc26151c2ea0462909545c709c127abd9428ac201e764564f26` | 405 | 13 |

The statement of `descent_kernel_eq_isogeny_image` is **byte-identical** in all three.

## The twelve inherited Lean sources — untouched by both runs

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
| `Main.lean` | `6951e8ee4170f479405e710ef94b36e940d16c90a7b75124ec2ad3bee4daa2ce` |

(`Main.lean` is carried as a thirteenth unchanged file; it is the import root, not a semantic
source.)

## Archives

| file | sha256 | bytes |
|---|---|---|
| `_external/originals/ARISTOTLE_P03E_DESCENT_KERNEL_IS_ISOGENY_IMAGE_V1.tar.gz` | `1daf41ef1b899fcaca08a9b2d58f77710385fb19cb11fdd0556f2dad70ae4f8a` | 59557 |
| `_external/originals/RUN_A_a5b17c28-aristotle.tar.gz` | `3c32b4bbbb0ad3022a8a64e08f2e52fbcb6cc443119c2a6d3fe5d2825ebad74e` | 99464 |
| `_external/originals/RUN_B_0b31aec2-aristotle.tar.gz` | `5c7ae1ffce2447d0fb190229736d49ff4b7c4c09e6654381f3fff3c294e6f366` | 125318 |

## Probe

| file | sha256 |
|---|---|
| `receipts/semantic_probe.lean` | `a6c56b75f190302fff81147f3297ea20114fe2d3200583ed90856cdcb8c171eb` |

Compiled unchanged against both developments.

## Toolchain

    leanprover/lean4:v4.28.0
    mathlib 8f9d9cff6bd728b17a24e163c9402775d9e6a365

No source object was modified.

## Archive recipe (this object)

Byte-reproducible; built twice and compared. Host extended attributes are excluded and the
entry list is sorted, which earlier freeze archives did not do (`ERRATA.md` E6).

```bash
find "$N" -exec touch -t 202609110000 {} +
find "$N" | LC_ALL=C sort > list.txt
tar --uid 0 --gid 0 --numeric-owner --no-mac-metadata --no-xattrs --no-acls \
    -n -cf - -T list.txt | gzip -n > "$N.tar.gz"
```

148 entries (105 files, 43 directories).
