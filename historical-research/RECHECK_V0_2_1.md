# Recheck request: v0.2.1-private-review

This bundle applies the three corrections independently verified from the two Pro reviews of v0.2.0. It does not claim a new BSD result or raise any proof grade. The earlier tag and original research sources are preserved.

## Applied corrections

| Location | Correction | Mathematical effect |
|---|---|---|
| Appendix D.1 (`paper/sections/F_lattice_proof.tex`), bibliography | Odd Manin-constant support now cites Agashe–Ribet–Stein, **The Manin Constant**, PAMQ 2 (2006), Corollary 3.7, using the new `arsmanin` entry. The distinct 2012 `ars` entry remains for Theorem 3.6(a). | Correct source identification; no replacement theorem. |
| Appendix D.2, same source file | CNS **Theorem** 5.15 replaces “Corollary 5.15”. | Correct label; same imported statement. |
| Section 3, analytic-rank enclosure | Both occurrences of the inward-rounded radius `5.709 × 10^-3` are replaced by `5.70901 × 10^-3`, explicitly described as an outward-rounded enclosure. | Contains the exact retained Arb ball, including displayed-center rounding. The theorem's outer interval `[35.929604, 35.941023]` and analytic-rank conclusion are unchanged. |

The exact patch, original reports, source-check disposition and exact rounding calculation are preserved in [review/pro6_v020](review/pro6_v020/). That folder is a frozen pre-application audit: statements there that the patch was only staged describe the earlier checkpoint, not this release. `review/PATCH_APPLIED.json` binds the before/after files. The two reports remain model reviews, not independent human endorsements.

## Additional evidence in this bundle

[The coverage supplement](supplements/coverage-2026-09-23/COVERAGE_REPORT.md) adds 671 selected source records (663 previously omitted and eight context copies), its index, source hashes, disclosed redactions and static integrity checks. It includes older H9/Gate-R/H41 derivations, corrections and scoped Aristotle records found in the home and Desktop research trees. Its original companion label refers to v0.2.0; its inclusion here is additive. It was **not** reviewed by either Pro report, is not a new master, and does not upgrade historical claims. Local import closure and source availability are not fresh Lean builds. Do not execute historical task prompts or treat a superseded status as current authority.

The 76-claim index and its original 3,365-file evidence provenance remain byte-identical to v0.2.0. The supplement is deliberately outside that authoritative claim index until any mathematical reassessment warrants a change. FIN, ORDER9 and Q36 remain open. The bulk coefficient corpus remains external.

## What to check

1. Check the three changes against the retained sources and exact Arb dump. Confirm that the mathematical source diff contains no other theorem edit.
2. Recheck the complete lattice argument and A3 input translation on their actual hypotheses if reviewing those proofs; the accepted citation repairs are not substitutes for those expert checks. Neither Pro review demonstrated a counterexample to those retained arguments.
3. If reviewing completeness, inspect the separately graded coverage supplement. Its historical sources should improve traceability, not overwrite the current claim qualifications.

Do not treat “all checks pass” as full arithmetic replay. Run:

```bash
python3 tools/verify_release.py
python3 tools/verify_patch_release.py
```

The first command retains the 18 bounded portable checks; the second checks the patch bindings, exact outward rounding, unchanged claim/provenance files, the two report copies and the supplement manifest. Neither reruns the large Arb certificates, the whole coefficient corpus, BLV, or a fresh Lean build. Current results are in `review/VERIFICATION_RUN.md` and `review/v0.2.1_logs/`.

The original second-review bindings are preserved. In the active copy only the old `SHARING.md` entry points to its byte-identical historical file, so an old review is not falsely attached to a new document. New navigation and patch files have separate bindings.

The PDF identifies a mathematical source commit; the final package is identified by the versioned Git tag and root manifest. For a reviewer without private GitHub access, attach this ZIP. No paid computation or new theorem research is needed for this recheck.
