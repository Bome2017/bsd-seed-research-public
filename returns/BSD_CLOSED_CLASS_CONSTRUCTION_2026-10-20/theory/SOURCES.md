# Sources and retained input boundary

## Primary sources freshly opened for this deduction

1. Stéphane Louboutin, *Explicit Upper Bounds for Residues of Dedekind
   Zeta Functions and Values of L-Functions at s=1, and Explicit Lower
   Bounds for Relative Class Numbers of CM-Fields*, Canadian Journal of
   Mathematics 53(6) (2001), 1194–1222,
   [DOI 10.4153/CJM-2001-045-5](https://doi.org/10.4153/CJM-2001-045-5),
   [publisher full PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/S0008414X00028418).
   Read Theorem 4(1), equation (10), printed page 1197 / PDF page index 3.
   It bounds a primitive ray-class L-value over an arbitrary number field
   using the norm of the finite conductor. Infinity ramification is
   permitted. Theorem 5 has an additional infinity condition and is not
   used. The CM consequence (11) is not used either.

2. Bruce W. Jordan and Bjorn Poonen, *The analytic class number formula
   for 1-dimensional affine schemes*, author manuscript dated April 2,
   2020, [full PDF](https://math.mit.edu/~poonen/papers/analytic.pdf).
   Read equation (1), printed page 1, for the classical residue formula
   and its normalization of regulator, roots of unity, and discriminant.
   Only that standard number-field formula is used, not the manuscript's
   generalization to other schemes.

3. J. S. Milne, *Algebraic Number Theory*, version 3.08, July 19, 2020,
   [full notes](https://www.jmilne.org/math/CourseNotes/ANT.pdf).
   Read Theorem 4.19, printed page 76 / PDF page index 77, for Minkowski's
   convex-body theorem, and “Regulators”, printed page 94 / PDF page
   index 95, for the factor-two complex-coordinate convention. The
   all-embedding conversion in the proof is derived by Cauchy--Binet.

Standard algebraic inputs are Dirichlet's unit theorem, the relative
order/field discriminant divisibility, quadratic class field theory and
its conductor-discriminant formula, and Chebotarev applied to the Hilbert
class field compositum. Their uses are explicit in the proof; they are
not claimed as new theorems or as formalized results.

## Actual seed field inputs

FIELD_INPUTS.json is a byte copy of

    /Users/bsm/BSD_GENUINE_RELATIVE_CLASS_METHOD_2026-10-20/review/DISCRIMINANT_GENERATION_BOUND.json

Its retained upstream field presentation is

    /Users/bsm/BSD_RELATIVE_UNIT_CLASS_ALTERNATIVE_2026-10-20/relative_source/fields.gp

with signatures and maximal-order discriminants recorded in the same
relative_source directory and subsequently independently checked in the
genuine-relative-class review. INPUT_BINDINGS.json records current file
hashes. No bnfinit, bnfcertify, L-function evaluation, or maximal-order
recomputation is performed in this new theory lane. The exact checker
rechecks the discriminant tower identity and the finite relative
discriminant factorization, while retaining their identification with
these actual fields.

## Earlier stops checked before this calculation

The preceding relative-unit/class alternative correctly rejected
transferring a smaller field's class number to the faithful scalar
component. The previous genuine-relative-class run exhausted its 196
specific pseudo-relations without a closed faithful relation or a
nontorsion unit. Neither is reused as a class completeness assertion.

The earlier observation that a relative class-number formula needs a
relative regulator remains correct. This deduction supplies an explicit
lower bound for that full regulator and accepts the resulting coarse
class upper bound; it does not pretend the regulator was computed.

The CM-minus shortcut was checked and excluded for this signature:
A has real embeddings and the relative unit rank is six. The ratio at
s=0 has a zero of that order, rather than a nonzero algebraic special
value giving the relative class number without a regulator.

## Verification grade

The source application and lattice/class-group deductions are written
mathematics. The numerical inequalities are executable exact rational
arithmetic. The field inputs are retained exact arithmetic. No proof
assistant checked the argument. A sibling desk review of the metric and
unit-index argument was requested separately and is not converted into
an assertion of independent certification of all retained field inputs.
