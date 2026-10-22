# v0.2.6 (local, unreleased): the Kurihara position

This revision preserves v0.2.5 with its route-K and K2 follow-ons (local commit `4344c6a`, the same commit as the
GitHub branch `v0.2.5`). It records one source-backed position: a mod-p unit Kurihara witness exists at every good
prime p ≥ 5, its minimal length is the Selmer dimension, and a character-depth test is sufficient. It proves no uniform
bound. No statement, grade or certificate of v0.2.5 is changed except as listed. The governing scope is
`evidence/src/BSD_SEED_V026_BANK_TASK_2026-09-30/inputs/V026_SCOPE.md`, as revised after the cross-model check and
Codex's check of it (`…/inputs/CODEX_THREE_BRIEFS_REVIEW_REPORT.md`, CONFIRMED_WITH_CORRECTIONS).

1. **B.20 (THEOREM; PROVED_WRITTEN, IMPORTED_PREPRINT; Research record `thm:kurexist`).** For every prime p ≥ 5 of good
   reduction for E, including the supersingular primes and 19, 59 and 487, M_∞(δ) = 0. Hence some squarefree Kato
   conductor n, which may depend on p, gives a mod-p unit Kurihara witness. The bad primes 2243, 4547 and 5843 and the
   primes p ≤ 3 are not covered.
   - Supersingular primes: Castella–Liu–Wan, "Kato's main conjecture for nonordinary modular forms", author-hosted
     revision dated 2026-09-21, Theorem A. (ram) holds via ℓ = 2243 (v₂₂₄₃(Δ) = 1, split I₁); k = 2 < p; p-regular
     since a_p = 0. The arXiv v1 required squarefree N; the revision does not. Then Castella–Sano (arXiv:2601.14504v1)
     Theorem A and Corollary A, with Tam = 16 and c_φ | 2⁹ prime to p.
   - **Version caveat.** The revision is author-hosted and not on arXiv as of 2026-09-30. arXiv 2608.29470 lists only
     v1, the squarefree-level version (checked live on 2026-09-30). The revision is pinned by sha256
     0686fa414b242e8e3b1cccd3fe906c8eefcfdb7b568563daa3089701d036fb98. A later version could change the hypotheses of
     Theorem A.
   - **Ordinary coverage.** Castella–Sano Theorem B as printed; its hypotheses are p > 3, (sur) and p ∤ c_φ, and its
     proof cites [Wan15, BCS25] for the ordinary main conjecture. 19, 59 and 487 are ordinary: a₁₉ = 4, a₅₉ = −4,
     a₄₈₇ = −28, re-derived here with PARI 2.17.3 `ellap`
     (`evidence/src/BSD_SEED_V026_BANK_RETURN_OPUS_2026-09-30/checks/seed_local_facts.{gp,log}`, which also gives
     Tam = 16, w = +1, v₂₂₄₃(Δ) = 1 with type I₁, 2242 = 2·19·59 and 5844 = 12·487). Theorem B has no hypothesis that
     excludes them. The Euler factors at 2243 and 5843 are nonunits at these primes; both formulations retain them and
     neither cancels them, so they create no extra exception. The supersingular primes come from the CLW revision,
     because Theorem B's supersingular case requires squarefree N.
2. **B.21 (THEOREM; PROVED_WRITTEN, IMPORTED_PREPRINT; `thm:rp`).** With r_p := min{ν(n) : δ_n ≢ 0 (mod p)}, for every
   good p ≥ 5: r_p = dim_{F_p} Sel_p(E/Q), even and ≥ 2, and r_p = 2 ⟺ Sha(E/Q)[p^∞] = 0. It uses only the
   Sha-independent clauses of Kim's Theorem 1.8 (arXiv:2203.12159v6), parity, the split dual Kummer sequence and
   Nakayama; no finiteness of Sha is assumed. The mandatory scope sentence is in the claim and in §9.1 of the paper:
   "This is an identity, not an upper bound. …"
3. **B.22 (CONDITIONAL; PROVED_WRITTEN, IMPORTED_PREPRINT; `thm:depth`).** For good p ≥ 5, a real cyclic degree-p K/Q
   with actual conductor m prime to pN (composite allowed) and a faithful χ: v_{ζ_p−1}(χ(θ_K^MT)) < 4 for the full
   Bullach–Honnor-normalized element (Def. 2.2, Ω⁺ = 2ω₁) implies Sha(E/Q)[p^∞] = 0. The inequality is strict (the
   "≤ 4" group-ring countermodel is recorded). It is sufficient only: no converse is claimed. The element is at the
   actual conductor; an enlarged conductor needs the norm relations (BH Prop. 2.4) with their Euler factors.
4. **The current known frontier** (claim O.1, paper §11, README), verbatim from the scope:

   > Find one finite set S containing {2,3,2243,4547,5843} and an independent argument that, for every p outside S, either a two-prime mod-p unit Kurihara witness exists or dim_{F_p} Sel_p(E/Q) ≤ 3. Under B.21 these two conditions are equivalent to each other and to Sha[p^∞]=0. A faithful value of the full BH-normalized element of a real cyclic degree-p field at its actual conductor prime to pN, with depth strictly below four, is another sufficient condition. No converse from Sha vanishing to existence of that character value is claimed. Fields, conductors and estimates may depend on p.

   No applicable theorem was located in the screened sources. The watch item of the v0.2.5 candidate edits
   (`BSD_BUILD_MAP/V025_CANDIDATE_EDITS_2026-09-29.md` §6: applicability of Castella–Liu–Wan at this non-squarefree
   level) is RESOLVED, as an applicability and version issue, by B.20. That file is outside the release and was not
   edited. The uniform upper-bound task remains OPEN.
5. **O.1 and O.2 wording refreshed** (grades and statements unchanged): the remaining regimes are the good primes
   p ≥ 53 and the bad primes (the primes p ≤ 47 are settled), and, given FIN, #Sha < 25,281 suffices. §11 of the paper
   now also says 25281 in place of 2601 for the conditional ORDER9 sufficiency.

**Review label** (verbatim in `verification.review_label` of B.20, B.21 and B.22):

> Derived by Codex (OpenAI). Independent review by ChatGPT Pro (OpenAI): ACCEPT_AT_IMPORT_GRADE. The source statements were checked by Claude Opus 5.5 and Claude Fable 5.1 (Anthropic); the Δ-component bridge by Claude Fable 5.1; the Part B deductions by Claude Opus 5.5. The author-hosted CLW revision is byte-identical across three independent downloads (sha256 0686fa41…d036fb98); arXiv v1 is a different file. Not a human review; not formalized.

The records that support it are released and bound:
- the Codex synthesis;
- the ChatGPT Pro review;
- the Codex return check with its fresh download (`FRESH_SOURCE.json`);
- the source-statement and Δ-component bridge check (reduction sheet §9, byte-identical, sha256 e9268897…746ec5707);
- the Claude check report (addenda 25 and 28), with the task-supplied copies of both addenda.

The retrieval records name the pinned synthesis copy (`SOURCE_BINDINGS.json`), the fresh download (`FRESH_SOURCE.json`),
the Fable download (sheet §9a) and Claude's fetch (addendum 28); each has the same sha256. Repeated byte-identical
downloads verify source identity, not independent proofs. The paper and README carry the mathematical grades, the
source citations and a one-line provenance clause: "derived by Codex (OpenAI) and independently reviewed by ChatGPT Pro
(OpenAI), with source and deduction checks by Claude models (Anthropic); not a human review; not formalized".

**Evidence.**
- 38 files appended byte-identical through `tools/build_evidence_transition.py` (`review/V026_EVIDENCE_ADDITIONS.json`;
  log `review/V026_EVIDENCE_TRANSITION.json`; baseline tables under `review/history/v0.2.5k2/evidence/`):
  - the Codex synthesis (13 own files);
  - the ChatGPT Pro review (12 own files and its `source_checks/anchors.json`);
  - the Codex return check (4 own files);
  - the reduction sheet;
  - the Claude check report;
  - four task inputs;
  - the PARI re-derivation (2 files).
- Third-party material is bound by path and sha256 only, in `review/V026_APPLIED.json` → governing_files, and is not
  redistributed. This covers 29 files: the synthesis's `sources/` (14 paper copies and text extractions), the return
  check's `CLW2_fresh.{pdf,txt,png}` (3), and the review's `source_checks/*.png` (12).
- All 3,559 earlier rows, 36,076 exclusions and 6 redactions are preserved, with the same five retained source changes.

**Bindings and checks.**
- The record is `review/V026_APPLIED.json`. The earlier records (`V025_BANK_APPLIED`, `V025K_ROUTEK_APPLIED`,
  `V025K2_APPLIED`) are unchanged.
- `tools/verify_patch_release.py` delegates to `tools/verify_v026_transition.py`. It reconstructs the `4344c6a` tree
  exactly and runs that tree's checker unchanged (K2, then route K, v0.2.5, and so on back). It then checks the v0.2.6
  delta exactly, including an allowed set of changed files fixed in the checker. The semantic bounds are also fixed in
  the checker:
  - B.20 coverage: every good p ≥ 5, with no exclusion of 19, 59 or 487, no restriction to ordinary primes, and no
    claim at p ≤ 3 or at a bad prime; the universal phrase alone is accepted;
  - the version caveat and the ordinary-coverage explanation;
  - "mod-p unit", not merely nonzero;
  - the strict "< 4";
  - the actual conductor;
  - B.22 sufficient only;
  - the verbatim review label;
  - the governing files, including the 29 hash-only ones;
  - outward scans for "only/all that remains", "no method exists" wording, and assertions that FIN, finite support or
    a uniform bound has been proved. Stated open targets and conditional implications are accepted.

Its `--negative-controls` are listed in the return; every corruption fails and the positive controls pass.

**Open.** FIN, ORDER9 and Q36 remain open.
