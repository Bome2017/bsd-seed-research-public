# Relative class certificate: a weaker sufficient computation

Date: 2026-10-20. Status: CERTIFICATE_INTERFACE_DERIVED;
UNCONDITIONAL_GENERATION_TEST_FAILS_AT_CURRENT_CUTOFF.

The relative method is mathematically genuine. It can collect faithful
class relations on the actual seed while cancelling base-extended ideals,
without computing a full base class group or principalizing those ideals.
The exact invariant and content-stripping operation are in
RELATIVE_ALGORITHM.md; the arithmetic implementation is in the sibling
lane and is not certified merely by this theory note.

For an upper bound, full class-group reconstruction is unnecessarily
strong. Let m be the number of selected faithful ideal columns, r_C the
rank of authenticated relation rows modulo p, and q the dimension of the
class component missed by those columns. If r_U is a verified lower bound
for the unit norm/local rank, the complete source bound is

    dim K_chi <= (p+1)/2-r_U+m-r_C+q.

PRESENTATION_BOUND.md proves this bound, including the ordinary class term.
At p=5, a generation-modulo-five certificate q=0 and
r_U-(m-r_C)>=1 would give bound at most two. Full relation saturation,
exact class orders, and a complete unit basis are not necessary. Those
relaxations do not justify dropping q.

I tested an available unconditional generation theorem against the actual
seed inventory rather than leaving it as a suggested next task. The
inventory contains every prime ideal with norm <=419775: 35,749 ideals
and 35,923 prime-power terms in the sum. Belabas–Diaz y Diaz–Friedman
Corollary 5.2 fails at T=419776. Its displayed sides are approximately
23.9784935 and 416.9969039; the independent exact acceptance calculation
proves LHS<56.181252468 while RHS>352. The exact calculation uses only
rational bounds, and check_bddf.py records input hashes.

This outcome does not show that the selected primes fail to generate. It
shows that this particular unconditional criterion does not certify that
they generate. Generation modulo five, which is weaker than full class
generation, remains available as a separate target requiring actual proof.

The small relative discriminant norm 2^4*5*4547^6 does not remove the
base-field discriminant from the known absolute bound. No replacement
bound depending only on this relative norm is supplied by the inspected
Cohen algorithm. This is a source-scoped finding, not a nonexistence claim.

No class contribution has been set to zero, no GRH result promoted, and
no seed Selmer upper bound obtained in this theory lane. The actionable
threshold is now weaker and explicit: prove generator coverage modulo p,
then obtain enough actual relative relations and unit norm rank. FIN,
ORDER9, and Q36 are unchanged.
