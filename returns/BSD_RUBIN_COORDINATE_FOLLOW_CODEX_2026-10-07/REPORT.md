# Follow-through: the Kato coordinate comparison and actual seed cofactors

2026-10-07. **RUBIN_COMPARISON_CONFIRMED_UNDER_RETAINED_INPUTS; FIXED_SOURCE_COMPARISON_DERIVED_COFINITELY; NO_PRIMITIVITY_BOUND.**

I followed the submitted construction through the published source and then into existing seed arithmetic. The comparison survives this written review. I also derived a cofinite normalization statement and computed the seed's actual logarithm/cofactor residues at 5 and 17. No new Kato coefficient or primary vanishing result was obtained.

## 1. The proposed comparison is usable at its stated grade

The published BKS formula and root factor agree with the submission. The finiteness-free case split works under the retained Kato/control inputs: a nonzero derivative supplies the finiteness needed to apply BKS; a zero derivative forces its quadratic Coleman coefficient to vanish through the rational local-duality lemma.

Thus, for the actual smoothed and transported source,

    H_p (A_p,B_p)^t = epsilon_p K_p (log(P1),log(P2))^t.

This holds without assuming height nondegeneracy and retains the good supersingular domain. It is a written derivation, not formal verification. [Review](COMPARISON_REVIEW.md).

## 2. Normalization need not create infinitely many new exceptions

Fix the modular parametrization, rational projection, nonzero Betti input and smoothing before varying p. The two resulting Betti lattices are commensurable, so they agree after inverting one fixed integer. The nonzero period ratio and smoothing factors also have fixed finite support.

Comparing the actual interpolation formulas then gives, outside that fixed support,

    v_p(K_p)=v_p([U^2]L_std,p).

This is a new written deduction in this return and requires independent review. The exceptional integer has not been computed; this does not certify the old source normalization at any particular prime. It bounds normalization exceptions only, not intrinsic Kato divisibility. [Proof](COFINITE_NORMALIZATION.md).

## 3. The seed at 17 really exhibits the cancellation the formula allows

New exact rational point calculations, combined with the saved canonical-model heights, give:

| p | log(P)/p mod p | adj(H_gamma)log(P)/p mod p | v_p(det H_gamma) |
|---|---|---|---|
| 5 | (0,2) | (1,4) | 0 |
| 17 | (2,13) | (16,6) | 1 |

The saved heights were consumed, not recomputed. Their identification with the BKS height convention remains explicit. With that match, the ordinary root factor has valuation -1, so

    content(delta_5)=v5(K5),
    content(delta_17)=v17(K17)-1.

In particular, a quadratic coefficient divisible by 17 exactly once could give a primitive derivative. Vanishing modulo 17 alone does not reject the route. This is an actual seed calibration of the correlated valuation, not a new primary certificate. The old p=5 symbol residue 2 was reproduced downstream; no second digit at 17 was evaluated. [Calculation and limits](SEED_CALIBRATION.md).

## The remaining seed obligation

In the nonsingular ordinary case the sufficient cofinite target is now

    v_p([U^2]L_std,p)
      + min v_p(adj(H_p)log(P)) - v_p(det H_p) - 1 = 0.

A proof of that equality on a cofinite domain would activate the retained primary-vanishing criterion there. No estimate forcing it has been obtained here. Singular heights retain the one-sided row criterion; supersingular primes retain the root-specific comparison. Neither can be discarded from a full FIN argument.

This continuation closes the proposed comparison at its retained-input review grade and removes a cofinite normalization ambiguity for a fixed source. It does **not** show that the remaining arithmetic estimate follows, or that the source has a fixed nonzero global derivative ancestor.

**FIN, ORDER9 and Q36 remain unchanged.** No large symbol computation, remote job, new agent or external message was launched. Lab publication records the work and does not certify its mathematics.

[Next review and research boundary](HANDOFF.md) · [Sources and actual reading](SOURCES.md) · [Input bindings](INPUT_BINDINGS.json) · [Exact seed controls](checks/SEED_COFACTORS.json).
