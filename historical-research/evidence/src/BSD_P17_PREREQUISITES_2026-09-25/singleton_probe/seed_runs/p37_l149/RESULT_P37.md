# RESULT: p = 37, l = 149 (out-of-sample test 2 of 2; 2026-09-27 UTC)

**Verdict (frozen checker): NONZERO.** Reasons: none.
- c₀ = 0 and c₁ = 28860 = 37·780 ≡ 0 (mod 37).
- **c₂ = 762756 ≡ 1 (mod 37).**

The result is recorded on three separate axes (PREDICTIONS_2026-09-26_ADDENDUM_1):

| axis | outcome |
|---|---|
| Numerical certificate | **ACCEPTED**: every binding passed (details below) |
| Arithmetic consequence | **Sha(E/ℚ)[37^∞] = 0**, by Ota Thm 1.5/6.4 at the audited grade, with p = 37 ∉ S₀, 37 ∤ 6N·16 and #E(F₃₇) = 28 |
| Prediction (sealed, `4853a5fb…`: c₂ ≡ 1) | **MATCH**. This is the second out-of-sample confirmation of the K ≡ 288 relation in this batch, after 41 |

**Bindings checked by the frozen checker:**
- the receipt root 7a174afd… equals the pinned root over segments 0..3044;
- PARAMS equals the frozen command;
- the engine sha256 is 47d07f2e…;
- the output hash matches the manifest;
- the label set is exactly the units mod 149;
- the COUNT identity holds at T = 51,086,622,719;
- each symbol is a unique point of (1/1024)ℤ;
- symmetry holds.

**Recomputations from the same certified table.**
- `recompute_downstream.py`: c₂ ≡ 1, all 148 symbols integral, orbit over 72 generators checked.
- A fresh interval check (`TWO_TESTS_2026-09-26/interval_check.py`, exact fractions, standard library only): all
  **296** printed plus/minus balls contain exactly their declared point of (1/1024)ℤ and no neighbour. The declared
  points reproduce c₀ = 0, c₁ = 28860 and c₂ = 762756.
- These are downstream checks, not independent symbol evaluations.

**Package and run.**
- Package: FROZEN_RUN_PACKAGE_p37_l149 @ 49368ccce6d892997ce3a8478aba84c31db03aae. It was unmodified after the run.
- The run went from 2026-09-27T04:53:42Z to 05:35:18Z.
- Resources: 2498 s wall, 19,811 user-s = **5.50 CPU-h** (+40 s sys), peak RSS 0.74 GB, and 178 MB of output.
- **Two-test total: 8.61 CPU-h**, under the 12 CPU-h cap. $0.

**Output hashes.**

| file | sha256 |
|---|---|
| msl.txt | `07f2a5e8e5c5cd93300ca1126e1255629c053a7279ff1210859560ab96e6b015` |
| RUN_MANIFEST.json | `6d290ba8…8676` |
| SINGLETON_REPORT.json | `6dfd6b2f…021f` |
| units/PARAMS | `8607ce9b…9e90` |

**Stop.** The two-test task is complete, and nothing further is launched.
- Not launched: the rest of Batch A (43, 83, 89, 113), Batch B (31), or any alternate l.
- The 8649 order threshold is unchanged while 31 is open.
