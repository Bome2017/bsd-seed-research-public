# RESULT: p = 41, l = 83 (out-of-sample test 1 of 2; 2026-09-27 UTC)

**Verdict (frozen checker): NONZERO.** Reasons: none.
- c₀ = 0 and c₁ = −5904 = −41·144 ≡ 0 (mod 41), as the theory requires.
- **c₂ = −83420 ≡ 15 (mod 41).**

The result is recorded on three separate axes (PREDICTIONS_2026-09-26_ADDENDUM_1):

| axis | outcome |
|---|---|
| Numerical certificate | **ACCEPTED**: every binding passed (details below) |
| Arithmetic consequence | **Sha(E/ℚ)[41^∞] = 0**, by Ota Thm 1.5/6.4 at the audited grade, with p = 41 ∉ S₀, 41 ∤ 6N·16 and #E(F₄₁) = 36 |
| Prediction (sealed, `4853a5fb…`: c₂ ≡ 15) | **MATCH**. This is the first fully out-of-sample confirmation of the K ≡ 288 relation at a new prime |

**Bindings checked by the frozen checker** (byte-identical to the p = 17 freeze):
- the receipt root e442e6c1… equals the pinned root over segments 0..1676;
- PARAMS equals the frozen command;
- the engine sha256 is 47d07f2e…;
- the output hash matches the manifest;
- the label set is exactly the units mod 83;
- the COUNT identity holds at T = 28,135,391,231;
- each symbol is a unique point of (1/1024)ℤ;
- symmetry holds.

**Recomputations of c₂ from the same certified symbol table.**
- `recompute_downstream.py`: c₂ ≡ 15, all 82 symbols integral, and the orbit over 40 generators was checked.
- A fresh minimal script with g = 2 also gives c₂ = −83420 ≡ 15.
- Both are downstream arithmetic checks, not independent symbol evaluations.

**Package and run.**
- Package: FROZEN_RUN_PACKAGE_p41_l83 @ 6c945e88ad1b5e570aa39428096ad88620fd06cf. It was unmodified after the run.
- The run went from 2026-09-27T04:29:32Z to 04:53:04Z.
- Resources: 1414 s wall, 11,206 user-s = **3.11 CPU-h** (+25 s sys), peak RSS 0.72 GB, and 66 MB of output.

**Output hashes.**

| file | sha256 |
|---|---|
| msl.txt | `385557f41b6fab7f5fb09963d4334a6e3d045d8cdb7f66210a3ef81a5d2d90dd` |
| RUN_MANIFEST.json | `c8a118ce…6bf5` |
| SINGLETON_REPORT.json | `f96ed8a6…a825` |
| units/PARAMS | `84e4a1ff…7a28` |

**Consequences.**
- The stop rule allowed test 2, (37, 149), which was launched.
- The 8649 order threshold is unchanged while 31 is open.
- Nothing else was launched.
