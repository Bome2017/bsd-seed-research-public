## Addendum 25 (09-30 ~10:30): Codex's uniform synthesis. A real source change: Kurihara witnesses exist at EVERY good p ≥ 5; the target is now "r_p < 4"
- **Files:** `~/BSD_UNIFORM_SYNTHESIS_CODEX_2026-09-30/` (and the .zip for Pro, 26 entries).
- **Verdicts:** SOURCE_UPDATE_APPLIES_AT_RETAINED_INPUT_GRADE; ALL_GOOD_PRIME_KURIHARA_EXISTENCE;
  UNIFORM_LOW_DEPTH_BOUND_STILL_OPEN.
- **Checked by Claude at source** (Claude fetched the PDF: CLW2.pdf, sha256 0686fa414b242e8e…):
  - Castella–Liu–Wan, "Kato's main conjecture for nonordinary modular forms", author-hosted, dated September 21, 2026.
    Theorem A: newform of weight k, p > 2 good nonordinary; (i) 2 ≤ k < p; (ii) either k = 2 and (ram), i.e. some
    ℓ ∥ N with ρ̄ ramified at ℓ, or (rtn); (iii) p-regular.
  - No squarefree hypothesis. For the seed: ℓ = 2243 (v(Δ) = 1, so ramified at every p ≥ 5), k = 2 < p, and a_p = 0 at
    supersingular p gives α ≠ β. Theorem A APPLIES.
  - Castella–Sano arXiv 2601.14504 (v1, not withdrawn), "On refined nonvanishing conjectures by Kurihara and
    Kolyvagin".
- **Codex's chain:**
  - the main conjecture at every good p ≥ 5 (ordinary from the known results; supersingular from the CLW revision),
    plus Castella–Sano, gives a Kurihara quantity nonzero mod p at every good p ≥ 5;
  - plus Kim's higher Fitting theorem (2203.12159 Thm 1.8): r_p = dim Sel_p, even and ≥ 2, and r_p = 2 ⟺
    Sha[p^∞] = 0.
  - So FIN-b ⟺ r_p < 4 for all p outside one finite set.
  - A broader sufficient test (from the BH argument): some order-p character value of the normalized θ with
    λ-depth < 4, with a composite conductor allowed.
- **Status:** coverage improved and the target is exact; NOT a proof. The independent upper bound "< 4" is the open
  core. The application (normalizations, the passage to Castella–Sano, Kim's indices) awaits an independent check:
  Pro, per Codex, or a pre-check by the Fable coordinator.
- **Corrections Codex made to CLAUDE's user overview** (09-30), all accepted:
  - (1) "no method exists for any rank-2 curve" was overstated. Correct: no applicable finite-support theorem was
    located in our screens, and Keller reported knowing none.
  - (2) "with rationality, the interval pins 36" is WRONG. A denominator or height bound is also needed (Q.1: ≤ 174),
    or another exact characterization.
  - (3) The exceptional prime set must be DERIVED from the eventual uniform theorem, not fixed in advance as the five
    named primes.
  - (4) "everything provable prime by prime has been proved" was too strong. More per-prime results remain possible
    (53, 59, 487; the bad primes via BH); they simply do not settle FIN.

