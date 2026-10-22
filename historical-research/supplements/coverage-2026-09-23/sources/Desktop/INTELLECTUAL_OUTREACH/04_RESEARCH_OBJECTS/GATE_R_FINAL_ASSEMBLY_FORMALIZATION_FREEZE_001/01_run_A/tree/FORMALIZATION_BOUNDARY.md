# Formalization boundary

    FORMALIZATION_LEVEL      = EXPLICIT_2_ISOGENY_DESCENT_REALIZATION
    ACTUAL_H1_SELMER_OBJECT  = NO
    touches_L_function       = NO
    PRIOR_ART_BLOCKER        = UNRESOLVED

What the certified base already contains: an explicit 2-isogeny descent on the
curves

    E_q  : y² = x(x² + Aq·x + r²q²)
    E'_q : Y² = X³ − 2Aq·X² + Dq²·X

with the isogenies `φ`, `φ̂` as actual maps on mathlib's `Affine.Point`, their
kernels, images, composites, cokernels, the explicit square-class groups, and

    E_q(ℚ)/2E_q(ℚ) ≅ C₂            (P04c)
    ∃C ≥ 1, ∀P, height P ^ 4 ≤ C * height (P + P)     (R1, for this family)
    an abstract proper-height / bounded-halving torsion theorem (R0)

What it does **not** contain, and what this job does not create: any actual
H¹ or Selmer object, any Ш, any L-function or analytic rank, and no claim about
curves outside the `H41` family with `Params`.

`E_q(ℚ)/2E_q(ℚ) ≅ C₂` alone does **not** give rank zero — an abstract group can
have that quotient and still contain elements of infinite order.  Closing that
gap on the actual point group is precisely what the five targets are for.

Success establishes exactly the five displayed statements for the `H41` family.
It is not a classification of the rational points, not a statement about any
larger family, and not a BSD result.
