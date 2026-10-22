# Addendum to the optional BKS discovery brief

This accompanies the sealed preflight; it does not change its manifest or authorize a run.

## Paste-ready instruction

> Keep the BKS truncation and period conventions explicit. Write \(E_{S,p}=\prod_{q\in S_f}P_q(q^{-1})\), with \(L_S(s)=L(s)\prod_{q\in S_f}P_q(q^{-s})\). Here \(S\) contains \(p\); it is not a fixed prime-independent Euler multiplier. For the seed at every good \(p\ge5\), \(P_p(p^{-1})=\#E(\mathbf F_p)/p\) has valuation \(-1\). In the formal normalization of BKS Proposition 4.14, also retain \(v_\xi=\Omega^+/\Omega_\xi\). Thus the coefficient relative to the untruncated \(q_{\rm an}=L''/(2\Omega^+R_\infty)\) is \(v_\xi E_{S,p}q_{\rm an}\). Any claim of integral descent, residual primitivity or agreement with a tame scalar must calculate the product in the specified lattice, including any compensating regulator divisibility. Do not absorb these varying factors into a fixed finite exception set or an unspecified unit. No identification with project \(q\), \(288\), \(w_{p,\ell}\) or \(C_p\) is supplied by this notation.

## Source and derivation

BKS §2.1 requires \(\{\infty\}\cup\{q:q\mid pN\}\subset S\). The paragraph after (2.1.4) compares \(\Omega_\xi\) and \(\Omega^+\); under residual irreducibility their ratio is a \(p\)-unit. Remark 2.1 separately warns about integrality when modifying Kato's normalization. Proposition 4.14 and (4.3.3) use
\[
\kappa_\infty=\frac{L_S^*(E,1)}{\Omega_\xi R_\infty}R_\omega^{\rm Boc},
\qquad \Omega^+=v_\xi\Omega_\xi .
\]
This is the conjectural relation in the formal normalization, not an unconditional comparison.

Since the seed has analytic rank two and the removed factors are nonzero at \(s=1\), multiplication of Taylor series gives
\[
L_S^{(2)}(E,1)=E_{S,p}L^{(2)}(E,1).
\]
Hence the corresponding scalar is \(v_\xi E_{S,p}q_{\rm an}\). The introduction's \(\Omega^+\) display must not be interchanged with the formal \(\Omega_\xi\) display without binding their data. No allegation of a source error is needed for this bookkeeping.

For good \(p\), \(P_p(X)=1-a_pX+pX^2\), so
\[
P_p(p^{-1})=\frac{p+1-a_p}{p}.
\]
The retained seed equation is
\[
y^2=x^3-22735x^2+106272484x.
\]
Its point \((0,0)\) gives nonzero two-torsion at every good odd prime; therefore \(\#E(\mathbf F_p)\) is even. For \(p\ge7\), Hasse gives
\[
0<\#E(\mathbf F_p)\le p+1+2\sqrt p<2p.
\]
Divisibility by \(p\) would force the odd value \(p\), a contradiction. At \(p=5\), exact enumeration gives \(\#E(\mathbf F_5)=8\). Thus \(p\nmid\#E(\mathbf F_p)\) and \(v_p(P_p(p^{-1}))=-1\) throughout the stated good-prime domain, including supersingular primes.

This computes the \(p\)-factor only. All other Euler and lattice factors still need their own accounting.

## Effect on the extraction tests

Trial C remains a valid abstract warning: an identity with a unit scalar does not alone prove residual primitivity. It is not a counterexample to the full BKS expression. In the actual expression, a \(1/p\) factor could compensate a proved factor \(p\) in the regulator; the relevant object would then involve \(R_\omega^{\rm Boc}/p\). Whether this is integral or primitive is a separate arithmetic question. Do not assume either answer from the schematic identity.

A global arithmetic index and its realization may therefore have known \(p\)-dependent multipliers. The goal is to prove and control those multipliers, not to reject a construction for depending on \(p\).

This addendum supplies no bound on those realizations, no common arithmetic index, and no new Sha vanishing result.
