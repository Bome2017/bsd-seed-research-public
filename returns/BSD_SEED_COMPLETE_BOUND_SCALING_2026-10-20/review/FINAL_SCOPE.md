# Final scope check

2026-10-20. Read the final root `REPORT.md` and
`uniform_valuation/PROOF.md`. No mathematical computation was rerun in
this final pass.

**Verdict: supported at the stated written-proof and exact-computation
grades, with the class-completeness boundaries retained.**

1. The previous `1664n1`, p=3 result is correctly counted as unit kernel
   one plus class contribution one, with no valuation contribution.
   The new p=5 statement is a unit-kernel upper bound two; it is not
   presented as a complete unconditional source bound two. Its failed
   class certificate remains visible.

2. On the actual seed, the complete bound has the correct sign:

       unit dimension - actual unit norm rank + surviving class dimension.

   Thus, after eliminating the valuation contribution, an upper bound
   two requires `r_U-k_C >= (p-3)/2`. The class term is positive in the
   upper bound and is not discarded, double-counted as an S-unit term,
   or inferred from known Sha vanishing. Replacing it by the full source
   p-class dimension gives the valid weaker bound.

3. The primitive-divisor formula retains its ramification ratio. Its
   multiplicative channels have integral factors p and one, and their
   Frobenius conditions give precisely the exceptional coefficient
   primes 19,59,487. The conclusion is a uniform removal of this one
   contribution, not a uniform bound on the full source.

4. The corrected argument at two in the final proof is valid and simpler
   than the alternative potential-good argument in this review folder.
   Conductor exponent three forces positive Swan conductor, since
   codimension of inertia invariants is at most two. Wild inertia has
   nontrivial finite 2-group image on each prime-to-two Tate module.
   Its image injects into reduction modulo p>=5, because the congruence
   kernel is pro-p. A nontrivial finite 2-group has an involution, and
   determinant-one inertia makes that involution `-Id` in odd
   characteristic. This uses the retained conductor and Artin/Swan
   theorem; it does not revive the incorrect potentially-multiplicative
   claim for this wild `I_1^*` place.

5. The ordinary coefficient-place proof correctly produces a genuine
   nontrivial scalar: after matching the diagonal entries to alpha,
   taking the pth power kills the off-diagonal nilpotent term. It
   therefore does not assume an unproved split ordinary extension.

6. The final report correctly distinguishes the actual seed's failed
   class/unit calculation from the same-curve control's authenticated
   unit bound. It states no new complete seed bound, new seed-prime
   coverage, FIN, ORDER9 or Q36 conclusion.

This remains same-team model review under explicit retained arithmetic
inputs, not independent human certification or formal verification.
