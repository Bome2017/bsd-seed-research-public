# Implementation corrections and acceptance

An initial deeply nested GP residue loop contained a surplus closing parenthesis. Its stderr and partial stdout remain under each case's failed_parse/. No kernel result from that invocation was accepted.

After correcting the parser, an initial residue-loop implementation returned zero eligible evaluations. Exact root tests still reported the noncube scalar directions as unresolved, so it could not falsely certify completeness. The loop was rewritten with explicit statement structure, and rational polynomial coefficient denominators are screened with denominator(content(lift(NV[j]))), rather than denominator(lift(NV[j])). The corrected computation produces simple noncube places and literal roots certifying complementary subspaces. The interim unresolved-output files were overwritten and are not presented as retained results.

The final independent checker verifies every selected residue place is simple, every evaluated norm is integral and nonzero there, and every residue generator is primitive. It recomputes norms by multiplication-matrix determinants and checks root identities exactly. The fresh-directory replay rejects nonempty stderr, requires its completion sentinel, compares arithmetic artifacts byte-for-byte, and independently enumerates the finite scalar kernels.

The producer's scan limit q≤2000 is only a bound on its search for negative certificates. Completeness follows from the successful exact positive cube-root certificates plus the exhibited independent negative rows, not from scanning all primes below that limit.
