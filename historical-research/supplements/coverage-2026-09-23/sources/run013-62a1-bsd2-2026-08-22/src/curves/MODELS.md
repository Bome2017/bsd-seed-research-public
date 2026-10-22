# Exact curve and twist models

Status: algebraically proved; independent review PASS.

## 1. Base change of variables

Start with the optimal `62a1` model

\[
 v^2+uv+v=u^3-u^2-u+1.
\]

Put

\[
 X=4(u+1),\qquad Y=8v+4u+4=4(2v+u+1).
\]

Using the Weierstrass equation,

\[
\begin{aligned}
Y^2
 &=16(2v+u+1)^2\\
 &=16\bigl(4(v^2+uv+v)+u^2+2u+1\bigr)\\
 &=64u^3-48u^2-32u+80\\
 &=X^3-15X^2+64X.
\end{aligned}
\]

The inverse is

\[
 u=X/4-1,\qquad v=(Y-X)/8.
\]

Thus the change is a rational isomorphism, not merely an equality of
invariants.

## 2. Integral minimal twist and descent model

For `q = 1 mod 4`, hence for every `q in F_62`, an integral twist model is

\[
 \mathcal E_q:\quad
 v^2+uv+v
 =u^3-\frac{3q+1}{4}u^2
      -\frac{q^2+1}{2}u
      +\frac{5q^3-1}{4}.
\]

The coefficients are integers because `q = 1 mod 4`.  Put

\[
 X=4(u+q),\qquad Y=8v+4u+4.
\]

Then

\[
\begin{aligned}
Y^2
 &=64u^3-48qu^2-32q^2u+80q^3\\
 &=X^3-15qX^2+64q^2X.
\end{aligned}
\]

Therefore the descent equation

\[
 E_q:\quad Y^2=X^3-15qX^2+64q^2X
\]

is the positive quadratic twist of `62a1` by `q`.

## 3. Differential normalization

The Neron differential on the integral model is

\[
 \omega_q=\frac{du}{2v+u+1}.
\]

On the descent model it is tempting to use `dX/(2Y)`, but

\[
 \frac{dX}{2Y}
 =\frac{4du}{8(2v+u+1)}
 =\frac12\omega_q.
\]

Hence a period integrated from the displayed descent model must be multiplied
by `2` to obtain the Neron-normalized period.  This factor is load-bearing in
the BSD-at-2 calculation.
