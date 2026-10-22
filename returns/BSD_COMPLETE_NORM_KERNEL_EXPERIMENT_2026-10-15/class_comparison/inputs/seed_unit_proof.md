# Proof and normalization of the continued norm experiment

Read reviewer/REPRESENTATION_SCREEN.md for the signature, exact unit exhaustion and general scalar-character count. Read reviewer/INCIDENCE_NORM_REVIEW.md for the integral incidence identities and the supplemental number-field class-number calculation. Both are written same-team deductions under the specified retained inputs.

## Exact line algebra for the original seed

The stored source representation uses the minimal model. Its x-coordinate is related to the original model by x_original=x_minimal+7578, while y is unchanged. Put a=-22735, b=106272484. With the dual-field generator z, set s=z/3 and

    n=(a^2+2 a s^2-3 s^4-3 b)/(6s).

The intersection y=sx+n has algebra

    B[x]/(G),    G=x^3+(a-s^2)x^2+(b-2sn)x-n^2.

The exact producer verifies that G divides the 3-division polynomial, reconstructs the source generator w from the y-coordinate, and verifies both original-model coordinates. Its three distinct finite points are 3-torsion and sum to O by the elliptic chord law. They cannot form the line through zero, since all three are nonzero. They therefore form one affine line of E[3] missing zero. The degree-eight irreducible slope polynomial gives the full orbit of eight lines.

Taking the algebra norm B[x]/G -> B is therefore the actual incidence norm. The exported exact roots satisfy u(a_i)=r_i^3 for the two point and two cubic source images. Compact cube corrections of those images change their norms by literal cubes, so the unit representatives satisfy the same admission condition. The checker verifies the norms again as determinants of multiplication matrices.

## Integral composition and its limitation

For a function alpha on nonzero vectors, double incidence counts alpha(P) p times, every vector outside the line through P once, and every other scalar multiple of P zero times. On an odd scalar-character unit lattice, products along each complete nonzero scalar line are trivial. Thus double incidence is multiplication by p. The reverse statement is identical. The first norm interchanges the scalar-coordinate characters chi and chi^{-1}; these must not be identified for p>3.

These are integral maps on torsion-free Z_p lattices. Their compositions p Id imply injectivity, full rank, and cokernels killed by p. Their Smith exponents belong to {0,1}, with complementary counts in the two maps.

At 3, the complete source antiunit lattice has rank two and both independent mod3 classes are admitted. First replace each representing unit a by a/tau(a). This makes it literally norm one and multiplies its anti-invariant mod3 class by 2, preserving independence. Each image is a cube in B. A cube root of a unit is a unit, and the antiunit condition passes to its root because the field has no nontrivial cube roots of unity. Hence u maps into 3 times the target lattice. Both Smith exponents are at least one and at most one. They are exactly (1,1); the reverse map has exponents (0,0).

For general p the scalar-component rank is r=(p+1)/2. The pair diag(p I_s,I_(r-s)), diag(I_s,p I_(r-s)) satisfies the same compositions for every s. No asserted uniform bound on s follows from the composition. Proving a small value requires additional arithmetic of the actual lattices, not another use of the same identity.

## The class coupling actually tested

For the valuation-zero source B0, units U and C=Cl(K)[3], the class boundary fits 0 -> U -> B0 -> C -> 0. Given admission defect D, the map c -> D(beta) mod D(U) is independent of the ideal-cube lift beta. Its kernel consists of class directions that can be repaired by units. The producer gives explicit repairs for both source class directions. On this tested span the map is zero. This does not assert class/unit splitting or a perfect pairing.

The source-independent two-unit argument also proves the (0,1,1) filtration for the four actual classes. Any unit class in their span must be anti-invariant and therefore in the two-dimensional norm-one unit plane already spanned by P1 and beta1/beta2. Its intersection with the point plane is exactly the P1 line, by four-class independence. All four full ideal valuations are multiples of3. The exact filtration sequences then give one unit and one ideal-class direction in the quotient, without knowing the complete class group.

## Scope

The coefficient3 is a bad prime for the seed. These calculations do not demonstrate the same kernel sizes at good p>=5. The norm identity is general, but the arithmetic Smith counts, class groups and local defects vary with p. No uniform arithmetic estimate, new prime exclusion, FIN, ORDER9 or Q36 result has been obtained.
