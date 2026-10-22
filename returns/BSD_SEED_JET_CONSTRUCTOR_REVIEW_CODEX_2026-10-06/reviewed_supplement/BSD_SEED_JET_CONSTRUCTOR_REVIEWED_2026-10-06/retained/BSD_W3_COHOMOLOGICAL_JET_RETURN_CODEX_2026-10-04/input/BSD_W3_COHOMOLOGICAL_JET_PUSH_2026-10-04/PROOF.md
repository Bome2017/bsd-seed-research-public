# W3: integral local control and a period-free fourth-order certificate

Date: 2026-10-04. Author-side mathematical derivation; independent review pending.

## 0. Result and limits

**DERIVED, conditional on the latest cofinite Hida datum:** the relevant local cohomology quotient over the weight/cyclotomic coefficient ring is free of rank one and commutes with every finite coefficient reduction. In that realization, a Coleman map with the precise pseudo-null kernel/cokernel property of Ochiai Proposition 5.1 is an integral isomorphism. Its pseudo-null error is proved zero before specializing, not discarded afterward.

This gives a period-free certificate target modulo p^4 for an actual integral Kato class. It does **not** establish that the latest modular-symbol value M_p has unit ratio to A_g; it does not produce the actual global Kato jet; and it gives no uniform nonvanishing bound. The new direction is to compute the genuine Kato zeta-map image in this finite deformation, rather than make the unproved period-unit comparison or a fixed cross-prime ancestor mandatory prerequisites.

No canonical project status is promoted. FIN, ORDER9 and Q36 remain open.

## 1. Retained arithmetic inputs

Fix a good ordinary prime p>=5 outside the fixed finite exceptional set of the submitted COFINITE_HIDA_CONTROL.md and outside the retained W3 exceptions. Work conditionally on that new written result, not on a fresh proof of it here.

Write R0=Z_p[[T]]. The full localized ordinary Hecke algebra and its primitive signed symbol lines are as in the submitted return. Let V be the integral homological/Deligne Hida representation, in the convention whose weight-three specialization has determinant chi_cyc^2 omega^(-1). Denote its ordinary unit character by bold-alpha. The relevant retained local profile, with trivial tame character, is

    0 -> R0(bold-alpha^(-1) chi_cyc nu_T)
      -> V -> R0(bold-alpha) -> 0,                    (1)
    det V = chi_cyc nu_T.

Here nu_T is the universal principal-unit cyclotomic character. For sigma in G_Qp set

    s(sigma) = log_p(<chi_cyc(sigma)>)/log_p(1+p),
    nu_T(sigma) = (1+T)^(s(sigma)).

The formulas define a continuous character, including on inertia. At T=0 it is trivial; at T=p it is <chi_cyc>=chi_cyc omega^(-1). The residual ordinary eigencharacter bold-alpha mod (p,T) is nontrivial and unramified. In particular alpha-bar != 1.

The ordinary-profile convention agrees with the Hida graded characters in KLZ Theorem 7.2.3 after carrying its coefficient/model conventions; equation (1) specifies the convention used in this proof, rather than silently transferring the names of its two filtration pieces.

The retained W3 index theorem uses U_g=D(g)(1), with integral singular quotient Q_g and normalized class z_g. Its sufficient bound is

    dim_Fp Sha(E/Q)[p] <= b_p-2,                       (2)
    b_p = length_Zp(Q_g/Z_p loc_p^s z_g),
    b_p>=2,
    b_p<=3 ==> Sha(E/Q)[p^infinity]=0.

This proof does not re-establish the global Euler-system, residual Selmer comparison or parity inputs of (2).

## 2. Construct the two-variable integral representation

Put R=Z_p[[T,S]], m=(p,T,S), and let nu_S be the same principal-unit character with parameter S. Define

    U = (V tensor_R0 R) tensor nu_S^(-1),
    A = R(bold-alpha^(-1) chi_cyc nu_T nu_S^(-1)),
    M = R(bold-alpha nu_S^(-1)).

Thus there is an actual exact sequence of continuous integral G_Qp-modules

    0 -> A -> U -> M -> 0.                            (3)

On the diagonal S=T, the two-dimensional determinant identity gives

    V tensor nu_T^(-1)
      = V tensor (det V)^(-1) chi_cyc
      ~= V^vee(1).                                   (4)

The last isomorphism is the standard alternating-pairing identity for a rank-two free module. Any choice of an integral generator of its determinant changes the resulting identification by a unit, not a power of p. At T=S=p this is the retained U_g=D(g)(1), and

    A_g = Z_p(alpha_g^(-1) chi_cyc),
    M_g = Z_p(alpha_g chi_cyc^(-1) omega).             (5)

In (5), A_g denotes the **rank-one representation**, not the numerical Kato value called A_g in the preceding return. Below that numerical value is never used in constructing the finite cohomology certificate.

This makes the diagonal and its tame character explicit. Substitution at T=S=p is not an assertion that the relevant complex L-function has a double zero in either formal variable.

## 3. Local freeness and exact base change

**THEOREM (imported input).** For a finite free continuous representation over a complete Noetherian local coefficient ring with finite residue field, the local Galois cohomology complex is perfect and satisfies derived coefficient base change. We use the finite-free case of Fukaya--Kato as recorded in KLZ Proposition 11.2.1. Local Tate duality and the local Euler characteristic formula are the other imported local facts.

**DERIVED LEMMA 1.** The following complexes have their only cohomology in degree one:

    R Gamma(Q_p,A) ~= R[-1],
    R Gamma(Q_p,M) ~= R[-1],
    R Gamma(Q_p,U) ~= R^2[-1].                        (6)

Consequently, for every ideal J for which R/J has the indicated complete coefficient topology, the natural maps

    H^1(Q_p,L) tensor_R R/J -> H^1(Q_p,L/JL)          (7)

are isomorphisms, for L=A,M,U. This includes J=m^4, J=(T-p,S-p), and J=(T-p,S-p,p^4).

**Proof.** Put k=R/m=F_p. The residual characters of A and M are respectively

    alpha-bar^(-1) chi-bar,     alpha-bar.

The first has no invariants because chi-bar is nontrivial on inertia. The second has none because alpha-bar is nontrivial unramified. Their Tate dual characters are alpha-bar and alpha-bar^(-1)chi-bar, so their H^2 groups are also zero by local Tate duality. The local Euler characteristic gives dimension one for each residual H^1. The residual sequence (3) then gives H^0=H^2=0 and H^1-dimension two for U.

Represent any one of the perfect complexes by a minimal bounded finite free R-complex. Such a representative is obtained by splitting off contractible summands whenever a differential has a unit entry. Every differential of the remaining minimal complex has entries in m, so reduction modulo m has zero differentials. Derived base change identifies that reduction with residual Galois cohomology. The residual calculation forces every free term except the degree-one term to have rank zero. Its remaining rank is one, one or two as appropriate. This proves (6).

Tensoring the actual free degree-one representative with R/J now proves (7). No Tor term has been assumed away: there is none for these particular local complexes because (6) has been proved. This is not a claim about the global cohomology complex or a Selmer complex. QED.

The long exact sequence of (3) is therefore the exact sequence of free R-modules

    0 -> H^1(Q_p,A) -> H^1(Q_p,U)
      -> H^1(Q_p,M) -> 0.                            (8)

It splits as R-modules, with no assertion of a splitting of Galois representations. In particular

    Q_family := H^1(Q_p,U)/H^1(Q_p,A)
              ~= H^1(Q_p,M) ~= R.                    (9)

At the weight-three specialization, the retained Bloch--Kato finite-line comparison identifies (9) with the actual Q_g. No Bloch--Kato condition is invented over the Artinian non-field coefficient rings.

## 4. What happens to a pseudo-null Coleman error

**DERIVED LEMMA 2.** Let R be the regular local domain above. If f:R->R has pseudo-null kernel and cokernel, then f is an isomorphism.

**Proof.** The map is multiplication by h. If h=0 the kernel has rank one, contrary to pseudo-nullity. Thus the kernel is zero. If h were a nonunit, some height-one prime would contain h, and (R/h)_P would be nonzero there, contradicting pseudo-nullity of the cokernel. Hence h is a unit. QED.

**SOURCE APPLICATION, with its hypotheses retained.** Ochiai Proposition 5.1 supplies an integral map from the cohomology of the rank-one quotient of the Kummer dual of his nearly ordinary representation to its coefficient ring, with pseudo-null kernel and cokernel. The ring here is regular, hence normal and Gorenstein; the source's Hida (MW) hypothesis is retained. Lemma 1 supplies the otherwise missing freeness of this particular cohomology module. Lemma 2 therefore upgrades this map to an isomorphism on the matched component:

    Col_p : H^1(Q_p,M) -> R.                          (10)

The module matching is as follows. Start with the ordinary cohomological Hida representation V^vee, whose unramified subline is bold-alpha^(-1), and in Ochiai's cyclotomic variable use the universal character chi_cyc nu_S. Its nearly ordinary representation is V^vee tensor chi_cyc nu_S. Its Kummer dual is exactly U, and the quotient occurring in Proposition 5.1 is exactly M. This specifies the dual and Tate twist before applying the source map.

If the source's cyclotomic coordinate is S_src for that character, the principal-unit coordinates satisfy

    1+S_src=(1+p)(1+S),
    S_src=p+(1+p)S.                                  (11)

This is an integral local-ring automorphism; it also shifts the tame-character component by omega. At the W3 point its source arithmetic character is chi_cyc^2 omega^(-1), of weight two and finite part omega^(-1). Forgetting either the coordinate shift or the tame component would evaluate the wrong class. The source interpolation factors are not set to one; (10) is proved by integral cohomology and the pseudo-null assertion, not by dropping Gauss factors in an interpolation formula.

If an implementation cannot establish the matching just specified for its chosen ordinary representation and coefficient convention, it must use the basis-free test in Section 5, rather than claim that an arbitrary big logarithm is (10).

This conclusion is **not** eta_p in Z_p^times for the modular-symbol value of the submitted return. It compares an actual integral cohomology lattice with R; it does not compare a complex modular-symbol period with a Kato period.

## 5. The finite certificate on a genuine global class

Let Z be an actual integral family Kato/Euler-system class, or its authentic finite m^4 reduction. Define the local quotient image by the genuine localization and quotient maps:

    H^1(global,U/m^4)
      -> H^1(Q_p,U/m^4)
      -> H^1(Q_p,M/m^4)
      -> H^1(Q_p,M_g/p^4).                           (12)

The last arrow is induced by T=S=p. Global H^1 is not declared to satisfy underived surjective base change. Z must come from the arithmetic source; an arbitrary lift of a residual global class cannot be substituted.

By Lemma 1 the final module is free of rank one over Z/p^4. This gives a basis-free nonzero test. Using (10), write F_p(T,S) for the quotient coordinate of the genuine Z. Then (12) is represented by

    epsilon_p = F_p(p,p) mod p^4.                    (13)

**DERIVED PROPOSITION 3.** Suppose the actual specialization Z_g is the fixed normalized Kato class z_g. Then

    epsilon_p != 0  <=>  b_p<=3.                     (14)

More generally, it is sufficient to prove the integral source relation

    Z_g = r_p z_g,     r_p in Z_p;                   (15)

a unit r_p is not required. Under (15), epsilon_p!=0 implies b_p<=3 and hence the retained ordinary-primary vanishing.

**Proof.** Since Q_g is free of rank one, the valuation of the coordinate of loc^s(z_g) in any primitive basis is exactly b_p. Its image modulo p^4 is nonzero if and only if that valuation is at most three. An integral multiplier r_p can only increase the valuation. Apply (2). QED.

The inclusion (15) is an arithmetic source condition, not a consequence of local freeness or of calling a class a Kato class. An arbitrary integral multiple also need not pass: extra p-divisibility can make its residue zero. Smoothing factors must be retained. This one-way certificate avoids needing to prove a *unit* period match, but does not license division by a nonunit or omission of the source condition.

Changing Col_p, the integral local basis, or a primitive family generator by an actual R-unit changes (13) by a Z_p-unit. Its nonzero status is unchanged. Multiplication by p is not such a change.

## 6. Only the genuine fourth-order jet is needed

For F=sum f_ij T^i S^j in R,

    F(p,p) = sum_(i+j<4) p^(i+j) f_ij mod p^4.        (16)

The coefficient f_ij is required only modulo p^(4-i-j). Thus R/m^4 has ten monomial coordinates for this computation, and the test is on their specified diagonal sum, not on whether the jet itself is nonzero. Higher total-degree terms lie in p^4 after evaluation.

This is an exact algebra identity, not a claim that extracting these ten arithmetic coefficients is cheap. The underlying modular-curve spaces and cohomology may still be large.

Two necessary controls:

* T-S is a nonzero jet with zero diagonal specialization. A nonzero higher-variable packet is not a certificate.
* p^2 T specializes to p^3: the first divided residual modulo p is zero, while the correct test modulo p^4 is nonzero. Thus b_p=3 must be kept.

In a one-variable diagonal coordinate F_diag(T)=F(T,T), the same test reads

    f_0 + p f_1 + p^2 f_2 + p^3 f_3 !=0 mod p^4.     (17)

No T^2 factorization has been assumed and neither of the first two coefficients has been discarded. If the actual source proves such a factorization, it may simplify (17), but rank-two terminology alone does not prove it.

## 7. Valuation-aware fallback for the existing symbol, not a forced unit gate

The submitted exact identity is b_p=h_p+v_p(M_p), h_p=v_p(eta_p). Even on the modular-symbol route, proving h_p=0 is stronger than necessary.

If h_p is computed and h_p<=2, set d_p=2-h_p. From b_p>=2 we then know M_p is divisible by p^d_p, and

    p^(-d_p) M_p mod p^2 !=0  <=>  b_p<=3.            (18)

If h_p=3, the right test is M_p mod p !=0. If h_p>=4, this particular b_p<=3 criterion cannot hold with integral M_p at that datum. The latter is a limitation of the sufficient criterion, not a proof that the curve has nonzero Sha.

The value h_p is not computed in this return. Equation (18) prevents a future correct nonunit comparison from being rejected merely because the previous brief demanded a unit.

## 8. The global step not supplied by these lemmas

The new local result proves that the target of (12) and its coefficient transport contain no unspecified specialization loss. It does not construct the global input Z or prove (13) nonzero. Ochiai's family construction is a source to instantiate, but its particular Betti period vector, smoothing factors and specialization cannot be identified with the fixed primitive z_g by naming convention.

The next actual arithmetic construction is the image, modulo m^4, of the original integral Kato zeta map on a primitive signed family Betti generator. It must include a proof of its source relation (15), or independently redo the Euler-system upper bound for that class. Once that image is constructed, the object to evaluate is exactly (16).

The requirement is cofinite ordinary nonvanishing of those actual diagonal residues. A prime-independent ancestor is one possible way to prove it, not a necessary premise. Formal norm relations, Hida freeness, mu=0, or an arbitrary choice of a nonzero local cohomology class do not prove it.

This is a new continuation specified by an integral cohomology map and a finite coefficient target, with a proved local-control lemma. It is not an independent upper bound or a completed route through the global nonvanishing problem.
