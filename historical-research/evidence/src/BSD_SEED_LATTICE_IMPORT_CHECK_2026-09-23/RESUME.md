# RESUME: source check of the symbol-lattice imports (claim A.4), 2026-09-23

User choice (2026-09-23): check the symbol-lattice imports, working from the reviewed v0.1.1 archive. Nothing is uploaded or sent. No downloads without permission. The v0.1.1 package is not modified; this folder is additive.

Target, claim A.4 as corrected by the first review:
* c0 = 2^a with a <= 8, and 4547 does not divide c0, for the optimal curve;
* c_E | 2^9 for the seed parametrization;
* hence [r]^+- lies in (1/1024)Z at the rational unitary cusps r = a/d (gcd(d,N) an exact divisor of N).

Steps:
* L1 the rational-cusp lattice argument;
* L2 odd primes dividing c0 (Mazur / ARS Cor. 3.7);
* L3 4547 does not divide c0 (Edixhoven);
* L4 the 2-adic bound a <= 8 (derived lemma);
* L5 c_E versus c0 across the 2-isogeny;
* L6 which cusps the certificates use.

Output: REPORT.md, with a per-step verdict, source lines, and the reading grade (at source / via a recorded verbatim quote / via restatement / not read).

## STATUS 2026-09-23: DONE
Verdict: SUPPORTED, with no gap found. See REPORT.md. Every cited CNS and ARS statement was confirmed at its line. Steps A and B were re-derived. The 4547 hypotheses were verified exactly for both curves of the class, and every certificate denominator is a rational unitary cusp. The proposed A.4 wording update was not applied. The v0.1.1 package is unmodified; nothing was downloaded or sent.
