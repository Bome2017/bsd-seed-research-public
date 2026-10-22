# Exact resolution of the returned C13 discrepancy

The returned residues 7 and 8 can both be reproduced exactly from the supplied output, but neither is C13 in the retained omega1 convention. They combine two separate scaling issues. The correct coefficient is **2 modulo13**, or **1** in the full-real-period convention.

## 1. The unit-root factor

The unit root of X²+4X+13 is alpha=9 modulo13 (126 modulo169), so alpha^-2=9 modulo13. With j(b)=-(b^12-1)/13 modulo13, the unfurled depth-two coefficient has weight

    9 * binomial(j(b),2).

Conjugation identifies S_b=S_(169-b) and j(b)=j(169-b), so the folded weight is

    2 * 9 * binomial(j(b),2) modulo13.

Using only 2*binomial(j(b),2) omits the unit-root factor. The ratio to the correct weights is 9^-1=3 modulo13. This explains the returned uniform factor of three; the factor two from folding is already present on both sides.

## 2. Lattice numerators versus symbol values

The raw Arb output identifies a symbol as Z_b/1024. The exact SYMBOLS_m169.txt file already performs that division. Summing the integer candidates Z_b instead of the symbols multiplies the result by 1024=10 modulo13. Its inverse is 4.

The predeclared groups, evaluated on the exact symbol file, give:

| Weight | Sum of symbols |
|---|---:|
| 1 | 163 |
| 2 | -138 |
| 4 | 272 |
| 5 | -52 |
| 10 | -230 |
| 11 | -215 |

Thus the weighted sum is

    163 + 2*(-138) + 4*272 + 5*(-52) + 10*(-230) + 11*(-215)
    = -3950 = 2 modulo13.

Using Z_b instead reproduces the reported gate residue 1024*(-3950)=7 modulo13. Omitting alpha^-2 as well reproduces the reported alternative residue 8. The corrections are

    7 * 1024^-1 = 7 * 4 = 2 modulo13,
    8 * 1024^-1 * alpha^-2 = 8 * 4 * 9 = 2 modulo13.

These identities completely explain the supplied residue discrepancy without changing the predeclared formula. The lattice inverse 1024^-1=4 and the interpolation factor (1-alpha^-1)^2=4 happen to be equal in F13; they are different factors with different roles.

## 3. Independent finite-measure check

downstream.py also constructs the Hensel unit root and Teichmuller representatives modulo13^20, and evaluates the full depth-two measure, keeping the lower-level correction. Its first three coefficients modulo13 are (0,0,2). The lower-level quadratic contribution is zero modulo13. Only the quadratic coefficient modulo13 is promoted to a certified digit of the infinite series through the retained convergence theorem.

The same implementation reproduces the retained coefficients at 7 and 11. The full-real-period convention divides the omega1 coefficient by two, giving 1 modulo13. None of these exact calculations reruns the large Fourier sum; they use the certified rational symbols. The separate completion review checks their numerical and byte provenance.

The original external RESULT.json and incident report remain unchanged as historical evidence. This note supersedes the claims that 7 or 8 is the retained normalized C13 value and that the discrepancy remains unresolved; it preserves the nonvanishing conclusion. COMPLETION_REVIEW.json now records passed custody and interval-recombination certification; audits/P13_PRIMARY_THEOREM.md supplies the qualified arithmetic consequence.
