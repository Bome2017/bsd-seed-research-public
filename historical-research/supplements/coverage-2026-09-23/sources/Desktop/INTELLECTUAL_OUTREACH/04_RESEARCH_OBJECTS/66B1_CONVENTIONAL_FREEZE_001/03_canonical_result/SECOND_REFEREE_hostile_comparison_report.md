# 66b1 hostile comparison audit — evidence package

This package is a new comparison-stage artifact. Neither model's frozen reconstruction has been edited. The full mathematical referee report is in the accompanying conversation response. This package preserves the inputs and makes the additional finite/symbolic checks reproducible; those checks do not constitute a uniform proof or a formal verification.

## Disposition

The specified uniform isogeny Selmer groups, order-two full 2-Selmer group, rank-zero and trivial 2-primary Sha, finite-field iff, rational 2-primary torsion order two, Tamagawa ledger (2,1,1,2), and BSD equality at 2 in the explicitly defined full-real-period convention pass the mathematical audit. No counterexample was found.

The explicit convention is Omega_R = integral over the entire real locus of the absolute minimal Neron differential. Omega_R = 2 Omega_plus. Separately, the displayed descent differential is half the minimal differential. The analytic and arithmetic BSD valuations are both zero.

Banwait–Huang 2.14 case (3) and literal BSTW 10.12 do not apply. BSTW's precise component factor remains uncertified by the inspected passages. Prior-art coverage is unresolved, not a negative novelty finding: BSTW 1.7 explicitly states a stronger result including 66b1. Its inspected supporting route has the issues explained in the report. The separate Banwait–Huang v3 Theorem 2.13 upgrade already recorded by this referee remains a literature-dependent corollary after BSD(2), with that preprint's stated dependencies; it is not a consequence of the elementary descent alone.

## Immutable records

- `frozen_referee/FROZEN_PRE_COMPARISON_RECONSTRUCTION.md` is an unchanged copy of this referee's Stage I. SHA-256: `2a627f6574cf20f2a9f63f42dc8b19c4173985d902fa0762df7c562b105a27a4`.
- `supplied_inputs/` contains byte-identical copies of the two newly attached first-model Markdown files.
- `first_model_receipts/` is the extracted continuation archive, preserved unchanged.
- `AUDIT_VERIFICATION.json` reports all manifest, byte-identity, recount, metadata and symbolic checks.
- `PROOF_CHECKPOINT_BEFORE_COMPUTATION_REVIEW.json` records completion of the proof audit before reviewing the count programs/rows. Numerical metadata and the prior conversation's claims were already visible; it is not a claim of complete metadata blindness.

No amendments to the referee's mathematical freeze were required. Additional calculations and clarifications here are comparison-stage work.

## Provenance qualification

The first-model freeze receipt records 2026-09-10 16:59:12.719650 UTC. The first retained count-program opening is recorded at 16:59:30.666740 UTC. The matching hashes and later retained copies are internally consistent with that order. These self-recorded timestamps do not independently authenticate actual historical access order.

The first model disclosed having seen the withheld README's inventory/sample size (38 family primes below 4000). The original target also supplied q=5 and N_5=4 and proposed the Selmer shape. Consequently, claims of entirely numerical-evidence-free or hypothesis-free preregistration would be inaccurate. The substantive signed-character iff, its proof, period conversion, model derivation and structural Selmer lower-bound analysis are present in the preserved preregistration. Uniform local upper bounds and actual Sha/BSD conclusions are explicitly post-freeze Stage-II derivations, not preregistered results.

## New finite computations

`referee_counts.cpp` independently computes both curve point counts by direct polynomial evaluation and square-residue multiplicities. It does not reuse the retained finite-difference algorithm. It freshly enumerated all 9,589 good odd primes below 100000, including 600 family primes; all counts match, and there are no exceptions to the signed-character iff. The family has 38 primes below 4000.

The verifier separately checks every retained CSV character, trace, valuation and family flag, exact prime coverage, the 25 outer-manifest and 21 inner-manifest entries, both attached/retained Markdown identities, and the referee's unchanged freeze hash. No mismatches occurred.

The first continuation's own 100000-bound work was a verification of retained rows rather than a fresh recount; this package adds the fresh recount. Neither the original checks nor these checks replace the local proof. High-precision numerical period checks in the first receipts are corroboration, not the exact modular-symbol source for the base value.

## Reproduce

Requirements: a C++17 compiler and Python 3 with SymPy.

From this directory:

```sh
g++ -O3 -std=c++17 referee_counts.cpp -o referee_counts
./referee_counts 100000 > referee_counts.csv
python verify_audit.py
```

The new verifier uses paths relative to its own location. Retained first-model scripts contain their original environment-specific absolute paths and have not been modified. Parameterizing those retained paths is the smallest reproducibility repair for running them elsewhere; it is not a mathematical repair.

## Checked identities and convention discrepancies

The halving quartic expands to

    x^4 + 32*x^3 + 416*x^2 + 2048*x + 4096

and factors, for s^2=-2, as

    (x^2+(16+4s)*x+64)*(x^2+(16-4s)*x+64).

Its values at 0, 8 and -8 are 4096, 67584 (=2048*33), and 2048. Its two quadratic discriminants have product 33792 (=32^2*33).

The first-model half-point ordinate (x^2-64)/(4s) is the negative of the referee's s*(x^2-64)/8. This is a harmless negation, not a disagreement.

The first continuation's minimal coordinates (U,V) and the referee's minimal coordinates (x,z) are related integrally by

    x=U-q, z=V+(q+1)/2.

Their minimal discriminant is 528*q^6 and their Neron differentials agree. The alternate equations introduce no additional period factor.

The phi d=3 obstruction has integral residues {3,11} modulo 16 for even z and {12} for odd z. Negative valuation and the U=0 projective chart are handled by the written proof, not by finite residue testing. The dual d=-1 integral obstruction is {2} modulo 3; its other charts likewise require the proof.

The full Selmer kernel is the subgroup generated by 33, of order two, not the entire four-element quotient 2-torsion image.

## Publication boundary

Freeze the conventional theorem for the exact stated prime family. Do not describe the result as an exact rational BSD equality at all primes based on the descent alone, as proof that Sha is trivial, as a perfectly blind or externally time-authenticated preregistration, or as a cleared novelty claim. No mathematical target revision is required.
