# Independent check of the two-prime scalar extension

**Verdict: CONFIRMED_AT_RETAINED_AND_IMPORTED_THEOREM_GRADE.**

No blocking error was found in the supplied extension, the coherent source normalization, or the four corrected local calculations. `NEW_LEMMA_WITH_OPEN_BOUND` is an appropriate return status. This check supports a written comparison theorem, without promoting its imported foundations, literature novelty, or BSD endpoint status.

## What is now supported

Under the retained seed hypotheses at every good p>=5, including the primitive residual Kato system, E(Q_p)[p]=0 and t=0, there is a single C_p in F_p such that, in the coherent source conventions,

    delta_ab = C_p e_a e_b D_ab^2

for every distinct cyclic Kato pair a,b. This includes z=0 and D_ab=0. Here D_ab is the determinant of the two rational-point localization rows and e_q is the independently defined finite/transverse Tate-pairing factor. Consequently

    delta_ab != 0  <=>  [D_ab != 0 and Sha(E/Q)[p^infinity]=0],
    C_p != 0       <=>  Sha(E/Q)[p^infinity]=0.

The second statement detects vanishing. It is not a formula for the order of a nontrivial primary group.

The z!=0 branch remains the retained prior derivation. This review independently checked the added z=0 branch, its use of the prior direct criterion, and its normalization. It did not redo every seed arithmetic certificate or the foundational main-conjecture/Kolyvagin-system proofs.

## Why the new argument works

At z=0, a nonzero point combination survives in each singleton-modified p-strict Selmer group. Stub membership therefore kills every singleton. The edge relations then place every pair class in the same unmodified p-relaxed Selmer group, with zero full localization at its own two auxiliaries.

In the Sha[p]=0 branch that common space has dimension three: the two point classes and a class y whose singular coordinate is one. The pair classes can therefore be interpolated explicitly using their two zero auxiliary coordinates. Cup-product reciprocity for the **three-prime** class against the two point classes supplies the extra relation between these interpolations. The determinant signs give the square, and the three-class affine Chebotarev argument connects all nondegenerate pairs. The proof never assumes a nonzero singleton.

In the Sha[p]!=0 branch all pair coefficients vanish by the retained length theorem, so the same comparison holds with C_p=0. This proof by cases is legitimate; it does not establish which branch an unsettled seed prime occupies. A separate kernel/stub argument handles D_ab=0 before any division.

Details of the independent reconstruction are in [AUDIT.md](AUDIT.md).

## Normalization passes, with its stated scope

The proof of [Kim Theorem 3.11, printed p.21](https://arxiv.org/html/2203.12159v6#S3.SS4) explicitly gives the image E_p delta_n in the correct fractional lattice, with E_p=#E(F_p)/p at good reduction. Thus the single lattice coordinate E_p*x -> x makes u_n=1 for the whole coherent system. This follows from the printed calculation, not just from the theorem's unspecified-unit statement. See [NORMALIZATION_CHECK.md](NORMALIZATION_CHECK.md).

This does not certify arbitrary stored PARI symbols or independently rescaled Kato components. Their periods, primitive roots and lattice conventions still need to match. The normalization is a coherent coordinate choice, not a claim that a previously arbitrary u_n already equaled one.

## Corrected controls pass locally

I used a different exact arithmetic implementation: transform to short Weierstrass form and use repeated rational addition. It reproduces the supplied coordinates and valuations:

| Curve | p | #E(F_p) | Valuations of t([#E(F_p)]P) |
|---|---:|---:|---|
| 5741a1 | 5 | 7 | 2, 4 |
| 3779a1 | 7 | 11 | 2, 2 |

Both have good non-anomalous reduction. The four displayed points are therefore locally p-divisible, and local p-torsion is absent. This confirms the corrected local claims. It does not independently establish global rank, basis saturation, Sha, the full scan or the reported modular-symbol pair tables.

The supplied finite algebra checks replay successfully. An additional exhaustive check solves the two triple-reciprocity equations in all 82,088 tested scalar assignments at p=5,7 and recovers exactly the one-dimensional family claimed, **including its zero member**. These are finite algebra checks, not proofs of the arithmetic imports.

## What changed and what remains

The prior localization-domain gap in the written scalar comparison is closed at this grade. The unknown pair-unit separation has also been resolved in coherent source conventions. Those are substantive improvements to the comparison.

The scalar is still not independently evaluated. Whole-system primitivity does not imply its nonvanishing at length two. `ATTEMPT_02_UNIFORM_ENDPOINT.md` correctly retains dim Sel_rel = dim Sel_p + 1 - epsilon and stops before discarding excess Selmer directions. No uniform upper bound, rational scalar across primes, or new seed witness follows.

Integrity: the input return manifest passes 59/59, its nested prior-input manifest passes 33/33, and all four loose files match the ZIP. The checked scripts were copied into this output folder before execution. No input, project record, repository or memory was edited; no external message, push, paid computation or seed production was performed.

FIN, ORDER9 and Q36 are unchanged.
