# Match to the same integral local frame

Grade: DERIVED under the local calculation and retained Kato datum.
The exact modular-to-local comparison scalar remains explicit and
unevaluated. This is not a completed global period/unit calculation.

## 1. Keep Kato's own period convention

At weight k=3 and Kato twist r=1, Kato 14.13 (printed p.242) identifies
the dual-exponential image with an element of S(g) whose period image is

    per_g^+(exp*(loc z_g)) = L_{ {p} }(g,2) gamma^+.

Here gamma^+ is exactly the primitive period vector used to normalize
the retained integral zeta element. Inserting a different 2pi i or a
new period convention without transporting this identity is forbidden.

Choose a nonzero rational de Rham vector w_g in S(g), extended to the
actual coefficient field. Define Omega_g by

    per_g^+(w_g)=Omega_g gamma^+.

Define c_g, without a unit assumption, by transporting through the
specified Kato/Bloch--Kato target identification and (3) of
LOCAL_LATTICE.md:

    w_g=c_g e_g.

In these conventions explicit reciprocity gives

    xi_g = c_g L_{ {p} }(g,2)/Omega_g.                (1)

The critical L-value divided by Omega_g is taken through its algebraic
realization and the chosen p-adic embedding. We are not assigning a
p-adic valuation to an arbitrary complex number. Multiplying w_g by
a rational nonzero scalar multiplies c_g and Omega_g by the same
scalar, so their occurrence in (1) is invariant.

## 2. The p-Euler denominator cancels the calculated local lattice

The primitive g has ramified nebentypus omega^{-1} at p. Its ordinary
local factor has degree one, with unit U_p eigenvalue a_p(g). Hence

    L_{ {p} }(g,2)=(1-a_p(g)/p^2)L(g,2).

Set

    A_g := c_g L(g,2)/Omega_g.

Substitution into (12) of LOCAL_LATTICE.md gives the exact identity

    p^2 xi_g = (p^2-a_p(g)) A_g,
    b_g = v_pi(A_g),                                (2)

since p^2-a_p(g) is an O-unit. All Gauss and local lattice factors
remain in the definition of the fixed e_g and therefore c_g; none has
been silently dropped. Ordinary dual-exponential conventions may
alter both sides by a unit but do not alter (2).

The retained integrality and b_g>=2 consequently prove A_g in pi^2 O.
This is a LOWER divisibility statement, not the upper bound we need.
The precise remaining sufficient statement in this normalization is

    A_{g_p} not in pi_p^4 O_p                        (3)

for suitable retained specializations outside a finite set of ordinary
primes, with no uncontrolled changes of coefficient lattice. Together
with the retained parity, (3) would imply primary vanishing there.

This formula removes the unknown local denominator d_g. It does not
evaluate c_g or prove (3). Calling A_g a normalized critical value is
not a bound on it and not a claim of identity with the old scalar C_p.

## 3. What the canonical-family reference does and does not give

Loeffler--Rivero, section B4.4 and Remark B4.2, choose the canonical
de Rham vector eta_f and state a reciprocity law with Ochiai's basis
corrections equal to one. The statement is over an analytic family
algebra O(V1), after inverting p. Section B4.1 also expressly allows
non-rational specializations of the family period bases. Its displayed
classical interpolation in B4.2 is stated for newforms of tame level N,
not as the missing integral proof for this ramified omega^{-1} point.

It does not establish that its chosen vector generates the integral
lattice in (11), or that c_g in (1) is a unit. Over a p-adic analytic
field algebra multiplication of a basis by p is invertible; over O it
changes the lattice. A canonical rational basis alone cannot settle
this comparison.

Ochiai's integral Theorem 3.13 retains a pseudo-null cokernel and has
Gorenstein, normality and (MW) hypotheses. One cannot discard its
specialization defect or apply it to every retained branch without
checking those hypotheses. This return instead computes the local
specialization directly by (6)-(10) of LOCAL_LATTICE.md. It does not
use these family statements to set c_g=1.

The first unfinished GLOBAL task is a lattice-accurate comparison of
this local frame with a period-normalized integral Kato/Hida value,
followed by an independent upper bound on that value's divisibility.
Merely choosing a name for c_g or a rationally canonical basis does
not complete either task.
