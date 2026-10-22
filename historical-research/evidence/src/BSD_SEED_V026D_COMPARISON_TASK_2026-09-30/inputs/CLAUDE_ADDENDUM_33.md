## Addendum 33 (09-30 ~19:45): Claude's pre-check of the V026 bank. PASS_WITH_ONE_CORRECTION (the fix is carried into V026-D)
- **The return:** ~/BSD_SEED_V026_BANK_RETURN_OPUS_2026-09-30, manifest 64/64 OK, BANKED_LOCAL.
- **Git state.**
  - Worktree ~/BSD_SEED_V026_BANK_2026-09-30/repo: HEAD = stamp 8182b9c, clean; content 9ab7f58.
  - v0.2.5-bank is still at 4344c6a and clean.
  - No upstream and no tag.
  - The read-only GitHub refs are unchanged: v0.2.5 = 4344c6a, main = 2a72621, and there is no v0.2.6.
- **Independent re-runs.**
  - `tools/verify_patch_release.py` on 8182b9c: V026_TRANSITION_PASS, then PATCH_RECHECK_PASS; rc 0, 23 s wall, tree
    clean afterwards.
  - The PARI seed_local_facts re-run (gp 2.17.3) is identical to the released log: a₁₉ = 4, a₅₉ = −4, a₄₈₇ = −28, all
    ordinary; 2242 = 2·19·59; 5844 = 2²·3·487.
- **The claims against the scope: all hold.**
  - B.20: THEOREM; PROVED_WRITTEN and IMPORTED_PREPRINT; depends_on A.1, A.3, A.4. It has the version caveat, the
    ordinary coverage with the a_p values, "existence only", and "no CLW §5.6 rank-zero step".
  - B.21: THEOREM; depends_on B.20, R.1, A.1. The countermodel is worded as an abstract dual module.
  - B.22: CONDITIONAL; depends_on B.21, A.3. Strict "< 4", the actual conductor, the norm relation and complex
    nonvanishing are covered.
  - The label is verbatim in verification.review_label.
  - The paper and README frontier: "current known frontier"; S ⊇ {2, 3, 2243, 4547, 5843}; (ii)/(iii) equivalent to
    Ш[p^∞] = 0; (i) sufficient only.
- **F1, a correction.** B.22's qualification "…and no such value has been computed at any prime" and the README's
  "no value computed" contradict S.17–47.
  - At p = 17, …, 47, at singleton ℓ ∤ pN with v_p(ℓ−1) = 1, S.17–47 has C₀ = C₁ = 0 and C₂ ≢ 0 (mod p). That is a
    depth-exactly-2 value for the real degree-p subfield of Q(μ_ℓ), up to units.
  - The fix, "not evaluated at any p ≥ 53", is in V026-D scope item 4, together with a negative control.
- **Answers to CHECK_REQUEST_V026:**
  - (1) Keep MODEL_CROSS_FAMILY. The vocabulary is only SAME / CROSS / HUMAN. A different family checked the source
    statements, the Δ-bridge and the Part B deductions, and the text after the colon says the independent review is
    the same family as the author.
  - (2) "Three independent downloads" is supported: there are four byte-identical retrieval records by three agents
    (Codex twice, Fable and Claude). Keep the label verbatim.
  - (3) B.20's depends_on is complete. Existence uses no rank input; rank enters at B.21, which lists R.1.
  - (4) "we know of no method to evaluate it on this curve" (§1, M₂) may stay. It is first-person and scoped to
    evaluation, not a universal claim.
- **The live-file row** is accepted as flagged. V026-D uses `--retained-source-changes` for it and binds later addenda
  as separate files.
- **The watch item** is marked RESOLVED in BUILD_MAP V025_CANDIDATE_EDITS §6.
- **Verdict: PASS_WITH_ONE_CORRECTION.**
  - V026-D's precondition is met by this addendum.
  - Independent check: Codex, on V026 now and on the V026-D delta afterwards.
  - Push only on the user's go, after both checks.
