# Global Mellin reduction of the midpoint residual

**EXPLICIT_SHIFTED_CONVOLUTION.**

The full-ray period is the value at \(u=1\) of an explicitly continued additive-convolution family:
\[
\boxed{2\Delta_{\rm mid}=P(1)=\mathcal D(1).}
\]
The exact series for \(\mathcal D(u)\) is (3.1), initially absolutely convergent for \(\Re u>3\). Its continuation to \(u=1\) is proved, not obtained by substituting into an unproved convergent double sum.

The Mellin transform of the residual itself factors into completed zeta functions and derivatives. Multiplication by \(f(iy)\), however, gives a Mellin–Barnes convolution with the completed \(L(f,\cdot)\), equation (4.6), not a finite product of special values. For the normalized Mellin family \(\mathcal D(u)\), §5 proves an obstruction stronger than failure of multiplicative coefficients: its Mellin measure has a nonzero continuous part on the explicit interval \((4548,4549)\). It therefore is not an ordinary Dirichlet series and has no Euler product of that kind.

This excludes finite combinations of ordinary Euler-product Dirichlet series and their derivatives as an identity for \(\mathcal D(u)\), under the precise normalizations in §5. It does not rule out every imaginable identity at the single value \(u=1\), or identities with freely inserted parameter-dependent special-function factors. No such additional identity is supplied here.

No period was evaluated numerically. No vanishing, nonvanishing, regulator comparison, or successor is claimed.

## 1. Inputs and the full-ray sign

Write \(p=4547\), \(M=N/p^2\), \(y_0=N^{-1/2}\), and \(R(z)=R_{\rm mid}(z)\). The inputs are the [middle-orbit residual, (6.4)](AUTOMORPHIC_MIDDLE_ORBIT_CLASSIFICATION.md) and the [trace calculation, §§1 and 4](MIDPOINT_UP_TRACE_TEST.md). They give
\[
f|_2W_N=-f,\qquad
f\!\left(\frac{i}{Ny}\right)=Ny^2f(iy),\qquad
R\!\left(\frac{i}{Ny}\right)=R(iy).
\tag{1.1}
\]
The positive sign in the middle identity includes the factor
\((Niy)^2=-N^2y^2\) in the weight-two slash operator.

In the lower-half integral substitute \(y=1/(Nv)\). The reversal of limits and the Jacobian give
\[
\int_0^{y_0}f(iy)R(iy)\,dy
=\int_{y_0}^{\infty}
f\!\left(\frac{i}{Nv}\right)
R\!\left(\frac{i}{Nv}\right)\frac{dv}{Nv^2}
=\int_{y_0}^{\infty}f(iv)R(iv)\,dv.
\]
Hence the requested normalization is exactly
\[
\boxed{
2\Delta_{\rm mid}=2\pi\int_0^\infty f(iy)R(iy)\,dy.}
\tag{1.2}
\]
This is consistent with the original orientation
\(\gamma:i\infty\to iy_0\), since \(2\pi i f(z)\,dz=-2\pi f(iy)\,dy\).

The residual Fourier expansion gives exponential decay at infinity, and (1.1) gives exponential decay in \(1/y\) at zero. These statements hold after every fixed number of \(y\,d/dy\) derivatives. The same assertion, allowing the factor \(y^{-2}\), holds for \(f(iy)\). Consequently
\[
P(u)=2\pi\int_0^\infty f(iy)R(iy)y^{u-1}\,dy
\tag{1.3}
\]
is entire in \(u\). There is no endpoint regularization in this integral.

The same substitution gives
\[
P(u)=N^{1-u}P(2-u).
\tag{1.4}
\]
Thus the completed convolution \(N^{u/2}P(u)/(2\pi)\) has symmetry about \(u=1\). This functional equation alone is not an Euler-product assertion.

The scoped collision check of the current master and automorphic reports found no prior Mellin–Barnes or shifted-convolution reduction of this residual. The local representation calculation is not reopened.

## 2. The residual and the elementary transform kernel

Let \(\mathcal O=O_{m,0}\cup O_{m,1}\), using the middle orbits of the preceding report. Put
\[
S_n=\sum_{a\mid n}a,\quad T_n=\sum_{a\mid n}a\log a,\quad
\kappa=\log(4\pi)-\gamma_{\rm E},\quad
k_n=\kappa-\log n+2T_n/S_n,
\]
\[
(b_d,e_d)=
\begin{cases}
(-1,3\log2),&d\in O_{m,0},\\
(3/2,-3\log2),&d\in O_{m,1}.
\end{cases}
\]
Then the existing Fourier formula on the ray is
\[
R(iy)=\sum_{d\in\mathcal O}\sum_{n\ge1}\frac{S_n}{n}
e^{-2\pi ndy}
\{b_dk_n+e_d+b_de^{4\pi ndy}E_1(4\pi ndy)\}.
\tag{2.1}
\]
Every \(d\) is divisible by \(p\). The already proved \(U_pf=0\) says \(a_{pm}=0\), so only \(p\nmid m\) occurs when
\(f(iy)=\sum_m a_me^{-2\pi my}\) is inserted.

For \(m,k>0\) and \(\Re u>0\), define
\[
\mathcal H_u(m,k)=
\int_0^\infty\frac{(m+k+2kv)^{-u}}{1+v}\,dv
=\int_{m+k}^{\infty}\frac{x^{-u}}{x-m+k}\,dx.
\tag{2.2}
\]
Both formulas converge absolutely. The defining integral
\[
e^{4\pi ky}E_1(4\pi ky)
=\int_0^\infty\frac{e^{-4\pi kyv}}{1+v}\,dv
\]
and the gamma integral yield
\[
\int_0^\infty y^{u-1}e^{-2\pi(m-k)y}E_1(4\pi ky)\,dy
=\frac{\Gamma(u)}{(2\pi)^u}\mathcal H_u(m,k).
\tag{2.3}
\]
The exponential has positive total decay \(m+k+2kv\), even when \(m-k<0\); no assumption \(m>k\) was made.

At the desired parameter,
\[
\boxed{\mathcal H_1(m,k)=
\frac{\log((m+k)/(2k))}{m-k}.}
\tag{2.4}
\]
For example, substitute \(t=1/(1+v)\) in (2.2) and integrate
\(1/(2k+(m-k)t)\) from zero to one. In our actual sums \(k=nd\) is divisible by \(p\) and \(m\) is not, so the case \(m=k\) is absent. There is no diagonal contribution hidden by this formula.

## 3. The additive Dirichlet family and its continuation

For \(\Re u>3\), set
\[
\boxed{
\mathcal D(u)=
\sum_{d\in\mathcal O}
\sum_{\substack{m,n\ge1\\p\nmid m}}
\frac{a_m S_n}{n}
\left\{
\frac{b_dk_n+e_d}{(m+nd)^u}
+b_d\mathcal H_u(m,nd)
\right\}.}
\tag{3.1}
\]
This is an absolutely convergent definition in that half-plane, not a formal rearrangement.

Here is a sufficient elementary bound. A weight-two cusp form satisfies
\(|a_m|\ll m\): boundedness of \(y|f(x+iy)|\), followed by Fourier coefficient extraction at \(y=1/m\), proves it. Also
\[
S_n/n\le1+\log n,\qquad |k_n|\ll1+\log n.
\]
For \(\sigma=\Re u>0\), splitting the \(v\)-integral at
\(\max(1,(m+k)/(2k))\) gives
\[
|\mathcal H_u(m,k)|
\le (m+k)^{-\sigma}
\left\{\log\!\left(1+\max\!\left(1,\frac{m+k}{2k}\right)\right)
+\frac1{\sigma}\right\}.
\tag{3.2}
\]
Grouping terms by \(m+dn=h\), the absolute sum is bounded by a constant times
\(\sum_h h^{2-\sigma}(1+\log h)^3\), which converges for \(\sigma>3\). The same majorant justifies the interchange with the \(y\)-integral in this half-plane.

Applying (2.3) and the elementary exponential gamma integral now proves
\[
\boxed{P(u)=(2\pi)^{1-u}\Gamma(u)\mathcal D(u)
\qquad(\Re u>3).}
\tag{3.3}
\]
Since \(P\) is entire, the formula
\[
\mathcal D(u)=\frac{(2\pi)^{u-1}}{\Gamma(u)}P(u)
\tag{3.4}
\]
provides its unique entire continuation. In particular
\[
\boxed{
2\Delta_{\rm mid}=\mathcal D(1)
=\underset{u=1}{\operatorname{AC}}\,
\sum_{d,m,n}\frac{a_mS_n}{n}
\left\{\frac{b_dk_n+e_d}{(m+nd)^u}
+b_d\mathcal H_u(m,nd)\right\}.}
\tag{3.5}
\]
The summation restrictions remain those of (3.1). At \(u=1\) the explicit continued kernel is
\[
\frac{b_dk_n+e_d}{m+nd}
+b_d\,\frac{\log((m+nd)/(2nd))}{m-nd}.
\tag{3.6}
\]
Equation (3.5), rather than an unqualified sum of (3.6), is the meaning of the answer. Absolute convergence of (3.1) at \(u=1\) has not been established or used.

The first summand of (3.1) is an additive convolution with coefficients
\[
c_h=
\sum_{\substack{d\in\mathcal O,\ n\ge1\\dn<h}}
\frac{a_{h-dn}S_n}{n}(b_dk_n+e_d).
\tag{3.7}
\]
The second is its explicitly specified integral-kernel counterpart. The coupling is through \(m+dn\), not the multiplicative pairing of equal indices in an unfolded Rankin–Selberg integral.

## 4. An independent Mellin–Barnes representation

This also makes precise which standard \(L\)-factors occur, and where the convolution remains.

Use the normalized variable \(t=\sqrt N y\), and set
\[
\mathscr R(t)=R(it/\sqrt N),\quad
\widehat{\mathscr R}(w)=\int_0^\infty\mathscr R(t)t^{w-1}\,dt.
\]
The decay proved in §1 makes this transform entire, rapidly decreasing on every fixed vertical line, and even in \(w\).

For clarity, define the meromorphic completed zeta function by
\[
\Xi(z)=\pi^{-z/2}\Gamma(z/2)\zeta(z).
\]
No factor \(z(z-1)/2\) is included. Thus \(\Xi(2s)=Z(s)\) in the preceding experiment.

Let
\[
r(s)=2^s+2^{-s}-1,\qquad
B(s)=(2^{s/2}+2^{-s/2})
\prod_{q\in\{3,2243,5843\}}(q^{s/2}+q^{-s/2}),
\]
\[
C(w,s)=
\frac{B(w)\,[r(w)-r(1-s)]}
{B(s)\,[r(s)-r(1-s)]}.
\tag{4.1}
\]
This is exactly the orbit scaling sum
\(\sum_{d\in\mathcal O}v_d(s)(d/\sqrt N)^{-w}\), with the already fixed midpoint coefficients \(v_d\). Evenness of the orbit divisor sums proves (4.1).

Start with the nonconstant Fourier part \(\mathscr F(iy,s)\) of the level-one Eisenstein series. Termwise Mellin transformation in its absolute-convergence region gives
\[
\int_0^\infty\mathscr F(iy,s)y^{w-1}\,dy
=\frac{\Xi(w+s)\Xi(w+1-s)}{\Xi(2s)}.
\tag{4.2}
\]
For completeness, the Bessel integral used here is
\[
\int_0^\infty y^{w-1/2}K_{s-1/2}(2\pi ny)\,dy
=2^{w-3/2}(2\pi n)^{-w-1/2}
\Gamma((w+s)/2)\Gamma((w+1-s)/2).
\]
For a direct derivation, use
\[
K_\nu(x)=\frac12(x/2)^\nu
\int_0^\infty v^{-\nu-1}e^{-v-x^2/(4v)}\,dv.
\]
This follows from the defining hyperbolic-cosine integral by exponentiating its variable. Mellin integration in \(x\) first and then in \(v\) gives
\(2^{\mu-2}\Gamma((\mu+\nu)/2)\Gamma((\mu-\nu)/2)\);
take \(\mu=w+1/2,\nu=s-1/2\) and scale \(x=2\pi ny\).
Multiplying by the Fourier coefficient
\(4n^{s-1/2}\sigma_{1-2s}(n)/Z(s)\) and using
\[
\sum_{n\ge1}\sigma_{1-2s}(n)n^{-(w+1-s)}
=\zeta(w+1-s)\zeta(w+s)
\]
proves all constants in (4.2). These operations are absolutely convergent, uniformly for \(s\) in a small compact neighborhood of zero and \(\Re w>1+\epsilon\), with that neighborhood chosen inside \(|\Re s|<\epsilon\).

The midpoint normalization therefore gives the exact meromorphic identity
\[
\boxed{
\widehat{\mathscr R}(w)
=\left.\partial_s^2
\left\{C(w,s)\frac{\Xi(w+s)\Xi(w+1-s)}{\Xi(2s)}\right\}
\right|_{s=0}.}
\tag{4.3}
\]
Differentiation under the initial convergent integrals is justified by the same bounds. Analytic continuation then gives the entire transform on the left.

There is a useful check on apparent poles. Before taking the second jet, put
\(h(t,s)=\mathcal E_{\rm mid}(it/\sqrt N,s)-t^s\). It decays exponentially at infinity, while at zero Fricke gives
\[
h(t,s)=t^{-s}-t^s+\text{exponentially small remainder}.
\]
Its Mellin transform has only the principal parts
\[
\frac1{w-s}-\frac1{w+s}
\]
near these two moving poles. Their second \(s\)-derivative at zero vanishes. The putative scattered poles are removed by the factor \(r(w)-r(1-s)\) in (4.1). Thus the second jet in (4.3) has removable apparent poles, consistently with the direct entire integral.

An expanded version of (4.3) is explicit in zeta functions and their first derivatives. Put
\[
c_0(w)=\frac{B(w)}8(3/2-r(w)),\qquad
c_1(w)=\frac{3B(w)\log2}{8}(1-r(w)),
\]
\[
X(w)=\Xi(w)\Xi(w+1),\quad
Y(w)=\Xi'(w)\Xi(w+1)-\Xi(w)\Xi'(w+1).
\]
Since \(1/\Xi(2s)=-2s+2\kappa s^2+O(s^3)\),
\[
\boxed{
\widehat{\mathscr R}(w)
=4\{(\kappa c_0(w)-c_1(w))X(w)-c_0(w)Y(w)\}.}
\tag{4.4}
\]
All apparent singularities in this displayed expression are interpreted by the removable continuation just proved.

Define
\[
\Lambda(f,z)=N^{z/2}(2\pi)^{-z}\Gamma(z)L(f,z).
\]
It is the Mellin transform of \(f(it/\sqrt N)\), initially by its Dirichlet series and then everywhere by cusp decay at both ends. Mellin inversion and Fubini give, for any fixed real \(c\),
\[
\boxed{
P(u)=\frac{2\pi N^{-u/2}}{2\pi i}
\int_{\Re w=c}\widehat{\mathscr R}(w)\Lambda(f,u-w)\,dw.}
\tag{4.5}
\]
Both Mellin transforms are rapidly decreasing on fixed vertical lines; the original functions have faster-than-power decay at zero and infinity. These facts justify the inversion, the interchange, and local uniformity in \(u\). No Dirichlet expansion outside its convergence half-plane is being substituted into this contour.

Combining (1.2), (4.4), and (4.5) gives the requested exact global representation
\[
\boxed{
2\Delta_{\rm mid}
=\frac{2\pi/\sqrt N}{2\pi i}
\int_{\Re w=c}
\Lambda(f,1-w)\,
4\{(\kappa c_0-c_1)X-c_0Y\}(w)\,dw.}
\tag{4.6}
\]
This is a Barnes convolution of standard factors. It has not become a finite combination of their values or derivatives.

The known central zero does not remove the contour: \(\Lambda(f,1)=\Lambda'(f,1)=0\) controls one point, while the integrand samples \(\Lambda(f,1-w)\) along a line. Nor is there an oddness cancellation. The root number \(+1\) gives \(\Lambda(f,1-w)=\Lambda(f,1+w)\), and \(\widehat{\mathscr R}(w)\) is even, so their product is even.

## 5. A coefficient-level obstruction to an Euler Dirichlet factorization

The integral kernel gives a rigorous structural test, without guessing from the appearance of (3.1).

For real \(x>0\), define the locally finite sum
\[
\rho(x)=
\sum_{d\in\mathcal O}
\sum_{\substack{m,n\ge1,\ p\nmid m\\m+nd\le x}}
\frac{a_m b_d S_n}{n(x-m+nd)}.
\tag{5.1}
\]
Equations (2.2) and (3.7) show, in the absolute-convergence half-plane,
\[
\mathcal D(u)=\int_0^\infty x^{-u}\,d\mu(x),\qquad
d\mu(x)=\sum_{h\ge1}c_h\delta_h+\rho(x)\,dx.
\tag{5.2}
\]
The estimates in §3 also prove finite total variation after weighting by \(x^{-\sigma}\), for every \(\sigma>3\).

The smallest divisor in either middle orbit is \(d=p\), in \(O_{m,0}\), where \(b_p=-1\). For
\[
p+1<x<p+2
\]
only \(d=p,\ n=1,\ m=1\) occurs in (5.1). The newform normalization gives \(a_1=1\), and \(S_1=1\). Therefore
\[
\boxed{\rho(x)=-\frac1{x+p-1}\ne0
\qquad(4548<x<4549).}
\tag{5.3}
\]
This proves that the continuous part survives **all** the actual orbit coefficients and the condition \(a_{pm}=0\). No other orbit or Fourier term has yet reached this interval, so cancellation there is impossible. The value of \(\kappa\) is irrelevant to this obstruction.

Suppose \(\mathcal D(u)\) were an ordinary absolutely convergent Dirichlet series in some right half-plane. Its Mellin measure would be purely atomic, \(\sum_\nu A_\nu\delta_\nu\). Choose a vertical line where both representations have finite weighted total variation. Substituting \(x=e^t\), equality on that line becomes equality of Fourier transforms of finite signed measures. Uniqueness of that transform forces equality of the measures, contradicting the nonzero absolutely continuous part (5.3).

The same argument excludes finite sums and products of ordinary Euler-product Dirichlet series, including twists, Rankin–Selberg Euler products, and their finitely many derivatives in the Mellin variable: their coefficients remain supported on discrete multiplicative indices. Fixed exponential rescalings \(A^{-u}\), fixed argument shifts, and finite Dirichlet-polynomial corrections still give atomic measures and do not repair the obstruction.

**Exact scope.** This is a theorem about the normalized family \(\mathcal D(u)\) after the explicit gamma factor in (3.3) has been removed. It excludes an Euler-product Dirichlet factorization of that family and the finite Dirichlet-series combinations just specified. It does not establish algebraic independence of isolated special values; it does not classify identities with arbitrary \(u\)-dependent gamma ratios or other inserted archimedean kernels. Such an extra kernel would itself require a proved identity. The present derivation supplies the Barnes integral (4.6), not a finite-factor evaluation of it.

Ordinary Rankin–Selberg unfolding does not apply to this one-dimensional ray integral as though it were an integral over a modular fundamental domain. In particular there is no integration over \(x\) imposing equality of Fourier indices. Directly, the calculation produces \(m+nd\) and the continuous shift in (2.2); the nonzero density (5.3) certifies that this feature was not erased by the seed's vanishing coefficients.

## 6. Result and stop

The full-ray sign is positive and the factor is exactly two. Equations (3.1)–(3.6) give the continued shifted-convolution series and its logarithmic kernel. Equations (4.3)–(4.6) give an independent exact Mellin–Barnes expression, including every normalization constant.

The first proved obstruction to an Euler Dirichlet factorization is the continuous density (5.3), not an analogy or a failed search. The value \(\mathcal D(1)\), equivalently \(2\Delta_{\rm mid}\), remains unevaluated. No additional local analysis, numerical calculation, regulator proposal, or successor route was performed.
