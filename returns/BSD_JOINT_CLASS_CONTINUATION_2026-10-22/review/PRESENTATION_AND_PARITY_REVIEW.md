# Independent review of the presentation defect and source parity

Date: 2026-10-22. Scope: `sources/PRESENTATION_DEFECT.md` and
`arithmetic/PROOF.md`, read in full. This is a desk proof review, not a fresh
replay of the exact seed arithmetic.

Verdict: both elementary deductions are supported as stated. Neither is a
small class bound or a FIN result.

## Presentation defect

The diagram has exact rows `0 -> K_A -> P_A -> C_A -> 0` and its target
analogue. The displayed snake sequence is correct. In particular, the
quotient of ker(u) by the image of ker(U) is a subgroup of
K_B/U(K_A). For finite **abelian** p-groups every subgroup and every quotient
has generator rank at most that of the original group. One proof for
subgroups uses H[p] inside G[p]; one proof for quotients uses G/pG onto
Q/pQ. The generator-rank extension inequality follows by lifting a generating
set of the quotient and adding generators of the submodule. Thus

    d_p ker(u) <= d_p ker(U) + d_p(K_B/U(K_A)).

It is important that the paper says finite abelian p-groups; this is not a
claim for arbitrary finite p-groups. When K_B=0, the correction disappears,
so complete source generation plus an exact target p-presentation is a
legitimate asymmetric certificate. The displayed target-error example is
valid and shows why a full-rank lifted matrix alone is insufficient.

The warning about P[p] -> C[p] is correct: quotienting Z/p^2 by its subgroup
p(Z/p^2) annihilates the source p-torsion but leaves target p-torsion.

## Parity and extraction of roots inside A

If tau(a)/a is a sign, then [a] is tau-invariant in A*/A*^p for odd p,
because -1=(-1)^p. Commuting scalar translates and their products preserve
that property. If b^n is one such product, then

    (tau(b)/b)^n in {1,-1}.

Hence tau(b)/b is a root of unity of order dividing 2n. A field with a
real embedding has only the roots of unity +1 and -1, since the embedding
preserves the order and its image is real. Thus [b] remains invariant.
This works for every n, not only odd n, and does not assume that the chosen
real embedding is fixed by tau. The requirement b in A is essential.

For a virtual unit with div(a)=pI, signs have zero divisor, so
p(tau(I)-I)=0. The divisor group is torsion-free, giving tau(I)=I. Therefore
faithful class support cannot evade the same parity exclusion.

The two displayed fifth-root identities are exact: the sign powers are
6 and 7 respectively. The idempotent denominator four is a five-unit.
The statement about functions of the isomorphism class of (E,P) is also
correct at weight zero without additional framing: [-1] gives an
isomorphism (E,P) to (E,-P). The exceptions for Hodge-line sections,
multiplier-valued functions, extra level structure and larger fields must
remain attached.

## What an analytic class-product check can and cannot certify

Let selected ideals generate H inside the true class group C, and let a
finite presentation P surject onto H. Write

    Q=C/H,   K=ker(P -> H).

Let an authenticated full-rank unit subgroup U0 have index j in the full
unit group, and use identical regulator conventions. Then

    h(C) Reg(U) / (|P| Reg(U0)) = |Q| / (|K| j).

This exact formula retains the omitted-generator, hidden-relation and unit
errors. A numerical analytic class-product match alone cannot prove that
Q has trivial p-part, even when U0 is p-saturated: Q and K can have equal
arbitrary p-power order and cancel. The abstract diagram P=C=(Z/p)^e
with selected subgroup H=0 has Q=K and analytic ratio one. This is not a
number-field realization; it refutes that inference from the listed data.

A changed sufficient certificate can bypass this presentation cancellation by
reconstructing the actual relative class number from the analytic relative
class product and a p-saturated relative-unit lattice. That separate proposal
is audited in `RELATIVE_RECONSTRUCTION_REVIEW.md` when its precise constants
and denominator bound are available. It requires actual units and a certified
analytic interval; neither can be replaced by the provisional BNF class
number or an unlabelled floating-point regulator.
