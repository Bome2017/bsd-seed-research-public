# Valuation mechanism supported; exact groups for the combined control

2026-10-13. **VALUATION_LAW_SUPPORTED_UNDER_RETAINED_INPUTS; COMBINED_CONTROL_PRIMARY_GROUP_DETERMINED.**

The submitted mechanism passes the primary-source and retained-data checks. I also applied it to the newer d329233 experiment, which was absent from the submitted application. Its actual nonunit regulator and positive excess give

    Sha(F_329233/Q)[5-infinity] ~= (Z/5)^2.

Both isogenous A partners have zero5-primary Sha. These are written theorem applications using the prior computational inputs, not new coefficient calculations or formal certification. [Proof](CONTROL_GROUPS.md)

## Supported mechanism

The integral ordinary main conjecture identifies the characteristic ideal with the standard measure ideal. The algebraic leading-term theorem then gives the corrected valuation as primary Sha length. The applicable theorems are BCS1.1.2(b) for the irreducible controls and ordinary seed, and CGS A/7.1.1 for the two reducible control pairs. Neither imported statement has an algebraic-rank-one restriction. The finiteness step is obtained from order2 before using the group-order formula. [Main-conjecture audit](MAIN_CONJECTURE_AUDIT.md) · [Leading-term audit](LEADING_TERM_AUDIT.md)

| Curve | Prime | v(L2) | v(det H_U) | v(Tamagawa) | Primary group |
| --- | ---: | ---: | ---: | ---: | --- |
| A_43737 | 5 | 1 | 0 | 1 | 0 |
| F_43737 | 5 | 2 | 0 | 0 | (Z/5)^2 |
| A_329233 | 5 | 3, derived | 2 | 1 | 0 |
| F_329233 | 5 | 4, computed | 2 | 0 | (Z/5)^2 |

The A_329233 numerator is inferred from the source-matched isogeny identity. All other displayed numerator valuations were calculated in prior experiments. Exact primary groups do not imply a full-Sha order. The original rank bounds, saturation, patched coefficient engine and height calculations retain their grades.

## What this says for the seed

At17, the bound old Ota certificate and the nonzero matched regulator imply L2,17 nonzero of valuation1. This is a supported reverse deduction, not an independent numerator or a new proof of Sha17 vanishing. The old certificate is explicitly retained at its recorded MODEL_SAME_FAMILY review grade. No leading unit of L2,17/17 is supplied. [Data audit](DATA_AUDIT.md)

On the already matched ordinary nonzero branch, where local factors are units, this added integral equality forces the previous source defect e_p to vanish. This does not cover arbitrarily rescaled Kato sources or supersingular primes. It removes an explanation based on an uncontrolled nonnegative defect on that domain; it does not bound the actual Sha term.

## The experiment remains a discovery process

The numerical contrast now has an established arithmetic explanation. Further tests merely reproducing this valuation law would not discover a new seed bound. The upgraded paired controls can instead test a proposed independent predictor: it must distinguish the zero A groups from the nonzero F groups while accounting for period, point-index and local factors. Its inputs must not include the measured coefficient quotient or the group order used as the answer.

No such predictor is supplied here. A full-image positive-excess control or a distinct-line combined control could test additional proposed hypotheses, but filling a table cell without a falsifiable hypothesis is not itself a reason for another run. No new scan or expensive production job was started in this review.

FIN, ORDER9, Q36 and seed coefficient-prime coverage remain unchanged. This return completes the explanation and group identification for experiments actually performed; it is not a claim that the seed's missing uniform estimate follows.

## Evidence and limits

- Six input manifest entries and all seven published files verify; the supplied checker output is byte-identical.
- Seven historical Git bindings and the newer paired packet's86 manifest entries verify.
- Fresh modular arithmetic confirms the saved digits and the seed17 regulator valuation.
- Theorem statements, integral qualifications, period normalization and ordinary leading-term equivalence were read from primary sources. The normalization subsection in Stein--Wuthrich is4.4, correcting the submitted4.5 locator.
- Separate model agents reviewed the main-conjecture and data interfaces. This is same-team review, not human review or kernel verification.
- No original descent, modular-symbol or height production was rerun. Source-supplied precision and normalizations remain explicit arithmetic inputs.
