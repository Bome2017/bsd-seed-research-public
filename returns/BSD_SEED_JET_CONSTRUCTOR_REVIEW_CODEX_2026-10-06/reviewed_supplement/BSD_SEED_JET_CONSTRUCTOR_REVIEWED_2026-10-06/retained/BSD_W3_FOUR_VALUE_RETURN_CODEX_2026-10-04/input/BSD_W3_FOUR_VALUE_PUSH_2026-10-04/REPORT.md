# W3: an arithmetic symmetry and a four-value continuation

**Status: W3_FUNCTIONAL_EQUATION_FOUR_VALUE_REDUCTION.**

Under the retained source/Hida/index inputs, I derived a source-matched functional equation and used it to reduce the genuine finite Kato jet from seven coefficients to four. Four critical values on two weight fibres (weights 5 and 6) now detect the same fourth-order jet for which the input used ten values on weights 12--15.

I have NOT evaluated those four arithmetic values or proved their uniform nonvanishing. The result is a reduction of the finite arithmetic extraction problem, not a new primary vanishing theorem or a claim that full BSD can now be assembled. Independent review of this derivation and the retained unreviewed inputs remains necessary.

## New arithmetic constraint

For the actual source-compatible optimized Kato coordinate F, define

    iota(T)=T, 1+iota(S)=(1+T)/(1+S),
    ell_N=log_p(<N>)/log_p(1+p).

The ordinary-family functional equation, matched to the source's Tate-shifted cyclotomic coordinate, gives

    F=(1+T)^(ell_N/2)(1+S)^(-ell_N) iota(F).

The root-number sign is +1 for the critical character through this seed. The comparison is derived from Howard's functional equation and checked against Ochiai's interpolation on a dense set with trivial finite characters. It does not assume any L-value is a unit and does not assume an unproved complex-to-Kato period comparison.

The explicitly integral unit normalization

    zeta=(1+S)/(1+T)^(1/2), H=zeta^(ell_N/2) F,
    Y=(zeta-zeta^(-1))/2

makes H invariant under Y -> -Y. Multiplying the whole arithmetic family by that unit preserves its Euler-system relations and all specialized local indices. Together with the input's global double zero, this gives

    H=A T^2+B Y^2+C T^3+D T Y^2 mod (p,T,Y)^4.

A,B are needed modulo p^2 and C,D modulo p. In the original seven-coefficient notation this also gives the explicit relations b=-c, g=-(1+ell_N/2)c, e+f=(1+ell_N/2)c-(ell_N/2)a.

## Smaller arithmetic certificate, same seed consequence

Use (w,s)=(3,2),(3,3),(4,3),(4,4), with t_n=(1+p)^n-1. The corresponding modular representations are the critical noncentral twists of forms of weights 5 and 6 listed in DERIVATION.md. The retained index argument is extended to these four points there, including residual local conditions and specialization Tor cancellation.

The actual evaluation matrix has determinant 864 modulo p, a unit on the retained p>=17 domain. Consequently

    F not in (p,T,S)^4
      <=> at least one of these four F(t_w,t_s) is nonzero modulo p^4
      ==> Sha(E/Q)[p^infinity]=0.

This preserves the p-adic index-three cases. A second p-adic digit of a quadratic coefficient is not discarded.

The two lower weight fibres suffice as a compatible finite source. No claim is made that ordinary cohomology at this seed's huge level is now cheap to compute. No claim is made that a finite set of coefficient primes settles the cofinite assertion.

## Actual next direction

Work on the images of the two genuine optimized Kato systems at weights 5 and 6 under the four specified critical local quotient maps, at precision p^4. The exact finite-ring extractor is implemented in four_value.py. ARITHMETIC_CONTINUATION.md states the inputs it requires, the permitted per-point unit freedom, and the arithmetic success condition.

The next task is not more interpolation or another proof that arbitrary series can vanish: it is extracting or bounding the actual four source values. Separate primitive integral local generators are sufficient for testing nonvanishing; a common source frame is needed only to reconstruct the four coefficients. A power of p hidden in a comparison is still forbidden.

No fixed cross-prime ancestor is required. No new comparison to C_p is assumed. Uniform nonvanishing of the four arithmetic values remains unproved.

## Checks and scope

* Main standalone checker: exact rational determinant/inverse, 4,200 synthetic finite-ring reconstructions over 35 primes, 140 index-three basis cases, 35 deliberately incompatible-precision inputs rejected, and all four critical ranges.
* Separate symbolic checker: exact rational identities in free variables for the functional-equation constraints, the invariant coordinate, and the four coefficient formulas.
* These are formula checks, NOT computations of seed Kato classes or independent verification of Hida theory, the optimized source theorem, or the global low-jet theorem.
* The seven main proof/source files from the a87b1af return were read through GitHub. Its advertised 32-entry ZIP manifest was NOT replayed here; a binary retrieval attempt failed. No large source corpus or historical canonical theorem was re-certified.
* Howard's source was read in parsed PDF text and Ochiai in the arXiv mathematical HTML; Howard PDF screenshot requests returned cache errors. No visual-source check is claimed.

The source references and immutable input blob identifiers are in SOURCES.json. The canonical research release was not changed. FIN, ORDER9 and Q36 are unchanged.
