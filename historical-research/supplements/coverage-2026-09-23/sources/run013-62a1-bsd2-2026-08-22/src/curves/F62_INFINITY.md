# Infinitude of the frozen prime family

Status: proof complete from a finite exact witness plus standard published
Frobenius and Chebotarev theorems; independent review PASS.

## 1. Exact witness

The dependency-free script `point_count_62a1.py` counts the minimal long
Weierstrass model over `F_13`.  It gives

\[
 \#E(\mathbf F_{13})=12,\qquad a_{13}=13+1-12=2.
\]

Moreover

\[
 13\equiv5\pmod8,
 \qquad \left(\frac{13}{31}\right)=-1.
\]

Thus `13` itself lies in `F_62`.

## 2. Frobenius class

Let

\[
 K=\mathbf Q(E[8],\sqrt{31}).
\]

The curve has good reduction at `13`, and `13` does not divide `8*31`, so
`13` is unramified in `K`.  Let `C` be the conjugacy class of its Frobenius
in `Gal(K/Q)`.

For every rational prime `r` unramified in `K` with Frobenius in `C`, the
restriction to `E[8]` has

\[
 \operatorname{tr}(\operatorname{Frob}_r)\equiv2\pmod8,
 \qquad
 \det(\operatorname{Frob}_r)\equiv5\pmod8.
\]

The determinant is the mod-8 cyclotomic character, hence

\[
 r\equiv5\pmod8.
\]

The restriction to `Q(sqrt(31))` is nontrivial, hence

\[
 \left(\frac{31}{r}\right)=-1.
\]

Because `r = 1 mod 4`, quadratic reciprocity gives

\[
 \left(\frac r{31}\right)=-1.
\]

Finally,

\[
 \#E(\mathbf F_r)
 =1+r-a_r
 \equiv1+5-2
 \equiv4\pmod8.
\]

Therefore `v_2(#E(F_r))=2`, while `a_r=2 mod 8` implies `a_r != 0`.

## 3. Chebotarev

The conjugacy class `C` is nonempty, so Chebotarev gives its unramified
primes positive density.  Removing the finitely many primes dividing `372`
does not change infinitude.  Every remaining prime lies in `F_62`.

Hence

\[
 \#F_{62}=\infty.
\]
