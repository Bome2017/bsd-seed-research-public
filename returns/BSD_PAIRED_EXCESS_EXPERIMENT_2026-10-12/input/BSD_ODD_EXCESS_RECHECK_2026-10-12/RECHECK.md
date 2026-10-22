# Positive odd-primary excess: exact recheck and paired-isogeny test

Date: 2026-10-12. Input: `Bome2017/bsd-seed-lab@f97843a1b4768606787a9760ea4bad727a3dc4a1`,
`work/returns/BSD_ODD_EXCESS_CONTROL_EXPERIMENT_2026-10-12/`.

**Disposition: LOWER_BOUND_SUPPORTED_UNDER_RETAINED_RANK_INPUT; SAVED_DIGITS_CHECK;
PAIRED_ISOGENY_QUOTIENT_IDENTITY_DERIVED.**

This is one assistant's written review with a separately implemented exact Python check.
It is not independent human review, a proof-assistant certificate, or a replay of the
PARI overconvergent numerator. The original repository was not modified. Constants in
the checker are transcribed from the pinned proof and outputs; no unseen local ZIP
is claimed to have been read. No new seed coefficient or seed bound is supplied.

## 1. Objects and the retained rank input

Use the two displayed minimal models

```
A = [0,0,1,-19766893413,-1937478573143510]
F = [0,0,1,-14959712463303,-22270654620235278500]
d = 43737 = 3*61*239
```

and the pairs P1,P2 on A and Q1,Q2 on F in the input proof. The exact checker verifies
their curve equations, the quadratic-twist model changes, and both isogeny images.

The input's PARI `ellrank` output bounds rank(A) above by two. **That upper bound is
retained, not rerun here.** The isogeny transfers it to F. Both displayed pairs are
independent modulo 5 by the reduction tests below, so both ranks equal two conditional
on this upper bound. The official PARI documentation describes the bounds returned
by `ellrank`; it is not an analytic-rank/BSD estimate.

The curve F in this note is an elliptic curve, not the quintic field denoted F in
older lab returns.

## 2. Exact checks that were actually executed

The separately written `verify_exact.py` checks, with integer/rational arithmetic:

* the degree-five rational map's polynomial identity and its noncancellation;
* the differential pullback phi*omega_F = omega_A;
* phi(P1) = -Q1-Q2 and phi(P2) = 3Q1-2Q2;
* the two real kernel x-coordinates, with their completed-square values/d positive squares;
* point-group operations and reduction certificates at 7 and 19;
* good-reduction counts at 5,7,13,19, excluding all rational torsion;
* discriminants, minimality and the particular Tate-algorithm branches at all bad primes;
* the quotient's leading digit from the saved p-adic numerator/regulator digits.

The point matrix (columns are images of P1,P2) is

```
M = [[-1,3],[-1,-2]],  det(M)=5.
```

The independently chosen generators of the reduction groups give rows

| Pair | q=7 row | q=19 row | determinant mod 5 |
| --- | --- | --- | --- |
| A: P1,P2 | (4,4) | (4,3) | 1 |
| F: Q1,Q2 | (3,2) | (4,0) | 2 |

The source used different generators, so its row entries and the F determinant need
not match these numbers. Both matrices are invertible; this is the invariant test.
The homomorphisms are reduction followed by multiplication by #E(F_q)/5 and discrete
logarithm in the chosen order-five subgroup. They kill rational five-multiples.
Together with the retained rank bound and absence of rational 5-torsion, they certify
that the two pairs are bases after tensoring with Z_5. No saturation away from 5 is
claimed.

Both curves have counts 7,10,18,20 over F_5,F_7,F_13,F_19, respectively. Prime-to-q
torsion injectivity at these good primes excludes all rational torsion, without
using PARI's torsion output.

## 3. Fresh local-factor check

The discriminants are exactly

```
Delta_A = -11^5*d^6
Delta_F = -11*d^6.
```

Their exponents are below 12, so the displayed integral models are minimal.
At 11 the c4 value is a unit and -c6 is a nonzero square modulo 11. The reduction
is split I5 on A and split I1 on F.

At q=3,61,239, complete the square Y=y+1/2 and set x=X+r, using r=1 for q=3
and r=0 for q=61,239. In these q-integral coordinates a1=a3=0 and

```
a2=3r, a4=3r^2+a, a6=r^3+a*r+b+1/4.
```

The code verifies q|a2, q^2|a4, q^3|a6 and failure of the earlier II/III/IV
exit tests. The I0* test is the separable cubic

```
t^3 + (a2/q)t^2 + (a4/q^2)t + a6/q^3   mod q.
```

Its root counts are 0,1,1 at q=3,61,239 for each curve. The constant 1/4 is q-integral
throughout; it is not rounded. The relevant Tate branch gives c_q=1+(number of roots)
and conductor exponent v_q(Delta)-4. This also handles residue characteristic 3;
no p>3-only shortcut was used there. See Cremona, Chapter 3, Section 3.2, printed p.67.

Thus the full table, independently recovered here, is

| q | A reduction | c_q(A) | F reduction | c_q(F) |
| --- | --- | --- | --- | --- |
| 3 | I0* | 1 | I0* | 1 |
| 11 | split I5 | 5 | split I1 | 1 |
| 61 | I0* | 2 | I0* | 2 |
| 239 | I0* | 2 | I0* | 2 |

Both conductors are 11*d^2=21042176859; C_A=20, C_F=4. These are new local rechecks,
not a claim that the whole original PARI computation was repeated.

## 4. The independent Sha lower bound has the right direction

The exact kernel calculation gives all five phi-kernel points over R. Both real
loci are connected (negative discriminant), and phi*omega_F=omega_A, so

```
Omega_F / Omega_A = 1/5.
```

With trivial rational torsion, Cassels' isogeny-Selmer formula, as printed in
Miller--Stoll Section 6, gives

```
#Sel_phi(A) / #Sel_phihat(F) = (Omega_F/Omega_A)*(C_F/C_A) = 1/25.
```

This theorem concerns finite isogeny Selmer groups and does not require Sha finite.
The point index is exactly 5: the matrix has determinant 5 on the Z_5 point lattices,
and the rational isogeny quotient is killed by 5. The dual point index is also 5
because phihat*phi=[5] and the rank is two. Therefore both isogeny Kummer sequences
have one-dimensional Mordell--Weil terms, and subtraction proves

```
dim_F5 Sha(F)[phihat] - dim_F5 Sha(A)[phi] = 2.
```

In particular Sha(F)[phihat] is a subgroup of Sha(F)[5] of dimension at least two.
This supports the input's lower bound under the retained rank-upper-bound computation.
It neither proves an upper bound on these dimensions nor proves primary finiteness.
No L-value, regulator, or BSD equality enters this argument.

## 5. Saved numerator digits and their correct scope

The actual overconvergent-symbol calculation remains the input producer's calculation.
Its source code computes the twisted modular-symbol numerator before the regulator;
no Sha value or regulator is passed to that numerator routine. The p-adic computation
was not rerun here, and its implementation/error bounds are retained.

From the saved digits:

```
J_F = 4*5^4 + O(5^5)
L2_F = 4*5^2 + O(5^3)          [also directly extracted from the series]
R_scalar,F = 4*5^2+4*5^3+4*5^4+3*5^5+4*5^7+3*5^9+O(5^10).
```

The independent rational log-series/Hensel arithmetic recovers

```
det H_U,F = 1419 mod 5^8,
v5(det H_U,F)=0,
epsilon=(1-alpha^-1)^2 = 4 mod 5,
Q_F/25 = 4/(4*4*4) = 1 mod 5.
```

Here Q_F = L2_F/(epsilon*det H_U,F)*torsion_F^2/C_F, with the specified point pair,
common gamma=6 and minimal Neron period. Thus Q_F=25+O(125) and its valuation is
exactly two at the reported precision. This is not a proof that Q_F is exactly 25.
The pair's possible prime-to-5 index affects units of a full-basis quotient, not
its 5-valuation. The comparison is consequently kept on the named point pair.

## 6. A paired-isogeny identity: new written deduction, not a new numerator run

Retain the standard Neron-period ordinary measures and the canonical ordinary
cyclotomic height pairing in one common character coordinate. Let H_A and H_F be
their matrices on P1,P2 and Q1,Q2. The two curves have the same newform and the same
ordinary Euler factor. Their period ratio therefore gives the exact measure identity

```
L_std,F = 5 L_std,A,  hence L2_F=5 L2_A.
```

This follows from the identical interpolated twists divided by their different
Neron periods. It is not obtained by multiplying by an assumed Sha ratio.

Isogeny functoriality of the canonical height gives

```
h_F(phi(P),phi(R)) = h_A(P,phihat*phi(R)) = 5 h_A(P,R).
```

The same ordinary unit-root splitting must be used: this is the canonical height,
not an arbitrary numerical pairing. The unit-root subspace is functorial under the
isogeny on de Rham cohomology, and Poincare-biextension duality identifies the adjoint
with the dual isogeny. Thus

```
M^t H_F M = 5 H_A.
```

Taking determinants in rank two and using det(M)=5 proves **det(H_F)=det(H_A)** on
these named pairs. This does not assert an integral Tate-lattice isomorphism across
a degree-five isogeny.

Consequently the two fully corrected point-pair quotients satisfy

```
Q_F/Q_A = (L2_F/L2_A)*(det(H_A)/det(H_F))*(C_A/C_F) = 5*1*5 = 25.
```

The formula applies wherever the nonzero quotient is defined; the saved F numerator
and regulator make it applicable here. It gives

```
L2_A = 4*5 + O(5^2),    det(H_A)=det(H_F),    Q_A=1+O(5).
```

These A-side values are **derived through the isogeny**, not independently computed
A-side values. A new independent A numerator run would test this identity and the
software conventions, but no such run is claimed in this return.

For the mathematical height input, see Iovita--Werner for the ordinary unit-root
height and functorial unit-root splitting, and the canonical pullback/tensor
properties of symmetric line-bundle logarithms in Besser--Mueller--Srinivasan,
Lemma 4.31 and Section 5. The displayed rank-two matrix/determinant calculation is
our deduction from those standard functorial properties and the exact point map.
This is not an application of a full-residual-image Kato bound to a reducible
representation.

## 7. Consequence for mechanism testing

The paired data separate three valuations:

| Curve | v5(L2) | v5(det H_U) | v5(C) | fully corrected quotient valuation |
| --- | --- | --- | --- | --- |
| A (derived through phi) | 1 | 0 | 1 | 0 |
| F (input's numerator, rechecked digits) | 2 | 0 | 0 | 2 |

The F excess is not manufactured by a missing Tamagawa factor or an unsaturated
five-adic point pair: those checks have been made, and the isogeny-Selmer argument
independently proves nonzero Sha[5]. But the observed quotient is not automatically
an exact Sha order, nor has Sha(A)[5] been proved zero by the unit A quotient.

The control falsifies an unconditional rule that rank two, good ordinary
non-anomalous reduction and regulator correction alone force zero excess. It does
not falsify a rule that also assumes full residual image, since this control has a
rational 5-isogeny. Nor does it establish such a full-image rule. An explanation
intended for the seed must make its residual-image, local-factor and lattice
hypotheses explicit and treat the known cancellation examples as well as this
positive-excess example.

A combined full-image/nonunit-regulator/independently proved odd-excess control
remains absent from the inspected panel. That is a limit of the current experiment,
not a reason to dismiss the real arithmetic content of this positive control.
No seed FIN, ORDER9, Q36 or new primary result is asserted.

## 8. Reproduction and custody

Run, with Python 3.10+ and SymPy installed:

```
python verify_exact.py > reproduced.json
cmp reproduced.json RESULTS.json
sha256sum -c SHA256SUMS
```

Only the named public theorem inputs and pinned research inputs enter the deduction.
`SOURCES.json` records URLs, scopes and read Git blobs; those references are not full
byte-for-byte source copies. Third-party papers are not included. Two exact checker
runs were compared byte-for-byte. The small Tate branches and polynomial/rational
checks are computationally executed; the source theorems are not proved in code.
