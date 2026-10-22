# Independent review of the saved 5-adic moment and single-table extractor

Date: 2026-10-12.

**Verdict: SUPPORTED_UNDER_STATED_INTEGRAL_MEASURE_AND_RETAINED_SYMBOL_INPUTS.**

This is a separate mathematical review of submitted `PROOF.md` §§2 and 4, with a small independent replay. It does not independently recertify the historical large modular-symbol computation, prove the tower theorem, evaluate a new symbol, or produce a coefficient at 17. I found no blocking mathematical error in the extractor or saved-data arithmetic.

## 1. Exact source convention

I freshly opened Stein–Wuthrich, *Algorithms for the arithmetic of elliptic curves using Iwasawa theory*, published author offprint:

<https://www.wstein.org/papers/mcom2649-iwasawa-alg.pdf>.

The relevant locations are **§3, printed pp.1762–1763**, and Proposition 3.5 on pp.1764–1765. The source defines plus symbols using the Néron real period, its good-reduction distribution as

\[
\mu_\alpha(a+p^n\mathbf Z_p)=\alpha^{-n}[a/p^n]^+
 -\alpha^{-n-1}[a/p^{n-1}]^+,
\]

and its finite polynomial by summing all Teichmüller components with exponent range \(0\le j<p^{n-1}\) for \(\gamma=1+p\). There is no division by \(p-1\). The packet uses these conventions correctly.

**Minor citation correction:** the submitted text calls this “Section 3.1.” The distribution and finite-polynomial definitions precede that subsection; §3.1 begins on p.1765 and concerns the p-adic multiplier. This locator issue does not change the formula. The web parser supplied the primary text; attempted page screenshots failed, so I do not claim fresh visual inspection.

## 2. The transfer is present, with the right index

Put \(q_n=p^{n-1}\) and

\[
\nu_n(U)=\sum_{k=0}^{p-1}(1+U)^{k p^{n-2}}.
\]

The lower-denominator symbol depends only on the exponent modulo \(q_{n-1}\), and the Teichmüller lifts reduce compatibly. Therefore the exact representative of the finite measure is

\[
P_n=\alpha^{-n}\Theta_n-\alpha^{-n-1}\nu_n\Theta_{n-1}.
\]

Its degree is less than \(q_n\). The group order is \(p^{n-1}\), not \(p^n\): denominator \(p^n\) corresponds to the degree-\(p^{n-1}\) principal-unit quotient.

The assumed integrality of the infinite measure implies

\[
L-P_n\in ((1+U)^{q_n}-1)\mathbf Z_p[[U]].
\]

The generator has zero constant coefficient, linear coefficient \(q_n\), and quadratic coefficient \(\binom{q_n}{2}\). Since \(p\) is odd, the last two are divisible by \(p^{n-1}\). Hence

\[
[U^2]P_n\equiv L_2\pmod {p^{n-1}}.
\]

This argument concerns an integral measure. Mere existence of a rational power series, without a denominator bound, would not establish the same precision.

For \(h=p^{n-2}\), the first three coefficients of \(\nu_n\) are

\[
p,\quad h\frac{p(p-1)}2,\quad
\frac12\left(h^2\frac{p(p-1)(2p-1)}6-h\frac{p(p-1)}2\right).
\]

For \(p\ge5\), the latter two are divisible by \(p^{n-1}\), including the boundary \(n=2\). It follows, using integral raw symbols, that

\[
[U^2](\nu_n\Theta_{n-1})\equiv p A_{n-1}\pmod {p^{n-1}}.
\]

All lower terms and their precision costs are therefore accounted for.

## 3. Elimination of lower tables

Write \(B_n=\alpha^{-n}A_n\), \(t=p/\alpha^2\). The preceding calculation gives

\[
B_n=L_2+tB_{n-1}+O(p^{n-1}),\qquad B_1=0.
\]

Induction is valid because multiplying the previous error by \(t\), of valuation one, raises its precision by one. Thus

\[
B_n=L_2(1+t+\cdots+t^{n-2})+O(p^{n-1}).
\]

Multiplication by \(1-t\) yields the claimed formula. Its multiplier is a unit because both \(\alpha\) and \(1-p/\alpha^2\) are units. Accordingly, if the top raw moment is nonzero modulo \(p^{n-1}\), its valuation is exactly that of \(L_2\). A zero residue supplies only a lower bound. Computing additional digits of \(\alpha\) alone cannot change this.

The general proof assumes integrality at the intervening layers, as the submitted statement says. It does not certify arbitrary numerical tables or permit replacing an unmatched source by a rescaled table. The extraction result does not require constant and linear terms of the infinite series to vanish.

The sharpness pair in §4.3 is valid: the difference of the two series is \((p-1)U((1+U)^q-1)\), so it vanishes at the finite quotient while changing the quadratic coefficient from \(q\) to \(pq\). This demonstrates the general precision limitation even for series vanishing below degree two. It is not a pair of actual seed measures.

## 4. Actual saved 5-adic arithmetic

I read the submitted checker before running it. It passes its 84 synthetic extraction tests, five precision controls, eight malformed-input controls, and four precision-boundary controls. Those controls do not prove arithmetic source authenticity.

The separate script `checks/independent_moment_check.py` instead reobtains the two supplied tables directly from the pinned historical Git commit

`0e8bb6859d1391e6d449b1ef02aff2cfd85310f1`,

under

`work/state-sync-2026-09-30/release/v0.2.6/evidence/src/BSD_SEED_2243_12_P5_RIGOROUS_UPGRADE_2026-09-19/run/`.

Both copies match byte-for-byte. Their hashes are:

| Table | Historical Git blob | SHA-256 |
|---|---|---|
| `SYMBOLS_m25.txt` | `b0d766f63e90ac9d17b2ca15ee2e387cd6b34ff6` | `d70db75fc5d6ac7dfddd8a36eef2aadba772ccdeb23f8a3253c1308065bc365e` |
| `SYMBOLS_m5.txt` | `a9961d9d45bc22605a331c994a3dee4119c1c12b` | `fb7b98d89b1885bacbb1d9d306c6c17fcefeafbb094baf1fcb5258756e6edf9c` |

Solving \(\omega^4=1\pmod {25}\) directly gives \(1,7,18,24\). Enumeration with \(\gamma=6\) gives grouped coefficients

\[
(-76,0,-76,76,76)
\]

and the complete raw finite polynomial

\[
380U+608U^2+380U^3+76U^4.
\]

All four plus-symbol Hecke rows agree. The lower table's augmentation is **exactly zero**, so in this particular replay the entire transferred lower polynomial is zero, not merely its quadratic coefficient modulo 5. Nevertheless, the finite projection still determines the infinite quadratic coefficient only modulo 5.

Using the retained table normalization \(\Omega_E=2\omega_1\), the moment is \(608/2=304\). Since \(\alpha\equiv3\pmod5\),

\[
\alpha^{-2}\cdot304\equiv1\pmod5.
\]

This reproduces the old coefficient unit. The independent check also verifies the transfer precision in 20 small \((p,n)\) cases and five sharpness cases, with results in `checks/independent_moment_check.json`. It neither regenerates the historical Fourier/Arb core nor makes a new seed coefficient evaluation.

## 5. Consequences and scope

The saved arithmetic supplies a genuine retained unit numerator for the separate tower argument. Whether it yields the stated integral Selmer identification additionally depends on the ordinary Kato and Greenberg inputs reviewed elsewhere; no finite computation proves those inputs.

For the ordinary 17-adic continuation, denominator \(17^3\) supplies precision modulo \(17^2\), and denominator \(17^4\) supplies precision modulo \(17^3\). With the retained matched height valuation and lower bound, these are the stated valuation-one and valuation-two tests. No such top table was computed in this review, and this formula alone does not predict a successful test.

There is no coefficient-prime uniformity statement here. The result removes lower-layer inputs from an authenticated numerator verifier while retaining the top-table arithmetic workload and its exact precision limitation.
