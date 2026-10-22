# Midpoint residual: bounded Green-kernel identification test

**PARTIAL_KERNEL_MATCH.**

There is an exact analytic identity with the Eisenstein series used by Berndt–Kühn, after one complex derivative. There is no identified arithmetic Green current for the residual itself. The distinction is between the auxiliary modular variable of an arithmetic-cycle generating series and the geometric variables supporting its cycles.

Write
\[
J(z)=\mathcal E_{\rm mid}''(z,0),\quad
L(z)=\log(\sqrt N\,\operatorname{Im}z),\quad
R(z)=R_{\rm mid}(z)=J(z)-L(z)^2,\quad
\mathscr D_z=\frac1{2\pi i}\partial_z.
\]
Use the primitive level-one Eisenstein series \(E(z,s)\) of the existing experiment, and put
\[
E^*(z,s)=Z(s)E(z,s),\qquad
Z(s)=\pi^{-s}\Gamma(s)\zeta(2s),\qquad
\mathsf E_2(z,s)=\mathscr D_zE^*(z,s).
\]
The last two definitions agree with Berndt–Kühn Part II, (2.0.2) and Definition 2.1. A prime on \(\mathsf E_2\) below means \(\partial_s\), not \(\partial_z\).

For the same two middle orbits \(\mathcal O=O_{m,0}\cup O_{m,1}\) and the same coefficients as the [Mellin report](MIDPOINT_GLOBAL_MELLIN_REDUCTION.md),
\[
(b_d,e_d)=
\begin{cases}(-1,3\log2),&d\in O_{m,0},\\
(3/2,-3\log2),&d\in O_{m,1},\end{cases}
\qquad \kappa=\log(4\pi)-\gamma_{\rm E},
\]
the exact match is
\[
\boxed{
\mathscr D_z\bigl(R(z)+L(z)^2\bigr)
=\frac12\sum_{d\in\mathcal O}d\left[
b_d\mathsf E_2'(dz,1)+(\kappa b_d+e_d)\mathsf E_2(dz,1)
\right].}
\tag{1}
\]
Equivalently, add \(L(z)/(2\pi y)\) to the right side to obtain \(\mathscr D_zR(z)\). Every coefficient is independent of \(f\) and of its regulator. Equation (1) is a differential identity, not an equality between \(R\) and arithmetic Green functions.

The scoped collision check used master §5.7 and the three preceding automorphic/midpoint reports. They do not contain (1) or a comparison with these specific Green kernels. No claim of literature novelty is made. No stopped local or Euler-factorization route is reopened.

## 1. Exact exponential-integral normalization

For \(t>0\), the same special function occurs with three notations:
\[
\beta_1(t):=\int_1^\infty e^{-tr}\frac{dr}{r}
=E_1(t)=\Gamma(0,t)=-\operatorname{Ei}(-t).
\tag{2}
\]
Thus each exponential-integral summand of our residual is exactly
\[
\frac{b_dS_n}{n}
e^{2\pi ndy}\beta_1(4\pi ndy)\cos(2\pi ndx),
\qquad S_n=\sigma_1(n).
\tag{3}
\]
In Berndt–Kühn Part I, (2.0.2) and (2.3.2), the geometric kernel is instead
\[
\Xi(v,Z,m)=\frac12\sum_{\det M=m}
\beta_1(2\pi v\,Q(Z,M)),\qquad Z=(z_1,z_2),
\]
\[
Q(Z,M)=\frac{|a-bz_2-cz_1+dz_1z_2|^2}{2y_1y_2},
\qquad M=\begin{pmatrix}a&b\\c&d\end{pmatrix}.
\tag{4}
\]
Here \(v\) is the imaginary part of a separate generating variable \(\tau\). In (3), \(4\pi ndy>0\) everywhere on the upper half-plane. In (4), the argument vanishes on the geometric correspondence. Equating the special functions does not equate these arguments or their lattice sums.

## 2. Term-by-term match, including the zero mode

Put
\[
T_n=\sum_{a\mid n}a\log a,\quad
\delta_n=-\log n+2T_n/S_n,\quad k_n=\kappa+\delta_n.
\]
Berndt–Kühn Part II, Theorem 2.2, gives the following nonconstant coefficients in the convention \(q=e^{2\pi iz}\):
\[
\begin{array}{c|cc}
&q^n\ (n>0)&q^{-n}\ (n>0)\\ \hline
\mathsf E_2(z,1)&S_n&0\\
\mathsf E_2'(z,1)&S_n\bigl(\delta_n+(4\pi ny)^{-1}\bigr)
&S_n\bigl(-E_1(4\pi ny)+e^{-4\pi ny}/(4\pi ny)\bigr).
\end{array}
\tag{5}
\]
The divisor logarithm agrees exactly: differentiating
\(n^\nu\sum_{a\mid n}a^{-2\nu}\) at \(\nu=1/2\), then dividing by its value, gives \(\delta_n\). This follows by replacing \(a\) with \(n/a\).

Here is the direct calculation explaining the match and its limitation. For one summand, let
\[
a=2\pi nd,\quad A=b_dk_n+e_d,\quad
Q_a(y)=e^{ay}E_1(2ay),\quad
h(y)=A e^{-ay}+b_dQ_a(y).
\]
Its contribution to \(R\) is \((S_n/n)h(y)\cos(ax)\). Since
\[
Q_a'(y)=aQ_a(y)-e^{-ay}/y,
\]
the two signed Fourier coefficients after applying \(\mathscr D_z\) are
\[
\frac{S_n}{2n}\frac{a h-h'}{4\pi}
=\frac{dS_n}{2}\left[A+\frac{b_d}{4\pi ndy}\right]e^{-2\pi ndy},
\tag{6}
\]
\[
\frac{S_n}{2n}\frac{-a h-h'}{4\pi}
=\frac{d b_d S_n}{2}
\left[-E_1(4\pi ndy)+\frac{e^{-4\pi ndy}}{4\pi ndy}\right]e^{2\pi ndy}.
\tag{7}
\]
They are exactly (5) with the coefficients in (1). Before differentiation, the positive Fourier mode of \(R\) contains an \(E_1\) term; the positive mode of \(\mathsf E_2'\) does not. The derivative in (1) is essential, not a normalization constant or a finite level trace.

For completeness, the zero coefficients from the same source are
\[
a_0(y)=-\frac1{24}+\frac1{8\pi y},
\]
\[
a'_0(y)=-\frac{24\zeta'(-1)+\gamma_{\rm E}-1+\log(4\pi y)}{24}
-\frac{-\gamma_{\rm E}+\log(4\pi y)}{8\pi y}.
\tag{8}
\]
The already proved incoming/scattered normalizations and complement symmetry imply
\[
\sum_d b_d=8,\quad \sum_d e_d=0,\quad
\sum_d b_d\log d=4\log N,\quad
\sum_d d b_d=0,\quad
\sum_d d(e_d+b_d\log d)=0.
\tag{9}
\]
For the last equality, differentiate the identically zero scattered sum
\(\sum_d v_d(s)(d/\sqrt N)^{1-s}\), using
\(b_d=8v_d(0)\) and \(e_d=-8v'_d(0)\).
Substituting (8) into the right side of (1) and using (9) gives exactly
\[
-\frac{\log(\sqrt N y)}{2\pi y}=\mathscr D_zL^2.
\]
Thus the residual derivative has zero constant term, as required. No constant, logarithmic term, or factor of two was discarded. All differentiated Fourier series converge locally uniformly on the upper half-plane; exponential decay dominates the divisor and logarithmic factors and their fixed derivatives.

An independent normalization check uses the completed functional equation. Write
\(E^*(z,s)=-1/(2s)+A_0(z)+A_1(z)s+O(s^2)\).
Then \(E^*(z,1+s)=1/(2s)+A_0(z)-A_1(z)s+O(s^2)\).
Combining this with \(1/Z(s)=-2s+2\kappa s^2+O(s^3)\) gives
\(\mathscr D_zE'(z,0)=-2\mathsf E_2(z,1)\) and
\(\mathscr D_zE''(z,0)=4\mathsf E'_2(z,1)+4\kappa\mathsf E_2(z,1)\).
Applying the midpoint coefficients proves (1) again; unspecified scalar Laurent terms disappear under \(\mathscr D_z\).

## 3. Differential equation, automorphy, and singularities

Use \(\Delta_0=-y^2(\partial_x^2+\partial_y^2)\), and let
\(H(z)=\mathcal E_{\rm mid}'(z,0)-L(z)\).
The eigenvalue equation
\(\Delta_0\mathcal E_{\rm mid}(z,s)=s(1-s)\mathcal E_{\rm mid}(z,s)\)
and \(\mathcal E_{\rm mid}(z,0)=1\) give
\[
\boxed{\Delta_0R=2H,qquad \Delta_0H=0,qquad \Delta_0^2R=0.}
\tag{10}
\]
Explicitly,
\[
H(z)=-\frac12\sum_{d,n}\frac{b_dS_n}{n}
e^{-2\pi ndy}\cos(2\pi ndx).
\]
Its coefficient at frequency \(p=4547\) is \(\frac12e^{-2\pi py}\), so \(H\ne0\). Hence \(R\) is biharmonic but not harmonic. Directly,
\(Q_a''-a^2Q_a=e^{-ay}/y^2\) verifies (10) mode by mode. There are no interior delta sources.

One important distinction already implicit in the trace report is that \(J\) is automorphic, whereas \(R\) is the constant-term-subtracted remainder. For \(\gamma=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\in\Gamma_0(N)\),
\[
R(\gamma z)-R(z)
=L(z)^2-\bigl(L(z)-2\log|cz+d|\bigr)^2.
\tag{11}
\]
Thus \(R\) itself is not an invariant Green function on that modular curve. Adding the explicit elementary term \(L^2\) repairs automorphy, but \(J\) is still smooth in the interior. Equation (11) does not invalidate the established identities on the selected ray.

Here is the precise singularity obstruction. A Green current for a divisor \(D\) satisfies
\[
dd^c g+\delta_D=\omega\quad\text{with smooth }\omega
\tag{12}
\]
on the interior. If \(g\) is smooth there, then its divisor current must vanish there. Consequently an equality between \(R\) (or \(J\)) and a finite linear combination of such currents, modulo terms smooth in the interior, requires the **net interior divisor to be zero**. Finite level pullbacks/pushforwards do not remove a surviving divisor current. A pullback meeting a divisor retains its logarithmic singularity; a pullback contained in the divisor needs an additional regularization and is not the ordinary pullback.

This is not an obstruction to every Green-derived expression. There are three explicit limits:

* Negative-index Kudla kernels can be smooth Green functions for the zero divisor. KRY §5, (5.12), explicitly permits \((0,\Xi(m,v))\) for \(m<0\).
* Differentiating the scale parameter removes the logarithmic source:
  \(\partial_v\beta_1(2\pi vQ)=-e^{-2\pi vQ}/v\), which extends smoothly across \(Q=0\).
* Integrating a logarithmic Green kernel over geometric variables can give a smooth function of the auxiliary variable \(\tau\). That is what the relevant Berndt–Kühn calculation does; it is not a finite level correspondence identifying the original functions.

So smoothness kills the proposed identification with a **nonzero net interior divisor**, not all zero-divisor, parameter-derivative, or integrated constructions. The biharmonic equation (10) is an exact condition any proposed remaining identification would have to meet; it is not being substituted for a general impossibility theorem.

The level comparison causes no extra discrepancy in (1): it uses precisely the old level-one functions pulled back by \(z\mapsto dz\). It supplies no ramified elliptic local data. In the generating variable, finite level correspondences preserve weight; they do not turn the weight-two series in (5), or KRY's weight-\(3/2\) generating series, into the weight-zero function \(J\). The complex derivative in (1) accounts for that change of weight.

## 4. What the known arithmetic identity does and does not identify

In Berndt–Kühn the geometric space is \(X(1)\times X(1)\), and the coefficients of the arithmetic generating series are
\((T(m),\widetilde\Xi_\rho(v,Z,m))\in\widehat{\mathrm{CH}}^1(X)\).
Part II's Main Theorem pairs that series with \(\widehat c_1(\overline{\mathcal L})^2\). Its scalar result is a function of the **auxiliary** \(\tau\), not a Green current in \(\tau\).

The source's further normalization must also be retained: its arithmetic theorem uses
\(\mathcal E_2(z,s)=-12\psi(s)\mathsf E_2(z,s)\), where
\[
\psi(1)=-1,\qquad
\psi'(1)=4\eta,\qquad
\eta=\frac{\zeta'(-1)}{\zeta(-1)}+\frac12.
\]
Thus \(\mathcal E_2'(z,1)=12\mathsf E_2'(z,1)-48\eta\mathsf E_2(z,1)\).
If \(\mathcal A_\rho(z)\) denotes its already-paired arithmetic generating series, its stated theorem is
\(\mathcal A_\rho=\mathcal E_2'(\cdot,1)+f_\rho\), with a cutoff-dependent correction \(f_\rho\). As a literal consequence, (1) can be rewritten
\[
\mathscr D_zJ(z)=
\sum_d\frac{d b_d}{24}\,[\mathcal A_\rho(dz)-f_\rho(dz)]
+\frac12\sum_d d[(\kappa+4\eta)b_d+e_d]\mathsf E_2(dz,1).
\tag{13}
\]
This records exactly where the cited arithmetic theorem touches the calculation. It does not identify \(R\) with any coefficient \(\widetilde\Xi_\rho\), and it does not eliminate \(f_\rho\), invert \(\mathscr D_z\) arithmetically, or specify an arithmetic cycle on the seed curve. The geometric variables have already been integrated out before (13) is used. These are substantive differences, not an omitted scalar normalization.

No arithmetic Chow class for \(R\) has been established. Accordingly no arithmetic-intersection meaning is assigned to the one-dimensional functional
\(2\pi\int_0^\infty f(iy)R(iy)\,dy\).
The available source pairing integrates over the geometric space and includes finite arithmetic contributions; it is not that ray functional.

**Verdict:** exact special-function and differentiated Fourier match, with the first unmatched operation and variable roles explicit. No exact Green-current identification, residual evaluation, regulator comparison, numerical calculation, or successor construction is claimed.

## Sources and verification scope

Only the requested source family was inspected. The local Mellin, midpoint, and trace proofs were reused, not re-audited. The new Fourier derivative and Laplace calculations were checked symbolically without numerical evaluation. This is a written derivation and source comparison, not an independent referee review or formal proof.

* [Berndt–Kühn, Part II](https://arxiv.org/abs/1209.3949), Definition 2.1, Theorem 2.2, Main Theorem and Remark 1.1. [Bound PDF](../sources/midpoint_green_kernel/BERNDT_KUEHN_PART_II_1209.3949.pdf).
* [Berndt–Kühn, Part I](https://arxiv.org/abs/1205.6417), (2.0.2), (2.3.2), Proposition 2.4, Theorem 2.19. [Bound PDF](../sources/midpoint_green_kernel/BERNDT_KUEHN_PART_I_1205.6417.pdf).
* [Kudla–Rapoport–Yang, Derivatives of Eisenstein series and Faltings heights](https://www.math.toronto.edu/skudla/kry.compo.pdf), §§4–5, particularly (4.11) and (5.12); used to check the Green-current definition and its smooth zero-divisor exception. [Bound PDF](../sources/midpoint_green_kernel/KUDLA_RAPOPORT_YANG_FALTINGS_HEIGHTS.pdf).
