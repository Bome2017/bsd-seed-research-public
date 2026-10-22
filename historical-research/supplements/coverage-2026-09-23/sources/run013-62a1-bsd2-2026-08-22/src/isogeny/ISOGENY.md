# Exact isogeny and Kummer orientation

Status: algebraically proved; independent review PASS.

## 1. General quotient identity

Let

\[
 E_{a,b}:\quad y^2=x^3+ax^2+bx=x(x^2+ax+b).
\]

For `x != 0`, set

\[
 X=\frac{y^2}{x^2}=x+a+\frac bx,
 \qquad
 Y=\frac{y(b-x^2)}{x^2}.
\]

Since

\[
 (X-a)^2-4b
 =\left(x+\frac bx\right)^2-4b
 =\left(x-\frac bx\right)^2,
\]

we obtain

\[
\begin{aligned}
X\bigl(X^2-2aX+a^2-4b\bigr)
 &=\frac{x^2+ax+b}{x}\frac{(x^2-b)^2}{x^2}\\
 &=\frac{(x^2+ax+b)(b-x^2)^2}{x^3}\\
 &=Y^2.
\end{aligned}
\]

The map extends over `(0,0)` and `O`, with kernel
`{O,(0,0)}`, and its quotient is

\[
 E'_{a,b}:\quad Y^2=X^3-2aX^2+(a^2-4b)X.
\]

## 2. Run013 specialization

For `a=-15q`, `b=64q^2`, this gives

\[
 E'_q:\quad Y^2=X^3+30qX^2-31q^2X
               =X(X-q)(X+31q)
\]

and

\[
 \phi_q(x,y)=
 \left(\frac{y^2}{x^2},
       \frac{y(64q^2-x^2)}{x^2}\right).
\]

Quotienting `E'_q` by `(0,0)` gives

\[
 Y^2=X^3-60qX^2+1024q^2X.
\]

The scaling `(X,Y) -> (X/4,Y/8)` identifies this curve with `E_q`.
Consequently the normalized dual is

\[
 \widehat\phi_q(x,y)=
 \left(\frac{y^2}{4x^2},
       \frac{y(-31q^2-x^2)}{8x^2}\right).
\]

It has kernel `{O,(0,0)}` on `E'_q`, and by the defining uniqueness of the
dual isogeny its compositions with `phi_q` are multiplication by `2`.

## 3. Covering equations and orientation

For `E_{a,b}`, write an `x`-coordinate as

\[
 x=d\frac{u^2}{v^2},\qquad
 y=d\frac{un}{v^3}.
\]

Substitution gives

\[
 n^2=du^4+au^2v^2+\frac bdv^4.
\]

Applying this to `E'_q`, whose coefficients are `(30q,-31q^2)`, fixes

\[
 C^{(\phi)}_{q,d}:\quad
 n^2=du^4+30qu^2v^2-\frac{31q^2}{d}v^4.
\]

Applying it to `E_q`, whose coefficients are `(-15q,64q^2)`, fixes

\[
 C^{(\widehat\phi)}_{q,d}:\quad
 n^2=du^4-15qu^2v^2+\frac{64q^2}{d}v^4.
\]

This derivation binds the first family to `Sel^(phi_q)(E_q)` and the second
to `Sel^(widehat(phi_q))(E'_q)`.

## 4. Rational torsion images

The rational 2-torsion of `E'_q` is

\[
 O,(0,0),(q,0),(-31q,0).
\]

Under the `x`-coordinate Kummer map their squareclasses are respectively

\[
 1,-31,q,-31q.
\]

For `E_q`, the other two roots have discriminant `-31q^2`, so

\[
 E_q(\mathbf Q)[2]=\{O,(0,0)\}.
\]

The exceptional Kummer value at `(0,0)` is `64q^2`, a rational square.
Thus the rational torsion supplies only the identity class in the dual
orientation.
