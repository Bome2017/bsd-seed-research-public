# Actual coefficient-seven local map on the changed rank-two controls

This note rebinds the retained formal-branch necessary condition to the two new curves. It does not claim that any sample of units is complete.

| Model | #E(F7) | a7 | Actual branches (e,f,v(x(T)),v(y(T))) |
|---|---:|---:|---|
| 655a1: [0,0,1,-13,18] | 11 | -3 | (6,1,-2,-3), (7,3,0,0), (7,3,0,0) |
| -47 twist of 11a1: [0,-1,1,-22826,2411880] | 10 | -2 | (6,1,-2,-3), (7,6,0,0) |

These are direct calculations on the supplied number fields and universal points. The preflight checks the actual equation and [7]T=0. The twist preflight additionally checks the scalar automorphism on the actual field coefficients exactly; the split evaluator checks it at all 48 embeddings of every tested split prime for either curve. The saved NF polynomial is required to match the source polynomial.

Both curves have ordinary nonanomalous reduction. On the retained ordinary local representation convention, the Kummer image is the image of H^1(Q7,V+). Evaluation against a nonzero formal-torsion point T through the Weil pairing kills V+, since that one-dimensional line is isotropic. Therefore a scalar representative of a genuine local Kummer class must be a seventh power in Q7(T) on the degree-six formal branch. Only this necessary implication is used for the upper-bound screen. The full source need not itself be identified with local cohomology.

For actual ordinary units, the test is computed in the unit group modulo the eighth and ninth powers of the branch prime ideal. This is sufficient precision: with ramification degree 6, every element of 1+P^8 has a seventh root by the p-adic logarithm and exponential on 1+P^2, where the convergence inequality 2>6/(7-1) holds. Hence reducing modulo P^8 does not lose an obstruction to being a seventh power. The ninth-power calculation is a further arithmetic control, not an additional independent constraint.

Compact factors need not individually be units. Each factor is normalized using the same uniformizer, its exact valuation is retained, and the integer relation matrix must cancel these valuations before its normalized unit logarithm is accepted. A different arbitrary uniformizer for each factor would not justify the calculation. The code separately tests a nonpower and its seventh power in the computed local quotient.

The split-prime map permits the full two-dimensional space of linear functions on E[7]. Its defect map is the complete affine-incidence norm screen at that split prime. It is not counted again as a new additive constraint. The coefficient-seven seventh-power row is a genuinely different local necessary condition.

The ordinary faithful-character unit space has dimension 4 under the retained full-image/signature theorem. Therefore two independent images of authenticated ordinary units under the stacked maps would give an upper bound of 2 on its kernel, even without a complete unit basis. This would still leave the ordinary class-supported contribution and the primitive divisor layer. Neither is discarded by this local calculation.
