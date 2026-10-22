# Handoff for Pro 6: actual source, variable critical points, seven coefficients

This return continues the supplied cohomological-jet task. Its status is W3_SOURCE_LAW_PROVED_WITH_VARIABLE_SPECIALIZATION_CERTIFICATE, at written-derivation/imported-theorem grade under retained inputs. It is not a cofinite bound.

## Read in this order

1. REPORT.md and LOCAL_REVIEW.md.
2. ARITHMETIC_SOURCE.md and VARIABLE_WEIGHT_INDEX.md.
3. TEN_POINT_CERTIFICATE.md.
4. ARITHMETIC_LOW_JETS.md and FINITE_ARITHMETIC_SOURCE.md.
5. The bound context copies, source locators, and formal checks.

## Exact new claim to review

Let Z_p be the actual optimized integral Euler system in U=V(T)nu_S^(-1), and F_p its coordinate in the proved rank-one integral local quotient. Then, on the retained cofinite ordinary domain,

    F_p mod (p,T,S)^4 != 0  ==>  Sha(E/Q)[p^infinity]=0.

The proof uses ten critical points, not the old diagonal:

    (w,s)=(10+i,7+j), i,j>=0, i+j<=3.

The representations are D(g_w tensor omega^(w-s))(w+1-s), in the explicit cohomological convention, and 1<=w+1-s<(w+2)/2. They have the seed's residual Selmer conditions. Their own Euler-system indices bound the seed. No comparison to the old normalized z_g is required.

## Review priorities

* Check the source application and character component: the tautological cyclotomic character is sent to chi nu_S, so its principal coordinate is p+(1+p)S. Verify the actual coefficient module rather than copying an L-value formula with an untransported involution. The optimized source is Ochiai 2006 Theorem 6.11/Corollary 6.17 and the construction in arXiv:1802.06427v3 Theorem 4.12. Its normalization is imported, not accomplished by declaring smoothing factors to be units.
* Check the residual local-condition comparison for all ten weights, including discrete coefficients. The ordinary exponent range, non-anomalous characters, bad-prime residual zeros and the two rational directions are explicit.
* Check the integral index proof for this Euler system, with the unit transvection and the Tor cancellation h-t<=a0, a=a0+t. Do not replace it by naive specialization of a two-variable characteristic ideal.
* Check the global low-jet proof separately. It uses the full family image in retained COFINITE_HIDA_CONTROL.md §6 to meet the integral deformation Euler-system hypotheses. A square Selmer complex has determinant dividing F_p; its characteristic-zero specialization contains the two actual rational point classes. That is the reason the constant and two linear coefficients vanish. If this additional proof is not accepted, retain the ten-coefficient criterion: the ten-point theorem does not depend on eliminating those coefficients.
* The earlier cofinite Hida result remains a retained written derivation, not newly independently certified here. Its status travels with every claim in this packet.

## The actual arithmetic calculation after review

Prove nonzero content, outside a fixed finite set of ordinary p, of

    a T^2+b TS+c S^2+d T^3+e T^2 S+f T S^2+g S^3,

where a,b,c are taken modulo p^2 and d,e,f,g modulo p. These must be the coefficients of the actual class supplied by the arithmetic source. They are not free polynomial variables. The return has proved three other coefficients zero; it has not evaluated these seven.

One nonzero jet is sufficient at that p because of the ten-point theorem. A uniform arithmetic nonvanishing statement would close the ordinary tail. A nonzero arbitrary power series, rational critical-value nonvanishing, or a formal control is not that statement.

The four-weight gluing in FINITE_ARITHMETIC_SOURCE.md gives an exact source for the jet, not a claim of an affordable finite-level evaluator. No fixed-prime campaign, source-only repair loop, or new automatic job is authorized by this handoff.

No equality with C_p has been proved. If a matched collision is found, write the actual identity before classifying it. Neither the source theorem nor the ten-point argument supplies supersingular coverage, FIN at excluded primes, ORDER9, or Q36.
