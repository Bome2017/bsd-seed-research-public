# Bounded check and repair of the two overviews

2026-09-29 — **CONFIRMED_WITH_CORRECTIONS.** This is a record and source check, not a fresh proof of the seed results or an exhaustive literature survey.

The stale-record diagnosis is substantially correct. The stronger synthesis “LINE = K288,” the unrestricted assertion that every proved tool works one prime at a time, and the universal claim that nobody has a method are not supported. The accepted U22 Link 2 audit also expressly rejects the claimed necessity of assuming a Selmer upper bound.

## 1. Integrity and the read-only question

The supplied Claude overview manifest passes 12/12, the Fable overview 12/12, and the rank-two screen 68/68. Their pre-edit bytes and manifests are preserved in this review's `before/` directory. Input hashes are in `INPUT_BINDINGS.json`; later inputs and actual edits are recorded separately.

I parsed the two complete Fable transcripts, deduplicating tool-use IDs. The first contains seven shell calls and two file writes. The shell calls create seven listing files in that session's scratch directory; the two file writes are in its output directory. The second contains 36 edits and ten writes, all in its output directory, and no shell calls. No recorded call mutates a protected research folder. `TRANSCRIPT_CHECK.json` retains the call evidence.

Thus **read-only toward the protected inputs** is supported by the transcripts. “Literally no writes” is false, and the first run did write outside its designated output folder, into its scratch directory. That narrow contract exception should remain visible. This is not an operating-system forensic audit of every process. Separately written overviews are corroborating reviews, not two independent proofs of their shared imported mathematics.

## 2. The three requested rank-two exclusions

**Darmon–Rotger: CONFIRMED, at the scope of the cited paper.** In the supplied published text, Conjectures 3.2 and 3.12 contain the rank-two nonvanishing/comparison input; the proved results do not give the requested prime-uniform integral Selmer upper bound for this seed. A rational Selmer dimension statement would moreover establish primary finiteness, not automatically the absence of finite primary torsion. No claim about every later adaptation follows from this check.

**DLR: CONFIRMED_WITH_CORRECTIONS.** Lemma 3.2 gives the vanishing of the specified *scalar* regulator when a constituent has rank at least two. Theorem 3.3 also assumes squarefree combined level, which our seed does not have. Consequently its vanishing conclusion cannot simply be applied to the seed. Darmon–Rotger §4.5.3 distinguishes potentially nonzero enhanced vector regulators from the vanishing scalar regulators in the rank-(2,0) configuration. “No nonzero rank-two regulator/formula even conjecturally” would be false. The configured DLR route still supplies no proved seed upper bound.

**Kudla/theta/shtuka: CONFIRMED_WITH_CORRECTIONS.** Liu–Tian–Xiao–Zhang–Zhu, arXiv:1912.11942v3, Theorem 1.1.1 is already uniform in the coefficient prime: it proves rational Selmer vanishing for almost all coefficient primes for a specified higher-rank tensor motive, under its hypotheses. It is not a theorem about this elliptic curve's integral primary torsion. Theorem 1.1.9 concerns rational Selmer dimension one under a nonzero cycle hypothesis. Li–Liu, arXiv:2006.06139v5, Theorem 1.5 uses a nonzero first derivative and gives a Chow nonvanishing result under its hypotheses; it is not a general theorem that all such Chow groups have rank at most one. Yun–Zhang's higher-derivative formula concerns function fields. No applicable number-field seed transfer is supplied here.

Therefore retain **NO_PROVED_ROUTE_AMONG_SCREENED** for the named applications. Withdraw “every proved tool is one prime at a time” and a blanket rank-at-most-one characterization of this whole literature. The other screened papers were not re-audited in this check. Screening nine published candidates does not exhaust possible geometric constructions from P1 and P2.

Primary sources: [Liu et al.](https://arxiv.org/abs/1912.11942), [Li–Liu](https://arxiv.org/abs/2006.06139), and the supplied source texts `DR16.txt`, `DLR15.txt` and Yun–Zhang in the rank-two screen. Relevant source files are hash-bound in the source ledger. This review uses the theorem statements, not the screen's abstracts as substitutes.

## 3. The two new syntheses

**LINE = K288: REFUTED as an established equivalence; a relationship is confirmed.** The retained LINE Theorem C′ requires a common rational comparison on core pairs at every p-power level. Its core auxiliaries have nontrivial p-power point torsion. The K288 audit instead gives a sufficient mod-p singleton nonvanishing criterion using selected G2 auxiliaries. Finite-quotient mod-p data do not supply LINE's higher-level comparisons or its quantifiers.

The 09-24 T-c proposal of ±9·2^j assumed Sha order 9 and concerned regime-A tests, not LINE core-pair tests. Since 288 = 9·2^5, the observation is compatible with that conditional prediction. It is not independent evidence for the assumption, a proof that the normalizations coincide, or a proof that the two targets are interchangeable. Cross-reference the lanes; do not merge them as equivalent theorems. The exact ℓ-independence proposal remains unproved.

Governing records: `BSD_SEED_2243_12_LINE_HOSTILE_AUDIT_2026-09-19/LINE_HOSTILE_AUDIT.md`, `BSD_LINE_TA_COMPATIBILITY_REVIEW_2026-09-24/INPUT_TA_TB_RESOLUTION.md`, and `BSD_K288_UNIFORMITY_AUDIT_CODEX_2026-09-27/AUDIT.md`.

**U22 toward G1 using G2: CONFIRMED_WITH_CORRECTIONS.** The scalar identities and Galois pairing dictionary are partial ingredients of a possible comparison on ordinary primes split in Q(sqrt(-7)), at their retained grades. G2 itself is the established regulator statement, not the missing gate. A new identity C2 = u det(h), with independently proved unit u and nondegenerate identified classes, could prove the Selmer bound as a conclusion. It need not assume that bound. The retained BKS factorization does not provide such a unit: its compound multiplier includes the uncontrolled Kato coordinate and Sha factor.

The Link 2 audit, `BSD_U22_ENGINE_LINK2_CHECK_CODEX_2026-09-29/REPORT.md`, confirms only insufficiency of the developed mechanisms. It corrects the pseudodeformation argument, the finite-length hypotheses, trace-cycle versus off-diagonal ideals, and the truncated bound e_k >= min(r,k). Keep those corrections. C-primitive, gluing, actual Hecke-class hypotheses, the comparison, nondegeneracy and prime coverage are separate obligations. The present evidence supports a recommendation to stop spending on this construction pending a new relation; this review does not cancel any session or make that user decision.

## 4. Other corrections and retained arithmetic

- The residue 1 modulo 7 on 389a1 cannot distinguish the normalizing factors 1 and 8. The proposed exact power of two is unsupported.
- The CRT proposal is conditional on rationality and a proved normalized comparison with q. It belongs below those missing inputs, not ahead of them in a dependency ranking. It does not prove q=36 from the interval and observed residues alone.
- The K288 analysis has an existing audit. Its uncorrected “entire refined conjecture,” exact auxiliary-independence and necessity claims must not govern current summaries.
- The retained primary conclusions cover all primes through 47: zero except the 3-part (Z/3)^2. For 17,19,23,29, theorem/source review is recorded but the checked overview records do not establish a separate outside audit of their full numerical outputs. The 31,37,41,43,47 outputs have recorded model artifact reviews with replay limits. No independent human review is asserted. The Batch C audit does not rehash/reverify the entire large coefficient corpus.
- Conditional on FIN, the retained square-order argument gives #Sha = 9 or #Sha >= 9*53^2 = 25,281. The common-scalar residue observation is modulo 20,475,850,236,047. Neither statement proves FIN, ORDER9 or Q36.
- The BH quadratic singleton criterion is retained at all three bad primes, including additive 4547, with theta_BH = theta_pipeline/2. It is a sufficient criterion with imported preprint inputs, not an evaluated witness. Its cost screen remains HOLD; no compute is authorized here.
- Keller's recorded lack of awareness and this bounded literature screen support “no applicable global proof was identified here.” They do not establish that nobody has a method. Route rankings are research judgments, not proved cost or possibility comparisons.
- The newer custodian record already marks the H41 seal and Keller reply complete. The pasted pending list is stale. I preserved those updates; I did not audit private email delivery or send anything.

## 5. Repairs and the remaining record limitation

The change ledger lists each actual edit and its before/after hash. Completed launch prompts are preserved as history and removed from the live dispatch surface. The master remains the canonical mathematical account under its existing AGENTS.md rule; PARTS_MAP is its subordinate operational/detail index. A dated supplement brings the checked current state into the master without deleting the older proof dossier. Overview corrections are explicit, with the original bytes preserved, rather than silently rewriting their claimed independent findings. The v0.2.5 material is a **draft outside the release repository**, not an applied release or a publication.

The master freshness checker was already failing before edits: three p=13 bound status/result files differ from their old hashes, and its discovery inventory has grown substantially (206,448 paths in the initial scan). The three p13 differences are now reconciled: current files were read and match the v0.2.4 evidence copies, the release manifest and provenance rows exactly. Their annotations preserve the governing corrected C13=2/1 and prohibit restarting; the older 7/8 values remain explicitly superseded historical data. Only those three external hashes were updated, with old hashes preserved and roles unchanged. See P13_BINDING_RECONCILIATION.json. This does not certify all newly discovered records. **Global archive freshness remains RECONCILIATION_REQUIRED.** Integrity of the present bounded repair is a different claim.

No prime run, full numerical replay, new construction, session cancellation, repository edit, push, publication, memory update or outreach was performed. **FIN, ORDER9 and Q36 remain open.**
