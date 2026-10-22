# Correlated divisibility measured on actual rank-two arithmetic

Date: 2026-10-12. Status: **MATCHED_EXTRA_DIVISIBILITY_ON_CONTROLS; TWO_HEIGHT_GEOMETRIES_OBSERVED**.
Grade: same-session computational experiment using PARI/GP 2.17.3, with exact modular-symbol tables and separate rational-arithmetic checks. Not a proof of a new uniform theorem, independent review, novelty claim, or new seed-primary result.

## What was actually done

We scanned 109 good ordinary, non-anomalous curve-prime pairs on five small rank-two curves. Four had an extra factor in their ordinary regulator. Before computing the numerator, the saved selection rule chose the first three by prime then conductor: 655a1 at 7, 433a1 at 13, and 655a1 at 31. We independently computed the quadratic p-adic modular-symbol coefficient for those three, plus two baseline controls. This measures the arithmetic on both sides of the proposed correlated estimate; no Sha value or BSD formula was used to manufacture a numerator.

All three exceptional cases have **one additional factor on both sides, and no additional factor in their quotient**. After retaining the ordinary Euler factor and Tamagawa/torsion factors, the quotients agree with 1 to the precision below.

| Curve | p | v_p(L2) | v_p(det H_U) | Difference | Corrected quotient Q_p |
|---|---:|---:|---:|---:|---|
| 655a1 | 7 | 1 | 1 | 0 | 1 + O(7^4) |
| 433a1 | 13 | 1 | 1 | 0 | 1 + O(13^5) |
| 655a1 | 31 | 1 | 1 | 0 | 1 + O(31) |
| 433a1 | 7 | 0 | 0 | 0 | 1 + O(7^5) |
| 655a1 | 11 | 0 | 0 | 0 | 1 + O(11^5) |

Here L2 and H_U use gamma=1+p, U=gamma-1. The third row is obtained by the exact finite-table route, not from the failed overconvergent computation. No infinite-precision equality is asserted. The fourth exceptional scan row, 664a1 at 59, was outside the preselected first three and its numerator was not computed.

## A distinction relevant to the seed

The same determinant valuation conceals two different configurations. Write ell=(log(P1)/p,log(P2)/p), and reduce H/p and ell modulo p. In every row below ell is primitive, so the local point index w is zero. Put n=(ell_2,-ell_1)^t. The row Hn/p tests whether the height's radical is the local-logarithm kernel.

| Curve, p | ell mod p | H/p mod p | (H/p)n mod p | Additional content of this row |
|---|---|---|---|---:|
| 655a1, 7 | (0,5) | [[0,0],[0,3]] | (0,0) | 1 |
| 433a1, 13 | (6,0) | [[3,5],[5,4]] | (9,2) | 0 |
| 655a1, 31 | (29,13) | [[1,4],[4,16]] | (21,22) | 0 |
| seed, 17 | (2,13) | [[13,5],[5,15]] | (6,1) | 0 |

All four reduced height matrices have rank one. At 655a1/7 the two lines agree. At the other three they differ. This incidence distinction is invariant under an invertible change of point basis and unit scaling of the height. It is not an artifact of a particular displayed matrix.

The seed's known exceptional regulator at 17 belongs to the **distinct-line case**, as do 433a1/13 and 655a1/31. Those are now actual computed controls with the same type of height degeneracy and a unit coefficient-height quotient. The seed row is a fresh replay of previously recorded height/local-logarithm behavior, not a new seed coefficient.

This gives two useful experimental lessons. A nonunit regulator alone does not signal extra content in the ratio. Moreover, measuring only the determinant loses the relative position of the logarithm kernel and height radical. Future samples can be stratified by this distinction instead of grouping all exceptional regulators together. Both types showed cancellation here, so agreement of the two lines is not necessary for the observed cancellation.

The numerical pairing row is not silently promoted to an authenticated cohomological Bockstein for these controls. That would require the appropriate source/lattice comparison. No Kato derivative coordinates were directly evaluated.

## Normalizations and independently obtained quantities

The controls use the exact equations and point pairs retained from the October 7 experiment:

- 433a1: [1,0,0,0,1], points (0,1), (-1,1).
- 655a1: [0,0,1,-13,18], points (1,2), (3,2).

The five-curve height scan additionally uses 389a1, 664a1, 1615a1. Every selected model is minimal. The retained rank-two/basis assertions are not recertified here.

PARI msfromell supplies the rational plus modular symbol; mspadicmoments and mspadicL compute the second derivative of its measure. Independently, ellpadicregulator computes the ordinary height determinant from the rational points. The latter is not an input to the former. Both selected curves have one real component, so the documented Omega+ period is the full real Neron period in these computations.

Let J_p=L_p''(0)/2 and R_p=det H_s in the analytic character coordinate s. At a double zero,

    L2 = J_p / log(1+p)^2,
    det H_U = R_p / log(1+p)^2.

Thus their valuation difference is v_p(J_p)-v_p(R_p). The raw valuations are 3 and 3 in the exceptional rows, and 2 and 2 in the baseline controls. Numerically the lower derivatives vanish to the recorded precision; the central modular symbol is exactly zero. The rank-two/double-zero interpretation is retained, not inferred solely from floating zero tests.

For the unit-level comparison we record

    Q_p = J_p / ((1-alpha_p^(-1))^2 R_p) * torsion_order^2 / Tamagawa_product.

The Tamagawa products are 1 and 2 respectively; torsion orders are 1. All these factors, and the ordinary Euler factor, are units at the selected primes. No conjectural identification of Q_p with actual #Sha is used. Agreement with 1 is consistent with the already retained analytic Sha prediction 1 on these controls; it is not a fresh proof of that prediction.

## Exact finite-table extraction

For 655a1/7 we computed all 2,058 rational plus symbols of denominator 7^4=2401. Writing a=omega(a)(1+p)^j and A_n=sum binomial(j,2)[a/p^n]^+, the sums of the zeroth, first and second moments are

    (0, 0, 306411).

The retained single-table formula gives

    L2 = (1-p/alpha_p^2) alpha_p^(-n) A_n mod p^(n-1),
    L2,7 = 4*7 + 2*7^2 mod 7^3.

This agrees with the overconvergent-symbol calculation. These are separate extraction paths sharing PARI's exact underlying modular symbol, not two independent implementations of modular symbols.

For 655a1/31 we computed all 28,830 rational plus symbols of denominator 31^3=29791. Its moments are

    (0, -26908, -18445775),
    L2,31 = 13*31 mod 31^2.

The first raw moment is not identically zero; it is divisible by 31^2. It was retained, not discarded. With R_U=27*31 mod31^2, Euler factor 10 mod31 and Tamagawa product 2, the corrected quotient is 13/(27*10*2)=1 mod31.

The standalone Python checker verifies unit-residue coverage, principal-unit indices, exact fraction sums, Hensel unit-root arithmetic, and both coefficient residues. Replacing gamma by gamma^2 only on the numerator side changes the coefficients by 1/4 modulo the certified modulus, and is detected in both tables. This is a convention countercontrol, not a fabricated arithmetic input.

## Errors, precision and custody

An overconvergent computation at 31 exceeded the 1.5 GB chosen PARI stack ceiling. PARI continued after that error and printed symbolic placeholders, even though the process exited zero and printed DONE. Its output is explicitly **invalid** and excluded. The driver now distinguishes ordinary stack-growth warnings from errors and the GP routine rejects non-p-adic outputs. The failed raw output is preserved under outputs/655a1_p31_n5.*.

The two successful exceptional overconvergent rows were repeated at higher requested precision. At 7, the returned second-derivative precision did not increase; this is reported rather than relabelled as an extra digit. At 13 it increased by one digit and agreed. No value beyond the returned precision was inferred.

The selection rule and its hash were written before numerator computation. This is same-session preregistration, not an external timestamp certificate. The subsequent logarithm/height-line comparison was an adaptive follow-up, explicitly recorded in CHECK_NOTES.md. Hashes certify file identity, not mathematical correctness.

## What this contributes to the seed search

This executes a small part of the previously proposed discovery program: actual numerator, height and local-point data are now joined, including deliberately selected nonunit-regulator cases. It supplies inexpensive control cases for testing a proposed explanation of correlated divisibility, and separates two geometric causes hidden by the determinant valuation.

A proposed mechanism that insists on a unit regulator, a primitive logarithm for each individual basis point, or coincidence of the two lines is too restrictive to explain all these successful control rows. An attempted arithmetic identity should accommodate both configurations and reproduce the displayed coefficients before being used on the seed.

No new identity controlling the quotient uniformly has been discovered. This small sample has no known odd-primary excess control, so it cannot distinguish a universal cancellation claim from one that fails precisely when odd-primary Sha intervenes. The next discriminating experiment would target a higher determinant valuation or a reliably certified odd-primary-excess rank-two control, preserving the same normalization and measuring the same data. A larger undirected prime scan is not claimed to settle the problem.

No seed L2,17 was computed. No new seed prime, FIN, ORDER9 or Q36 result follows. The result is actual experimental evidence and a better specified comparison panel, not a promised route to completion.
