# Final test of the vertex-spherical completions

**ENDPOINT_DELTA_NONZERO_PROVED.**

\[
\boxed{0.000757821864\le\Delta_*\le0.000841639764.}
\]

The direct-integral enclosure is
\([0.000691563630,\,0.000907897998]\); the integration-by-parts enclosure is the narrower interval displayed above. Both independently bounded representations exclude zero, with their shared retained coefficient certificate and shared Arb implementation. Endpoints are outward-rounded exact rationals extracted from the ball dumps.

**Scoped theorem.** With the fixed away-from-4547 data and incoming/scattered normalization of the existing construction, no completion obtained by Fricke symmetrization of a single vertex-spherical line of the specified length-two local segment reproduces the weighted Mellin period. These are exactly the midpoint and symmetrized-endpoint choices proved in §1. Their residuals are both rigorously positive.

This closes the specified two-case mechanism. It does not exclude the entire invariant linear span or other local conditions. No other completion is tested and no successor is started.

The numerical run used **54.315 seconds**, **33234944 bytes** peak resident memory, and **128-bit Arb** arithmetic, within the predeclared 600-second / 2-GB budget. Earlier midpoint source and certificate files remain unchanged.

| Rigorous error component | Direct integral | Integration by parts |
|---|---:|---:|
| Unknown coefficients beyond 150 million | 0.00010814529 | 0.000039966166 |
| Coefficient compression | 1.2020895e-9 | 1.8886127e-6 |
| Residual Fourier truncation and omitted arguments | 1.1374716e-10 | 4.3390944e-8 |
| Panel-specific coefficient cutoffs | 2.0582044e-8 | 1.0780315e-8 |
| Quadrature remainder | 4.2136510e-15 | 5.9826501e-15 |
| Infinite integration tail | 8.1886329e-895 | 5.7342346e-898 |
| Ball arithmetic radius | 4.9026847e-25 | 2.4687647e-24 |
| Total analytic error before final ball-radius rounding | 0.00010816719 | 0.000041908950 |

All tabulated bounds are rounded upward. The final intervals use the full exact ball outputs, including the final radius rounding; the printed partial-sum centre alone is not a proof input. See the [machine-readable certificate](endpoint_delta_numeric/evidence/CERTIFICATE.json), [full execution log](endpoint_delta_numeric/evidence/endpoint128.log), and [resource record](endpoint_delta_numeric/evidence/execution_budget.json).

## 1. Exact scope and the vertex gate

Fix the meromorphic Eisenstein family, its away-from-4547 data, and its incoming/scattered normalizations from the [four-orbit classification](AUTOMORPHIC_MIDDLE_ORBIT_CLASSIFICATION.md). Here **vertex-spherical/Fricke symmetrization** means: choose the spherical line of one vertex of the specified length-two segment, apply the Fricke symmetrizer, and then impose those existing normalizations. It does not mean the span of several vertex lines with freely chosen coefficients.

**Lemma.** This procedure has exactly two normalized outcomes: the midpoint section and the endpoint-symmetrized section already defined in classification (6.3).

**Proof.** Work over meromorphic germs at zero, before specialization. In the unramified local family, the maximal compact fixing vertex \(j\) has the one-dimensional spherical line
\[
\mathscr L_j=\mathcal M e_j,\qquad e_j(z,s)=E(p^jz,s),\qquad j=0,1,2.
\]
The local Fricke involution exchanges \(e_0\) and \(e_2\), and fixes \(e_1\), with the normalization verified in classification §§4–5. The symmetrizer therefore sends the three lines to precisely
\[
\mathcal M(e_0+e_2),\qquad \mathcal M e_1.
\]
These lines are distinct as meromorphic families: the first Fourier frequency of \(e_0+e_2\) is absent from \(e_1\). Specialization at zero, where each \(E(z,0)=1\), does not classify the families or their jets.

Writing \(r(s)=2^s+2^{-s}-1\), \(D(s)=r(s)-r(1-s)\), \(h(s)=p^s+p^{-s}\), and \(B(s)\) as in that classification, the two constant-term equations uniquely give
\[
(v_0,v_1)=\frac{(1,-r(1-s))}{BD}
\quad\text{on the midpoint line},
\]
\[
(u_0,u_1)=\frac{(1,-r(1-s))}{hBD}
\quad\text{on the symmetrized endpoint line}.
\]
Here \(B(0)=16\), \(D(0)=-1/2\), \(h(0)=2\), so both are regular genuine jets. Thus the normalized outcomes are exactly
\[
\mathcal E_{\rm mid}(z,s)=\mathcal C_M(pz,s),\qquad
\mathcal E_*(z,s)=\frac{\mathcal C_M(z,s)+\mathcal C_M(p^2z,s)}{p^s+p^{-s}}.
\tag{1}
\]
This proves the claimed two-case exhaustion for the stated procedure. ∎

The full invariant *linear space* is instead
\(\mathcal M(e_0+e_2)\oplus\mathcal M e_1\), which has infinitely many lines. Two individual nonvanishing certificates would not exclude every mixture. Such mixtures are expressly outside this operation; no coefficients are chosen using an \(f\)-period. Nor are all other local conditions or all Bruhat–Tits vertices being classified.

## 2. Residual identity and the certified evaluator

Put \(J_{\rm mid}=\mathcal E_{\rm mid}''(z,0)=L(z)^2+R_{\rm mid}(z)\), where \(L(z)=\log(\sqrt N\operatorname{Im}z)\). Since \(\mathcal E_{\rm mid}(z,0)=1\), \(h'(0)=0\), and \(h''(0)=2\log^2p\), differentiating (1) gives
\[
J_*(z)=\frac{J_{\rm mid}(z/p)+J_{\rm mid}(pz)}2-\log^2p.
\]
The averaged elementary terms are \(L(z)^2+\log^2p\). Hence
\[
\boxed{R_*(z)=\frac{R_{\rm mid}(z/p)+R_{\rm mid}(pz)}2.}
\tag{2}
\]
This agrees term by term with the original endpoint residual in [the second-jet experiment](AUTOMORPHIC_SECOND_JET_EXPERIMENT.md), (13): its two coefficients are \((-1/2,3\log2/2)\) and \((3/4,-3\log2/2)\). No lower logarithmic moment is discarded.

For \(t=\sqrt Ny\), write \(r_*(t)=R_*(it/\sqrt N)\). With the exact function \(H\) and eight odd divisor products \(q\) of [the midpoint certificate](MIDPOINT_DELTA_INTERVAL.md), §3,
\[
r_*(t)=\frac12\sum_q\left[
H(qt/\sqrt N)+H(p^2qt/\sqrt N)\right].
\tag{3}
\]
The only change to the residual evaluator is these sixteen arguments and the factor \(1/2\). The midpoint section, source files, coefficient data, and its saved numerical certificate remain unchanged.

The geometric identity \(H(v)=H(1/(8v))\) and all real/complex bounds in the midpoint report still apply. Doubling the number of arguments while halving their coefficients preserves exactly the same majorants \(B_R,B_C,B_1,B_{1,C},\varepsilon_R,\varepsilon_1\). Every coefficient-tail, Taylor-compression, residual Fourier, quadrature, and infinite-integral bound in that report therefore applies unchanged, with the actual endpoint residual substituted into the interval-cell bounds (14)–(15).

The two existing representations are
\[
\Delta_*=c\int_1^\infty f(it/\sqrt N)[r_*(t)-r_*(1)]\,dt
=\int_1^\infty\phi(t)r_*'(t)\,dt,
\tag{4}
\]
where \(c=2\pi/\sqrt N\), \(\phi(t)=\sum a_n e^{-cnt}/n\), and \(\phi(1)=0\) is the already proved zeroth moment. These are separately bounded mathematical representations with shared coefficient inputs and shared ball-arithmetic software.

## 3. Predeclared numerical protocol

The operation has a 600-second aggregate execution budget and a 2-GB memory budget, declared before computation. The initial calculation uses 128-bit Arb arithmetic. It imports the verified coefficients through 150 million and their exact integer-bin moments, whose input hashes are checked against the retained certificate. No cached midpoint integral is accepted by the adapted engine.

Parameters are those of the final midpoint run: 24 residual Fourier terms, argument cutoff 16 with its explicit error, coefficient-bin degree 7, 96 integration panels of length \(1/4\) in \(u=\log t\), 20-point Gauss quadrature, and 768 interval cells covering \(1\le t\le4\) for unknown-coefficient tails. The integral beyond \(u=24\) has its separate certified bound. Complete formulas and proofs of all these bounds are midpoint certificate §§3–6; none is inferred from a floating estimate or agreement between the representations.

The [adapted engine](endpoint_delta_numeric/src/delta.c), [budget wrapper](endpoint_delta_numeric/src/run_bounded.py), and input hashes in [the retained-input record](endpoint_delta_numeric/evidence/retained_inputs.txt) are local evidence for this operation. The resulting positive enclosure is recorded above. The [replay script](endpoint_delta_numeric/src/replay.sh) checks the retained input hashes, rebuilds the adapted source, and reruns both integrals. This has computer-assisted proof grade with the stated shared trust base; it is not an independent human review or a proof-assistant verification.
