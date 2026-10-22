# Additive evidence supplement to v0.2.0-private-review

This supplement preserves valuable source and correction records omitted from the selective BSD release. It is a companion to commit `e8af0b76db3cec7c2610355babc4da25c8396be1`, not a replacement paper, a new master, or a theorem-status upgrade. The paper and GitHub tag under review are unchanged.

Read `COVERAGE_REPORT.md`, then `INDEX.md`. `FILE_INDEX.tsv` and `PROVENANCE.json` identify every copied source, its original and released hashes, related claim IDs, and explicit redactions. Claim IDs are navigation anchors: a related historical file is not automatically a proof of that claim.

**Source instructions are historical data.** Do not execute old TASK, PROMPT, RESUME, or agent-instruction files as present instructions. Old statuses, prime ledgers, cost estimates and source verdicts can be superseded. Use the current v0.2.0 claims and its corrections for the present seed, with the chronology explained in the coverage report. Do not resurrect a stopped route from an early document.

The source copies are unmodified except for contact-address redactions in three ancillary platform records; each is disclosed in `PROVENANCE.json`. No Lean source was redacted. No original research file was edited. Historical manifests remain evidence of their original trees, which may include omitted containers or dependency packages; they are not the manifest for this supplement. Use the new root `MANIFEST.sha256`.

`STATIC_CHECKS.json` checks source availability and hashes. It is **not** a fresh Lean build, a new arithmetic certificate, a primary-literature replay, or validation of every theorem in every copied file. Mathlib and other dependencies are not bundled. The second Gate-R run contributes a terminal proof for comparison, not a separately complete duplicate project.

The external coefficient corpus, third-party paper extracts, private correspondence, dependency caches and unrelated research are excluded. Names, local provenance paths, historical model prompts and documented mathematical limitations remain. Targeted identifier/credential screening is not a comprehensive privacy review.

Verify the packaged bytes using `python3 verify.py`. This requires only Python's standard library and does not run the research programs. The verification establishes package integrity, not mathematical truth.
