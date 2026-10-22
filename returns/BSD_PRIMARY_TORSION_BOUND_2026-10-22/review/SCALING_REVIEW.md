# Review of the cross-prime limitation of this packing expression

22 October 2026. **SUPPORTED UNDER THE RETAINED METRIC, TYPE-III DISCRIMINANT, AND ANALYTIC INPUTS.**

I compared `theory/SCALING_LIMIT.md` with the October20 `SCALING.md` and the supplied October21 `ANALYTIC_OBSTRUCTION_PROOF.md`. This reviews the proof of the limitation, not merely finite integer tests. The result concerns the specified common-radius packing budget, its lambda-based self-injectivity certificate, and its admitted prime ranges. It is not an exclusion of p-primary methods generally.

## General-p volume constant

The factor 2^((p+3)/4) is correct. In the retained all-embedding metric,

    V_E = I 2^(-(r_A−1)/2) (R_A/R_K),
    r_A=(p²+p−4)/2, r_K=(p²+2p−7)/4.

K has real embeddings, hence its roots of unity are ±1. Thus

    [U_K:U_K²]=2^(r_K+1),
    [U_K:N(U_A)] I =2^(r_K+1).

The same norm-unit kernel from the coefficient-five proof has order at most [U_K:N(U_A)]. Its cancellation against I gives

    vol(G) ≤h_relative (R_A/R_K) 2^[r_K+1−(r_A−1)/2]
           =h_relative (R_A/R_K) 2^((p+3)/4).

The factor is a real metric-volume factor; its fractional exponent when p≡3 mod4 is not a finite-group cardinality assertion. No2-primary error has been dropped.

## Comparison with the old expression

Write v_d=pi^(d/2)/Gamma(d/2+1). The old regulator lower bound is

    R_A/R_K ≥2^(-(p−1)/4) v_d (lambda/2)^d.

Using the same analytic product majorant C_an, its old class expression is therefore exactly

    B_old =2^((p−1)/4) C_an/[v_d(lambda/2)^d].

The new budget is

    B_pack=2^((p+3)/4) C_an/(M v_d R^d).

Under the expressly retained sufficient self-injectivity restriction R≤lambda/2, these expressions give B_pack≥2 B_old/M. This comparison is about the chosen majorants. It is not an inequality between actual class groups, and it need not hold after replacing C_an or the self-injectivity bound by substantially stronger arithmetic information.

## Prime-count and discriminant calculation

For the quadratic extension, a distinct unordered split pair corresponds to one base prime. At most m=[K:Q] base primes lie over a rational prime, so M≤mX is a valid generous upper bound. The proof grants X≤delta^(1/(2p)), wider than the author-relative LOW window.

Before replacing sqrt(Q) by q^d, the October21 calculation gives

    B_old >2^(1+(p−1)/4) sqrt(D_K delta)/4^d.

This follows from its same factorial and lambda estimates: the remaining bracket is greater than1/4 using log(4547)>8, e^(3/2)>2, pi^(3/2)<8, and sqrt(2p/(p+1))>1. Retaining sqrt(D_K delta) is essential when dividing by X.

Since both D_K and delta are at least q^d, q=4547,

    B_old/X >(q^(1−1/(2p))/4)^d >400^d.

The last comparison follows from q^(9/10)>1600, equivalently4547^9>1600^10, and p≥5. Hence B_pack>2·400^d/m>p^4. The final all-p comparison follows from d≥p, m<p² and p≤2^(p−1), not numerical extrapolation.

## Exact scope

The argument shows that this explicit upper-bound expression, even with maximally generous split-prime supply in the stated range, cannot alone certify p-torsion dimension≤3. It says nothing about the true class group being large. It also does not exclude class-map/local cuts on that group, sharper actual lattice minima, a stronger analytic product estimate, nonuniform packing, larger prime ranges with a new separation proof, or a different primary method.

The older scalar-minus-one class sector can contain odd nonfaithful characters for p>5. Bounding the whole relative p-torsion controls the desired faithful sector but does not identify those sectors. No equality of their dimensions is used here.

No missing constant or reversed inequality was found in the stated comparison. FIN, ORDER9 and Q36 are unchanged.
