# Source algorithm and boundedness review

Date: 2026-10-18
Status: ADMISSION_AND_CHANGED_GEOMETRY_SUPPORTED; BOUNDED_EXECUTION_RETURNED_NO_UNIT.

This reviewer inspected the actual producer search.gp, SEARCH_CONTRACT.md, setup and inputs. No broad arithmetic search or full BNF was launched by the reviewer. Concrete accepted candidates, if any, require the separate evaluation lane and independent exact replay.

## Exact source checks

The reviewer independently checked all fourteen producer ideals in unmodified GP: each is an integral ideal in the recorded maximal-order basis, has the recorded exact norm, and satisfies tau(I)=I in HNF. The scalar matrix has tau^2=1. This replay took approximately 0.12 seconds; its receipt and outputs are in SETUP_REPLAY.json. It does not certify principality of any ideal.

## The numerical geometry is actually changed

The saved archimedean pairing has twelve two-element orbits and three fixed places. All sixteen recorded integer directions are nonzero, have opposite exponents on each paired orbit and exponent zero on fixed places. An independent reconstruction of the producer's rounded metric at amplitude two shows that none of the sixteen metrics commutes with tau. Relative maximum-entry discrepancies range from approximately 0.279593 to 0.685354. These are substantial changes, not merely rounding differences in the unweighted metric.

The producer assigns the same weight to the real and imaginary coordinates of a complex place, includes the standard sqrt(2) factors, and uses an integer unimodular LLL change of the ideal lattice. Thus reduced columns and their integer sums/differences remain in the actual ideal. The mixed-parity filter discards tau-fixed and tau-negated candidates before exact norm evaluation.

The field's embedding matrix is cached. Calling precision(...,180) does not reconstruct lost embedding digits, and these weights must not be described as 180-digit independently certified embeddings. That affects search quality, not the exact admission rule: the rounded lattice is a source of integer candidate coefficients, and membership, ideal equality and norms are checked in the number field afterward.

## Admission and export boundary

For each retained candidate, the producer computes nfeltnorm exactly. Equality of its absolute value to the ideal norm triggers exact membership, exact tau-stability and principal-ideal-HNF checks. It forms epsilon=alpha/tau(alpha), checks both epsilon and its inverse are integral in the maximal-order basis, and checks absolute norm one. Relative norm one also follows exactly from the quotient definition and verified involution. No candidate is admitted from floating-point norm estimates.

The compact export places exponents +1 and -1 at scalar positions zero and three, respectively, matching alpha/tau(alpha). This is an ordinary-unit export; the faithful character projection and actual global/local image are separate evaluation work. If the process is interrupted before its final compact export, the append-only admissions.gp, when present, must be reconstructed and audited rather than treating an absent compact file as proof of zero output.

## Boundedness and permitted inference

The program schedule has six amplitudes, sixteen directions and fourteen ideals: at most 1,344 lattice stages. Each stage tests twelve columns and twelve pair sums/differences, before pure-parity and sign-deduplication filters. Exact norm calls are distinct retained candidates up to sign according to the program's exact basis-vector keys. It stops after eight distinct admitted epsilons or at the recorded time/resource bound. A completed finite schedule does not exhaust generators of the chosen ideals, let alone all invariant ideals or all relative units.

The external wrapper enforces wall time and samples RSS, and the GP alarm supplies an additional termination boundary. Exit code zero alone does not demonstrate completion; final markers and receipts govern accounting. The first wrapper checks memory at intervals, so its RSS figure is an observed peak, not a proof that no transient spike occurred.

This route does not infer a class bound or seed result, even if it obtains units. The exact whole-source ledger remains (4-r_U)+(c-r_C). A successful unit image can lower-bound r_U; the complete class term still requires its own source and constraints.

## Reviewer repairs

Two short reviewer-only geometry checks initially failed: omitted realprecision initialization, then vecmax applied to a vector of columns. Both failures are preserved. Correcting the diagnostic to match the producer precision setting and scalar maxima gave the required pass marker for all sixteen directions. The producer itself contained the correct precision initialization and was not modified by these reviewer repairs.

## Completed run accounting

The source process ended by its GP alarm after 177.110361 seconds, with observed peak RSS 124,325,888 bytes. Its wrapper exit code was zero, but there is no SEARCH_SCHEDULE_COMPLETE marker. Thus this was a bounded interruption, not a completed schedule. The last complete checkpoint is stage 1,317 of the maximum 1,344, at amplitude 64, direction 15, ideal 1.

A separate Python parser reconstructed the checkpoint counts and compared every saved exact norm to the relevant exact ideal norm: 14,326 logged norm calls, 17,281 pure-parity skips, one sign duplicate, and zero equality matches. These sum to 24 candidate positions at each of the 1,317 complete stages. No admissions file exists and no admitted unit was reported. The interruption occurs in the next LLL call, rather than after a reported admission. `check_accounting.py` replays this scoped check and `FINAL_ACCOUNTING.json` binds the inputs.

This check validates arithmetic/accounting of the saved norm outputs, not an independent regeneration of those norms or the floating-point search. It establishes no exhaustion claim for all generators of any ideal. The operation changed the search geometry as intended but supplied no faithful unit image or new whole-source upper bound. The class contribution and seed endpoints are unchanged.
