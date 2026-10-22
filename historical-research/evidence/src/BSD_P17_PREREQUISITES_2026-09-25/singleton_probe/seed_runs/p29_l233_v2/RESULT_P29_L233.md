# p = 29 (supersingular), l = 233 (version 2): NONZERO, so Sha(E/ℚ)[29^∞] = 0 (2026-09-26)

**Status.** Computer-assisted 29-primary vanishing (Ota Thm 1.5/6.4, source-audited, including the supersingular case
under audit item 5), supported by:
- a pre-run freeze (`FROZEN_RUN_PACKAGE_p29_l233_v2`, commit 29aabc1; checker byte-identical to the p = 17 freeze);
- the frozen checker's verdict;
- a downstream recomputation.

Outside artifact-level review is outstanding; the evidence branch is local, not pushed.

**History.**
- l = 59 gave INCONCLUSIVE_ZERO (the tame regulator predicted that zero).
- The v1 package for 233 (2f6f053) was superseded before launch, after p19_l191 run 1 failed closed at the same tail
  margin.
- Version 2 uses T = the aligned cutoff with the tail ≤ ¼ of the budget. That needed corpus_ext_4802: 249 segments,
  verified by the repaired verifier, with an acceptance check reproducing seven earlier roots.

**The run.**
- Seed E, p = 29 (a₂₉ = 0, #E(F₂₉) = 30), l = 233 (E(F₂₃₃) ≅ ℤ/248, v₂₉(232) = 1).
- T = 80,564,191,231: 4,802 segments, read through `corpus_ext_4802/view` (read-only).
- Engine sha256 47d07f2e…. From 21:07:27Z to 22:18:03Z: 9.30 CPU-h (33,472 user-s), 70.6 min wall; peak RSS 0.75 GB.

**The verdict** (exit 0: NONZERO, with every binding passing):
- the receipt root c329c118… equals the pinned root;
- PARAMS equals the frozen command;
- the manifest binds the engine and output hashes;
- 232 labels, each exactly once, and **XB_PLUS_DETERMINED 232 of 232**;
- the COUNT identity holds with T;
- the symmetry holds.

**The witness.** With g = 3: c₀ = 0, c₁ = 2320 = 29·80 ≡ 0, and **c₂ = −98942 ≡ 6 (mod 29)**.

The downstream recomputation (same table, separate code) gives the same values, and all symbols are integral. The
generator orbit is 6·(F₂₉ˣ)²; that is a covariance check only.

**A pre-registered value prediction** (diagnostic; the Mazur–Tate refined conjecture with K = 288 fitted on 17 and 23):
- `mt_prescreen/PREDICTION_29_233.md`, sha256 b7641c63…, was written at 21:09:45Z, before the result existed. It
  predicted **c₂ ≡ 6 (mod 29). The certified value is 6.**
- This is the second exact out-of-sample hit, after 19/191 (predicted 6, certified 6).

**What it changes.**
- Sha(E/ℚ)[29^∞] = 0.
- 17, 19, 23 and 29 are now settled, beyond the earlier p ≤ 13 and 2. Conditional on FIN, the next possible order moves
  to **8649 = 9·31²**.
- It does not change FIN, ORDER9 or Q36.
