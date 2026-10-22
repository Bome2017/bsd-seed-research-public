# Collision audit: the normalized residual comparison is not yet available

The mandated collision test has been investigated against the actual retained
objects. It has **not passed**: equation (1) of the supplied brief is still
unproved in the required lattice. Nor has a collision been proved. No
`W3_COLLAPSES_TO_EXISTING_WITNESS` verdict is justified by this return.

The constructed integral value is M_p=E_2(phi_g). The retained index is
b_p=v_p(eta_p M_p). Until eta_p is a unit (or its exact valuation is proved),
one cannot substitute p^(-2)M_p mod p for p^(-2)A_g mod p.

## The retained objects, with their different domains

| Object | Actual construction | What is retained | Missing comparison to the constructed W3 value |
|---|---|---|---|
| Two-prime C_p | Coherent residual Kato/Kurihara system for the weight-two seed; delta_ab=C_p e_a e_b D_ab^2 | C_p nonzero iff Sha[p^infinity]=0 on its retained theorem domain | A lattice-preserving map from the weight-three critical specialization to this coherent weight-two system |
| Tame singleton C2(theta_l) | Quadratic augmentation coefficient of a one-auxiliary-prime weight-two Mazur--Tate element | Theorem W uses (a_l-2) and the tame regulator; the admissible primes here are not the cyclic Kato-prime condition a_l=2 mod p | An integral tame/weight/cyclotomic comparison, retaining the regulator and all Euler factors |
| Definite theta c2 | Second coefficient of the anticyclotomic Gross-point theta element, which is a square-root object | Its degree-two term is not the degree-two term of the full product theta*theta^*; the latter starts in degree four under the recorded order-two hypothesis | An integral comparison of this anticyclotomic square-root object with the W3 critical value; no such map is supplied by shared coefficient degree |
| Branch-theta augmentation coefficient | Ordinary stabilization of that Gross-point theta system | The stabilization correction is invisible in (p,I^3), conditional on the stated three-term relation in the actual system | This is already related to the previous row; it is not a fourth independently constructed arithmetic scalar |

The final row uses the exact file BRANCH_THETA.md, including its section 5
which keeps the arithmetic three-term relation as a source-matching obligation.
This return does not upgrade that conditional interface to a new unconditional
arithmetic theorem.

Do not confuse the tame singleton coefficient with a nonzero singleton
**Kato class**. The corrected singleton-class converse also needs nonzero
localization of the point space at p. That is a different object and an extra
condition, not something silently built into the tame coefficient.

## Reconstructed stabilization calculation

Let pr nu=p, alpha^2-a_p alpha+p=0, and
theta_n^alpha=theta_(n+1)-alpha^(-1)nu(theta_n). The three-term relation gives

    pr(theta_(n+1)^alpha)=alpha theta_n^alpha.

For a cyclic norm in a chosen group-algebra coordinate t,

    N_p(t)=sum_(i=0)^(p-1)(1+t)^i
          =p+binom(p,2)t+binom(p,3)t^2 mod t^3.

All three coefficients vanish modulo p for p>=5. Hence the correction lies
in (p,I^3). Multiplication by the ordinary unit alpha changes the quadratic
coefficient by a unit. This is an actual existing relation between the last
two entries; it says nothing about eta_p or the W3 comparison.

The tame--wild Betti calculation was also checked against its correction
record. The two-step multiplier on the tame quadratic term is
**(a_p-1)^2**, not the withdrawn a_p^2-a_p+1. In that source the proposed
mixed quadratic shape remains open. Its prose also uses the name c2 for
several objects; this return does not use those names as identifications.

## Why matching consequences cannot settle the collision test

The retained W3 statement is b_p<=3 => Sha[p^infinity]=0. It is not a
converse. The two-prime scalar has a retained if-and-only-if statement.
Neither those two statements nor common vanishing order proves
p^(-2)M_p mod p = unit*C_p.

Likewise, a formal model in which b_p>3 and Sha[p]=0 would demonstrate the
logical weakness of that attempted deduction; it would not disprove an
identity for the actual seed. No such model is represented as seed data.

## Disposition

The collision gate is **NOT_REACHED_IN_MATCHED_LATTICE**, after this
object-level and source-level check. The return does not claim that W3 is
independent of the old witness, and it does not continue to a nonvanishing
campaign on that unproved premise. The specific unresolved gate remains the
period comparison in INTEGRAL_EVALUATION.md, followed by an actual integral
collision identity or a proved separating map.
