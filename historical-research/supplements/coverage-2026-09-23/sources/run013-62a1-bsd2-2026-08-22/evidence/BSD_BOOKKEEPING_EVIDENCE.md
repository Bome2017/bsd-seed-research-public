# Evidence for the conditional `62a1` BSD chain

Evidence date: 2026-08-22 (America/Los_Angeles)

Scope: exact curve, isogeny orientation, period, torsion, Tamagawa,
full-2-Selmer consequence, BSD-at-2 bookkeeping, and the qualified
odd-primary assembly.  This file does **not** prove the two frozen
isogeny-Selmer identities.

## 1. Source bindings and publication status

| source | exact object | SHA-256 / URL | status at evidence date | use |
|---|---|---|---|---|
| Cremona/LMFDB ecdata | `/Users/bsm/run013-bsd-scout-2026-08-22/_data/ecdata/curvedata/curvedata.00000-09999` | `b42836e901ac75874d13207faef0bdc47a3799571937b1099df56c57897e8040` | frozen database bytes | base model, discriminant, conductor, local data, rank, torsion; decimal period and L-value are corroboration only |
| Cremona `opt_man` | `/Users/bsm/run013-bsd-scout-2026-08-22/_data/ecdata/opt_man/opt_man.00000-09999` | `11e4ebd69dbef2c6d9fce35c989d374f64a179e9d6ec13b5916cf453acd9298a` | frozen database bytes | exact `62 a 1 ... 1 1` optimality and Manin-constant row |
| PARI/GP exact modular-symbol runtime | `evidence/tooling/pari-2.17.4.tar.gz` | `02651d99c391007d384b3fadbc20abc6916b77036f9e496c99e9ce8688ca4b53`; [official release](https://pari.math.u-bordeaux.fr/download.html) | **published stable source**, 2.17.4 | exact Hecke eigenspace and canonical integral-lattice certificate for `abs(L(E,1)/Omega_E^+)=1/4` |
| LMFDB `62.a4` | API row | [live API](https://www.lmfdb.org/api/ec_curvedata/?lmfdb_label=62.a4&_format=json) | public database | independent label/model check |
| LMFDB `62.a3` | API row | [live API](https://www.lmfdb.org/api/ec_curvedata/?lmfdb_label=62.a3&_format=json) | public database | quotient minimal-model check |
| Shuai Zhai | arXiv published-version PDF `1409.0231v2` | `ca104aac009c76d167c9eae0e2069d448e4f2187eeda0368272c89e4ee084c36`; [journal DOI](https://doi.org/10.4310/AJM.2016.v20.n3.a4) | **published**, Asian J. Math. 20 (2016), 475--502 | Theorem 1.5 analytic valuation/nonvanishing and finiteness |
| Barrios--Roy--Sahajpal--Tallana--Tobin--Wiersema | local-data PDF `2501.03209v2` | `9e170d95fada236093bd7edc0ce9404587d98c858fe41239f5f78b589470b893`; [DOI](https://doi.org/10.1007/s40993-025-00650-w) | **published**, Res. Number Theory 11 (2025), no. 3, Paper 75 | uniform twist Kodaira, conductor, discriminant and Tamagawa rules |
| Banwait--Huang | PDF `2601.16044v3` | `81d2be4c05042240a67567194cead279131d7fd51b8bcfb027a35d145da7885c`; [arXiv](https://arxiv.org/abs/2601.16044) | **public preprint**, v3 2026-06-04, marked to appear at ANTS XVII | definition of `BSD(E,p)` and Theorem 2.13 odd-primary assembly |
| Burungale--Skinner--Tian--Wan | PDF `2409.01350v2` | `18e05982cdb2ac57cd7fcdc4791e5db8bff2945755653a5b76dd94377ed11ecf`; [arXiv](https://arxiv.org/abs/2409.01350) | **public preprint**, no journal reference on the arXiv record at evidence date | load-bearing input cited inside the odd-primary assembly; not an exact 2-descent source |
| Castella--Ciperiani--Skinner--Sprung | [arXiv:1804.10993](https://arxiv.org/abs/1804.10993) | public arXiv record | **public, unpublished input** as classified by Banwait--Huang Remark 2.11 | supersingular component of assembly |
| Keller--Yin | [arXiv:2402.12781](https://arxiv.org/abs/2402.12781) | public arXiv record | **public, unpublished input** as classified by Banwait--Huang Remark 2.11 | reducible ordinary component of assembly |

The LMFDB numerical analytic Sha value is corroboration only.  No twist BSD
claim below is inferred from an analytic-Sha database field.

## 2. Exact base row

The frozen ecdata row is:

```text
62a1 a 1 62.a4 a 4 0 0 1 62 [1,-1,1,-1,1]
[-35937,496] 0 [1,2,4] 1 0 -1 496 ...
bad primes [2,31]
Tamagawa numbers [4,1]
Kodaira codes [8,5] = [I4,I1]
reduction signs [1,-1] = [split,nonsplit]
rank 0
torsion order 4, structure [4]
real period 4.4349626414470361059448948451 (decimal corroboration)
special value 1.1087406603617590264862237112723341825 (decimal corroboration)
analytic Sha 1
```

The decimal database ratio is numerically `0.25`, but it is not promoted to
an exact rational value.  The exact certificate
`checker/exact_base_modular_symbol.gp`, replayed in
`evidence/EXACT_BASE_L_VALUE_RUN.txt`, isolates the plus Hecke eigenline,
computes its canonical integral lattice, and uses the one-real-component
normalization together with the bound Manin constant `1`.  It gives

\[
 \left|\frac{L(E,1)}{\Omega(E)}\right|=\frac14,
 \qquad v_2=-2.
\]

Thus the base facts used later are:

```text
Cremona label            = 62a1
LMFDB label              = 62.a4
minimal a-invariants     = [1,-1,1,-1,1]
conductor                = 62
minimal discriminant     = -496 = -2^4*31
optimality               = 1
Manin constant           = 1
CM                       = no
rank                     = 0
torsion                  = Z/4
bad local data           = 2:I4 split c4; 31:I1 nonsplit c1
abs(L(E,1)/full period) = 1/4
```

## 3. Rational model change and differential scaling

Start from the global minimal model

\[
 \mathcal E:\quad v^2+uv+v=u^3-u^2-u+1.
\]

Set

\[
 X=4u+4,\qquad Y=8v+4u+4.
\]

Its inverse is

\[
 u=X/4-1,\qquad v=(Y-X)/8.
\]

Direct substitution gives

\[
 Y^2=X^3-15X^2+64X.
\]

This is an admissible rational Weierstrass transformation with scale `2`.
For

\[
 \omega_{\min}=\frac{du}{2v+u+1},
 \qquad
 \omega_{\mathrm{short}}=\frac{dX}{2Y},
\]

the displayed formulas give

\[
 \omega_{\mathrm{short}}=\frac12\omega_{\min}.
\]

Correspondingly,

\[
 \Delta_{\mathrm{short}}=2^{12}\Delta_{\min}=-2^{16}\cdot31.
\]

The short equation is consequently not a Neron-minimal period model at `2`.
Every analytic formula below uses the Neron period of the minimal twist, not
the uncorrected short-model differential.

## 4. Quotient and isogeny orientation

For

\[
 E:y^2=x^3+Ax^2+Bx
\]

with kernel generated by `(0,0)`, the quotient model is

\[
 E':y^2=x^3-2Ax^2+(A^2-4B)x.
\]

Taking `A=-15`, `B=64` gives `A^2-4B=-31` and

\[
 E':y^2=x^3+30x^2-31x=x(x-1)(x+31).
\]

This quotient is Cremona `62a2` / LMFDB `62.a3`.  Its minimal model is

\[
 v^2+uv+v=u^3-u^2-21u+41,
\]

and the admissible change

\[
 X=4u-11,\qquad Y=8v+4u+4
\]

has inverse

\[
 u=(X+11)/4,\qquad v=(Y-X-15)/8
\]

and gives the displayed quotient equation.  Thus the quotient identification
is by a checked rational isomorphism, not a label transfer.

Quadratic twisting is functorial under rational isomorphism.  For a positive
prime `q`, this gives

\[
 E_q:y^2=x^3-15q x^2+64q^2x
\]

and

\[
 E'_q:y^2=x^3+30q x^2-31q^2x=x(x-q)(x+31q).
\]

Away from the kernels, the maps are

\[
 \phi_q(x,y)=
 \left(\frac{y^2}{x^2},
       \frac{y(64q^2-x^2)}{x^2}\right),
\]

\[
 \widehat\phi_q(X,Y)=
 \left(\frac{Y^2}{4X^2},
       \frac{Y(-31q^2-X^2)}{8X^2}\right).
\]

They extend across the kernels and satisfy

\[
 \ker\phi_q=\{O,(0,0)\}\subset E_q,
 \quad
 \ker\widehat\phi_q=\{O,(0,0)\}\subset E'_q,
 \quad
 \widehat\phi_q\circ\phi_q=[2].
\]

For the `phi_q` Kummer map from `E'_q(Q)/phi_q(E_q(Q))`, use the
`x`-coordinate away from `(0,0)` and the squareclass of the coefficient
`-31q^2` at `(0,0)`.  The four rational 2-torsion points give

| point on `E'_q` | Kummer squareclass |
|---|---|
| `O` | `1` |
| `(0,0)` | `-31` |
| `(q,0)` | `q` |
| `(-31q,0)` | `-31q` |

This proves only the lower bound

\[
 \{1,-31,q,-31q\}\subseteq\operatorname{Sel}^{(\phi_q)}(E_q/\mathbf Q).
\]

It does not exclude additional Selmer classes.  The reverse inclusion and
the triviality of the dual Selmer group remain the theorem-bearing proof
obligation in `TARGET.md`.

## 5. Prime-family and infinitude check

The frozen family is

\[
F_{62}=\{q:\ q\text{ prime},\ q\nmid372,\ q=5\bmod8,
(q/31)=-1,\ v_2(\#E(\mathbf F_q))=2,\ a_q(E)\ne0\}.
\]

For `q=13`, exact enumeration on the minimal model gives

```text
#E(F_13) = 12
a_13     = 13+1-12 = 2
13 mod 8 = 5
13^15 mod 31 = 30, hence (13/31) = -1
```

The affine points found were

```text
(1,0), (1,11), (4,1), (4,7), (5,9), (5,11),
(8,6), (8,11), (11,6), (11,8), (12,0)
```

together with the point at infinity.

For good odd primes, `#E(F_q) mod 8` is determined by the conjugacy class of
Frobenius on `E[8]`; the congruence and Legendre conditions are Frobenius
conditions in cyclotomic/quadratic subextensions.  Since `13` is unramified
in the finite compositum and supplies one such Frobenius element, Chebotarev
gives a positive-density conjugacy set.  Removing the finite set dividing
`372` leaves infinitely many primes.

The separately printed condition `a_q(E)!=0` is redundant on this signature:

\[
 q=5\pmod8,\quad \#E(\mathbf F_q)=4\pmod8
 \quad\Longrightarrow\quad a_q(E)=q+1-\#E(\mathbf F_q)=2\pmod8.
\]

In particular every prime in the Chebotarev set is ordinary for `E`.

## 6. Uniform local and Tamagawa calculation

### At `2`

The base has split multiplicative type `I_4`, `c_2=4`.  A unit
`q=5 mod 8` represents the unique unramified nonsquare quadratic class over
`Q_2`.  Twisting the split multiplicative character by that unramified
quadratic character changes split to nonsplit without changing `I_4` or the
minimal-discriminant valuation.  For nonsplit `I_n`, the component number is
`1` for odd `n` and `2` for even `n`.  Hence

\[
 E_q/\mathbf Q_2:\quad I_4\text{ nonsplit},\qquad c_2=2,
 \quad v_2(\Delta_{\min})=4,
 \quad f_2=1.
\]

This transition is also covered by the characteristic-2 tables in Barrios
et al., Theorem 5.1/Tables 5--6.

### At `31`

The base has nonsplit multiplicative type `I_1`, `c_31=1`.  Since
`(q/31)=-1`, the unramified quadratic twist toggles it to split
multiplicative `I_1`; the component number remains `1`:

\[
 E_q/\mathbf Q_{31}:\quad I_1\text{ split},\qquad c_{31}=1,
 \quad v_{31}(\Delta_{\min})=1,
 \quad f_{31}=1.
\]

### At the new prime `q`

The base has good reduction at `q`.  An odd ramified quadratic twist has
type `I_0^*`, minimal-discriminant valuation `6`, and conductor exponent `2`.
The normalized component polynomial is

\[
 P(T)=T(T^2-15T+64).
\]

Its quadratic discriminant is `-31`.  As `q=1 mod 4`, quadratic reciprocity
gives

\[
 \left(\frac{-31}{q}\right)
 =\left(\frac{31}{q}\right)
 =\left(\frac q{31}\right)=-1.
\]

Thus `P` has exactly one root over `F_q`.  Barrios et al., Theorem 4.1,
Table 4, gives

\[
 c_q=1+\#\{\alpha\in\mathbf F_q:P(\alpha)=0\}=2.
\]

### Global output

There are no other bad finite places, so

```text
minimal discriminant = -2^4*31*q^6
conductor            = 62*q^2
Tamagawa product     = 2*1*2 = 4
v2(Tamagawa product) = 2
```

### Independent sample corroboration, not uniform proof

For `q=13`, the twist is Cremona `10478e1`, LMFDB `10478.f4`.  The public
[LMFDB local-data API](https://www.lmfdb.org/api/ec_localdata/?lmfdb_label=10478.f4&_format=json)
returns

| prime | discriminant valuation | conductor valuation | Kodaira code | split sign | Tamagawa |
|---:|---:|---:|---:|---:|---:|
| `2` | `4` | `1` | `8 = I4` | `-1` | `2` |
| `13` | `6` | `2` | `-1 = I0*` | `0` | `2` |
| `31` | `1` | `1` | `5 = I1` | `+1` | `1` |

The sample matches the symbolic table.  It is not used to establish
uniformity in `q`.

## 7. Exact torsion calculation

The 2-division cubic is

\[
 x(x^2-15qx+64q^2).
\]

The quadratic factor has discriminant `-31q^2`, which is not a square in
`Q`.  Therefore

\[
 E_q(\mathbf Q)[2]=\{O,(0,0)\}\simeq\mathbf Z/2.
\]

For a point `P=(x,y)` on `y^2=x^3+ax^2+bx`, the duplication formula gives

\[
 x(2P)=\frac{(x^2-b)^2}{4y^2}.
\]

If `2P=(0,0)` on `E_q`, then `x^2=64q^2`, so `x=+/-8q`.  At `x=8q`,

\[
 y^2=64q^3,
\]

which is not a rational square because `q` is prime.  At `x=-8q`, the
right-hand side is `-1984q^3<0`.  Hence `(0,0)` is not rationally divisible
by `2` and there is no rational point of order `4` or higher 2-power order.

The base `62a1` has no rational `3`-, `5`-, or `7`-isogeny.  For odd `ell`,
the representations of a quadratic twist satisfy

\[
 E_q[\ell]\simeq E[\ell]\otimes\chi_q.
\]

Tensoring by a scalar character does not change Galois-stable lines.  Thus a
rational odd-order torsion point on the twist would force a rational
odd-prime isogeny of the base.  Mazur's torsion theorem leaves no other odd
torsion prime.  Therefore

\[
 E_q(\mathbf Q)_{\mathrm{tors}}\simeq\mathbf Z/2,
 \qquad v_2(\#E_q(\mathbf Q)_{\mathrm{tors}})=1.
\]

## 8. Zhai analytic theorem and period audit

Zhai defines

\[
 L^{(\mathrm{alg})}(E^{(M)},1)
   =L(E^{(M)},1)/\Omega^+_{E^{(M)}},
\]

where `Omega+` is the least positive real period of a Neron differential.
Theorem 1.5, journal p. 478, assumes negative discriminant, rational
2-torsion, `M=epsilon*q=1 mod 4`, and

\[
v_2(\#E(\mathbf F_q))=-v_2(L(E,1)/\Omega_E^+)\ne0.
\]

For `62a1`, the discriminant is negative, `Omega(E)=Omega_E^+`, and the
exact integral modular-lattice certificate in
`checker/exact_base_modular_symbol.gp` gives absolute base ratio `1/4` and
therefore valuation `-2`.  Also, `q in F_62` has `q=1 mod 4` and
point-count valuation `2`.  Thus every hypothesis specializes exactly, with
`M=q`.  The conclusion is

\[
L(E_q,1)\ne0,
\qquad
v_2(L(E_q,1)/\Omega^+_{E_q})=0,
\]

and finiteness of `E_q(Q)` and `Sha(E_q/Q)`.  The proof on journal pp.
487--488 is analytic/modular-symbolic; it does not prove the frozen Selmer
identities.

The positive twist has

\[
\Delta_{\min}(E_q)=q^6\Delta_{\min}(E)<0,
\]

so `E_q(R)` has one connected component and
`Omega(E_q)=Omega^+_{E_q}`.  Therefore

\[
v_2(L(E_q,1)/\Omega(E_q))=0.
\]

No positive-discriminant factor of `2` occurs, and no decimal period ratio is
used to decide this valuation.

## 9. Conditional full-2-Selmer calculation

Assume, and do not claim to prove here,

\[
\#\operatorname{Sel}^{(\phi_q)}(E_q)=4,
\qquad
\#\operatorname{Sel}^{(\widehat\phi_q)}(E'_q)=1.
\]

The exact comparison sequence begins

\[
0\to
E'_q(\mathbf Q)[\widehat\phi_q]/\phi_q(E_q(\mathbf Q)[2])
\to\operatorname{Sel}^{(\phi_q)}(E_q)
\to\operatorname{Sel}_2(E_q)
\to\operatorname{Sel}^{(\widehat\phi_q)}(E'_q).
\]

The first nonzero term has order `2`: the numerator is the order-`2` dual
kernel and the denominator is trivial because `E_q(Q)[2]=ker(phi_q)`.  Since
the final group is trivial, exactness gives

\[
\#\operatorname{Sel}_2(E_q)=4/2=2.
\]

The Kummer exact sequence

\[
0\to E_q(\mathbf Q)/2E_q(\mathbf Q)
\to\operatorname{Sel}_2(E_q)
\to\Sha(E_q)[2]\to0
\]

has first term of order `2`, from rank zero and torsion `Z/2`.  Hence

\[
\Sha(E_q)[2]=0.
\]

Since Zhai supplies finiteness of Sha, this is equivalent to

\[
\Sha(E_q)[2^\infty]=0.
\]

## 10. Conditional `BSD(E_q,2)` calculation

Banwait--Huang Definition 2.3 defines `BSD(E/Q,2)` to include rank equality,
finiteness of the 2-primary Sha, rationality of the analytic Sha order, and
equality of its 2-adic valuation with the actual 2-primary Sha order.

Rank zero makes the regulator `1`.  The analytic Sha order is

\[
\#\Sha(E_q)_{\mathrm{an}}
=\frac{L(E_q,1)}{\Omega(E_q)}
 \frac{\#E_q(\mathbf Q)_{\mathrm{tors}}^2}
      {\prod_p c_p(E_q)}.
\]

The established inputs give

```text
v2(L/Omega)       = 0
2*v2(#torsion)    = 2
v2(product c_p)   = 2
v2(#Sha_an)       = 0
```

The assumed Selmer theorem gives actual `Sha[2^infinity]=0`, also valuation
`0`.  Zhai/Kolyvagin gives rank equality and finiteness; modular-symbol
rationality gives the remaining clause.  Thus the Selmer theorem implies

\[
\operatorname{BSD}(E_q/\mathbf Q,2).
\]

This conclusion is an exact valuation identity, not merely the statements
`rank=0` and `Sha[2]=0`.

## 11. Banwait--Huang Theorem 2.13 audit

Use `d=q`.  Since `q=1 mod 4`, the discriminant of `Q(sqrt(q))` is `D=q`.

| hypothesis | exact evidence |
|---|---|
| `E` semistable | `N=62` squarefree; local types `I4`, `I1` |
| `(D,3N)=1` | literal `q does not divide 372` |
| `L(E_q,1)!=0` | Zhai Theorem 1.5 |
| `BSD(E_q,2)` | Section 10, conditional only on the frozen Selmer theorem |
| `a_3(E)` in the stated set | direct count gives `#E(F_3)=4`, hence `a_3=0` |
| no rational `3,5,7` isogeny | frozen isogeny data has prime-degree isogenies `[2]` only |
| for `p=2`, a different multiplicative ramification witness | use `31`, with `v_31(Delta_min)=1`, not divisible by `2` |
| for `p=31`, a different multiplicative ramification witness | use `2`, with `v_2(Delta_min)=4`, not divisible by `31` |
| ordinary at the prime dividing `d` | `a_q!=0`; indeed the frozen signature gives `a_q=2 mod 8` |

At a multiplicative prime `r != p`, the residual representation is ramified
when `p` does not divide `v_r(Delta_min)`, which supplies the two witnesses
in the table.

Therefore Theorem 2.13 gives `BSD(E_q,p)` for every odd prime `p`.  Combining
it with Section 10 and the positive real-place statement yields the exact
strong rank-zero BSD formula.

### Qualification of this arrow

Banwait--Huang is a publicly retrievable preprint, not yet a published
journal article at the evidence date.  Its Remark 2.11 expressly marks the
following dependencies as unpublished: the BSTW and CCSS inputs used in
its Cases 1/4, and Keller--Yin for the reducible ordinary case.  These are
public preprints, so the implication is available under the project's
**public-source** standard, but it is not an **all-published** implication
chain.

## 12. Priority and authority boundary

The source audit located no public source-complete proof of the exact
oriented Selmer identities.  Zhai 2016 p. 480 asserts that a classical
2-descent is straightforward, and historical Wan/BSTW texts attribute the
named curve family to Zhai, but their load-bearing theorems assume the
2-primary input and do not contain this calculation.  Banwait--Huang 2026
identifies the resulting public proof gap.

Accordingly:

```text
PUBLIC_SOURCE_COMPLETE_BLOCKER = NO_LOCATED
PUBLIC_SOURCE_TARGET_FREEZE     = PRESERVED
PRIVATE_PRIORITY                = UNRESOLVED
ABSOLUTE_NOVELTY                = NOT_CLAIMED
SELMER_IDENTITIES               = UNPROVED_HERE
SAMPLE_Q13                      = CORROBORATION_ONLY
STRONG_BSD_ARROW                = PUBLIC_PREPRINT_QUALIFIED
ARISTOTLE                       = NOT_USED_NOT_AUTHORIZED
```

This evidence supports the implication chain only.  It must not be used to
mark the local Selmer proof, certificate, or independent-review gates as
complete.
