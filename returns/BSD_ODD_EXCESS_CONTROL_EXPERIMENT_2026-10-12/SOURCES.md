# Sources actually used and evidence grades

- [Miller–Stoll, Explicit isogeny descent on elliptic curves](https://www.mathe2.uni-bayreuth.de/stoll/papers/isogeny-descent.pdf), dated January 23, 2011. Sections 2 and 6 give the isogeny Kummer exact sequences and Cassels' Selmer-ratio formula used in PROOF.md. Section 7 was read while testing the quadratic class-group filter; its generator identification is not needed for our final positive lower bound. The general formula is applied with actual minimal differentials, not an analytic BSD formula. PDF and extracted text were read locally; primary-source download hashes are in sources/LOCAL_SOURCE_BINDINGS.json.
- [PARI elliptic-curve documentation](https://pari.math.u-bordeaux.fr/dochtml/html/Elliptic_curves.html): ellrank's unconditional two-descent bounds, ellisomat, ellsaturation, local reduction, p-adic heights and ellpadicL conventions. The numerical rank upper bound relies on this implementation; it is not a Lean proof.
- [PARI modular-symbol documentation](https://pari.math.u-bordeaux.fr/dochtml/html/Modular_symbols.html): mspadicmoments with fundamental-discriminant twist and mspadicseries. The installed runtime is PARI/GP 2.17.3. The official 2.17.3 source tarball and modsym.c / ellpadic.c were inspected for the actual twisting operation, the denominator handling, and twist Euler factors. No numerator was obtained from ellpadicbsd, an assumed Sha value, or a regulator.
- [Stein's 2008 research account](https://389a.blogspot.com/2008/11/gross-zagier-hilbert-class-polynomials.html): source of the rejected first candidate [1,-1,0,94,9]. Its analytic Sha=9 report is not an independent proof of nontrivial Sha; our local check also found a_3=0.
- [Fisher's order-five covering table](https://www.dpmms.cam.ac.uk/~taf1000/g1data/order5.html): read the description and first conductor range. Its independently described covering examples have ranks zero or one, so none was admitted as a rank-two positive control.

The prior experimental input is the lab return at f6684d7ef3f1deebfb8165a3b8b1359aea12a70d, work/returns/BSD_CORRELATED_VALUATION_EXPERIMENT_2026-10-12/. Its old controls and seed17 geometry remain at their retained grades; their underlying computations were not all repeated here.

## Dependency separation

The positive Sha lower bound uses: rank upper bound, rational point/isogeny checks, mod-5 saturation certificates, minimal local reductions, real differential/period ratio, and Cassels' theorem.

The numerator uses: the conductor-11 Neron-normalized plus symbol, quadratic twisting, the ordinary overconvergent lift and finite-precision coefficient extraction.

The regulator uses: the explicit rational points and ordinary p-adic heights. Neither the Sha lower bound nor the numerator is an input to that height calculation.

Downloaded full primary texts are retained locally and hash-bound; they are not redistributed in the public return. No claim is made of an exhaustive literature novelty search.
