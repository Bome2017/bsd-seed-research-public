# Attempts beyond the residual control theorem

Status: NO_INDEPENDENT_UPPER_BOUND_OBTAINED.

These attempts use GLOBAL_CONTROL.md rather than assuming the residual/discrete comparison. They do not re-open determinant equivalence-chasing as a default project lane.

## 1. Exact residual removal of the rational-point contribution

Write B=B_g for the actual discrete Bloch--Kato group in GLOBAL_CONTROL.md and W_g for its two-dimensional rational-point image inside B[pi]. Then

    B[pi]/W_g ~= Sha(E/Q)[p] tensor k.                     (1)

This is now an actual exact sequence for the changed weight-three datum, not a definition of a hypothetical automorphic module.

However, the proposed INTEGRAL quotient B/W_g is not an appropriate replacement for the right side of (1). The functor taking pi-torsion is not right exact. More precisely, applying pi to 0 -> W_g -> B -> Q -> 0, where Q=B/W_g, gives

    0 -> B[pi]/W_g -> Q[pi] -> W_g -> B/pi B -> Q/pi Q -> 0.  (2)

The middle arrow Q[pi] -> W_g sends b+W_g to pi*b. Thus Q can retain nonzero pi-torsion even if the residual excess in (1) is zero.

### Countermodel to automatic baseline cancellation

For any discrete valuation ring O, set

    B=(O/pi^r)^2,    r>=2,    W_g=B[pi].

Then B[pi]/W_g=0, but

    B/W_g ~= (O/pi^{r-1})^2 !=0,
    length_O B=2r.

The first claim is the same residual absence of excess that the desired conclusion would use. The quotient remains nonzero because the two residual point directions can have longer divisibility towers. No claim is made that this model is realized by a particular seed specialization.

**First failed inference:** 'remove two residual rational-point directions, therefore divide an integral characteristic/congruence factor by precisely pi^2 and obtain an excess module.' Neither the depth of those towers nor an integral point lift is supplied. An additional integral comparison or splitting is needed. The finite module example disproves this inference in general; it is not a nonexistence theorem for an arithmetic construction.

A length bound length_O B<=3 would still suffice by GLOBAL_CONTROL (with the coefficient ring specified). It is stronger than merely requiring B[pi]/W_g=0, as the countermodel shows. No such bound is obtained by this operation.

## 2. Can two auxiliary primes remove the point contribution on the discrete group?

The already retained Kummer--Chebotarev argument supplies cyclic Kato pairs a,b for which the point determinant D_ab is nonzero. Using the inverse of the GLOBAL comparison, there is a well-defined residual map

    Lambda_ab : B[pi] -> k^2,

obtained by identifying B[pi] with Sel_p(E/Q) tensor k and then taking the finite Kummer coordinates at a,b. Since Lambda_ab restricts to an isomorphism on W_g, elementary linear algebra gives

    B[pi] = W_g direct-sum ker Lambda_ab,
    ker Lambda_ab ~= Sha(E/Q)[p] tensor k.                 (3)

This is useful for identifying the target. It is not an independent upper bound, and it does not show that Lambda_ab extends to an O-linear localization map on all of B.

### Why ordinary strict localization on B is not that map

Let q!=p be a good unramified place for U. Suppose det(F_q-1 | U)!=0. Then

    H_ur^1(Q_q,U)=0,
    L_q(A)=0.

The definition of B already imposes zero localization in H^1(Q_q,A). Replacing that condition by 'zero localization' a second time does nothing. Nevertheless the residual finite local line H_ur^1(Q_q,M) can be nonzero. The local long exact sequence identifies the missing information with

    H^0(Q_q,A)/pi H^0(Q_q,A)
       = ker[H^1(Q_q,M) -> H^1(Q_q,A)].                   (4)

In this unramified case the kernel in (4) is the whole residual unramified line when F_q-1 is rationally invertible. This follows by applying multiplication by pi to the unramified cohomology sequence: A is pi-divisible and H_ur^1(Q_q,A)=0.

### Exact local matrix illustration

Over Z_5, take q=11 and unramified Frobenius

    F = [[1,1],[-5/11,1-5/11]].

Then det F=1, its residual matrix is regular nonidentity unipotent, and

    det(F-1)=5/11 !=0.

The elementary divisors of F-1 are a unit and an element of valuation one. Hence A^F ~= Z/5, while the rational unramified cohomology is zero. The residual unramified cohomology is one-dimensional and lies entirely in the kernel of the map to discrete cohomology. The matrix even has its two complex eigenvalues on the unit circle (trace 17/11, determinant one); it is not asserted to come from a modular form or the seed.

**First failed inference:** determinant-nonzero tests at residual level can be imposed merely by making the existing discrete conditions at a,b strict. They cannot in the situation just described. An integral implementation would have to retain the local invariant/nullhomotopy data in (4), or use a properly framed Selmer complex and prove its comparison. No such integral implementation is constructed here.

## 3. What remains a legitimate upper-control target

The following are sufficient targets, not independently proved bounds:

- Bound dim_k B[pi] <=3 by an independent arithmetic theorem; parity then gives exactly two.
- If B is proved finite, obtain length_O B<=3 in the specified coefficient ring.
- Bound the ACTUAL residual excess B[pi]/W_g by an independently vanishing quotient of an automorphic module, with all maps and local conditions proved.

The first two are not claims that criticality, complex nonvanishing, or a raw Eisenstein congruence gives the bound. The third is not permission to define the automorphic quotient using the unknown Sha group. No actual GL3 upper-control theorem was proved in this pass.

The completed global comparison can now be used as an input to such an argument. It does not itself furnish that argument or extend ordinary coverage to supersingular primes.

FIN, ORDER9 and Q36 are unchanged.
