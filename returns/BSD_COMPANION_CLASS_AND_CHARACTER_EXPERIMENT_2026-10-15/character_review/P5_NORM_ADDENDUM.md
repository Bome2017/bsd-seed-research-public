# Actual p=5 unit norm bound: independent minimal witness

2026-10-17. This reviews the root's new `p5_norm_upper` experiment. Its conclusion is an upper bound on a complete unit-supported space, not just detection of a listed nonzero class. The remaining class-group qualification is separate.

## The inference is valid and needs less data than the full matrix

The full-image source for 389a1 has ordinary chi-unit dimension three at p=5. Let U denote that entire mod-fifth-power character space. The actual incidence norm gives a linear map u from U into the inverse-character unit space of the companion field.

An actual global unit beta whose norm is not a fifth power proves `rank u >= 1`. Rank-nullity therefore gives

    dim ker(u:U -> U_B^(chi^-1)) <= 2.

This conclusion does not require a fundamental-unit basis, or even three independent unit candidates. Completeness comes from the independently known dimension of the entire space U. Thus the uncertified completeness of the producer's BNF unit system is irrelevant to this particular upper bound, provided the chosen candidate is rigorously authenticated as an actual global unit.

The rank-three source-residue matrix supplies an additional completeness check for the span of the projected candidates. It should not be used to say the actual norm rank equals one: the observed norm-residue rank is a lower bound on the global norm rank. Only an upper bound on its kernel is concluded here.

## Projection convention

For scalar pullback sigma_2 and chi(2)=2, the character projector modulo five is

    (1/4) sum_(j=0)^3 2^(-j) sigma_2^j
      = 4 + 2 sigma_2 + sigma_2^2 + 3 sigma_2^3.

The coefficients `[4,2,1,3]` are correct. Applying the integral exponents to an actual unit gives an actual unit representative of the desired mod-fifth-power character class. This does not require an exact integral representative of the p-adic idempotent.

## Independent arithmetic extraction

`check_minimal_norm_witness.py` uses only `eval_data.json` and `split_primes.json`. It does not read `NORM_UPPER.json`, use its residue logarithms, use the printed ranks, or import the producer's group-law code.

At q=1831 it independently checks primality, all 24 distinct polynomial roots, all 24 curve points, their order five, and the scalar permutation. It completes the square to `Y=2y+1` and uses the elliptic group law in those coordinates. A fresh torsion basis defines the affine line with first coordinate one. The chosen candidate is number nine (zero-based index eight).

The five projected unit values on this line are

    250, 88, 215, 1268, 223 modulo 1831.

Their product is 693. The direct fifth-power-residue test gives

    693^366 = 123 modulo 1831,
    123^5 = 1 modulo 1831,
    123 != 1.

Thus the incidence norm is not a fifth power. No discrete-log addition is needed in this independent extraction. Since q splits the full 5-torsion, an affine line in that vector space is exactly a covector's level-one fiber and supplies a companion-field embedding. This is the actual incidence norm residue, rather than an arbitrary product of point evaluations.

The pending/fresh unit-authentication record must be bound to the exact candidate exported in `eval_data.json`. This reviewer did not replace that authentication by the fact that PARI called the candidates units.

## Whole-source conclusion and its grade

The separately checked primitive divisor norm at 389 is injective on the relevant character modulo five. At 5 the relevant divisor character is zero. Therefore a global admitted class has valuations divisible by five and belongs to the ordinary virtual-unit space.

If the ordinary source class group has no 5-torsion, that virtual-unit space consists of actual units modulo fifth powers. Combining with the unit bound yields

    dim(global admitted source)^chi <= 2.

The source-class absence remains provisional/GRH-dependent in the current arithmetic lane, because the requested certification did not complete. Hence the unconditional result is the unit-space upper bound after exact unit authentication; the full-source upper bound retains the class condition. There is no silent upgrade to a certified Selmer or seed result.

This experiment establishes a stronger actual arithmetic bound than the earlier generic dimension-three estimate. It does not establish a bound across coefficient primes, compute the original seed's p=5 source, or change FIN, ORDER9, or Q36.
