# Verified scope of the completed D=-23 certificate

2026-09-21. Exact bounded applicability check; no ideal evaluation or new Sha bound.

The returned [coverage report](/Users/bsm/BSD_TWIST_D23_CERTIFICATE_2026-09-21/CERTIFICATE_CONFIRMED_AND_COVERAGE.md) is correct about the primes served through 160. The [replay](D23_COVERAGE_CHECK.py) checks every prime from 5 through 160 against the exact regime (P) in [the source composition](MCS_NONSQUAREFREE_JOIN.md), together with splitting in K=Q(sqrt(-23)). It independently counts the points on the stated curve over each of those 35 finite fields. Every trace matches the retained coefficient corpus; its first segment was freshly hash-checked. [Exact results](D23_COVERAGE_CHECK.json) include all excluded primes and reasons.

| p | a_p | #E(F_p) |
|---|---:|---:|
| 13 | -4 | 18 |
| 31 | -8 | 40 |
| 41 | 6 | 36 |
| 47 | 4 | 44 |
| 71 | -2 | 74 |
| 73 | -6 | 80 |
| 101 | -6 | 108 |
| 127 | 22 | 106 |
| 139 | 4 | 136 |
| 151 | -8 | 160 |

These are exactly the served primes in the stated range. Each is good, ordinary, non-anomalous, outside {19,59,487}, and split in K. The other fixed K hypotheses were checked in the completed certificate. In particular 11 is inert, 23 is ramified and supersingular, 29 and 131 are split but supersingular, and 59 is split and ordinary but explicitly excluded by (P). These exclusions describe applicability, not support of Sha.

The printed finite-ball interval plus the conservative tail bound was also checked by exact rational arithmetic. It lies inside [39.512236,40.182321]. This rechecks the endpoint arithmetic; it is not a second full derivative computation or an independent audit of the software and source-theorem trust base.

## Exact implication at 13

Under the retained comparison and certificate grades, the now-known rank-three point contribution supplies
\[
I_3(\epsilon^{\rm Hg}_{1,0})
=\operatorname{Fitt}^0_{\mathbf F_{13}}\bigl(\Sha(E/K)[13]^*\bigr).
\]
Consequently
\[
I_3(\epsilon^{\rm Hg}_{1,0})=\mathbf F_{13}
\iff \Sha(E/K)[13]=0
\implies \Sha(E/\mathbf Q)[13^\infty]=0.
\]
The last implication is the retained restriction/corestriction argument at an odd prime, followed by the elementary torsion argument. Neither the ideal nor the 13-primary group has been evaluated by this check.

The test is stronger than seed vanishing alone: it also excludes 13-torsion arising from the quadratic twist. The twist's analytic rank one gives finiteness of its Sha, not its order or 13-primary vanishing. This qualification is already in [the quotient deduction](MCS_DERIVED_HEIGHT_GATE.md), equation (5), and remains load-bearing after the twist certificate.

The current conditional next-order threshold remains 1521. If seed 13-primary vanishing were separately proved, it would become 9*17^2=2601 under FIN; this is only a conditional consequence, not an updated result or proposed operation. FIN and Q36 are untouched. The point count at 13 corroborates the earlier Aristotle data; no Lean build was rerun here.

## Custody

The returned report and its five-file manifest were read and verified. Its STATE.json has a completed-certificate status but retains old phase, next-step and pre-correction fields. Those are historical, superseded by the actual completed local certificate; they do not authorize a restart. The external files and the sealed derivative-run artifacts remain unchanged. This additive review is integrated in the existing master. No next-prime calculation, new package, source survey or successor was launched.
