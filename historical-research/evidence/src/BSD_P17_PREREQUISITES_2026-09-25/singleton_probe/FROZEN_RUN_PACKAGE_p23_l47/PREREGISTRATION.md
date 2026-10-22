# Pre-registration: singleton Ota witness at p = 23, l = 47 (frozen 2026-09-26, before launch; NOT launched)

**The run.** Exactly one run: the seed E: y² = x³ − 22735x² + 106272484x, with p = 23 (good supersingular (a_23 = 0)), l = 47,
Q = N = 6503188012738584, sign +1, T = 14914945023 (889 segments of 2²⁴) and LATDEN 1024.
- The coefficient corpus is `/Users/bsm/BSD_SEED_P13_RUN_2026-09-21/run/ap`, read-only; Stage W is not run.
- Pinned receipt root: a83f42e33f0697bf0f29421b70e6143114e6b67703f18652aa028e8458787ebd.

**Admissibility**, recounted independently by the audit:
- #E(F_47) = 44, and p ∤ #E(F_47), so E(F_47)[23] = 0;
- v_23(47 − 1) = 1, and 47 ∤ 23N;
- #E(F_23) = 24, so p is not anomalous.

**Grade.** Ota Thm 1.5/6.4 carries no ordinary-reduction hypothesis at p; audit item 5 CONFIRMED this at the
retained-import grade. The acceptance code is byte-identical to the frozen p = 17 package's `checker/` (20/20 controls).

**Three outcomes, fixed now:**
1. **NONZERO** (exit 0), accepted only if every binding passes:
   - the receipt root equals the pinned root;
   - PARAMS equals the frozen command;
   - the manifest binds the engine and output hashes;
   - the label set is exactly the units mod 47;
   - the numeric COUNT identity holds with the frozen T;
   - each symbol is a unique lattice point;
   - symmetry holds, c₀ = 0 and c₁ ≡ 0 (mod 23).

   Then **Sha(E/ℚ)[23^∞] = 0** (Ota), at the audited grade. By itself this does not move the conditional order
   threshold while 19 is unsettled.
2. **INCONCLUSIVE_ZERO** (exit 3). This says only that c₂ ≡ 0 (mod 23), and nothing about Sha[23^∞]. The next
   candidate, l = 139, is NOT launched automatically.
3. **INVALID** (exit 2), or any refusal or crash. **Stop** and diagnose. It is never read as a mathematical zero.

A zero or invalid result here does not affect the accepted p = 17 result.
