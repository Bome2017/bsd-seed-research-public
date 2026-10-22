# Relative ideal reduction, with the missing-class term visible

Date: 2026-10-20. Algorithm design and elementary ideal identities.

The primary relative algorithm inspected is Cohen, Advanced Topics in
Computational Number Theory, §§7.3.2–7.3.3, Algorithms 7.3.7–7.3.8. It reduces
pseudo-ideal representatives modulo principal and base-extended ideals.
The full algorithm also uses base class/unit data and GRH stopping tests.
The restricted procedure below instead records only exact anti-invariant
relations needed for PRESENTATION_BOUND.md; it does not claim to implement
or certify the entire published class-group algorithm.

Let A/K be the actual quadratic scalar extension, tau its involution.
Maintain an exact invariant

    I = (alpha) j(a) J.                          (1)

For any fractional ideal J define its base content by

    v_Q(content(J)) = min_{P|Q} floor(v_P(J)/e(P/Q)).

This is the greatest base fractional ideal whose extension divides J in
the valuation sense. Dividing J by this extension makes all valuations
nonnegative, and at least one valuation above every Q smaller than its
ramification index. It gives an integral primitive relative ideal.

In the quadratic case its extension can be computed from J+tau(J): at
split primes take the common smaller valuation; at inert primes keep the
valuation; at ramified primes round the common valuation down to an even
integer. The last step is essential, including for negative valuations.
Actual relative ramification and contraction must be authenticated first.

To reduce a primitive J, choose beta in A^* by a lattice reduction or a
relative pseudobasis rule. Replace J by J/(beta), strip its base content,
and update alpha and a to preserve (1). Retain the replacement only if
the positive integer norm of its primitive integral representative
strictly decreases. This terminates. It can terminate without finding a
small enough or repeated ideal; success is not automatic.

When two runs end at the same primitive ideal, their invariants give an
exact pseudo-principal relation. A terminal ideal equal to O_A does so
directly. Apply 1-tau to cancel the base ideals, as in equation (2) of
PRESENTATION_BOUND.md. Closed principal cycles can additionally produce
actual units alpha/tau(alpha); their norm/local evaluation ranks must be
checked modulo p-th powers before entering r_U.

This is a genuine relative operation: it strips maximal extended-ideal
content and works modulo base ideal classes. Using LLL only to select beta
does not convert it into an absolute class-group calculation. Conversely,
using only absolute ideal reduction without content stripping or the
invariant (1) does not demonstrate relative class computation.

Every unclosed terminal ideal remains a column or a named defect. The
generation gate from PRESENTATION_BOUND.md is independent of the success
of reduction on selected ideals. Neither a large collection of cycles nor
small terminal norms proves the absence of ungenerated class directions.

## Discriminants and the generation scale

The retained actual fields satisfy

    |Disc(A)|=|Disc(K)|^2 Norm_{K/Q}(d_{A/K}),
    Norm(d_{A/K})=2^4 * 5 * 4547^6.

The first identity has been checked by exact integer arithmetic in the
review lane. A small relative discriminant does not allow deletion of the
base factor from the absolute Minkowski argument: its square-root term is
|Disc(K)| sqrt(Norm(d_{A/K})).

The inspected Cohen implementation does not supply a prime-generation
bound depending only on Norm(d_{A/K}); its fast generation bound uses the
absolute discriminant under GRH. This is a statement about that source,
not a proof that no sharper relative theorem exists. In particular, the
content-stripping identity proves nothing about a uniform bound on all
relative ideal classes.

An available unconditional alternative is the explicit prime-ideal-sum
criterion of Belabas–Diaz y Diaz–Friedman, Corollary 5.2. It also uses the
absolute discriminant. Its evaluation at the actual retained inventory
cutoff is recorded separately; it is not replaced by the GRH criterion in
the same paper.

## Implementation acceptance

Accept a row only after exact ideal equality, scalar action, prime support,
and any fifth-power/base-ideal terms verify. Compute r_C modulo five from
those rows. Accept a unit-rank lower bound only from authenticated units
and evaluations. Accept q=0 only from an independent generation-modulo-five
certificate. A process exit code or a printed success marker after a GP
error is not such a certificate.
