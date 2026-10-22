# Contradictions and discrepancies register

Discrepancies recorded by the builder and the first review are listed here, including the ones already resolved. Unresolved items stay visible until they are resolved by an argument; they are never settled by which file is newer. Ids beginning with W refer to the withdrawn register in `CLAIM_INDEX.md` (section B).

## Unresolved

**K.1 — Stein–Wuthrich Theorem 6.1, multiplicative case: the "iff" and its attribution.**
* **The statement.** SW 6.1 says "ord_T f_E = r if and only if the p-adic height is nondegenerate and Sha(p) is finite", crediting the multiplicative case to Jones 1989.
* **What Jones proves.** Jones assumes finiteness of the primary Sha as a standing hypothesis, used even in defining the height. He proves only "nondegenerate ⟹ ρ = r + 1 and the leading-term formula" (Theorem 3.1). His Theorem 2.1 leaves the quasi-isomorphism α conditional (Lemma 2.2).
* **A second attribution.** The same SW paragraph credits Λ-torsion at multiplicative p to Kato 17.4, which Skinner 2016 states excludes p | N.
* **Status.** Unresolved as a literature question.
* **Effect here: none.**
  * S.3 derives finiteness first and uses an independent height certificate.
  * B.6 now does the same: D4 for finiteness, and the D5 certificate of 2026-09-23.
* Evidence: `BSD_2243_EVALUATOR_REVIEW_2026-09-23/dependencies/D2_D5_RECONCILIATION.md`; `BSD_CODEX6_MASTER_HANDOFF_2026-09-19/audits/p3_r1_r2_2026-09-19/R1_R2_THEOREM.md` §2.2; `BSD_2243_D5_INDEPENDENT_2026-09-23/PROOF.md` §7.

**K.2 — The 5843 exceptional zero for the twist E^{-7}.**
* **The dispute.** Four external runs say the split multiplicative reduction of E^{-7} at 5843 defeats the naive Kato bound there. That is contrary to a Sage docstring, which is a secondary source.
* **Status.** Disputed.
* **Effect here: none.** The Cassels–Tate shortcut (B.3) removed any need for the twist's Sha support.
* Evidence: `BSD_C2_WITNESS_2026-09-22/CATCHUP_GRADING_2026-09-22.md`, item 3.

**K.3 — Custody of the external C13 run record.**
* **The discrepancy.** `BSD_SEED_P13_RUN_2026-09-21/SUPERSEDED_BY_NORMALIZATION.md` says `RESULT.json` and `STATE.json` are "preserved unedited". In fact all three of `RESULT.json`, `STATE.json` and `RESUME.md` changed after the master bound their hashes:
  * `RESULT.json` gained a `SUPERSEDED` key.
  * `RESUME.md` gained a "SUPERSEDED 2026-09-22" section.
  * `STATE.json` had its `status` field overwritten and a `superseded_by` field added.
* **Why the master check flags it.** The master's checker reports these three files as changed bound sources.
* **Current qualified effect.** Nine calculation-input bindings, including both symbol tables and Arb outputs, match the pre-change completion record. The current downstream replay does not read the three changed metadata files. The theorem retains that separate arithmetic chain and its original trust qualifications; the historical metadata are not certified intact. See `review/followup_logs/c13_custody_reconciliation.json` and the verifier appendix.
* **Pending.** The master's reconciliation, which needs the user's authorization. The original STATE `status` value is recoverable only if a pre-change copy exists; none was located in this build.

**K.4 — The master record is behind the research.**
* **The discrepancy.** `verify_master.py` returns RECONCILIATION_REQUIRED.
  * Master §3 still lists 2243 as having "no completed certificates; split case also needs its stated nonzero L-invariant input".
  * It does not yet contain D=-7 (K.2), the ordinary lane (B.3), A3 (B.4), the 2243 dependency results (B.6: D2 discharged, D5 certified, ℓ_γ = 1799) or the compression obstruction (X.15).
* **How this release handles it.** It integrates those records as a derived export, marked "since master" in the index.
* **Scope correction.** The master is intentionally read-only and later records supersede additively. Its age is not a mathematical defect or a reason to modify it. This derived release incorporates the later records at their recorded grades.

**K.5 — Grade of the 2243 evaluator defect F4.**
* The cross-family review grades restart isolation FAIL; the same-family fresh reviewer grades the same defect "major".
* Both agree on the defect and on the fact that no false arithmetic result was shown.
* The fix is proposed but not applied.

**K.6 — Which proof of the ordinary bridge is canonical.**
* **Two proofs.**
  * The frozen record's route: Bertolini–Darmon derived heights, the Cassels–Tate shortcut and the D=-7 certificate. Several of its steps have not been replayed by the project.
  * The A3 argument, which also runs at ordinary p and bypasses those steps. Its algebraic core is Lean-checked.
* **What the records say.** "Recorded, not substituted", pending the user's decision.
* This is not a mathematical contradiction. The manuscript presents both proofs and states which one the records treat as canonical.

## Resolved (kept visible)

**K.7 — `FRONTIER.md` contradicts itself.**
* Lines 111–112 claim a certified good specialization at 13; line 125 calls the comparison at 13 open.
* Resolved by `CORRECTION_2026-09-22_I3_AT_13.md`: the claim is withdrawn (W.1). The frozen file is preserved unedited.

**K.8 — The 3-primary theorem's two wordings.**
* The original step 4 of `SHA3_THEOREM.md` invokes the equality clause of SW 6.1 at the multiplicative prime 3.
* The governing R1 addendum instead derives finiteness first and uses an independent nondegenerate-height certificate. It says explicitly: "No converse to Jones's conditional theorem is being silently imported."
* The R1 chain governs, as the master records.

**K.9 — A Manin-constant bound at 7 for E^{-7}.**
* A secondary characterization (Agashe–Ribet–Stein §2) says Edixhoven gives bounds at 2, 3, 5 and 7. The thesis itself calls such bounds a problem that "should also be tried".
* Resolved: the bound is not established (V7_MANIN_BOUND_OPEN). The question is off the critical path.

**K.10 — The arrow-orientation rule.**
* The 2026-09-20 invention packet ships the rule "wrong direction" (`KILLED_ROUTES.md`, `KNOWN_TRAPS.md`).
* It is withdrawn by `FRONTIER.md` §4 (W.2). The packet must not be reissued without that correction.

**K.11 — Older status wording for p = 3.**
* `SEED_PROVED_STATE.md` (a frozen 2026-09-19 snapshot) lists R1/R2 as "carried, not closed".
* The master supersedes it: R1 passes; R2's μ-transfer is rejected; the theorem is retained via Skinner Theorem A as published, with internal SU provenance open.

**K.12 — The blind twist-Sha experiment was compromised.**
* The blind arm's root `STATE.json` leaked the predicted value, so the aware/blind pair cannot measure anchoring.
* Both arms' conclusions are recorded, and the experiment is off the critical path.

**K.13 — `C13 = 7 or 8` against `C13 = 2`.**
* Resolved by the normalization reconciliation (W.3). Nonvanishing was invariant under the error.

## First-review corrections (2026-09-23)

**K.14 — Coefficient-verifier distinct factors.** The old C verifier accepts a false coefficient at 4099 on the seed because factor primes need not be distinct. The repair and exact positive/negative regression are in `review/repairs/` and `tools/replay/coefficient_verifier_regression.py`. A supplemental hash-bound check of all 3,757 retained witness files passed the missing conditions. This did not rerun their group arithmetic and did not show a wrong retained coefficient. See `review/FIRST_REVIEW.md`.

**K.15 — Basis evidence and missing 3-adic height code.** The cited preprint and bounded saturation did not alone establish the full displayed integral basis. The older global index-bound/saturation certificate was found, restored and successfully replayed. The independent 3-adic formal-height code was also restored and replayed for its required valuation. These were packaging/attribution defects, not newly proved gaps in rank or the 3-primary arithmetic.

**K.16 — Mathematical wording.** Corrected: finite Iwasawa lambda versus finite mod-p order; the false assurance that rounding detects a wrong two-power lattice; the rational-cusp scope of the symbol lattice; exact L-invariant and global-height normalizations; FIN plus ORDER9 in the uniform-bound equivalence; overly broad enumeration/impossibility and stopped-route claims. The frozen source files remain historical evidence rather than silently corrected originals.

**K.17 — Release checking and privacy.** Generated-spec drift, dependency cycles and stale success output are now rejected. The synthesis brief now includes the normalization and verification fields. The paper remains separately authored and needs semantic review. Private identifiers were removed from the builder code but remain in original Git history, so the reviewed archive is history-free.

**K.18 — Paper-only review, accepted corrections.** The source derivations for the Manin bound and A3 were omitted from the manuscript, not absent from the evidence. The new proof appendices expose them and the verifier preservation argument. The Arb wording, 27/81 symbol inventory, p=5 exception, D8 classification, period and point notation, and FIN quantifiers are corrected. Historical under-specified exclusion summaries are Research records. See `review/PRO_REVIEW_RESPONSE.md`.

**K.19 — Lattice-margin and local-check script.** The nine-power margin belonged to an older 17-versus-8 target; it does not apply to the current 1/1024 lattice. The historical checker printed failures without nonzero exit; a new fail-closed checker and negative control replace its execution role.

**K.20 — Nested archive privacy.** A redundant twice-nested archive retained a private identifier. It is excluded with content coverage documented; the recursive builder check is repaired. Earlier archives are not suitable for sharing.
