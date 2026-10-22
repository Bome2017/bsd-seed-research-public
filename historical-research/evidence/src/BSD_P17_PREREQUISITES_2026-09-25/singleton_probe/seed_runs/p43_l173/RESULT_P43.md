# RESULT: p = 43, l = 173 (Batch C step 1; 2026-09-27 UTC)

**Verdict (frozen checker): NONZERO.** Reasons: none.
- c₀ = 0 and c₁ = −13072 = −43·304 ≡ 0 (mod 43).
- **c₂ = −227412 ≡ 15 (mod 43).**

| axis | outcome |
|---|---|
| Numerical certificate | **ACCEPTED**: every binding passed |
| Arithmetic consequence | **Sha(E/ℚ)[43^∞] = 0**, by Ota Thm 1.5/6.4 at the audited grade, with 43 ∉ S₀, 43 ∤ 6N·16 and #E(F₄₃) = 52 |
| Prediction (sealed `4853a5fb…`: c₂ ≡ 15) | **MATCH** |

**Bindings checked by the checker:**
- the receipt root 80b814ed… equals the pinned root over segments 0..3544;
- the engine is 47d07f2e…;
- T = 59,475,230,719;
- the labels are exactly the units mod 173;
- each symbol is a unique point of (1/1024)ℤ;
- symmetry holds.

**Downstream checks.**
- `recompute_downstream.py` gives 15, with all 172 symbols integral and 84 generators checked.
- A fresh interval check found all **344** balls unique, and the declared points reproduce c₂ = −227412.

**Package and run.**
- Package FROZEN_RUN_PACKAGE_p43_l173 @ 1a4564d, unmodified after the run.
- The run went from 15:32:52Z to 16:26:50Z.
- Resources: 3238 s wall, 25,410 user-s + 163 sys-s = **7.10 CPU-h**, peak RSS 0.68 GB.

**Output hashes.**

| file | sha256 |
|---|---|
| msl.txt | `f61132e18906c5a407e3fc03560e5fe21a744dd3a02f59eba9809c8d97361bb8` |
| RUN_MANIFEST.json | `b7b14977…2833` |
| SINGLETON_REPORT.json | `118c012c…b3bb` |

**Next.** Stop rule satisfied (ACCEPTED and MATCH), so step 2, Stage W for corpus_ext_6445, was launched at
16:27:17Z.
