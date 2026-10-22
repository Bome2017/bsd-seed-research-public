# Full-ray integration by parts and secondary descent

**SECONDARY_CLASS_OBSTRUCTED.**

The integration by parts and descent modulo exact **one-forms** work. They do not give a relative de Rham class or a holomorphic Deligne-regulator class with connection. The exact defect is nonzero curvature. A weaker object does exist: a topologically trivial, nonflat smooth complex line bundle with connection on the punctured modular curve. It is specified below rather than incorrectly excluded. It does not extend as a smooth connection across the cusps, and cannot be the pullback of a smooth connection on the elliptic quotient, even up to gauge.

The verdict concerns the proposed relative/regulator interpretation on \(X_0(N)\), not the false blanket assertion that no smooth differential-cohomology object can be associated to a nonclosed form. Arbitrarily enlarged singular-current theories are not ruled out.

## 1. Objects and collision check

Let \(X=X_0(N)(\mathbf C)\), let \(S\) be its cusps, and put \(U=X\setminus S\). All computations can be made on a torsion-free cover and descended, or directly on orbifold charts. Set
\[
\alpha=\alpha_f=2\pi i f(z)\,dz,\qquad
J(z)=\mathcal E_{\rm mid}''(z,0),\qquad
L(z)=\log(\sqrt N\,y).
\]
The [Green-kernel calculation](MIDPOINT_GREEN_KERNEL_TEST.md) proves that \(J=L^2+R_{\rm mid}\) is real, smooth on \(\mathbb H\), and automorphic. On the imaginary axis it is even in \(x\), and it has the exact differentiated Eisenstein identity used below. The earlier [trace calculation](MIDPOINT_UP_TRACE_TEST.md) had only a truncated integration-by-parts formula with an interior endpoint. Master §5.7 records nonclosure of weighted forms, but no full-ray Čech/connection and cusp-extension test.

This operation uses a nonholomorphic \(J\), so the holomorphic finite-algebraic-frame hypotheses of [L3](/Users/bsm/BSD_CODEX6_ARITHMETIC_LOGARITHMIC_REALIZATION_2026-09-19/EXACT_CORRECTION_OBSTRUCTION.md) do not apply directly. This is a scope distinction, not an arithmeticity result. The ordinary elliptic-homology obstruction [M4](/Users/bsm/BSD_CODEX6_COMMON_B_ARITHMETICITY_ATTACK_2026-09-19/MELLIN_JET_THEOREM.md) remains applicable to any flat, homotopy-invariant interpretation on the unpunctured elliptic curve.

## 2. The primitive and both endpoint terms

On the simply connected upper half-plane define
\[
\Phi(z)=\int_{i\infty}^{z}\alpha
=\sum_{n\ge1}\frac{a_n}{n}e^{2\pi inz}.
\tag{1}
\]
Local uniform convergence proves \(d\Phi=\alpha\). The normalization gives \(\Phi(i\infty)=0\). The Mellin formula, initially in its convergence region and continued using the cusp decay at both ends, gives
\[
\Phi(0)=2\pi\int_0^\infty f(iy)\,dy=L(f,1)=0.
\tag{2}
\]
The limit here is the cusp limit in a cusp chart; it is not an unqualified termwise evaluation of (1) at \(q=1\).

There is also direct control of the rate at zero. Since \(W_N^*\alpha=-\alpha\),
\(\Phi(W_Nz)+\Phi(z)\) is constant. Evaluating at the cusps and using (2) shows
\[
\Phi(W_Nz)=-\Phi(z).
\tag{3}
\]
Consequently \(\Phi(iy)=O(e^{-2\pi y})\) at infinity and
\(\Phi(iy)=O(e^{-2\pi/(Ny)})\) at zero. The previous Fourier expansion and Fricke symmetry give
\(J(iy)=\log^2(\sqrt Ny)+\text{exponentially small remainder}\)
at both ends, with the corresponding differentiated estimates. Thus
\[
\lim_{y\to\infty}\Phi(iy)J(iy)=
\lim_{y\to0}\Phi(iy)J(iy)=0.
\tag{4}
\]
Both integrals in the following formula converge absolutely. First apply integration by parts on a compact segment, then use (4):
\[
\boxed{\int_{i\infty}^{0}\alpha J
=-\int_{i\infty}^{0}\Phi\,dJ.}
\tag{5}
\]

For signs and constants, on the downward ray \(\alpha=-2\pi f(iy)\,dy\).
Evenness in \(x\) gives
\[
\mathscr D_zJ(iy)=-\frac1{4\pi}\partial_yJ(iy),
\qquad \mathscr D_z=(2\pi i)^{-1}\partial_z.
\]
Therefore, with \(I_J=\int_{i\infty}^{0}\alpha J\),
\[
\boxed{\begin{aligned}
I_J&=2\pi\int_0^\infty f(iy)J(iy)\,dy\\
&=-4\pi\int_0^\infty\Phi(iy)\mathscr D_zJ(iy)\,dy\\
&=-2\pi\sum_{d\in\mathcal O}d\int_0^\infty\Phi(iy)
\left[b_d\mathsf E_2'(diy,1)
+(\kappa b_d+e_d)\mathsf E_2(diy,1)\right]dy.
\end{aligned}}
\tag{6}
\]
All notation and normalizations on the last line are those of the Green-kernel report. Individual summands there have at most polynomial/logarithmic growth at the cusps by the level-one transformation law; the exponential decay of \(\Phi\) proves convergence. The sum over \(d\) is finite. No Fourier sum at zero is interchanged with an integral.

The earlier full-ray identities also give \(I_J=L''(f,1)+2\Delta_{\rm mid}\). Formula (6) evaluates neither term; it is an exact analytic rewrite with no endpoint correction.

## 3. What the period cocycle actually descends

For \(\gamma\in\Gamma_0(N)\), invariance of \(\alpha\) proves
\[
\Phi(\gamma z)-\Phi(z)=\lambda_\gamma,\qquad
\lambda_{\gamma\delta}=\lambda_\gamma+\lambda_\delta.
\]
Since \(J\) is invariant, \(\beta=\Phi\,dJ\) satisfies exactly
\[
\boxed{\gamma^*\beta-\beta=d(\lambda_\gamma J).}
\tag{7}
\]
On a cover of \(U\), choose local primitives \(\Phi_i\) with
\(\Phi_j-\Phi_i=\lambda_{ij}\). Put
\[
\beta_i=\Phi_i dJ,\quad r_{ij}=\lambda_{ij}J,\quad h_i=\Phi_iJ.
\]
Then \(\beta_j-\beta_i=dr_{ij}\), \(r_{ij}+r_{jk}+r_{ki}=0\), and
\[
\boxed{\beta_i-dh_i=-J\alpha=:A,\qquad
r_{ij}=h_j-h_i.}
\tag{8}
\]
Thus the exact-form descent is real and explicit: its global representative is \(A=-J\alpha\). It has not produced a new independent differential. Along the specified ray the change of representative has zero boundary contribution by (4).

For a de Rham cocycle the Čech equations must be supplemented by closedness. Here
\[
\boxed{d\beta_i=dA=\alpha\wedge dJ=:F\ne0.}
\tag{9}
\]
To prove nonvanishing, write
\(F=2\pi i f(z)\partial_{\bar z}J\,dz\wedge d\bar z\).
The cusp expansion shows that the real function \(J\) is nonconstant. If
\(\partial_{\bar z}J\) vanished identically, it would be a real holomorphic function and therefore constant. Since \(f\) is nonzero, with isolated zeros, the product is not identically zero.

Adding an exact form does not change (9). Passing to relative cohomology with cusp endpoints changes boundary data, not the requirement of interior closedness. It cannot remove this defect. Also, \(dJ\) itself **is closed**: the nonclosed form is \(\Phi dJ\), not \(dJ\).

The direct curvature-cancelling combination \(\Phi dJ+J\alpha=d(\Phi J)\) is a Čech coboundary. With the endpoint normalization (4), its relative integral is zero. It does not preserve the desired weighted integral while creating a nontrivial cohomology class.

## 4. Smooth differential cohomology versus a regulator class

Nonzero curvature does not forbid all secondary classes. Indeed take transition functions
\(g_{ij}=\exp(r_{ij})\) and local connection forms \(\beta_i\). Equation (7) is precisely the connection gluing law, and the triple products of \(g_{ij}\) equal one. The gauge change \(\exp(-h_i)\) makes the transitions trivial and the connection form global:
\[
\boxed{\nabla=d+A=d-J\alpha\quad\text{on the trivial complex line over }U.}
\tag{10}
\]
This gives a genuine smooth complex-line differential-cohomology class, using explicitly the complex
\(\mathcal C^\infty(\mathbf C^*)\xrightarrow{d\log}\mathcal A^1_{\mathbf C}\).
It is the complex-connection version of the smooth Deligne construction. Its curvature is (9), so the connection class is not gauge-equivalent to the zero connection. The construction is available for any smooth global \(J\); its existence alone is not arithmetic information.

The relevant distinctions are exact:

* It is not an ordinary absolute or relative de Rham class of degree one, by (9).
* It is not a holomorphic line bundle **with holomorphic connection** representing the corresponding degree-two, weight-two holomorphic Deligne class. On a complex curve every such connection is flat, whereas (9) is gauge-invariant and nonzero.
* Forgetting the connection in (10) gives the trivial holomorphic line bundle: \(A\) has type \((1,0)\), so its \((0,1)\)-operator is the usual \(\bar\partial\). The resulting weight-one Picard/Deligne class is zero, not a new arithmetic divisor. The chosen endpoint frames agree with the trivial frame because \(\Phi J\to0\).

These distinctions are definitional, not an inference that all nonflat connections are arithmetically useless. Smooth Deligne connections and holomorphic/Deligne–Beilinson regulator targets are different categories. The latter cannot be replaced by the former without a new comparison. No such comparison is assumed or obtained here.

## 5. Cusps and the one permitted elliptic-descent test

The endpoint integrals exist, but regular extension of the connection is a stronger requirement. At the width-one cusp \(\infty\), use \(q=e^{2\pi iz}\), \(r=|q|\). Then
\[
\alpha=(1+O(q))\,dq,
\quad y=-\frac{\log r}{2\pi},
\quad J=\log^2(\sqrt Ny)+O(r^{4547}).
\]
The known Fourier expansion gives \(\partial_{\bar q}R_{\rm mid}=O(r^{4546})\). Consequently
\[
\boxed{
F=\left[-\frac{\log(\sqrt Ny)}{2\pi y\,\bar q}(1+O(q))
+O(r^{4546})\right]dq\wedge d\bar q.}
\tag{11}
\]
Its coefficient has size asymptotic to
\(\log\log(1/r)/(r\log(1/r))\), which is unbounded. This is a locally integrable density, not a delta mass. Thus (10) has no smooth extension over the compact curve \(X\), even after gauge change: curvature is unchanged by gauge.

This is consistent with (4). In the local primitive satisfying \(\Phi(\infty)=0\), \(\Phi=q+O(q^2)\), and \(\beta=\Phi dJ\) has coefficients tending to zero at the cusp. It admits endpoint integration and a continuous local extension, but its curvature is not smooth. Integrability, continuous endpoint framing, and a smooth Deligne class on the compactification must not be conflated. Fricke gives the same conclusion at the other endpoint.

Now let \(\pi:X\to E\) be the modular parametrization with
\(\pi^*\omega_E=c_E\alpha\), \(c_E\ne0\), and \(\pi(\infty)=O\). In an elliptic logarithm coordinate \(w\) at \(O\),
\[
w\circ\pi=c_E\Phi=c_Eq+O(q^2).
\tag{12}
\]
So \(\pi\) is unramified at this cusp. If (10), up to gauge, were pulled back from a smooth connection on \(E\), its curvature would be the pullback of a smooth two-form, bounded in the \(q\)-coordinate. Equation (11) contradicts this. This also excludes the usual smooth biextension-connection interpretation on the unpunctured elliptic curve. No Néron–Tate interpretation follows.

The statement is scoped: it does not classify artificially singular connections on \(E\setminus\{O\}\) with additional prescribed log-log behavior, nor prove or disprove arbitrary fiberwise identities for such singular objects. No such object was constructed. Under the regularity required for a connection on \(E\), the surviving open-curve class fails the requested elliptic-descent test.

Finally, \(\pi(0)=\pi(\infty)=O\) and (2) show that the full image path has lift with displacement zero; it is null-homotopic in \(E(\mathbf C)\). A flat homotopy-invariant interpretation would give trivial holonomy. A nonflat connection can have nontrivial holonomy on a contractible loop through its curvature. Thus this null-homotopy does not force the analytic integral in (5) to vanish. It also does not establish a height interpretation. This is exactly consistent with M4.

## 6. Outcome and scope

The exact full-ray identity (6) has zero endpoint correction. The period cocycle descends modulo exact forms to \(-J\alpha\), and therefore produces the explicit nonflat smooth connection (10) on \(U\). The first obstruction to the proposed relative/regulator class is (9); the separate regular elliptic-descent obstruction is (11).

**SECONDARY_CLASS_OBSTRUCTED** means the proposed relative de Rham/holomorphic Deligne-regulator class on the compact modular curve is not obtained by this construction modulo exact forms. It does not mean that its weaker smooth differential-cohomology class on \(U\) fails to exist. No arithmetic cycle, regulator comparison, value or nonvanishing of \(\Delta_{\rm mid}\), numerical period calculation, or successor is claimed.

Only two external definition checks were made, not a theorem survey:

* [Hamm, Line bundles, connections, Deligne–Beilinson and absolute Hodge cohomology](https://arxiv.org/abs/1501.04048), opening definition and Theorem 0.1, distinguishing holomorphic line bundles and connections from their smooth counterparts. [Bound PDF](../sources/midpoint_secondary_descent/HAMM_DELINE_LINE_CONNECTIONS_1501.04048.pdf).
* [Gomi, Equivariant smooth Deligne cohomology](https://arxiv.org/abs/math/0307373), §2.1 and Definition 2.1, for the smooth Deligne complex; our complex-valued gluing is proved directly in (7)–(10). [Bound PDF](../sources/midpoint_secondary_descent/GOMI_SMOOTH_DELIGNE_0307373.pdf).

The proof grade is a written analytic and cohomological derivation with explicit categories and imported project inputs. It is not an independent referee review or formal proof.
