# Complete affine-norm controls: points and genuine excess survive the same admission test

Date: 2026-10-15. Grade: exact new finite arithmetic under retained complete descent sources. No new BNF computation, analytic Sha input, field search, or endpoint claim.

The entire scalar-compatible source was tested, before comparing its answer with known points or excess classes. Both norm kernels are now certified by complementary positive and negative evidence:

| Curve | Full source | Scalar source | Norm-image rank | Exact norm kernel | Interpretation after arithmetic |
|---|---:|---:|---:|---:|---|
| 1913b1 | 9 | 3 | 1 | 2 | Two genuine excess-unit directions; no rational-point directions |
| 389a1 | 10 | 4 | 2 | 2 | Exactly the two rational-point directions |

The retained complete sources and all-place membership/rank results are not reconstructed here. The new result is the complete global norm map on their scalar sources, including directions absent from the previously displayed true-class lists.

## Actual arithmetic and complete kernel certificates

Use the short model y²=x³+ax+b, with a=−c₄/48 and b=−c₆/864. The affine-line field is

    B=Q[z]/(z⁸−54c₄z⁴+216c₆z²−243c₄²),   m=z/6.

The three points on the corresponding affine line have x coordinates in

    G(X)=X³−m²X²+(m⁴+2a)X−(m⁶+2am²−4b).

The y coordinate is mX−(m⁴+a)/(2m). The producer constructs the map from the retained torsion-point field into B[X]/G, verifies its defining polynomial and both elliptic coordinates, and takes the actual degree-three norm of every scalar-basis representative. This is the geometric affine-line norm, not a collection of residue equations substituted for it.

For 1913b1, in the retained full-source basis e₁,…,e₉, the complete scalar basis is

    s₁=2e₃+e₄,   s₂=2e₆+e₇,   s₃=e₈.

At the simple B-place z≡11 mod67, with primitive residue generator 2, the norms have cubic-character row (1,0,0). Thus any norm-cube class must have first scalar coordinate zero. The norms of s₂ and s₃ have literal cube roots in B. Consequently the **entire** norm kernel is ⟨s₂,s₃⟩. Afterward, comparison with the retained admission data identifies both as genuine Selmer classes; the retained rank-zero input leaves no point plane.

For 389a1 the scalar basis is

    s₁=2e₄+e₅,   s₂=e₇,
    s₃=2e₁+e₂+2e₈+e₉,   s₄=2e₈+e₁₀.

The simple places (q,z)=(19,9),(73,18), with respective primitive generators 2,5, give rows

    (2,0,2,0),   (2,0,0,0).

These have rank two, and their common kernel is ⟨s₂,s₄⟩. Both corresponding norms have literal cube roots. The retained point images are 2s₂+s₄ and s₂+s₄, whose coordinate determinant is one. Thus the complete global norm kernel is exactly the point plane in this case.

The norm operation is multiplicative modulo cubes. Exact roots on a kernel basis therefore prove cubehood of every combination in its span, including exponent reductions modulo three. Conversely a nonzero cubic-character value at a genuine residue place excludes a global cube. The certified residue rank and root-certified subspace have complementary dimensions; this proves completeness without assuming that a finite list of zero residues implies cubehood.

## A simpler proposed rule was tested and rejected

Both computed kernels are valuation-zero and lie in the global-unit span. After recording that observation, VALUATION_CANDIDATE.json sealed the question whether the norm kernel equals the valuation-zero scalar subspace. Fresh exact matrix calculations show equality on both controls: their valuation-zero scalar dimensions are two.

The simultaneously constructed 433a1 control disproves extending this rule even across the three curves. Its exact norm kernel contains the extra source vector

    (1,2,0,2,1,2,0,0,1,0,0,0,1)

with nonzero valuation vector (1,2,0,2,1,2,0,0,1). Its affine norm has a literal cube root, although both the 3-local and 433-local Kummer conditions reject it. The bound sibling certificate is copied under countercontrol433/. This review relies on that sibling's exact norm verification for the countercontrol; it does not claim a second independent reconstruction of its field norm.

Therefore a uniform “discard nonunit directions before global admission” rule would be incorrect. The controls separate three operations: global cohomological admission, local Selmer admission, and quotienting by rational points. None can be substituted for another merely because two curves give the same dimension.

## Verification and remaining scope

The independent checker recomputes all seven norms as determinants of multiplication matrices, rather than using the producer's norm function. It verifies all four literal cube roots, all three simple residue places, the primitive residue generators, the source bindings, and the complete residue-kernel dimensions. A Python checker independently enumerates the 27 and 81 scalar vectors and checks the resulting nine-element kernels. A fresh temporary-directory replay reproduces all eight arithmetic artifact files byte-for-byte; every GP process is checked for errors as well as its exit code. GP can exit zero after a parser error, so an exit code alone is not accepted.

A preliminary parser failure and a corrected denominator-screen implementation are documented in IMPLEMENTATION_NOTES.md. Neither was accepted as a mathematical outcome.

The norm test rejects false global source directions but deliberately retains genuine excess. Its complete computation here does not explain why the seed's unresolved primary components should vanish. The positive 1913 control prevents promoting “unit” or “norm-cube” to that conclusion. The full-source map and its exact kernels are available for the parent's common-point repair experiment; no cross-prime bound or new FIN, ORDER9 or Q36 result is claimed.
