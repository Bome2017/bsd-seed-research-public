# Sources and reading scope

## Primary sources

Robert L. Miller and Michael Stoll, *Explicit isogeny descent on elliptic curves*, 23 January 2011.

https://www.mathe2.uni-bayreuth.de/stoll/papers/isogeny-descent.pdf

Read Section 2 for the isogeny-Kummer sequence and descent-function convention; Section 3 for the local image; Theorem 11 on printed p.12 for the exact local-membership assertion and its exceptional cases. That theorem page was visually inspected with the web PDF screenshot tool. The curve-specific local and isogeny inputs are retained from the supplied proof and earlier arithmetic; their complete computation was not rebuilt here. This source does not contain this particular local detector calculation.

Tom Fisher, *Explicit 5-descent on elliptic curves*, The Open Book Series 1 (2013), 395--411.

https://msp.org/obs/2013/1-1/obs-v1-n1-p20-s.pdf

Read Theorem 5.3 and the preceding equations for C_lambda and D_lambda on printed p.402; visually inspected the full matrix page. The supplied matrix is reproduced with the same signs. The degree-five isogeny covering is not a degree-25 multiplication-by-five map. No explicit projective-coordinate isomorphism to the separate affine equation was computed.

The local decomposition Q_11^*=11^Z times Z_11^*, fifth-power Hensel lifting, finite-field cyclic-group arithmetic, Chebyshev identities, and restriction/corestriction used here are proved or explained directly in PROOF.md. No research theorem concerning the seed's uncomputed Sha is inferred from them.

## Retained repository inputs

All inputs are in Bome2017/bsd-seed-lab at commit
257af6888c80fda3b90d481cf2d94f9950701811, under
work/returns/BSD_EXPLICIT_OBSTRUCTION_CLASS_2026-10-13/.

- REPORT.md: actual representatives and result scope.
- theory/DESCENT_FUNCTION_AND_NONTRIVIALITY.md: isogeny direction, normalized f, rational point pair, local membership, and original class-group proof.
- AUDIT.md: prior same-team check and generator-inversion qualification.
- implementation/FISHER_MODEL.json: complete five-quadric model.
- implementation/CONSTRUCTION.md: geometric source matching and existing local witnesses.

The new checker transcribes the arithmetic data from these files. It is separately written, not a replay of their original code. Source blob identities and scopes appear in SOURCE_BINDINGS.json. The entire user archive was not downloaded or verified, and no claim of archive-byte identity is made.

The rank upper bound and 5-saturation, as well as the curve-specific inputs to the local descent theorem, remain retained. Class-group data are not needed for the new lower bound; they remain an input only for the optional statement that the surjective detector is an isomorphism. The original smoothness computation was read, not rerun; Fisher's theorem is the geometric source.

## Research status

The newly derived result is the explicit local-signature matrix and its consequence for the two actual classes, together with the displayed quintic splitting field. No novelty search or independent review was undertaken. No main conjecture, analytic Sha prediction, numerator, regulator, or p-adic BSD formula enters this proof. No seed prime or BSD endpoint is newly settled.
