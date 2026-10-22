# Positive Sha excess with a nonunit regulator: a new combined control

2026-10-12. **PAIRED_PREDICTION_REPRODUCED; POSITIVE_EXCESS_NONUNIT_REGULATOR_CONTROL_COMPUTED.**

This return continues the discovery experiment after the supplied Pro recheck. It independently computes the predicted partner value, then constructs and measures a new control combining the two features previously available only separately: independently established odd-primary Sha excess and a nonunit regulator. No seed coefficient or BSD endpoint is claimed.

## 1. The paired prediction became an actual calculation

For the earlier d=43737 control, a fresh A-side modular-symbol calculation gives

    L2_A = 4*5 + O(5^2),
    det H_U,A = 4+3*5+5^2+5^3+2*5^4+O(5^8),
    Q_A = 1+O(5).

The producer receives neither F's numerator nor its regulator. These agree with the exact paired prediction L2_F=5 L2_A, detH_F=detH_A, Q_F=25 Q_A, at available precision. A separate height calculation checks M^t H_F M=5 H_A to O(5^11), and logarithm functoriality to O(5^10).

The supplied Pro checker was also replayed and reproduced its mathematical output. The exact identity remains a theorem about the specified Neron periods, point pairs and canonical ordinary-height convention; numerical agreement is not a proof that either quotient equals its integer approximation exactly. Both extractions share PARI's modular-symbol implementation.

## 2. New arithmetic control

Set d=329233 and

    F: y^2+y=x^3-x^2-847680091476076*x-9499397825675855099600.

It is the d-twist of [0,-1,1,-7820,-263580], with conductor 1192338051179. It has algebraic rank two, trivial rational torsion, and good ordinary non-anomalous reduction at5 (a5=-1, #F(F5)=7).

An independent isogeny-Selmer calculation gives

    dim_F5 Sha(F/Q)[5] >= 2.

This lower bound does not use a numerator, height, class number, BSD, or Sha finiteness. Its computational rank upper bound is retained from PARI's two-descent. A separate exact checker verifies the rational map, point matrix, reduction certificates of5-saturation at7 and109, real-kernel/period calculation and local Tamagawa factors. See COMBINED_EXCESS_PROOF.md and outputs/combined_exact.json.

The actual direct power-series extraction gives

    L2_F = 3*5^4 + O(5^5),
    det H_U,F = 3*5^2 + 3*5^3 + 4*5^4 + 4*5^6 + 5^8 + O(5^11).

Therefore

    v5(L2_F)=4,   v5(det H_U,F)=2.

With the ordinary Euler factor and actual torsion/Tamagawa normalization, independently recomputing the saved digits yields

    Q_F=25+O(125),   v5(Q_F)=2.

The unit check is Q_F/25 = 3/(3*4*4) =1 mod5. The numerator is calculated first, with neither a regulator nor a Sha value supplied to it.

| Control | v5(L2) or indicated prime valuation | Regulator valuation | Corrected quotient valuation | Independent positive odd-Sha bound |
| --- | ---: | ---: | ---: | --- |
| Prior selected controls at7,13,31 | 1 | 1 | 0 | Not supplied by those experiments |
| d43737 at5 | 2 | 0 | 2 | dim Sha[5]>=2 |
| **d329233 at5** | **4** | **2** | **2** | **dim Sha[5]>=2** |

The displayed point pairs are5-saturated. Their prime-to5 indices are not certified; numerical unit statements refer to those pairs. Valuation conclusions are unaffected by such an index.

## 3. Geometry and a sharper selection rule

The new residual height/logarithm data are

    H_scalar,F/5 mod5 = [[4,2],[2,1]],
    log(Q)/5 mod5 = (1,3),
    log(P)/5 mod5 = (0,0),
    M=[[-2,1],[-1,-2]], detM=5.

The height radical, logarithm kernel and image of M mod5 are the same line, spanned by (1,3). Thus this is the coincident-line configuration seen in an earlier cancellation control, not the seed17 distinct-line configuration.

There is a useful derived selection lemma. Under the actual height and logarithm identities, a rank-one residual height on F has radical im(M mod5). If the A-side normalized logarithm row is nonzero mod5, that radical must differ from F's logarithm kernel. This gives an arithmetic filter for selecting a closer control before paying for its numerator. The new case fails that primitive A-log premise; it is not silently counted as a seed-geometry match.

The local point indices can also be determined: w_F=0 and w_A=1. The latter follows from ell_A=ell_F M, detM=5, and the displayed rows. Thus equal regulator determinants coexist with unequal local point indices. See PAIRING_AND_GEOMETRY.md for the deduction and exact scope.

## 4. How the new case was selected and computed

Two predeclared bounded screens extended the prior class-group filter, then selected exact-rank-two cases by height geometry before calculating their numerators. They examined11052 eligible real quadratic fields, retained49 class-group candidates, and measured9 rank-two point pairs. All candidate rows, including rank-two cases lacking a second supplied point, remain in the saved logs. The search stopped at d329233, the first measured nonunit-regulator case. The class-group filter suggested the candidate; it is not an input to the final Sha lower-bound proof.

The unmodified whole-twist moment calculation overflowed its4GB memory allowance. That output is rejected. A small, audited partial-sum patch evaluates the identical character sum in batches. Full moment vectors agree exactly with the unmodified producer for d13,29,-7 and the saved d43737 case. The new calculation then completed using512MB.

Precision7 supplied only L2=O(5^4), which was recorded as a lower bound. An adaptive precision8 calculation took about214seconds and supplied the nonzero next digit above. No zero residue was promoted to an exact zero or valuation. ENGINE_REPAIR.md and the source patch preserve this distinction and the arithmetic of the repair.

## 5. Effect on the seed research

We now have a control showing both cancellation of nonunit regulator factors and independently proved residual arithmetic excess in one calculation. An explanation of the seed's desired cancellation can be tested against this combined case as well as the earlier unit-quotient examples. The exact isogeny transformation also constrains that explanation quantitatively.

This does not transfer a Sha bound to the seed. The control's rational5-isogeny makes its residual representation reducible; the seed's retained representation has full image. Its coincident-line geometry also differs from the seed17 configuration. The full-image positive-excess control and the combined distinct-line control remain unfilled. No claim that these remaining cells are impossible is made.

No exact order25, Sha finiteness, infinite-precision quotient equality, or new seed-primary vanishing is established. **FIN, ORDER9, Q36 and seed prime coverage remain unchanged.** The result is a new arithmetic experiment and written control proof, not independent human certification or formal verification.
