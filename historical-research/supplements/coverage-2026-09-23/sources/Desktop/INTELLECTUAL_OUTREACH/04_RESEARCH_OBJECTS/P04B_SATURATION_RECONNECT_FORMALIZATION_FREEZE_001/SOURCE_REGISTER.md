# Source register

| copy | sha256 |
|---|---|
| handoff as built | `7d7daa55b0e71a38ab91ad353408a94986887e782fca161de517074fcb968167` |
| returned by Run A | `7d7daa55b0e71a38ab91ad353408a94986887e782fca161de517074fcb968167` |
| returned by Run B | `7d7daa55b0e71a38ab91ad353408a94986887e782fca161de517074fcb968167` |

## Carried trees

| directory | files | manifest failures |
|---|---|---|
| `00_v1_handoff/` | 50 | 0 |
| `01_run_A/tree/` | 53 | 0 (50 handoff files + input tar + `ARISTOTLE_SUMMARY.md` + `RECONNECT_RUN_RECEIPTS.md`) |
| `02_run_B/tree/` | 53 | 0 (50 handoff files + input tar + `ARISTOTLE_SUMMARY.md` + `P04B_RECONNECT_RESULT.md`) |

## The file the runs were asked to change

| copy | sha256 | lines | declarations |
|---|---|---|---|
| handoff `P04b/Reconnect.lean` | `eefc5279a189b0b766fd868fc19eca12e02569521ac09a6e8b50d7aeae3f9e29` | 100 | 2 |
| Run A `P04b/Reconnect.lean` | `bd78f5de4e93ca6f1b7dd4742ba081a61bef0e7862d97f851f1f8cbcb51737ba` | 290 | 14 |
| Run B `P04b/Reconnect.lean` | `e86998ef87561ddebd806d9cd6e55c29d18edce59499b60b0eaea03ebdb577d2` | 285 | 17 |

The statement of `saturation_reconnect` hashes to
`41b0fd96974e7d5c54b9c8bb1f274871e7b91e8086952d37ff51e6aac33ab1b8` in **all three** copies.

`cls_phiB_eq_cls_DD` — the elementary bridge `cls (phiB) = cls D`, **authored and proved in the
handoff by Claude**, not by either run — came back byte-identical in both returns
(`b0e183c911f64ad3435167a5dae9222918b7b907e3e2a6354327149673c6f1e4`). Its authorship is
recorded here so that it is never mistaken for run-certified mathematics; what the two runs
certify about it is only that it compiles and is used.

## The twenty-nine inherited Lean sources — untouched by both runs

Point branch (from the P04a freeze's Run B continuation base):

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
| `P04a/Cokernels.lean` | `82f3698942ac99d5336caed9a33be56fc5975f116240c9c9407dc78998cb6e70` |

Saturation branch — `Arith`, `CovAlg`, `DualSide`, `LocalCommon`, `LocalEll`, `LocalQ`,
`LocalTwo`, `PadicTools`, `PhiSide`, `Saturation`, `Structure`, `Witness` are **saturation
Run A**; `Instances` is **saturation Run B**. Per-file digests are in
`receipts/RUN_A_INDEPENDENT_VERIFICATION.txt` §3 and were verified against
`S_DYADIC_SATURATION_FORMALIZATION_FREEZE_002` before the handoff was built.

`Run013/Basic.lean`, `Run013/Selmer.lean` and `SDyadic/Family.lean` are byte-identical in both
saturation runs **and** in the point branch. That is what made the merge clean; a declaration
census over the two trees found **0 collisions**.

## Archives

| file | sha256 | bytes |
|---|---|---|
| `_external/originals/ARISTOTLE_P04B_SATURATION_RECONNECT_V1.tar.gz` | `7d7daa55b0e71a38ab91ad353408a94986887e782fca161de517074fcb968167` | 93246 |
| `_external/originals/RUN_A_9905fc47-aristotle.tar.gz` | `5d045ef4cb8e3a6806c7ef30207e172b58f37a13763246ce549b1cbc9eeb6bcd` | 192316 |
| `_external/originals/RUN_B_b19f4a89-aristotle.tar.gz` | `189691739477d30fc2e646f782881501295383ea6906c00e434eb172cd9900d5` | 192711 |

## Probe

| file | sha256 |
|---|---|
| `receipts/semantic_probe.lean` | `f75e9a6e9c8ad94562a1d837a6453b306781040e60a77745d93d87c497655d6c` |

Compiled unchanged against both developments. It names no run-specific helper.

## Toolchain

    leanprover/lean4:v4.28.0
    mathlib 8f9d9cff6bd728b17a24e163c9402775d9e6a365

## Archive recipe (this object)

```bash
find "$N" -exec touch -t 202609110000 {} +
find "$N" | LC_ALL=C sort > list.txt
tar --uid 0 --gid 0 --numeric-owner --no-mac-metadata --no-xattrs --no-acls \
    -n -cf - -T list.txt | gzip -n > "$N.tar.gz"
```

No source object was modified.
