# p = 23 (supersingular), l = 47: NONZERO, so Sha(E/ℚ)[23^∞] = 0 (2026-09-26)

**Status.** Computer-assisted 23-primary vanishing (Ota Thm 1.5/6.4, source-audited, including the supersingular case
under audit item 5), supported by:
- a pre-run freeze, `FROZEN_RUN_PACKAGE_p23_l47`, commit 0f4683d, whose checker is byte-identical to the p = 17 freeze;
- the frozen checker's verdict;
- a downstream recomputation.

Outside artifact-level review is outstanding: the evidence branch is not yet pushed.

**The run.**
- Seed E: y² = x³ − 22735x² + 106272484x; p = 23, with a₂₃ = 0 (good supersingular) and #E(F₂₃) = 24.
- l = 47, with #E(F₄₇) = 44, so E(F₄₇)[23] = 0, and v₂₃(46) = 1.
- T = 14,914,945,023: 889 segments of the verified corpus, read-only, no Stage W.
- Engine sha256 47d07f2e…. From 15:16:37Z to 15:29:20Z: 1.67 CPU-h (6019 user-s), 12.7 minutes wall on 8 threads,
  peak RSS 0.72 GB.

**The verdict** (frozen checker, exit 0: NONZERO, with every binding passing):
- the receipt root a83f42e33f0697bf… equals the pinned root;
- PARAMS equals the frozen command;
- the manifest binds the engine and output hashes;
- 46 labels, each exactly once, each a unique lattice point;
- the COUNT identity holds with T;
- the symmetry holds.

**The witness.** With g = 5 (the smallest primitive root mod 47): c₀ = 0, c₁ = 9430 = 23·410 ≡ 0, and
**c₂ = 103854 ≡ 9 (mod 23)**.

**Downstream recomputation** (main session, separate code; `DOWNSTREAM_RECOMPUTE_MAIN.json`): the same table gives the
same c₀, c₁ and c₂, and all symbols are integral. The generator orbit is 9·(F₂₃ˣ)²; that is a covariance check only,
not symbol certification.

**What it changes.**
- Sha(E/ℚ)[23^∞] = 0, at the grade of a source-audited published theorem plus a certified computation. It is not
  Lean-checked.
- The conditional order threshold does **not** move while 19 is unsettled: it stays at 3249.
- The earlier estimate for this prime was about 500 CPU-h (Criterion SS), with 200–310 GB of witnesses.

**What it does not change:** FIN, ORDER9 and Q36.
