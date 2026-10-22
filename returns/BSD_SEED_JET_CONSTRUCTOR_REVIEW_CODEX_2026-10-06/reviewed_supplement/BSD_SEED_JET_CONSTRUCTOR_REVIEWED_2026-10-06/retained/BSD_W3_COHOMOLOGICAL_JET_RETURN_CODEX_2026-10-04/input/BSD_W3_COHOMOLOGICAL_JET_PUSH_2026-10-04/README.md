# W3 integral cohomological-jet continuation

**Result:** written local-family freeness/base-change lemma, a rank-one Coleman error-removal corollary, and a precise period-free mod-p^4 certificate for an authentic Kato class. Independent review pending.

**Direction:** construct the genuine integral Kato zeta-map image modulo (p,T,S)^4; evaluate its local quotient at T=S=p. This avoids making a unit comparison of two complex/de Rham period conventions, or a fixed cross-prime ancestor, compulsory before attempting nonvanishing.

**Not obtained:** the actual global Kato jet, eta_p's valuation, a new seed primary certificate, a uniform bound, FIN, ORDER9 or Q36. The latest cofinite-Hida theorem is used at its producer's written grade, not independently certified by this return.

Files:

- PROOF.md: objects, local-control derivation, source application, exact finite certificate and limits.
- NEXT.md: the arithmetic construction to execute next, including primitive-source custody and coordinate shifts.
- SOURCES.json: immutable project source locations and actual public source read scopes.
- STATUS.json: explicit result/non-result accounting.
- checks/check_jets.py and checks/RESULTS.json: executable exact algebra controls.
- MANIFEST.sha256: file identity checks; not a mathematical certificate.

Replay from this folder:

    python3 checks/check_jets.py

To evaluate a supplied ten-coefficient jet:

    python3 checks/check_jets.py --jet actual_jet.json

That mode explicitly does not certify arithmetic provenance. No built-in jet represents the seed's Kato value.
