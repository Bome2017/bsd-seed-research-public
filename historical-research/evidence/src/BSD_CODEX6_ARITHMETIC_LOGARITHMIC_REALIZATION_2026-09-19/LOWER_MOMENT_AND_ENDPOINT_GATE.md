# L1: the lower moments and exact endpoints must be distinguished

Status: a mathematical deduction from the predecessor's Fricke/Mellin
identities. It is a correction to the proposed proof strategy, not a
new arithmetic fact about Sha or the value of q.

Let \(\gamma:i\infty\to i/\sqrt N\) be M1's half-ray, let
\(\delta:i\infty\to0\) be the full ray, and write

\[
\ell(z)=\log(-i\sqrt N z),\quad
H_j=\int_\gamma\alpha_f\ell^j,\quad
J_j=\int_\delta\alpha_f\ell^j.
\]

## L1a. Exact full/half relation

For every nonnegative integer j,

\[
\boxed{J_j=(1+(-1)^j)H_j.}
\]

**Proof.** Put \(F(t)=f(it/\sqrt N)\), so
\(F(1/t)=t^2F(t)\). The oriented full-ray integral is
\((2\pi/\sqrt N)\int_0^\infty F(t)(\log t)^jdt\).
In the part from 0 to 1 substitute \(t=1/u\). It becomes
\((-1)^j\int_1^\infty F(u)(\log u)^jdu\), proving the formula.
All integrals converge by cusp decay. QED.

Thus the retained rank-two data give

\[
H_0=J_0/2=L(E,1)/2=0,\qquad
J_1=0,\qquad H_2=J_2/2=L''(E,1)/2.
\]

But **J1=0 gives no value for H1**. In particular, \(L'(E,1)=0\)
does not justify deleting a constant multiple of H1 in a half-ray
comparison. The full centered first moment already vanishes by
Fricke parity. No proof that the seed's H1 vanishes or is nonzero is
asserted here.

Here is an exact counterexample to the *formal moment inference*.
Let

\[
\varphi(x)=(x^2-\tfrac12)e^{-x^2}.
\]

It is even, and its bilateral Laplace transform is

\[
\int_{\mathbb R}\varphi(x)e^{ux}dx
 =\frac{\sqrt\pi}{4}u^2 e^{u^2/4}.
\]

The transform has an exact double zero and even symmetry. Nonetheless,

\[
\int_0^\infty\varphi(x)dx=0,\quad
\int_0^\infty x\varphi(x)dx=\tfrac14,\quad
\int_0^\infty x^2\varphi(x)dx=\tfrac{\sqrt\pi}{4}.
\]

Taking \(F(t)=t^{-1}\varphi(\log t)\) also gives the same Fricke
relation \(F(1/t)=t^2F(t)\). This is not a modular newform and is
not claimed to describe the seed. It isolates precisely why the
functional equation and two vanishing full moments do not imply the
claimed half-moment cancellation.

## L1b. Exact does not mean zero on this path

For an admissible primitive G, the comparison

\[
\alpha_f\ell^2-\beta
 =a\alpha_f+b\alpha_f\ell+dG
\]

would give

\[
H_2-\int_\gamma\beta=bH_1+G(i/\sqrt N)-G(i\infty).
\]

The a term vanishes, but neither displayed term on the right is
automatically zero. If a tangential regularization is required, its
endpoint choices must be specified and its boundary difference proved.
An exact term in a relative de Rham complex carries these boundary data;
it cannot simply be discarded.

There are two correct comparison contracts:

* **Half-ray:** prove b=0 or independently cancel bH1, and prove the
  boundary difference is zero.
* **Full-ray:** both constant lower Mellin terms disappear, but the
  endpoint difference at 0 and infinity must still vanish. Recover the
  half-ray value only after a proved even Fricke symmetry for the
  other second-order period.

The unit candidate L2 has the needed squared-weight parity for the
second contract. It still fails the admissible modulo-exact comparison
by L3; parity alone is not that comparison.

**Endpoint:** neither FIN nor FORMULA. **Implication role:** remove false
arrows from the proposed path to q=36. **Still missing:** the corrected
period comparison and quantitative arithmeticity, then FIN/order nine.
**Kill condition:** a comparison relying only on the invalid half-ray
cancellation or an unspecified zero boundary is rejected.
