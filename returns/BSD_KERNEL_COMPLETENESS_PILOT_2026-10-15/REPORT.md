# Common-point consistency and complete-source kernel pilot

Date: 2026-10-15. **A STRICTLY STRONGER DETECTOR ON ACTUAL SEED DATA; NO NEW SEED BOUND.**

The user asked for experiments directed at completeness or kernel control. This return executes two tests, using the saved exact descent arithmetic. It finds information that the previous separate local quotients discarded. It does not compute new torsion-field data, prove a new upper bound for the seed, or advance FIN, ORDER9 or Q36.

The independent source and proof reviews are additional AI-assisted checks. They do not recertify the underlying descents, establish novelty, or constitute proof-assistant verification.

## 1. An actual change to the experiment

Previously, at each auxiliary place q, a class was tested modulo the local image of all rational points. Passing meant that some rational-point combination explained that local value. The combination was allowed to differ from place to place.

Now require **one common rational-point combination at all selected places**. For S=Sel_3(E/Q) and its full point plane W, use

    D_Q : S/W -> (direct sum over q in Q of E(Q_q)/3E(Q_q)) / loc_Q(W).

The denominator is the image of a single global W, not the direct sum of its separate images. This construction is well-defined on S/W. The new kernel is contained in the old intersection of local detector kernels and can be strictly smaller. It still evaluates Kummer lifts; the corresponding Sha torsors remain locally soluble.

The selected pair and the rule to add the next individually blind block were sealed in COMMON_POINT_CONTRACT.md before the stacked quotient was calculated. The local values themselves were already published. This is a new combination of existing arithmetic, not a fresh or blinded field computation.

## 2. The seed calculation

Work at coefficient prime 3, on the retained true-class span (P1,P2,beta1,beta2). At each of q=1213,1543,1699 the two point images fill the local Kummer space. Thus **each old detector is zero on every genuine class**, including the two known excess classes.

Solving for the unique local point coefficients gives the following matrices on (beta1,beta2), with rows giving coefficients of (P1,P2):

    T_1213 = [[2,1], [0,0]],
    T_1543 = [[2,1], [1,2]],
    T_1699 = [[1,1], [2,0]]               over F_3.

For the first pair, the condition that one point combination explain both places is

    (T_1543 - T_1213) (x,y)^t = 0,

or x+2y=0. Hence only the excess line beta1+beta2 remains invisible. Adding q=1699 eliminates that line from the detector kernel: a nonzero multiple of beta1+beta2 has point coordinates (0,0) at the first two places, but (2,2) at the third.

| Auxiliary places | Rank of old separate detector on known excess | Rank of common-point detector |
|---|---:|---:|
| 1213,1543 | 0 | 1 |
| 1213,1543,1699 | 0 | 2 |

The target is expressed in the fixed global point basis. No identification of local torsion bases at different primes is required: any local coordinate change acts on the point and excess images together and leaves T_q unchanged.

This is an explicit way of recovering information lost by the earlier detector. It is **not** proof that the displayed class list is complete. The seed's already retained separate 3-primary theorem is not being rediscovered or upgraded here.

## 3. Complete-source test: do not supply the class list

For controls with a retained certified source, the script reconstructs the entire necessary-condition kernel from all source columns before consulting the known class list.

| Control | Complete source dimension | Containing Selmer kernel | Point dimension | Candidate excess dimension |
|---|---:|---:|---:|---:|
| 1913b1 | 9 | 2 | 0 | 2 |
| 389a1 | 10 | 2 | 2 | 0 |
| 433a1 | 13 | 2 | 2 | 0 |

For 1913b1, exhaustive enumeration of all 19,683 source vectors independently reproduces exactly nine survivors, without using the two supplied excess columns. Only afterward is their span compared with the recovered kernel; it agrees. The old q=1867 detector misses one full source direction. The q=997 block has zero kernel on the recovered two-dimensional space, so there are no unseen directions in that source left to detect.

For 1913b1 and 389a1, the scalar and saved necessary global-additivity rows already supply the upper bound two. Their actual two classes are admitted separately, by the retained exact norm/local certificates or point identities. Thus the upper calculation does not rely on declaring a sample of local images complete.

For 433a1, omitting the local rows leaves dimension three; retaining them gives two. The source BNF is certified, but this pilot does not independently recertify its earlier local-image computation. That interface remains at its retained grade.

These are retrospective checks of already completed control descents. Their purpose is to validate a procedure for discovering omitted classes and certifying an invisible kernel, not to claim new control groups or seed coverage. The incomplete 28042a1 source and the seed's historically conditional source are not silently promoted.

## 4. Exact meaning of a kernel certificate

Let A be a certified complete source, C necessary admission rows, U=ker C, and W the full global point plane. We need the proved containment

    W subset S subset U subset A.

Let M_Q be the stacked source-evaluation matrix and let L_Q annihilate the stacked point image M_Q W. Then the exact remaining invisible space is

    Z = U intersect ker(L_Q M_Q)
      = W + (U intersect ker M_Q).

If Z=W, the common-point detector is injective on the **entire** S/W, including classes not previously listed. This is a genuine upper-control statement about its kernel, conditional on the source containment. It does not assert that S/W vanishes: detected classes can still exist. Their number requires a bound on the image as well.

One must not append detector rows to admission rows and call the result Selmer. Admission rows must vanish on every true Selmer class; detector rows intentionally need not.

PROOF_REVIEW.md supplies this argument and explains the fixed-prime separation consequence of the retained joint-evaluation theorem. Eventual detection does not supply a bound on the number of unknown classes or on detecting primes across coefficient primes.

## 5. Scope of the wider comparison

All 276 pairs of the 24 saved blocks were compared on each of four panels. This is retrospective exploration, not 1,104 new arithmetic calculations.

* Seed known span: common-point rank strictly increases for 162 pairs. Of 66 pairs where the old detector is zero, 24 now have rank one and 42 have rank two.
* Rank-one positive control 28042a1: 67 pairs improve; its incomplete source still forbids a complete upper bound.
* Rank-zero 1913b1: no change, as expected when there is no point subgroup to quotient separately.
* Point-only 389a1: every quotient remains zero, so the construction does not manufacture excess from rational points.

The primary seed example was selected using published individual point ranks, before the new pair calculation. The two independent implementations agree on its point repairs and all combinations in its named span. Root arithmetic uses exact F_3 elimination and a separate exhaustive source enumeration. Original field, rank, point saturation, global admission and local arithmetic retain their original grades.

## 6. Experiments that can now be distinguished

1. **Complete-source common-point kernel.** Apply the stacked detector to the whole necessary-condition space, not only known columns. Output each remaining source vector, its unit/class/valuation support, and whether it has an exact global admission certificate. Success is Z=W with a certified source, not just a full-rank matrix on supplied classes. The controls above validate this workflow; a new arithmetic case must change the source or previously unresolved kernel.
2. **Compute the whole norm-obstruction map.** The earlier degree-24 polynomial concerned one false repaired class. Apply actual affine norms to a basis of the entire scalar-compatible source and certify its cube relations, rather than observing one candidate at more primes. Combine this complete global map with the actual local maps while retaining the point plane. This could turn isolated rejections into a complete source presentation and reveal relations that repeat across examples. It is not performed here.
3. **Test the relation, rather than just the rank, across coefficient primes.** If the completed presentations expose a fixed family of integral relations accounting for every residual kernel, freeze that proposed family and test it on a different coefficient prime and a positive-excess control. It fails if it discards a genuine class or leaves a claimed-complete kernel. Passing would justify trying to prove that family covers the relevant source. We do not yet have such a family or a bound on its index.

The useful new datum is incompatibility of the **same** global point coordinates across places. The missing BSD arithmetic remains a complete-source/image bound on unresolved coefficient primes, with suitable uniform control. Neither this improved detector nor the complete small controls supply that theorem.
