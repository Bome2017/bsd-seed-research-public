# Actual seed relative ideal-relation gate

Use A/Aplus, with A the degree-24 nonzero-five-torsion-point field and
tau=sigma^2. Keep both faithful C4 characters modulo five.

Implement Cohen's relative-content driver with exact ideal arithmetic:
I=(alpha)j(a)J. Strip base-extended ideal content, choose a short multiplier
by LLL, strip again, and retain strictly decreasing primitive ideal norms
or exact collisions. LLL is an auxiliary choice; it is not a claim to have
implemented Cohen's relative-HNF short-element routine in full.

Compute base content as gcd(J,tau(J)), corrected to even valuations at
the genuinely ramified relative primes. Authenticate those primes through
the Aplus embedding. No base ideal is principalized and no BNF routine is
called. Exact ideal equality must authenticate every accepted multiplier.

Start from a bounded set of genuine scalar prime-ideal orbits. Preserve all
residual supports and test relation cycles. A selected presentation or its
rank is not a full class-group bound. Complete generation and five-primary
saturation remain separate obligations even if rows close.

Each arithmetic stage has a process-group wall limit at most five minutes,
with direct log files and incremental exact checkpoints. No publication by
this worker. No known Sha value is an input.
