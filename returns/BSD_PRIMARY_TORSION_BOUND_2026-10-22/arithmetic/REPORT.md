# Direct p-torsion method: actual split-prime test, no small class bound

Executed 20 October; resumed and corrected against additional sources on 22 October 2026.

**ACTUAL_PRIMARY_TORSION_METHOD_TESTED — NO_NEW_SMALL_CLASS_BOUND.**

This calculation addresses a different mechanism from the exhausted principal-relation families. The relative Ellenberg–Venkatesh method bounds the torsion subgroup of the complete relative class group, using primes split in the quadratic extension A/K. It does not treat selected prime ideals as class generators. The relevant faithful five-class sectors lie in this relative group, so a sufficiently small resulting torsion bound would apply to the class term we need.

I read the 21 October `BSD_FIN_SOURCE_EXPERIMENTS` report and analytic obstruction proof before resuming. Their Cayley-family and whole-class-expression exclusions remain retained. No Cayley search, old ideal-row family, BNF, or whole-class-bound tuning was rerun here.

## Actual seed arithmetic

The retained maximal-order fields have [A:Q]=24, [K:Q]=12, with A/K quadratic and tau the scalar-minus-one involution. Their relative discriminant norm is

    delta = 707033045140895852346320.

The prime supply was computed directly in the maximal orders, retaining exact prime ideals and the scalar action. There are three source versions to distinguish:

| Source formula | Strict maximum integer norm at this seed | Split pairs | Faithful divisor-support dimensions |
|---|---:|---:|---:|
| Published 2025 relative lemma, read literally with its displayed absolute degree | 1 | 0 | 0 in each character |
| Author preprint relative lemma, with relative degree two | 15 | 2 | 1 in each character |
| Original EV relative norm window for its absolute-class torsion estimate | 242 | 26 | 13 in each character |

The two pairs in the intended relative window both have norm seven. They are two primes of K split in A, lying over the same rational prime. The larger window uses rational primes

    7,29,31,53,67,73,113,137,149,151,181,223,229,

with two conjugate pairs over each. All accepted pairs are absolutely unramified and of degree one. The full small-prime scan contains no other eligible split pairs.

**The last column is a dimension of prime-ideal support, not a class-group rank.** Neither this count nor the splitting test proves that any of these ideal classes is nonzero or independent. In particular it cannot be subtracted as relation rank from the prior ceiling 97.

## Source correction is substantive

The published 2025 Lemma 2.1 prints `d=[L:Q]`; the preserved author preprint prints `d=[L:K]`. Their proof passages and applications use relative degree. The initial admission test read the published display literally; the author version was then checked and the larger relative range was tested. The zero-pair result for the literal display is not used as an exclusion of the intended relative theorem.

For the author version, theta<1/(4 ell(d-1)), giving delta^(1/20) at ell=5,d=2. The exact integer checks are 15^20<delta<16^20. For original EV's quadratic norm range, 242^10<delta<243^10. There is a theta strictly below the limiting exponent that includes every listed norm; no equality endpoint was used.

Both estimates contain field-degree-dependent implied constants. The original EV range concerns an absolute-class estimate with the absolute discriminant; it must not be combined with the better relative numerator without a new proof. No unreported choice of implied constant is used to manufacture a numeric upper bound.

## Independent checks and scope

Three computations agree:

1. A-prime decomposition and exact tau action on ideal HNF matrices.
2. Independently, K-prime decomposition and quadratic-residue tests for the defining radicand f(x(T)) in the finite residue fields.
3. Integer point counts on the seed modulo the thirteen rational primes. Each reduction group has exactly one factor of five, producing four nonzero rational five-torsion points and two negation pairs.

The second method also checks the absence of higher-residue-degree pairs throughout the selected norm range. A fresh-directory replay reproduces all saved exact output bytes; the point-count implementation is separate Python integer arithmetic. The maximal-order field constructions and their identification with the seed are retained inputs, not newly proved in this run.

`RESULT.json`, `REPLAY_RESULT.json`, and `SOURCE_VERSIONS.md` record the exact boundaries. `SCALING_TEST.md` shows what the corrected relative theorem does and does not say across coefficient primes.

## Outcome

This was an actual test of a published mechanism for the **complete relevant primary class contribution**, not a new detector or a relocation of unknown classes. At coefficient five it supplies two primes in the intended relative range, but no authenticated small numerical torsion bound. The degree-dependent analytic numerator and constants remain. The prior complete relative five-primary length ceiling 97 is not improved.

FIN, ORDER9, Q36, and seed-prime coverage are unchanged. The exact prime supply is available if a stronger explicit characterwise packing argument removes the remaining loss; its existence is not evidence that such a stronger argument has been proved.
