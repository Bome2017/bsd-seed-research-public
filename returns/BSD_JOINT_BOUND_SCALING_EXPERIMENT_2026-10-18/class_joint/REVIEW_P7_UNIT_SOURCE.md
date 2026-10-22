# Independent check of the coefficient7 simultaneous-divisor source

Verdict: actual global unit construction passes; the tested faithful-character residue ranks remain zero. No ordinary-class upper bound follows.

This is a second-agent exact replay under the retained degree48 field, maximal order and scalar3-automorphism certificates. I did not rerun their construction, BNF or a class computation. The parent generated26 elements, their156 scalar translates and99 integral divisor relations. I freshly factored all156 principal ideals, reconstructed each from its complete factorization, matched every producer orbit descriptor, and rebuilt the entire150-by156 divisor matrix. The rebuilt matrix agrees exactly. See `review_p7_ideals.gp`, output and receipt.

Separately, standard-library Python verifies D K=0 over Z for the156-by99 exponent matrix K. Modular minors at101 prove rank D>=57 and rank K>=99; the zero product forces complementary upper bounds, so the exact rational ranks are57 and99. At7 the ranks are again57 and99. This avoids treating99 compact expressions as99 independent units.

For each integer column k of K, the product of the156 actual elements to exponents k has zero valuation at EVERY finite prime, since the factor list was complete. Hence it and its inverse are integral: it is an ordinary global unit, independently of class completeness or GRH. The faithful projector coefficients (6,2,3,1,5,4) are 6*3^(-j) mod7 for j=0,...,5. Integral products with these exponents remain actual units. Their residues satisfy the expected scalar character if the retained automorphism acts as multiplication by3, as verified in the producer's point-coordinate checks.

An independent multiplicative calculation, using no producer discrete logs or rank output, verifies the projected seventh-power characters at all48 roots for all99 units at each of38711,66977,131671. All14,256 products equal1. Thus the recorded zero residue rank is reproduced. This is finite residue information; it alone does not prove these units globally seventh powers or that their faithful components vanish identically. No lower rank on the actual incidence map is supplied by this test, so the ambient unit upper bound remains4.

## Exact finite-source class conclusion

Let a_1,...,a_156 be these elements and D their complete integral divisor matrix. Every product a^r with divisor divisible by7 has Dr=0 mod7. The independently checked equality

    ker(D mod7) = image(K mod7)

shows that r=Kc+7s for integer c,s. Therefore

    a^r = (a^(Kc)) * (a^s)^7,

with the first factor an actual ordinary unit. Consequently every virtual-unit class obtained from this finite multiplicative family has ZERO image in the ordinary7-class group. There are no extra class-supported virtual-unit directions hidden by replacing this family's integral divisor equations with equations modulo7.

This is a statement about the generated family only. It does not assert that the family contains all virtual units, or that Cl(A)[7]^chi is zero. It therefore cannot turn the current complete-unit bound into a whole-source bound. It does identify precisely what this changed experiment supplied: genuine compact units, without an additional class source.

The p5 class certificate remains conditional as documented in `CLASS_SOURCE_AUDIT.md`. All unknown ordinary class directions must remain in a larger-prime whole-source bound. FIN, ORDER9 and Q36 unchanged.
