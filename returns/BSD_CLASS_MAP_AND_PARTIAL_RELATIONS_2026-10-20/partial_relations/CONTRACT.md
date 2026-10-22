# Bounded partial-relation cancellation gate

Date: 2026-10-20. This lane uses the fixed degree-48 point field of the rank-two -47 twist of 11a1 at coefficient prime 7, not the original BSD seed.

The saved norm log has 14,326 exact norms and deterministic LLL reconstruction coordinates. Complete vectors were not saved except for twenty previously excluded elements. No claim that all 14,326 vectors were read is permitted. Reconstruct only a selected panel and check every saved norm exactly.

Changed operation: retain candidates with shared rational norm support as selection hints, then use actual prime-ideal divisors to seek cancellation. The prior instrumented PARI collector exported only elements passing its smooth filter and had no retained mixed partial relations. This does not claim the standard partial-relation method is new.

Stage 1 (120 seconds maximum): strip rational primes through 1000 from all saved norms, compute exact batch GCD shared cofactors and overlap groups. Rank candidates by private cofactor bit length, residual cofactor bit length, full norm bit length and original row index. This is a feasibility/selection device only: a private rational factor can have zero anti-divisor, so it is not a mathematical exclusion.

Stage 2 (120 seconds maximum): reconstruct up to 80 candidates, prioritizing shared-support graph components; exact match to saved norms, mixed-parity check and norm-preserving candidate bindings required. Retain explicit vectors.

Stage 3 (120 seconds maximum): factor actual principal ideals for a bounded panel, reconstruct each ideal and tau conjugate exactly, build full anti-divisor matrix including every prime. Compute exact integer kernel and mod-seven rank. A partial prime factorization cannot certify an ordinary unit.

A nonzero divisor-kernel vector is only a candidate. Multiply the actual field elements, require integral element and inverse, reject identity/root-of-unity and seventh powers when authenticated, and compute faithful scalar projection. Only nonzero faithful units proceed to the existing norm/local evaluator. Zero output is a bounded source result, not a complete unit or class bound. No full BNF, new family sweep, or publication is authorized in this worker.

Maximum arithmetic time before a useful signal: 5–8 minutes. Record all incomplete states and don't infer success from GP exit code alone.
