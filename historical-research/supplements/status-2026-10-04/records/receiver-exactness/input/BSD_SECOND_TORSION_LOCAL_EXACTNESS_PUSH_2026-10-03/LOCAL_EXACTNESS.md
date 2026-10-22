# Exact local splitting, and the seed receiver without the extra local line

**Grade: DERIVED.** This document supplies a written proof, not a claim of literature novelty, human review, or formal verification. The local lemma is proved here from the printed local representation facts identified below. The seed corollary additionally imports the explicitly named retained global inputs.

## 1. Local statement, with all hypotheses

Let p>=5, let E/Q_p have good reduction, and assume

    p does not divide #E_tilde(F_p).

Write V=E[p]. Let R belong to E_1(Q_p), with nonzero class generating E(Q_p)/pE(Q_p). Fix Q in E(Q_p_bar) with pQ=R, and define

    K = Q_p(E[p]),       Omega = K(Q).

Both extensions of Q_p are finite Galois: once E[p] is included, all p-division points of R are included. Different choices of Q give the same Omega.

**DERIVED — local exactness lemma.**

    ker[H^1(Q_p,V) -> H^1(Omega,V)]
        = H^1_f(Q_p,V)
        = F_p * kappa(R).                                      (L1)

Here H^1_f means exactly the image of E(Q_p)/p under the Kummer map. No rational point of infinite order over Q is needed. In particular no non-Wieferich hypothesis on a global Mordell--Weil basis occurs.

## 2. Printed local inputs

**THEOREM (Serre).** In J.-P. Serre, *Proprietes galoisiennes des points d'ordre fini des courbes elliptiques*, Inventiones Mathematicae 15 (1972), pp. 259-331, section 1.11, the facts used are these:

* For good ordinary reduction over Q_p, V has a Galois-stable formal torsion line V^+. The quotient V^- is one-dimensional and unramified. Proposition 11 on printed p. 273 and its e=1 corollary on p. 274 give the inertia characters on V^+ and V^- as the mod-p cyclotomic character and 1. In particular the first inertia character has full image F_p^*.
* For good supersingular reduction over Q_p (absolute ramification e=1 and residue field F_p), Proposition 12 on printed p. 275 gives trivial wild inertia, full nonsplit Cartan inertia of order p^2-1, and the full Cartan normalizer as the local Galois image. The residue field does not contain F_(p^2), so the normalizer, rather than only the Cartan, is essential.

The relevant scanned pages were visually inspected. These are statements about good reduction over the unramified local field Q_p; they are not being extended to arbitrary ramified local fields. A source URL and page mapping are in SOURCES.md.

## 3. Ordinary case: a nontrivial scalar and the formal line

Put G=Gal(K/Q_p), identified with its image in GL(V). In a basis adapted to V^+, every element is upper triangular. Write the unramified character on V^- as psi and set a=psi(Frob_p). The assumption p does not divide #E_tilde(F_p) implies a!=1: otherwise a nonzero reduced p-torsion point would be F_p-rational.

Choose a Frobenius lift with diagonal entries (u,a). Inertia has diagonal entries (t,1) for every t in F_p^*. Multiply by an inertia element with t=a/u. The resulting image has the form

    A = aI + b E12.

Since E12^2=0 and the matrix field has characteristic p,

    A^p = aI.

Thus G contains the central nonidentity scalar aI. Its cyclic subgroup Z has order prime to p and V^Z=0. Averaging gives H^j(Z,V)=0 for j>0, and the invariant term is zero as well. The inflation-restriction spectral sequence for Z normal in G therefore gives

    H^i(G,V)=0 for every i>=0.                              (L2)

This proves the cohomology vanishing directly; it is not an assumption that the ordinary representation splits.

Let D=Gal(Omega/Q_p) and P=Gal(Omega/K). The Kummer homomorphism

    P -> V,       sigma |-> sigma(Q)-Q

is injective and identifies P with a G-submodule of V. The class kappa(R) is nonzero over Q_p. Since H^1(G,V)=0, it remains nonzero on restriction to K. Therefore P is nonzero.

We can choose Q in the formal group. One explicit justification is that for the height-one formal group, [p](X) has a unit coefficient at degree p and all lower coefficients in pZ_p. As R has parameter in pZ_p, Weierstrass preparation for [p](X)-t(R) gives roots of positive valuation. Such a root is a formal p-division point of R. The formal group is defined over Q_p, so all Galois conjugates of this Q are formal. Their differences lie in the formal p-torsion line. Thus

    0 != P subset V^+,        hence P=V^+.

The action of P on the coefficient V is trivial. By (L2), inflation-restriction for 1 -> P -> D -> G -> 1 gives

    H^1(D,V) = Hom_G(P,V) = Hom_G(V^+,V).                  (L3)

The last space has dimension one. Indeed choose an inertia element whose first diagonal entry t is not 1. Its t-eigenspace is precisely V^+, even if its upper-right entry is nonzero. A G-equivariant map from V^+ to V has image in that eigenspace, and the scalar inclusions supply all possibilities.

Finally, inflation identifies H^1(D,V) with the kernel on the left of (L1), since G_Omega acts trivially on V. This kernel contains the nonzero Kummer class kappa(R), and has dimension one. The finite Kummer line is itself one-dimensional: reduction has order prime to p and E_1(Q_p) is isomorphic to pZ_p by the formal logarithm. Hence (L1) follows in the ordinary case.

**Important safeguard.** In a split ordinary representation End_G(V) can have dimension two. The argument uses Hom_G(V^+,V), not End_G(V). Dropping the fact that the translation subgroup is the formal line would invalidate the proof.

## 4. Supersingular case: the full normalizer matters

By the cited Serre Proposition 12, G is the normalizer of a nonsplit Cartan. Identify V additively with F_(p^2). Cartan elements act by multiplication by F_(p^2)^*, and an element outside the Cartan acts semilinearly through z |-> z^p.

The Cartan acts irreducibly on the two-dimensional F_p-space V. Its centralizer in End_Fp(V) is F_(p^2), acting by multiplication. Commuting also with the semilinear element leaves only F_p. Therefore

    End_G(V)=F_p.                                           (L4)

Moreover |G|=2(p^2-1) is prime to p, so H^i(G,V)=0 for i>0 by averaging. As before, restriction of the nonzero kappa(R) to K is nonzero. Its translation image P is a nonzero G-submodule of V. Irreducibility forces P=V. Inflation-restriction now gives

    H^1(D,V)=Hom_G(V,V)=F_p.

The same one-dimensional-kernel argument proves (L1).

**Important safeguard.** The Cartan alone has a two-dimensional centralizer over F_p. The Frobenius/normalizer step is indispensable. It is justified here specifically by residue field F_p, not by good supersingular reduction over an arbitrary larger unramified base.

## 5. Apply the lemma to the seed completion

Retain the seed and field definitions from context/FORWARD_RECEIVER_RETAINED.md:

    E: y^2=x^3-x^2-66020924x-65074271436,
    d_p=1-p^2-66020924p^4-65074271436p^6,
    F_p^quad=Q(sqrt(d_p)),
    R_p=(p^(-2),sqrt(d_p)*p^(-3)),
    L_p=Q(E[p],sqrt(d_p),Q1,Q2,Q3),
    pQ1=P1, pQ2=P2, pQ3=R_p.

The symbol F_p^quad in this section is a quadratic number field, not the finite residue field.

For every good seed p>=5, the retained non-anomalous input holds. Since d_p=1 mod p^2, F_p^quad splits at p. At either embedding into Q_p,

    t(R_p)=-p/sqrt(d_p),        v_p(t(R_p))=1.

Thus R_p generates E(Q_p)/p. This is the explicit primitive auxiliary point already in the input, not a new assertion about P1 or P2.

Fix a completion L_(p,w) at p. In this completion sqrt(d_p) belongs to Q_p. There exist a_i in Z and S_i in E(Q_p) such that

    P_i=a_i R_p+pS_i,       i=1,2,

because R_p spans E(Q_p)/p. Hence Q_i-a_iQ3-S_i belongs to E[p]. Consequently

    L_(p,w)=Q_p(E[p],Q3).                                 (L5)

This also holds when a_1=a_2=0 mod p, so the argument does not require either rational basis point to be locally primitive. At the other quadratic embedding R_p changes sign and spans the same finite line.

Combining (L1) and (L5),

    ker[H^1(Q_p,V)->H^1(L_(p,w),V)] = H^1_f(Q_p,V).       (L6)

## 6. Global consequence on the retained cofinite domain

Define

    A_p=Cl(O_(L_p)[1/p])/p,
    B_p=Hom_(Gamma_p)(A_p,V),
    Bstar={2,3,19,59,487,2243,4547,5843}.

The following inputs are retained, not newly certified seed computations:

(i) the full affine Galois group and kernel W=E(Q)/p of global restriction, from context/FORWARD_RECEIVER_RETAINED.md;
(ii) H^2(Gamma_p,V)=0 and therefore surjectivity of global restriction, from context/RECEIVER_DESCENT_RETAINED.md;
(iii) outside Bstar, every descended receiver class is unramified at good q!=p and has the required local condition at every bad prime; the new quadratic ramification is included in that check;
(iv) the forward map Sel_p/W -> B_p from the same retained sources.

**DERIVED — exact seed receiver.** For p outside Bstar, restriction induces a natural isomorphism

    Sha(E/Q)[p]  ~=  B_p.                                  (L7)

Proof. Let f in B_p. By (ii) it has a global cohomology lift c, unique modulo W. Class field theory for the p-inverted class group makes f zero on every decomposition group above p: those places split in the corresponding extension. Thus the restriction of loc_p(c) to L_(p,w) is zero. Equation (L6) makes loc_p(c) finite. All other local conditions hold by (iii), so c is a Selmer class. The kernel is W by (i), and the forward identification is (iv). This proves (L7).

The retained exact sequence

    0 -> Sha[p] -> B_p -> C_p^loc -> 0

therefore has C_p^loc=0 on this domain, without assuming nonzero localization of W. This is the precise improvement over the earlier at-most-one-dimensional error.

## 7. What (L7) does and does not establish

It identifies the exact arithmetic object controlled by the standard old-factor-base relations. No residual receiver direction can be dismissed as an extra local line on the stated cofinite domain.

It does not bound that object. With the retained even-parity input, dim B_p is even and a proof dim B_p<=1 would force B_p=0. No such estimate is supplied by (L1)-(L7). The local representation facts used in the proof are not principal-relation rank estimates.

In particular (L7) yields no new vanishing prime, no finiteness of the full Sha group, no exact order 9, and no leading-term comparison. FIN, ORDER9 and Q36 remain unchanged.
