# Independent desk audit of the corrected Bockstein content certificate

Date: 2026-10-12.

**Disposition: ALGEBRA_ACCEPTED_UNDER_STATED_HYPOTHESES; ARITHMETIC_APPLICATION_CONDITIONAL; NO_NEW_SEED_RESULT.**

This is an independent AI desk review of the submitted `PROOF.md`, compared with the October 7 `CONTENT_BOUND_PROOF.md`. It is not formal verification, independent human review, or fresh certification of Kato's arithmetic hypotheses. No submitted input was changed, no seed quantity was computed, and nothing was published.

The subsequent `ALGEBRA_INTERFACE_ADDENDUM.md` separately checks the primitive-target deduction and the resulting ordinary source-gap identity under an exact height comparison.

## 1. Scope and principal finding

The equality

\[
m=\tau+b+e,\qquad e=v_p((g/d_1)(0))\ge0
\]

is correct under the hypotheses in submitted `PROOF.md` §2. I found no mathematical defect in its written derivation. The arithmetic consequence

\[
\delta_p\ne0,\quad m_p-w_p-b_p\le1
\quad\Longrightarrow\quad \Sha[p^\infty]=0
\]

then follows if the retained arithmetic inputs really identify this complex, class, lattice, and torsion correction. Those identifications remain imports at their existing grades. In particular, this audit does not independently establish the all-height-one Kato inequality or the seed local-torsion exclusions.

The correction is a strict improvement of the previous sufficient bound in abstract algebraic examples. It is not a necessary criterion for vanishing, a cofinite bound, a numerical seed result, or an arithmetic realization of the abstract examples.

Inputs read:

- `submitted/BSD_BOCKSTEIN_CORRECTED_CERTIFICATE_2026-10-12/PROOF.md`, especially lines 36–192 and 194–266.
- `/Users/bsm/BSD_GITHUB_UPDATE_CODEX_2026-10-04/lab/work/returns/BSD_KATO_CONTENT_BOUND_CODEX_2026-10-07/CONTENT_BOUND_PROOF.md`, especially §§2–6.
- Submitted `REPORT.md` and `SOURCES.md`, to check that their stated scope is consistent with the proposition.

## 2. Re-derived algebra

Write \(A=\mathbf Z_p\), \(R=A[[U]]\), \(D:R^{n+1}\to R^n\), and \(M=R\eta\). Let \(\Delta\) be the signed maximal-minor vector.

1. **The primitive assertion is correctly limited to codimension one.** Since \(D\Delta=0\), there is \(d\in R\setminus\{0\}\) with \(\Delta=d\eta\). An irreducible common divisor \(f\) of the coordinates of \(\eta\) would give an integral vector \(\eta/f\in\ker D\). Freeness with basis \(\eta\) would force \(1/f\in R\), a contradiction. Thus at every height-one localization at least one coordinate of \(\eta\) is a unit. This does not imply that the coordinates generate the unit ideal in \(R\), nor that \(\eta(0)\) is primitive over \(A\).

2. **The characteristic factor is correctly extracted from the actual minors.** Over the DVR \(R_{\mathfrak q}\), the valuation of the ideal of maximal minors is the length of the torsion cokernel. Since \(\eta\) has a unit coordinate there, this valuation is \(v_{\mathfrak q}(d)\). Therefore \(d\) generates \(\operatorname{char}_R(X)\). The specified source quotient is \(M/Rz\simeq R/(Ug)\), so the inequalities at every height-one prime imply \(d\mid Ug\). This is exactly where the global integral divisibility enters.

3. **The first-order nonvanishing follows; it is not assumed by defining \(b\).** Rank \(D_0=n-1\) gives \(\Delta(0)=0\). Thus \(U\mid d\), while \(g(0)\ne0\) and \(d\mid Ug\) force \(\operatorname{ord}_U(d)=1\). Consequently \(d=Ud_1\), \(d_1\mid g\), and
   \[
   [U]\Delta=d_1(0)\eta(0)\ne0.
   \]

4. **The Smith calculation gives equality, not merely divisibility.** Put \(D_0\) in Smith form by constant unimodular changes of bases, with nonzero entries \(s_1,\ldots,s_{n-1}\). Its kernel is exactly the last two coordinate directions; the primitive torsion-free cokernel is exactly the last target coordinate. Let \((u,v)\) be the last row of \(D_1\) in those two directions. It is the row of \(\overline\beta\). Every nonzero first derivative of a maximal determinant must differentiate the zero last row and retain the other diagonal entries. Hence the cofactor vector has only the last two possible nonzero entries,
   \[
   [U]\Delta=\pm s(0,\ldots,0,v,-u),\qquad
   s=\prod_{i=1}^{n-1}s_i.
   \]
   Since the vector is nonzero, \(\overline\beta\ne0\), and its content is exactly \(\tau+b\). The empty product for \(n=1\) is correctly 1.

5. **The specialization defect is retained.** The kernel \(W=\ker D_0\) is saturated in \(A^{n+1}\), so content in \(W\) equals ambient content. Put \(\mu=\operatorname{cont}_W\eta(0)\). Then
   \[
   v_p(d_1(0))+\mu=\tau+b,
   \qquad m=v_p(g(0))+\mu.
   \]
   Writing \(g=d_1\rho\) gives the asserted equality, with \(e=v_p(\rho(0))\ge0\). Neither pseudo-isomorphism nor a Smith form over the two-dimensional ring \(R\) has been used.

All five steps survive the indicated edge cases. No BSD leading-term formula, main-conjecture equality, height nondegeneracy conjecture, or assumption \(e=0\) is needed for this algebra.

## 3. Invariance and the primitive target

The target must be the integral module \(H/H_{\mathrm{tors}}\), with a generator of this module. A generator of a proper finite-index sublattice is not a primitive basis. Rational comparison alone cannot authenticate the value of \(b\).

- Changing the basis of \(M\) by \(\eta'=h\eta\), \(h\in R^\times\), gives \(d'=d/h\), \(g'=g/h\), and \(d_1'=d_1/h\). Thus \(\rho'=\rho\) for this change. A unit ambiguity in the determinant generator changes \(\rho\) by a unit and preserves \(e\).
- For constant row and column changes \(D'=PDQ\), the maximal-minor vector transforms by \(\det(P)\det(Q)Q^{-1}\). This is a unit times an invertible vector transformation, so its content is unchanged. The induced maps on \(W\) and \(H_{\mathrm{tf}}\) are integral isomorphisms; they preserve \(m\), \(\tau\), and \(b\).
- The same assertion holds for actual invertible \(U\)-dependent basis changes. Differentiating \(P(U)D(U)Q(U)\) introduces terms involving \(D_0\); on \(W\), one vanishes and the other is zero in the cokernel. Thus the induced Bockstein is unchanged up to the maps at \(U=0\). Since \(\Delta(0)=0\), extra first derivatives of the vector transformation do not affect \([U]\Delta\).
- An augmentation parameter change \(U'=aU+O(U^2)\), \(a\in A^\times\), rescales the first derivative and divided augmentation by units and preserves all contents. Replacing the parameter by \(pU\) is not such a coordinate change.
- Adding an integral contractible summand \([R\xrightarrow{1}R]\) preserves these invariants. An isomorphism only after inverting \(p\) does not provide the same guarantee.

Multiplying a numerical row by \(p\) raises its apparent content by one. Without the integral comparison to the actual primitive target, subtracting that extra one from \(m-w\) can produce a false certificate. The submitted warning at `PROOF.md` line 266 is mathematically necessary.

## 4. A sharper interpretation of the finite specialization defect

The proof permits a useful intrinsic interpretation of \(\mu\). Expanding \(D(U)\eta(U)=0\) to first order gives

\[
D_0\eta_1+D_1\eta_0=0,
\]

so \(\eta_0\in\ker\overline\beta\). Because \(\overline\beta\ne0\), its kernel is a saturated rank-one direct summand of \(W\). If \(k\) is a primitive generator, then \(\eta_0=u p^\mu k\) for a unit \(u\). Therefore

\[
\mu=\operatorname{length}_A\bigl(\ker\overline\beta/A\eta_0\bigr).
\]

The specialization exact sequence gives

\[
0\longrightarrow M/UM\longrightarrow W\longrightarrow X[U]\longrightarrow0.
\]

It follows that \(X[U]\simeq A\oplus A/p^\mu A\) as an \(A\)-module, noncanonically. Thus \(\mu\) is the length of its finite \(A\)-torsion part. It is not the length of every finite \(R\)-submodule of \(X\), and should not be described as such. This interpretation makes precise why characteristic ideals alone cannot discard the specialization error.

The submitted family with \(P=p^a\) has

\[
\eta_0=P^2e_3,\quad \mu=2a,\quad \tau=2a,
\quad d_1=p^b,\quad \overline\beta=(0,p^b).
\]

Hence \(m=2a+b+e\) and the corrected torsion bound is \(2a+e\). The finite pair remains visible even for \(e=0\). The description of this family in §7 is correct.

## 5. Adversarial edge controls

These are exact desk calculations, not executed seed computations.

| Control | Calculation | Consequence |
|---|---|---|
| Smallest size | \(n=1\), \(D=(0,p^bU)\), \(\eta=(1,0)\), \(g=p^{b+e}\) | \(\tau=0\), \(b=b\), \(m=b+e\); the empty Smith product causes no failure. |
| Zero first Bockstein | \(D=(0,U^2)\), \(z=U\eta\) | The row is zero, but \(d=U^2\nmid U\). Such a nonzero first divided derivative is incompatible with the required inequality. This does not produce a counterexample under the hypotheses. |
| Omit \((p)\) | Submitted family with \(a=1,b=2,g=1\) | \(m=2,\tau=2,b=2\); the false bound \(\tau\le0\) comes precisely from omitted \((p)\)-divisibility. |
| Omit a different height-one prime | \(n=1\), \(D=(0,U(U+p^k))\), \(\eta=(1,0)\), \(g=1\), \(k\ge1\) | \(m=\tau=0\), \(b=k\). The inequalities hold at both \((U)\) and \((p)\), but fail at \((U+p^k)\). The false corrected bound is negative. Thus checking only \((U)\) and \((p)\) is insufficient. |
| Positive defect without a \((p)\)-valuation gap | \(D=(0,U)\), \(\eta=(1,0)\), \(g=U+p^k\) | The hypotheses hold and \(e=k\), although the valuations of both characteristic generators at \((p)\) are zero. The defect records augmentation of the full quotient, not merely a missing power of \(p\) in an Iwasawa characteristic factor. |
| Arbitrarily large finite pair | Submitted family with \(a\ge1,e=0\) | Corrected bound remains \(2a\). A finite specialization pair is not removed by the Bockstein correction. |
| Zero derivative residues | All coordinates known to be zero only modulo \(p^N\) | This establishes a lower bound on derivative content, not nonvanishing or a finite upper bound. No certificate follows at that precision. |

In particular, the all-height-one hypothesis is essential in its full stated form. A residue checker cannot authenticate it.

## 6. Arithmetic passage and what the refinement buys

Conditional on the old return's exact sequence

\[
0\to\Sha[p^\infty]^\vee\to H^2_S
\to A\oplus A/p^wA\to0
\]

with finite left term, the torsion-length identity \(\tau=\operatorname{length}\Sha[p^\infty]+w\) is algebraically correct. A lift of a torsion element of the quotient is torsion because a multiple lands in the finite kernel. Therefore the induced sequence on torsion is exact and lengths add. This checks the terminal module-theoretic step of old §5; it does not recertify its Poitou–Tate, local Kummer, or source-matching premises.

Set \(L=\operatorname{length}\Sha[p^\infty]\) and \(t=m-w-b\). The new statement is exactly

\[
t=L+e,\qquad L\ge0,\quad e\ge0.
\]

After primary finiteness, alternating parity makes \(L\) even. Thus \(0\le t\le1\) forces \(L=0\). Nothing in this argument assumes \(e=0\). Conversely, \(L=0\) permits arbitrary \(e\), so the criterion is not necessary. For instance, the abstract model \(D=(0,U)\), \(g=p^2\) has \(\tau=b=0\) and \(m=2\).

The threshold 1 cannot be raised using only nonnegativity and evenness: the finite-pair control with \(a=1,e=0\) gives corrected bound 2 and permits a nonzero even-length torsion group. This is an algebraic sharpness assertion, not an elliptic-curve realization.

There is also a useful exact description of the missing equality. Since \(\rho\in A[[U]]\),

\[
e=0\ \Longleftrightarrow\ \rho(0)\in A^\times
\ \Longleftrightarrow\ \rho\in R^\times
\ \Longleftrightarrow\ (Ug)=(d).
\]

Thus zero defect is equivalent, in this algebraic setting and for this specified class, to equality of the two characteristic ideals. Finite specialization contributions can still remain when this equality holds. No such equality is established by the corrected certificate.

The new \(b\) is defined from the complex independently of the Kato class and independently of Sha. Using it is not circular. However, deriving a supposed numerical \(b\) by rearranging the desired Sha formula would not constitute an independent computation of the Bockstein row.

## 7. Practical finite-precision consequence

Once \(m\) has been detected exactly from a nonzero derivative residue, lower bounds \(w\ge w_0\) and \(b\ge b_0\) suffice. The arithmetic target is

\[
0\le m-w_0-b_0\le1.
\]

Equivalently, it is enough to certify \(w_0+b_0\ge m-1\), with a consistency check that the sum does not exceed \(m\). There is no need to compute exact values of both correction terms or to prove that they are units. A priori upper control \(m\le M\) would also suffice if nonvanishing is separately established and \(M-w_0-b_0\le1\).

Two zero Bockstein residues modulo \(p^N\), in an authenticated primitive target, legitimately give \(b\ge N\). They do not prove that the Bockstein is zero; the theorem already forces it to be nonzero under the retained hypotheses. A negative resulting bound is evidence that the packet's values or hypotheses are incompatible and must be rejected.

This changes the shape of a future certificate. It does not supply the derivative, its upper bound, the primitive-target comparison, or a cofinite control theorem.

## 8. Disposition ledger

| Status | Finding |
|---|---|
| REMOVED within this audit | The concern that the Bockstein factor can only be subtracted after proving a main-conjecture equality. The explicit nonnegative defect proves the one-sided refinement without that equality. |
| REMOVED within this audit | The concern that the maximal-minor calculation silently discards the nonprimitive augmented kernel vector or finite specialization pair. Both remain in the exact identities. |
| EXCLUDED | Subtracting content of a rationally compared or nonprimitively normalized numerical height row without integral target matching. |
| EXCLUDED | Replacing the all-height-one input by its \((U)\)-local version, by its \((p)\)-local version, or even by those two conditions together. |
| OPEN | Authentication of the retained arithmetic source, exact complex, saturated point lattice, local correction, and any numerical Bockstein realization. |
| OPEN | Any independent bound on the actual corrected quantity at a new seed prime or cofinitely many primes. |
| UNCHANGED | FIN, ORDER9, Q36, and the previously outstanding exceptional-primary obligations. |

No proof repair is required for the algebra as written. A minor editorial clarification would replace “the integer inside the floor” at submitted `PROOF.md` line 232 by “the integer numerator inside the floor”: the quotient by 2 can be a half-integer. This does not affect the deduction.
