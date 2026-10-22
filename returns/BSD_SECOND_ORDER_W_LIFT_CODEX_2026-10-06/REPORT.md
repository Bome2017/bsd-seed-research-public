# Second-order lifting and the actual character-realization gate

Date: 2026-10-06. This continues the supplied Pro review of lab bb6ed896.

**SECOND_ORDER_COMMON_CORRECTION_CRITERION_DERIVED.**
**FIXED_TAME_EQUAL_CHARACTERISTIC_FORMAL_STAGE_REFUTED.**
**MIXED_CHARACTERISTIC_CHARACTER_CONSTRUCTED; POINT_LIFTING_OPEN.**

All new mathematical assertions have written proofs and remain subject to
independent review. The Stage-A span and the seed inputs retain their
provisional grades. The 9,915 exact algebra assertions pass; none computes
a seed Selmer group or the new arithmetic obstruction value.

## The requested calculation was carried out

For an actual lambda in D^W, let R_lambda=ker b_lambda. The finite-module
Cassels--Tate construction gives an alternating second obstruction

    h_lambda^(2): R_lambda x R_lambda -> F_p.

For the two known point classes w1,w2 define

    alpha_lambda=h_lambda^(2)(w1,w2).

The exact answer to the question about ONE common eta is:

    both prescribed first lifts can be corrected and lifted to order three
      if and only if alpha_lambda=0.

The proof solves all the other terms using Stage A. It identifies the
correction-map cokernel with wedge^2(W^*), a single dimension. Changing
the first lifts does not change alpha_lambda. A common eta cannot change
it either, because eta contributes a symmetric form and this remaining
restriction is alternating.

This is an exact criterion, not a proof that the seed fails it. No seed
alpha_lambda was evaluated, and no useful direction with alpha_lambda=0
was constructed. An unconditional POINT_SECTIONS_ORDER3 status would be
incorrect. See [the full proof](SECOND_ORDER_PROOF.md).

## The planned formal stage needs a substantive correction

The next stage in the supplied chain cannot literally use a nonzero fixed
tame scalar character over F_p[[t]]. At any already ramified q!=p, local
reciprocity bounds the abelian p-inertia order by p^v_p(q-1), whereas
1+t F_p[[t]] is torsion-free. A nonzero linear inertia term cannot even
lift through t^(p^v_p(q-1)) in that characteristic.

This failure is independent of Sha. More second-order algebra cannot fix
it. It also persists for matrix deformations with the same scalar
first-order term, by taking their determinants. It does not invalidate
Stage A, which needs only dual numbers, or the actual order-three and
order-four modules used in this return.

The source OpenAI manuscript uses moving conductors and a separate true
torsion-free variable. Our result does not refute that different setup.
It corrects the proposed extrapolation of this FIXED seed direction to
all equal-characteristic orders.

## A concrete repair, with its precise limit

The actual character chi_lambda(g)=zeta_p^[lambda(g)] over O=Z_p[zeta_p]
exists. The representation

    T_p(E) tensor O(chi_lambda)

reduces modulo pi^3, pi=zeta_p-1, to the same exponential order-three
module after the explicit coordinate change u=pi-pi^2/2.

One cannot freely insert any eta into this fixed character. But Stage A
allows a useful repair: choose lambda with ker b_lambda=W. If
alpha_lambda=0, changing the first point lifts then kills the ENTIRE
second obstruction with eta=0. Thus the finite lifting test fits a
genuine characteristic-zero character without requiring a fictitious
free correction parameter.

This constructs the ambient arithmetic representation, not its point
sections. Higher mixed-characteristic lifting, generic rank two and the
specialization/index comparison are unproved. See
[character realization](CHARACTER_REALIZATION.md).

## Concurrent material checked during this turn

The lab advanced from bb6ed896 to e7abad93 while this work was underway.
The new Aristotle return and revision-two task were read and bound here.
That return uses a strict-space scalar direction module and reports a
single-plane determinant failure; its Lean and arithmetic were NOT replayed
in this turn. It is not an independent reproduction of the full-Selmer,
vector-valued Stage-A construction used here.

The new revision-two task requests this same second-order correction
calculation. This return supplies a result to compare with it, and the
additional character-realization correction. No remote job was started or
messaged. The concurrent records are preserved in the lab and in input/.

## Effect on BSD

FIN, ORDER9 and Q36 are unchanged. There is no new primary certificate,
cofinite upper bound, fixed annihilator, or completed determinant switch.

What can responsibly be continued is narrower than the supplied chain:
prove the simultaneous second-pairing vanishing for useful actual tame
directions, then lift the point sections in a specified arithmetic
coefficient ring. The fixed-character F_p[[t]] implementation should be
stopped now. A determinant job based on its alleged generic point sections
would start from a nonexistent family.

These are not all remaining BSD problems: even successful point lifting
would still leave the independent cross-prime support comparison. This
return does not present the repaired character as an established route
through that last step.
