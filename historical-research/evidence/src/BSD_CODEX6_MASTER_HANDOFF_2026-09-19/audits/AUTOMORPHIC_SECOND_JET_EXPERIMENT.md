# Automorphic completion of the second Mellin weight

**C. JET_IDENTITY_SURVIVES_WITH_ONE_TERM.**

One experiment, from the defining Eisenstein series and Poisson summation. The exact result is

\[
\boxed{\int_\gamma\alpha_f\,\mathcal E''(z,0)
       =M_2+\Delta,\qquad
\Delta=\int_\gamma\alpha_f R_N(z).}
\tag{1}
\]

The scalar multiplying M1 is **A = 1**. Every constant-term error cancels in the explicit normalization below. The sole residual is the fully specified nonconstant Fourier period \(\Delta\), not an unspecified difference of two desired quantities. Its integrand is nonzero. Its integral has **not** been proved zero or nonzero. Thus the user's equality (*) is not proved or refuted. Outcome C records an exact analytic decomposition, not a real-regulator comparison or a demonstrated difficulty reduction for BSD.

The parameter is \(s_0=0\), the endpoint at which the level-one Eisenstein series is 1. It is not the spectral symmetry centre \(1/2\). Expansion at the latter would leave a \(y^{1/2}\) multiplier in the constant-term logarithmic jets, rather than the unweighted Mellin logarithm sought here.

## 1. Collision and normalization checks

The [current master, §§4 and 5.7–5.8](../MASTER_BSD_DAG.md), [M1–M4](/Users/bsm/BSD_CODEX6_COMMON_B_ARITHMETICITY_ATTACK_2026-09-19/MELLIN_JET_THEOREM.md), [L3](/Users/bsm/BSD_CODEX6_ARITHMETIC_LOGARITHMIC_REALIZATION_2026-09-19/EXACT_CORRECTION_OBSTRUCTION.md), and [lower-moment calculation](/Users/bsm/BSD_CODEX6_ARITHMETIC_LOGARITHMIC_REALIZATION_2026-09-19/LOWER_MOMENT_AND_ENDPOINT_GATE.md) were the controlling prior results. The relevant local mechanism search also found earlier Eisenstein–Kronecker literature queries, but no proof of this normalization in the inspected records. No global novelty claim is made.

This uses smooth, nonholomorphic, automorphic functions on the upper half-plane and equality along one ray. It does not claim a holomorphic local identity in L3's finite algebraic class. It constructs no Eisenstein ideal, Galois extension, Selmer class, or GL(3) representation. It therefore does not invoke the previously failed mechanisms in those forms.

The half-ray first moment \(H_1\) is not known to vanish. Only \(H_0=0\) and the full-ray \(J_1=0\) are retained. This experiment does **not** discard any half-ray linear-log term: the constant-term normalization removes all such terms before integration.

Throughout

\[
N=2^3\cdot3\cdot2243\cdot4547^2\cdot5843
 =6503188012738584,\quad t=\sqrt N\,y,
\quad \gamma:i\infty\longrightarrow i/\sqrt N.
\]

On this ray \(\ell(iy)=\log t\), with the original normalization of \(\alpha_f\), the period, and the regulator unchanged. Neither \(q=36\) nor FIN enters any construction.

## 2. Defining Fourier expansion

For \(\Re(s)>1\), set

\[
E(z,s)=\frac12\sum_{\substack{(c,d)\in\mathbf Z^2\\(c,d)=1}}
                \frac{y^s}{|cz+d|^{2s}},\qquad z=x+iy.
\tag{2}
\]

Let

\[
Z(s)=\pi^{-s}\Gamma(s)\zeta(2s),\qquad
\varphi(s)=\frac{\sqrt\pi\,\Gamma(s-\tfrac12)\zeta(2s-1)}
                  {\Gamma(s)\zeta(2s)}.
\]

Poisson summation in the second coordinate of the unrestricted lattice sum gives

\[
E(z,s)=y^s+\varphi(s)y^{1-s}+\mathscr F(z,s),
\tag{3}
\]

\[
\mathscr F(z,s)=\frac{4\sqrt y}{Z(s)}
 \sum_{n\ge1}n^{s-1/2}\sigma_{1-2s}(n)
 K_{s-1/2}(2\pi n y)\cos(2\pi n x).
\tag{4}
\]

For clarity about constants: multiply (2) by \(2\zeta(2s)\) to obtain the sum over all nonzero lattice pairs. The \(c=0\) terms give \(y^s\) after division. The zero Fourier mode for \(c\ne0\) uses
\(\int_{\mathbf R}(u^2+a^2)^{-s}du
=\sqrt\pi\Gamma(s-1/2)a^{1-2s}/\Gamma(s)\), giving \(\varphi\). The nonzero modes use
\(2\pi^s|m|^{s-1/2}a^{1/2-s}K_{s-1/2}(2\pi|m|a)/\Gamma(s)\).
Writing \(n=mc\) produces the divisor sum in (4). These identities also give the meromorphic continuation used near zero.

At zero, \(1/Z(s)=-2s+O(s^2)\) and \(\varphi(s)=O(s)\). Therefore \(E(z,0)=1\), with (3)–(4) regular there.

## 3. Two invariant divisor orbits

Put

\[
\mathscr D=\{3^a2243^b4547^{2c}5843^e:a,b,c,e\in\{0,1\}\},
\]

\[
\mathscr O_0=\{d,8d:d\in\mathscr D\},\qquad
\mathscr O_1=\{2d,4d:d\in\mathscr D\},\qquad
F_j(z,s)=\sum_{d\in\mathscr O_j}E(dz,s).
\tag{5}
\]

Each orbit has 32 elements. Both sums are \(\Gamma_0(N)\)-automorphic and invariant under **every** exact-divisor Atkin–Lehner involution, including the Fricke involution.

Here is a direct verification. If \(Q\parallel N\), write
\(d=d_Qd_R\) with \(d_Q\mid Q\), \(d_R\mid N/Q\), and put
\(d'=Qd_R/d_Q\). An unscaled Atkin–Lehner matrix has the form

\[
W_Q=\begin{pmatrix}Qa&b\\Nc&Qe\end{pmatrix},\qquad \det W_Q=Q.
\]

The matrix

\[
\frac1{d_Q}\begin{pmatrix}d&0\\0&1\end{pmatrix}
W_Q\begin{pmatrix}1/d'&0\\0&1\end{pmatrix}
=
\begin{pmatrix}d_Qa&d_Rb\\(N/Q)c/d_R&Qe/d_Q\end{pmatrix}
\]

is integral of determinant one. Consequently \(E(dW_Qz,s)=E(d'z,s)\). The involution sends each exponent at a prime dividing Q to its complementary exponent in N. This preserves both orbits in (5). The same matrix argument for a matrix in \(\Gamma_0(N)\) proves automorphy of each \(E(dz,s)\).

These are indeed linear combinations of cusp Eisenstein series, as requested. For a cusp \(\mathfrak a=a/c\) in lowest terms, set

\[
w_{\mathfrak a}=N/\gcd(c^2,N),\qquad
k_{\mathfrak a,d}=w_{\mathfrak a}\gcd(c,d)^2/d,
\tag{6}
\]

with \(c=0,w_\infty=1\) at infinity. In the usual width-one scaling coordinate, the incoming term of \(E(dz,s)\) at this cusp is \(k_{\mathfrak a,d}^{s}y^s\). To see this, transform the first column \((da,c)^T\) to \((\gcd(d,c),0)^T\) by an integral determinant-one matrix. The remaining upper-triangular map multiplies imaginary parts by (6).

It follows that

\[
E(dz,s)=\sum_{\mathfrak a}k_{\mathfrak a,d}^{s}E^{(N)}_{\mathfrak a}(z,s).
\tag{7}
\]

One can also justify (7) without leaving an unspecified cusp-form summand: for real \(s>1\) the difference has no incoming terms, is square-integrable, and has Laplace eigenvalue \(s(1-s)<0\). The nonnegative hyperbolic Laplacian forces it to be zero. Meromorphic continuation proves (7) near zero.

## 4. Exact cancellation of the scattered constant term

Define the explicit even functions

\[
A_j(s)=\sum_{d\in\mathscr O_j}(d/\sqrt N)^s,
\qquad r(s)=2^s+2^{-s}-1.
\]

The elementary identity \(\cosh(3u)/\cosh(u)=2\cosh(2u)-1\) gives

\[
A_0(s)=r(s)A_1(s),\quad A_1(0)=32,
\quad r(0)=1,\quad r(1)=3/2.
\]

Set

\[
u_0(s)=\frac1{A_1(s)[r(s)-r(1-s)]},\qquad
u_1(s)=-r(1-s)u_0(s),
\]

\[
\boxed{\mathcal E(z,s)=u_0(s)F_0(z,s)+u_1(s)F_1(z,s).}
\tag{8}
\]

The denominator is nonzero at zero. All coefficients in (8) are explicit and independent of f, its periods, the rational points, and the desired BSD quotient. In the user's cusp notation,

\[
c_{\mathfrak a}(s)=\sum_{j=0}^1u_j(s)
                   \sum_{d\in\mathscr O_j}k_{\mathfrak a,d}^{s}.
\tag{9}
\]

The constant term at infinity of \(F_j\), expressed using t, is

\[
A_j(s)t^s+\varphi(s)A_j(1-s)t^{1-s}.
\]

Direct substitution proves

\[
u_0A_0+u_1A_1=1,\qquad
u_0A_0(1-s)+u_1A_1(1-s)=0.
\tag{10}
\]

Thus the complete constant term of \(\mathcal E\) is **exactly \(t^s\)** for all s near zero. In particular

\[
\mathcal E''(x+iy,0)=(\log(\sqrt N y))^2+R_N(x+iy),
\tag{11}
\]

where only the nonconstant Fourier modes contribute to \(R_N\). There is no residual \(y\log y\), \(y\), constant, or linear logarithm from the constant term. No Mellin-moment vanishing is used for this cancellation.

## 5. Explicit Fourier residual

Let

\[
\kappa=\log(4\pi)-\gamma_{\mathrm E},\quad
S_n=\sum_{a\mid n}a,\quad T_n=\sum_{a\mid n}a\log a,
\quad E_1(x)=\int_x^\infty e^{-u}\frac{du}{u},
\]

\[
h_n(v)=\kappa-\log n+\frac{2T_n}{S_n}
          +e^{4\pi n v}E_1(4\pi n v).
\tag{12}
\]

On the actual ray the residual is

\[
\boxed{\begin{aligned}
R_N(iy)={}&\sum_{d\in\mathscr O_0}\sum_{n\ge1}
 \frac{S_n}{n}e^{-2\pi ndy}
 \left[-\frac12h_n(dy)+\frac32\log2\right]\\
&+\sum_{d\in\mathscr O_1}\sum_{n\ge1}
 \frac{S_n}{n}e^{-2\pi ndy}
 \left[\frac34h_n(dy)-\frac32\log2\right].
\end{aligned}}
\tag{13}
\]

Off the ray, insert \(\cos(2\pi ndx)\) in each summand. This is a fully specified correction; it was obtained from the Fourier coefficients, not defined by subtracting the target integral.

**Derivation.** The reciprocal factor in (4) has

\[
(1/Z)'(0)=-2,\qquad (1/Z)''(0)=4\kappa.
\]

These follow by expanding \(\Gamma(s)\), \(\zeta(2s)\), and \(\pi^{-s}\), using \(\zeta(0)=-1/2\) and \(\zeta'(0)=-\tfrac12\log(2\pi)\). Also

\[
\left.\partial_\nu K_\nu(x)\right|_{\nu=-1/2}
=-K_{1/2}(x)e^{2x}E_1(2x).
\tag{14}
\]

For a direct verification of (14), at \(\nu=1/2\) differentiate the Bessel equation in the order. The derivative solves the inhomogeneous equation with forcing \(K_{1/2}\). Writing the proposed solution as \(K_{1/2}(x)h(x)\), with \(h=e^{2x}E_1(2x)\), reduces that equation to \(x^2(h''-2h')=1\), which follows from \(h'=2h-1/x\). Exponential decay and the asymptotic ratio \(h\sim1/(2x)\) select the solution uniquely. Evenness of \(K_\nu\) in \(\nu\) gives the minus sign at \(-1/2\).

Differentiating each Fourier mode in (4) consequently gives

\[
\mathscr F'(iv,0)=-4\sum_{n\ge1}\frac{S_n}{n}e^{-2\pi nv},\qquad
\mathscr F''(iv,0)=8\sum_{n\ge1}\frac{S_n}{n}e^{-2\pi nv}h_n(v).
\tag{15}
\]

Since \(A_1'(0)=0\), direct differentiation of (8) gives

\[
u_0(0)=-\frac1{16},\quad u_1(0)=\frac3{32},\qquad
u_0'(0)=-\frac3{16}\log2,\quad u_1'(0)=\frac3{16}\log2.
\tag{16}
\]

The nonconstant part of the second jet is
\(\sum_{j,d}[u_j(0)\mathscr F''(dz,0)+2u_j'(0)\mathscr F'(dz,0)]\), since \(\mathscr F(z,0)=0\). Substitution of (15)–(16) proves (13).

The first Fourier frequency occurs only at \(d=n=1\) in the first orbit. Along the ray it gives

\[
R_N(iy)=\frac12e^{-2\pi y}
 \left[\gamma_{\mathrm E}+\log(2/\pi)
       -e^{4\pi y}E_1(4\pi y)\right]
 +O(e^{-4\pi y})\qquad(y\longrightarrow\infty).
\tag{17}
\]

The bracket is not identically zero: its last term has asymptotic \(1/(4\pi y)+O(y^{-2})\). Even if its constant part were zero, that inverse-y term would survive. Thus the completion's Fourier correction does not vanish identically. **This is not a proof that its pairing with f is nonzero.**

## 6. The one residual period

Put \(y_0=N^{-1/2}\). The original orientation gives

\[
\boxed{\Delta=2\pi\int_{y_0}^{\infty}f(iy)R_N(iy)\,dy,}
\tag{18}
\]

with \(R_N\) explicitly given by (12)–(13). This is the sole remaining term in (1).

For an expression entirely in the known Fourier coefficients \(a_m\) of f, set

\[
k_n=\kappa-\log n+2T_n/S_n,\qquad
(b_d,e_d)=
\begin{cases}(-1/2,\,3\log2/2),&d\in\mathscr O_0,\\
(3/4,\,-3\log2/2),&d\in\mathscr O_1.
\end{cases}
\]

For positive integers m,k define

\[
\mathcal K_{m,k}=
\begin{cases}
\displaystyle\frac{e^{-2\pi(m-k)y_0}E_1(4\pi k y_0)
       -E_1(2\pi(m+k)y_0)}{2\pi(m-k)},&m\ne k,\\[6pt]
\displaystyle\frac{e^{-4\pi k y_0}}{4\pi k}-y_0E_1(4\pi k y_0),&m=k.
\end{cases}
\]

Then

\[
\Delta=2\pi\sum_{d\in\mathscr O_0\cup\mathscr O_1}
 \sum_{m,n\ge1}\frac{a_m S_n}{n}
 \left[(b_dk_n+e_d)\frac{e^{-2\pi(m+nd)y_0}}{2\pi(m+nd)}
       +b_d\mathcal K_{m,nd}\right].
\tag{19}
\]

To check the kernel, integrate
\(e^{-2\pi(m-k)y}E_1(4\pi k y)\) from \(y_0\) to infinity by parts. The separate \(m=k\) formula is its continuous limit. Formula (19) gives no sign or vanishing assertion.

All series and differentiated series are absolutely convergent on \(y\ge y_0>0\). Divisor sums and the cusp-form coefficients have polynomial growth, whereas the displayed kernels have exponential decay. Uniformity on compact parameter neighborhoods of zero and exponential cusp decay justify the second derivative under the integral in (1). Therefore (11) and retained M1 prove (1) with no conditional interchange or discarded endpoint term.

## 7. What the experiment establishes and where it stops

* The requested real-analytic automorphic family exists with explicit cusp coefficients (9), full Atkin–Lehner invariance, and a pure incoming constant term.
* Its second jet reproduces the literal logarithmic square on the ray **plus exactly the explicitly calculated Fourier correction (13)**.
* The proposed integrated identity (*) for this normalization holds if and only if \(\Delta=0\). No proof or counterexample for that equality was obtained here. Pointwise nonvanishing of (13) cannot be promoted to nonvanishing of (18).
* The outcome does not kill all automorphic-second-jet constructions and does not classify other cusp combinations. It does not supply an arithmetic intersection or a Néron–Tate regulator comparison. No such interpretation is assumed.

Elementary exact checks verified both 32-element orbits, their disjointness, \(\sum_{\mathscr O_0}d/\sum_{\mathscr O_1}d=3/2\), and the rational coefficients in (16). Independent 45-digit numerical spot checks of (14), individual differentiated Fourier modes, and (10) agreed; these are sanity checks, not proof of the identities or of \(\Delta\). The proof is the derivation above. No seed residual-period computation, large L-series run, source survey, subagent, or successor operation was performed.

**Stop at outcome C.** The result is an exact analytic decomposition. Neither q=36 nor the Sha/order-nine endpoint advances to a theorem from this result.
