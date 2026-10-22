# Continuation of the uniform seed construction

**CLOSED_LIFT_AND_WEIGHTED_PERIOD_DERIVED; ADMISSIBLE_WITNESS_COMPARISON_NOT_CONSTRUCTED.**

I repaired the previous full-sum cancellation by constructing a closed, noninvariant lift through a full-marking modular cover. The cover has degree divisible by p, but its deck group has no abelian quotient of order p. Consequently cycles lift modulo p without dividing by the cover degree. A commutator recipe makes this lifting argument explicit.

Combining that lift with the already retained prime-level degeneracy matrix gives an actual family of isogeny-map periods with

    zeroth moment = 0,
    first moment = 0,
    second moment = -2 modulo p.

The written construction covers every good seed prime p>=5, including supersingular primes. It is not just a numerical pattern. Its new proof has not received independent review.

This closes the immediate geometric question left by the preceding construction. It has **not** supplied a BSD witness. The chosen closed cycle is not the prescribed Gross/CM packet or the complete discrete-log modular-symbol packet required by the retained descent criteria. The missing comparison has not been constructed, and this report does not present its existence as likely, easy, or established.

The check program passes 744 moment controls across 24 small primes, plus commutator, period-matrix and supersingular controls. Those are formula checks, not seed primary certificates.

No claim of new literature novelty, uniform Sha control, FIN, ORDER9 or Q36 is made. The full argument and its precise endpoint dependency are in PROOF.md.
