# A rank-two elliptic curve: certified arithmetic, conditional criteria, and the remaining BSD obligations

**Private review version 0.2.3 (local, unreleased; 2026-09-25), built on version 0.2.2 (2026-09-23).** Version 0.2.3 adds only the A4 formal check of the finite part (see `RECHECK_V0_2_3.md`). A private research release, in three connected parts:
* a manuscript;
* an evidence repository;
* a claim-to-evidence index.

For this editorial revision, start with [RECHECK_V0_2_2.md](RECHECK_V0_2_2.md). It restores the correct Bertolini–Darmon issue/pages and defines the first-layer variable explicitly. Earlier review reports and the separately graded coverage supplement remain preserved; claim grades are unchanged.

See [SHARING.md](SHARING.md) for the current private snapshot and access instructions. [Follow-up review](review/SECOND_REVIEW.md) records the lattice-source check and corrections.

First review: [findings and repairs](review/FIRST_REVIEW.md), [claim-by-claim coverage](review/REVIEW_COVERAGE.md), and [reviewed snapshot](review/FIRST_REVIEW_FREEZE.md). The original release and evidence sources were preserved.

It is written so that an expert can answer three questions without reconstructing the research history:
* Are these results correct?
* What remains?
* Does this particular curve offer an advantage for further work?

```
E : y^2 = x^3 - 22735 x^2 + 106272484 x,      N = 2^3 * 3 * 2243 * 4547^2 * 5843 = 6503188012738584
```

## Status in one table

| | statement | grade |
|---|---|---|
| **Proved** | E(Q) = Z/2 + Z P1 + Z P2 with an explicit basis; rank = analytic rank = 2 | preprint rank theorem applied, plus replayed global saturation for the displayed basis; computer-assisted L''(E,1) certificate |
| **Proved** | q = L''(E,1)/(2 Ω_E Reg) lies in (35.99427, 36.00573) | computer-assisted |
| **Proved** | Sha[p^∞] = 0 for p = 2, 5, 7, 11, 13; Sha[3^∞] ≅ (Z/3)^2 | computer-assisted, with published theorems applied (Kato; Skinner, as published) |
| **Proved** | full BSD(E) ⟺ (Sha finite of order 9) and (q = 36) | elementary |
| **Conditional** | every good p ≥ 5, p ∤ 7N: M_2(p) ≠ 0 ⟹ Sha[p^∞] = 0 | written proof; supersingular algebraic core Lean-checked; **M_2 is open at every prime** |
| **Conditional** | 2243: K ≢ 0 (mod 2243) ⟹ Sha[2243^∞] = 0; no additional theorem prerequisite was identified at the retained dependency grade; D5 is supplied | **K is not computed** (about 1e5 core-hours) |
| **Open** | FIN (Sha finite), ORDER9 (#Sha = 9), Q36 (q = 36) | — |

No statement has had independent human review. The claim index records, for each statement:
* which reviews were automated (language-model) reviews;
* what was replayed;
* what was only read.

## Layout

| path | contents |
|---|---|
| `paper/` | the manuscript: `seed_bsd.tex` with its `sections/` and `refs.bib`; the built `seed_bsd.pdf` |
| `claims/CLAIM_INDEX.md` | **the claim-to-evidence index.** 76 claims, each with its statement, kind, grades, imports, normalization, verification, qualifications and hashed evidence. It is generated from `claims/spec/`. |
| `claims/LABELS.md` | the grade, kind, stop and review vocabulary |
| `claims/CONTRADICTIONS.md` | every discrepancy, resolved or not |
| `claims/CROSS_CONNECTIONS.md` | what the whole record shows: shared dependencies, a map of which witnesses can be evaluated, and similar requirements whose arithmetic identification has not been proved |
| `evidence/src/` | 3,365 research records (including 116 restored during the first review and six follow-up audit records, with one redundant privacy-leaking archive excluded), copied byte-for-byte from the originating machine (6 masked; see below) |
| `evidence/PROVENANCE.tsv` | each record's original path and sha256, and its master-binding check |
| `evidence/EXCLUDED.tsv` | every file left out, with the reason |
| `evidence/REDACTIONS.tsv` | the six masked files, with the original and released hashes |
| `data/LARGE_DATA.md` | the coefficient corpora that are not in Git: where they are, how they are pinned, how to regenerate them, and the availability limits |
| `coverage/COVERAGE.md` | what was examined, what was included, and what was not |
| `tools/` | `verify_release.py` (the checks), `replay/` (exact replays), and the generators of the index, coverage and evidence |
| `supplements/coverage-2026-09-23/` | additional historical evidence and corrections; 671 source records, separately graded, with its own provenance and integrity verifier |
| `review/` | the frozen-version record, the audit request, the synthesis brief, decisions for the author, the privacy review, and the verification run |
| `builder/` | the builder's checkpoints |

## Verify

```bash
python3 tools/verify_release.py
python3 tools/verify_patch_release.py
```

This uses the standard library only and takes seconds. It checks:
* every evidence hash;
* the binding of the claim index to the evidence, consistency with its generating specification, and absence of dependency cycles;
* bindings for the review logs and repairs, plus the portable exact counterexample to the old verifier;
* independent exact lattice-local checks and a deliberately failing control;
* the exact replays: curve data; **every certified Mazur–Tate coefficient recomputed from the certified symbol tables by an independent implementation**; the 2243-adic height certificate and its verifier; the exact F_2243 rank computation; and the Atkin–Lehner pairing.

Add `--lean` to rebuild the Lean core. That needs a Lean 4.32.2 + Mathlib v4.32.2 project; set `LEAN_PROJECT` to its path. The large Arb certificates need the coefficient corpus (`data/LARGE_DATA.md`). The first review found and repaired a distinct-prime-factor defect in the legacy coefficient verifier and checked the missing conditions on all retained witness files. This was not a fresh full arithmetic replay; see the review report. Run `python3 tools/replay/coefficient_verifier_regression.py --compile` on macOS to exercise both actual C programs on the counterexample and a genuine control.

## Relationship to the canonical record

The research's canonical mathematical record is `evidence/src/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/MASTER_BSD_DAG.md`, last integrated on 2026-09-21. This release is a **derived export**, not a second map:
* it contains that record unchanged;
* it contains the records created since, each marked "since master" in the index;
* the packaged freshness snapshot reports RECONCILIATION_REQUIRED. Additive supersession is intentional; this does not authorize editing the frozen master. Differences are listed in `coverage/COVERAGE.md` and `claims/CONTRADICTIONS.md` (K.4).

## Not included

* The coefficient corpora and run work units (about 80 GB); see `data/LARGE_DATA.md`.
* Third-party publications; they are cited, and their local hashes are in `EXCLUDED.tsv`.
* Correspondence with named researchers.
* Host telemetry.

In six text files, a private e-mail thread identifier is masked. The first review also removed private identifiers from the redaction script. **This repository was initialized from a history-free reviewed archive. The original local history containing that script is not included.** Names and correspondence paraphrases remain listed in `review/PRIVACY_REVIEW.md`. A deeper scan also found a private identifier in a nested archive; this version excludes that redundant container while retaining its mathematical contents. **Use v0.2.2-private-review for this recheck.** Version 0.2.0 remains preserved as the snapshot the Pro reviewers examined. The user authorized private GitHub sharing of this version; see `SHARING.md`.

All rights reserved. This is a private review copy.

Current paper-only review response: [evidence-based disposition and revisions](review/PRO_REVIEW_RESPONSE.md). The paper now includes the complete retained lattice and A3 arguments and a compositional verifier/custody appendix. This is a provisional research dossier for expert review; no independent human endorsement is claimed.
