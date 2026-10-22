# Integration into the current research record

This is an addendum to a completed review, not a request for a fourth Aristotle
job and not an instruction to interrupt the running source-construction jobs.
No job was submitted and no GitHub file was modified in this session.

## Change supported by the written proof

In the reviewed comparison, replace the all-but-4547 global exactness statement
and its at-most-one global error by:

> Under the retained receiver inputs, restriction identifies B_p with
> Sha(E/Q)[p] for every prime p >= 5. At p = 4547, use the global Kummer class
> of P_2 and single-place reciprocity to remove the possible global relaxation.
> No equality of the full pulled-back local condition at 4547 is asserted.

The proof is PROOF.md, sections 2-4. It uses the BFR generator at the coefficient
place in exactly the same global-duality mechanism that the reviewed return
uses at its exceptional away-from-p places. The new application is absent from
the inspected pinned review. No assertion of novelty across the entire archive
or published literature is made.

## Do not change

Keep the existing FIN, ORDER9, and Q36 statuses. Do not label this a new primary
certificate or an independently established upper bound. The earlier sufficient
criterion dim B_p <= 1 already covered 4547; this addendum removes uncertainty
in identification, not an obstacle to that criterion's logical implication.

Keep all corrections in the third review, including the global/local
distinction, the repaired place-2 argument, the full supersingular local-image
input, and the correctly scoped S-unit/Brauer statement.

## Relevance to the running source job

The jet-constructor experiment seeks authenticated global Hida/Kato source
values and an independent index estimate. This addendum does not construct its
seed presentation, its higher-weight eigenvalues, its dual certificate, or its
forcing term. It supplies no new ordinary or supersingular valuation bound.
There is no mathematical reason in this addendum to redirect that experiment.

A future independent upper bound from a source or field-arithmetic job can be
compared with the exact receiver under the corresponding retained hypotheses.
It must not be obtained by assuming Sha vanishes, by imposing new relations on
actual receiver elements without proving them, or by reusing P_2's automatic
Selmer orthogonality as a new constraint on Sha.

## Verification boundary

Read in this session: the pinned REPORT.md, CORRECTED_PROOF.md, CORRECTIONS.md,
and the BFR MATHEMATICAL_RECONSTRUCTION.md; relevant published local-duality,
reciprocity, and additive-reduction statements were opened and checked. Fresh
integer arithmetic checks are in checks.py and CHECK_RESULTS.json.

Not rerun: the three new upper-control Lean modules; all prior residual-image,
basis-saturation, parity, finite-group-descent, and class-field identifications;
the full original Aristotle continuation archive. The third report's Lean
compilation and axiom results are reported prior checks, not new checks here.
The new global step is a written proof, not formalized in this package.
