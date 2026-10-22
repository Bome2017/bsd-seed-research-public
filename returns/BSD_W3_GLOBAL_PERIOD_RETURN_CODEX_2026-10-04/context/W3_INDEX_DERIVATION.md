# Independent derivation of the weight-three index bound

Status: CONFIRMED_AT_RETAINED_INPUT_AND_IMPORTED_THEOREM_GRADE.

This derivation checks the submitted corollary. It does not reprove Kato, Carayol, Hida control, or the seed certificates. The added details in sections 3 and 4 make the integral adaptation and its specialization explicit.

## 1. Datum, twist and finiteness

Fix a good ordinary seed prime p >= 5 outside {19,59,487}. Retain the reviewed weight-three specialization g with nebentypus omega^{-1}, its saturated lattice, and no additional tame ramification. Let O be its actual coefficient DVR, pi its uniformizer, k its residue field and L its fraction field. Every length below is an O-length, not a valuation normalized by v_p(p)=1.

For the homological representation V_g, det V_g = chi^2 omega^{-1}. Kato's representation D(g) is cohomological. His (14.10.2), printed p.240, agrees with

    D(g)=V_g^vee,
    D(g)(1)=V_g (det V_g)^{-1} chi
           =V_g chi^{-1} omega=U.

Consequently the direct Kato twist is r=1 for g. By (14.10.1), the Tate dual has twist r=2 for g*. Both lie in 1 <= r <= k_weight-1 and avoid the center 3/2. Kato 14.2(1), printed p.235, gives finiteness of the propagated discrete Bloch--Kato Selmer group B for every stable lattice at this fixed datum. There is no inference of primary finiteness for the seed from this fact alone.

Write T for the lattice in U and A=U/T. The previous independently reviewed comparison is retained:

    B[pi] = Sel_p(E/Q) tensor_Fp k,
    0 -> W -> B[pi] -> Sha(E/Q)[p] tensor_Fp k -> 0,
    dim_k W=2.

This equality is residual. It neither identifies all of B with the seed's primary Selmer group nor supplies a characteristic-zero lift of W.

## 2. Local and global correction terms

At a bad q != p in the specified domain, the retained residual H0 and H1 are zero. From 0 -> A[pi] -> A --pi--> A -> 0, H1(Q_q,A)[pi]=0. Every continuous cocycle into discrete A has finite image and is killed by a power of pi. Thus H1(Q_q,A)=0. The same argument works for the Tate dual, whose residual module is again E[p] tensor k by the Weil pairing.

At the other places q != p, U and A are unramified. The surjection U -> A induces a surjection on Frobenius coinvariants. The propagated rational finite condition is therefore the full discrete unramified condition. Kato's local discrepancy S(T)/Sel(T) in 14.8 is zero at every q != p, for T and its Tate dual. Hence his S(T) is this B.

Residual irreducibility kills global invariants. The retained non-anomalous p-local filtration kills p-local invariants, also for the Tate dual. Absence of pi-torsion invariants kills all discrete invariants. Integral local duality gives H2(Q_p,T)=0.

For clarity the ordinary filtration used here is

    T+ = O(alpha^{-1} chi),
    T- = O(alpha chi^{-1} omega),
    alpha-bar != 1.

The graded characters of T^vee(1) are alpha^{-1} chi^2 omega^{-1} and alpha. Over Q_p(mu_{p^infinity}) they restrict to alpha^{-1} and alpha. This cyclotomic extension is totally ramified, so the nontrivial residual unramified characters remain nontrivial. Their discrete invariant groups vanish, as do those of the extension. Thus the entire integral local Iwasawa H2 module vanishes, not merely its rationalization.

Throughout, global H^i(Z[1/p],T) and the Iwasawa groups use Kato's j_* convention. They are not obtained by silently allowing arbitrary ramification at the bad primes.

## 3. Integral height-one bound

### 3.1 A unit transvection, rather than an unproved higher-weight full image

At q0=2243 the primitive g has tame conductor exponent at most one. Residual ramification, retained from the seed's I_1 place, prevents exponent zero. The central character is unramified at q0. The local representation is therefore Steinberg with an unramified twist: principal series with unramified determinant cannot have exactly one ramified character, and the other local possibilities do not have conductor one here. Carayol Theorem A identifies the prime-to-p Galois local type. Its extra finite discrete-series assumption applies when the totally real field has even degree; F=Q has odd degree.

Choose an inertia element tau with nonidentity residual action. Its action is unipotent with N=tau-1 of rank one and N^2=0. The intersection of ker N with T is saturated. In a basis extending its generator, tau has matrix [[1,u],[0,1]]. Residual nonidentity forces u in O^times. The cokernel of 1-tau on T is free of rank one. Since q0 != p, its inertia lies in the cyclotomic kernel and both twists are trivial there.

This proves exactly the extra integral hypothesis in Kato 13.4(3), printed p.226. It does not assert that the full g-image contains SL_2(Z_p). It also excludes CM for g: this nontrivial Steinberg inertia is incompatible with a potentially abelian CM representation.

### 3.2 Normalized zeta integrality

Residual irreducibility implies homothety of stable O-lattices. Indeed scale another lattice T' into T but not into pi T; its nonzero image in T/pi T is the whole residual representation. Nakayama applied to the finite module T/T' gives T'=T after this scaling. This compares the chosen lattice with Kato's natural modular lattice. If L extends the newform's local coefficient field, first extend scalars; the extension of DVRs is finite flat.

Let H_Iw be the global Iwasawa H1 for T, and let Z_ES and Z_norm denote the integral Euler-system submodule and the normalized zeta module. Tate twisting is included in these notations. Kato 12.6 gives a finite quotient Z_norm/Z_ES. Kato 12.4(3), not merely its rational rank-one assertion, gives freeness of H_Iw over the component rings of O[[G_infinity]].

A finite module over each two-dimensional component ring vanishes at height one. Thus Z_norm is contained in H_Iw at every height-one localization. A free module over the normal ring O[[X]] is the intersection of those localizations in its fraction space. It follows that Z_norm is integral in H_Iw. This is the lattice argument of Kato 13.14, with residual irreducibility supplying the freeness and lattice comparison used there.

### 3.3 The Euler-system nonzero-component condition

Kato 13.7 says that the module generated by the modular Euler systems is nonzero on every component. It is not a claim that every individual modular Euler system is nonzero on every component. This distinction does not block the argument, but the application should say why.

Write Delta=Gal(Q(mu_p)/Q). Since p is odd, O contains its character values and its character idempotents are integral. For a specified height-one prime P of O[[G_infinity]], choose a modular Euler-system generator whose value generates (Z_ES)_P; the latter is an ideal in a rank-one free module over a DVR. On each other Delta-component choose a generator with nonzero image, using 13.7. Combine these systems using the Delta-idempotents, leaving the chosen P-component unchanged. Only finitely many systems are involved. Restrict their allowable conductors to avoid the union of their finite exceptional sets. They now satisfy the same Euler-system relations, and their integral idempotent combination is an Euler system nonzero on every component. Its localization at P is the originally chosen generator.

This verifies the nonzero-component condition in 13.4(i) without promoting 13.7 to an assertion about each individual system. The other conditions are rank-one complex-conjugation eigenspaces, purity, irreducibility, odd p, and the unit transvection above. Applying 13.4(3) and using the local Iwasawa H2 vanishing gives, at every height-one P,

    length_P H2_Iw(T) <= length_P(H_Iw/Z_ES)
                       = length_P(H_Iw/Z_norm).

The equality uses only the finite quotient at height one. It does not discard that quotient after specialization.

## 4. Explicit specialization with the Tor term retained

Work on the component for specialization to Q, after the twist, with R=O[[X]], X=gamma-1. Put M=H2_Iw(T) on this component. Choose the integral normalized class z_infinity specializing to the stated z. Its period vector is a primitive generator of T(-1)^+; this does not claim that z is primitive in global H1.

The preceding height-one inequality remains true with R z_infinity in place of Z_norm, since R z_infinity is a submodule of Z_norm. Write H_Iw=R e and z_infinity=F e on this component. Its specialization is nonzero by Kato 14.13 and the nonvanishing of the critical value at s=2. Therefore F(0) != 0.

Kato (14.14.1)-(14.14.2), printed p.243, give

    0 -> H_Iw/X H_Iw -> H -> M[X] -> 0,
    M/X M = H2(Z[1/p],T),

where H=H1(Z[1/p],T). Set

    t = length_O M[X],
    a0 = length_O(H_Iw/(X H_Iw+R z_infinity)),
    a = length_O(H/O z),
    h = length_O H2(Z[1/p],T).

The first exact sequence yields a=a0+t, not a=a0. Since F(0) is nonzero, X is a nonzerodivisor on R/(F). Applying Kato 14.15 to M and R/(F) and taking O-lengths gives

    h-t <= a0.

Consequently h <= a. The term t occurs on both sides and cancels. It was neither assumed zero nor dropped. This supplies the exact integral specialization needed for the return's inequality.

The possible codimension-two defect is precisely why one should not replace this step by naive specialization of characteristic ideals. The derivation is also independent of a numerical de Rham period formula.

## 5. Poitou--Tate and the exact index

Kato 14.5(1) gives rank_O H=1 and finite H2. Global invariant vanishing makes H torsion-free. The local singular quotient Q=H1(Q_p,T)/Hf1(Q_p,T) is free of rank one: the finite condition is the inverse image of a rational subspace, hence saturated, and the retained local dimensions are 2 and 1. Nonzero singular localization of z makes H -> Q injective with finite cokernel. In particular a and b are nonnegative integers, where

    b = length_O(Q/O loc_p^s z).

Using section 2, Kato (14.9.3) becomes

    0 -> H -> Q -> S(T^vee(1))^vee -> H2(Z[1/p],T) -> 0.

The cokernel of H -> Q has length b-a. Thus the Tate-dual Selmer group has length b-a+h. Kato 14.16(1), printed pp.244-245, identifies the orders of S(T) and S(T^vee(1)) for these twists; this is not an assumed self-duality of the weight-three representation. Over the same O equal orders mean equal lengths. Hence

    length_O B = b-a+h <= b.

The sign can also be checked using 14.16(2): mu has valuation a-h and nu has valuation b because all its invariant and H2(Q_p,T) correction factors are one.

## 6. Quotient and the sufficient bound

Since W has O-length two,

    length_O(B/W)=length_O B-2=b-a+h-2 <= b-2.

The natural map B[pi]/W -> (B/W)[pi] is injective, but need not be surjective. Therefore

    dim_Fp Sha(E/Q)[p]
      <= length_O(B/W)
      <= b-2.

Under the retained even residual-Selmer parity, b<=3 forces Sha[p]=0. A p-primary torsion group with no p-torsion is zero, so this gives Sha[p^infinity]=0. No prior primary Sha finiteness is needed. The inequality also forces b>=2 for every datum in the domain.

This is sufficient, not necessary. Divisibility inside the known point directions can make b larger even when there is no excess residual Selmer direction.

## 7. Numerical and uniform boundaries

The dual exponential induces a nonzero L-linear map from the one-dimensional rational singular quotient, so it is an isomorphism onto its de Rham target. The image of its actual integral quotient is a lattice P_g=d_g O. For x_g=exp*(loc_p^s z), the index is

    b=v_pi(x_g/d_g).

Replacing P_g by an arbitrarily chosen de Rham lattice would change the claimed index. The printed hypotheses of Kato 14.21 include p not dividing the modular level. They fail for this g, whose nebentypus omega^{-1} is ramified at p. The clean crystalline formula in that proposition is therefore unavailable as stated. This does not refute other ramified local calculations.

For a fixed weight-three h, choose a fixed good auxiliary prime ell. Residual compatibility with E[p] forces p to divide the nonzero fixed integer Norm(ell epsilon_h(ell)-1). A finite pool of such forms covers only finitely many p. This refutes that finite-pool shortcut. It does not refute a uniform theorem about varying g_p, or an independent bound on the varying indices b_p.

FIN, ORDER9 and Q36 are unchanged.
