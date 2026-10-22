# Second-torsion push: what passed, and what reached the missing bound

**LOCAL_EXACTNESS_CONFIRMED_AT_RETAINED_INPUT_GRADE.**
**NO_NEW_UNIFORM_UPPER_CONTROL_FROM_THE_TWO_TESTED_EXTENSIONS.**

The new local lemma is correct under its stated hypotheses. Together with the
named retained global inputs, it gives

    Hom_Gamma_p(Cl(O_Lp[1/p])/p, E[p]) ~= Sha(E/Q)[p]

outside {2,3,19,59,487,2243,4547,5843}. This includes ordinary and supersingular
good primes, and does not assume that either rational generator localizes
nontrivially. The receiver's former possible extra local line is removed.

I independently read Serre's relevant scanned statements, reviewed the local
and completion arguments, checked the other new identities, verified 30/30
manifest entries, and reproduced both supplied programs. See REVIEW.md. The
seed's residual image, global Kummer group, saturated basis, global descent
and parity remain retained inputs at their existing grades.

## Actual attempts beyond the comparison

1. **Relate two different tails directly.** Use two pencil values with the same
   selected prime, cancel that prime, and reduce their quotient to the old
   factor base. The resulting row is exactly rho_n-rho_m over the integers.
   This does not increase the span of the existing rows. This is proved for
   the actual fixed reductions, not inferred by changing the convention.

2. **Recover the p lost by a translation norm.** The selected prime has a free
   translation orbit of length p. The norm's valuations there are (1,...,1).
   They cannot be divided by p. The first group-ring derivative likewise has
   valuations (0,1,...,p-1), not a p-divisible divisor. Thus these actual
   elements do not supply a divided relation. Moreover, even a principal
   divisor p Delta need not make Delta principal: the exact Q(sqrt(-47))
   control exhibits a nonzero order-five class this way, including after
   inverting five.

These are scoped failures of two concrete attempts. They do not refute the
original pencil, arbitrary additive identities, refined reciprocity maps, or
an independently proved rank/saturation theorem. The new proofs are written
derivations with exact controls, not independently reviewed results themselves.

## What would actually move the uniform step

The comparison now tells us exactly what a successful bound would control.
For the cofinite domain above, an independently proved bound dim B_p<=1 forces
B_p=0 by retained parity. A bound on a rigorously defined larger selected-row
kernel also suffices. That would prove cofinite primary vanishing; finiteness
at the remaining coefficient primes is still a separate FIN obligation.

The two attempts in this review do not provide that bound. They also show why
two proposed substitutes do not count: a new expression for a linear combination
of existing rows adds no rank, and formal division by p does not create an
integral principal relation.

For a divided-relation construction, the concrete next obligation would be
to construct integral divided divisors AND independently control their actual
ideal classes in the required representation. For a different additive identity,
the obligation is to prove a new independent constraint on the old coordinates.
Neither obligation has been solved here; neither is presented as a new theorem
or a ready computational task. A common rational scalar or this particular
class-group method is not mandatory for uniform FIN.

**Assessment:** this remains an exact arithmetic route to the seed's uniform
problem. This pass does not establish that its missing bound is easier, or that
more instances of its relations will supply it. I would not launch a relation
enumeration or a fixed-prime campaign on the strength of this packet.

No new vanishing prime, cofinite vanishing theorem, fixed annihilator or
leading-term comparison was obtained. No release, build map, memory, remote
repository or other session was modified.

FIN, ORDER9 and Q36 are unchanged.
