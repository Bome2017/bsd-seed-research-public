# Actual seed excess: one unit direction and one ideal-class direction

October 13, 2026. **EXECUTED_STRUCTURAL_EXPERIMENT; EXPLICIT_SEED_UNIT_SOURCE.**
The complete one/one classification is conditional on the saved class-group
computation. The explicit positive unit certificate does not require that
class-group completeness assumption. No new primary vanishing, FIN, ORDER9,
or Q36 conclusion is claimed.

## The experiment and its answer

We tested a specific explanation of the seed's already known excess at 3:
can ideal classes distinguish both non-point directions from the point plane?
The inputs were the two actual certified ternary cubics and the two rational
points. No Sha order, modular-symbol coefficient, regulator, or analytic
prediction was used to compute their images.

The answer is **only one direction is visible that way**. The other can be
represented by an explicit global unit. This is more information than the
old dimension-four descent calculation: it identifies arithmetic components
of the actual surviving classes.

All four principal ideals were factored completely. Their union has 26
prime ideals, including good-prime cube factors. Every exponent is divisible
by three. Thus the proposed ramification-support intervention removes none
of these four classes.

In the cached class group Z/12 x Z/6 x Z/2, their cube-root ideals have columns

| Coordinate | P1 | P2 | cubic 1 | cubic 2 |
|---|---:|---:|---:|---:|
| Z/12 | 0 | 8 | 8 | 8 |
| Z/6 | 0 | 0 | 4 | 4 |
| Z/2 | 0 | 0 | 0 | 0 |

Converting the 3-torsion coordinates correctly gives

    C = [0 2 2 2]
        [0 0 2 2].

The point image has rank one and the full image rank two. The exact quotient
calculation in [FILTRATION.md](FILTRATION.md), independently checked in
[the matrix review](reviewer/SEED_MATRIX_REVIEW.md), therefore gives

    (valuation contribution, unit contribution, ideal-class contribution)
        = (0, 1, 1).

This is a filtration, not a canonical direct-sum splitting. Nontriviality and
completeness of these class coordinates retain the GRH qualification of the
historical bnf calculation. The known cubic independence does not use GRH.

## A positive arithmetic object, independently replayable

Let beta1,beta2 be the actual reconstructed cubic images in K*/K*^3, where

    K = Q(w),
    w^8 - 1188376638 w^4 - 7030398068360 w^2 - 117686586145348587 = 0.

We constructed a compact field element g with

    (g) = I_beta1 / I_beta2,       (beta_i) = I_beta_i^3.

Consequently

    epsilon = beta1 / (beta2 g^3)

is an actual global unit representing the cubic-difference direction.
Its 1,845-factor representation is in
[unit_certificate.gp](seed3/unit_certificate.gp). Keeping a product of exact
field elements and integer powers avoids expanding enormous unit coordinates.

The separate [portable checker](checks/verify_unit_portable.gp) rebuilds the
number field and its integral basis, reconstructs the point and cubic images,
and completely factors every term of this unit expression. The accumulated
valuation is zero at all 1,872 prime ideals appearing in that independent
calculation. It uses no bnf, class-group computation, fundamental-unit basis,
L-value, or expected Sha value. Omitting the cube correction or changing the
first exponent fails the same ideal-valuation test.

The original four-class independence certificate was replayed separately.
Because the removed factor is a literal cube, the unit class is beta1-beta2.
It is nonzero modulo both point directions. This is an exact positive unit
certificate under the retained interpretation of the explicit coverings and
rank-two point plane, not a consequence of a GRH class-group rank.

Moreover tau(w)=-w sends the chosen torsion point T to -T. The exported unit

    epsilon_minus = epsilon / tau(epsilon)

has norm one to Q(w^2). Weil-pairing equivariance makes its class twice the
class of epsilon modulo cubes, so it still supplies a non-point direction.
The checker verifies the exact paired-factor identity and tau(T)=-T. The
Cardano inversion convention is retained; the assertion is about the precise
reconstructed classes, not an unrecorded choice of signs on the two cubics.

An additional exact orbit check finds that T's y-coordinate has degree eight
over Q. Therefore the orbit of T is all eight nonzero 3-torsion points; E[3]
is irreducible and there is no rational 3-isogeny. This unit contribution on
the actual seed cannot be explained solely by the rational isogeny present
in the earlier positive control. This is an irreducibility check, not a claim
of good reduction at 3 or a new integral full-image theorem. See
[the orbit check](checks/irreducible_source.out) and the separate
[norm-one/source review](reviewer/NORM_ONE_REVIEW.md).

## What this changes for discovery

There is now a concrete seed unit carrying genuine excess on which to test
proposed global source restrictions. A proposed exclusion based only on
ramification misses both directions; one based on this torsion field's
class-group quotient misses the explicit unit direction. Keeping the unit
term is a necessary repair, and the exact filtration records how to do it.

This does not contradict the earlier exact class-group receiver: that receiver
uses a different, larger division-point field. It also does not establish a
uniform bound for the unit and class terms in the varying p-torsion fields.
Coefficient 3 is bad for the seed. Its local conditions cannot be substituted
into the good-prime Kato theorem.

The next relevant arithmetic question is now testable on an explicit source:
which full descent relations and local conditions admit this norm-one unit,
and what additional restriction could exclude analogous non-point units on
the unresolved good-prime domain? Answering that requires new arithmetic;
neither norm one nor zero ideal class alone is enough. This return provides
the specimen and exact maps, not a demonstrated theorem finishing that task.

## Evidence, cost and status

Predictions were sealed before calculation. The older mixed tame-prime test
was rejected as a historical duplicate; see [selection](SELECTION.md).
The accepted producer took 32.8 seconds. Three erroneous implementation trials
are preserved and rejected; their completion markers were not accepted in
the presence of GP errors. No BNF regeneration or new Selmer solve was run.

The independent matrix checker recomputes ranks from the actual entries,
and the portable arithmetic checker supplies a separate positive-unit check.
The abstract quotient controls are labeled separately from seed arithmetic.
This is same-team computation and written reasoning, not human review,
formal verification, or a literature-novelty claim.

**The experiment produced new structural data and an explicit seed source.
It did not produce an upper bound for the unresolved excess. FIN, ORDER9,
Q36 and coefficient-prime coverage are unchanged.**
