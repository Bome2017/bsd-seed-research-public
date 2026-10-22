# BSD release coverage audit — 23 September 2026

**Result: worthwhile supporting mathematics and correction records were missing from the selective export. They are now preserved in this additive supplement. The inspection did not identify an omitted theorem that closes FIN, ORDER9, or Q36 for the current rank-two curve.**

The material is often more substantial than a status summary: detailed descent proofs, complete local Lean source trees, a geometric compatibility theorem, and corrections that narrow earlier claims. This is an evidence-completeness improvement, not a new proof of the open endpoint.

The comparison is against private release **v0.2.0-private-review**, commit `e8af0b76db3cec7c2610355babc4da25c8396be1`. Its paper, claims, evidence and GitHub tag were kept fixed while the independent Pro reviews were running. The supplement does not supersede that paper. Original research folders and the frozen master were read only.

## What was worth recovering

| Release claims | What the release retained | Additional material preserved here | Mathematical significance and boundary |
|---|---|---|---|
| H.5: H9R16-C | Milestone summary and nonclaims | `01_THEOREMS.md`, `02_AUDIT_RECORD.md`, `03_CORRECTIONS_LEDGER.md`, `04_RESIDUAL_CITATIONS.md`, authored derivations and reviews; later H9 scope records | The actual compatible Hom-valued Jacobian point tower, integral transition constant one, and corrected carrier normalization. Retained written/model-reviewed mathematics; it does not establish non-torsion, descent to rational points, or the missing BSD comparison. |
| H.4: Gate-R | Mostly final status records | Local Lean projects for the rank and point-group finiteness assemblies, original replay receipts, formalization boundaries and errata; earlier descent/saturation scope records | Makes the existing recorded formal result inspectable. The finiteness is of the rational-point group for the stated family under Params/H41, not of Sha for the present seed. |
| H.1: Run013/62a1 | Proof ledger and minimization proposition | Models, isogeny orientations, descent derivation, exact sequences, period/BSD bookkeeping, checker, returned Lean source and independent formal audit | Preserves the qualified earlier rank-zero/full-BSD family work. Its published/preprint dependencies and analytic nonvanishing input remain essential. This is a different family from the current rank-two curve. |
| H.2: 66b1 | Theorem and literature-dependent corollary | Detailed derivations, reconciliation, referee comparisons, arithmetic receipts, period and prior-art qualifications | The summary was present; the argument and corrections were under-exported. Preserve the kernel/order and period-factor corrections, and the restricted meaning of review independence. |
| H.3: H41 | Final proof and late addenda | Final errata, source-reading note, referee/delta records and earlier additive scope history | Prevents an old obstruction or source shortcut from being read as the final verdict. The retained source-reading qualification on the Fricke-sign import must not disappear. |
| S.FIN, S.U, W.2; A.3 context | Some final statements and summaries | Latest Aristotle A6/B3 correction records and formal countermodels | Preserves withdrawals of overbroad no-go claims, the localization-kernel distinction, and the difference between a formal group model and arithmetic control of Sha. Historical prime thresholds are not the present ledger. |
| Q.2, X.11, B.1/B.2 and earlier route context | Principal conclusions | Explicit finite-check files and local linked support; earlier scoped verdicts, including RS2 | Helps reconstruct exactly what was checked and why a route stopped. A procedural stop or missing comparison is not a theorem of nonexistence. |

`INDEX.md` gives entry points. `FILE_INDEX.tsv` and `PROVENANCE.json` give all copied paths and navigation anchors. Some records serve more than one group. These anchors do not assert that every file proves every associated claim.

## Corrections that matter to the whole record

**H9 is a positive geometric result with a restricted arithmetic application.** Its omitted theorem file and correction ledger explain the content of the milestone, including the normalization and representation in which compatibility holds. A summary alone makes it too easy either to overlook that mathematics or to promote it beyond what it proves. Later H9 status records and the current release's X.17 remain necessary context.

**Gate-R's two different finiteness statements must stay distinct.** The final formalization addresses actual rational points and their finite generation in the stated family. It is not a formalization of general BSD, the classical cohomological Selmer group, or Sha finiteness. The earlier explicit square-class Selmer object is described in the imported boundaries. The conventional post-descent composition also uses the two isogeny-Selmer conditions together; rank zero by itself does not imply trivial 2-primary Sha.

**Run013 has a genuine proof/export boundary.** The independent formal audit records a successful named build and also a manifest discrepancy. Those are different findings. It further distinguishes the conventional equivalence between the minimized family and the original family from what was formalized in Lean. Both facts belong with the claim; neither is grounds to erase the conventional mathematics or to call it all machine-checked.

**Run014 is mixed research, not another BSD proof tree throughout.** The B and C2 returned assessments address the 62a1 family and its scope; they are preserved with their narrow Lean facts. Other Run014 returns concern a combinatorial game or coding theory and were not imported into BSD. The C2 assessment explicitly distinguishes a qualified strong-BSD family from all twists or all elliptic curves. Its recorded external dependencies remain external.

**The H41 source grade must remain visible.** The final errata/source note records that a load-bearing Fricke sign is taken through the cited Conrad–Stein account while the earlier primary source was not independently read by the author/referees of that record. This audit preserves that qualification; it does not independently settle the cited theorem or reopen H41.

**The Aristotle corrections belong alongside their results.** In particular, an intersection of local images is a quotient by the localization kernel unless injectivity is supplied. An abstract duality countermodel does not prohibit every global construction. The returned corrections explicitly withdraw broader claims. Also, the old 1089/1521 thresholds and an old C11 execution blocker are historical: the current release's fixed-prime results and conditional 2601 threshold govern present status.

## Current material already represented

The source census found the recent fixed-prime, twist, ordinary/signed-bridge, bad-prime feasibility, evaluator and D5 records represented in the release or its documented exclusions. This audit found no omitted *recent* result that changes their current endpoint status. It did not rerun the arithmetic or re-audit the imported main-conjecture theorems.

The three latest supplied Aristotle archives were checked at the authored-text/member level against local material. Their selected substantive Markdown/Lean/configuration records were present locally. One symbol JSON initially appeared unmatched because the census had not hashed that JSON name; a direct follow-up found it byte-identical both locally and in the release. This was a coverage-index limitation, not a lost certificate. Archive-member comparison is not proof replay.

A loose Desktop H5/H6/H9 checkpoint is truncated and historical. The existing successor audit already records that limitation and the corrected-export history. It was inspected for missing leads but not elevated into a governing mathematical source. No cloud-only document was recovered in this task.

## What was checked

- Scoped inventory of **134 relevant roots**, including the home BSD/H9/H41/seed folders, the older Run013/Run014 records and both Desktop outreach trees, including `04_RESEARCH_OBJECTS`.
- **131,454 filesystem entries** enumerated, including dependencies, duplicate containers, logs and unrelated records. This is not a count of mathematical documents read. Selected non-bulk text up to 2 MB was hashed; about 764 MB of text was processed.
- **1,308 candidate result records**, reduced to **569 byte-distinct candidates**, followed by targeted reading of the substantive proof, correction and status records identified above.
- Explicit local file-reference tracing from the 76 release claims: 1,622 already-included incidences, two duplicate-content incidences, and 105 missing-link incidences. Incidences repeat files and include source literature and operational state; they are not 105 missing theorems. Selected substantive local targets were copied. This is not a complete semantic dependency graph.
- **671 source files** staged, approximately **4.69 MB** before ZIP compression. Eight are deliberate context duplicates needed at their relative paths for the local Lean source/configuration trees. Hash checks found no source drift during assembly.
- Static import-path checks for the selected Gate-R finiteness tree, Gate-R rank tree and Run013 minimization tree: respectively **39, 37 and 19 Lean files**, with **no missing local RequestProject imports**. One duplicate terminal module was added after the first check detected its absent relative path. External dependencies are not bundled; no fresh Lean build was run.
- Known private-identifier and credential-pattern screening; three ancillary files have explicitly recorded contact-address redactions. No Lean source was changed. Third-party primary-source extracts and private outreach correspondence were excluded from the supplement.

The initial comparison falsely marked 41 older restored files as changed because it did not fall back from an empty original-hash field to the release hash. Direct byte comparisons resolved all 41 and the census was corrected. This audit does not retain that false change claim.

## Limits and release handling

This was a targeted completeness audit, not a proof of global completeness. It did not read every file end to end, inspect every old nested archive, follow all symlinks, fetch cloud-only files, replay the large coefficient corpus, rebuild Mathlib, or independently verify every imported theorem. A claim that “nothing valuable exists anywhere else” would exceed this work.

No recovered record was found to close FIN, ORDER9, or Q36 for the present curve. That is a finding about the inspected records, not a mathematical impossibility claim. Earlier qualified full-BSD families and geometric/formal results should remain visible as actual prior results with their own hypotheses.

Keep Pro's current review tied to v0.2.0. This supplement can be shared as additional evidence without changing the reviewed paper. A later consolidated revision can include the selected evidence and corrected references after the independent reviews return. No successor theorem project or computation is launched by this report.
