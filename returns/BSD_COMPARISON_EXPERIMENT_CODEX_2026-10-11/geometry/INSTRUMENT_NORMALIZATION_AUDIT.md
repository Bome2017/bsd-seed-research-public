# Independent desk check of the executed mixed-place instrument

Later continuation: `GLOBAL_TORSOR_REVIEW.md` now proves both proposed global Kummer identities using the saved exact torsor maps. The local-only status below describes the earlier instrument audit and is superseded specifically for those two identities; the CM source indices remain open.

Date: 2026-10-11. Reviewed `checks/mixed_instrument.py` and the completed output as present at the audit time. This checks the mathematical normalization of that script under the separately checked global torsion maps and the earlier model admission. It is not an independent replay of every Sage finite-field computation, a Shimura-CM evaluation, or a BSD theorem.

**Verdict: the instrument computes the stated finite-coefficient mixed-place tensor, with an explicit local sign convention. No hidden Weil-similitude factor is discarded.** Its values belong to actual rational points on the raised curves; they are not the original CM-source values.

## 1. The finite Kummer operation is actual division

For every place used, q modulo 5 is 2 or 3, and both point-group orders have 5-adic valuation one. Thus residual Frobenius has distinct eigenvalues 1 and q, and the full rational five-torsion is its one-dimensional invariant line.

The script constructs a fifth division point Q of the given point over F_(q^5). If c=Frob_q(Q)-Q then Frob_q^5(Q)=Q implies

    (1+Frob_q+...+Frob_q^4)c=0.

On the q-eigenspace the operator is 1 modulo 5; on the 1-eigenspace it is 0. Consequently c lies in the invariant line. The script additionally checks Frobenius invariance and that every division point in that field gives the same c. Differences of those division points are invariant five-torsion, so this independence is also explained theoretically.

Over the inert quadratic completion the residue Frobenius is Frob_q^2. The restricted cocycle value is therefore c+Frob_q(c)=2c. This explains every factor 2 in the script. It is not an arbitrary cofactor projection such as [#E(F_q)/5]P. The finite-local quotient is identified with its invariant representative because the other Frobenius-squared eigenvalue is q^2 != 1.

## 2. The toric direction and its scale

The script enumerates all 24 nonzero base five-torsion points over F_(ell1^4) and applies the exact globally defined forward torsion map f:E[5]->E1[5]. Exactly four images reduce to smooth points on the nodal target; these identify f^(-1)(mu_5), the toric direction. The other 20 images reduce to the node. This uses the actual map, not a separate local isomorphism.

For a chosen smooth image (x,y), completed-square coordinate YY=y+(x+1)/2 and selected tangent slope v at the node x=r, it sets

    zeta=(YY+v(x-r))/(YY-v(x-r)).

This is the inverse of the parametrization used in `toric_mu5.py`; the difference is an explicit orientation sign. It is a multiplicative coordinate on the smooth nodal group. Choosing the corresponding tame-inertia generator makes the singular Kummer generator evaluate to f(T). Pulling back through f yields T in the base representation.

The numbers

    a_i = log_zeta e_E(T, 2*kappa_q(P_i))

therefore give the base finite-point evaluations against that singular generator, up to the one conventional sign attached to the order of the local duality pairing. If local duality is defined with finite class first, reversing the displayed Weil-pairing order changes every a_i by a common minus sign. The script should be reported with its displayed convention, not identified with an independently normalized Shimura component generator without its factor k.

The square root v is explicitly selected separately at the two raised places. Reversing v inverts zeta and flips the instrument's sign. Thus raw signs across different ell1 are not a certified common global Shimura orientation. Squares remove this local sign ambiguity; matching the actual component convention remains part of k.

## 3. Similitude and all other scalar choices cancel as required

At ell2 choose a nonzero base invariant torsion point G. The script writes the two base restricted Kummer values as b_i G and the raised-point value as b_Y f(G). It computes

    r=a_1*b_2-a_2*b_1,
    c_Y=b_Y/r,

only if r is nonzero.

Changing G to tG multiplies both b_i and b_Y by t^(-1), leaving the ratio unchanged. Changing the toric point T to tT changes both the Weil pairing and zeta by exponent t, leaving a_i unchanged. Changing the global torsion map f to sf changes zeta to zeta^s and f(G) to sf(G): both a_i and b_Y are multiplied by s^(-1), so c_Y remains unchanged.

The computation always uses the base curve's Weil pairing. If f has nontrivial Weil similitude, that effect is already present because its target multiplicative coordinate supplies zeta while its source supplies T. Replacing the base pairing with the target pairing without its multiplier would be a different calculation. No such replacement occurs.

## 4. What the completed output says

The current script uses q<500. It does not obtain four detecting tests per partner in that range; the output contains:

- At ell1=113: two detecting places 103 and 227, with c_Y=4; one zero-determinant place 373, with b_Y=0.
- At ell1=167: three detecting places 193, 227 and 373, with c_Y=1.

The zero-determinant row is retained and not divided. These are bounded exact observations, not an all-prime constancy theorem.

They suggest sharper local comparisons. For 113, a=(0,4), so the observed relation b_Y=4*r is b_Y=4*b_1. At 167, a=(1,3), so b_Y=r is b_Y=2*b_1+b_2. Equivalently, at the places tested:

    f^(-1) kappa(Y_113) = kappa(-P_1),
    f^(-1) kappa(Y_167) = kappa(2P_1+P_2).

Only the localized equalities have been computed. They are candidates for genuine global Kummer-torsor identities, not established equalities in global cohomology. No Sha=0 hypothesis is needed to formulate or test them.

A direct global test would compare the actual degree-25 fifth-division fibers of those base points and of Y, then check equivariance for Q -> Q+T under the fixed f. A field isomorphism without affine-equivariance verification is insufficient. Proving either identity would validate a common-source relation for the instrumented points, but the actual CM trace coefficient and component-map index would still need evaluation.

## 5. Limits preserved

A nonzero Y-coordinate at any test place proves the displayed Y is not globally 5-divisible. Together with a certified rank-one bound and absence of rational 5-torsion, this admits it as a basis modulo 5; it does not establish saturation at every prime. At ell1=167 the separately computed minus-19 twist rank bounds [0,0] make this a K-side rank-one instrument as well, subject to the torsion check.

The actual source remains pi_*(D_K), not Y. The tensor for that source still carries n/k from MIXED_PLACE_DIAGRAM.md. Instrument constancy, a rank-one raised quotient and verified residual congruence do not determine n/k or transfer to mod25. In particular the displayed bounded values do not supply the seed's derivative-content estimate.
