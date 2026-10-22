# Additive final scope review

Date: 2026-10-18
Status: FINITE_SOURCE_EXCLUSIONS_SUPPORTED_AT_RECORDED_SCOPE; NO_RANK_TWO_JOINT_BOUND.

This review supplements the sealed review/ tree without modifying it. The reviewer read the three adaptation contracts and producer code, their final outputs and resource receipts, and the root REPORT.md and REPLAY.md. The final report correctly distinguishes a failed bounded source construction from an impossibility theorem or seed result.

## Actual-principal-ideal and pair adaptations

A separate exact Python selection check confirms that the saved twenty records are precisely the twenty smallest positive integral norm ratios in the 14,326-row log, with lexicographic full-record tie-breaking. This is selection from that log, not a globally minimal norm claim.

In unmodified GP, the reviewer then independently recomputed all twenty cached candidate norms and principal-ideal HNFs, matched them to the saved records, verified mixed parity and failure of tau-stability, and repeated all 380 direct/conjugate principal-ideal comparisons on 190 pairs. Every check passed; no pair matched. This took approximately 0.30 seconds and involved neither LLL nor a fresh search. See FINAL_SCOPE_CHECK.gp, its output and receipt, and FINAL_SCOPE_SELECTION_CHECK.json.

The pair test alone excludes only simple ratios. It does not exclude multi-element products, which is why the final anti-divisor test is a changed and relevant operation rather than a repetition of that pair test.

## Final twenty-ratio divisor calculation

The final producer completely factored each of the twenty saved principal ideals and checked exact reconstruction for the ideal and its tau conjugate. Those producer factorization/reconstruction statements remain inputs to this review at their recorded computer-arithmetic grade. The reviewer attempted a separate product-reconstruction pass, but its 15-second alarm interrupted it. This incomplete replay is preserved under INITIAL_INCOMPLETE_FINAL_ANTI_CHECK.* and is not reported as a completed independent factorization or reconstruction certificate.

The completed independent pass checks that all twenty factor records bind to the previously verified candidate vectors, verifies the exact tau action on every saved prime-ideal HNF, reconstructs the anti-divisor matrix from those records, and matches it entry-for-entry to the saved matrix. It obtains a 127-by-20 integer matrix. A separate standard-library Python Gaussian elimination modulo seven finds all twenty pivot columns. Thus its rational column rank is also twenty and its integer kernel is zero. See FINAL_ANTI_CHECK.gp, FINAL_ANTI_CHECK_RECEIPT.json and FINAL_ANTI_MATRIX.json. No BNF or factor search was run by this reviewer.

Conditioned on the producer's complete prime-ideal factorizations, these columns are exactly div(alpha_i/tau(alpha_i)). A product of the twenty ratios is an ordinary unit only if its integer exponent vector lies in this matrix kernel. The kernel is zero. Consequently no nonzero exponent vector in this particular twenty-generator multiplicative family gives an ordinary unit. The statement includes arbitrary integer exponents in those twenty generators, but does not include additional scalar translates, further candidates, or unknown units.

The producer's first compact exporter failed on an empty-column matrix after saving the exact divisor data. The subsequent repair reads that data, checks its kernel and writes the final result without repeating the factorization. The required completion marker occurs in the repaired run. The report preserves this distinction and does not treat an exit code of zero as completion.

## Bound and endpoint discipline

No ordinary unit was admitted by the main search or its three adaptations. Therefore there is no new source on which the norm/local evaluator can calculate a faithful image rank. Its correct status is ACTUAL_RANK_UNMEASURED. In particular, zero output from this finite source process is not rank zero on the whole unit group.

The root report correctly retains complete unit dimension four, the full-source expression (4-r_U)+(c-r_C), and the unbounded ordinary class contribution. It does not promote a partial unit list, a provisional class group or a field-norm identity into a complete source. Neither the control's rank-two setting nor the unrestricted relative-unit coverage lemma establishes a bound across coefficient primes or a transfer to the fixed seed.

FIN, ORDER9, Q36 and seed-prime coverage are unchanged. The final finite-source exclusions are valid stopping points for this particular experiment; they are not a conclusion that the broader relative-unit construction is dead.

## Provenance limits

All independent checks here use the retained actual field and maximal-order/scalar input files. They do not recertify the original field construction, full residual image or rank computation. The review contains no novelty claim and is not a proof-assistant certificate. Hash bindings establish file identity only. The sealed review/ tree remains byte-for-byte unchanged.
