# A rank-two positive-excess control, with an independently computed numerator

2026-10-12. **POSITIVE_ODD_EXCESS_CONTROL_CONSTRUCTED; NONUNIT_CORRECTED_RATIO_OBSERVED.**

This continues the actual coefficient–regulator experiment after Pro's review. It constructs the missing kind of positive control instead of collecting further unit-quotient examples. The result is a written isogeny argument supported by exact computations and a new p-adic coefficient. It is not an independent review, a novelty claim, a formal certificate, or a new seed bound.

## Result

Put

    F: y^2+y = x^3 -14959712463303*x -22270654620235278500.

This is the quadratic twist by d=43737 of [0,-1,1,-7820,-263580], a conductor-11 curve. It has conductor 21042176859, algebraic rank two, trivial rational torsion, and good ordinary non-anomalous reduction at 5: a_5=-1 and #F(F_5)=7.

**An isogeny-Selmer calculation, independent of L-values, gives**

    dim_F5 Sha(F/Q)[5] >= 2.

The proof uses Cassels' isogeny-Selmer ratio, an explicit degree-five isogeny, exact point-map identities, and exact finite-field certificates of 5-saturation. It does not assume finiteness of Sha or BSD. Its rank upper bound and local reduction data are PARI computations. See [PROOF.md](PROOF.md).

Separately, an actual twisted modular-symbol calculation gives, with U=gamma-1 and gamma=6,

    L2,5 = 4*5^2 + O(5^3),
    det H_U = 4 + 3*5 + 5^2 + 5^3 + 2*5^4 + O(5^8).

Hence

    v_5(L2,5) - v_5(det H_U) = 2.

Including the ordinary Euler factor and the actual Tamagawa/torsion factors, the quotient for the displayed 5-saturated point pair is

    Q_5 = 25 + O(125).

No regulator or Sha value was supplied to the numerator routine. No L-value was used to prove the positive Sha lower bound. The coefficient came from the conductor-11 symbol with quadratic character d=43737; we did not construct a modular-symbol space at conductor 21 billion.

This does **not** prove #Sha(F)=25, finiteness of Sha(F), or exactness of its 5-primary order. The displayed points are proved 5-saturated; their index at other primes is not certified here. Accordingly the leading-unit statement refers to that specified point pair. The valuation difference is unaffected by a prime-to-5 point index.

## What this changes for the seed experiment

The previous exceptional controls had nonunit regulators but unit corrected quotients. That alone could not discriminate between regulator-only cancellation and additional arithmetic content.

The new control has independently established odd-primary excess and a corrected quotient with **two factors of 5 remaining**. Thus a proposed universal explanation that cancels all content merely because the curve has rank two and good ordinary non-anomalous reduction is inadequate. This is a genuine positive control for arithmetic excess, rather than a Sha prediction taken from a numerical BSD quotient.

There are two important mismatches with the seed. This control has a rational 5-isogeny, so its residual representation is reducible; the seed's retained representation is irreducible. Its U-height determinant is a unit, whereas the seed at 17 has a rank-one residual height matrix. We have not supplied the ideal control with both independently established odd excess and the seed's distinct-line, nonunit-regulator geometry.

| Arithmetic sample | Regulator valuation in U coordinate | Corrected quotient |
|---|---:|---|
| Prior exceptional controls at 7,13,31 | 1 | unit, to their recorded precision |
| New control F at 5, with Sha[5] lower bound | 0 | valuation 2 |
| Independently established excess plus nonunit regulator | not yet supplied | not yet measured |

This narrows the discovery problem. An explanation must distinguish the new control from the unit-quotient controls using arithmetic beyond a regulator determinant, and must account for the different residual representation before being transferred to the seed. The 5-isogeny descent is a way to construct/test controls, not a proposed 5-isogeny of the seed.

## How the control was found

1. The first published candidate checked, [1,-1,0,94,9], has exact rank two but a_3=0 and only a numerical Sha_analytic=9 claim in the located source. It was not admitted as an ordinary positive control.
2. Fisher's published order-five covering table explicitly limits its examples to ranks zero and one. Those were not relabelled rank-two controls.
3. A bounded, newly recorded screen of 1000 admissible quadratic twists of the conductor-11 isogeny class found 62 exact rank-two cases. Their relative isogeny indices gave no asymmetry; that does not prove their Sha groups trivial.
4. Six of those quadratic class groups had 5-torsion, but it disappeared after quotienting by the ideal class above 11. This suggested filtering on the surviving quotient first.
5. The structure-guided screen stopped at its third surviving class-group candidate, d=43737. An exact rank-two descent and a changed isogeny point index then gave the independent positive lower bound.

The class-group calculation suggested the candidate; the final positive-control proof uses the independently checked isogeny ratio and point indices. It does not identify an unproved class-group-to-Sha map.

## Checks and limitations

- PARI/GP 2.17.3 returns rank interval [2,2].
- A separate standard-library Python implementation verifies the rational isogeny equation and point-image matrix exactly.
- At primes 7 and 19 it counts the reduction groups and verifies two independent mod-5 evaluation rows for each point pair. Given the rank upper bound, these certify 5-saturation without relying on a floating regulator ratio or on PARI's saturation routine.
- The p-adic numerator calculation was replayed. Direct extraction of the power-series coefficient agrees with the derivative conversion at the stated finite precision. Both use the same PARI overconvergent modular symbol, not independent modular-symbol implementations.
- The saved digits independently give Q/25=4/(4*4*4)=1 mod5. The three denominator factors are the leading regulator unit, the ordinary Euler factor and the Tamagawa product.
- Two lower-memory numerator attempts overflowed and produced no coefficient. They are rejected and preserved. The valid run used a fixed 4 GB stack and approximately ten seconds of numerator computation. Process exit zero is never the acceptance test.

The scalar height geometry is

    log(P)/5 mod5 = (0,2),
    H_scalar/5 mod5 = [[3,3],[3,1]],

whose determinant is 4 mod5. It is therefore not the seed's nonunit-regulator configuration.

**FIN, ORDER9, Q36 and seed coefficient-prime coverage remain unchanged.** What is added is an actual rank-two control with independently derived odd-primary excess and a separately evaluated numerator that retains excess after the regulator correction.
