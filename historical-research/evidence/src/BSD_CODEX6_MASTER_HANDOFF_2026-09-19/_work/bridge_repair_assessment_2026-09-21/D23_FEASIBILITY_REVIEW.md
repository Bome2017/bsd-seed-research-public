# D=-23 feasibility: valid measurements and unsupported conclusions

2026-09-21. Review of the [returned feasibility report](/Users/bsm/BSD_TWIST_D23_CERTIFICATE_2026-09-21/FEASIBILITY_REPORT.md), its STATE/RESUME, the actual retained engine source, and the completed C11 timeline. No derivative sum, benchmark, new engine, or arithmetic run was launched. The original external files and sealed engine remain unchanged.

## 1. Tail values are reproduced; adequacy is not decided

Ordinary floating evaluation of the already-derived bound reproduces:

| T | B_D(T), approximately |
|---:|---:|
| 1,000,000,000 | 5548.43 |
| 3,450,000,000 | 0.342642633 |
| 5,000,000,000 | 0.001265315 |
| 7,000,000,000 | 0.00000107977 |

These are numerical cross-checks of the formula, not outward-rounded certificate values. For a ball S_T enclosing the truncated sum and a certified tail upper bound B, the test is

\[
0\notin S_T+[-B,B],
\qquad\text{equivalently }\operatorname{dist}(0,S_T)>B.
\]

Before S_T is computed, B=0.343 proves neither adequacy nor inadequacy of the 3.45-billion cutoff. The report also incorrectly replaces a condition on the truncated sum by |L'|>0.343. That latter condition is not the certificate test. The same issue applies at seven billion: a small absolute tail is not six orders of *margin* without a lower bound on the truncated sum. Neither cutoff is yet certified adequate.

A floating pass at one billion can provide heuristic scale information only. The available rigorous tail there is about 5548, so it cannot by itself rigorously select between five and seven billion. Decay at cn=1 is not a theorem that later terms are negligible.

## 2. The recorded timing is real, but Stage A was misidentified

The [actual timeline](../active_full_bsd/p11/run/logs/timeline.log) records 1937 seconds for denominator 121 and 153 seconds for denominator 11, at the stated cutoffs and twelve workers. Linear scaling to seven billion gives about 346 or 316 seconds. These are extrapolations of the *complete modular-symbol workload*, not an isolated coefficient-stream benchmark or a measurement of the twisted derivative.

In particular, Stage A does not accumulate modular integers. The retained [arbcore.c](/Users/bsm/BSD_RIGOROUS_STREAM_CORE_2026-09-19/src/arbcore.c:203) uses arb_t balls, exponentials, and Arb multiply/add operations in both the smooth and large-prime parts. The report's proposed floating-operation count and 1.5x–20x multiplier have no measured basis.

Stage W's 2h33m is the recorded stage elapsed time; the run reused 928 previously sealed segments and produced 1405 new ones. It is not the cost of producing all 2333 from scratch. Reuse of the completed coefficient corpus remains valid.

## 3. E1 machinery already exists; the twist mode does not

The source's [g2_node](/Users/bsm/BSD_RIGOROUS_STREAM_CORE_2026-09-19/src/arbcore.c:78) already calls arb_hypgeom_expint for E1 and computes its Taylor coefficients by

\[
E_1'(x)=-e^{-x}/x.
\]

It then integrates the coefficients of -E1/x to obtain the G2 model. Thus the claim that the E1 approximation machinery does not exist is too strong. The [existing design](/Users/bsm/BSD_RIGOROUS_STREAM_CORE_2026-09-19/DESIGN.md:29) already supplies the Taylor-model framework, range guards, and ball-error propagation.

The analogous remainder argument is available directly:

\[
(-1)^kE_1^{(k)}(x)=\int_1^\infty u^{k-1}e^{-xu}\,du>0
\]

for x>0; the derivative magnitude decreases with x. A degree-J Taylor polynomial about x0 therefore has remainder at x bounded by

\[
\frac{|E_1^{(J+1)}(a)|}{(J+1)!}|x-x_0|^{J+1},
\qquad 0<a\le\min(x,x_0).
\]

This is an elementary adaptation, not a novelty claim or a tested implementation. Handling the small-x range efficiently, incorporating the character, and bounding the accumulated errors remain real work. The existing engine has no twisted-first-derivative command.

Two concrete implementation constraints were omitted from the return:

* The old l2 mode allocates a dense 4(T+1)-byte table: about 28 GB at seven billion, before other memory. The completed C11 msl mode instead uses a table-free smooth/large-prime decomposition. A twist adaptation must preserve bounded memory rather than simply switch the old derivative mode.
* The retained segment reader rejects trailing data. A cutoff inside an existing coefficient segment needs an explicitly justified prefix reader, or rounding the cutoff upward to a full segment boundary; the sealed segment itself must remain unchanged.

All ten retained engine source/binary identities still match the completed C11 bindings. The external three-file manifest and the pre-review canonical 285-file manifest also passed.

## 4. Decision and endpoint

The useful next implementation step is an isolated twist adapter reusing the verified corpus, table-free traversal, and existing E1/Taylor components. Benchmark representative small-, middle-, and large-x work with that actual adapter before predicting a full runtime. Choose the final cutoff adaptively using the certified truncated ball and tail; a floating scout may guide the choice but does not certify it. No separate numerical engine or guessed multiplier is justified by this report.

This review neither launches that implementation nor certifies rank one. A successful derivative enclosure would close the stated twist-rank premise and give rank E(Q(sqrt(-23)))=3 under the retained rank-one theorem. The independent Stark-ideal evaluation remains missing. FIN, ORDER9, Q36, and all primary-group statuses are unchanged.
