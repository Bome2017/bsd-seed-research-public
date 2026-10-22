# D=-23 derivative adapter: mathematical contract

This operation evaluates

\[
L'(E^{-23},1)=2\sum_{n\ge1}\frac{\chi_{-23}(n)a_n(E)}n E_1(cn),
\qquad c=\frac{2\pi}{23\sqrt{6503188012738584}}.
\]

The formula, root number, twist conductor and independent derivative-tail proof are retained from ../bridge_repair_assessment_2026-09-21/MCS_TWIST_IDEAL_REVIEW.md, sections 1 and 3. The character is the quadratic character modulo 23, zero on multiples of 23. It is implemented by listing nonzero squares and cross-checked by Euler's criterion. No value, sign or nonvanishing of the derivative is assumed.

## Inherited arithmetic and traversal

retained_arbcore.c is the byte-identical sealed C11 engine, included with its main renamed. Its fixed seed coefficients, verified prime input, prime-power recurrences, cofactor division, segment sieve, atomic work-unit writer, SHA verification, and deterministic combination are reused. The sealed original is never edited. The coefficient prefix and verifier records are freshly hash-checked against completed C11 bindings; this imports the retained coefficient grade rather than replaying all witnesses.

Set R=floor(sqrt(T)). Every n<=T is either R-smooth or uniquely m*q with q>R prime and m<=R. In the latter case gcd(m,q)=1, so a_n=a_m*a_q. The adapter sums the same partition as the retained table-free mode. It checks #smooth+#pairs=T on completion. A zero a_m, a_q, or character may be skipped only after the coverage counters are incremented.

Cutoffs are whole retained segments, T=k*2^24-1. Thus the existing reader's no-trailing-data check remains valid. No sealed segment is truncated. Memory consists of the small-prime table up to R, per-worker fixed blocks, and a fixed kernel table; there is no T-sized prime table.

## E1 Taylor model

For each exponent e from -32 to 8 and j=0,...,255, put

\[
s=2^e,\quad x_0=s(1+j/256),\quad u=(x-x_0)/s.
\]

Store the degree-eight polynomial for E1(x0+s*u), with coefficients in 256-bit Arb balls. The coefficient recurrence is precisely the E1 portion of the retained g2_node construction: expand exp(-(x0+s*u))/(x0+s*u), multiply by -s, and integrate termwise; the constant coefficient is Arb's direct expint(1,x0).

All constants and nodes entering an enclosure are exact integers/dyadics or Arb-generated balls. Floating frexp chooses a candidate node only. Before using it, the actual ball step must lie in [-1/256,2/256]; otherwise execution fails.

Complete monotonicity gives

\[
(-1)^k E_1^{(k)}(x)=\int_1^\infty v^{k-1}e^{-xv}\,dv.
\]

Therefore the ninth-derivative magnitude decreases with x. At a=x0-s/256>0, compute the ninth normalized coefficient in balls and use

\[
|R_8|\le \frac{s^9|E_1^{(9)}(a)|}{9!}(2/256)^9.
\]

This absolute error is added to every evaluation. Horner evaluation and summation use 128-bit Arb; all rounding and propagated uncertainty remain in the balls. The table covers every cn needed by the retained corpus, including the small-x region. This adapts existing Taylor machinery; it is not a claim of a new mathematical algorithm.

## Truncation and stopping test

The adapter uses B_D(T)=2*tail_MS(c,T)/(cT), algebraically identical to the derivative tail proved in the retained review. The endpoint is

\[
2S_T+[-B_D(T),B_D(T)].
\]

Only exclusion of zero by that interval certifies nonvanishing. All finite numerical/model error is already in S_T. Printed decimal endpoints are rounded outward. A failed nonvanishing test is inconclusive.

## Validation, checkpoints and scope

Kernel tests compare the Taylor balls with higher-precision direct Arb E1 values across dyadic cells and actual cn values. Representative 64-term blocks use independent trial-factor multiplication and Euler-character computation, then direct Arb E1, and compare their sums with the new kernel. These checks supplement the written error proof; sampling alone is not the proof of all evaluations.

Every work unit is write-once with a self-hash; restart reuses only units under the same parameter and source/binary bindings. The final coefficient root is compared to the prehashed prefix. A fresh combine pass checks every unit's self-hash, identity and coverage. Benchmark measurements precede selection of a full run; no old modular-symbol timing is relabeled a twist timing.

Success gives a computer-assisted analytic-rank-one twist input, conditional on the retained coefficient and analytic-source trust base. With the retained rank-one theorem and rank-two seed result it supplies rank E(Q(sqrt(-23)))=3. It evaluates no Stark ideal, settles no new primary component of the seed, and proves neither FIN, ORDER9 nor Q36.
