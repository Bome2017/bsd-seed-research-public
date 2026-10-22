# Magma counterexample story and the seed

Date: October 4, 2026. Status: **INCIDENT_IDENTIFIED; NO_SEED_COUNTEREXAMPLE_EVIDENCE**.

This is a source and retained-evidence check, not a new BSD theorem or a fresh replay of the large seed certificates.

## What actually happened

The supplied video is Álvaro Lozano-Robledo's [The day I almost made $1M with math](https://www.youtube.com/watch?v=i1hiPIQbt0M), published September 3, 2026. I read its exported, automatically generated English transcript and the displayed title, author, and date.

At 0:43–1:27, he describes an LLM treating a reported algebraic value 0 and analytic rank 1 as a contradiction. At [1:53–2:31](https://www.youtube.com/watch?v=i1hiPIQbt0M&t=113s), he explains the error: the algebraic rank result included a false status flag. Its numerical value was only a lower bound. He reports that the actual algebraic rank was one; the computation had not found an infinite-order generator.

The [current official Magma Rank documentation](https://docs.magma-maths.org/ArithmeticGeometry/EllipticCurvesOverQAndNumberFields/mordell-weil.html) independently confirms that Rank returns a lower bound and a Boolean indicating whether equality is established. Thus an output with value 0 and flag false permits rank 1. The account identifies a misinterpretation of the result contract, not a demonstrated Magma rank bug or a rounding discrepancy. I did not reproduce the speaker's particular computation: the transcript supplies no curve equation, software version, or command sequence.

Separately, [Magma's AnalyticRank documentation](https://docs.magma-maths.org/ArithmeticGeometry/EllipticCurvesOverQAndNumberFields/intro-2.html) describes its numerical procedure as heuristic. That is an additional reason to require analytic certification; it is not the stated cause of this incident.

## Comparison with the actual seed evidence

The retained release is research v0.2.6, commit `8414aea58180f3a18bcee7fba23475c8cac90996`. Its [claim index](https://github.com/Bome2017/bsd-seed-research/blob/8414aea58180f3a18bcee7fba23475c8cac90996/claims/CLAIM_INDEX.md) distinguishes R.1–R.7 from the open FIN, ORDER9, and Q36 claims. The following underlying records were read, not merely inferred from those labels:

* The PARI descent log reports `[2, 2, 0]`: the rank lower and upper bounds agree. The corresponding isogenous curve has the same recorded bounds.
* The eclib log records rank 2 and explicitly records that the rank was determined unconditionally. Rank determination and full saturation are distinct; the release records the latter separately.
* The analytic certificate proves L(E,1)=L'(E,1)=0 using the retained arithmetic and theorem inputs, and encloses L''(E,1)/2 in `[35.929604,35.941023]`, which excludes zero. This yields analytic rank exactly two under its stated trust base.

Therefore the retained seed evidence has algebraic rank = analytic rank = 2. This check finds no analogue of the video's rank mismatch. The underlying computations were not rerun in this pass; the binding file identifies the precise records inspected.

## What would constitute a real counterexample signal here

This is an elementary consequence already contained in release R.7, not a newly discovered research mechanism. Under the retained period, regulator, and local-data normalization, full BSD would give

    q_E = 4 * #Sha(E/Q),
    35.99427 < q_E < 36.00573.

Hence full BSD would force

    8.9985675 < #Sha(E/Q) < 9.0014325,

and the only integer in that interval is 9. The included exact-rational check verifies this arithmetic without evaluating an L-function.

Consequently an independently proved nonzero Sha(E/Q)[p] for any prime p >= 5 would contradict full BSD for this seed, provided the retained interval and normalization certificates remain valid. One need not first prove FIN: full BSD itself implies finiteness, so that implication can be used in a proof by contradiction. Such a discrepancy would concern the full conjecture, not exhibit unequal ranks. No such nonzero primary certificate is present in the reviewed current record.

A failed point search, a Selmer upper bound, a zero value from one auxiliary witness, or failure of a one-way Kato/jet criterion does not supply this certificate. The analogous mistake would be promoting failure to certify vanishing into proof of nonvanishing.

## Effect on the project

The video supplies an identified software-interpretation error and a concrete comparison with the seed's retained evidence. It supplies no new arithmetic input for uniform FIN, no reason to change the seed into a counterexample campaign, and no indication that such a counterexample is close. FIN, ORDER9, and Q36 remain open. No fixed-prime campaign or new external mathematical job was launched.

