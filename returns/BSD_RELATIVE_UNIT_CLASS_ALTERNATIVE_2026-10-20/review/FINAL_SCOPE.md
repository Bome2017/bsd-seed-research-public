# Independent scope review of the actual-seed alternative

Date: 2026-10-20. Reviewer: sibling agent `same_curve_scaling`.

This reviews the actual seed's relative-field construction, the elementary class-transfer and scaling deductions, and the memory/search experiments. It is not independent certification of the prior global BSD source theorems. No FIN, ORDER9 or Q36 result is supplied.

## What is established in this packet

The degree-six and degree-twelve fields are genuine scalar fixed fields inside the actual degree-24 nonzero-five-torsion point field. Their embeddings, signatures, discriminants and quadratic tower equations were checked exactly. This is a useful representation of the source field, but neither field is a substitute for the missing faithful arithmetic upstairs.

The class-transfer proof is sound at its stated scope. Since extension degrees two and four are units at five, ideal extension and norm split the ordinary 5-primary class groups. The faithful characters lie precisely in the relative minus group for the degree-two extension. Norms to either proper scalar fixed field kill these faithful components. Thus even complete lower-field class calculations cannot, by themselves, bound them. The abstract arbitrary-rank countercontrol tests this inference; it is not an example of a seed class group.

The general signatures and character multiplicities in `class_control/SCALING.md` check. The full anti-unit rank is `(p^2-1)/4`; a single faithful odd-character unit rank is `(p+1)/2`. A relative quadratic engine therefore still faces quadratic total unit rank unless it targets the desired character directly. The complete sufficient bound remains

    dim admitted_source <= (p+1)/2 - r_U + k_C,

on the retained valuation-zero domain, with actual authenticated norm rank `r_U` and the surviving ordinary class contribution `k_C`. This is bookkeeping of the needed arithmetic, not an upper estimate for `k_C` or lower estimate for `r_U`.

## The memory hypothesis was tested and corrected

The first proposed software patch compacted the result of each prime-decomposition call. Small-control arithmetic survived a separate, unmodified-runtime certification and exact unit/class replay. Nevertheless, the patch did not repair the seed run. Instrumentation found zero discarded bytes at every recorded sample: essentially all accumulating stack use was retained prime-decomposition data. Calling this a successful garbage-collection repair would be false.

The independent profile review estimates about 677–725 MB for the completed factor base alone. This is an observed scaling estimate, not a memory guarantee for the whole algorithm.

The subsequent **unmodified** `bnfinit(NF,1,[.02,0,4])` run completed factor-base construction with maximum resident memory 732,577,792 bytes. Thus that stage's previous 512 MB limitation was passed using sufficient RAM and the standard smaller-relation-base parameters. The full ideal bound remained 419775, the relation base had 721 prime ideals, and the unchanged honesty check remained in the algorithm.

That run then reached its 117-second internal alarm in small-norm relation collection. Its log shows an initial 11-column relation matrix and later requests still missing 721 relations. It returned no BNF, no unit basis and no class group. Script/output hashes, the explicit alarm, absence of the success marker, and absence of the promised data files were checked independently. Process exit zero is not accepted as successful completion.

## The random producer and the measured default cache

The unmodified random-relation run with `[.02,0,-1]` reached its 177-second internal alarm at 734,720,000 bytes peak resident memory without returning a BNF. Its hashes and lack of output were independently checked. Source inspection confirms that the negative third parameter bypasses `small_norm` and invokes the existing random relation producer without deleting factor-base or final honesty checks. This was a changed search method with the same mathematical acceptance condition, but it did not complete the arithmetic.

The separate source-count measurement is complete and accepted. It streams all 35,373 rational primes through 419775, using distinct residue degrees from polynomial factorization away from the polynomial index and maximal-order ideal decomposition at the ten index primes. Its norm cutoff and rational-prime cutoff reproduce the `FBgen` conventions, including the actual smaller run's 721 ideal and 175 rational-prime counts.

The full default relation base has 35,749 ideals. Source line 3865 calls `zero_Flm_copy(KC,KC)`. The installed inline constructor allocates separate machine-word columns, so the entries alone occupy exactly `8*35749^2=10,223,928,008` bytes (9.521775 GiB). This is a concrete lower bound for that one implementation allocation; headers and every other stage require further memory. The c1=.2 alternative has 5,077 ideals and 206,207,432 entry bytes. All numerical products and receipt hashes are independently checked in `DENSE_CACHE_COUNT_REVIEW.json`. This count supplies no class group or unit system.

## Final balanced producer gate

The last parent-approved gate used c1=.2 and the random producer, with the full larger ideal bound retained. It completed the factor-base stage with exactly the independently counted `KC=5077`, `KCZ=1199`, then reached its 177.13-second internal alarm at 933,396,480 bytes peak resident memory. The log records 24 initial accepted relation columns and no additional accepted column before the interruption. Source inspection confirms that `dbg_newrel` prints each accepted column at the selected debug level. The first `rnd_rel` pass did not finish; this is not evidence that it could never produce a further relation.

The final receipt's script and output hashes match. Its explicit alarm, absent success marker, and absent BNF/class files were independently checked. The gate is rejected as a completed arithmetic computation despite process exit zero. No further producer run is planned or launched by this reviewer. The complete numerical review is in `BALANCED_RELATIONS_REVIEW.json`.

## Current conclusion

The packet has identified the correct faithful relative component, isolated the default dense-cache cost, and passed an earlier resource stage with standard parameter changes. All three bounded full-field production gates ended before a BNF was returned. It has not obtained a complete class/unit bound for the actual seed at five, much less a bound across coefficient primes. A successful later relation computation would still need authenticated ideal relations, source/norm maps, and class completeness before its result can be used as the desired upper bound. A bounded run failing to finish would be a computational outcome, not evidence that the field method or FIN is impossible.
