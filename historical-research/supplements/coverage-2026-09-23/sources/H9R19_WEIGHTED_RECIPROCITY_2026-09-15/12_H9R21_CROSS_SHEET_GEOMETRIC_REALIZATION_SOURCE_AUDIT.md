# 12 — H9R21 source audit: is the cross-sheet contraction realized geometrically before etale realization?

Question (operator): where, if anywhere, is the unmodified cross-sheet Poincare contraction realized geometrically — on the
point/Albanese object carrying the diagonal class rather than only on cohomology? Mine Hida (limit Mordell-Weil), Ohta (duality),
MRS (geometric twist), DR (diagonal-cycle correspondence), the CM theta-family realization.  [V] verbatim, [D] derived, [O] open.

## 0. Correction to 09 sec 1-2 (the premise must be stated exactly)
09 wrote that h at the anti-diagonal point is "the complex conjugate of g_x". As FORMS that is false: with CH's sign convention
(p.22: g_x = theta_{chi psi_x^{-1}}, a_p(g_x) = chi psi_x^{-1}(sigma_pbar), so psi_x^{-1} has type (1,0)), the complex conjugate form
gbar_x = theta_{(chi psi_x^{-1})^{-1} N} has a_p(gbar_x) = p / a_p(g_x), valuation 1: it is ANTI-ordinary and lies on no Hida family.
Line IV pairs the point x of g (weight k) with the point iota(x) of h at which Psi_{iota(x)} = Psi_x^{-1}, i.e. weight 2-k: h_{iota(x)} =
theta_{chi^{-1} psi_x} has type (-1,0) when x has weight 2 — a NON-classical specialization of h. Line IV's classical points are only
T = zeta - 1 (weight-one wild pairs) and T = 0. What is true, Lambda-adically [D]:
    V_h o iota_anti = Ind(chi^{-1} Psi_T) = Ind(chi Psi_T^{-1})^dual = V_g^dual,            (CM: Ind(Phi)^dual = Ind(Phi^{-1}))
    V_{g^c} (x) chi_g^{-1} chi_cyc^{-1} = V_g^dual                                          (BCPV l.557, g^c = g),
so T_h o iota_anti and BCPV's twisted third slot T_{g^c}(chi_g^{-1}chi_cyc^{-1}) are ISOMORPHIC Lambda-adic G_Q-representations; they differ only
in the ordinary line F^+ (09 sec 1: the lines are exchanged; at T = 0, unr(alpha) versus unr(beta)). The verdicts of 09 sec 2 stand.

## 1. The only duality on the tower is same-sheet, and it is W-modified  [V]
- bcpv l.535-541: the usual Poincare duality on Y_1(N_h p^r) is  e'_ord H^1(TSym^k(H)(1)) (x) e_ord H^1(Sym^k(H^dual)) -> Z_p:
  U_p'-ordinary against U_p-ordinary. Perfectness of the modified pairing (l.516) is the isomorphism
  W_{N_h p^r}^{-1}(U_p')^r : e'_ord H^1 -> e_ord H^1 (l.540) with inverse U_p^{-r} W (l.545), "as W intertwines U_p' and U_p, cf. ohta99 (1.5.4)"
  (l.542); compare ohta99 sec 2.2, KLZ2 sec 7.4, BSV between Prop 3.2 and Remark 3.3 (l.549).
- klz2.tex l.2253-2282 (Ohta, Ohta-ordinaryII Cor 1.3.8 / 2.3.6): the canonical perfect pairing of Lambda_D-modules on the ordinary
  tower, with KLZ's models differing from Ohta's by the twist 1 + kappa + eps_N; l.2382-2391 (Ohta's lemma): the sum over
  alpha in (Z/p^r)^x of eps(alpha)^{-1} <alpha> U_p^r W_{Np^r}^{-1} f_r.
- [D] Consequence: on the tower every geometric duality is Poincare duality composed with correspondences (W, U_p, diamonds, Hecke).
  Ordinary (x) ordinary pairs to ZERO under unmodified Poincare duality (bcpv l.536: the second factor must be e'_ord); the
  W-transport lands the g-branch on itself (09 sec 2): this is the H9R16 modified Poincare contraction (MPC) and the line-I point tower.

## 2. Why no correspondence realizes the cross-sheet contraction  [D]
Fix a weight-2 point lambda of g and the abelian variety A_{g_lambda} subset J_s over Q (isogeny factor of the newform). Let K_g be its
Hecke field; V_p(A_g) = (+)_{Q | p} V_{g,Q} over the primes Q of K_g above p; U_p acts on V_{g,Q} by iota_Q(a_p(g)), which is a unit iff
Q lies above p_frak (a_p(g) = Phi(pbar) generates pbar up to units). So the g-sheet at lambda is V_{g,P} (P | p_frak), the anti-ordinary
partner V_{g,Pbar} (Pbar | pbar), and Poincare duality on A_g pairs V_{g,Q} with V_{g,Qbar}: P with Pbar. Correspondences on X_s act on
A_g through End^0(A_g), which is K_g-linear, and G_Q commutes with the Hecke action; both preserve the Q-decomposition. Hence:
  (a) no correspondence and no Galois element maps a P-component to any other component;
  (b) the only geometric pairing available pairs P with Pbar — same sheet after W;
  (c) the h-sheet's ordinary modules at weight 2 are P-type components of OTHER newforms h_mu (when h_mu is a coefficient-Galois
      conjugate g_lambda^sigma, sigma|_K = id, sigma(chi) = chi^{-1}, they are components V_{g,sigma^{-1}P} of the SAME A_g, still above
      p_frak), never V_{g,Pbar}; and the line-IV partner iota(lambda) is not classical at all.
So the cross-sheet identification T_h o iota ~ T_g^dual is a change of p-adic place of the coefficient field (tau with tau|_K = c), an
operation on coefficients, not on the curve. It is not induced by any correspondence on the tower, nor by Galois, nor by a twist of
A_g in the sense of MRS (mrs.tex sec 2-3: I (x)_Z V twists by finite-rank Galois modules; the sheet exchange is not a twist of A_g, it
is a different decomposition of the same V_p(A_g)). CATEGORICAL OBSTRUCTION, stated exactly: the cross-sheet contraction pairs the
P-ordinary line of g with a second ordinary line above p_frak (or with a non-classical Lambda-adic point), and no structure on J_s
or on lim J_s^ord (Hida's limit Mordell-Weil / Ohta's tower, KLZ l.2208-2282) pairs two components above the same prime.

## 3. DR's diagonal-cycle correspondence and Chow-Heegner points (what IS printed)
- The geometric contraction of a cycle Z subset X x X x X in slots (2,3) by a correspondence T subset X x X is pr_{1*}(Z . pr_{23}^* T);
  for the diagonal Z this is the fixed-point divisor of T on X (0-cycle -> divisor -> Jacobian -> E). With T a Hecke correspondence the
  fixed points are CM points: these are the Chow-Heegner points of Darmon-Rotger-Sols and Bertolini-Darmon-Rotger (not in the local
  corpus; cited from memory of DRS 2012 / BDR 2015 and BCPV abstract l.330 "Chow-Heegner points and twisted Heegner points in Hida
  families"). They realize the SAME-sheet (f, g, gbar) contraction at weight 2, Poincare/W type, i.e. line I; their heights are
  Gross-Kudla-Schoen type, proportional to L'(E,1) . L(E (x) ad^0 g, 1), so they are torsion in rank 2.
- Line IV has no weight-2 classical points: its classical points are (f_2, theta_{chi phi}, theta_{chi^{-1} phi^{-1}}) with weight-one CM
  slots. Weight-one forms have no cycle and no Jacobian realization; the class there is a p-adic limit (CH p.2-3, (1.2)-(1.4):
  kappa(f,g_alpha,h_{alpha^{-1}}) = lim_{l -> 1} kappa(f, g_l, h_l)). The receptacle at T = 0 is H^1(K, V_pE) (CH (1.7)), i.e. E(K) (x) L
  when Selmer = Mordell-Weil, but no map from a Chow/Albanese object to it is printed.
- CH p.2 [V]: "a stumbling block in this setting is the lack of a systematic construction of algebraic points on E playing the role
  of Heegner points"; Remark 1.5: the only other known Selmer-class construction in rank 2 (Skinner-Urban) is also not a point
  construction. In CH's definite setting (Thm 4.2 (ii), N^- odd) there are no Heegner points on E over K at all; Bertolini-Darmon's
  anticyclotomic classes (BD05) come from level-raised Shimura curves by congruences, not from Kummer images of E-points.

## 4. Verdict (source side) — NARROWED 2026-09-16 after reconciliation with Pro 6's Artin-model result
```
MODULAR_TOWER_CROSS_SHEET_REALIZATION   = BLOCKED / NOT_REALIZED. On the tower and its limit Jacobian the only duality is
                                          Poincare + W (same sheet, BCPV l.535-546; Ohta via KLZ l.2253-2282); no printed
                                          correspondence, Galois action, or MRS twist supplies the sheet exchange (sec 2, sec 6).
KUMMER_REALIZATION_ON_MODULAR_TOWER     = BLOCKED / NO CROSS-SHEET CORRESPONDENCE FOUND
KUMMER_REALIZATION_OUTSIDE_MODULAR_TOWER = UNDECIDED (Pro 6's finite-etale / Artin-motive coefficient map exists in a broader
                                          category; the class-level comparison is open — sec 5)
TARGET_SPECIALIZED_MOTIVIC_MAP          = NONE PRINTED on the tower; Artin coefficient map claimed by Pro 6 (H9R22 to audit)
ALBANESE_FACTOR                         = NONE PRINTED (weight-one slots have no Albanese realization on the tower)
FIRST_EXACT_OPEN_STATEMENT              = (TC) the target cross-sheet Chow–Abel–Jacobi comparison  c_{0,*}( AJ(D_0) - z_0 ) = 0 :
                                          construct the contracted divisor D_0 and identify its Abel–Jacobi image with the diagonal
                                          class. A rank-2 Heegner-point construction would be ONE realization of (TC), not its
                                          definition; a construction outside the modular tower is not excluded by anything here.
SHA_FINITE                              = REQUIRED by every printed route (CH Cor 5.1 / Cor B, file 11);
                                          NOT logically required if a (TC) construction exists.
FULL_FAMILY_NEEDED                      = NO; the target-only (T = 0) version is the one to build.
```

## 5. Reconciliation with Pro 6 (why the two results are compatible)
Pro 6 constructs the coefficient pairing for the target through a finite-etale / Artin model: at T = 0 the CM slots are the Artin
representations Ind_K^Q(chi) and Ind_K^Q(chi^{-1}), dual to each other, both realized on H^0 of a finite etale Q-scheme (the ring
class field), where the evaluation pairing Ind(chi) (x) Ind(chi^{-1}) -> 1 is the diagonal of a 0-dimensional scheme. Sec 2's
obstruction lives on H^1 of the weight-2 Jacobians (prime decomposition of V_p(A_g)); weight-one slots are not in H^1 of any curve,
so the Artin model EVADES that obstruction rather than contradicting it. What the Artin model does not supply — and what sec 3 says
no printed source supplies — is the CLASS: kappa_{alpha,alpha^{-1}} is a p-adic limit along the weight-2 tower (CH (1.2)-(1.4)), and a
divisor D_0 on the Artin-model side must be compared to that limit. That comparison is (TC). Agreement: coefficient-level pairing is
not enough; H9R16's tower does not retarget; local finiteness is not Kummer; nothing printed constructs the point; the missing
object is a global class-level geometric comparison.

## 6. The K_g-linearity step, stated for hostile checking (H9R22)
Claim used in sec 2: every algebraic correspondence on X_s acts on V_p(A_{g_lambda}) preserving its decomposition by primes of the
Hecke field K_g, hence cannot exchange the two ordinary components above p_frak. Exact form and backing:
 (i) [theorem] Ribet (Twists of modular forms and endomorphisms of abelian varieties, 1980): End^0_{Qbar}(A_g) is a central simple
     algebra over the fixed field F_g of the inner-twist group Gamma_g subset Aut(K_g), with K_g a maximal commutative subfield; its
     elements are K_g-linear exactly when Gamma_g is trivial, and an inner twist gamma is realized by an endomorphism phi_gamma with
     phi_gamma o T = gamma(T) o phi_gamma, which maps the P-component to the gamma^{-1}(P)-component.
 (ii) [D] For CM g with the twist by eta_K, the associated gamma is the identity (a_l eta_K(l) = a_l on split l, 0 on inert l), so the
     CM endomorphisms (over K) are K_g-linear; End^0_K(A_g) = K_g . K (a field, or K_g x K_g if K subset K_g), commutative.
 (iii) [D] The sheet-exchanging coefficient automorphism sigma (sigma|_K = id, sigma(chi) = chi^{-1}) is an inner twist only if
     chi^2 is of the form (p-power-conductor) . (phi o N), i.e. only if chi^4 = 1. With ord(chi) > 4 it is not, so by (i) no
     endomorphism of A_g, over any field, realizes it. Hom^0(A_g, A_{g'}) = 0 unless g' is a coefficient-Galois conjugate of g, in
     which case A_{g'} = A_g and the same statement applies; correspondences between factors reduce to endomorphisms of one factor.
 (iv) Hypotheses to be checked by H9R22: ord(chi) > 4 (CH assume only chi(pbar) != +-1); absence of further inner twists of the
     weight-2 members theta_{chi psi Psi_2}; and that "correspondence" means an algebraic cycle on X_s x X_s over Qbar — the
     finite-etale Artin model is outside this category by construction (sec 5), so (i)-(iii) say nothing about it.
 (v) What (i)-(iii) do NOT show: that no global algebraic construction outside the tower produces D_0 with (TC). They only locate
     the obstruction: any successful construction must leave the tower / limit-Jacobian category, and its class-level comparison
     with the p-adic limit is the whole content.

## 7. Correction (2026-09-16, from 13 sec 2(d)) — the user's H9R22 question (c) has answer YES over F
Sec 2(c) and sec 6(iii) treated only correspondences over Q and endomorphisms of a single A_g. They missed correspondences between
the two DIFFERENT motives M(g^o), M(h^o) over the ring class field F = K_chi, where both restrict to Psi (+) Psi^c: h^o is the CM
twist of g^o by chi^{-2} (a character of G_K, not a Dirichlet character), and chi o N_{F/K} = 1. Such a correspondence exists as an
absolute-Hodge/Tate class; it is an honest isogeny (algebraic) at weight 2, and a Tate-conjecture instance at weight >= 3. So the
obstruction of sec 2 stands over Q and, over F, becomes: algebraicity of the CM-twist class in weight >= 3. For the H9R23 approximants
(weight l_n >= p) this is exactly the first failing operation (13). The K_g-linearity statement of sec 6 is unaffected for
endomorphisms of A_g; it simply does not govern maps between different factors over F.
Superseded in part (operator correction, 2026-09-16; 13 sec 5): the CM-twist correspondence over F, composed with the polarization,
contracts the fixed constituent Ind chi^2 (slots 2,3), on which the CH class is zero (CH Lemma 4.5(1)); it is NOT the live contraction
(slots 1,4, moving constituent Ind Psi^{1-c}), which has no G_F-equivariant model at any weight >= 2. So its algebraicity is no longer
"the first failing operation" of H9R23; the first failure is the equivariance of the live contraction itself. The existence statement of
this section (a correspondence between the two factors over F) stands.
