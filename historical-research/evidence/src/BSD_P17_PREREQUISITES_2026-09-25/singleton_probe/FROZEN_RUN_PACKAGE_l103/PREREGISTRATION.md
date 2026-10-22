# Pre-registration: singleton Ota witness at p = 17, l = 103 (frozen 2026-09-26, before launch)

**The run.** Exactly one run: the curve E: y² = x³ − 22735x² + 106272484x, with p = 17, l = 103, Q = N =
6503188012738584, sign +1, T = 33218887679 (1,980 segments of 2²⁴) and LATDEN 1024.
- The coefficient corpus is `BSD_SEED_P13_RUN_2026-09-21/run/ap`, read-only.
- Pinned receipt root: 5509573097647fcb6e7f92439bc707a0a894d2b0cc18f282974fb95eb4695a17.
- The acceptance code is this package's `checker/`, hashes in `FREEZE_MANIFEST.json`. It is not modified before or
  during the run.

**Three outcomes, fixed now:**
1. **NONZERO** (checker exit 0).
   - **Accept only if** every binding passes:
     - the corpus receipt root equals the pinned root;
     - PARAMS equals the frozen command line;
     - the manifest binds the engine and output hashes;
     - the label set is the units mod 103, each exactly once, with no duplicates;
     - the numeric COUNT identity holds with T equal to the frozen T;
     - each symbol is a unique lattice point;
     - the symmetry holds, c₀ = 0 and c₁ ≡ 0 (mod 17).
   - **Then** Ota Thm 1.5/6.4 gives Sha(E/ℚ)[17] = 0, hence **Sha(E/ℚ)[17^∞] = 0**, at the audited grade.
   - **Conditional on FIN,** the next possible order of Sha above 9 becomes 3249 = 9·19².
2. **INCONCLUSIVE_ZERO** (exit 3).
   - This says only that c₂(θ₁₀₃) ≡ 0 (mod 17), and nothing about Sha[17^∞].
   - The next candidate is l = 137, which is **not launched automatically**. The 103 receipt is examined first.
   - It is not the depth-three run.
3. **INVALID** (exit 2), or any launcher refusal or crash.
   - **Stop** and diagnose the acceptance or custody failure.
   - It is never to be reinterpreted as a mathematical zero.
