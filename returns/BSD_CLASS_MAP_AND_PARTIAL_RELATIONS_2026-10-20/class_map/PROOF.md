# Complete source proof and arithmetic bindings

## 1. Actual correspondence

Let A be the nonzero three-torsion point field, and B the affine-line companion field for the displayed elliptic curve. The retained short-model incidence construction embeds A in the cubic B-algebra

    X^3 - m^2 X^2 + (m^4+2a)X -(m^6+2am^2-4b),

where m=z/6 and z satisfies the saved degree-eight companion polynomial. The code verifies the source polynomial, both universal point coordinates, and the prescribed embedding before taking the cubic algebra norm u.

The induced divisor map u_D is the primitive arithmetic push-pull map: div(u(alpha))=u_D(div(alpha)). It is not an unweighted permutation-incidence count. For an ideal I with I^h=(beta), torsion-freeness of the divisor group gives

    u_D(I)=div(u(beta))/h.

The arithmetic checks divisibility of every exponent and reconstructs the whole target ideal. It does not infer principality of that ideal from principality of its h-th power.

## 2. Class map and connecting map

For the ordinary virtual-unit groups A(empty,3), B(empty,3), use the exact rows

    0 -> O_A^*/O_A^{*3} -> A(empty,3) -> Cl(A)[3] -> 0

and its B counterpart. The fields have real embeddings and therefore no third roots of unity. Both certified unit ranks are four. The certified source class group is cyclic of order six, so Cl(A)[3] has dimension one.

Take I equal to the square of the certified class-group generator. The exact source certificate supplies I^3=(beta). The target calculation supplies J=u_D(I), a literal rho with J=(rho), and

    e=u(beta)/rho^3 in O_B^*.

The saved integer coordinates of e and the computed norm-unit matrix exhibit e as u(v) times a literal cube. Hence the source 3-class lies in ker u_C and its connecting class in coker(u_U mod3) is zero. Since it generates Cl(A)[3], the ideal-class kernel dimension is one and the connecting-map rank is zero.

For 1664n1 the actual four-by-four unit matrix has determinant -3 and rank three modulo three. The snake lemma therefore gives the exact equality

    dim ker u on A(empty,3) = dim ker u_U + dim ker u_C - rank partial
                           = (4-3)+1-0 = 2.

This is a complete-source calculation because both BNF computations were certified, and actual fundamental units and an actual generator of the entire source 3-class group were used. A matrix on selected units alone would not justify this equality.

## 3. Faithful S-source

For S={2,3,13}, the source valuation group has a basis consisting of the actual prime ideals above S. The scalar involution tau=[-1] fixes every such prime, as verified on exact HNF ideals. A minus-character class has valuation vector v satisfying tau(v)=-v mod3, while here tau(v)=v. Thus 2v=0, so v=0.

It follows that

    A(S,3)^minus = A(empty,3)^minus.

Consequently

    dim ker(u:A(S,3)^minus -> B(S,3)^minus) <= 2.

The support calculation also reconstructs the ramification-corrected divisor norm and verifies scalar equivariance, rather than identifying actual prime-ideal valuations with geometric orbit counts. The upper bound does not need a nonsingularity hypothesis for heights or a conjectural Sha formula.

## 4. What follows and what does not

The bound is for a necessary source in the established three-descent architecture. SOURCE_APPLICATION.md identifies the precise published injection (Schaefer–Stoll Corollary 7.9 and Proposition 7.10), matches S and the incidence map, and states the control Selmer consequence conditional on the retained rank-two input. The original seed is a different curve. This coefficient-three control cannot establish scaling at seven or larger primes, cofinite Sha vanishing, FIN, ORDER9, or Q36.

The selected class is not excluded by the norm. It survives and is point-occupied; one ordinary unit direction also survives. This is precisely why class-group zero is an unnecessarily strong target. The complete total, rather than the vanishing of each separate source sector, is what is bounded here.

## 5. Arithmetic status distinctions

Mirror389's map and connecting obstruction were predetermined by the old norm-cube lift; their fresh ideal authentication does not constitute a new bound. The 64-row source search and fourteen point-occupancy calculations are provisional BNF selection data; only 1664n1 was newly promoted by complete source certification. Its target was also certified. No negative selection result is a theorem excluding further examples.
