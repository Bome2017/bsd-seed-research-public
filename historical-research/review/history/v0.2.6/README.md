# A rank-two elliptic curve: certified arithmetic, conditional criteria, and the remaining BSD obligations

**Private review version 0.2.6 (local, unreleased; 2026-09-30), built on version 0.2.2 (2026-09-23).** Version 0.2.3 added the A4 formal check of the finite part; version 0.2.4 replaced the rank and 2-descent preprint import by an exact descent certificate and added the A5 formal check at p = 3; version 0.2.5 added the primary components at 17 ≤ p ≤ 47, finiteness and a lower bound at p = 3 without the main conjecture, a bad-prime criterion and three research records; version 0.2.6 adds three research records on Kurihara witnesses at every good prime (see `RECHECK_V0_2_3.md`, `RECHECK_V0_2_4.md`, `RECHECK_V0_2_5.md` and `RECHECK_V0_2_6.md`). A private research release, in three connected parts:
* a manuscript;
* an evidence repository;
* a claim-to-evidence index.

The v0.2.2 editorial revision is described in [RECHECK_V0_2_2.md](RECHECK_V0_2_2.md). It restores the correct Bertolini–Darmon issue/pages and defines the first-layer variable explicitly. Earlier review reports and the separately graded coverage supplement remain preserved. v0.2.2 left claim grades unchanged; v0.2.3 and v0.2.4 change them only as their recheck notes record.

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
| **Proved** | E(Q) = Z/2 + Z P1 + Z P2 with an explicit basis; rank = analytic rank = 2 | exact 2-descent computed by two independent implementations, plus replayed global saturation for the displayed basis; computer-assisted L''(E,1) certificate |
| **Proved** | q = L''(E,1)/(2 Ω_E Reg) lies in (35.99427, 36.00573) | computer-assisted |
| **Proved** | Sha[p^∞] = 0 for p = 2, 5, 7, 11, 13; Sha[3^∞] ≅ (Z/3)^2 | exact computation at p = 2; at p = 5, 7, 11, 13 computer-assisted, with published theorems applied (Kato), and the deductions Lean-checked; at p = 3 see the next row, with Skinner's theorem, as printed, as a second route (two steps of its printed proof are not established for this curve; that deduction is Lean-checked) |
| **Proved** | Sha[3^∞] ≅ (Z/3)^2 without any main conjecture (route K) | written derivation (Kato's Euler system with an integral Coleman map at 3, Jones's leading-term theorem, the height and coefficient certificates), read by three Anthropic model readers and in one cross-family source reading (Codex, OpenAI) at the retained input grades; not a full certificate replay; no human review; with an exact 3-covering certificate for Sha[3] ⊇ (Z/3)^2 |
| **Proved** | Sha[p^∞] = 0 for 17 ≤ p ≤ 47 | computer-assisted singleton certificates; a theorem of Ota applied as stated in its arXiv version; model audits only (same-family at 17–29) |
| **Proved** | full BSD(E) ⟺ (Sha finite of order 9) and (q = 36) | elementary |
| **Conditional** | every good p ≥ 5, p ∤ 7N: M_2(p) ≠ 0 ⟹ Sha[p^∞] = 0 | written proof; supersingular algebraic core Lean-checked; **M_2 is open at every prime** |
| **Conditional** | 2243: K ≢ 0 (mod 2243) ⟹ Sha[2243^∞] = 0; no additional theorem prerequisite was identified at the retained dependency grade; D5 is supplied | **K is not computed** (about 1e5 core-hours) |
| **Conditional** | p = 2243, 4547, 5843: a singleton coefficient C_2 ≢ 0 (mod p) ⟹ Sha[p^∞] = 0 | written corollary of a preprint theorem; **no coefficient evaluated**; modeled at 2.4e4–7.4e4 core-hours |
| **Proved** | every good p ≥ 5 (the supersingular primes and 19, 59, 487 included; 2243, 4547, 5843 and p ≤ 3 not covered): a mod-p unit Kurihara witness exists, and its minimal length r_p equals dim Sel_p(E/Q), so r_p = 2 ⟺ Sha[p^∞] = 0 | written application of preprint theorems (Castella–Liu–Wan, author-hosted revision of 2026-09-21, Theorem A; Castella–Sano; C.-H. Kim), derived by Codex (OpenAI) and independently reviewed by ChatGPT Pro (OpenAI), with source and deduction checks by Claude models (Anthropic); not a human review; not formalized; **no bound on r_p** |
| **Conditional** | good p ≥ 5, K/Q real cyclic of degree p with actual conductor prime to pN, χ faithful: depth v(χ(θ_K)) < 4 ⟹ Sha[p^∞] = 0 | written deduction from a preprint theorem (Bullach–Honnor) and the previous row, with the same provenance; **no value computed; no converse claimed** |
| **Open** | FIN (Sha finite), ORDER9 (#Sha = 9), Q36 (q = 36) | — |

**Current known frontier (the uniform step).** Find one finite set S containing {2,3,2243,4547,5843} and an independent argument that, for every p outside S, either a two-prime mod-p unit Kurihara witness exists or dim_{F_p} Sel_p(E/Q) ≤ 3. Under B.21 these two conditions are equivalent to each other and to Sha[p^∞]=0. A faithful value of the full BH-normalized element of a real cyclic degree-p field at its actual conductor prime to pN, with depth strictly below four, is another sufficient condition. No converse from Sha vanishing to existence of that character value is claimed. Fields, conductors and estimates may depend on p. No applicable theorem was located in the screened sources.

No statement has had independent human review. The claim index records, for each statement:
* which reviews were automated (language-model) reviews;
* what was replayed;
* what was only read.

## Layout

| path | contents |
|---|---|
| `paper/` | the manuscript: `seed_bsd.tex` with its `sections/` and `refs.bib`; the built `seed_bsd.pdf` |
| `claims/CLAIM_INDEX.md` | **the claim-to-evidence index.** 87 claims, each with its statement, kind, grades, imports, normalization, verification, qualifications and hashed evidence. It is generated from `claims/spec/`. |
| `claims/LABELS.md` | the grade, kind, stop and review vocabulary |
| `claims/CONTRADICTIONS.md` | every discrepancy, resolved or not |
| `claims/CROSS_CONNECTIONS.md` | what the whole record shows: shared dependencies, a map of which witnesses can be evaluated, and similar requirements whose arithmetic identification has not been proved |
| `evidence/src/` | 3,597 research records (including 116 restored during the first review, six follow-up audit records and the records appended by later revisions, with one redundant privacy-leaking archive excluded), copied byte-for-byte from the originating machine (6 masked; see below) |
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
* it contains that record unchanged, as integrated on 2026-09-21; five of its files were later edited in place at their source, and the release keeps the integrated copies byte for byte, recording the current source hashes in `review/V025_RETAINED_SOURCE_CHANGES.json`;
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
