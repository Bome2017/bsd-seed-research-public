# Certified rank-one D=-23 twist and its exact implication

The computation completed on 2026-09-21. RESULT.json and the independent metadata/custody replay in COMPLETION_REVIEW.json supply the computer-assisted premise

\[
39.512236\le L'(E^{-23},1)\le40.182321.
\]

Every displayed endpoint is an outward-rounded rational. The original comparison cutoff, rounded to 3,456,106,495, sufficed; no extension was run. The mathematical implication is as follows, with the explicitly retained trust qualifications at the end.

Let E be the retained curve y²=x³−22735x²+106272484x and K=Q(sqrt(−23)).
The discriminant −23 is fundamental, coprime to N, and is 1 modulo 8. Exact Euler-criterion calculations show that every odd bad prime 3,2243,4547,5843 splits in K; 13 also splits. The seed root number is +1. Therefore the coprime twist formula gives

\[
N(E^{-23})=23^2N=3440186458738710936,\qquad
w(E^{-23})=\chi_{-23}(-N)w(E)=-1.
\]

Consequently the central L-value vanishes. The Fricke-folded Mellin integral gives the derivative series in DESIGN.md. A final Arb enclosure excluding zero, with its full coefficient and arithmetic error included, proves

\[
\operatorname{ord}_{s=1}L(E^{-23},s)=1.
\]

The standard Gross–Zagier–Kolyvagin analytic-rank-one theorem then gives rank E^{-23}(Q)=1 and finiteness of Sha of the twist. This is the same imported rank-one theorem used in the retained MCS_DERIVED_HEIGHT_GATE.md, section 3; its proof is not re-proved here.

Using the retained rank E(Q)=2 and rational Galois eigenspace decomposition,

\[
\operatorname{rank}E(K)
=\operatorname{rank}E(Q)+\operatorname{rank}E^{-23}(Q)=3.
\]

This fixes an actual K in the previously conditional rank-three comparison. For every prime satisfying the exact regime (P) in MCS_NONSQUAREFREE_JOIN.md and splitting in this K, the retained comparison and Kummer splitting give

\[
\operatorname{Fitt}^{\,i}_{\mathbf Z/p^n}
  \bigl(\Sha(E/K)[p^n]^*\bigr)
=I_{i+3}(\epsilon^{\rm Hg}_{n,0}).
\]

In particular p=13 meets that regime using the retained a13=−4 and #E(F13)=18 and the exact splitting check. The ideal on the right is not evaluated. Finiteness of Sha of E^{-23} does not imply finiteness of Sha of E or E/K.

The new numerical assertion needs the retained verified coefficient corpus, the imported functional equation and conductor facts, the written tail/model bounds, and the new compiled Arb adapter. The rank and Fitting consequences additionally import the existing Mordell–Weil and source-composition grades. There is no Lean verification or independent human review of this new computation.

No order of Sha of the twist is computed. No new primary group of the seed is settled, and FIN, ORDER9 and Q36 remain open. No subsequent ideal-evaluation or next-prime computation is part of this operation.
