# Arithmetic origin of the mirror389 four-row certificate

Date: 2026-10-15. Independent reconstruction from the saved source elements,
field, torsion point and local data. No BNF or source-generation computation was
rerun. The replay regenerated the first 64 additivity rows and freshly evaluated
the selected local coordinate on all eleven source generators.

## Result

The short certificate is the following equality of arithmetic functionals on
the five-dimensional valuation-zero source `H0`:

\[
\boxed{c(a)=s(a)+a_{127}(a)+a_{151}(a)+2\lambda_3(a)\quad\text{in }\mathbf F_3.}
\]

Here `c` is the already-verified ordinary class-group boundary; its coordinate
on the four units followed by the class lift is `(0,0,0,0,1)`. The four terms on
the right are defined below. This equality holds on this actual saved source,
not on arbitrary number-field elements or on a family of curves.

The source curve is the mirror control
`E=[0,0,1,-21,-27]`, not the rank-two BSD seed. The torsion field is

\[
L=\mathbf Q(w),\quad
w^8-4w^7-17w^6+12w^5+270w^4+33w^3-1101w^2-1218w+3945=0.
\]

The saved nonzero 3-torsion point is `T=data.gp[5]`. The eleven actual field
elements are `G=data.gp[6]`; source coordinates 7–10 are the four units and
coordinate 11 is the class lift. All source indices in this paragraph are
one-based. The table below uses the producer's zero-based row indices.

| Row | Arithmetic functional | Restriction to `(u1,u2,u3,u4,c)` |
|---|---|---|
| G[7], scalar[7] | G8 coordinate of the cube class of `a·τ(a)` | `(0,0,1,0,1)` |
| G[12], additivity[1] | Cubic-symbol additivity at 127 | `(1,1,1,2,2)` |
| G[44], additivity[33] | Cubic-symbol additivity at 151 | `(1,2,0,1,2)` |
| local3[1] | Unit cube coordinate at the specified degree-one prime above 3 | `(2,0,2,0,1)` |

The sum of the first three rows and twice the fourth is `(0,0,0,0,1)`.
Thus simultaneous vanishing of these necessary scalar, additivity and local
conditions already forces the ordinary class boundary to vanish. No claim
that the finite global screen is a complete description of global cohomology
is needed for that one-direction exclusion.

## 1. Scalar condition

The saved automorphism `τ` fixes `x(T)` and sends `y(T)` to `-y(T)-1`, hence
sends `T` to `-T`. The source action is the matrix `TAU=data.gp[9]`.
Every column identity

\[
\tau(G_j)=r_j^3\prod_iG_i^{\operatorname{TAU}_{ij}}
\]

was checked literally using the saved roots `r_j=data.gp[11][j]`. Therefore
`s(a)` is precisely the eighth source coordinate of `[aτ(a)]`, not a label
attached only to a numerical row. Its full eleven-entry row is

`[0,0,1,1,1,0,0,0,1,0,1]`.

The target coordinate is the cube-class coordinate of

\[
G_8=\frac{1}{1009955}
(2497w^7-10675w^6-78988w^5-30330w^4+1286000w^3
+3329961w^2+1747617w-5904400).
\]

This coordinate depends on the fixed independently checked source basis.
It is not asserted to have a canonical meaning without that basis.

## 2. Additivity at the split prime 127

The ordered roots of the defining polynomial modulo 127 are

`24,57,71,78,79,98,108,124`.

Put `ω127=107`, the exact primitive cube root selected by the producer. For
an embedding `w→r` and a source element `a` that is a unit there, define

\[
\chi_{127,r}(a)=j\quad\Longleftrightarrow\quad
a(r)^{42}=107^j\pmod{127},\qquad j\in\mathbf F_3.
\]

The selected torsion points are

\[
T_{24}=(102,15),\quad T_{57}=(53,39),\quad T_{71}=(51,29),
\qquad T_{24}+T_{57}=T_{71}.
\]

Hence the row is the explicit functional

\[
a_{127}=\chi_{127,24}+\chi_{127,57}-\chi_{127,71}.
\]

Its eleven source values are
`[0,2,2,0,0,1,1,1,1,2,2]`.
These were freshly calculated from the actual field elements, not copied from
the saved row matrix. All source elements were nonzero at these embeddings.

## 3. Additivity at the split prime 151

The ordered roots modulo 151 are

`5,20,25,36,47,58,119,147`.

Put `ω151=32`, and define `χ151,r(a)` by `a(r)^50=32^χ151,r(a)`.
The torsion relation is

\[
T_5=(24,138),\quad T_{25}=(60,47),\quad T_{58}=(53,14),
\qquad T_5+T_{25}=T_{58}.
\]

Thus

\[
a_{151}=\chi_{151,5}+\chi_{151,25}-\chi_{151,58},
\]

with full source row `[0,0,1,1,1,0,1,2,0,1,2]`.
This too was freshly calculated. The replay reconstructs all 32 rows at 127
and all 32 at 151 and matches every one to the saved prefix.

## 4. The exact local condition at 3

This is the first prime ideal in the saved `idealprimedec(nf,3)` order. It has
ramification degree and residue degree `(e,f)=(1,1)`, so its completion is
`Q3`. Its field embedding satisfies `w≡2 mod27`. The precise prime ideal is
also bound by its HNF in the replay output; the congruence is descriptive,
while the HNF removes any possible ambiguity.

The local cube test uses depth two and uniformizer 3. The unit quotient is
`(Z/9Z)^×`, of cyclic order six. In the saved `idealstar` coordinate,
`ideallog(5)=1` and `ideallog(2)=5`. Consequently the selected functional is

\[
\lambda_3(a)=
\operatorname{ind}_{5}\!\left(3^{-v_{\mathfrak p}(a)}a\bmod9\right)\bmod3
=2\operatorname{ind}_{2}\!\left(3^{-v_{\mathfrak p}(a)}a\bmod9\right)\bmod3.
\]

The valuation is removed before taking the unit residue. This is a local cube
coordinate, not a height or a ray-class boundary. Its full source row is
`[1,1,0,2,0,2,2,0,2,0,1]`, obtained afresh by `locvec` on the actual eleven
elements.

The saved full local vector at 3 has twelve coordinates from three primes
above 3. The chosen Kummer-annihilator row is simply
`[0,1,0,0,0,0,0,0,0,0,0,0]`: it selects this unit coordinate at the first
degree-one prime. It vanishes on both columns of the saved two-dimensional
local Kummer image. Completeness and precision of that local image retain the
separate local dimension and exact-Hensel checks from `COMPATIBILITY_REVIEW.md`;
no fresh local point sampling was performed here.

## 5. Exact scope and a source-formula target

The four-term relation is a concrete arithmetic explanation of this control's
joint obstruction: the ordinary class boundary equals a combination of one
scalar descent condition, two specified split-prime additivity conditions,
and one specified 3-adic unit condition. A class that separately admits global
and local unit repairs need not admit the same repair for both, because these
four functionals force its boundary to vanish when imposed together.

The source-formula question suggested by the calculation is whether this
particular relation can be derived from a reciprocity or class-field identity
with the displayed embeddings and local character, and whether any such
identity has a controlled analogue in other torsion fields. This file does
not establish that generalization or an independent bound for the original
seed. Nor does it identify this mixed relation with the unrestricted ray-class
boundary. FIN, ORDER9 and Q36 are unchanged.

## Replay and custody

`map_arithmetic_rows.gp` has an explicit 60-second alarm and reads only saved
arithmetic. It prints `ARITHMETIC_ROW_MAP_PASS`; the only stderr is PARI's
normal stack-expansion warning. It does not call `bnfinit`, `bnfcertify`,
`lsgens2`, `lockummer` or any other new source/local-point producer.
Bindings, runtime and two-run byte agreement are in
`ARITHMETIC_ROW_MAP_RECEIPT.json`. The exact individual cubic-symbol vectors,
local-prime HNF and coordinate labels are retained in `ARITHMETIC_ROW_MAP.out`.
