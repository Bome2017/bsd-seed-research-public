# Actual CM source comparison on the 167 control

Date: 2026-10-11. Predecessor: lab commit `19866bd9ef40cb1abd82a964fe4de16685902adc`.

**Result: ACTUAL_CM_COMPARISON_NONZERO_MOD5; SQUARED_RATIO_4.**

The missing source indices have now been controlled on the admitted 167 model. For the normalized CM source and the previously specified component coordinate,

\[
 r^2=9,\qquad n\equiv r\pmod5,\qquad k^2=1\pmod5,\qquad (n/k)^2=4\pmod5.
\]

Thus the actual CM comparison is a **nonzero** multiple of the constructed-point comparison. Its multiplier is one of **2 or3 modulo5**. This run does not choose between these two signed values. It closes the control experiment's source-nonvanishing question, not its remaining orientation-sensitive sign and not a seed BSD obligation.

Grade: written geometric/arithmetic deduction with executed exact and ball-arithmetic computations, under the explicitly retained C3/global-torsor inputs and classical modular-degree record. Separate same-team audits were performed. This is not external certification, formal verification, or a novelty claim.

## Which source was calculated

The base curve is E0=[1,1,1,3,12], conductor2541, with the predecessor's saturated points P1,P2. The raised curve is

\[
 C:y^2+xy+y=x^3+x^2+1878418x-485198548,
\]

of conductor424347, with Y=(480,22723). Work over K=Q(sqrt(-19)), on the Shimura curve of discriminant501 and Eichler level847. Let pi:Jac(X)→C be optimal, P its maximal-order CM point, and ξ the rational degree-one Hodge class.

Write the Hodge-normalized source as H=pi([P−ξ])=rY. The actual integral divisor used to clear degree is

\[
 D=[2(T_5-6)-(T_{13}-14)]P.
\]

Its eigenvalue on C is−2, so pi(D)=−2H. We calculated **H=±3Y**, hence pi(D)=±6Y. The base eigensystem gives the correction eigenvalue3, whose inverse appears in the canonical residual CM map. Thus its coefficient is n≡(−2/3)r≡r modulo5. The rational representative D/3 has coefficient ±2; the Hodge lift has coefficient ±3 and gives the same residual source. They must not be identified as rational classes. Using the raw index6 without the inverse correction would give a different squared comparison.

The component factor k is the image of the specified source generator in C's split-I5 component coordinate at167. It is independent of the global point Y, whose own singular localization is zero.

## How the two indices became calculable

**1. Discrete CM coefficient.** Fresh unrestricted eclib saturation certifies Y as a primitive rational generator. Direct enumeration gives #C(F4)=8 and #C(F5)=9, excluding all torsion over K. With the retained rank-one/rank-zero-twist bounds, C(K)=C(Q)=Z·Y. The integral CM image therefore has an integer coefficient. This is what permits exact recovery from a sufficiently narrow height enclosure.

**2. Actual degree and period normalization.** Pastén's degree comparison applies to the nonsquarefree level847. Its two component-image factors are1 because they divide both9 and16. Its two component-cokernel factors are equal and divide14 and5, so both are1. Therefore δ0/δX=70. The Cremona classical degree record δ0=20576640 yields δX=293952; the original classical degree computation was not rerun. Semistable-prime support and the Manin-divides-degree theorem imply c0=1: only11 could divide c0, and11 does not divideδ0. No conjectural unit normalization is used. See [the independent arithmetic review](component/BASIS_AND_DEGREE_REVIEW.md).

**3. CM height and exact extraction.** The quaternionic Gross–Zagier formula, with its K-height convention, reduces the actual index to

\[
 r^2=\frac{\sqrt{19}\,L'(C,1)L(C^{(-19)},1)}{280\,\operatorname{Area}(C)\,\widehat h(Y)}.
\]

Executed Arb arithmetic, exact elliptic coefficients, explicit infinite-series tails and a separate Tate-height calculation enclose the right side in

\[
 [9-8.27\cdot10^{-23},\;9+8.27\cdot10^{-23}].
\]

The integral corrected point makes 2r an integer, so this interval isolates r²=9. This is bounded discrete identification, not rational recognition with an arbitrary denominator limit. The height convention and the source's degree correction remain visible in [the CM derivation](cm/RESULT.md).

**4. Component normalization from the small base graph.** The actual base Brandt space has176 vertices, all weights1. The exact simultaneous mod5 eigenspace for T2,T13,T17 is one-dimensional, and its primitive eigenvector has norm144. This both supplies the specific base-freeness hypothesis and determines the doubled-vertex norm288.

The actual elliptic character vector lies in the residual gradient line. A mod25 monodromy calculation, using an even-supported degree-zero divisor on which the old and literal graph normalizations agree, gives

\[
 \delta_X/k^2\equiv-36\cdot288\equiv2\pmod5.
\]

Since δX≡2, k²=1. No graph eigenvector is substituted for the actual quotient vector without proof; no general optimality-to-component-surjectivity theorem is assumed. See [the graph proof](comparison/GRAPH_NORM_COMPARISON.md).

## Composition with the previous global comparison

The predecessor constructed one global isomorphism f167:E0[5]→C[5] and proved

\[
 \kappa_C(Y)=f_{167*}\kappa_{E0}(2P_1+P_2).
\]

This return identifies the Hodge CM image as ±3Y, and proves that the canonical normalized residual CM source is its same mod5 Kummer class. It also controls the separate component factor. Consequently the former constructed-point tensor becomes the actual CM tensor after multiplication by n/k, whose square is4 and which cannot vanish modulo5. The predecessor's detecting local pairs therefore remain detecting pairs for the genuine CM source. The result is global in the control model; it was not inferred by fitting scalar values at a few local primes.

## What this contributes to the seed-directed process

The experiment now has an executed example in which both previously unknown source factors are arithmetically controlled. The reusable procedure is: certify the point lattice; compute the degree ratio with its component corrections; prove the differential normalization; use an applicable height identity to identify the actual CM image; use the small base graph to normalize the component map; then compose with the established global torsor comparison.

The rank-one Gross–Zagier theorem is the independent arithmetic input that made this control calculation work. It is not a rank-two theorem for the seed. A seed continuation must supply the corresponding **actual source identity or adequate content control**; running more copies of this control does not supply uniformity. In particular this result gives no identity equating the seed's Kato derivative or all its tame coefficients with the control value.

The remaining signed value on this model requires an oriented CM-image calculation. A height square cannot choose that sign. The separate seed transfer and control across coefficient primes remain open. **FIN, ORDER9 and Q36 are unchanged.**

## Evidence and limitations

- Fresh exact base Brandt calculation plus a separately implemented check of its saved integer matrices and residual dimensions.
- Fresh complete point saturation; independent small-field torsion and index checks.
- Executed ball-enclosed L-values, periods and canonical height; parent replay completed.
- Source-level degree, Manin and height-convention checks; same-team review of the component and graph arguments.
- Retained rather than freshly recertified: the classical modular degree, antecedent rank bounds, geometric C3 transport and preceding global torsor identity. The package binds those inputs explicitly.

The checks do not construct a seed class group, evaluate a seed Kato derivative, certify the sign of n/k, or prove a cross-prime theorem.
