# The actual seed cofactors at 5 and 17

**EXACT_NEW_LOG_AND_COFACTOR_CONTROLS; HEIGHT_VALUES_RETAINED.**
These are calculations on the seed's known rational points, combined with saved height outputs. They are not computations of a Kato class and do not settle a new primary component.

## What was recomputed

Use the minimal equation and the stated saturated basis. Direct finite-field counts give #E(F5)=8 and #E(F17)=24. For n=#E(Fp), exact rational elliptic-curve arithmetic computes nP_i and its formal parameter t=-x/y. Since n is a p-unit and t belongs to pZ_p,

    log(P_i)/p = t(nP_i)/(np) modulo p.

For p>=5 the integral formal differential gives log(t)=t modulo p^2. The script uses exact fractions, checks every resulting point against the curve, compares repeated addition with double-and-add, and repeats the logarithm residue with 2nP_i. It finds

    (log(P1)/5, log(P2)/5) = (0,2) mod 5,
    (log(P1)/17,log(P2)/17) = (2,13) mod 17.

This independently recovers P1's local divisibility at 5. Neither point is locally divisible at 17. This fact alone does not control the Kato coefficient.

## The saved heights and their convention

The September 25 canonical-model PARI and Sage outputs agree on the cyclotomic height at 17. The September 18 Sage calibration supplies the entries at 5. We read these actual outputs; neither engine was rerun. Set H_gamma=H_native/log_p(1+p), entry by entry. Then

    H_gamma mod 5  = [[2,2],[2,0]],
    H_gamma mod 17 = [[13,5],[5,15]].

The saved higher precision establishes

    v5(det H_gamma)=0,   det H_gamma=1 mod 5;
    v17(det H_gamma)=1,  det H_gamma/17=13 mod 17.

The checker parses the recorded height digits and independently recomputes these determinant facts; it does not infer the second fact from a singular matrix modulo 17. The old PARI raw-model result at 17 is deliberately not used. Its leading regulator digit was wrong, as the existing canonical-model review records.

Combining the fresh logarithms with the saved heights gives

    adj(H_gamma) log(P)/5  = (1,4) mod 5,
    adj(H_gamma) log(P)/17 = (16,6) mod 17.

In both cases the cofactor vector has content valuation exactly one. At 17 the determinant is nonunit while the divided cofactor vector is primitive. This is actual seed data, rather than the abstract diagonal-matrix example in the submitted note.

## What this says about the proposed derivative calculation

The numerical heights are in the record's Stein–Wuthrich / Mazur–Stein–Tate convention. BKS constructs the height by its stated ordinary splitting and Bockstein convention. A common unit rescaling of the height preserves the following valuations and projective directions; an unproved p-power rescaling would not. We retain the classical-height identification as a required convention match, rather than treating calibration on another curve as its proof.

With that match, let K_p be the quadratic Coleman coefficient of the *actual* class, as defined in COMPARISON_REVIEW.md. The formula gives

    min(v5(A5),v5(B5)) = v5(K5),
    min(v17(A17),v17(B17)) = v17(K17)-1.                (S1)

The zero-coefficient case is interpreted separately: the coordinate pair is zero, since the recorded matrices are nonsingular over Q_p.

Thus integrality itself forces K17 to be divisible by 17. If its valuation is exactly one, the derivative is primitive; if it is at least two, this particular derivative fails the primitive test. Merely finding K17=0 mod 17 does not distinguish those two outcomes.

If primitive, its projective residual coordinate direction is [1:4] at 5 and [16:6] at 17, with a common matched height scaling. The absolute coordinate residues still depend on the source scalar and height convention.

## What has and has not been evaluated

Reusing the saved m=5 and m=25 symbol tables, the old exact downstream adapter again gives the standard cyclotomic quadratic coefficient 2 mod 5 in the omega_1 period convention (1 mod 5 in the total-real-period convention). This is an old arithmetic result reproduced here. It agrees with the required valuation-zero calibration at 5 after source matching; it is not a fresh Kato-coordinate certificate for the unspecified earlier homothety.

No value of the quadratic coefficient modulo 17^2 was produced. The retained regulator report itself leaves that coefficient as a premise. A previously reported vanishing mod 17 supplies no second digit. We did not substitute the already-known tame 17-primary witness for that missing digit.

The cofinite normalization lemma gives a way to avoid arbitrary homothety errors when defining one fixed source across p. Its finite exceptional set has not been computed, so it cannot simply be invoked to certify that this particular p=5 or p=17 source is matched.

## Consequence for continuation

This calculation narrows the arithmetic test without requiring regulator unitness. It does not supply the cross-prime estimate. The direct target is equality between the genuine quadratic coefficient's valuation and the **forced** valuation r-c+1 (ordinary case), with the height cofactor and determinant taken in one convention. A claim that L_2 must be a unit at every ordinary prime would be the wrong target for this seed.

No additional p=17 symbol computation is authorized or recommended as a uniform proof. At 17, a second-digit calculation would be a bounded calibration only, at a prime already settled by another route.
