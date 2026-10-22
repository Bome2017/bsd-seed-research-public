# Bounded FIN continuation, 21 October 2026

Baseline: lab branch research/fin-relative-discriminant-gate-2026-10-21 at 77d4b331885138eb1f3f93d8063b06d6d7eb730b.

1. Actual seed norm-one source experiment. Use the retained monic even degree-24 polynomial F(w)=G(w^2), with tau(w)=-w. Test Cayley norm-one elements (b*w+a)/(b*w-a), 1<=a<=2048, 1<=b<=16, gcd(a,b)=1. Also test u=(a+b*w^2+c*w)/(a+b*w^2-c*w) with a=1,2,4,...,512; b=+/-1,+/-2,+/-4,+/-8; c=1,4,16,64,256. Remove projectively duplicate triples. A nonintegral exact trace rejects ordinary-unit admission. Trace integrality is only necessary; passing it must be followed by full characteristic-polynomial integrality and nontriviality checks. No known Sha5 result is used. The aim is an authentic nontrivial ordinary unit in the odd sector; class completeness remains separate even upon success.

2. Audit and test the existing whole-relative-class order expression B_p. Determine whether positivity can turn it into the sufficient ceiling three, even granting the best possible removal of its unit term. Bound the expression itself, not the true class number; any obstruction is scoped to the existing expression, not all analytic methods or FIN.

3. Adapt based on actual arithmetic outcomes. Do not treat partial class generators as complete; do not retry the stopped 196-row and 31-function families or launch p53/743. Stage 2 (p53) and stage 3 (Q36) remain deferred.

Execution environment lacks PARI/GP; attempted installation/download failed. Wolfram's actual degree-24 unit call returned no result within a 12-second bound after an earlier backend failure. Those are resource outcomes, not mathematical impossibility claims. Python exact rational arithmetic is used for the candidates and certificates below.
