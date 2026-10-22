# Class map experiment: complete bound on a new coefficient-three control

Date: 2026-10-20.
Status: COMPLETE_FAITHFUL_NORM_SOURCE_UPPER_TWO_ON_1664N1; NO_SEED_OR_UNIFORM_BOUND.

The changed experiment produced an arithmetic upper bound on the entire necessary norm source for the rank-two database control

    E: y^2 = x^3 - 4x + 16  (1664n1), p=3, S={2,3,13}.

The point-field A and companion line-field B both have certified ordinary class group C6. Their complete ordinary unit groups have rank four. The actual incidence norm on these unit groups modulo cubes has rank three. Its map on the one-dimensional ordinary 3-class group is zero, and its connecting map is zero, verified by a literal unit repair and cube root. Therefore

    dim_F3 ker(A(empty,3) -> B(empty,3)) = (4-3)+1 = 2.

Every source prime above S is fixed by the actual scalar involution [-1]. Consequently the faithful (minus) divisor component is zero: a faithful S-virtual unit is already an ordinary virtual unit. Thus the complete faithful S-norm source has dimension AT MOST TWO. This accounts for ordinary units, all ordinary 3-classes, and the entire allowable valuation layer; no class-zero assumption is used.

This is a new finite-control bound at coefficient three. It is not a bound for the original BSD seed, a larger coefficient prime, or an infinite set of primes. SOURCE_APPLICATION.md spells out the published Selmer injection and the conditional control conclusion using the retained rank-two input. This is not a fresh rank certificate or a novelty claim about this control. FIN, ORDER9 and Q36 are unchanged.

## Correction to the original proposed test

The proposed mirror389 versus old rank-two class-map contrast was not an open discriminating test. In the old record, a norm-cube lift already represented the whole faithful class direction. That forces both its ideal-class map and connecting obstruction to vanish. Mirror389 was retained only as an authentication control; its ordinary norm kernel of dimension one is old information.

We changed the source before continuing. The frozen 64-row panel covers conductor 1639 through 2429, with database rank two and good reduction at three. Fifty-nine sources passed degree-eight transitive-field construction; five (1856d1,1862a1,1922b1,2350c1,2366e1) did not. These five are exclusions from this implementation, not class-group bounds or timeouts. All 59 provisional BNF presentations have 3-rank at most one.

Within the SAME panel, an explicitly sealed adaptation computed the actual ordinary class images of the displayed point combinations for the fourteen sources with 3-divisible provisional class number. Each faithful class sector had dimension one and was occupied by displayed rational-point images. This is selection evidence, not fourteen certified upper bounds. The 2080d1 file includes a third displayed torsion point; the coordinate count three is not a claim of Mordell-Weil rank three.

The first new source, 1664n1, was then certified and its complete norm source computed. The resulting bound arises from the combined unit and class calculation, not from rejecting its surviving class: that class survives, alongside one unit direction.

## Exact arithmetic

With the certified source and target unit bases, the integer unit norm matrix is

    [-1  0  0  0]
    [ 0  1  1  0]
    [ 0  0  0 -1]
    [ 0 -1  2  1].

Its determinant is -3; its rank modulo three is three. The class-generator ideal I has norm 409600. From the exact relation I^3=(beta), the primitive incidence image J is recovered from div(u(beta))/3. At the ramified target prime over 2 the valuation of u(beta) is 126, and J has valuation 42; the ramification is retained. At the degree-one and degree-two primes over 5 the valuations are 6, giving J-exponents two. J has norm 68719476736000000.

A literal element rho satisfies J=(rho). The unit u(beta)/rho^3 has target coordinates (1,1,0,-1); source unit exponents (2,1,0,0) repair it modulo cubes. A saved literal cube root verifies the repair exactly. No principality is inferred merely by dividing a principal ideal relation.

The support check independently reconstructs the primitive divisor correspondence at every prime above 2,3,13, using certified principalizations P^6=(beta_P), exact incidence norms, and division of valuations by six. The integral coefficients and scalar equivariance are checked. The source faithful divisor dimension is zero.

## Verification and limitations

Source bnfcertify returned 1; target bnfcertify returned 1. Two clean-directory replays per control pass with empty stderr and byte-identical exact ideal-map certificates. The accepted program is one guarded GP function, so a runtime error exits the arithmetic body before its completion marker. The Python driver additionally rejects nonempty stderr and missing certificate files.

Earlier rejected attempts are retained: GP's reserved I symbol, binary-restored source variable t19 versus w, and invalid raw-byte replay comparisons caused by GP write appending to an existing file. The accepted code asserts equality of source polynomials after variable transport, substitutes the actual source variable into the incidence embedding, and replays only into clean directories. Earlier success-like stdout markers with errors are NOT evidence.

The class map and unit norm construction use the retained incidence interpretation already established in the project. The new BNF certification and exact ideal calculations are performed here; the database's rank-two designation and its global arithmetic provenance are not recertified. No original seed input is used to manufacture this control bound.
