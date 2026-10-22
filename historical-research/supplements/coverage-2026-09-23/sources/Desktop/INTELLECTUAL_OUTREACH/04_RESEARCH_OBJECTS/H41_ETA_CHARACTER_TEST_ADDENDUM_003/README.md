# H41_ETA_CHARACTER_TEST_ADDENDUM_003

The four corrections to Claude's rank-one argument, and the containment test actually run.

**Not Aristotle's job** — there is no Lean statement here, and the programme's rule puts Aristotle after
an ordinary proof. Done locally with the recorded PARI/GP 2.17.4 and exact Python arithmetic.

**The test passes at both available levels, non-vacuously:**

    N = 62   1338 cycles   873 even / 465 odd   1338/1338 agree   0 disagreements
    N = 254  1367 cycles   922 even / 445 odd   1367/1367 agree   0 disagreements

identically across all four curves of the isogeny class at `N = 62`, and stable under a 6× wider sample.
The normalization question the frozen report warned about was settled: `2·xs` is a primitive vector of
PARI's integral lattice and the gcd normalization reproduces it exactly.

**Four corrections recorded:** the divisor-order inference was invalid (`ord(c) ∣ M`, not `=`); the
containment is *equivalent* to the character equality, not weaker; the Jacobian form is a pullback
`T_p = φ*S₀` and contravariance matters; and **factorization cannot hold when `a = 1`**, so uniform
factorization would be strictly stronger than the seed rather than equivalent to it.

    ADDENDUM.md    the corrections, the test, the residual
    computation/   the GP scripts, the cycle data, and compare_characters.py
    receipts/      TEST_OUTPUT.txt
    MANIFEST.sha256  DIGESTS.md

**The H41 seed remains unproved.** The identification is unproved in general, and nothing here touches
`a = 1`.
