# The arithmetic comparison left by the experiment

This document separates exact source linear algebra, observed arithmetic, and an unconstructed comparison. It introduces no new BSD implication beyond the retained descent and analytic source theorems.

## A. Exact joint admission, not independent smallness of two pieces

Let B be a finite F_p source containing every possible class under consideration; let D:B->Q be a linear collection of necessary global and local defects. Let W be the actual rational-point image, with W contained in ker D. Once the source and Kummer comparison are authenticated, ker D/W is a containing space for the excess. Equality with Selmer is not needed to obtain an upper bound. An incomplete list of generators is insufficient.

For the valuation-zero source B0, the Kummer field sequence has the form

    0 -> U -> B0 -> C -> 0,

where U is the unit source modulo p-th powers and C the appropriate p-torsion ideal-class source. Restrict scalar components only through justified exact projections or explicit intersections. Given c in C, choose a lift beta in B0 and put

    kappa_D(c) = D(beta) mod D(U).

Changing beta by a unit changes D(beta) by D(U), so the map is well-defined. Its kernel consists precisely of class directions admitting a repair by a unit. Consequently

    0 -> U intersect ker D -> B0 intersect ker D -> ker kappa_D -> 0.

No assertion that B0 splits canonically is used. At primes where nonzero allowed valuation columns may occur, B0 must not replace B without either retaining those columns or proving their removal. The433 control illustrates this concretely.

For H=ker D, U_H=H intersect U, and V_H=H intersect B0, quotienting by W gives a filtration with dimensions

    unit excess      = dim U_H - dim(W intersect U_H),
    class excess     = dim V_H - dim U_H
                       - dim(W intersect V_H) + dim(W intersect U_H),
    valuation excess = dim H - dim V_H - dim W + dim(W intersect V_H).

These sum to dim H-dim W. The expressions come from the induced intersections and projections in H/W. They apply to the full authenticated source or to a specified span; a span computation is a lower/structural result, not a full upper bound.

In the new complete controls, H=W, dim U_H=2, and W is contained in U_H. Every excess term is zero. In the retained seed four-class span the filtration is valuation0, unit1, class1. Both situations have the same forward unit norm Smith factors(3,3), under the matched incidence theorem. Thus even an exact unit norm index alone cannot determine this quotient: it lacks the point intersections and the admitted class contribution.

## B. Common moments and their behavior under change of detector

For a fixed modular symbol Phi, cyclic character coordinate psi, and named period normalization, the degree-two moment is

    c2 = sum binomial(psi(a),2) Phi(a).

If the lower moments vanish modulo p, replacing psi by v psi with v nonzero modulo p changes c2 by v^2. The tame point-height determinant changes by the same factor. Their ratio is consequently independent of the primitive-root choice at a fixed conductor whenever that determinant is nonzero. The executable test checks the full primitive-root orbit for every copied tame table.

This generator invariance is not independence of the conductor or coefficient prime. Those comparisons require arithmetic beyond this polynomial transformation.

The successful seed rows exhibit

    c2 / ((a_ell-2) R_tame) /32 = 9 mod p,
    L2 / (epsilon R_U) *4/16    = 9 mod p.

The normalization32 is inherited from the previously specified comparison. The measurements test it; they do not derive an integral common realization theorem. The same-prime independent overlap is5. No use of a CRT fit turns these finite residues into proof that an unknown global object equals9.

The two failed-conductor examples have a zero point determinant and zero coefficient while their Euler factors are nonzero. At another conductor for the same curve and coefficient prime both are nonzero. These examples require a comparison to be valid before dividing by the determinant, or to track the loci where division is allowed. The seed3 control instead has a nonzero point determinant and zero coefficient. It is outside the good-coefficient-prime source domain and cannot be silently used to infer that domain's theorem.

## C. What has to be constructed rather than renamed

An actual unifying construction would give a map or identity relating the independently defined admission complex and the modular-symbol source, with the actual point plane and integral factors retained. The experiments provide tests for such a map:

1. Reproduce the corrected leading units, not just their valuations.
2. Account for a zero caused by a singular chosen point detector and its repair at another conductor.
3. Retain admitted non-point units and class lifts; do not predict equal excess from equal norm indices.
4. Work with a complete or proved containing source, including allowed valuation columns.
5. Avoid importing known Sha, q, BSD or a unit chosen from the answer into its construction.

This is a specification for falsifying a proposed comparison, not a proof of its existence. The published main-conjecture/leading-term identities calibrate several cases but do not supply independent cross-prime upper control just by writing Sha on both sides. The historical fixed-scalar, determinant-line and ETNC comparisons remain unresolved at their recorded arithmetic steps.

The present bounded experiment ends after these actual calculations and tests. Its strongest new discriminant is point placement and class admission, not a numerical feature of the coefficient primes. It supplies neither a held-out predictor for unresolved seed primes nor a proof that every sufficiently large prime has a good detector with nonzero scalar.
