# 10 — Line IV: the printed law, the exact local graded line, and the audit of Pro 6's IDENTICALLY_ZERO theorem

Line IV := the (g,h) anti-diagonal (S_2,S_3) = (v(1+T)-1, v(1+T)^{-1}-1) through the live point (v-1,v-1) [CH Cor 4.8 proof, p.23,
used there for (g,g')]. Its classical points are T = zeta-1, zeta in mu_{p^infty}: (f_2, theta_{chi phi}, theta_{chi^{-1}phi^{-1}}) with phi = psi_zeta
a finite-order character of Gamma_{p_frak^infty} — weight (2,1,1) with inverse wild twists; T = 0 is the target (g_alpha, h_{alpha^{-1}}).
[V] = verified verbatim (page/line), [D] = derived here, [O] = open.

## 1. The exact local graded line (Q2, source side)
[V] BSV extract l.3169-3170: V(f,g,h)^f = V(f)^- (x) V(g)^+ (x) V(h)^+ (x) Xi_fgh, a summand of gr^2 (l.3177); Prop 7.3 (l.3305-3320):
    L_f factors through p_{f*}: H^1_bal -> H^1(Q_p, V(f,g,h)^f).
[V] DR22 l.3647-3650 (Vklm): at (k,l,m) the f-line is L_p(chi_f^{-1} psi_{f_x} psi_{g_y}^{-1} psi_{h_z}^{-1})(t), t = (-k+l+m)/2; l.3635-3641.
[D] On line IV: t = 0 (l+m = 2), chi_f = 1, and a_p(g)(T) a_p(h)(T') = chi Psi_T^{-1}(sigma_pbar) . chi^{-1} Psi_T(sigma_pbar) = 1
    [from CH p.22: a_p(g_x) = chi psi_x^{-1}(sigma_pbar), a_p(h_x) = chi^{-1} psi_x^{-1}(sigma_pbar), with Psi_{T'} = Psi_T^{-1}]. Hence
        V(f,g,h)^f |_{IV} = unr(a_p(f)) = V_f^- = V_pE / F^0V_pE,   CONSTANT along line IV.
    Equivalently, at the wild points V_g^+ (x) V_h^+ = (chi phi)|_{K_p_frak} (x) (chi^{-1} phi^{-1})|_{K_p_frak} = 1_{p_frak}, and at T = 0
    unr(beta) (x) unr(alpha) = 1 (alpha beta = 1). So the graded line is the p_frak-copy of V_f^- inside V_f (x) Ind(1).
[D] EXACT_LOCAL_QUOTIENT = H^1(Q_p, V_f^-) = H^1(Q_p, unr(alpha_p)), one-dimensional, with H^1_f = H^1_unr = 0 because alpha_p != 1
    (alpha_p = 1 would force a_p = p+1, impossible by Hasse for p >= 5). So this H^1 IS the p_frak-singular quotient
    H^1(K_p_frak, V_pE)/H^1_f, and exp*: H^1(Q_p, V_f^-) -> D_dR(V_f^-) is injective (ker exp* = H^1_g = H^1_f = 0).
    It is exactly the one condition by which the Ind(1)-part of a balanced class on line IV is short of Selmer (09 sec 3, row IV).

## 2. The printed reciprocity law on line IV and the vanishing chain (Q1)
(a) [V] BSV Theorem A (l.217-219), xi = f, for the triple (f,g,h), centres (2,1,1), Assumptions 1.1 (l.138-140; theta_chi p-regular,
    CM by imaginary K, no RM) and 1.2 (eta_K^2 = 1): L_f(res_p kappa_BSV) = L_p^f(f,g,h) in O_fgh, on BSV's discs U_f x U_g x U_h.
    Any level-N test vector; with Hsieh's vectors BSV's L_p^f is the square root of Hsieh's L_p (BSV l.2919-2922, Assumption 6.3 l.2913-2918).
(b) [V] CH Theorem 4.1 (l.976-1006; hypotheses (CR),(ev),(sq),(Sigma^-)): interpolation of Hsieh's L_p^f on X_R^f, which contains the
    line-IV points (x_1, y, z) with y, z weight-one classical wild twists (l.960-965: X^cls includes weight-one classical points):
        nu(L_p^f)^2 = Gamma(2,1,1)/2^{alpha} . E(f,g_y,h_z)^2/(E_0(f)^2 E_1(f)^2) . prod c_q . L(E (x) theta_{chi phi} (x) theta_{chi^{-1}phi^{-1}}, 1)/||f||^2.
    [D] L(E (x) theta_{chi phi} (x) theta_{chi^{-1}phi^{-1}}, s) = L(E,s) L(E^K,s) L(E/K, chi^2 phi^{1-c}, s) since Ind(chi phi)(x)Ind(chi^{-1}phi^{-1})
    = Ind(1) (+) Ind(chi^2 phi^{1-c}) (CH (1.6)-(1.7) at phi = 1). With L(E,1) = 0 (analytic rank 2; CH Remark 1.4 (1.9)) the L-value is 0.
    Denominators: E_0(f) = 1 - beta/alpha_p, E_1 = 1 - beta/(p alpha_p), ||f||^2, 2^alpha — all finite non-zero; Gamma(2,1,1) = 0!^4 = 1;
    at wild points beta_g = beta_h = 0 (p-new) so E(f,g_y,h_z) = 1 - beta_f/p = 1 - alpha_p^{-1} != 0. NO CANCELLATION IS POSSIBLE.
    Hence L_p^f|_{IV}(zeta-1) = 0 for every zeta in mu_{p^infty}; Hsieh's L_p^f lies in R = I_f (x) O[[S_2]] (x) O[[S_3]], so its restriction is in
    O[[T]] and has infinitely many zeros => L_p^f|_{IV} = 0 (Weierstrass preparation).
    [Pro 6's route: Hsieh Prop 8.1 two-CM-variable factorization with W_2 = 0 on line IV, frozen factor Theta_{f/K}(0), Theta_{f/K}(0)^2
    ∝ (1-alpha_p^{-1})(1-alpha_p) L(E/K,1) = 0 (CH Thm 4.2, n = 0). Hsieh's paper is NOT in the local corpus (searched), so the printed
    line-IV shape of Prop 8.1 could not be read; the diagonal shape is CH Prop 4.3 (l.1104-1115) with C_{f,chi} in K(chi,alpha_p)^x.
    The conclusion is established independently by (b), so check 1 of the amendment is VERIFIED IN CONTENT, not in Hsieh's form.]
(c) [V] BSV Prop 7.3 at w = (2,1,1) in Sigma_f (2 >= 1+1; the centre 1 lies in U~^cl, l.167): alpha_k beta_l beta_m = alpha_p . beta . beta^{-1}
    = alpha_p != p, so
        L_f(Z)(2,1,1) = (p-1) alpha_k . (1 - beta_k alpha_l alpha_m / p^{c_w}) . (k - c_w - 1)! . exp*_p(Z_w)_f, with alpha_k = alpha_p, alpha_l alpha_m = alpha . alpha^{-1} = 1,
        beta_k = chi_f(p) p / alpha_p = p/alpha_p, c_w = 1: the factor is (1 - alpha_p^{-1}) != 0 and (k - c_w - 1)! = 0! = 1;
        so  L_f(Z)(2,1,1) = (p-1) alpha_p (1 - alpha_p^{-1}) exp*_p(Z_w)_f.
    Check 2 of the amendment: VERIFIED. Moreover, since H^1(Q_p, V_f^-) is one-dimensional and exp* != 0, EVERY linear functional on it is a
    multiple of exp*; so the specialization of L_f at any point of line IV is u(w).exp* for a scalar u(w), with u(0) != 0 printed.
(d) [D] Check 3 (passage to the whole line). Let Z = p_{f*} res_p kappa restricted to line IV. Because V(f,g,h)^f|_{IV} is the constant
    representation V_f^-, flat base change gives Z in H^1(Q_p, T_f^-) (x) O[[T]] = (O.e (+) torsion) (x) O[[T]]; write Z = z(T).e + torsion.
    L_f is O_fgh-linear, so on the line L_f(Z) = z(T).u(T) with u in O[[T]], u(0) = (p-1)alpha_p(1-alpha_p^{-1}) exp*(e) != 0, hence u != 0.
    From (a),(b): L_f(Z) = L_p^f|_{IV} = 0 on U cap IV. O[[T]] is a domain => z(T) = 0 on U cap IV => z = 0 (identity principle) =>
    Z = 0 rationally on the whole line. No interpolation formula at the wild points is needed for the regulator (only for L_p^f, which is
    CH Thm 4.1). The torsion of H^1(Q_p, T_f^-) is killed by L_f and disappears after (x) Q. Check 3: VERIFIED, and stronger than
    "injectivity near T = 0": the regulator on line IV is u(T).exp* with u a non-zero element of a domain; no exceptional zero can occur
    anywhere on the line because the Euler factor is the constant 1 - alpha_p^{-1}.
(e) [D] Consequence: p_{f*} res_p kappa_IV = 0 => the p_frak-component of the Ind(1)-part of kappa_IV lies in the image of H^1(Q_p, F^0 V_pE),
    i.e. is Bloch-Kato finite (good ordinary, alpha_p != 1). With z = z^+ + z^- (Q-rational and K-twisted parts; loc_{pbar} = 0 from
    09 sec 3 row IV forces z^+_p = z^-_p): z^-_p in H^1_f and z^- unramified outside p => z^- in Sel(Q, V_pE^K) = 0 (L(E^K,1) != 0, Kolyvagin/Kato,
    CH p.24) => z^- = 0 => z^+_p = 0 => z^+(T) in Sel_str(Q, V_pE) (x) O[[T]], with z^+(0) = kappa_{alpha,alpha^{-1}} (CH Cor 4.8(1); strictness
    is consistent with Cor 5.1's P (x) log Q - Q (x) log P, whose log vanishes).

## 3. Status block (Fable source audit of the Pro 6 theorem)
```
LINE_IV_SINGULAR_STATUS     = IDENTICALLY_ZERO   (verified; conditions in sec 4)
EXACT_LOCAL_QUOTIENT        = H^1(Q_p, V_f^-) = H^1(Q_p, unr(alpha_p)) = H^1(K_p_frak, V_pE)/H^1_f ; BSV gr^2 line V_f^- (x) V_g^+ (x) V_h^+ = V_f^- (x) 1_p_frak,
                              constant along line IV (t = 0, a_p(g)a_p(h) = 1, V_g^+ (x) V_h^+ = 1_p_frak)
PRINTED_RECIPROCITY_LAW     = BSV Theorem A (xi = f) on (f,g,h), centres (2,1,1), with Prop 7.3's Sigma_f interpolation at (2,1,1);
                              L-values at the wild points from CH Theorem 4.1 (Hsieh). [Hsieh Prop 8.1 line-IV form: not locally checkable]
ANALYTIC_FUNCTION           = L_p^f(f,g,h)|_{IV} in O[[T]]: interpolated values ∝ L(E,1) L(E^K,1) L(E/K,chi^2 phi^{1-c},1) = 0; ≡ 0.
                              (Hsieh factorization reading: Theta_{f/K}(0) . Theta_{f/K,chi^2}(T) . C, frozen factor Theta_{f/K}(0) = 0.)
ROOT_NUMBER_OR_SYMMETRY     = NONE. Forced zero: the Artin constituent Ind(1) of V_g (x) V_h on line IV carries L(E,s)L(E^K,s), and L(E,1) = 0.
FIRST_EXACT_MISSING_STATEMENT = none for Q1 on BSV's class over BSV's disc. For the DR-weighted class on the FULL line: the gate-A
                              comparison kappa_DR = (+-)c^{-1} kappa_BSV on the disc (02; W-CRIS + TF + sign/2), then the identity principle.
KUMMER_UPGRADE_NEEDED       = YES. Sec 2(e) gives a family in Sel_str(Q, V_pE) (x) O[[T]]; passing to E(Q) (x) L needs V_p Sha(E/Q) = 0,
                              i.e. #Sha(E/Q)[p^infty] < infinity — see 11. If dim Sel_str = 1 the family is a(T).kappa_{alpha,alpha^{-1}}.
POINT_FAMILY_ROUTE_SURVIVES = as a Selmer family: YES.  As a point family: UNDECIDED = the Sha gate.  As a "tower": trivial —
                              the fixed strict-Selmer class times a scalar function; it carries no new geometric point construction.
```

## 4. Conditions carried
BSV Thm A hypotheses (1.1, 1.2) and its disc U (the CM branch is expected etale over the full disc; not needed: the identity principle
extends the vanishing); Assumption 6.3 / Hsieh test vectors to identify BSV's L_p^f with Hsieh's; CH's (CR),(ev),(sq),(Sigma^-) for
Theorem 4.1; L(E,1) = 0; L(E^K,1) != 0 (for sec 2(e) only); alpha_p != 1 (automatic). Nothing else.
