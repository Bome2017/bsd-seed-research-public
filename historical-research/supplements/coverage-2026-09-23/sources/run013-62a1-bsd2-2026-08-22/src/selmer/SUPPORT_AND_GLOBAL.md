# Support lemma and global Selmer calculation

Status: proof complete; independent review and checker replay PASS.

## 1. Support lemma

Consider

\[
 C_d:\quad n^2=du^4+au^2v^2+\frac bdv^4
\]

over `Q_p`, and choose a squareclass representative with `v_p(d)` equal to
`0` or `1`.  Suppose `p` does not divide `b` and `v_p(d)=1`.  Multiplying by
`d` gives

\[
 d n^2=d^2u^4+adu^2v^2+bv^4.
\]

Scale homogeneous coordinates so that `u,v` are integral and not both
divisible by `p`.

- If `v` is a unit, the right side is a unit modulo `p`, whereas the left
  side has odd valuation.
- If `v` is divisible by `p`, then `u` is a unit.  The first term has
  valuation exactly `2`; the other two have larger valuation, so the right
  side has even valuation `2`, whereas the left side has odd valuation.

For `p=2` in the first Run013 covering, the same conclusion follows after
division by `4`: when `v` is even and `u` odd, the `d^2u^4` term remains a
unit modulo `2` and the other terms do not cancel it.

Therefore an everywhere locally soluble class is supported on the squarefree
prime divisors of `b`, together with the sign.

For the `phi_q` covering, `b=-31q^2`, so representatives may be chosen from

\[
 \{\pm1,\pm31,\pm q,\pm31q\}.
\]

For the dual covering, `b=64q^2`, so representatives may be chosen from

\[
 \{\pm1,\pm2,\pm q,\pm2q\}.
\]

These sharper eight-class sets imply the common sixteen-class bound stated
in `PROOF.md`.

## 2. The phi Selmer group

The four classes

\[
 1,-31,q,-31q
\]

are globally soluble.  On the covering

\[
 n^2=du^4+30qu^2v^2-\frac{31q^2}{d}v^4
\]

take respectively

\[
 (n,u,v)=(1,1,0),(q,0,1),(0,1,1),(0,1,1).
\]

The four remaining supported classes

\[
 -1,31,-q,31q
\]

have no `Q_2` point by `src/local_2/LOCAL_2.md`.  Hence

\[
 \operatorname{Sel}^{(\phi_q)}(E_q/\mathbf Q)
 =\{1,-31,q,-31q\}.
\]

## 3. The dual Selmer group

Negative supported classes have no real point by
`src/infinity/INFINITY.md`.  The class `2` has no `Q_2` point by
`src/local_2/LOCAL_2.md`.  The classes `q` and `2q` have no `Q_q` point by
`src/local_q/LOCAL_Q.md`.  The identity class is globally soluble via
`(n,u,v)=(1,1,0)`.

Therefore

\[
 \operatorname{Sel}^{(\widehat\phi_q)}(E'_q/\mathbf Q)=\{1\}.
\]

The proof uses only `q = 5 mod 8` and `(q/31)=-1` from the frozen family;
the point-count and ordinarity fields are retained for the analytic and
odd-primary theorem chain.
