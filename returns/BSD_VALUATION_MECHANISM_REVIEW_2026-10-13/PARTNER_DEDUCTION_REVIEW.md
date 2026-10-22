# Independent review of the two A-partner deductions

Date: 2026-10-13.

**Verdict: PARTNER_PRIMARY_VANISHING_SUPPORTED_UNDER_RETAINED_INPUTS.** The deduction is valid for both d=43737 and d=329233. It uses the retained exact measure/height/isogeny comparisons, 5-saturated point pairs and coefficient digits, together with the integral main-conjecture interface and the ordinary algebraic leading-term theorem. No new coefficient calculation was made.

For each twist write phi:A -> F. Retain

    L_std,F = 5 L_std,A,
    M^t H_U,F M = 5 H_U,A,
    det M = 5,
    C_A = 20, C_F = 4,
    |A(Q)_tors| = |F(Q)_tors| = 1.

Both curves use the same cyclotomic coordinate and ordinary unit-root splitting. The height equation gives 25 det H_U,F = 25 det H_U,A, so the regulator determinants are exactly equal on the named point pairs. The normalized measures belong to different elliptic curves and use their respective Neron periods; division of the displayed measure identity by 5 is therefore legitimate. It is not arbitrary division of a fixed Kato source to manufacture primitivity.

The common Euler factor cancels. Defining Q_C with the same torsion, Euler, Tamagawa and regulator corrections as in the original packet gives

    Q_F / Q_A = 5 * (C_A/C_F) = 25.

This identity remains an identity of the actual matched quotients; it does not say Q_F=25 or Q_A=1 to infinite precision.

## Applying the arithmetic theorems

The previous source audit verifies CGS separately for A as well as F: the residual semisimplification is chi_d plus omega*chi_d, and at 5 both constituents differ from 1 and omega. Neither curve is excluded for being nonoptimal or having algebraic rank two. The 5-saturated pairs are sufficient for valuation formulas; a possible index prime to 5 changes only a unit.

Stein–Wuthrich Theorem 6.1 (printed p.1776), freshly read in the primary PDF, states that the characteristic series has order at least the algebraic rank. Equality of order gives both primary Sha finiteness and nondegeneracy of the ordinary height, and then its leading-term valuation records the regulator, local, torsion and primary Sha factors. Combined with CGS's integral equality, the nonzero quadratic coefficient of A therefore establishes primary finiteness before its order is used.

https://wstein.org/papers/mcom2649-iwasawa-alg.pdf
https://arxiv.org/pdf/2303.04373v2

The input data and deductions are:

| Twist d | v5(L2_F) | v5(L2_A) | v5(det H_U,A) | v5(C_A) | v5(epsilon_5) | primary length of A |
|---|---:|---:|---:|---:|---:|---:|
| 43737 | 2 | 1 | 0 | 1 | 0 | 1-0-1=0 |
| 329233 | 4 | 3 | 2 | 1 | 0 | 3-2-1=0 |

For d=43737, the A-side coefficient was also independently computed in the paired experiment: 4*5+O(5^2). For d=329233, the present A-side value is **derived**, namely 3*5^3+O(5^4), from L2_F=3*5^4+O(5^5) and the exact period comparison. Its nonzero leading digit proves the required nonvanishing. It is not a second independent numerator run.

Consequently, at the stated written-proof/retained-computation grade,

    Sha(A_43737/Q)[5^infinity] = 0,
    Sha(A_329233/Q)[5^infinity] = 0.

Equivalently, after applying the valuation theorem to both curves, their primary lengths differ by exactly two. Thus a supported F-length of two forces A-length zero. The argument above also obtains zero directly from the actual coefficient/regulator valuations without using a presumed Sha(F) order.

## Limits

These conclusions concern only the 5-primary components of these two control curves. They establish no finiteness or order for either full Sha group, no complex BSD identity, no new seed-prime coverage and no uniform-in-p seed bound. They retain the original rank, point-saturation, normalization and finite-precision computation grades. This is an independent check of the deduction and theorem interface, not an independent replay of those computations.
