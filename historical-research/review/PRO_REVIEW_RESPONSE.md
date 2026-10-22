# Evidence-based response to the paper-only Pro review

23 September 2026. Governing sharing draft: **0.2.0-private-review**. This response supersedes the unfinished 0.1.2 sharing plan, not any original mathematical evidence. The supplied review concerns the exact 25-page v0.1.1 PDF, SHA-256 `11599b2b022ce9d21ad7cf5a79b8232c7f67c429501212c88abda95166b7e2ab`. Its four-file ZIP passed its manifest; its standard-library arithmetic script was inspected and replayed, with byte-identical output. These are useful checks, not an independent certificate for the large computations.

## Verdict and changes

The review correctly identified omitted derivations, an overbroad custody assurance, and concrete wording/counting errors. It did **not** exhibit a false rank theorem, a failed A3 implication, a wrong retained coefficient, or a contradiction to the lattice bound. Its scope was the paper, without the evidence package. We accept the presentation and evidence-access criticism without treating lack of access as mathematical refutation.

| Review item | Evidence-based disposition |
|---|---|
| I1: missing numerical Manin proof | **Accepted.** The lattice appendix now gives the optimal map, differential-lattice inequalities, intersection estimate yielding eight, isogeny transfer, rational-cusp argument and exact period convention. The corrected historical proof was already present. The geometric imports, including source statements read through CNS, remain expressly identified; this is not a claim that elementary arithmetic checks prove integral-model geometry. |
| I2: A3 only an outline | **Accepted.** The signed-bridge appendix supplies the exact specialization argument, Tor/Nakayama step, sign-twisted equivariant resolution, individual eigenspace comparison and quotient argument. The literal capstone signature is in `proofs/A3_SIGNATURE_AND_INPUTS.md`. Arithmetic applicability remains a source-checked import/written comparison, not Lean-verified. The existing residual-order notation was correct and is preserved. |
| I3: verifier rehabilitation needs a proof | **Accepted.** The verifier appendix states the witness format and soundness argument, the exact restricted preservation claim for the patch, and the remaining software/execution assumptions. We joined all 3,757 scanned files to their retained original acceptance and hash receipts. Included receipt texts make that join portable. No billion-record group-arithmetic replay is claimed. |
| I4: unexplained C13 custody assurance | **Accepted.** Three changed metadata files have explicit old/current hashes. Nine calculation-input bindings remain intact, including both symbol tables and both Arb outputs. The downstream replay does not consume those three metadata files. The theorem retains its computer-assisted grade and trust dependencies; the old execution history is not declared intact. |
| I5: surjectivity exposition | **Accepted.** Added the independently reproduced Frobenius table, the alternate transvection prime when the residual prime is 2243, and the elementary group argument. Prime-isogeny classification and integral lifting remain named imports. |
| I6: rank and saturation | Added `(m,n)=(2243,12)` explicitly. The global saturation bound two, index one, exact scripts and earlier replay log are already present and remain unchanged. This was not a failure of the retained basis proof. |
| I7: undefined historical theorem scopes | **Accepted.** Entries lacking full definitions in the manuscript are now Research records, not standalone exclusion theorems. Full historical records remain linked through the claim index. The continuous-density exclusion is restricted to the representation class actually treated, not every Euler-product identity. |
| I8: literature allegations | **Accepted at the appropriate scope.** The paper now refutes the displayed unrestricted trace inference, without claiming that counterexample alone refutes a named paper under unstated hypotheses. The Jones passage states only the forward direction used, with finiteness first. Skinner's published theorem remains a normal import, not downgraded because an internal reconstruction stopped. Historical source audits remain preserved. |
| I9: exact local corrections | **Accepted.** Arb controls floating-point error; 81 has 54 unit residues and 27 has 18, hence 72 entries per sign across both levels; p=5 is checked separately; omega1/full-period series are distinguished; D8 moves to certificate production; FIN may combine cofinite vanishing with separate finite exceptional components. Gross points and rational basis points now use different symbols. |
| I10: inaccessible repository | Resolved by the user-authorized private GitHub snapshot, with a versioned tag and source-snapshot identification. Private access is still required. A portable check is explicitly distinguished from independent regeneration using external large data. |
| I11: contribution and positioning | The document is a provisional research dossier. It distinguishes applications of existing methods, the high-conductor certificate implementation, the proposed equivariant argument, and archived reformulations. No broad novelty claim or promised mass-compute path to BSD is made. Operational prices and unrelated-curve material are retained outside the main PDF. |

## What has not been established by this revision

The referee's three principal priorities are now inspectable; that does not mean an independent human has approved them. The numerical Manin bound still relies on the specified integral-model geometry. The bridge still relies on its arithmetic comparisons and imported theorems. The coefficient result still combines original execution evidence with a supplemental missing-condition scan. A fresh full numerical implementation was not run. No fixed prime, FIN, ORDER9, or Q36 was newly settled.

The old source records and their inconsistent historical sentences remain byte-preserved. This response, the new proof appendices, the receipt join and the C13 reconciliation are additive/current explanations. They do not erase the old discrepancy or silently regenerate a historical manifest.

## Checkpointed outputs

- `pro_report/`: supplied issue ledger, script, expected output and original manifest.
- `proofs/A3_SIGNATURE_AND_INPUTS.md`: verbatim formal theorem signature.
- `followup_logs/corpus_acceptance_receipts.json`: complete original-receipt transcription and scan joins.
- `followup_logs/c13_custody_reconciliation.json`: three mismatches and nine intact input bindings.
- `../paper/sections/F_lattice_proof.tex`, `G_bridge_proof.tex`, `H_verifier_proof.tex`: mathematical exposition and boundaries.
- `../tools/replay/receipt_join.py`: portable verification of the new receipt/custody composition.

See the current `VERIFICATION_RUN.md` for the completed replay, and the GitHub tag/delivery receipt for the final snapshot. Historical 0.1.1 and unfinished 0.1.2 review reports are not claims about this final upload.
