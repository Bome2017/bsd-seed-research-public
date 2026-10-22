# The twist changes the faithful class sector

Let E0=11a1 and E1 its -47 twist in the submitted models. Completing the square with Y=2y+1 gives

    E0: Y^2 = 4x^3-4x^2-40x-79,
    E1: Y^2 = 4x^3-4x^2-91304x+9647521.

The exact substitution x1=-47x0+16, Y1=-47 sqrt(-47) Y0 identifies them over Q(sqrt(-47)). The independent checker verifies the cubic polynomial identity over Q.

Choose corresponding nonzero seven-torsion points and identify their x-coordinate fields B via this rational affine substitution. Under the retained full-image and irreducibility inputs, [B:Q]=24 and each point field A0/B and A1/B has degree two. A0 has discriminant -7^47*11^36, independently read from the retained maximal-order data. Since Q(sqrt(-47)) ramifies at47 while A0 does not, sqrt(-47) is not in A0.

Set L=A0(sqrt(-47)). Then L/B is biquadratic. Write a for the involution negating Y0 and fixing sqrt(-47), and b for the involution fixing A0 and negating sqrt(-47). Its three quadratic intermediate fields are

    A0=L^{<b>},   A1=L^{<ab>},   B(sqrt(-47))=L^{<a>}.

This is a field-theoretic statement, independent of any class computation.

## Seven-primary class components

Put M=Cl(L)[7]. For any quadratic intermediate field K, extension and ideal norm satisfy N j=2 and j N=1+tau, where tau generates Gal(L/K). Since two is invertible modulo seven, extension gives an isomorphism Cl(K)[7] -> M^{tau}. This elementary identity retains the entire seven-torsion class group and does not assume its size.

The four commuting eigenspaces for a,b are direct summands. The odd relative class components are therefore

    Cl(A0)[7]^{-}  = M^{a=-1,b=+1},
    Cl(A1)[7]^{-}  = M^{a=-1,b=-1},
    Cl(B(sqrt(-47)))[7]^{-} = M^{a=+1,b=-1},

where each equality means the canonical identification via extension.

The scalar action sigma3 on A0 lifts to L by fixing sqrt(-47), and commutes with a,b. On both point fields sigma3^3 is point negation. Both faithful characters have chi(sigma3)^3=-1, so they lie in the odd components above. Thus the original and twisted faithful components occupy DIFFERENT b-eigenspaces, even though their x-field is the same.

In particular a class in the twisted faithful component has cross-norm to A0 equal to zero: after extension back to L, that norm is (1+b)x=0, and extension from A0 is injective. Its cross-norm to B(sqrt(-47)) is also zero, using (1+a)x=0. There is no induced upper bound for the twisted component from a bound on either of those two other components through these maps. This remains true even if the old provisional class-number-one answer were independently certified.

This does not rule out a larger construction involving the class group of L, extra ideal relations, or an independent analytic comparison. It identifies precisely which new component such a construction must control. No class bound has been obtained here.

## Independent valuation-source audit

The supplied actual prime permutations at7,11,47 have orders dividing three. The independent checker reconstructs their permutation matrices and verifies both faithful eigenspaces (eigenvalues3 and5 in F7) are zero. It also verifies every sum of ramification index times residue degree is48. Since3^3=5^3=-1 modulo7, the elementary equation sigma3^3 v=v=-v forces v=0.

Thus the ENTIRE faithful S-divisor source, for S={7,11,47}, is zero. The allowance t_D,chi is zero without any sampling or class-group completeness assumption. The exact factorization/permutation data and identification of sigma3 with the actual scalar automorphism remain retained producer inputs; this review checks their stated mathematical consequence, not a fresh refactorization of all ideals.

Consequently the remaining exact sequence is the ORDINARY virtual-unit sequence

    0 -> U^chi -> V^chi -> Cl(A1)[7]^chi -> 0.

It is not the S-class quotient. Vanishing of this divisor source removes the valuation allowance only; it does not remove the ordinary class term.
