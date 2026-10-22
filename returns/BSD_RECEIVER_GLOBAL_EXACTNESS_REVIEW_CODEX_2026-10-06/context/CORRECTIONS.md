# Required corrections to the supplied upper-control return

These corrections govern use of the archived original. They do not modify it.

## C1. Theorem C is global, not pointwise local

The opening bullet says every pulled-back local condition equals the finite
condition for p≠4547. Its §6.6 instead relaxes one two-dimensional local H1 at
each of p=19,59,487. Both statements cannot be retained.

Replace the bullet with: “The global pulled-back Selmer group S_p equals the
usual Selmer group for p≠4547. The local conditions may differ at the indicated
exceptional place. Nonzero rational-point localization prevents this relaxation
from adding a global class.”

For proving global equality it is not necessary to strengthen the local
calculation to L_q=H1. It is enough that f_q⊆L_q⊆H1, dim H1=2, dim f_q=1,
and localization of a rational point spans f_q. See the reciprocal-pairing proof
in CORRECTED_PROOF.md; it handles both possible local subspaces.

## C2. The place-2 Tate explanation is inapplicable

For the actual minimal model:

    c4 = 3169004368,
    Delta = 16586638656786071143743744,
    v2(c4)=4, v2(Delta)=8, v2(j)=4.

Thus the I1* label in residue characteristic 2 does not justify treating this
curve as a ramified quadratic twist of a Tate curve. The printed proof does so.

The correct argument needs no such classification: additive reduction has
E0/E1 of order 2, the retained component number is 2, and E1(Q2) is pro-2.
Consequently E(Q2) has no p-torsion for p≥5. Local Euler characteristic and
Tate self-duality give H1(Q2,E[p])=0. This proves exactly the required claim.

Also replace the purported exhaustive list of quadratic-base-change Kodaira
types in §7. The only needed assertion is p-unit Tamagawa factors. Good
reduction stays good; multiplicative valuations at the odd bad primes grow by
at most two under quadratic base change, and their geometric component numbers
are then at most four. The additive places 2 and 4547 are potentially good, so
over a quadratic extension they are either good or additive with component
number at most four. For p≥5 these are p-units. No incomplete type list is needed.

## C3. Supersingular absolute irreducibility needs Frobenius

Two distinct fundamental inertia characters become separate eigenspaces over
F_(p^2). They do not alone imply absolute irreducibility. Over Q_p the retained
Serre description includes an element interchanging the two eigenspaces: the
local image is the normalizer of the full nonsplit Cartan. Its centralizer on
V is F_p. Use this fact, already present in the local-exactness record, in §6.4.

## C4. The displayed S-only Brauer injection is false

The erroneous assertion is

    H2(P,L^×) -> direct_sum_(v in S) H2(P_w,L_w^×) injective.

Here S contains only the places of K' above p. Even when L/K' is unramified
outside S, relative Brauer classes need not be supported on S.

An explicit existence counterexample inside this setup is as follows. P is a
nontrivial elementary abelian p-group. Choose two places v1,v2 outside S, with
Frobenius a fixed nonzero element of P, using Chebotarev. Both have local degree
p in L/K'. Brauer–Hasse–Noether supplies a class with invariants 1/p and -1/p
at v1 and v2, and zero elsewhere. It is nonzero over K'. Restriction to L
multiplies local invariants by p and therefore kills it at every place; it is
a nonzero member of H2(P,L^×). Its localizations at S are all zero. This refutes
the asserted injection, without hypothesizing any seed Sha element.

Correct replacement: the relative Brauer group injects into its local groups
over **all** places. Moreover the image

    image[H2(P,O_(L,S)^×) -> H2(P,L^×)]

is supported on S. At v outside S, localization factors through the units of an
unramified local extension, whose positive-degree cohomology vanishes. Thus
restriction to S is injective on this image. This is sufficient for the
S-unit obstruction term actually appearing in the ambiguous-class sequence.

Theorems A–D do not depend on the incorrect S-only statement.

Sources: [Milne, III §1](https://www.jmilne.org/math/CourseNotes/CFT.pdf)
for unramified unit cohomology, and IV Example 2.14(e) for the full Brauer
localization sequence. The counterexample above is a deduction from those
statements and Chebotarev, not a separately cited seed computation.

## C5. Do not silently assume non-Wieferich localization

The supplied formula already gives

    dim ell_p = 2 - dim loc_p(W).

Since the latter rank can be zero or one, ell_p can have dimension two or one.
Replace subsequent uses of “the line” by “the one- or two-dimensional kernel”.
The formula and the norm-sequence inequality remain valid with this correction.

## C6. Equivalence is not an impossibility theorem

Withdraw these claims from the opening and §11:

* “The input must come from outside this construction.”
* “The class-field-theoretic side ... cannot supply it, because ... the
  class-group side is the Selmer side.”
* “The relative-class/transgression side is exhausted”, if meant to exclude
  further arithmetic input into the S-unit or class-group terms.

Replace them with: “The tested formal cohomological and class-group sequences
give comparisons, and no independent upper bound has been obtained. The
transgression is zero. A new estimate on the class-group or S-unit terms could
still supply the desired bound; no such estimate is proved here.”

An isomorphism transfers an independently proved estimate. It does not make
that estimate circular. The return establishes failure to obtain the bound,
not that these arithmetic objects cannot furnish one.

## C7. Retained results and proof grades

RECEIVER_DESCENT.md in the submitted historical reading set already contains
the H2 vanishing, the same Sylow/torus/no-lift mechanism, global surjectivity,
and the cofinite bound/vanishing equivalence. LOCAL_EXACTNESS.md already removes
the good-prime local error outside the named exceptions. Credit those as
retained results. The new exceptional-prime treatment and Lean support remain
separate contributions.

The new Lean eta assertions evaluate a concrete group-law program at six
points. They do not themselves prove that this program implements the local
Kummer map. The mathematical identification and its hypotheses remain written
imports; the separate torus check independently verifies the needed values.

## C8. Manifest and audit receipts need rebinding

research_return/MANIFEST.sha256 contains the old HANDOFF.md digest, and the old
manifests do not cover all continuation files. The saved build/axiom logs and
ASSUMPTIONS.json refer to the BFR stage. They are historical receipts, not
evidence that the added modules or new proof dependencies were audited.

This review freshly binds all received files, rebuilds the three new modules,
and supplies a new assumptions list and axiom output. Original files and stale
manifests remain preserved so the discrepancy is visible.
