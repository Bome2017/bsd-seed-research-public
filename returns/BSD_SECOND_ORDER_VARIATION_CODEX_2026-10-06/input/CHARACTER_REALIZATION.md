# The proposed formal-character stage fails; its mixed-characteristic replacement

2026-10-06. **WRITTEN_DERIVATION; INDEPENDENT_REVIEW_REQUIRED.**

## 1. A finite-order obstruction before any Selmer calculation

Let q!=p and let chi be a continuous scalar character of G_(Q_q) into
1+t k[[t]], k=F_p. In the local abelianization, the pro-p inertia quotient
is finite of order p^a, a=v_p(q-1). One way to see this is local reciprocity:
inertia corresponds to Z_q^*, whose principal units are pro-q and whose
residue units have order q-1. A pro-q group has no nontrivial continuous
image in a pro-p group. Equivalently use tame Frobenius conjugation.

But 1+t k[[t]] has no nontrivial finite-order element. If
u=1+c t^r+... with c!=0, then u^(p^a) has first nonconstant term
c^(p^a)t^(r p^a). Raising further to a prime-to-p power cannot remove it.
Thus chi is unramified at q.

In particular, a direction lambda with lambda(I_q)!=0 cannot be the
linear term of such a character. Every nonzero direction in our D has
nonzero tame inertia at some q: characters of distinct prime conductors
are independent on their inertia groups.

This is already visible at a finite Artin order. For a hypothetical lift

    chi(tau)=1+c t+... mod t^(p^a+1),   c!=0,

the local abelian inertia relation forces chi(tau)^(p^a)=1, but the
coefficient of t^(p^a) in that power is c^(p^a)!=0. No higher coefficient
can repair it. If a=1, failure occurs no later than the ring k[t]/t^(p+1).
This does not contradict the actual order-three and order-four characters.

Adding new tame conductors at later orders does not remove this obstruction
at the already ramified q. Nor does allowing an arbitrary matrix correction
at higher orders while retaining the SAME scalar first-order direction:
the determinant of rho_t/rho has first term 1+2t lambda. Since p>=5,
the scalar determinant has the same forbidden ramified linear term.

The last assertion means det(rho_t)/det(rho), with rho viewed as a
constant k-representation, not a division of matrices.

## 2. Precise correction to the proposed workflow

The chain in the supplied review included a stage called FORMAL_W_LIFT,
envisaging compatible lifts at every k[t]/t^n order and then generic
sections. For the nonzero scalar tame directions actually constructed in
Stage A, the CHARACTER itself cannot pass this stage over k[[t]].
This is a proved failure of that implementation, not merely a presently
missing theorem about point sections.

This is NOT a refutation of the source manuscript's moving-prime formalism.
The bound `OPENAI_04_VERTICAL.tex`, opening subsection, distinguishes its
torsion-free cyclotomic/anticyclotomic variable from artificial tame variables
formed from sequences of DISTINCT conductors with increasing p-power orders.
Changing conductors and replacing the limiting object is a different
construction. It does not give compatible lifts of the fixed global
character lambda considered here. No assertion about all such moving-prime
limits is proved in this return.

It does not refute Stage A or the finite second-order calculations. It
does refute treating those Artin characters as an automatically available
equal-characteristic family with nonzero generic parameter.

Even in a different setting where compatible lifts exist, the passage to
generic sections requires an actual compatible arithmetic representation,
local conditions and a cohomological limit argument. Compatibility cannot
be replaced by unrelated solutions at each order.

## 3. A concrete characteristic-zero character really does exist

For an actual additive direction lambda:G_Q -> F_p define

    O=Z_p[zeta_p],  pi=zeta_p-1,
    chi_lambda(g)=zeta_p^[lambda(g)],
    T_lambda=T_p(E) tensor_(Z_p) O(chi_lambda).

The exponent is any integer representative of lambda(g); changing it by
p changes nothing. This is an actual continuous finite-order character,
with exactly the ramification of lambda and locally trivial at Sigma.
The ambient representation is defined without Sha or a leading-term
conjecture. It is NOT a construction of point sections in its Selmer group.

For completeness, the polynomial

    Phi_p(1+X)=p+binom(p,2)X+...+X^(p-1)

is Eisenstein. Hence pi is a uniformizer and p is a unit times pi^(p-1).
For p>=5, O/pi^3 has characteristic p. In this quotient set

    u=pi-pi^2/2.

This is a uniformizer coordinate, with inverse pi=u+u^2/2. Therefore

    zeta_p^[lambda(g)]
      =1+u lambda(g)+u^2 lambda(g)^2/2 mod u^3.

Also T_p(E) mod p=V. Consequently T_lambda/pi^3 is exactly the M3
used in SECOND_ORDER_PROOF.md after this coordinate change, and its
first-order quotient is M2. At these orders the stated local conditions
match coefficientwise at Sigma and are zero at the new acyclic primes.

IMPORTANT: u is a truncated POLYNOMIAL coordinate. It is not the p-adic
logarithm of zeta_p; that logarithm is zero. Applying a formal logarithm
beyond its justified truncated range would recreate the characteristic
error we have just removed.

## 4. Why the repair is not a free higher-order lifting theorem

For the fixed order-p character, the second additive character eta is
not freely variable. Once lambda is specified, chi_lambda is fixed (up
to changing the generator of mu_p and the coefficient coordinate).
In an exponential coordinate, such coordinate changes add only a scalar
multiple of lambda to eta. Its first-order pairing already vanishes on W.
An independently chosen eta from D need not be realized by this character.

There is a usable finite-order repair: choose lambda with ker b_lambda=W.
Then the theorem in SECOND_ORDER_PROOF.md shows that alpha_lambda=0 is
equivalent to lifting BOTH known classes through pi^2 in T_lambda,
after changing the first lifts. No free eta is needed.

Past this order one must work in O, not silently continue in k[[u]]. At
order pi^(p-1), p is no longer zero at the next quotient. Lifting the
underlying elliptic representation and its local Kummer conditions now
enters as well as the character. The existence of chi_lambda does not
make either rational-point class lift through all these mixed-characteristic
orders. No generic rank-two Selmer statement has been proved here.

Nor would rank-two generic sections alone bound the original seed Selmer
group. The independent specialization/index and cross-prime support
obligations recorded in Stage A remain.

## 5. Disposition

Stop the equal-characteristic scalar FORMAL_W_LIFT implementation.
Preserve Stage A and the finite-order second-pairing calculation.
The characteristic-zero representation above repairs the character's
existence, but its rank-two point lifting and specialization control
remain research tasks. This return does not recommend an automatic large
campaign or a determinant-switch job.

The next specific seed calculation would have to show, for useful
directions lambda with ker b_lambda=W, that alpha_lambda vanishes, using
the actual Kummer cocycles and local conditions. No successful example
of that arithmetic calculation is supplied here; synthetic algebra checks
are explicitly not substitutes.
