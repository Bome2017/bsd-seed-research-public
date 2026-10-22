# Exact local exclusions at 2

Status: proof complete; independent review and checker replay PASS.

Throughout, `q = 5 mod 8`.  Hence `q^2 = 9 mod 16` and
`30q = 6 mod 16`.  A square modulo `8` lies in `{0,1,4}`, and a square
modulo `16` lies in `{0,1,4,9}`.

Scale a putative 2-adic point so that `u,v in Z_2` are not both even.

## 1. Four exclusions in the phi orientation

For each

\[
 d\in\{-1,31,-q,31q\},
\]

write

\[
 c=-31q^2/d.
\]

The covering is

\[
 n^2=du^4+30qu^2v^2+cv^4.
\]

For these four classes, `d` and `c` are odd and congruent modulo `8` to
either `3` or `7`.

- If `u` is odd and `v` even, the right side is `d mod 8`, hence `3` or
  `7`, not a square.
- If `u` is even and `v` odd, it is `c mod 8`, again `3` or `7`.
- If `u,v` are both odd, then `u^4=v^4=1 mod 16` and
  `u^2v^2` is `1` or `9 mod 16`.  Multiplication by `30q = 6 mod 16`
  gives `6` in either case.  Directly for all four `d`,
  `d+c+6 = 12 mod 16`, which is not a square.

Thus none of `-1,31,-q,31q` lies in the `phi_q` Selmer group.

## 2. Exclusion of `d=2` in the dual orientation

The covering is

\[
 n^2=2u^4-15qu^2v^2+32q^2v^4.
\]

- If `u` is odd and `v` even, the right side is `2 mod 4`.
- If `u,v` are odd, the right side is
  `2-15q = 7 mod 8`.
- Suppose `u` is even and `v` odd, and put `k=v_2(u)`.
  - If `k=1`, division by `4` leaves the odd unit
    `-15q(u/2)^2v^2 = 5 mod 8`; it is not a square unit.
  - If `k=2`, division by `16` leaves
    `-15q(u/4)^2v^2+2q^2v^4 = 5+2 = 7 mod 8`.
  - If `k>=3`, the last term has the unique minimum valuation `5`, which
    is odd.

Every primitive parity case is impossible, so `2` is absent from the dual
Selmer group.
