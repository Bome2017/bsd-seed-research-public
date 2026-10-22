# RESULT: p = 31, l = 311 (Batch C step 4; 2026-09-27 UTC)

**Verdict (frozen checker): NONZERO.** Reasons: none.
- c₀ = 0 and c₁ = 22072 = 31·712 ≡ 0 (mod 31).
- **c₂ = 330990 ≡ 3 (mod 31).**

| axis | outcome |
|---|---|
| Numerical certificate | **ACCEPTED** |
| Arithmetic consequence | **Sha(E/ℚ)[31^∞] = 0**, by Ota Thm 1.5/6.4 at the audited grade, with 31 ∉ S₀, 31 ∤ 6N·16 and #E(F₃₁) = 40 |
| Prediction (sealed `4853a5fb…`: c₂ ≡ 3) | **MATCH** |

**Bindings.**
- The receipt root 92cd0222… equals the pinned root over all 6445 segments (corpus_ext_6445, CORPUS_CHECK_6445 all_ok).
- The engine is 47d07f2e…, T = 108,129,157,119, and g = 17.
- **Downstream checks:** recompute_downstream gives 3, with 310 symbols and 120 generators checked. A fresh interval
  check found all **620** balls unique.

**Package and run.**
- Package FROZEN_RUN_PACKAGE_p31_l311 @ f970040.
- The run went from 21:48:21Z to 23:25:57Z.
- Resources: 5836 s wall, 45,913 user-s + 226 sys-s = **12.82 CPU-h**, peak RSS 0.74 GB.

**Consequence.** With 31, 43 and 47 settled, Sha[p^∞] = 0 now holds for every prime p ≤ 47 except p = 3, where
Sha[3^∞] ≅ (ℤ/3)². Each holds at its recorded grade. **If Sha(E/ℚ) is finite, then #Sha = 9 or #Sha ≥ 9·53² = 25,281.**
