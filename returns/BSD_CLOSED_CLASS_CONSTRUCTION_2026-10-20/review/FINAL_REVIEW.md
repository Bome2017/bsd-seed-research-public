# Independent review: complete coarse bound and closed geometric source

Date: 2026-10-20.

**Supported outcome:** the actual seed coefficient-five point field has a
complete, unconditional upper bound of **97** on the length of its relative
five-primary ideal class group, under the retained exact field inputs. This
includes classes absent from every collected relation list. The tested geometric
function family supplies **zero** new closed class-relation rank and **zero**
nontrivial relative units. Neither result is a sufficiently small seed bound.

## What was independently checked

### Analytic complete bound

I read `theory/COMPLETE_CLASS_BOUND.md` in full and checked the quadratic-order
inequality, the 20-coordinate logarithm estimate, Minkowski constant, standard
regulator conversion, unit-index sign restriction, whole ordinary class-norm
surjectivity, and the analytic class-number formula. Details and the exact primary
source citation are in `ANALYTIC_REVIEW.md`. The displayed primary Louboutin
Theorem 4(1), formula (10), was checked directly; its hypotheses permit this
non-CM extension and the ramified infinite places.

A separate implementation, `check_analytic_coarse.py`, uses different coarse
rational constants and exact integer/Fraction arithmetic. It proves

    h_A/h_K < 2.8 * 10^68 < 5^98,

so it independently confirms the integer threshold 97. The theory script gives
the tighter bound 2.62 * 10^68; I inspected its enclosure directions, but my
independent script does not claim to reproduce that tighter numerical ceiling.
The exact integer threshold is the same. `ANALYTIC_COARSE_REVIEW.json` records it.

I also checked the algebra of `theory/SCALING.md`: its signatures, relative rank
(p^2-1)/4, regulator factor, and general conditional expression specialize to
the actual-five formula. No discriminants or positivity gates at new primes
were computed. This is not an across-prime smallness result.

### Actual geometric elements and norms

`replay_line_norms.gp` authenticates the retained division-point source, order
five, scalar action, all 31 distinct line functions, their point/tangent/chord
incidences, and the exact number-field norm/resultant identity. A separate Python
integer calculation exhaustively trial-divides their rational norms by every
prime through 419775. All 31 have nontrivial outside cofactors, of 42--237 digits.
This alone did not reject combinations of the functions; those were tested next.

### Full fixed-family support closure

`replay_geometric.gp` independently checks all 124 actual principal fractional
ideals, including the rational denominator ideals, against their saved exponent
rows on 134 pairwise-coprime ideal atoms. It checks every atom's scalar image,
every actual element's scalar orbit, and both character projections. Its explicit
pass marker records completion in 61.874 seconds. A nominal 55-second GP alarm
was present but did not interrupt it; no timeout result was accepted as a pass.

`check_geometric_closure.py` uses independent finite-field elimination. In each
of the two faithful characters it finds 28 columns, with six inside and 22
outside the bound. Full and outside ranks are both 20. It additionally constructs
and verifies the exact matrix identity over F5

    R_inside = R_outside * T,

saved in `GEOMETRIC_FACTOR_CERTIFICATES.json`. Thus all combinations that cancel
the outside support also cancel the inside rows: closed relation rank is zero.
The displayed selected quotient dimension 28-20 is not a bound on all classes.

The outside classification is independently justified by exhaustive rational
prime division of all 28 representative atom norms, together with the actual
ideal factorizations checked in GP. Every small rational factor in these norms
has exponent one, which forces residue degree one for its supporting prime
ideal; hence none is secretly above the cutoff by residue degree. Removing all
such factors gives exactly the saved outside ideal norm. Every nontrivial outside
norm is not a fifth power. Combined with pairwise-coprime scalar-closed support,
this proves the 22 outside projected columns are genuine nonzero independent
divisor directions modulo five. No composite ideal norm was confused with a
prime-ideal norm.

### Complete multiplicative unit kernel of this family

The anti-divisor matrix is authenticated directly from the exact divisor rows.
Independent modular ranks give rank 40 for it and rank 84 for the saved kernel
matrix; the product is zero over the integers. Together these prove rational
rank 40 and a full 84-dimensional rational kernel. GP independently evaluates
every one of the 84 corresponding products of alpha/tau(alpha); all are exactly
+1. Saturating the integer kernel cannot conceal a non-torsion unit: a power of
any such product is one. Because A has a real embedding, its only roots of unity
are +/-1, both trivial modulo fifth powers. This statement is restricted to the
fixed 31-function family and its scalar closure.

### Smaller-field norm certificates

The exact GL2(F5) subgroup check and the carefully separated rational and
5-integral module obstructions are in `NORM_RELATION_SCREEN.md`. They exclude a
universal transfer certificate built only from smaller-degree subfields for
this component. They do not exclude arbitrary arithmetic class bounds; indeed
the complete analytic bound above uses a different mechanism.

## Retained inputs and limits

The existing maximal orders, discriminants, field signatures, torsion-point
field construction, and source-to-elliptic interfaces retain their previous
proof/computation grades. I did not rerun a maximal-order construction, a full
class-group computation, an elliptic Selmer calculation, or a Kato computation.
The new proof is not kernel-formalized and no novelty certification is claimed.

The optional complete-source ceiling 3+97=100 is conditional on the retained
source and valuation interfaces, in addition to the reviewed field theorem.
It is much too large for the target of two. It proves neither that the real
class contribution is 97 nor that it is nonzero. The geometric search's failure
is a finite-family result; it does not exclude other geometric functions.

The analytic bound is genuinely complete, but it does not yet remain small at
larger coefficient primes. FIN, ORDER9, and Q36 are unchanged.
