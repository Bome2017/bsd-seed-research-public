# Independent same-team audit of the local detector and splitting field

Date: 2026-10-13.

Reviewed input: `input/BSD_LOCAL_OBSTRUCTION_DETECTOR_2026-10-13/PROOF.md`, with its stated baseline `257af6888c80fda3b90d481cf2d94f9950701811`.

**Verdict: LOCAL_DETECTOR_AND_DEGREE5_SPLITTING_SUPPORTED_UNDER_RETAINED_INPUTS.** No mathematical error was found in the requested detector, splitting-field, or period-index passages. This is a separate-agent written review and independent exact arithmetic, not a human review, proof-assistant certificate, novelty assessment, or new seed bound.

## 1. Why the detector really factors through Sha

The source cohomology is H^1(Q,F[hatphi]), with Kummer subgroup A(Q)/hatphi F(Q). At the chosen split place above 11, the norm-one/anti-invariant description identifies localization with Q_11^*/Q_11^{*5}. Its two coordinates are valuation modulo 5 and the unit residue modulo fifth powers. The pro-11 principal-unit group contributes nothing because raising to the fifth power is bijective there.

This description is compatible with multiplication and annihilates global fifth powers, so Delta is defined on the Selmer classes. Checking Delta on P1 and P2 is sufficient under the retained rank-two, no-rational-5-torsion and 5-saturation inputs: those points span A(Q)/5A(Q), and 5A(Q) is contained in hatphi F(Q). Thus the detector kills the entire rational-point Kummer image, not just the two selected classes. It genuinely induces

    D_11: Sha(F/Q)[hatphi] -> F_5^2.

Its two displayed columns have determinant 4 modulo 5, so it is surjective and proves independence of the epsilon and alpha11 torsor classes. The proof needs no class-group or fundamental-unit computation for this lower bound. It still needs their global Selmer membership and the retained rational-point spanning statement.

The distinction in Section 5 is correct. Localization of these torsors in H^1(Q_11,F) is zero. The detector measures their local finite-coefficient Kummer lifts before forgetting the isogeny-covering structure. There is no contradiction with everywhere local solubility.

A surjection onto F_5^2 supplies no upper bound by itself. Its being an isomorphism depends on the separate retained S-class dimension calculation. The new package states this correctly.

## 2. Independently recomputed arithmetic

I wrote and ran `audit/independent_local.py` with Sage, without using the submitted checker implementation. The output `audit/independent_local.json` records:

| Element | Exact valuation at the selected prime | Residue of leading unit | Signature |
|---|---:|---:|---|
| epsilon | 0 | 6 | (0,4) |
| alpha11 | 4 | 1 | (4,0) |
| f(P1) | 0 | 1 | (0,0) |
| f(P2) | 0 | 1 | (0,0) |

The 11-adic square root was computed through the specified Hensel root of x^2-x-10934. The exact rational point coordinates were substituted in the original descent function. These independent calculations agree with the packet; no previously printed signature was passed into the computation as a result.

This arithmetic does not independently recertify the rank bound, saturation, differential, Tamagawa inputs, or Miller–Stoll membership theorem. Their role remains explicit.

## 3. The splitting field proof is sound

I independently verified irreducibility of P(X)=X^5-5X^3+5X-46846 over F_11. The packet's two Rabin conditions are sufficient: degree 5 is prime, and divisibility into X^(11^5)-X also ensures squarefreeness. Consequently M=Q(t) has degree 5 and is disjoint from the quadratic K.

I also checked the polynomial Chebyshev identity and verified directly, in the exact degree-ten compositum M(sqrt(43737)), that

    z=(t+224*sqrt(43737)/(t^4-3*t^2+1))/2

satisfies z^5=epsilon. The denominator is nonzero because the displayed identity has the nonzero right side 46846^2-4=224^2*43737.

The finite-coefficient Kummer class restricts to zero over MK. Restriction from M to MK is injective on H^1(M,F[hatphi]): corestriction composed with restriction is multiplication by 2, which is invertible on this exponent-five group. Therefore the class itself is zero over M and the genus-one covering has an M-point. This conclusion does not require explicit projective coordinates of that point.

The nonzero torsor class has order 5, so its period is exactly 5. For any finite extension L giving a point, restriction/corestriction forces 5 to divide [L:Q]. The exhibited degree-five splitting field then gives index 5 and minimum splitting degree 5. This reasoning is valid without assuming finiteness of Sha.

## 4. Covering convention and equation checks

The packet preserves the necessary distinction between Fisher's kernel generator and the one used in the normalized f-function. Inversion changes the signature's sign and does not affect local solubility, nontriviality, or the splitting-field argument. Its model has Jacobian F and is a dual-isogeny covering of A; it is not being identified with a full multiplication-by-five cover.

For this focused audit I retained the earlier matched Fisher theorem and geometric smoothness calculation. I did not rerun the five-chart Groebner computation or independently reconstruct a projective-coordinate covering map. The packet does not claim that it did either. Its local Hensel checks supplement the global membership theorem; they are not presented as an all-place solubility proof.

## 5. Limits and safe conclusion

The proposed general map from full p-Selmer modulo rational points to a local Kummer quotient modulo the localized global point image is well-defined. Its kernel can contain the whole Sha[p]. Therefore a zero local target or zero detected signature cannot prove vanishing. Section 8 accurately records this limitation and does not treat the seed's irreducible representation as an automatic vanishing mechanism.

The safe new conclusion is an explicit one-place arithmetic detector of two actual obstruction classes on the positive control, together with a degree-five splitting field and exact period/index for the unit covering. This reduces the global arithmetic needed for the lower-bound proof and exposes the local-versus-global point-image mismatch. It does not give an independent upper bound for unresolved seed primes. FIN, ORDER9 and Q36 remain unchanged.
