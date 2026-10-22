# Sealed seed-3 global-source intervention

The intervention holds E, coefficient 3, the number field, actual point/cubic representatives and every local condition fixed. It removes one allowed valuation-support block at a time; then studies the unramified unit/class-group filtration. No new Selmer group is solved.

Inputs: certified final P1,P2,C1,C2 from verify_certificate.gp; cached search-side 15-generator L(S,3), saved four-dimensional search kernel, and cached GRH BNF. The final cubics are recomputed from their coefficients, not identified with the earlier seed_ctx chosen vectors.

Predictions sealed before evaluating:
1. CLASS_SEPARATED: the valuation kernel contains the whole four-dimensional span, and its ideal-cube-root map to Cl(L)[3], modulo the image of the rational-point plane, has rank two. This supports the proposed class-group explanation for this actual seed excess.
2. PARTIAL_CLASS: the induced class-group image modulo rational points has rank one; a remaining direction requires units or ramification.
3. UNIT_OR_SHARED: the image quotient has rank zero. This rejects class-group separation; excess lies in a unit-type kernel or shares the point image.
4. RAMIFIED_OR_MIXED: at least one class has a nonzero valuation modulo3. First report which prime blocks survive and the complete valuation-kernel matrix. The class-group map is defined only on that kernel, never on all four by assertion.
5. COST_OR_CUSTODY_STOP: 300 CPU seconds, maximum PARI stack4GB, no bnfinit/bnfcertify, no expansion of K.fu, no new Selmer solve; preserve partial results.

Required outputs: exact representatives/norms, valuations and prime ideals, prime-by-prime rank drops, ideal cube identities, cached class coordinates and their order checks. Do not assume expected Sha order, analytic values or height values. Correctly separate exact ideal arithmetic from GRH-dependent completeness/nontriviality of the cached class-group coordinates. This experiment need not yield a bound; its possible payoff is to identify a specific unit/class-group component that any independent source-rank theorem would have to control.

Historical collision: the old run already found local-only dimension7 versus global norm/additivity dimension4, and already made relaxed-good-prime controls. Neither is being repeated as a new discovery. p=3 is a bad coefficient prime for this seed; no extrapolation to good p>=5, full-image ordinary Kato hypotheses or uniformity is allowed.
