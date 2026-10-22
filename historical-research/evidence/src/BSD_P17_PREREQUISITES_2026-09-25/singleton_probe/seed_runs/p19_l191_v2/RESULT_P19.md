# p = 19, l = 191 (version 2): NONZERO, so Sha(E/ℚ)[19^∞] = 0 (2026-09-26)

**Status.** Computer-assisted 19-primary vanishing (Ota Thm 1.5/6.4, source-audited; 19 is good ordinary), supported
by:
- a pre-run freeze (`FROZEN_RUN_PACKAGE_p19_l191_v2`, commit 2dd268d; checker byte-identical to the p = 17 freeze);
- the frozen checker's verdict;
- a downstream recomputation.

Outside artifact-level review is outstanding; the evidence branch is local, not pushed.

**History, stated plainly.** Run 1 (package f587b88, T = 62,360,911,871) returned **INVALID**.
- It was a fail-closed identification margin: `arb_div` inflation at |symbol| ≳ 140.
- It is diagnosed and sealed in `../p19_l191/RESULT_P19_RUN1_INVALID.md`, with the probe in `margin_probe/`. No value was
  taken from it.
- Version 2 changes only T, by a stated rule: the aligned cutoff with the tail ≤ ¼ of the identification budget. The
  engine, checker, lattice and acceptance rules are unchanged.

**The run.**
- Seed E, p = 19 (a₁₉ = 4, #E(F₁₉) = 16), l = 191 (E(F₁₉₁) ≅ ℤ/202, v₁₉(190) = 1).
- T = 65,783,463,935: 3,921 segments of the extended corpus, read through `corpus_ext_4553/view` (read-only).
  - Segments 3281..3920 are new. They were produced by the certified apwit and verified by the repaired verifier, with
    a witness structure scan.
  - The corpus acceptance (`CORPUS_CHECK_4553.json`) reproduced the four earlier pinned roots.
- Engine sha256 47d07f2e…. From 20:00:38Z to 21:07:14Z: 8.69 CPU-h (31,277 user-s), with a concurrent Stage W for
  about 47 min; peak RSS 0.68 GB.

**The verdict** (exit 0: NONZERO, with every binding passing):
- the receipt root 58d28b37… equals the pinned root;
- PARAMS equals the frozen command;
- the manifest binds the engine and output hashes;
- 190 labels, each exactly once, and **XB_PLUS_DETERMINED 190 of 190**;
- the COUNT identity holds with T;
- the symmetry holds.

**The witness.** With g = 19 (the smallest primitive root mod 191): c₀ = 0, c₁ = −3572 = −19·188 ≡ 0, and
**c₂ = −30432 ≡ 6 (mod 19)**.

The downstream recomputation (main session, same table, separate code; `DOWNSTREAM_RECOMPUTE_MAIN.json`) gives the
same values, and all symbols are integral. The generator orbit is 6·(F₁₉ˣ)²; that is a covariance check, not symbol
certification.

**An out-of-sample check (diagnostic, conjecture-based; not part of the certificate).**
- The Mazur–Tate tame-regulator relation c₂ ≡ −#E(F_l)·K·det H(E) (mod p) uses K = 288, fitted on p = 17 and 23 before
  this run, and det H(M·E) = 2 with M = 202, recorded in `mt_prescreen/candidates.out` at 16:00Z.
- It predicts c₂ ≡ −202·288·3 ≡ 6 (mod 19). **That equals the certified value.**
- The pre-screen had also predicted nonzero (det ≢ 0).

**What it changes.**
- Sha(E/ℚ)[19^∞] = 0.
- 17, 19 and 23 are now settled beyond p ≤ 13. Conditional on FIN, the next possible order moves from **3249 to
  7569 = 9·29²** while 29 is open, and to 8649 = 9·31² if 29/233 v2 is NONZERO.
- It does not change FIN, ORDER9 or Q36.
