# Integral BD return: what survives and what needs repair

October 7, 2026. **CONDITIONAL_TENSOR_RECIPE_SUPPORTED; HOWARD_VALUATION_CORRECTED; ARITHMETIC_REALIZATION_OPEN.**

There is a construction worth retaining here: a tensor-valued quotient that cancels the arbitrary choice of an isomorphism between the level-raised Galois representation and E[m]. Its algebra is coherent. The supplied return does not yet establish every geometric map needed to instantiate it for the proposed seed setting, so its headline claim of a fully defined canonical arithmetic scalar is too strong.

I read the original report and detailed D1–D5, checked the named BD and Howard source statements, and made the following repairs in [MATHEMATICAL_REVIEW.md](MATHEMATICAL_REVIEW.md).

- **Cancellation:** the Hom-line formulation really removes the auxiliary representation isomorphism, conditional on the geometric comparison and CM-divisor map. It does not automatically fix every orientation across raised levels.
- **Integral quotient:** the claimed inference from a torsion coinvariant group to a rank-one localized Hecke algebra is not justified. A fixed rational Hecke idempotent gives a finite-support replacement for the fixed base quotient. Its exceptional integer is uncomputed.
- **Detecting pairs:** ell=283 is admissible at 5 and 7 with negative sign, but both rational-point classes there vanish. Correct positive-sign denominator controls include (73,223) at 5 and (47,271) at 11, with determinants 4 and 6 respectively. The additional control at 7 is outside BD's coprime-discriminant hypotheses for this K. These computations evaluate no Gross numerator or scalar C.
- **Selmer comparison:** under the specified self-dual local conditions and an invertible two-point localization matrix, replacing the two finite local lines leaves exactly Sha(E/K)[p^k]. The written proof uses reciprocity and subtracts the unique matching point combination. It does not assume Sha vanishing.
- **Howard correction:** rigidity gives a common defect plus the modified Selmer contribution, not the common defect alone. The detailed supplied argument had assumed Sha=0 before dropping that contribution; the summary must retain that assumption.

Consequently this proposed scalar, once its actual geometric construction and Euler-system hypotheses are established, would detect the right BSD obstruction. A cofinite nonzero value would give cofinite primary vanishing. No such value or nonvanishing law is supplied by this return, and no comparison with the actual Kato derivative's excess content has been proved.

The next justified mathematical step on this separate branch is the missing exact bottom-layer geometric construction and CM/localization compatibility, followed by a correctly normalized evaluation. The proposed literature survey or unnormalized small-curve probe is not a substitute for that step. No task card or research job was started.

The old 16-case matrix control reproduces exactly. The new local-point controls pass with exact finite-field arithmetic. The tensor and Selmer deductions are written and conditional, not Lean-checked or a novelty claim. All original files remain unchanged and the supplied report/derivation are included byte-for-byte for comparison.

**FIN, ORDER9 and Q36 are unchanged.** This is an audit with scoped repairs, not a new uniform bound.
