# Rank-two continuation of the coefficient-seven joint bound

Date: 2026-10-18

**Result: no rank-two joint unit bound and no complete class bound obtained.** The actual valuation allowance is zero on both new rank-two controls. The tested arithmetic source constructions supplied no nonzero faithful unit directions, so the requested norm/local rank profile remains unmeasured. FIN, ORDER9, Q36 and seed-prime coverage are unchanged.

This is the completed continuation of the previous coefficient-seven experiment, not a proposal for an unexecuted search. The earlier complete unit-kernel-zero result concerned rank-zero 11a1. This return deliberately tests rank-two sources and retains the entire ordinary class contribution.

## What was actually tested

| Arithmetic source at p=7 | Rank input | Complete valuation allowance | Authenticated faithful unit contribution from tested families | Complete class contribution |
| --- | --- | --- | --- | --- |
| 655a1 | Fresh PARI rank bounds [2,2] | 0 | All 24 tangent/chord relation products are literally signs | No bound obtained |
| Quadratic twist of 11a1 by -47 | Fresh PARI rank bounds [2,2] | 0 | Direct and partial-relation constructions below supply none | No bound obtained |

These rank computations are computer arithmetic inputs, not independently formalized descent certificates. Neither curve is the original seed. The field and local calculations use their actual nonzero 7-torsion point fields, of degree 48 and signature (6,21), with exact torsion-point and scalar-action checks.

The whole-source target is retained in [PROOF.md](PROOF.md):

    dim ker L = (4 - r_U) + (c - r_C).

Here 4 is the complete faithful ordinary-unit dimension, r_U is the rank of the combined authenticated norm/local map on it, c is the complete ordinary class dimension, and r_C is the class-lift obstruction rank modulo the same unit image. Both actual valuation allowances are zero. Two rejecting independent unit directions would already bound the unit kernel by two; a complete fundamental-unit basis is unnecessary for that partial goal. But zero rank on a found list supplies no upper bound on the full unit kernel. The class term cannot be replaced by a provisional class table or an S-class quotient.

## First source: functions from rational points

On 655a1, four tangents, six chords and four vertical functions at P, Q and P±Q gave 84 scalar-translated factors. Every principal ideal was completely factored and reconstructed. Their 142-row divisor matrix has rank 60 and an integer kernel of dimension 24.

This produced actual units, but exact expansion in the number field showed that all 24 kernel products equal +1 or -1. Thus the entire ordinary-unit subgroup produced by this finite family is trivial modulo seventh powers. Separate residue calculations at three split primes and the coefficient-seven formal branch agree. They are not evidence that the full faithful unit space has zero rank under the maps.

Several changed BNF configurations were also tested with saved bounds and completion markers. None completed. The changed small-factor-base and randomized options did not provide a class or unit certificate. See [source report](rank_two_source/REPORT.md) and [local report](local_pipeline/REPORT.md).

## Second source: a smaller-discriminant rank-two twist

A bounded rank scan selected the -47 twist of 11a1 without using a Sha value or the desired norm result. Its model is

    [0,-1,1,-22826,2411880],

with displayed points (63,1104), (110,1104). The point-field discriminant is

    -7^47 * 11^36 * 47^24.

The smaller root discriminant made this a changed arithmetic source, not a repeat of the same field calculation. The exact field, ordinary formal branch and split-prime evaluation data were constructed. Its BNF computation still did not finish within the recorded budget.

A direct scan of 2,000 integral candidates found three genuine units. All three are fixed by central [-1], so they contribute zero in the faithful character. Of 1,471 mixed-parity candidates, none had norm supported only at 7, 11 and 47. Complete ideal factorization of the selected 24 mixed scalar orbits gave a 421-by-144 matrix of rank 144: this finite family has no integer divisor relation and produces no ordinary units. See [exact direct-source report](twist_source/direct_units/REPORT.md).

## A diagnosed selection problem, followed by a changed search

We then inspected the matching official PARI 2.17.3 source and built an isolated instrumented collector. The installed engine was not changed. Exporting exact generators before the collector's relation-rank filter yielded 1,424 complete polynomial rows. An unmodified GP calculation verified that **every exported generator is central-fixed**. The [character calculation](pari_partial_source/CENTRAL_CHARACTER_PROOF.md) therefore excludes the entire harvested family from the faithful component. This is an exact statement about this saved family, not a claim about all short elements or all PARI searches.

The next search explicitly selected mixed-parity sums and differences of reduced ideal columns to change that selection problem. It logged 92,544 internal filter trials across 723 completed collector invocations and produced zero accepted exports before its 120.09-second external stop. Trials are not distinct field elements; invocations can repeat ideals. The internal rounded-norm filter is not an independent proof of nonsmoothness. This outcome is a bounded computational failure, not a nonexistence theorem.

No candidate from the instrumented program is automatically a certified unit or relation. Independent unmodified-engine ideal reconstruction and exact integer-kernel checks remain required for admission. The [source report](pari_partial_source/REPORT.md), original source archive, patches, build receipts, capture hashes and [independent instrumentation reviews](ROOT_MIXED_INSTRUMENTATION_REVIEW.md) preserve that boundary. No further search is running.

## The complete class question was tested separately

The actual prime-divisor permutations and primitive incidence maps give zero valuation allowance for both controls. The twist result has a particularly direct check: scalar cubing fixes every relevant prime while the faithful character has cube -1, so the faithful divisor spaces vanish.

This does not remove ordinary ideal classes. Two proposed shortcuts were checked:

- An exact GL2(F7) subgroup enumeration shows that every subgroup of index below 48 meets the scalar center. Strictly smaller subfields inside this normal closure cannot reconstruct the faithful component through the tested generalized norm-relation method. This does not exclude other class-group methods.
- The twist shares the old curve's degree-24 x-field, but its faithful class sector is a different eigenspace in the degree-96 compositum. Cross-norm annihilates that sector. Even a certified class-zero result for the original field would not supply the missing bound for the twist.

The class-group certification and p-rationality source checks supplied no complete class upper bound. Their scope is recorded in [class control](class_control/REPORT.md) and the [independent twist audit](class_twist_notes/REPORT.md). The original failed class certificate is not upgraded.

## What this establishes for the continuation

The rank-two test was carried out far enough to separate the difficulties. The actual field, local maps and complete valuation layer can be constructed; the finite source families tested here do not reach the faithful units needed to measure the rank profile. Independently, complete ordinary class control remains absent.

The result does not say that the earlier joint norm/local mechanism fails on rank-two curves. It says that this run has not supplied the arithmetic source and class bounds needed to test that claim completely. Further residue rows on these same zero-character families would add nothing. Any continuation must change the authenticated faithful source construction or supply an independent complete class bound; it should reuse the existing field/local data rather than recompute them.

Written deductions and exact computations retain the earlier image, incidence and local-condition inputs. Same-team independent reviews cover the whole-source formula, divisor consequences, twist class sectors and instrumented export boundary; they do not recertify every antecedent theorem. File hashes establish custody, not mathematical validity. See [REPLAY.md](REPLAY.md) for bounded verification and [STATE.json](STATE.json) for the final status.
