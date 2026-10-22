# Source register

| copy | sha256 |
|---|---|
| handoff as built | `d2f77d12d0a271ad78182103f1be2b5348143a510437fbb65b721671ac2f3708` |
| returned by Run A | `d2f77d12d0a271ad78182103f1be2b5348143a510437fbb65b721671ac2f3708` |
| returned by Run B | `d2f77d12d0a271ad78182103f1be2b5348143a510437fbb65b721671ac2f3708` |

## Carried trees

| directory | files | manifest failures |
|---|---|---|
| `00_v1_handoff/` | 54 | 0 |
| `01_run_A/tree/` | 57 | 0 (54 handoff files + input tar + `ARISTOTLE_SUMMARY.md` + `P04C_COMPLETION_NOTES.md`) |
| `02_run_B/tree/` | 57 | 0 (54 handoff files + input tar + `ARISTOTLE_SUMMARY.md` + `receipts_p04c_completion/verification.txt`) |

## The file the runs were asked to change

| copy | sha256 | lines | declarations |
|---|---|---|---|
| handoff `P04c/TwoDescent.lean` | `529f08cd2ece76723b873ec749cbfc37dcc665531380a0b4dd61bf4e9e912704` | 127 | 5 |
| Run A `P04c/TwoDescent.lean` | `a174a7c4b73676c344850c4179934143e66da1b5c7376799f1c0759f227ba1ab` | 346 | 20 |
| Run B `P04c/TwoDescent.lean` | `56d10309f5acb8ea0610d53e72d8453114f797120bb7da306d13ac7a09ae61b2` | 370 | 22 |

The statement of `two_descent_quotient` hashes to
`4f28de06a5117cae6a68940bbc3fccadd630e33b4a9f094e5e2dc66f14d668da` in **all three** copies.

## Plumbing authored by Claude, not by a run

`dblHom`, `twoE`, `mem_twoE` and `KExp_le_GphiExp` were written and proved **in the handoff**.
Both returns brought that block back byte-identical
(`5060c0ac0ba8f6b1299aefcc9442469bfac343d8684e470f3273e21ee034889c`). Authorship is recorded
here so it is never mistaken for run-certified mathematics; what the two runs certify about it
is only that it compiles and — for `dblHom`, `twoE`, `mem_twoE` — that it is used.

`KExp_le_GphiExp` was used by **neither** run (`receipts/DEPENDENCY_FOOTPRINT.txt`).

## The thirty inherited Lean sources — untouched by both runs

Per-file digests are in `receipts/RUN_A_INDEPENDENT_VERIFICATION.txt` §3. The tree is the P04b
freeze's Run B continuation base plus this stage's `Main.lean`:

* point branch (14): `Run013/Basic`, `Run013/Selmer`, `SDyadic/Family`, `Descent/Delta`,
  `Descent/Ported`, `P01/TwoTorsion`, `P01/PortedRunB`, `P01/Instances`, `P03a/PointMaps`,
  `P03b/Additivity`, `P03c/Kernels`, `P03d/Composites`, `P03e/Bridge`, `P04a/Cokernels`;
* saturation branch (13): `SDyadic/Arith`, `CovAlg`, `DualSide`, `Instances`, `LocalCommon`,
  `LocalEll`, `LocalQ`, `LocalTwo`, `PadicTools`, `PhiSide`, `Saturation`, `Structure`,
  `Witness`;
* the merged stages (2): `P04b/Reconnect`
  (`e86998ef87561ddebd806d9cd6e55c29d18edce59499b60b0eaea03ebdb577d2`), `Main.lean`.

## Archives

| file | sha256 | bytes |
|---|---|---|
| `_external/originals/ARISTOTLE_P04C_TWO_DESCENT_QUOTIENT_V1.tar.gz` | `d2f77d12d0a271ad78182103f1be2b5348143a510437fbb65b721671ac2f3708` | 100678 |
| `_external/originals/RUN_A_d671cf2d-aristotle.tar.gz` | `d98533b6b5571982fa8ef599326f73fb93bf5de30e44d32c06c119c4a86b037f` | 207031 |
| `_external/originals/RUN_B_ff442041-aristotle.tar.gz` | `2e52c099b7db3282431205823287830abe64ace5496ecc9e5706ad739206fb98` | 206777 |

## Receipts that are themselves source

| file | sha256 |
|---|---|
| `receipts/semantic_probe.lean` | `8446c92394f3512e613e405005dd981eb2fc4d7f4beb685cdb804627c83f5059` |
| `receipts/dependency_footprint.lean` | `4af447f0f5beed37074b78dce412f87c0c30fa8abb32593732704f8fbd30adc3` |

Both compiled unchanged against both developments. Neither names a run-specific helper.

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
