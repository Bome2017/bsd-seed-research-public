# Independent review of the global Kummer-torsor comparison

Date: 2026-10-11.

**Verdict: the affinity argument is valid under the separately certified full residual-image input. The saved exact arithmetic maps prove global mod-5 Kummer identities once the scalar is fixed by a good specialization.** This is a written mathematical review with separate exact-arithmetic replay, not Lean certification or a novelty claim. It concerns the two small control curves, not the seed Kato class or a computed CM trace.

## 1. Exact objects

Let E=2541c1 with P1=(0,3), P2=(7,17). For the raised models E113=287133c1 and E167=424347b1 the proposed identities use

    P113=-P1=(0,-4),
    P167=2P1+P2=(7/4,-53/8),
    Y113=(39736379971/293764,7496759272384463/159220088),
    Y167=(480,22723).

Let f113 and f167 be precisely the global torsion maps specified in `map_113_1_0.json` and `map_167_0_0.json`. Their addition and Galois compatibility retain the grade of the separate exact torsion-map computation. No unlabelled scalar replacement of f is allowed in the asserted identities.

For each pair, the saved source polynomial is the numerator of x([5]Q)-x(P), made monic. It is irreducible of degree25. Since P is not2-torsion, its25 roots correspond bijectively to the25 points of [5]^-1(P). The completed y-coordinate is recovered using the differential identity

    v([5]Q)=X5'(x(Q))*v(Q)/5,

where v(Q)=y(Q)+(a1*x(Q)+a3)/2. The saved target coordinate r(u) belongs to the source root field K0=Q[u]/f; its minimal polynomial is the target degree25 polynomial. The source and target points reconstructed from the saved coordinates satisfy [5]Q=P and [5]R=Y exactly.

Thus H:Q -> R is a rational, Galois-equivariant bijection between the two25-point division fibers. Field isomorphism alone has not yet proved that H respects their torsor actions; that is the next step.

## 2. Why the bijection must be affine

Let L be the splitting field of the source fiber. Choosing one geometric division point identifies its Galois action with a subgroup G of V semidirect GL2(F5), where V=E[5]. Projection to GL2 is surjective by the separately certified full residual image. The translation intersection N=G intersect V is GL2-stable, hence either0 orV by irreducibility.

If N=0, then |G|=|GL2(F5)|=480. But irreducibility of the degree25 fiber says that G acts transitively on25 points, forcing25 to divide|G|. It does not. Consequently N=V and G is the full affine group AGL2(F5).

The same applies to the target fiber. The rational degree25 field isomorphism identifies their normal closures, so both actions are actions of one common Galois group. In AGL2(F5), the translation subgroup is the characteristic subgroup O_5(G): GL2(F5) has no nontrivial normal5-subgroup, while V is itself a normal5-subgroup. Thus the two intrinsic translation subgroups coincide inside the common Galois group.

It follows that H is affine for an additive bijection L0:V -> E1[5]: for every T,

    H(Q+T)=H(Q)+L0(T).

Conjugating translations by Galois shows L0 is Galois-equivariant. Since End_G(V)=F5 and the specified f is one equivariant isomorphism, there exists a unique c in F5^* with L0=cf. This is a global statement, proved before any finite-field scalar test. It is not inferred from a collection of numerically matching translations.

The producer subsequently gives a weaker-input version of this argument in `torsors/RESULT.md`, which I also checked. Using the already-constructed f, put K0=Q(E[5])=Q(E1[5]). The Kummer image of G_K0 is either0 orV by irreducibility; zero is excluded by the same transitive25 versus order-dividing480 argument. For v choose sigma in G_K0 with sigma(Q)=Q+v and define L0(v)=sigma(H(Q))-H(Q). Equivariance of H makes this well-defined and additive, since an automorphism fixing Q fixes H(Q). It also makes L0 Galois-equivariant. This directly proves affinity without identifying characteristic subgroups or needing full GL2. The producer's scalar-centralizer argument uses an actual inertia transvection and irreducibility. Those inputs suffice. The stronger retained full-image proof above is therefore an independent sufficient route, not an additional necessary hypothesis of the producer's result.

## 3. Why one good reduction can determine c

At a prime q of good reduction for both curves, q!=5, and where the displayed fiber points and rational-map coefficients extend integrally, reduction preserves the geometric five-torsion and its group law. For one nonzero T,

    reduction(H(Q+T)-H(Q)) = c reduction(f(T)).

The rightmost point has exact order5, so its scalar c is distinguished modulo5. Therefore checking equality to reduction(f(T)) determines c=1. It is legitimate to determine this already-proved global scalar at one good prime; it would not be legitimate to infer global affine equivariance from that specialization alone.

The producer checks all25 translations at3061. The independent review additionally checks that the25 points are distinct, all reduced fiber factors are squarefree, and repeats the scalar test at a held-out good prime4261. Rational coefficient conversion fails if a denominator is not a unit; no denominator is discarded. The exact rational polynomial and [5]-division identities are replayed before either finite-field check.

## 4. Resulting identities and their locality consequence

With c=1, choose a division point Q and put R=H(Q). Galois equivariance and affinity give equality of cocycles:

    sigma(R)-R = f(sigma(Q)-Q).

Hence the computed global identities are

    kappa_E113(Y113)=f113_* kappa_E(-P1),
    kappa_E167(Y167)=f167_* kappa_E(2P1+P2).

They imply the corresponding equality at every localization, not merely the auxiliary places used to discover the pattern. No assumption of Sha[5]=0 enters this deduction. In the measured toric orientations, a113=(0,4) and a167=(1,3), so the instrument's coefficients are respectively4 and1 for every admitted detecting ell2 at which the same conventions apply. This extends that specific instrument's observed constancy by a global source identity. It does not evaluate the original Shimura CM source.

## 5. The narrower but useful K=-19 corollary at167

Retain the separate exact descent bounds rank(E167/Q)=1 and rank(E167^(-19)/Q)=0. The quadratic eigenspace decomposition gives rank(E167/K)=1 for K=Q(sqrt(-19)). The target fiber polynomial for Y167 is irreducible of degree25. A fifth division point over K would have an x-coordinate of degree at most2, which is impossible. Thus Y167 is nonzero modulo5 in E167(K).

The full residual image restricted to the index-at-most-two subgroup G_K contains SL2(F5), whose standard representation has no invariant vector. Thus E167(K)[5]=0. It follows that E167(K)/5 is one-dimensional, generated by Y167.

Consequently every actual K-rational CM image in E167(K)/5 has a unique coefficient n, and its Kummer class transports back to

    n kappa_E(2P1+P2).

This determines the possible source direction on the control model without a Sha assumption. It does not determine n or prove n!=0. The component map factor k in MIXED_PLACE_DIAGRAM.md also remains uncomputed. At113, the twist rank bounds [0,2] do not justify the corresponding K-rank-one conclusion; the global identity for its rational point remains valid.

## 6. Exact scope

The experiment has constructed a common global mod-5 arithmetic realization for actual rational-point source classes on two admitted small curves. It has not yet constructed the Shimura parametrization, evaluated the chosen CM trace, computed the component-group normalization, lifted the congruence to mod25, or compared any source with the seed Kato derivative. Both control partners in fact have a separately witnessed mod25 trace obstruction.

The remaining n and k are specific geometric source indices, not units that may be freely fitted. The global Kummer identities show that the observed instrument relation can be proved from a genuine arithmetic map; they do not bound the seed's excess content. FIN, ORDER9 and Q36 are unchanged.

## 7. Replay record

`replay_global_torsors.py` is the independent checker written for this review. `GLOBAL_TORSOR_REPLAY.json` records exact polynomial, field-generator and division identities and both good-prime action checks. The producer's root search is not rerun: the saved maps are verified directly. The review imports the full residual image and verified torsion maps from the adjacent admission/torsion records, and does not claim to have re-proved their entire chains here.
