# A quantitative bound from the actual Kato derivative

2026-10-07. **DERIVED_UNDER_RETAINED_INPUTS; INDEPENDENT_REVIEW_REQUIRED.**

This is a new written deduction in this return, not a novelty claim or a formal certificate. It uses the already-matched integral Kato inequality, the actual two-term cohomology complex, the saturated Mordell–Weil lattice, and the previous nonzero-derivative finiteness implication. No new value of the derivative is supplied.

## 1. Result

Retain the seed, minimal differential and domain

    D={p>=5 : p does not divide N, p not in {19,59,487}}.

Let the actual transported, smoothed class satisfy z=Uy in M=H^1_Iw, and let

    delta=aug(y)=A kappa(P1)+B kappa(P2).

Suppose delta is nonzero. Define its content and the local point index by

    m=min(v_p(A),v_p(B)),
    w=min(v_p(log_omega(P1)/p),v_p(log_omega(P2)/p)).

The second quantity is a finite nonnegative integer. The seed is good and non-anomalous at p, so log identifies the p-completed local point group with pZ_p. A nontorsion rational point has nonzero local logarithm. No non-Wieferich assertion is assumed for either point.

Here the full Mordell–Weil basis and minimal differential are fixed. The notation w in this return is a local point index, not the older tame witness scalar sometimes also denoted w_p.

The deduction is

    length_Zp Sha(E/Q)[p^infinity] + w <= m.              (B1)

In particular, the weaker bound without the local correction is length Sha<=m. Cassels–Tate duality, applied after the retained nonzero-derivative implication has established primary finiteness, gives

    m <= w+1  ==>  Sha(E/Q)[p^infinity]=0.                (B2)

The original primitive criterion is the case m=0. Even the simpler condition m<=1 suffices. A nonprimitive derivative with m=1 is therefore not automatically a failed certificate.

All statements concern the specified class. Dividing that class by p, or replacing it by an independently normalized class without the integral comparison, is not allowed.

## 2. Precise retained algebraic inputs

Put R=Z_p[[U]]. The full S-Iwasawa complex has a finite free representative

    C=[ R^(n+1) --D(U)--> R^n ]                         (B3)

in degrees 1 and 2. Here ker D=M is free of rank one, X=coker D is torsion over R, and derived augmentation computes RΓ(G_(Q,S),T_pE). In particular,

    H^1_S=ker D(0),  H^2_S=coker D(0)=X/UX.

The existence of this representative, not merely concentration of cohomology, is retained from INTEGRAL_MATCHING.md §7. The all-height-one inequality is

    length_(R_q) X_q <= length_(R_q)(M/Rz)_q

for **every** height-one q, including (p). Its source is the integral Kato 13.4(3) application already matched in the preceding return. The argument below would be false if only the localization at (U) were retained.

Since delta is nonzero, the previous weak-order argument gives rank_Zp H^1_S=2 and primary Sha finiteness. The saturated point lattice W has rank two and thus equals H^1_S integrally. Therefore m is also the p-content of delta in ker D(0). This invokes a proved consequence of nonzero delta; finiteness is not an initial hypothesis.

## 3. Signed maximal minors retain the finite errors

Choose a basis eta of M and regard it as a column vector in R^(n+1). Its coordinates have greatest common divisor a unit. Indeed, if a nonunit irreducible divided every coordinate, eta divided by it would be an integral kernel vector, contradicting that eta is an R-basis of ker D.

Let Delta(U) be the vector of signed n-by-n minors of D, with signs chosen so that D Delta=0. At least one minor is nonzero because D has generic row rank n. Hence

    Delta(U)=d(U) eta(U)                                (B4)

for a nonzero d in R. At every height-one localization, Smith reduction over the DVR shows

    v_q(d)=length_(R_q) X_q.

Thus d generates the characteristic ideal of X. This identity does not replace X by a pseudo-isomorphic module; the actual minors and actual kernel vector remain in (B4).

Write y=g eta, so z=U g eta. The integral inequality yields

    d divides U g in R.                                (B5)

Since delta=g(0) eta(0) is nonzero, g(0) is nonzero and eta(0) is not the zero vector. The matrix D(0) has rank n-1, since its kernel has rank two. Its maximal minors vanish, and (B4) then implies d(0)=0. As g is not divisible by U, (B5) forces

    d=U d_1,  d_1 divides g,  d_1(0) is nonzero.          (B6)

Taking the coefficient of U in (B4) gives the exact vector identity

    [U]Delta(U)=d_1(0) eta(0).                           (B7)

## 4. Bounding the torsion in the actual specialization

Perform Smith reduction on D(0) **over Z_p**, using constant invertible changes of bases. The resulting matrix has the n-1 nonzero diagonal entries s_1,...,s_(n-1) and one zero row, with two remaining zero columns. Put

    tau=v_p(s_1...s_(n-1))
       =length_Zp (H^2_S)_tors.

For n=1 the product is 1 and tau=0. Extend the constant basis changes to R. In the first derivative of any maximal determinant, exactly one row can contribute its U-term. That row must be the last row, since the last row of D(0) is zero. The other rows contribute their constant entries. Therefore every entry of [U]Delta is divisible by s_1...s_(n-1). Some entries may be zero; the assertion does not require them all nonzero.

Let mu be the p-content of eta(0) in Z_p^(n+1). Equation (B7) gives

    tau <= v_p(d_1(0))+mu
         <= v_p(g(0))+mu.                               (B8)

The kernel of D(0) is saturated in the free source: if p x is killed by D(0), then so is x, since the target is torsion-free. Consequently content in this kernel equals content in the ambient free module. The last term in (B8) is exactly m. Thus

    length_Zp (H^2_S)_tors <= m.                         (B9)

This is the quantitative step not present in the primitive-cycle splitting proof. When eta(0) is p-divisible, its content mu is retained. Finite R-modules can contribute here even though their characteristic ideal is a unit. No Smith normal form over the two-dimensional ring R is assumed.

## 5. The precise global-duality passage

Put A_disc=E[p^infinity] and define the strict (fine) Selmer group

    F=ker(H^1(G_(Q,S),A_disc) -> direct_sum_(v in S) H^1(Q_v,A_disc)).

The finite-module Poitou–Tate sequence, passed to the compatible p-power limits, gives

    0 -> F^vee -> H^2(G_(Q,S),T_pE)
                -> direct_sum_(v in S) H^2(Q_v,T_pE).    (B10)

The dual twist matches because T_pE is its integral Weil dual. The passage to limits is legitimate: finite-S finite-coefficient cohomology groups are finite, so the inverse systems have the Mittag–Leffler property; on the discrete side filtered direct limits are exact. This is the compact/discrete version of finite Poitou–Tate, not a BSD leading-term theorem.

More explicitly, the relevant finite sequence runs from local H¹ with coefficients E[p^n] into the dual of global H¹ with its Weil-dual coefficients, then into global H² and local H². Local duality identifies the first map as the dual of localization. The quotient by its image is therefore the dual of the localization kernel. Taking the indicated limits gives (B10). See SOURCES.md for the finite-S statement and its hypotheses.

On D all local groups at the right of (B10) vanish. At p this is the retained non-anomalous torsion vanishing. At bad q the retained residual local calculation excludes precisely 19,59,487 and gives E(Q_q)[p]=0; higher p-power torsion is then zero. Local Tate duality gives H^2(Q_q,T)=0. At the real place odd-p cohomology contributes nothing. Hence

    F^vee = H^2_S.                                     (B11)

For the uncorrected inequality length Sha<=m, only the injection in (B10) is needed. The equality (B11) is used for the explicit local correction w.

The discrete Kummer sequence gives

    0 -> E(Q) tensor Q_p/Z_p -> Sel_(p^infinity)(E/Q)
                              -> Sha[p^infinity] -> 0.

At a good prime outside S, a G_(Q,S)-class is unramified. The unramified group with these discrete coefficients is A_disc/(Frob-1)A_disc=0: Frob-1 is invertible on V_pE and hence surjective on A_disc. Thus using the finite set S here loses no outside-S local condition.

At q!=p the discrete local Kummer group E(Q_q) tensor Q_p/Z_p is zero. This follows by taking the p-power Kummer direct limit of a compact local group with an open pro-q subgroup; its finite p-primary contribution disappears in that tensor limit. This does not assert that H^1(Q_q,A_disc) is always zero.

At p the local Kummer group is Q_p/Z_p. On the global Mordell–Weil part the localization is the row

    (log(P1)/p, log(P2)/p): (Q_p/Z_p)^2 -> Q_p/Z_p.

A nonzero row of p-adic integers defines a surjection of these divisible groups even when both entries are divisible by p. Its kernel K_MW is, noncanonically,

    K_MW = Q_p/Z_p direct_sum Z/p^w Z.

Thus global point classes can remove the p-localization of every Selmer class, yielding

    0 -> K_MW -> F -> Sha[p^infinity] -> 0.              (B12)

Primary finiteness has already been proved from delta!=0. Dualizing (B12) and using (B11) gives

    0 -> Sha[p^infinity]^vee -> H^2_S -> K_MW^vee -> 0,
    K_MW^vee = Z_p direct_sum Z/p^w Z.

The induced map on torsion is onto Z/p^w: any lift of an element killed by p^w is killed by some further power of p, since its p^w multiple lies in the finite kernel. Therefore

    length_Zp (H^2_S)_tors = length_Zp Sha[p^infinity] + w. (B13)

Combining (B9) and (B13) proves (B1). In particular m>=w. The local contribution has been counted, not called an unknown unit or discarded.

## 6. Why one extra factor still suffices

The Cassels–Tate pairing for an elliptic curve is alternating and has divisible kernel. A finite p-primary component therefore has a perfect alternating pairing and even Z_p-length. The finiteness needed here follows from delta!=0, not from the desired conclusion.

By (B1), its even length is at most m-w. If m-w<=1 it must be zero. More generally,

    length_Zp Sha[p^infinity] <= 2 floor((m-w)/2).

The zero-derivative case gives no finite m and no assertion. Supersingular primes in D are included: no ordinary decomposition or height nondegeneracy occurs in this proof.

## 7. What is not proved

Neither m nor an upper bound for it has been computed at a new seed prime. This strengthens the sufficient test from primitivity to content at most w+1; it does not prove that weaker test succeeds cofinitely. The finite exceptional domain and independent FIN, ORDER9 and Q36 obligations remain.

Independent review should concentrate on (B4)–(B9), the compact/discrete Poitou–Tate passage (B10), and the local Kummer correction in (B12)–(B13). The prior integral Kato/source matching is retained, not independently recertified by this argument.
