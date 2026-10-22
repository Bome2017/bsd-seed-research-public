# Algebraic leading term and convention audit

2026-10-13. Written review under retained arithmetic, not a fresh evaluation of any modular symbol or height.

The primary PDF https://wstein.org/papers/mcom2649-iwasawa-alg.pdf was read as extracted text at printed pp.1774 and1776 (PDF pages17 and19). Browser screenshot attempts failed; no fresh visual-inspection claim is made. The regulator-normalization locator is **section4.4**, not section4.5 as printed in the submitted SOURCES.md. This is a locator correction, not a change to the formula.

Theorem6.1 is the ordinary algebraic result attributed there to Schneider and Perrin-Riou (Jones supplies the multiplicative case). For the characteristic series f of the ordinary Selmer dual, ord_U(f)>=rank E(Q). Equality is equivalent to primary Sha finiteness and nondegeneracy of the specified p-adic height. In that case its leading coefficient has valuation given by the Euler factor, Tamagawa product, primary order and gamma-normalized regulator, divided by squared p-primary torsion. Section4.4 fixes Reg_gamma=Reg_scalar/log_p(chi_cyc(gamma))^r. The source distinguishes this valuation theorem from the exact-unit conjecture in section5.

## Application, without assuming finiteness first

Assume rank2 and an applicable **integral** main-conjecture equality. The two nonzero series f and L_std differ by a Lambda-unit. Thus their U-orders agree and their leading coefficient valuations agree. If the computed quadratic coefficient L2 is nonzero, rank2 excludes lower powers and ord_U(f)=2. The equality case of Theorem6.1 now supplies primary finiteness and height nondegeneracy. Only after that step do we apply its order formula. No complex rank-two BSD assertion is used.

Conversely, already established primary finiteness and a nonzero matched regulator imply order2 by the same algebraic theorem. Integral main conjecture then gives a nonzero L2 and its valuation. This is the direction used at seed17; it cannot be recycled as an independent proof of its input Sha vanishing.

## Actual conventions retained

The numerical producers use the canonical ordinary unit-root height and the standard Neron-period modular symbol. Their U-coordinate is gamma=1+p. For the new combined control the saved script computes the second s-derivative divided by2, then divides both that value and the scalar regulator by log(1+p)^2. The direct `mspadicseries` x^2 digit independently supplies the numerator at the same stated precision. We checked this source logic and saved digits, not the complete implementation of PARI's height or symbol engines.

The displayed point pairs are p-saturated, so their regulator differs from a full rational basis regulator only by a p-unit square. That suffices for valuations, not an exact p-adic unit assertion. Both positive-control curves have connected real loci, eliminating a full-real versus primitive-plus ambiguity. At the seed, any remaining factor2 is a unit for the coefficient primes used. No arbitrary p-homothety of either measure or height is admitted.

The original n8 combined-control coefficient uses the preserved batching patch and its precision checks. Its grade remains retained computation; this theorem audit does not independently certify the patched modular-symbol engine.

## Verdict

LEADING_TERM_APPLICATION_SUPPORTED_UNDER_RETAINED_ARITHMETIC. The source contains the needed equivalence, with no separate primary-finiteness hypothesis concealed in the forward argument. Together with MAIN_CONJECTURE_AUDIT.md it supports the submitted valuation law, the new combined-control application, and the reverse seed17 deduction. It proves neither an exact unit in a corrected quotient nor a uniform bound across primes.
