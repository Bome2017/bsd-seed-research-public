# Rank-two partial relation-generator source: bounded result

No new faithful unit, class bound, or joint upper bound was obtained. FIN, ORDER9 and Q36 are unchanged. The source is the degree 48 nonzero 7-torsion point field of the rank-two -47 twist of 11a1.

## First changed source: retain rejected relation generators

Inspection of matching official PARI 2.17.3 showed that its small-norm collector can discard generators whose divisor rows do not increase its relation rank. A minimal isolated local patch exported the exact algebraic generator before that decision. It neither changed the original installed GP nor supplied an arithmetic certificate.

The patch compiled in 1.79 seconds; a cubic smoke test completed. A single 72.41-second capture produced 1424 complete exact polynomial rows (1416 distinct polynomial strings) and was stopped early. Original GP then converted each polynomial into the original maximal-order basis and verified that all 1424 are fixed by scalar[-1]. The exact character identity in CENTRAL_CHARACTER_PROOF.md proves their faithful projections are seventh powers. This excludes this entire finite captured family, including virtual-unit products, without inferring a global class-group fact.

## Second changed source: mixed reduced-ideal columns

The first failure identified a geometric bias: the retained short generators all belonged to the central-fixed subfield. The second patch therefore sampled sums and differences of actual LLL-reduced ideal columns, selected only mixed central parity, and bypassed the original factor-attempt cutoff. The smaller column index was at most 8; each ideal-collector invocation tried at most 128 mixed candidates. Ideals can be products and can recur. The exact input NF basis was checked literally before applying the authenticated central matrix.

This source-only pass compiled in 1.25 seconds and ran for 120.09 seconds before the external wall limit stopped it. It logged 92544 internal candidate-filter trials across 723 completed ideal invocations, with zero accepted smooth generators. The last incomplete invocation may contain additional unlogged trials. These counts are not counts of distinct field elements. No assertion that every candidate is independently proved nonsmooth is made: factorgen was a candidate filter, and its rejects were not separately factored. With no exported candidates there was no subsequent ordinary-unit admission.

## Custody and review boundary

The original official tarball hash is in SOURCE_BINDING.json. Both patches, exact build commands, library hashes, smoke output, harvest logs and resource receipts are retained. The libraries and raw build/work copies live in the adjacent PARI_BUILD directory and are not global installations. The large first capture is stored as deterministic gzip; CAPTURE_COMPRESSION.json records raw and compressed hashes. ARITHMETIC_BINDINGS.json pins the original field, maximal order, scalar matrix and unmodified GP binary.

The modified collector supplies candidate algebraic polynomials only. All mathematical acceptance requires exact original-GP checks; no internal relation vector or incomplete BNF is promoted to a class certificate. A computational source failure does not prove that useful units or a seed-finishing mechanism do not exist.

## Exact remaining boundary

The experiment produced no independently admitted faithful unit directions on this rank-two control. The preceding three direct-scan ordinary units were central-fixed; the 24 mixed direct-source orbits had no integer divisor relation. The separately established valuation-layer control is not a class-group bound. Thus the complete joint-source bound remains uncomputed. No further source search was launched after this cap.
