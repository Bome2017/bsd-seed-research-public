# RESULT: p = 47, l = 283 (Batch C step 3; 2026-09-27 UTC)

**Verdict (frozen checker): NONZERO.** Reasons: none.
- c₀ = 0 and c₁ = 27260 = 47·580 ≡ 0 (mod 47).
- **c₂ = 596378 ≡ 42 (mod 47).**

| axis | outcome |
|---|---|
| Numerical certificate | **ACCEPTED** |
| Arithmetic consequence | **Sha(E/ℚ)[47^∞] = 0**, by Ota Thm 1.5/6.4 at the audited grade, with 47 ∉ S₀, 47 ∤ 6N·16 and #E(F₄₇) = 44 |
| Prediction (sealed ADDENDUM_2 `2be68ea1…`: c₂ ≡ 42) | **MATCH** |

**Bindings.**
- The receipt root 9fc6b8e8… equals the pinned root over 0..5853, on the new corpus_ext_6445. That corpus passed
  CORPUS_CHECK_6445 with 10/10 earlier roots reproduced.
- The engine is 47d07f2e…, T = 98,213,822,463, and g = 3.
- **Downstream checks:** recompute_downstream gives 42, with 282 symbols and 92 generators checked. A fresh interval
  check found all **564** balls unique.

**Package and run.**
- Package FROZEN_RUN_PACKAGE_p47_l283 @ 0d4711e.
- The run went from 20:20:42Z to 21:47:52Z.
- Resources: 5229 s wall, 41,261 user-s + 177 sys-s = **11.51 CPU-h**, peak RSS 0.75 GB.

**Next.** The stop rule was satisfied, so step 4 (31/311, package f970040) was launched.
