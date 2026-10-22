# The earlier 20806a1 rejection: evidence and limits

The prior project did not overlook this preprint. The master already lists DM Theorem 5 as rejected in
[DO_NOT_RESURRECT.md, row 18](/Users/bsm/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/DO_NOT_RESURRECT.md:24),
following [the Lane 3 counterexample argument](/Users/bsm/BSD_SEED_2243_12_FULL_BSD_LANE3_2026-09-18/C_frontier/C2_STATE_OF_THE_ART_2026.md:79).
That record explicitly says it did not locate the proof error. The present audit supplies that missing diagnosis independently.

## Earlier mathematical argument

For the different curve 20806a1, the record uses:

    a-invariants [1,1,0,−1332753376,−18727754685966],
    N = 2·101·103,   Tamagawa product = 2,
    L(E,1)/Ω = 242,   no rational 11-isogeny,   a₁₁ = 6.

It applies Skinner–Urban Theorem 2(a), whose hypotheses are good ordinary reduction at 11, residual surjectivity, and a multiplicative prime q different from 11 with ramified residual representation. The valuation v₂(Δ)=1 gives ramification at q=2 and a transvection. Irreducibility plus that transvection gives SL₂(F₁₁), and the determinant gives full image. Residual surjectivity lifts 11-adically. The theorem then gives #Sha[11^∞]=121, conditional here on the exact input L(E,1)/Ω=242.

The theorem statement was read in the retained Skinner–Urban introductory text and cross-checked against the [authors' full paper](https://www.math.columbia.edu/~urban/eurp/MC.pdf), Theorem 2 / Theorem 3.6.11. This application is a rank-zero result and does not assume full BSD.

## Fresh checks in this audit

[CREMONA_20806_SOURCE_ROWS.json](/Users/bsm/BSD_CODEX6_DM_TAIL_HOSTILE_AUDIT_2026-09-19/CREMONA_20806_SOURCE_ROWS.json) records rows obtained from the author's ecdata repository at the immutable commit

    25cec5ecfec8b9f016eb1631ac633194c2bed39f.

The data gives conductor 20806, rank zero, trivial torsion, Tamagawa product 2, analytic Sha order 121, a singleton isogeny class, and optimal/Manin flags 1,1. The author's Manin documentation records full modular-symbol computations for levels through 60000.

Exact arithmetic independently checked here gives

    Δ = −2·101⁹·103²,
    #E(F₁₁)=6,   a₁₁=6,
    c₄ = 63972162073,   c₆ = 16180300257459139.

The integral short model with A=−27c₄, B=−54c₆ has 4A³+27B² congruent to 3 modulo 11. Thus the short-model discriminant condition in DM holds. Multiplicative reduction at 2 gives non-CM. The result file explicitly distinguishes these small exact arithmetic checks from a Sha computation.

## Evidence boundary

The retrieved allbsd row contains floating approximations to L(E,1) and Ω and the integer **analytic** Sha entry 121. It does not itself contain an independently replayable exact modular-symbol certificate for the rational value 242. The earlier audit asserts that value is exact; this session has corroborated its database inputs but has **not freshly proved or replayed that exact L-ratio**. The direct LMFDB page was unavailable (404), and no new modular-symbol computation was started.

Accordingly, this counterexample remains a strong, previously recorded theorem-plus-exact-data argument, with the exact L-ratio imported from that record. It is **not needed for the present verdict**, which rests on the explicit trace failure and direct impossibility proofs for Theorem 6 and Proposition 10. An analytic Sha table entry alone is not being promoted to a proved Sha order.

No computation at a proposed exceptional prime of the seed was performed.
