# Direct-base map audit and an exact trace-zero Selmer comparison

2026-10-12. Input: `submitted/BSD_DIRECT_BASE_CONTROL_PROBE_2026-10-12/PROOF.md`.

**Verdict: the submitted injection is correct.** The argument below also identifies its local error exactly and proves an integral target comparison on an explicit clean tame domain. This is a written deduction under the stated standard duality and retained seed inputs, not a numerical bound, formal verification or a new vanishing prime.

## 1. Global restriction and the canonical injection

Let L/Q be cyclic of degree p>=5, G=<sigma>, A=E[p^infinity], and assume E(Q)[p]=0. If E[p](L) were nonzero, its action by the p-group G would have a nonzero fixed vector, contradicting the assumption. Consequently A(L)=0. The full inflation–restriction sequence therefore gives an isomorphism

    H^1(Q,A) -> H^1(L,A)^G.                           (1)

Both H^1(G,A(L)) and H^2(G,A(L)) vanish. This is stronger than the injectivity needed in the submitted proof; it does not yet say that Selmer local conditions descend.

Write S_Q and S_L for the usual discrete p-infinity Selmer groups and

    K=ker(N_G:S_L->S_L),  N_G=sum(g in G),  pi=sigma-1.

If K is finite, it is a finite module over O=Z_p[G]/(N_G)=Z_p[zeta_p]. Invariants in K are automatically killed by p. Conversely, any p-torsion invariant in S_L is killed by N_G. Thus

    K[pi]=S_L^G[p].                                  (2)

Restriction preserves Selmer conditions and gives S_Q[p]->K[pi] injectively. Let W=E(Q) tensor Q_p/Z_p. Its divisibility gives the exact sequence

    0 -> W[p] -> S_Q[p] -> Sha(E/Q)[p] -> 0.

Quotienting by the same injected point plane proves the submitted canonical injection

    Sha(E/Q)[p] -> K[pi]/res W[p].                   (3)

It does not require injectivity of restriction on Sha, equality of point groups, finiteness of base Sha, or a choice of lift of a Sha class. The quotient construction is precisely what makes it canonical.

Kato's faithful-character nonvanishing theorem supplies finiteness of K when its twist hypothesis holds. That theorem is retained from the companion primary-source audit; no assertion of such nonvanishing for a cofinite family is made here.

## 2. The exact local error in (3)

Via (1), define the relaxed base group

    D={c in H^1(Q,A): res(c) belongs to S_L}.

Then D=S_L^G under restriction and K[pi]=res D[p]. For a place v and a place w above it, define

    Delta_v=ker[H^1(Q_v,E)[p^infinity]
                   ->H^1(L_w,E)[p^infinity]].

Kummer compatibility gives an exact sequence at the first two terms

    0 -> S_Q -> D -> direct-sum_v Delta_v.             (4)

The last arrow need not be onto. Denote its image by Q_D. Restriction–corestriction makes Q_D a finite group killed by p. Taking p-torsion gives

    0 -> S_Q[p] -> D[p] -> Q_D -> S_Q/pS_Q.

Let C_D be the kernel of the last arrow. After removing W[p], the exact correction to (3) is

    0 -> Sha(E/Q)[p]
      -> K[pi]/res W[p] -> C_D -> 0.                 (5)

Thus local defects may enlarge the target, but only through globally realizable classes that also lift to p-torsion. Merely listing local norm cokernels does not prove that every one occurs globally.

Local Tate duality identifies Delta_v with the Pontryagin dual of the p-primary norm quotient

    Q_v^norm=(E(Q_v)/Norm E(L_w))[p^infinity].         (6)

For a split place the quotient is zero. For a nonsplit cyclic degree-p completion it is killed by p. Statements (4)–(6) preserve the local error; E[p](L)=0 alone does not remove it.

Standard inputs: inflation–restriction, local Tate duality for abelian varieties and compatibility of restriction with norm. A primary reference for the duality framework is [Milne, *Arithmetic Duality Theorems*, Chapter I, local duality](https://www.jmilne.org/math/Books/ADT.html). The explicit deductions above are not quoted as a theorem of that source.

## 3. An actual integral source for K

There is a useful geometric comparison beyond the socle injection. Set

    R=Res_{L/Q}(E_L),     B=ker(n:R->E),

where n is the norm. Over Qbar this is the sum map E^p->E, with connected kernel E^(p-1). Thus B is an abelian variety over Q. On geometric p-power torsion there is an exact sequence

    0 -> B[p^infinity] -> R[p^infinity] -> A -> 0.     (7)

For surjectivity, lift a torsion point arbitrarily and subtract a suitable point of the divisible connected kernel. The assumption A(Q)=0 makes the resulting map

    H^1(Q,B[p^infinity]) -> H^1(Q,R[p^infinity])

injective. Shapiro identifies the target with H^1(L,A), and n induces corestriction. Its kernel is the norm kernel after restriction because (1) is injective and res cor=N_G. Therefore every c in K has a unique global cohomology lift to B[p^infinity].

The lift need not automatically be Selmer. At v its image in H^1(Q_v,B) lies in

    ker[H^1(Q_v,B)->H^1(Q_v,R)]
      = E(Q_v)/n R(Q_v),                             (8)

by the abelian-variety cohomology sequence. The p-primary part of (8) is exactly the norm quotient in (6). Consequently there is an exact sequence at its first two terms

    0 -> Sel_{p^infinity}(B/Q) -> K
      -> direct-sum_v Q_v^norm.                      (9)

The image on the right is again a global realizability condition, not an asserted surjection. In particular, if every Q_v^norm vanishes, (9) gives an actual isomorphism

    K = Sel_{p^infinity}(B/Q).                       (10)

The integral Tate lattice is equally explicit. Put I=ker[Z_p[G]->Z_p], the augmentation ideal. Then

    T_pR=T_pE tensor Z_p[G],
    T_pB=T_pE tensor I.                              (11)

These statements follow by taking the kernel of the norm on Tate modules; the quotient E has connected kernel B, so the integral sequence is exact. The map

    O -> I,   h mod N_G -> (sigma-1)h

is an integral O-linear isomorphism. Its kernel before quotienting is Z_p N_G, since the kernel of multiplication by sigma-1 in Z_p[G] consists exactly of constant-coefficient sums. Thus the lattice really is a rank-two O-lattice carrying the faithful twist, with an explicitly specified integral generator of I.

One must still transport the class and period along this lattice identification. In the quotient map Z_p[G]->O, the displayed generator maps to pi; replacing this geometric lattice by another embedded lattice without transporting the source can introduce p-content. The abstract isomorphism I=O proves the target identification, not a unit comparison with a separately normalized modular period.

For an abelian variety the usual discrete Selmer group agrees with the Bloch–Kato Selmer group of its Tate lattice. This is stated in Kato's primary definition preceding Theorem 14.2, printed pp.234–235. Hence (10) matches K to the standard Selmer group of the actual lattice T_pE tensor I, rather than to an unspecified finite character proxy.

## 4. A clean tame domain where both comparisons are exact

Assume:

- p>=5 is a good reduction prime for E;
- ell!=p is a good reduction prime with ell=1 mod p;
- L is the degree-p subfield of Q(mu_ell);
- p does not divide #E(F_ell);
- p is a unit in every bad-prime Tamagawa number c_v of E.

For the seed, the last condition holds for every p>=5 because the retained c_v are powers of two. Ordinarity at p is not needed for this tame comparison.

Only ell ramifies in L. At ell the extension is totally tamely ramified, its residue field is unchanged, and the norm on the reduction is multiplication by p. The formal subgroup is uniquely p-divisible because its residue characteristic is ell!=p; its norm has no p-primary cokernel. Therefore

    Q_ell^norm = E(F_ell)/pE(F_ell)=0.               (12)

At a good unramified place, the norm on the connected reduction is onto by the finite-field norm/Lang argument, and the norm on the formal filtration is onto by the unramified trace argument. This includes the coefficient prime p; the unramified residue-field trace is surjective even for an extension of degree p in residue characteristic p.

At a bad unramified place, the same argument handles the identity component of the Neron model. The remaining norm cokernel is killed by p and is a quotient of the base component group. Its p-primary part vanishes because p does not divide c_v. No assumption that the whole bad-prime cohomology group vanishes is used. Archimedean places contribute no odd-primary defect.

Hence all Q_v^norm vanish. Equations (5), (9) and (11) give two simultaneous exact identifications:

    K = Sel(T_pE tensor I),
    K[pi]/res W[p] = Sha(E/Q)[p].                   (13)

If the faithful twisted L-value is also nonzero, K is finite by Kato and is the correctly identified rank-zero character Selmer object to which an independently authenticated integral source bound can be applied. This closes the target-identification interface on the clean domain. It does not supply the bound or twisted-value nonvanishing for a family.

When p divides #E(F_ell), the exact local term at the ramified good prime is instead the nonzero group in (12). Its dimension is dim_Fp E(F_ell)[p], at most two. In particular the defect is not automatically absent at Kolyvagin/Kurihara-type primes with eigenvalue one. Global conditions can still prevent a local defect from occurring, as (5) and (9) specify.

## 5. What the audit changes

The submitted injection and the length threshold are valid. More is now specified: its possible excess is an explicit realizable local norm defect, and on the clean tame domain its finite character target is exactly the standard Selmer group of the geometric trace-zero lattice. This gives the companion integral-Kato calculation an actual target and exact local hypotheses.

An integral Fitting/index estimate for that lattice and its correctly transported source remains separate. In particular no algebraic twisted L-value has been placed in Fitt_0(K) merely from nonvanishing or from (13). No source normalization, local factor or lattice content is silently declared a unit.

There is no new seed prime, cofinite small-length bound, FIN, ORDER9 or Q36 conclusion in this audit. The new comparison is available for the next arithmetic estimate; repeating the injection is not that estimate.
