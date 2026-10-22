# Independent review of the explicit primary Arakelov packing bound

22 October 2026. Verdict: **WRITTEN_PRIMARY_BOUND_SUPPORTED_UNDER_RETAINED_INPUTS; NUMERICALLY_WEAKER_THAN_THE_RETAINED_BOUND.**

Reviewed `theory/EXPLICIT_PRIMARY_PACKING.md`, `check_primary_packing.py`, `PRIMARY_PACKING_RESULT.json`, and the retained exact analytic input. I separately derived the norm-unit error accounting and archimedean separation inequality, and implemented a different rational numerical checker. This is a same-team desk review and exact arithmetic check, not human certification or proof-assistant formalization. The seed-field construction and the antecedent analytic class-number/Hecke bound remain retained inputs.

## Norm-one ideals and complete class coverage

The map from C^1=I^1/P^1 to C=ker(N:Cl(A)->Cl(K)) is correct. Its cokernel is killed by2 because a class c in C represented by an ideal a with N(a)=(b) has 2c represented by a²/(b), a norm-one ideal. The kernel is

    (U_K ∩ N(A×))/N(U_A).

This kernel is also killed by2: the square of a K-unit is its norm as an A-unit. Neither error has been assumed to have order at most2. Their finite2-primary nature proves that C^1 and C have the same odd-primary groups, hence the five-torsion being bounded includes every unseen relative five-class.

The compact group G in the proof has identity component V/Log(E) and component group C^1. Multiplication by5 is onto the identity torus. Consequently [G:5G]=|C^1/5C^1|=|C[5]|, and the measure identity for5G is legitimate. This is not a selected relation quotient.

## The factor four retains the full norm-unit error

With I=[N(U_A):U_K²] and the retained all-embedding metric calculation,

    V_E = (I/64)(R_A/R_K).

Rank(U_K)=7 and μ(K)={±1}, so |U_K/U_K²|=256. Therefore

    [U_K:N(U_A)] I=256.

The kernel of C^1→C is bounded by [U_K:N(U_A)]. Multiplying this bound by V_E gives precisely the conservative factor4:

    vol(G)=|C^1|V_E ≤4h(R_A/R_K).

This cancels the potentially large2-primary norm-unit error against the unit-index factor. It does not omit it. Treating an error “killed by2” as an error “of order2” would have been invalid; the final proof does not do that.

## Fractional elements and separation

If two balls overlap, alpha has norm1 and principal ideal (b_i/b_j)^5. Its opposite nonzero valuations over the distinct K-prime pairs force alpha∉K. The rank-two O_K-lattice O_K+alpha O_K lies inside the fractional O_A-ideal O_A+alpha O_A. Comparing their relative discriminants gives the denominator-inclusive inequality

    delta ≤N(den alpha)² |N_K((alpha−alpha^−1)²)|.

At a prime where alpha has a negative valuation, O_A+alpha O_A has that negative ideal valuation; its norm is the inverse denominator norm. Thus the displayed denominator factor has the correct direction and exponent. No false integrality premise is used.

For the all-embedding logarithm metric, a split-real pair has coordinates (x,−x), so |x|≤sqrt2 R when the collision vector has norm≤2R. A complex K-place supplies four coordinates (x,x,−x,−x), giving |x|≤R. The two real places of K that become complex have modulus1. Their contributions give exactly

    delta ≤ X^20 2^24 sinh(sqrt2 R)^4 cosh(R)^16.

The sinh factors are essential. The cruder exponential-only inequality does not permit positive separation for the two norm7 pairs. The new proof correctly retains the vanishing of these split-real factors at R=0.

The retained relative-unit minimum exceeds8.55; all submitted radii are below1. Each ball therefore injects into the identity torus. The strict reverse of the discriminant inequality makes balls at distinct centers disjoint. Division of vol(G) by their volume yields the stated complete five-torsion bound.

## Independent exact numerical check

`independent_primary_packing_check.py` uses direct positive rational sinh/cosh Taylor series, not the producer's cosh-of-square identity. It independently checks all13 submitted prefix radii and reproduces every claimed safe integer order ceiling from the submitted radii and retained analytic bounds.

It also gives a separate simpler certificate with fixed radius41/100, pi>3.14159, and the independently recomputed coarse analytic product ceiling42·10^71. Its separation ratio is below0.988760899 and its torsion order ceiling is

    342199112254412245471282911641581284817221147154540004409185937945009605891 <5^107.

Hence the independent checker also obtains five-torsion rank≤106. The producer's slightly sharper radius gives a smaller integer with the same rank ceiling. The saved prime-pair supply was separately checked by maximal-order ideal arithmetic, K-residue-field squares, and rational elliptic point counts in the arithmetic lane.

## Endpoint and optimization limits

The resulting rank ceiling106 is weaker than the retained97 ceiling. It must not replace97, be reported as a smaller class allowance, or be treated as a new FIN result. This direct p-torsion proof differs from bounding the whole class group, but its numerical outcome does not improve the actual seed bound.

Only the thirteen common-radius prefixes and the displayed separation inequality are tested. This does not exclude optimized nonuniform packings, stronger character-specific volume or separation bounds, or independent arithmetic class control. It does not supply a bound across coefficient primes. No claim about the actual class group being large follows from a large upper-bound expression.

FIN, ORDER9, Q36, and seed-prime coverage remain unchanged.
