# Primitive target and corrected ordinary source gap

Date: 2026-10-12.

**Disposition: TARGET_LATTICE_DEDUCTION_ACCEPTED; ORDINARY_GAP_IDENTITY_DERIVED_UNDER_MATCHED_HEIGHT_COMPARISON.**

This addendum independently checks the new target-lattice deduction proposed during review. It complements `ALGEBRA_AUDIT.md`. It does not evaluate a seed Kato coefficient, regulator, Bockstein row, or primary component.

The source-facing assumptions are the retained duality and local Kummer sequence from the October 7 `CONTENT_BOUND_PROOF.md` §5, together with the exact rational Bockstein/Poitou–Tate/height comparison being separately reviewed against BKS Lemma 5.8. Here the latter is an explicit assumption of the algebra check. The existing `context/RUBIN_COMPARISON.md` was read directly: line 19 fixes the height in the \(U\)-coordinate, lines 39–47 give the nonzero/zero derivative case split, and lines 51–59 give the matrix Rubin identity and ordinary prefactor.

## 1. The primitive target introduces no further index

Put \(A=\mathbf Z_p\), let \(W=A P_1\oplus A P_2\) be the actual augmented point lattice after primary finiteness, and write

\[
\ell=(\log_\omega P_1,\log_\omega P_2)^t,\qquad
L=\ell^t/p=p^wL_{\rm prim},
\]

where \(L_{\rm prim}:W\to A\) is primitive and surjective. The transpose distinguishes the covector from its coordinate column. Non-anomalous local normalization is part of the retained arithmetic interface.

Dualizing the global-to-local point map gives

\[
K_{\rm MW}^{\vee}=W^*/A L.
\]

Its torsion is precisely \(A L_{\rm prim}/A L\), of length \(w\). Consequently

\[
(K_{\rm MW}^{\vee})_{\rm tf}=W^*/A L_{\rm prim}
\xrightarrow[\text{restriction}]{\sim}
\operatorname{Hom}_A(\ker L_{\rm prim},A).
\]

The restriction map is onto because \(\ker L_{\rm prim}\) is a direct summand; its kernel is exactly \(A L_{\rm prim}\). There is no further determinant or saturation index in this identification.

The retained exact sequence

\[
0\to\Sha[p^\infty]^\vee\to H^2_S\to K_{\rm MW}^\vee\to0
\]

has finite kernel once \(\delta\ne0\). It induces an isomorphism on torsion-free quotients. Indeed, the inverse image of the torsion of the quotient is exactly the torsion of \(H^2_S\): a multiple of any such lift lies in the finite kernel. Therefore the preceding primitive lattice is the actual \((H^2_S)_{\rm tf}\), not merely a rationally isomorphic line.

Choose

\[
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
q_{\rm fine}=J\ell/p^{1+w}.
\]

Then \(q_{\rm fine}\) is a primitive generator of \(\ker L_{\rm prim}\). Its sign is immaterial for valuations. Evaluation at this generator identifies \(\operatorname{Hom}_A(\ker L_{\rm prim},A)\) with \(A\).

## 2. Exact height comparison yields the Bockstein content

Let \(H=(h(P_i,P_j))\) be the symmetric height matrix, with its entries expressed in the same \(U\)-basis of \(I/I^2\) used to define the first Bockstein. Suppose the exact rational height/Bockstein comparison identifies \(\overline\beta(x)\), in the preceding integral target embedded in its rationalization, with the functional

\[
q\longmapsto h(x,q)\quad(q\in\ker L_{\rm prim}).
\]

Then the two coefficients of the actual integral Bockstein row are \(h(P_i,q_{\rm fine})\). In column notation they are

\[
Hq_{\rm fine}=HJ\ell/p^{1+w}
=J\operatorname{adj}(H)\ell/p^{1+w},
\]

because \(HJ=J\operatorname{adj}(H)\) for a symmetric two-by-two matrix. As \(J\) is unimodular, if

\[
c=\min_i v_p((\operatorname{adj}(H)\ell)_i),
\]

then

\[
\boxed{b=c-1-w.}
\]

The subtraction of \(1+w\) is exactly the passage from the raw logarithm vector to the primitive fine direction. No further lattice index is missing. Under the retained hypotheses the Bockstein is nonzero and integral, so this expression must be a finite nonnegative integer. A negative or nonintegral value in a proposed ordinary numerical packet signals incompatible data or normalizations.

A purely rational equality with an unspecified nonunit scalar is insufficient: its valuation would enter the formula for \(b\). The needed comparison is exact, or at least up to a verified \(p\)-adic unit, relative to the stated cohomological target identification. Numerical height software is not authenticated by this algebra.

## 3. The corrected gap and its hypotheses

In the retained Rubin comparison, put \(K=K_\rho\), \(\epsilon=\epsilon_\rho\), and \(r=v_p(\det H)\). For \(K\ne0\) and \(\det H\ne0\), that comparison gives

\[
m=v_p(K)+v_p(\epsilon)+c-r.
\]

Using the same \(H\), unscaled \(\ell\), \(U\)-coordinate, and actual transported class in both comparisons, the correction cancels exactly:

\[
\boxed{m-w-b=v_p(K)+v_p(\epsilon)+1-r.}
\]

At a retained non-anomalous ordinary prime, \(v_p(\epsilon)=-1\), so

\[
\boxed{m-w-b=v_p(K)-v_p(\det H).}
\]

Combining with the reviewed algebraic decomposition yields

\[
\boxed{v_p(K)-v_p(\det H)
=\operatorname{length}_A\Sha[p^\infty]+e,\qquad e\ge0.}
\]

This does not assert \(e=0\). It proves, under the matched arithmetic interfaces, the sufficient ordinary criterion

\[
K\ne0,\quad\det H\ne0,\quad
0\le v_p(K)-v_p(\det H)\le1
\quad\Longrightarrow\quad\Sha[p^\infty]=0.
\]

The existing implication \(\delta=0\Rightarrow K=0\) supplies \(\delta\ne0\) from \(K\ne0\) before invoking the finite-Sha target identification. Thus the ordering does not presume primary finiteness. It must use that established case split, not an argument that applies a finiteness-hypothesized formula before knowing the hypothesis.

The nonsingularity of \(H\) is needed for this source-gap expression and the existing inverse-matrix content formula. It is not a new requirement of the original corrected Bockstein certificate. The additive constant 1 before ordinary cancellation comes from the local \(pA\) point lattice; it must not be dropped when changing normalization or considering another prefactor.

This isolates a sharper arithmetic target: upper control of the actual source coefficient relative to the determinant of the correctly normalized height. It neither supplies that upper control nor identifies an arbitrary stored numerical height matrix with \(H\). FIN, ORDER9, Q36, and all exceptional-prime obligations remain unchanged.
