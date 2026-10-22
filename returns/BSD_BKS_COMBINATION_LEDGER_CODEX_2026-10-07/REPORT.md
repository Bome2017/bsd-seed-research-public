# BKS source comparison and a finiteness-free weak-order deduction

**Status: WEAK_CYCLOTOMIC_ORDER_DERIVED_WITHOUT_SHA_FINITENESS;
TAME_NORMALIZATION_PINNED; NO_NEW_UNIFORM_BOUND.**
The written deduction requires independent review. Novelty is not asserted.

I completed the requested source-to-seed dependency calculation and pushed
one identifiable step: re-running the weak cyclotomic order argument with
a rank lower bound instead of the rank equality that used primary finiteness.
Under the retained seed inputs and published Kato/cohomology inputs this gives

    z_∞ ∈ (γ−1)H¹_Iw,

for the actual integral smoothed Kato class at every good p≥5 in the retained
irreducible domain, including supersingular p. The proof preserves the
unknown Tate-module contribution to Sha. It constructs an integral first
derivative, which is allowed to be zero.

This repairs a construction dependency. It does not prove the analytic
BKS comparison, the derivative's nonvanishing, or a cofinite Sha bound.
The conditional consequence “nonzero rational first derivative implies
primary finiteness” is written separately; primary finiteness is weaker
than primary vanishing and weaker than full FIN.

The tame normalization is now explicit:

    c_N=(2^5·19·59·487)/(2243·5843),
    [θ]₂=(1/2)c_N C₂ U²,     R_F=4R_(p,ℓ)U².

A finiteness-free tame comparison with a fixed nonzero rational scalar α
would therefore give

    C₂(p,ℓ)=8 bar(α)(a_ℓ−2)R_(p,ℓ).

G2 and Ota would then close the cofinite good-prime vanishing step. For
α=q_E, that is the recorded 8q_E target, still requiring rationality and
the arithmetic comparison. BKS's algebraic formula contains #Sha and
cannot supply this input by substitution.

The [combination ledger](COMBINATION_LEDGER.md) records which local hypotheses
the seed satisfies, which source assumptions remain, and the corrected
Howard/DLRV/leading-term statuses. The [weak-order proof](WEAK_ORDER_PROOF.md)
and [tame calculation](TAME_COMPARISON.md) are the mathematical deliverables.
[HANDOFF.md](HANDOFF.md) specifies the independent review points.

Checks recompute the rational constant and test the conditional scalar
conversion, period/sign controls, and elementary divisibility examples.
They do not evaluate a seed Kato derivative or certify the written proof.
The source/read record distinguishes whole files, selected sections, retained
inputs and unavailable fetches. No all-corpus or exhaustive-novelty claim is made.

FIN, ORDER9 and Q36 are unchanged. No Aristotle job or fixed-prime campaign
was launched. This is a laboratory return, not a research-release promotion.
