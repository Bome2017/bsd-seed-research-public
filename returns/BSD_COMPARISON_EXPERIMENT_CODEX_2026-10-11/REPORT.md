# Executed arithmetic-comparison experiment

Date: October 11, 2026. Status: **GLOBAL_POINT_CLASS_COMPARISONS_CONSTRUCTED_ON_CONTROL_MODEL; CM_SOURCE_INDEX_OPEN; NO_SEED_BOUND.**

This return executes the preceding discovery brief and follows an observed relation through an exact global construction. It is a computer-assisted written argument, with a separate same-team mathematical review. It is not a Lean certificate, an independent external certification, or a novelty claim.

## 1. What was made

On the small rank-two control curve

\[
E=[1,1,1,3,12],\qquad P_1=(0,3),\quad P_2=(7,17),
\]

we constructed explicit rational Galois-equivariant group isomorphisms

\[
f_{113}:E[5]\longrightarrow E_{113}[5],\qquad
f_{167}:E[5]\longrightarrow E_{167}[5],
\]

where

\[
E_{113}=[1,1,1,-1669982047,-25795561267816],\qquad
E_{167}=[1,1,1,1878418,-485198548].
\]

The same maps are used at the bad raised prime and the good second prime. Thus the two local measurements are no longer related by an independently fitted unit.

The observed local identities led to actual global fifth-division-torsor maps. The resulting equalities, with the action compatibility and review in `torsors/RESULT.md` and `geometry/GLOBAL_TORSOR_REVIEW.md`, are

\[
\boxed{\kappa_{E_{113}}(Y_{113})=(f_{113})_*\kappa_E(-P_1)},
\qquad
\boxed{\kappa_{E_{167}}(Y_{167})=(f_{167})_*\kappa_E(2P_1+P_2)}
\]

in the respective global H¹ groups over Q. Here

\[
Y_{113}=(39736379971/293764,7496759272384463/159220088),
\qquad Y_{167}=(480,22723),
\]

and \(2P_1+P_2=(7/4,-53/8)\). These are point-class comparisons at modulus five, not rational isogenies and not formulas that apply the torsion coordinate maps directly to arbitrary rational points.

## 2. How the discovery became a proof candidate

The process had four distinct stages.

1. **Admit the actual models.** Exact full Sturm comparisons checked 80,256 and 118,272 coefficients of the correctly stabilized forms. Both congruences hold modulo five. An explicit inertia/Frobenius argument gives full residual GL₂(F₅). The CM field Q(sqrt(-19)) has the required splitting, and the base twist has rank zero by exact descent bounds. These statements do not use an analytic Sha order.
2. **Construct the common representation map.** Rational polynomial maps on the fifth-division schemes were found and verified exactly. Group addition was checked in a universal 240-dimensional rational algebra, including both coordinates; dependent pairs were checked by doubling and oddness. The selected maps have Weil-pairing multipliers one and three respectively, which are kept in the transport.
3. **Measure actual Kummer classes.** At each admitted finite prime we calculated fifth-division points and the cocycle Frob(Q)-Q. We did not replace it by the unrelated projection [#E(F_q)/5]P. Restriction to the inert quadratic completion and the toric pairing were then applied using the single global map.
4. **Prove the suggested global comparison.** Each fifth-division fiber is an explicit irreducible degree-25 rational algebra. A rational map between these fibers was constructed and checked against the equations [5]Q=P and [5]R=Y. The written group argument makes the induced Galois-equivariant bijection affine; a separate exact finite-field translation calculation identifies its linear part with the already fixed torsion map. This step is what upgrades the point-class identity beyond the finite list of observations.

See the torsor proof and its separate review for the hypotheses in the last step. A field isomorphism alone would not suffice without the affine-action argument. The finite-field calculation determines a scalar only after that argument; it is not an extrapolation that the translation identity holds globally.

## 3. The measurements and their explanation

In the explicitly recorded tangent orientations, the toric pairing row on the base point basis is

\[
a_{113}=(0,4),\qquad a_{167}=(1,3).
\]

At a second place write \(b=(b_1,b_2)\) for the two finite Kummer coordinates and \(b_Y\) for the transported raised point. The detector is

\[
r=a_1b_2-a_2b_1.
\]

The first six measured rows contained five nonzero detectors and one zero-detector control. They suggested the coefficient vectors (4,0) and (2,1). Those predictions were sealed before testing eight further detecting places between 500 and 2000; all eight passed. All fourteen rows, including the zero-detector case, agree with the predicted point-class identities.

| Raised prime | Global point-class coefficients | Nonzero detector rows | Recorded scalar b_Y/r |
|---:|---:|---:|---:|
| 113 | (4,0) | 6 | 4 |
| 167 | (2,1) | 7 | 1 |

The global equalities explain the constancy wherever the same compatible local maps are defined: (4,0)=4(-4,0), and (2,1)=(-3,1) modulo five. Collecting more matching second primes would now add no evidence about a missing global point-class comparison—it is the torsor construction that supplies it.

The signs at different raised primes are not a canonical CM cross-level normalization. Reversing one tangent orientation reverses its toric sign. The actual geometric component factor must account for this.

## 4. A defect was found and repaired

Both raised curves have split multiplicative I₅ reduction at their raised prime. Both displayed rational points reduce to smooth points. Their singular Kummer images there are therefore zero. Taking either of those points as a nonzero toric generator would have invalidated the proposed experiment.

We instead constructed the independent local component generator from the nodal multiplicative group. Its fifth roots of unity were pulled into the base representation using the forward global map. The inverse rational map has denominators divisible by the raised prime and cannot simply be reduced there. Using the forward map avoids that invalid reduction and identifies four smooth toric images among the 24 nonzero base torsion points.

This is a repair of the experiment's map, not a redefinition that absorbs an unknown arithmetic scalar.

## 5. What remains before this evaluates the actual CM source

Let \(\pi:J\to E_1\) be the specified Shimura quotient, \(D_K\) the degree-corrected CM divisor, and \(\phi_J\) its geometrically normalized component source. Their images must be computed separately:

\[
\pi_*D_K=nY,\qquad \pi_5(\phi_J)=k\phi_{E_1}.
\]

When these statements hold in the required residual quotient and k is a unit, the actual CM tensor is

\[
\boxed{\text{CM tensor}=(n/k)\,(\text{point tensor measured here}).}
\]

The point tensor is now constructed and its global point-class relation has an explicit proof. **Neither n nor k has been computed.** They must not be removed by replacing the CM image with a primitive point or choosing a new local unit. The quotient's existence does not itself give its integral component map.

For 167, irreducibility of the degree-25 target division fiber also excludes five-divisibility of Y over the quadratic field K. Full residual image excludes K-rational five-torsion. Together with rank(E167/K)=1, this proves that Y spans E167(K)/5. Therefore every actual K-rational CM point image has class n times the constructed point class, without assuming Sha(E167/K)[5]=0. This fixes its source direction, while n can still be zero.

The 167 partner is the cleaner next source calculation: its minus-19 twist has exact rank bounds [0,0], so its K-rank is one, and a measured nonzero mod-five Kummer image proves that Y167 is not five-divisible. In the appropriate five-adic point lattice, n is then a genuine index of the actual CM image. The 113 partner's twist bounds are only [0,2]; no rank-one assertion over K is made for it.

The next substantive task is therefore to construct the actual Shimura quotient/CM image at the 167 model and compute its component map in the same normalization. It is not another trace scan or another collection of second-prime ratios. A successful source-index calculation would complete this control-model CM comparison; applying it to the seed would still require a justified construction and arithmetic control across coefficient primes.

## 6. Relation to the BSD seed

This experiment has made an actual global residual point-class comparison from exact measurements. It demonstrates an executable way to turn a proposed comparison into a finite algebraic proof on a manageable model. It does not construct the seed's Kato derivative, evaluate the seed's CM source, or bound its excess content.

The retained seed endpoint on this route remains: the specified derivative is nonzero and its content satisfies m_p-w_p<=1 outside a fixed finite set, or an independently justified tame identity supplies the required cofinite vanishing. The present model calculation proves neither condition. FIN, ORDER9 and Q36 are unchanged.

Both particular raised partners already fail to match the base modulo 25: at the good prime 13 their traces differ by -5. This exact precision limit does not refute a global comparison mechanism; it prevents pretending that the current mod-five maps provide higher precision.

## 7. Evidence and scope

- Full coefficient vectors, exact admission controls and provenance: `admission/`.
- Explicit rational torsion maps, inverse denominators, universal addition identities and Weil-pairing checks: `torsion/`.
- Actual mixed-place arithmetic, predictions sealed before held-out tests and complete values: `checks/`.
- Explicit global division-torsor maps, action checks and proof: `torsors/`.
- Source-index diagram, local normalization audit and separate global proof review: `geometry/`.
- Replay instructions and scope: `REPRODUCE.md`.

No paid/remote job or production seed evaluation was launched. This return is published to the lab under the user's standing instruction; publication certifies custody, not the mathematics. Full third-party papers and unrelated research data are not copied into the package.
