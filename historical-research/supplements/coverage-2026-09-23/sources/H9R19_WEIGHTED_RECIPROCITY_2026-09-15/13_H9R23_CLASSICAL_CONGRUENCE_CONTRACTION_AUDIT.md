# 13 — H9R23_CLASSICAL_CONGRUENCE_CONTRACTION_AUDIT (source side, 2026-09-16)

Task: at the balanced classical weights (2, 1+phi(p^n), 1+phi(p^n)) identify the algebraic Clebsch–Gordan/evaluation
correspondence on the generalized diagonal cycle; decide whether its pushforward to the f-factor is a degree-zero divisor whose
etale Abel–Jacobi class is the coefficient contraction of the DR22/BSV classical specialization; then audit integrality mod p^n
and STOP at the first exact operation without uniform control.  Notation: r_n := phi(p^n) - 1, l_n := r_n + 2 = 1 + phi(p^n).
[V] verbatim, [D] derived, [O] open.

## 1. The classical data at (2, l_n, l_n)  [V]
- DR22 l.2687-2690: Clebsch–Gordan exponents (kk',ll',mm') = ((-kk+ll+mm)/2, (kk-ll+mm)/2, (kk+ll-mm)/2) = (r_n, 0, 0); the invariant is
  P = det(x_2, x_3)^{r_n}; l.2692-2695: the section over the diagonal is cl = (X_2 (x) Y_3 - Y_2 (x) X_3)^{(x) r_n}, integral in TSym.
  BSV (41) l.991-994: Det^r_N = det(y,z)^{r-r_1} with r - r_1 = r_n.  Pro's approximation Det_{211} = det(y,z)^{-1} = det(y,z)^{phi(p^n)-1}
  mod p^n is exactly this kernel; BSV l.3446-3450 confirm the weight-one exponent (l_o+m_o-k_o-2)/2 = -1.
- DR22 l.3121-3130: with (kk,ll,mm) = (0,r,r): #A = 0, #B = #C = r, #(B cap C) = r, so Delta^{0,r,r} = {(x, a, a)} subset X x A^r x A^r —
  the fibrewise diagonal of the Kuga–Sato variety, over the diagonal of X^3.  l.3223: (eps_0,eps_r,eps_r)Delta is null-homologous;
  (cycleDR1) kappa(f,g,h) = pi_{fgh} AJ_et((eps) Delta).  The approximating class is kappa(f, g_{l_n,alpha}, h_{l_n,alpha^{-1}}) with both
  CM slots ORDINARY (CH (1.2)-(1.4) p.2-3: the target is the limit of these along the diagonal family); the level-C newforms are
  g_l^o = theta_{chi Psi_l}, h_l^o = theta_{chi^{-1} Psi_l}, crystalline (nebentype eta_K), hence with REAL Hecke eigenvalues and
  gbar_l^o = g_l^o (l = 1 mod p-1 on the k_o = -1 branch).

## 2. The contraction: what is algebraic, and what it does to the approximants
(a) [V/D] The only Hecke-compatible algebraic contraction of the two coefficient factors is the polarization H^r (x) H^r -> Z_p(-r) (Weil
    pairing, induced on cohomology by Poincare duality of H^1(X_1-bar, H^r) with itself, geometrically the diagonal of A^r x A^r
    moved by a Hecke correspondence: DRS/BDR Chow–Heegner mechanism, fixed-point divisors). Poincare duality is Hecke-adjoint:
    "the T_l are the transposes of the T_l' with respect to Poincare duality" (BSV l.580; KLZ l.580). Hence it pairs the g_l^o-isotypic
    piece ONLY with the gbar_l^o = g_l^o-piece, and for x in the g^o-part, y in the h^o-part: a_q <x,y> = b_q <x,y> with
    a_q - b_q = (chi(q_frak)-chi(qbar))(Psi(q_frak)-Psi(qbar)) != 0 for suitable split q, so <x,y> = 0.
    => the polarization contraction of the cross-newform approximant kappa(f, g_{l_n}, h_{l_n}) is IDENTICALLY ZERO, for every n,
    integrally (a zero map is zero mod p^n).  It does contract the SAME-newform class kappa(f, g_l^o, g_l^o) (line I type), whose limit
    is the vanishing class kappa_{alpha,beta^{-1}} (03; CH Cor 4.8(2)); and the Euler factors relating level-C and stabilized classes
    (DR22 prop:main-crystalline l.3261-3281) are n-independent units or fixed non-units, so those Chow–Heegner points are = 0 mod p^{n-d}.
(b) [D] The target contraction at weight one is the self-duality of Ind(chi) (Ind(chi) = Ind(chi^c) = Ind(chi^{-1}) for ring-class chi)
    applied to the pair (g_alpha, g_beta); it pairs unr(alpha) with unr(beta) and is non-zero on the line-IV/III local structure.
    Mod p^n it is induced on the approximants only through the abstract isomorphism V_{h_l^o}/p^n ~ V_{g_l^o}/p^n ~ Ind(chi)/p^n
    (both branches pass through theta_chi; Psi_{l_n} = 1 mod p^n as a G_K-character since phi(p^n) kills units mod p^n). That
    isomorphism is NOT the polarization and is not Hecke-compatible at p (U_p = alpha versus alpha^{-1}).
(c) [D] Over Q no correspondence induces it: correspondences over Q are G_Q-equivariant and Hom_{G_Q}(V_{g^o}, V_{h^o}) = 0 (distinct
    irreducibles); integrally the lattices L_g/p^n and L_h/p^n are disjoint inside H/p^n because T_p - a_p(h^o) is a unit on L_g when
    alpha^2 is not 1 mod m (p-distinguished at the weight-one point).
(d) [D] CORRECTION TO 12 sec 2 / sec 6(iii). Over the ring class field F = K_chi the two motives become isomorphic: V_{g^o}|_{G_F} =
    Psi_l (+) Psi_l^c = V_{h^o}|_{G_F}, because h_l^o = theta_{chi^{-1}Psi_l} is the CM twist of g_l^o by the character chi^{-2} of G_K, and
    chi o N_{F/K} = 1. So Hom over F between the two DIFFERENT motives is non-zero: a "correspondence between two factors" does exist
    over F (the user's question (c) in the H9R22 brief). At weight 2 it is an isogeny of CM abelian varieties (Shimura–Taniyama:
    equal Hecke characters over F), hence ALGEBRAIC. At weight l >= 3 it is a Tate/absolute-Hodge class on A^r x A^r over F whose
    algebraicity is the Tate conjecture for CM Kuga–Sato correspondences — NOT PRINTED. The approximating weights are l_n >= p >= 5.
    This correspondence, composed with the polarization on M(h^o), gives the correct cross-sheet pairing <iota x, y> which pairs
    F^-V_g with F^+V_h (line-IV local structure) — it is exactly the operation H9R23 needs, and it is unconditional only at weight 2,
    which does not occur in the sequence (weight 2 is not = 1 mod p-1 for p >= 5).
STOP: FIRST EXACT OPERATION WITHOUT CONTROL = existence, as an ALGEBRAIC cycle, of the cross-newform correspondence
    Z_n in CH^{r_n+1}(A^{r_n} x A^{r_n})_F realizing M(g_{l_n}^o) -> M(h_{l_n}^o) (the chi^{-2}-twist) for every n.
    Before any p-adic integrality question, the contraction does not exist over Q, and over F it is a Tate class of weight l_n >= p.

## 3. Integrality audit of the remaining operations (conditional on Z_n existing), for completeness
| operation | control | anchor |
|---|---|---|
| theta_q, 1/C_q (modified diagonal) | C_q = (a_q - q - 1)^3 a p-adic unit; bounded | DR22 l.2863-2869 (kappa1), l.3489 |
| e_ord | integral (limit of U_p^{n!}) | BCPV l.498; DR22 l.2972 |
| U_p^{-r} | a_p a unit; bounded | BCPV l.1546-1567 |
| W and pseudo-eigenvalues | crystalline approximants have level C prime to p: lambda_C(g_l^o) is a p-adic unit (Gauss sums of conductor prime to p); bounded. (The p^{s/2} growth of BCPV l.1924 occurs only at wild levels, not used here.) | BCPV l.1552, 1924; DR22 l.1898-1901 |
| degeneracy maps / Euler factors E(g_a) = 1 - beta_l/alpha_l, E^bal | E(g_a) = 1 mod p^{l-1}; E^bal factors are units or fixed non-units (1 - alpha_p^{-1} zeta); n-independent | DR22 l.3267-3280 |
| wild averaging | NONE needed: crystalline approximants sit at level X_1 (tame only); the p^{r-1} denominators Pro found arise only for wild points | DR22 l.2536 (p^3/(p-1)^3 tame, unit) |
| descent | tame only: Q(zeta_1) = Q(mu_p), the delta-twisted descent (03/04, D-DR22-2538) divides by (p-1)^3 at most; no growing cyclotomic degree | DR22 l.2542-2554 |
| Scholl projector eps_r / Sym vs TSym | the ONLY growing denominator: v_p(r_n!) -> infinity if (eps)Delta or Sym^r is used; avoidable because DR22's class is defined through integral moment maps and the integral TSym section cl (l.1407-1440, l.2692-2695); the DR14/eps comparison is needed only for the reciprocity law, not for the class | DR22 l.3223-3235, 3245-3257 |
| AJ functoriality under correspondences | (AJ-corr), frozen PROVED_FORMAL (packet G9); integral for proper intersections; use Hecke translates T_q, q != p, to make the contraction proper | packet 06 G9 |
None of these is the first failure; the first failure is sec 2(d).

## 4. Status block
```
H9R23_CG_EVALUATION_DATA          = IDENTIFIED: det(x_2,x_3)^{r_n}, section (X_2 Y_3 - Y_2 X_3)^{(x) r_n}, cycle {(x,a,a)} in X x A^r x A^r
H9R23_ALGEBRAIC_CONTRACTION        = POLARIZATION ONLY (Hecke-compatible); it KILLS the cross-newform approximants identically
H9R23_TARGET_CONTRACTION           = self-duality of Ind(chi) on (g_alpha, g_beta); mod p^n it is the non-Hecke isomorphism V_h/p^n ~ V_g/p^n
H9R23_CROSS_NEWFORM_CORRESPONDENCE = over Q: none (Schur); over F = K_chi: exists as an absolute-Hodge/Tate class (chi^{-2} CM twist);
                                     ALGEBRAIC at weight 2 only; at l_n >= p it is a Tate-conjecture instance, NOT PRINTED
FIRST_FAILING_OPERATION            = existence of Z_n in CH^{r_n+1}(A^{r_n} x A^{r_n})_F inducing M(g^o_{l_n}) ~ M(h^o_{l_n}), uniformly in n
INTEGRALITY_OF_THE_REST            = controlled (sec 3), except Scholl's eps_{r_n} (v_p(r_n!) unbounded), which DR22's TSym construction avoids
CORRECTION_TO_12                   = the "no correspondence between factors" claim holds over Q and for endomorphisms of one A_g, but fails
                                     over F for CM twists between DIFFERENT newforms (algebraic at weight 2, conjectural above)
H9R23_STATUS                       = BLOCKED_AT_FIRST_OPERATION (no printed algebraic cross-newform contraction at any approximating weight)
```

## 5. CORRECTION (operator, 2026-09-16): sec 2(d) contracts the COMPLEMENTARY constituent; the first failure is earlier than algebraicity
Constituent bookkeeping (CH (1.7) l.123, (1.8) l.123-125, (4.4) l.1119-1120, (4.7) l.1137-1140; chi is a ring class character, Remark 1.4
l.171, so chi^c = chi^{-1}). Over G_K: V_{g_l} = chiPsi_l (+) chi^{-1}Psi_l^c and V_{h_l} = chi^{-1}Psi_l (+) chiPsi_l^c. After removing
the Tate-type factor Psi_l Psi_l^c, the tensor has four one-dimensional slots
    slot 1 = (chiPsi)_g (x) (chi^{-1}Psi)_h   = V_g^+ (x) V_h^+ : character rho := Psi_l^{1-c}
    slot 2 = (chiPsi)_g (x) (chiPsi^c)_h      = V_g^+ (x) V_h^- : character chi^2
    slot 3 = (chi^{-1}Psi^c)_g (x) (chi^{-1}Psi)_h = V_g^- (x) V_h^+ : character chi^{-2}
    slot 4 = (chi^{-1}Psi^c)_g (x) (chiPsi^c)_h    = V_g^- (x) V_h^- : character rho^{-1}
Slots 1,4 form the MOVING constituent Ind_K^Q Psi_T^{1-c} of CH (4.4); slots 2,3 form the FIXED constituent Ind_K^Q chi^2. Over the ring
class field F = K_chi the four characters are (rho, 1, 1, rho^{-1}).
(i) Where the class lives. CH Lemma 4.5(1) (l.1146-1168): kappa(f-breve, g-breve h-breve) lies in H^1-hat(K_inf, V_f(1)), the moving
    constituent; its Ind chi^2-component is ZERO because Sel(K, V_f(1) (x) chi^2) = 0 under L(f/K (x) chi^2, 1) != 0 ([CH15, Thm 1]).
    This is a statement about the Lambda-adic class, hence about every specialization, in particular every H9R23 approximant
    kappa(f, g_{l_n}, h_{l_n}). At T = 0 the moving constituent is Ind 1 = 1 (+) eta_K and kappa_{alpha,alpha^{-1}} is the image
    under Ind 1 -> 1 (CH (1.8)): the live contraction c_0 is the evaluation Ind chi (x) Ind chi^{-1} -> 1, nonzero exactly on
    slots 1 and 4:  c_0 = (1, 0, 0, 1).
(ii) What sec 2(d) built. iota: V_g -> V_h over F is G_F-equivariant, so it maps the Psi-line to the Psi-line and the Psi^c-line
    to the Psi^c-line (Psi != Psi^c on G_F for l >= 2). The polarization of M(h) pairs the Psi-line with the Psi^c-line. Hence
    <iota x, y> pairs (chiPsi)_g with (chiPsi^c)_h and (chi^{-1}Psi^c)_g with (chi^{-1}Psi)_h: it is nonzero exactly on slots 2,3,
        b_CM = (0, 1, +-1, 0).
    The local statement of sec 2(d) ("nonzero on F^-V_g (x) F^+V_h") is TRUE — that line is slot 3 — but the inference "it is exactly
    the operation H9R23 needs" is FALSE: slot 3 lies in the fixed constituent, on which the CH class is identically zero by (i).
    Applied to the approximants, the sec 2(d) contraction returns 0 for every n, exactly like the polarization of sec 2(a).
    ("line-IV local structure" in 2(d) was a mislabel of this file, not of 09/10: the line-IV/f-dominant law of 10 uses
    V_f^- (x) V_g^+ (x) V_h^+, BSV l.3169, i.e. slot 1, inside the moving constituent.)
(iii) Equivariance defect. For sigma in G_F acting on the four slots by diag(a/b, 1, 1, b/a), a = Psi_l(sigma), b = Psi_l^c(sigma):
        c_0 o sigma - c_0 = (a/b - 1, 0, 0, b/a - 1),
    zero iff rho(sigma) = 1. rho = Psi_l^{1-c} has infinity type (l-1, 1-l), so it is nontrivial on G_F for every l >= 2 and every
    number field F; it is trivial only at weight one. Therefore Hom_{G_F}(moving constituent, twist) = 0 at every classical weight:
    the live contraction has NO G_F-equivariant characteristic-zero model at the approximating weights, algebraic or not. The only
    equivariant contractions at those weights are those of the fixed constituent (b_CM and its multiples), where the class is zero.
(iv) Consequence for correspondences. An algebraic cycle Gamma over any number field F' acts on etale cohomology by a
    G_{F'}-equivariant map of lattices phi: T_g (x) T_h -> O(twist). On the saturated moving sublattice M_sat := (T_g (x) T_h) cap
    (moving constituent) one has phi|_{M_sat} = 0, because Hom_{O[G_{F'}]}(T_rho, O) = 0 (rho of infinite order, O torsion-free).
    Hence phi-bar vanishes on M_sat/p^n. The mod-p^n live functional c-bar_n (the weight-one evaluation transported through
    T_{g_{l_n}}/p^n ~ T_{g_1}/p^n, sec 2(b)) is NONZERO on M_sat/p^n as soon as n exceeds the fixed index e of ev_1 on the saturated
    Ind-1 sublattice at weight one and the constituents are separated residually (chi^2 != 1 mod m). So no algebraic correspondence on
    the weight-l_n approximants — over Q, over F, or over any extension — induces c-bar_n, even mod p^n, whether or not Z_n / C_n are
    algebraic. The lifting obstruction is explicit: rho_n := Psi_{l_n}^{1-c} = 1 mod p^n (14, check 1), so c-bar_n is equivariant mod p^n,
    and the connecting map of 0 -> O(rho_n^{-1}) --p^n--> O(rho_n^{-1}) -> O/p^n(rho_n^{-1}) -> 0 sends the invariant 1 to the class
        beta_n(sigma) = (rho_n(sigma)^{-1} - 1)/p^n  in  H^1(G_F, O(rho_n^{-1}))[p^n],
    nonzero because H^0(G_F, O(rho_n^{-1})) = 0 makes the connecting map injective. beta_n is a coefficient-level obstruction: it is not
    identified with the Sha obstruction and it produces no point.
(v) Corrected verdict. FIRST_FAILING_OPERATION (H9R23) = the coefficient contraction of the MOVING constituent at any classical weight:
    it is not G_F-equivariant (iii), so no correspondence can induce it (iv). This failure precedes, and is independent of, the
    algebraicity question for Z_n / C_n (sec 2(d), file 14), which concerns only the fixed constituent. The STOP line of sec 2 is
    superseded accordingly; the classification BLOCKED_AT_FIRST_OPERATION stands with the operation re-identified. The integrality table of
    sec 3 is unchanged but moot for the moving constituent. Operative statement (operator, verbatim): "The CM model exists; its
    modular-source comparison is unconstructed. But that comparison alone is not sufficient: polarization on the model contracts the
    complementary finite-character constituent. The live contraction must be matched explicitly after reduction, rather than inferred
    from the model's existence."
