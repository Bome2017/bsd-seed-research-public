# Scoped screen of lower-degree norm reductions

The prior p=7 return already screened this mechanism in `BSD_RANK_TWO_JOINT_CONTINUATION_2026-10-18/class_control/PROOF.md`. I checked the actual p=5 group as a short admission test, not as a new class bound.

G=GL_2(F_5) has order480, scalar center of order4, and the point-stabilizer H has order20. The exact GAP enumeration in `SUBGROUP_SCREEN.json` checks every conjugacy class of subgroups. Every subgroup of index<24 meets the scalar center nontrivially; the minimum index of a scalar-center-free subgroup is24.

Over a characteristic-zero field containing the fourth roots of unity, the faithful scalar component of K[G/H] contains a nonzero H-fixed vector v=sum_z chi(z)^(-1)[zH]. The cosets zH are distinct. For every subgroup J of index<24, its intersection with the scalar center contains an element on which chi is nontrivial. The norm N_J kills the entire faithful component. By contrast N_H v=20v is nonzero. Therefore no rational group-algebra identity N_H=sum a_i N_{J_i} b_i exists using only such smaller-degree fields, including nonnested fields in the same normal closure. This is the same mechanism as the archived p=7 obstruction, now checked for the actual p=5 group.

There is also an independent integral permutation-module obstruction which needs no subgroup enumeration. Let W=Z_5[G/H] and V=F_5^2. Then Hom_G(W/5,V)=V^H is nonzero. If [G:J]<24, then |J|>20; J cannot fix a nonzero vector, since the stabilizer of any such vector has order20. Hence Hom_G(F_5[G/J],V)=0. If a5-unit multiple of the identity on W factored through a sum of these smaller permutation lattices, reduction modulo5 and application of Hom_G(-,V) would give a nonzero map factoring through zero, a contradiction. The dual standard representation gives the analogous test on the inverse scalar character.

This integral argument is about factoring the identity as G-equivariant permutation-lattice maps. It must not be replaced by the invalid argument that N_H acts nontrivially on V modulo5: |H| is divisible by5 and N_H actually acts as zero there.

Primary-source scope: Etienne defines generalized norm relations for non-Galois fields as identities with left side N_H and derives arithmetic algorithms from them. Biasse–Fieker–Hofmann–Page explains why the integer denominator matters for class-group control. Those frameworks are genuine, but this specific smaller-degree application fails its representation-theoretic admission test. The screen does not exclude arithmetic bounds particular to this seed, larger/equal-degree auxiliary fields, reflection theorems with separately controlled errors, or the new closed-support elliptic-function construction.

Sources freshly opened:

- [Fabrice Etienne, Computing class groups by induction with generalised norm relations](https://www.math.u-bordeaux.fr/~fetienne002/computing_class_groups.pdf), introduction and generalized relation definition.
- [Biasse, Fieker, Hofmann, Page, Norm relations and computational problems in number fields](https://www.normalesup.org/~page/Recherche/Documents/articles/brauer.pdf), Proposition B and the denominator-sensitive class comparison.

No class-group bound or FIN conclusion follows from this screen. The active review proceeds to the arithmetic producer's actual closed-support identities.
