# Independent review of the unit/class filtration

Scope: exact algebra in `../FILTRATION.md`, under its stated independent four source classes, independent point plane, and faithful descent-field representation. This review does not recertify the covering maps, full Sha upper bound or conditional class-group computation.

**Verdict: the two exact sequences and the three nonnegative dimensions are correct.** They define a filtration of the two-dimensional quotient, not a canonical decomposition.

For a linear valuation map v:A→D and a subspace W⊂A, the induced map A/W→v(A)/v(W) is well defined and onto. Its kernel consists of cosets with v(a)=v(w) for some w∈W; replacing a by a−w gives a representative in A0=ker(v). The kernel of A0→A/W is exactly W0=A0∩W. Thus the first short exact sequence is correct without assuming that either point image is unramified.

On the full kernel of all finite-ideal valuations modulo3, (a)=I³ has a unique fractional-ideal cube root. If a changes by b³, I changes by (b), so [I] is independent of the representative. Since I³ is principal, [I] lies in Cl(K)[3]. The class map is a homomorphism. Its kernel is represented by a global unit, because I=(b) implies a/b³ has trivial fractional ideal. Conversely units have trivial class. The natural unit map O_K*/O_K*³→K*/K*³ is injective: a cube root in K of a unit has zero valuation everywhere and is itself a unit.

Apply the first linear argument a second time to c:A0→Cl(K)[3] and W0. Its kernel in A0/W0 is (U+W0)/W0≅U/(U∩W0). Since U⊂A0, U∩W0=U∩W. This proves the second sequence. Dimension additivity then gives

    [dim v(A)−dim v(W)] + [dim U−dim(U∩W)]
      + [dim c(A0)−dim c(W0)] = dim(A/W)=2.

## Arithmetic qualifications needed in execution

1. The valuation matrix must include every prime ideal in the support of the four principal fractional ideals, including denominators and primes outside a preselected bad-prime set. No other prime can acquire nonzero valuation in their products modulo cubes, so completeness for the four generators suffices.
2. The class matrix is defined only on a basis of the full valuation kernel. It must use ideal cube roots, not arbitrary ideal classes attached separately to ramified representatives.
3. With class invariants [12,6,2], a3-torsion coordinate is a multiple of4 in Z/12 and a multiple of2 in Z/6; the Z/2 coordinate is zero. Its F3 coordinates are therefore c1/4 and c2/2. Naively reducing the original cyclic coordinates modulo3 gives an incorrect map in general. The independent verifier checks this conversion explicitly.
4. Changing a cubic representative by a point image can change its visible valuations or ideal class. Only the quotients by v(W) and c(W0) are invariant. The numerical test must preserve these denominator subspaces rather than inspect individual representative rows.
5. Retaining only some valuation rows gives the first exact sequence for that smaller map. Its kernel generally contains S-unit classes, not just elements with principal ideal an ideal cube. The global-unit/class second step cannot simply be reused on this larger kernel. Any ramification-prime intervention must retain this distinction.
6. If the bnf class group is only certified under GRH, a complete class/unit dimension decomposition derived from it retains that condition. Exact valuations and exact witnessed cube/principal relations can be stated separately. No part of this review promotes a conditional upper bound to unconditional.

## Independent checker

`verify_filtration.py` uses only Python's standard library and exact arithmetic over F3. Input matrices use four ambient columns P1,P2,C1,C2. The kernel basis is supplied as a list of vectors; the program verifies it is exactly ker(V). It constructs W0, c(W0), U and U∩W, checks both dimension equalities and refuses inconsistent cyclic coordinates.

The self-test enumerates all212 subspaces of F3^4, every nested U⊂A0 (2193 flags), and all81 additions of arbitrary point vectors to the two excess representatives for each flag. It verifies that the three quotient dimensions are unchanged. This is an algebra/control test, not a seed arithmetic computation. Its output is `CONTROLS.json`.
