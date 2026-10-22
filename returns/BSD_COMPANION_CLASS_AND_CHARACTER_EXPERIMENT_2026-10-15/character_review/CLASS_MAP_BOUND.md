# Upper bounds using the actual ideal-class norm kernel

Written deduction, 2026-10-17. This improves the form of an available arithmetic upper bound when an actual ideal-class correspondence is computed. No such additional computation is claimed here.

Use the actual incidence correspondence u, including the primitive ramification-weighted map on divisors. It sends principal divisors to principal divisors and hence induces ordinary and S-ideal-class maps

    u_C,S : Cl(A,S) -> Cl(B,S).

It sends chi to chi^-1. The virtual-unit class map sends alpha with `div_S(alpha)=p a` to `[a]`. Therefore it commutes with u: `div_S(u(alpha))=p u_D(a)`. In particular, every admitted alpha projects to the kernel of u_C,S on p-torsion.

Let `k_C,S,chi` denote the dimension of that p-torsion kernel. The snake lemma applied to

    0 -> U_A,S/p -> A(S,p) -> Cl(A,S)[p] -> 0

and its B analogue gives the exact sequence

    0 -> ker(u_U mod p) -> K_chi -> ker(u_C,S on p-torsion)
      -> coker(u_U mod p).

Thus, with an actual connecting map partial,

    dim K_chi = s_US,chi + k_C,S,chi - rank(partial)
              <= s_US,chi + k_C,S,chi.                 (A)

This replaces r_AS,chi by a potentially smaller arithmetic quantity. The connecting map must not be presumed zero.

There is also a source-only version. Let K_empty be the norm kernel in ordinary virtual units. The valuation sequence yields

    dim K_chi <= dim K_empty + t_D,chi.

Applying (A) to the empty set gives

    dim K_chi <= s_U,chi + k_C,empty,chi + t_D,chi
              <= (p+1)/2 + k_C,empty,chi + t_D,chi.    (B)

Here `k_C,empty,chi` is the ordinary source-to-companion p-class kernel. This is a valid refinement of equation (4), without identifying the actual unit lattice with a geometric permutation lattice. It retains both unit and class-supported directions.

A class-map computation can certify k_C from generators, relations, and the actual image of each generator under the incidence ideal norm. Certified upper presentations can be used, but a provisional class group or an unverified lift of its generators cannot silently establish the dimension of the true kernel. To prove only an upper bound one can instead supply an independently certified presentation of a group surjecting onto the relevant kernel.

For the seed the main difficulty remains arithmetic: the class map has not been evaluated here. The existing known Sha dimension is not an input to (A) or (B), and these formulas are not used to infer an uncomputed class kernel from it.
