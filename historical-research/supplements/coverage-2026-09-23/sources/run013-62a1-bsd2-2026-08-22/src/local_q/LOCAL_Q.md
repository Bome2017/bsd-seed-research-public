# Exact local exclusions at the moving prime q

Status: proof complete; independent review and checker replay PASS.

For every `q in F_62`, `q = 1 mod 4`.  Quadratic reciprocity therefore gives

\[
 \left(\frac{-31}{q}\right)
 =\left(\frac{-1}{q}\right)\left(\frac{31}{q}\right)
 =\left(\frac q{31}\right)=-1.
\]

## 1. Class `d=q`

The dual covering becomes

\[
 n^2=q\bigl(u^4-15u^2v^2+64v^4\bigr).
\]

Scale so `u,v in Z_q` are not both divisible by `q`.  If `v=0 mod q`, the
parenthesis is nonzero.  If `v` is a unit and the parenthesis vanishes, then

\[
 z=(u/v)^2
\]

would solve

\[
 z^2-15z+64=0
\]

over `F_q`.  Its discriminant is `-31`, a nonsquare.  Thus the parenthesis
is always a unit, the right side has valuation exactly `1`, and it cannot be
a square in `Q_q`.

## 2. Class `d=2q`

The covering becomes

\[
 n^2=q\bigl(2u^4-15u^2v^2+32v^4\bigr).
\]

If `v=0 mod q`, the parenthesis is again nonzero.  Otherwise a zero would
give

\[
 2z^2-15z+32=0,
\]

whose discriminant is also `-31`.  The right side again has odd valuation
`1`.  Therefore neither `q` nor `2q` belongs to the dual Selmer group.
