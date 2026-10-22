# Review of the twist candidates, cost estimate, and characteristic-ideal claim

2026-09-21. Reviews [the returned attempt](/Users/bsm/BSD_MCS_SOURCE_APPLICATION_CHECK_2026-09-21/TWIST_AND_IDEAL_ATTEMPT.md). Verdict: its NEITHER_SUPPLIED conclusion stands; the claimed exact cost and index-to-ideal computation do not. No twist derivative or Stark ideal is evaluated here. No arithmetic engine is launched.

The separate [wording acceptance](/Users/bsm/BSD_MCS_SOURCE_APPLICATION_CHECK_2026-09-21/WORDING_CORRECTIONS_2026-09-21.md) agrees with §5 of the [existing height review](MCS_DERIVED_HEIGHT_GATE.md). It supplies no further mathematics.

## 1. Exact candidate checks pass

An independent small-integer check reproduced both eight-entry lists in the return. For each negative integer down to \(-4999\), test \(D\equiv1\pmod8\), squarefreeness of \(|D|\), and Euler's criterion at \(3,2243,4547,5843\), additionally at \(11\) for that list. The bad-prime primalities were checked by trial division.

The first list begins \(-23,-143,-863,-1031\); the list with 11 split begins \(-1031,-1055,-1847,-2471\). In particular \(-23\) is not admissible for \(p=11\). No candidate has been certified to have analytic rank one in this operation.

The coprime quadratic-twist formulas \(N_D=ND^2\) and
\[
a_n(E^D)=\chi_D(n)a_n(E),\qquad
w(E^D)=\chi_D(-N)w(E)=-1
\]
give the stated parity and coefficient reuse. Parity alone leaves orders \(1,3,5,\ldots\) possible.

## 2. The numerical cost was calibrated to the wrong count and an older corpus

The [retained analytic-rank certificate](/Users/bsm/BSD_RIGOROUS_STREAM_CORE_2026-09-19/ANALYTIC_RANK_CERTIFICATE.md), §§1, 4 and 6, distinguishes:

| Quantity | Actual count |
|---|---:|
| Prime coefficients \(a_q\) verified | 8,444,396 |
| Summation cutoff for the generated \(a_n\) | 150,000,000 |

Thus 0.1047 is not the old cutoff divided by \(\sqrt N\). The old normalized cutoff is about 1.86006. Keeping that normalized cutoff for \(D=-23\) gives
\[
T_{-23}=23(150,000,000)=3,450,000,000,
\]
not 194 million. This comparison is not a sufficient cutoff or runtime certificate: the twist uses a different derivative kernel, and its nonzero derivative size is unknown.

There is also a substantial reuse input missing from the return. The completed [C11 certificate bindings](../active_full_bsd/p11/CERTIFICATE_BINDINGS.json) retain 2,333 coefficient segments, covering the engine cutoff
\[
T_{\rm C11}=39,141,244,927.
\]
The retained [launch record](../active_full_bsd/p11/LAUNCH.json) and completion bindings specify segments of length \(2^{24}\). Therefore the 3.45-billion comparison cutoff is already inside the existing corpus.

**Current byte check:** all coefficient files and verifier records for segments 0 through 205 match their C11-bound sizes and SHA-256 hashes: 206 segments, 661,154,227 bytes, coverage through 3,456,106,495. The read-only hash pass took 1.57 seconds. This verifies custody of that prefix, not a fresh witness replay; the retained coefficient trust qualifications remain.

No new prime-coefficient generation is required to use this prefix. Generating composite coefficients, performing the twisted derivative sum, proving its numerical errors, and measuring the actual implementation cost remain separate obligations. The old engine timings cannot supply an exact multiplier for them.

## 3. The derivative and tail calculation that a valid cost gate needs

This is a direct adaptation of the retained Mellin calculation, not a new algorithm. Put \(c=2\pi/(|D|\sqrt N)\) and \(E_1(x)=\int_x^\infty e^{-u}\,du/u\). Odd functional-equation sign gives
\[
L'(E^D,1)=2\sum_{n\ge1}\frac{\chi_D(n)a_n(E)}n E_1(cn).
\tag{1}
\]
Indeed, differentiate the Fricke-folded Mellin integral at its center. Its weight becomes \(2\log t\), and integration by parts gives
\(\int_1^\infty e^{-xt}\log t\,dt=E_1(x)/x\).
The completed-function normalization then gives (1). Exponential decay justifies differentiation and summation.

For an integer cutoff \(T\ge1\), an explicit valid absolute tail bound is
\[
B_D(T)=2e^{-cT}\left[
\frac{2\sqrt T}{cT}
+\frac{T^{-1/2}}{cT}
\left(\frac{\log T+2}{c}+\frac1{Tc^2}\right)\right].
\tag{2}
\]
To prove it, use \(|a_n|\le d(n)\sqrt n\), put \(g(x)=x^{-1/2}E_1(cx)\), and use the retained divisor-sum bounds
\(x\log x-x\le\sum_{n\le x}d(n)\le x(\log x+1)\).
Partial summation at integer \(T\) bounds the tail by
\[
2\left(2Tg(T)+\int_T^\infty(\log x+2)g(x)\,dx\right).
\]
Now use \(E_1(cx)\le e^{-cx}/(cx)\), \(x^{-3/2}\le T^{-3/2}\), and
\(\log x\le\log T+(x-T)/T\) to obtain (2).

A ball enclosure of the truncated sum plus this tail could certify nonvanishing. Neither that sum nor an adequate precision/cutoff nor a runtime benchmark is supplied here. The report's claim that the cost is exact must therefore be withdrawn, while its coefficient-reuse observation survives in a stronger form.

## 4. Finite twist coverage: a valid obstruction with narrower scope

Let \(D_1,\ldots,D_k\) be fixed negative fundamental discriminants and let \(r\) be the \(\mathbf F_2\)-rank of their quadratic characters. The density of primes inert in all the fields is
\[
2^{-r}>0,
\]
not necessarily \(2^{-k}\).

**Proof.** Put \(M=\operatorname{lcm}(|D_i|)\). The joint character map on \((\mathbf Z/M)^\times\) has image of size \(2^r\). The all-minus pattern occurs: it is the image of \(-1\), because all characters are odd. Its fiber is a coset of the kernel. Dirichlet's equidistribution of primes in reduced residue classes gives density \(2^{-r}\). More simply, every prime congruent to \(-1\pmod M\) is inert in all the fields. \(\square\)

Consequently finitely many fixed imaginary twists cannot cover all sufficiently large primes by requiring \(p\) to split in at least one of them. This does not exclude a theorem allowing \(K\) to vary with \(p\), or a theorem handling a nonsplit regime. Splitting coverage itself settles no primary group: the independent ideal bound is still required, along with the other hypotheses of the join.

## 5. The equivalence was already known; the claimed evaluation route is not established

The equivalence
\[
I_3(\epsilon^{\rm Hg}_{1,0})=\mathbf F_p
\quad\Longleftrightarrow\quad\Sha(E/K)[p]=0
\]
is exactly equation (5) of the existing height review, conditional on its rank-three hypotheses. Re-proving it is not new progress or an impossibility argument. The requirement is a non-circular proof or computation, not a ban on mentioning Sha in such a proof.

The return next asserts that all needed ideals are determined by the Heegner \(\Lambda\)-index. The source [Kataoka–Sano, Conjecture 5.7 and Proposition 5.12](https://jamathr.org/index.php/jamr/article/download/Vol-2Issue-2Paper-1/Vol-2Issue-2Paper-1/38199) relates characteristic ideals and a specified element of a determinant line. It does not identify characteristic-ideal data alone with every specialized higher Fitting ideal. MCS uses the full Selmer-complex comparison.

Here is a concrete algebraic counterexample to that inference. In \(\Lambda=\mathbf Z_p[[t]]\), put
\[
h=(t-p)((1+p)t+p),\qquad g=th,
\]
and consider perfect two-term complexes in degrees 1 and 2 with differentials
\[
A=\operatorname{diag}(0,g,g),\qquad
B=\operatorname{diag}(0,t,t,h,h).
\]
Both have \(H^1\simeq\Lambda\). Their \(H^2\) torsion modules have the same characteristic ideal \((g^2)\). In both take \(y=g b\) in the same abstract free rank-one \(H^1=\Lambda b\); the quotient \(H^1/\Lambda y\) is identical. Even the involution condition is compatible: for \(\iota(t)=-t/(1+t)\), one has \(\iota(g)=-g/(1+t)^3\).

Nevertheless \(h(0)=-p^2\), so at augmentation their \(H^2\) groups are respectively
\[
\mathbf Z_p^3,\qquad
\mathbf Z_p^3\oplus(\mathbf Z_p/p^2)^2.
\]
Both specialized \(H^1\) groups have \(\mathbf Z_p\)-rank three. After reducing the complexes modulo \((p,t)\), their degree-one groups are \(\mathbf F_p^3\) and \(\mathbf F_p^5\); hence their third Fitting ideals are respectively \(\mathbf F_p\) and zero. This is an abstract counterexample, not a claim that either complex is the seed's Selmer complex. It shows exactly why the stated index/characteristic data alone do not determine the desired specialization.

Nor has the return proved that explicit construction of the entire Heegner tower is the only way to evaluate the ideal, or that a large \(N\) forces a particular computational representation of \(X_0(N)\). Those claims need their own arguments. They are not obstructions established by the absence of an implementation in the inspected corpus.

## 6. Decision and exact scope

Retain the verified admissible candidates, root-number calculation, and the finite fixed-family coverage obstruction with the corrected density. Reject the advertised exact cost and the inference that the characteristic ideal determines \(I_3\). Retain the existing join and rank-three shift.

The concrete new reuse finding is that the C11 coefficient corpus already covers the scaled \(D=-23\) cutoff; equations (1)–(2) give the analytic calculation to certify if it is undertaken. No claim is made that this cutoff excludes zero, that a suitable rank-one twist is now certified, or that its certificate alone would resolve a Sha component. FIN, ORDER9, and Q36 remain open. This review launches no successor.
