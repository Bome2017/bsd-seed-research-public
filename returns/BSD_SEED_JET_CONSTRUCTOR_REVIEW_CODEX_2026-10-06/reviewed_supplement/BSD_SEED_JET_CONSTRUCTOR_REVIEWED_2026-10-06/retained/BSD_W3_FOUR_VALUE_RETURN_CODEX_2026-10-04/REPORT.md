# W3 four-value review and actual-symbol extraction

**FOUR_VALUE_REDUCTION_CONFIRMED_CONDITIONALLY; CLASSICAL_SYMBOL_EXTRACTION_DERIVED; UNIFORM_BOUND_OPEN.**

I checked the supplied reduction and derived an explicit arithmetic way to compute its four values. I did not compute a seed value or prove their nonvanishing uniformly.

The new formula replaces a call to localize a global Kato class with finite weighted sums of classical modular-symbol coefficients. On the retained ordinary domain, it uses the two actual Hida specializations of weights 5 and 6 and the cusps a/p, 1<=a<p. There are 2(p-1) polynomial symbol values; only their first four coefficients are required, at precisions p^4,p^3,p^2,p. Every division in the extraction is by a p-unit. The source period ratio is already included in the literal family-symbol specialization; the old eta_p is not set equal to one.

The endpoint connection is exact under the retained inputs:

    one of the extracted, authenticated values nonzero mod p^4
      => the actual optimized Kato local index is at most 3
      => seed Sha[p^infinity]=0.

Proving that condition outside one fixed finite set of ordinary primes would close the ordinary uniform component. It does not settle supersingular primes or exceptional primary finiteness, ORDER9 or Q36.

## What was executed

- The input's 10/10 manifest and both supplied exact checkers replay successfully, byte-for-byte.
- The eight supplied bindings to the prior source return were checked against their pinned Git blobs.
- A new exact calibration constructs Delta's integral modular symbol from Manin relations and its T_2 eigensystem. At p=11, the one-level moment formula reproduces three values obtained independently from a sum over all 13,310 units modulo 11^4.
- The extraction implementation passes 192 independent rational-expansion comparisons and rejects 192 malformed inputs. It explicitly refuses to label unauthenticated arrays as a seed certificate.

The calibration is on Delta, not the seed. These are algorithm and formula checks, not evidence of a new seed primary vanishing result.

## What remains uncomputed

The actual integral symbols of the seed's two weight fibers have not been constructed or supplied. The new formula does not make computing those symbols at tame level 6503188012738584 cheap. It avoids a mandatory high cyclotomic-level realization for these critical values; it does not prove an affordable full evaluator or a uniform estimate.

I tested whether primitive source generation, the functional equation and the unit evaluation matrix already force a nonzero weighted sum. They do not establish that implication: primitivity is a statement about the entire symbol, whereas the test uses four specific functionals. No rank or unit-index assertion for their images was proved. This is a limit of the attempted argument, not a nonexistence theorem for another uniform argument.

The deliverable is the explicit source-matched formula and implementation in [ARITHMETIC_EXTRACTION.md](ARITHMETIC_EXTRACTION.md) and [symbol_values.py](symbol_values.py), with its calibration. It is a further arithmetic extraction result on the proposed route; it is not progress through the uniform nonvanishing theorem. Literature novelty is not claimed. Independent mathematical review of this new derivation remains required.

FIN, ORDER9 and Q36 are unchanged.
