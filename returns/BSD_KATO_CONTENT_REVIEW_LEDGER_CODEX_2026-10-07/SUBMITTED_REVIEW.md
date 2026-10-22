# User-supplied review of the Kato derivative-content bound

Provenance: formal review portion of the user's message received 2026-10-07. Mathematical display formatting has been normalized for readability. First-person source-reading and verification statements below belong to the supplied reviewer, not to this ledger's author. No separately downloadable review was supplied in this turn.

---

Date: 2026-10-07

Reviewed return: Bome2017/bsd-seed-lab, commit c194a996a627e5bdff5c237e43f9f4c2300b7ecf, directory work/returns/BSD_KATO_CONTENT_BOUND_CODEX_2026-10-07/.

Verdict: **NEW_LENGTH_ARGUMENT_SUPPORTED_UNDER_RETAINED_INPUTS.**

This is a desk review of the new maximal-minor and global-duality deduction, not a formal certificate, a novelty assessment, or a new audit of all antecedent seed and Kato inputs. No derivative coefficient was computed. No prime is newly settled.

## 1. Exact statement and hypotheses

Let

\[
D=\{p\ge5:p\nmid N,\ p\notin\{19,59,487\}\}.
\]

The actual source must also satisfy the previously imposed smoothing and simultaneous lattice/class-transport conditions. A cofinite normalization statement does not establish its normalization at a specific prime without further checking.

Retain the preceding integral Kato inequality at every height-one prime of R=Z_p[[U]], the two-term finite-free representative of full S-cohomology, the saturated point basis, local torsion vanishings, and the implication that a nonzero divided derivative gives primary finiteness and rational global cohomology of dimension two.

For the specified nonzero class

\[
\delta_p=A_p\kappa(P_1)+B_p\kappa(P_2),
\]

write

\[
m_p=\min(v_p(A_p),v_p(B_p)),\qquad
w_p=\min_i v_p(\log_\omega(P_i)/p).
\]

The reviewed deduction establishes

\[
\operatorname{length}_{\mathbf Z_p}\Sha(E/\mathbf Q)[p^\infty]+w_p\le m_p.
\]

The nonzero hypothesis is essential. Setting the content of the zero vector to infinity does not supply primary finiteness or a usable finite bound.

## 2. The maximal-minor argument

Use the actual presentation

\[
[R^{n+1}\xrightarrow{D(U)}R^n],\qquad
\ker D=R\eta,\quad X=\operatorname{coker}D.
\]

The coordinates of the kernel generator have no common irreducible divisor: otherwise division by that divisor would give an integral kernel vector contradicting its being an R-basis. This is a height-one primitivity assertion, not an assertion that one coordinate is a unit at the maximal ideal.

For the signed maximal-minor vector Delta, the kernel identity gives

\[
\Delta=d\eta.
\]

At a height-one localization, the content of these actual minors is the length of the localized cokernel. Thus d generates the characteristic ideal there, while eta retains information not determined by that characteristic ideal.

Write y=g eta and z=Ug eta. The integral inequality implies

\[
d\mid Ug.
\]

Nonzero augmentation gives g(0) nonzero, eta(0) nonzero, and the retained rank consequence gives rank D(0)=n-1. Therefore all maximal minors vanish at zero, so

\[
d=Ud_1,\qquad d_1\mid g,\qquad d_1(0)\ne0,
\]

and

\[
[U]\Delta=d_1(0)\eta(0).
\]

Smith reduction is performed only on D(0) over Z_p. If its nonzero diagonal entries are s_1,...,s_(n-1), then every first derivative of a maximal minor is divisible by their product: the one zero row must supply the differentiated entry, and all other rows supply their constant pivots.

Writing tau=sum_i v_p(s_i) and mu=min_j v_p(eta_j(0)), this proves

\[
\tau\le v_p(d_1(0))+\mu\le v_p(g(0))+\mu=m_p.
\]

The last equality uses saturation of the kernel of D(0) in its free source and, in the nonzero-derivative branch, its identification with the full Mordell–Weil lattice. Consequently

\[
\operatorname{length}(H^2_S)_{\mathrm{tors}}\le m_p.
\]

No Smith normal form over the two-dimensional ring R is invoked. The term mu is not discarded.

## 3. Global duality and the local correction

Let F denote the fine Selmer group with discrete coefficients E[p^infinity], using the stated finite ramification set. Finite-S Poitou–Tate duality, together with compatible limits and Weil self-duality, gives

\[
0\longrightarrow F^\vee\longrightarrow H^2_S
\longrightarrow\bigoplus_{v\in S}H^2(\mathbf Q_v,T_pE).
\]

On the retained domain the local terms vanish, yielding F^vee isomorphic to H^2_S. This step requires the retained local hypotheses; it is not valid as an unconditional identity for arbitrary primes.

The discrete local Kummer image away from p is zero. At p the non-anomalous good-reduction hypothesis identifies the completed local point lattice with pZ_p. The global point localization is the nonzero row

\[
(\log(P_1)/p,\log(P_2)/p):
(\mathbf Q_p/\mathbf Z_p)^2\longrightarrow\mathbf Q_p/\mathbf Z_p.
\]

It is surjective even when its two coefficients are divisible by p: multiplication by a nonzero p-adic integer is surjective on this divisible group. Its kernel is noncanonically

\[
K_{\mathrm{MW}}\simeq\mathbf Q_p/\mathbf Z_p\oplus\mathbf Z/p^{w_p}\mathbf Z.
\]

Subtracting a suitable point class removes the p-localization of any classical Selmer class, giving

\[
0\longrightarrow K_{\mathrm{MW}}\longrightarrow F
\longrightarrow\Sha[p^\infty]\longrightarrow0.
\]

Primary finiteness is already a consequence of the nonzero derivative. Dualizing and taking torsion therefore gives the equality

\[
\operatorname{length}(H^2_S)_{\mathrm{tors}}
=\operatorname{length}\Sha[p^\infty]+w_p.
\]

The torsion map is onto the finite summand of K_MW^vee: a lift of a torsion element has a multiple in the finite kernel, and hence is itself torsion. This checks the exact positive sign and coefficient of the local correction.

## 4. Parity and the revised threshold

Milne’s cited exposition states the Cassels–Tate pairing with divisible kernels and alternation for a polarization arising from a rational divisor. The elliptic identity divisor supplies this polarization. Once the particular p-primary component is finite, its induced pairing is perfect alternating. Its Z_p-length is therefore even; finiteness of the entire Sha group is not required for this step.

Putting g_p=m_p-w_p, the conditional bound becomes

\[
0\le\operatorname{length}\Sha[p^\infty]
\le2\left\lfloor\frac{g_p}{2}\right\rfloor.
\]

In particular g_p<=1 forces primary vanishing. This is genuinely less restrictive than demanding that the actual derivative be primitive. It does not justify dividing the source class by p or asserting a converse.

At 17 the retained matched calibration gives w_17=0 and m_17=v_17(K_17)-1. Thus either valuation 1 or valuation 2 suffices. Equivalently, when the stated integral and convention matching has been proved at 17, a coefficient divisible by 17 but nonzero modulo 17^3 passes. No such digit was computed here.

## 5. A separate finite-error control

I checked the following symbolic matrix independently:

\[
D(U)=\begin{pmatrix}p^a&U&0\\0&0&U\end{pmatrix}.
\]

Its signed maximal minors are (U²,-p^a U,0), and its kernel generator is eta=(U,-p^a,0). Hence d=U, while the actual cokernel is

\[
R/(p^a,U)\oplus R/(U).
\]

The finite first summand is invisible to the height-one characteristic ideal but contributes length a to the torsion of the augmented H². The content of eta(0) is also a, exactly where the reviewed proof retains that contribution. Choosing g=1 makes the length inequality an equality in this algebra example.

This is a check on the algebra, not a realization by the seed or a new Selmer computation. The arbitrary exponent is not evidence about the seed’s actual Sha.

## 6. Remaining arithmetic

The remaining sufficient cofinite target is

\[
\delta_p\ne0,\qquad m_p-w_p\le1.
\]

The proof supplies a bound on Sha in terms of actual arithmetic content. It supplies no upper estimate for that content across primes. Supersingular primes remain covered by the cohomological theorem on its stated domain, without an ordinary height formula or a nondegenerate height determinant. Such formulas enter only when translating the content into numerical height/Coleman data.

FIN, ORDER9 and Q36 remain unchanged. This review neither initiates another computation nor recommends an additional candidate-search package.

## Sources and review scope

Read at the pinned commit: REPORT.md, CONTENT_BOUND_PROOF.md, VALUATION_TARGET.md, SOURCES.md. Earlier Kato/source-matching and seed inputs are retained, not recertified.

Freshly opened and visually inspected J.S. Milne, Arithmetic Duality (February 28, 2026), printed p.5 (finite-S global duality), pp.7–8 (Cassels–Tate pairing and alternation). These supply the duality framework; the limit passage, local correction, and minor estimate above are checked as deductions, not attributed as quoted theorems from Milne.

A symbolic calculation verified the matrix, minors, kernel vector and derivative in Section 5. I did not rerun the return’s 288 checks, the height engines, the modular-symbol engine, or any Kato-value computation. This is not machine formalization.
