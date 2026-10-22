# Exact quadratic-twist admission check: 6465c1 at 5

Date: 2026-10-15. Status: **NOT_ADMITTED_NONUNIT_TWIST_FACTORS**.

For E = [0,1,1,-36,20], exact base-level 6465 modular-symbol arithmetic gives

| Fundamental discriminant | Exact sum in the pure imaginary eigencycle convention | Factor in the previous experiment's convention | 5-adic valuation |
|---|---:|---:|---:|
| -83 | 20 | 10 | 1 |
| -107 | 20 | 10 | 1 |

Neither factor is a 5-adic unit. Both proposed fields fail the unit-twist prerequisite in `../../experiment/PREDICTIONS_SEALED.md`. This is an admission failure, not a refutation or confirmation of the proposed scalar law. No Gross outcome was used to choose or normalize these values. The root worker stopped the separate Gross run before it returned a Gross sum.

## Exact calculation and scope

PARI/GP 2.17.3 computed `[M,xminus] = msfromell(E,-1)` at the original level 6465, not at the much larger quadratic-twist levels. For q = 83,107 the producer saved every exact rational value `xminus([infinity,a/q])`, 1 <= a < q. All 188 values are integers. Their quadratic-character-weighted sums are both 20. No `lfun`, decimal-to-rational recognition, `bestappr`, regulator, or Sha order appears in the producer.

The separate GP replay verifies the symbol relations, minus involution, level and weight, Hecke eigenvalues at 2,3,5,7,11, all saved evaluations, and the two sums. The symbol's generator values have denominator 1 and gcd 1. These checks authenticate the computed rational eigensymbol and its evaluations; they are not an independent implementation of PARI's modular-symbol construction.

`recheck.py` independently reconstructs the character sums and odd symmetry from the saved integer rows, checks the character values using Euler's criterion, and counts points by both direct enumeration and quadratic-discriminant enumeration. It does not claim to regenerate the symbol itself. A fresh full producer replay can be run in a temporary directory; the saved producer uses append-style GP `write`, so do not run it repeatedly into existing output files.

## Period and Gauss-sum convention

Use the Neron differential dx/(2y+1). The discriminant is positive, so E(R) has two components. PARI defines its imaginary eigencycle period by

    Omega_minus = -(2/c_infinity) Im(E.omega[2]) = |Im(E.omega[2])|.

Its normalized symbol is the coefficient of i Omega_minus in the complex modular symbol. For the primitive odd quadratic character chi modulo q, finite Fourier summation gives

    sum_a chi(a) F(a/q) = tau(chi) L(E,chi,1),
    tau(chi) = i sqrt(q).

The plus component cancels. Therefore the saved rational sum is exactly the quantity

    s_eigen = sqrt(q) L(E^{-q},1) / Omega_minus

under PARI's documented Neron normalization. The older `proxy/twist_values.gp` instead divides by `2*abs(Im(E.omega[2]))`, irrespective of the number of real components. Here that denominator is twice Omega_minus, so its `s` equals s_eigen/2 = 10. This factor of two changes the numerical constant but cannot change its 5-adic valuation.

The direct finite-Fourier derivation above fixes the Gauss factor explicitly; it does not rely on the abbreviated twisted-value display in the PARI manual, which omits that factor. The defining decomposition of the complex symbol fixes the convention used here.

The normalization theorem in use is PARI's documented `msfromell` normalization for the specified elliptic curve. Exact row arithmetic should not be confused with a formal verification of the software's entire period-normalization implementation. There is no arbitrary rescaling of the symbol in this run. At 5, a least-degree isogeny from an optimal quotient to this curve has prime-to-5 degree: otherwise the dual kernel has a nonzero Galois-stable subgroup of E[5], hence contains all E[5] by irreducibility, and factoring the dual map through [5] contradicts minimality. The semistable optimal Manin-constant theorem supplies unit normalization for the optimal parametrization; conductor 6465 is squarefree. These facts explain why an unspecified power of 5 is not freely available to turn these nonunits into units.

## Source-domain arithmetic

The exact discriminant factorization is

    Delta = 3^5 * 5^2 * 431.

Both fields have class number 3, are inert at 2 and 5, and split at 3 and 431. Their discriminants are prime to 6465. Thus the candidate has N-minus = 1 in the intended all-other-bad-primes-split setting; the residual ramification condition over N-minus is vacuous. At the coefficient prime 5 the curve has nonsplit multiplicative reduction, a_5=-1 and ord_5(Delta)=2, the latter a 5-adic unit. At the auxiliary prime 2, a_2=-2 is congruent to 2+1 modulo5, and 2 is neither +1 nor -1 modulo5.

The full residual-image check can be made elementary. Point counting at 11 gives a_11=-6, so the Frobenius characteristic polynomial has discriminant 2 modulo5, a nonsquare. Hence the representation is irreducible. Multiplicative reduction at 431 with discriminant valuation 1 supplies a nontrivial transvection. An irreducible subgroup containing such a transvection has a conjugate with a different fixed line; their powers generate both elementary unipotent subgroups, hence SL_2(F_5). The cyclotomic determinant is surjective, giving GL_2(F_5). The use of Tate inertia here is a standard arithmetic input, not a claim that point counts alone establish the full image.

The factor 5 in the Tamagawa product comes from split multiplicative reduction at 3. Since both quadratic fields split at 3, this local factor persists in both twists. This is an arithmetic feature consistent with the observed nonunit sums. The two computations do not prove a blanket theorem forcing that valuation for every admissible field.

## Consequence for the experiment

The current sealed comparison asked for a unit twist factor and a nonzero point determinant. The first requirement fails, so its proposed zero-versus-nonzero conclusion is not applicable. It would be a post-hoc change to divide away the newly found factor 5 and call the resulting experiment the original test.

There is a second independent source issue: a primitive eigenfunction in a mod-5 Brandt eigenspace has only algebraic normalization. It has not thereby been proved to equal the geometric Fornea--Gehrmann normalization (25) up to a 5-adic unit. No inference about an actual global scalar is licensed by silently making that comparison. The current exact twisted L-values do not resolve it.

FIN, ORDER9, Q36 and seed-prime coverage are unchanged. The new result is a completed exact arithmetic admission check that stops a misleading scalar-law interpretation before the expensive proxy sum is used.

## Reproduction and primary sources

The producer took about two seconds of GP computation for its symbol construction and sums, growing its stack to about 1 GB. The verifier read the saved 13.7 MB symbol and completed the listed exact checks. Stack-growth messages are retained separately from errors.

From a fresh output directory, run the saved GP source with:

    gp -fq -s 128000000 --default parisizemax=1000000000 /path/to/exact_twists.gp

Then run `verify_symbol.gp` from that same output directory. `recheck.py` is portable and reads its own containing directory.

Primary sources checked: [PARI modular-symbol documentation](https://pari.math.u-bordeaux.fr/dochtml/html-stable/Modular_symbols.html#msfromell), especially the defining complex-symbol and Neron-period conventions; [Cesnavicius, The Manin constant in the semistable case](https://www.imo.universite-paris-saclay.fr/~kestutis.cesnavicius/Manin-semistable.pdf), the optimal semistable Manin-constant theorem. The field and residual-image hypotheses should still be read together with the parent audit's precise Fornea--Gehrmann source map; this note does not promote the exploratory scalar law to their theorem.
