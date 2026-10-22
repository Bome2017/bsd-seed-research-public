# Exact location of the excess after order-three tuning

**WRITTEN_DERIVATION_UNDER_RETAINED_INPUTS; NOT_INDEPENDENTLY_REVIEWED.**
No novelty assertion and no uniform upper bound.

## 1. Hypotheses and notation

Fix a good seed prime p>=5 in the retained theorem domain. Let k=F_p,
V=E[p], S=Sel_p(E/Q), and W=E(Q)/p inside S, of dimension two.
The retained rank, saturation and residual-image inputs identify W with
the span of the two specified point classes. Put d=dim_k S.

Fix a genuine tame character lambda with the local conditions of
input/SECOND_ORDER_PROOF.md, Section 2. Let

    A_n=k[t]/t^n,
    M_n=V tensor A_n, with action rho(g) exp(t lambda(g)),
    C_n=Sel(M_n),                   1<=n<=3.

Here C_1=S. The local conditions are coefficientwise Kummer at Sigma,
zero at the new acyclic conductor primes, and unramified elsewhere.
They are stable under t and have the inverse-image and image properties
for the coefficient inclusions and quotients. Global H^0(M_n)=0: V has
no invariants and every successive coefficient quotient is V.

Assume exactly these two finite-order conclusions:

(H1) the image of C_2 -> S is W;
(H2) both independent classes w1,w2 in W are images of C_3 -> S.

By the retained Cassels--Tate kernel comparison, (H1) follows from
rad(b_lambda)=W. The preceding tuning proof claims (H2) after alpha=0.
We do NOT assume S=W. We do not require independent acceptance of the
new existence proof in order to prove the conditional result below.

## 2. Exact coefficient kernels, including the local conditions

For 1<=a<n<=3, use the coefficient sequence

    0 -> M_a --t^(n-a)--> M_n -> M_(n-a) -> 0.

Vanishing of H^0 of the quotient makes the first induced global H^1 map
injective. The long exact sequence identifies its image with the kernel
of projection. The inverse-image local condition then identifies that
kernel INSIDE Selmer groups with C_a, not merely global cohomology.
These statements assert left exactness; they do not assert surjectivity
of the projection between global Selmer groups.

Multiplication by t^a on M_n factors as projection to M_(n-a), followed
by its coefficient inclusion back into M_n. The latter H^1 map is
injective, by the same H^0 argument. Consequently

    C_n[t^a] = image(C_a --t^(n-a)--> C_n).            (1)

This proves the coefficient-kernel identity rather than assuming
unrestricted base change for global Selmer groups.

Apply (H1) at n=2. The exact sequence is

    0 -> S --t--> C_2 -> W -> 0.

In particular dim C_2=d+2. Now put C=C_3, and write i:S->C for the top
inclusion induced by V --t^2--> M_3. Equation (1) gives

    C[t]=i(S),             dim C[t]=d,
    C[t^2]=image(C_2 --t--> C),  dim C[t^2]=d+2.       (2)

The reduction C->S factors through C_2, so its image is contained in W
by (H1). By (H2), that image is all of W. Since multiplication by t^2
is i composed with this reduction,

    t^2 C=i(W),             dim t^2 C=2.              (3)

## 3. Module structure and canonical residual quotient

Multiplication by t is a nilpotent endomorphism of the finite-dimensional
k-space C with cube zero. Its Jordan blocks have sizes 1,2,3. Let n_j
be the number of blocks of size j. Equations (2)--(3) imply

    n_1+n_2+n_3=d,
    n_2+n_3=dim C[t^2]-dim C[t]=2,
    n_3=dim t^2 C=2.

Thus n_2=0 and n_1=d-2. We have proved

    C ~= A_3^2 direct-sum k^(d-2).                    (4)

The splitting in (4) is not canonical. The quotient identification is:

    C[t]/t^2 C = i(S)/i(W) ~= S/W ~= Sha(E/Q)[p].     (5)

The last map is the ordinary Kummer exact sequence, under the retained
identification of W with the entire rational-point contribution.
No assumption of finiteness of Sha is used in (5).

For clarity: C is the Selmer group of the specified CHARACTER-TWISTED
finite representation. It is not being identified with Sel_(p^3)(E).
The fact that it has a subquotient equal to the original Sha[p] follows
from the coefficient maps just proved, not from such an identification.

## 4. Actual mixed-characteristic coordinate

In O=Z_p[zeta_p], pi=zeta_p-1, the previous proof identifies O/pi^3
with k[u]/u^3 using u=pi-pi^2/2. Here u and pi are associates and
u^2=pi^2 modulo pi^3. The character agrees with exp(u lambda).
Transporting (4)--(5) through the matched local conditions yields

    Sel(T_lambda/pi^3) ~= (O/pi^3)^2 direct-sum k^(d-2),
    Sel(T_lambda/pi^3)[pi] / pi^2 Sel(T_lambda/pi^3)
                         ~= Sha(E/Q)[p].            (6)

This is only an order-three statement. It assumes no formal extension
of the fixed tame character over k[[t]], no arbitrary-order exactness,
and no integral global specialization theorem.

## 5. Why integral torsion-freeness does not remove the extra summand

One tempting inference would be: integral H^1 is pi-torsion-free, so C
must be free over O/pi^3. That inference is false without control of
cohomology base change. The following exact algebra supplies a control.
It is not asserted to be a seed Selmer complex or to satisfy all global
arithmetic dualities.

Over a DVR O, put in degrees 1 and 2 the free complex

    O^(e+2) --diag(pi^3,pi^3,pi,...,pi)--> O^(e+2).

Its H^1 is zero, hence torsion-free. After reducing the COMPLEX modulo
pi^3, its H^1 is

    (O/pi^3)^2 direct-sum (pi^2 O/pi^3 O)^e
          ~= (O/pi^3)^2 direct-sum k^e.

The residual first obstruction is diag(0,0,1,...,1), and the two initial
directions lift modulo pi^3. The second obstruction on those directions
is zero. All these properties hold for arbitrary e.

The discrepancy comes from H^2 torsion. For a free complex, the usual
coefficient exact sequence here reads

    0 -> H^1(Cplx)/pi^3 -> H^1(Cplx tensor O/pi^3)
          -> H^2(Cplx)[pi^3] -> 0.

In this example the right term accounts for the ENTIRE finite-level
H^1. Both the integral and generic H^1 are zero. Thus even actual
finite-order lifts cannot be promoted to compatible all-order classes
by a torsion-freeness argument.

## 6. What would count as additional arithmetic information

Equation (5) locates the excess; it does not control it. For this tuned
module the following are equivalent:

    Sha[p]=0;
    C[t]=t^2 C;
    C is free of rank two over A_3.

Calling any of the last two assertions a new flatness or saturation
criterion does not produce an independent mechanism. An arithmetic
argument for one of them, with hypotheses proved without Sha-vanishing,
could matter. None is obtained here. The proof also does not imply that
all possible future arithmetic arguments are impossible or equal G1.

Retained parity makes d-2 even, but supplies no upper bound on d-2.
All original excess directions survive in (5); the lifting result alone
neither reduces their number nor excludes their existence cofinitely.
