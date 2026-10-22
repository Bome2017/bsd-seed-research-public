# 01 — Dependency tree of the reciprocity proof, node by node

Classes: CHARACTER_BLIND (CB) | FORMAL_CHARACTER_TWIST (FCT) | NEEDS_RECOMPUTATION (NR) | PRINTED_ONLY_AT_delta=1 (P1) |
BREAKS_AT_delta_NE_1 (BR).  Tracked symbols: omega_i, delta, Xi, chi_g, chi_{g^c}, eps_g, eta_{K/Q}, cyclotomic powers,
Teichmuller powers, U_p eigenvalues, Atkin-Lehner pseudo-eigenvalues, Euler factors, periods, de Rham vectors.
"Weighted replacement" = what the node reads on the CH triple (types (0,-1,-1), delta = omega^{-1} or omega^{-1}(./p)).

## A. The class (DR22 route, dr22.tex)

| # | node | source | original statement | weighted replacement | proof changes? | class |
|---|---|---|---|---|---|---|
| A1 | cycles Delta_r[d], diamond/Galois action | l.2020-2060 | <a>Delta_r[d] = Delta_r[a2a3 d1,a1a3 d2,a1a2 d3]; sigma_m Delta_r[d] = Delta_r[md] | none | no | CB |
| A2 | Lambda(G_r)-extension class kappa_r[a,b,c], wild (1/2)-twist | l.2223-2259, 2340-2400 | wild half-twist only; Lambda(G_inf)(1/2) (x)_nu = Z_p(-t)(omega^t) (l.2257) | none; the omega^t at l.2257 is exactly what delta supplies at non-crystalline weights | no | CB |
| A3 | weighted class kappa_inf(omega;delta) | l.2521-2540 | sum over [a,b,c] with delta^{-1}(abc)omega_1(a)omega_2(b)omega_3(c); omega_1omega_2omega_3 = delta^2 | (1,omega^{-1},omega^{-1};omega^{-1}); reading of the index must be [a,b,c] (l.2788), not [bc,ac,ab] (l.2538) — see 04 | no (definition) | FCT |
| A4 | equivariance lemma (iwasawa-cycles) | l.2542-2554 | sigma_m by delta(m); <a> by omega_123 | verified by direct computation from A1 under the all-triples reading; delta-descent puts the class in H^1(Q, H_inf (x) delta^{-1}) | no | FCT |
| A5 | balanced specialization = AJ of cycle (AJklm-thm) | l.2747-2781 | spec* kappa_inf[a,b,c] = AJ_{klm}(Delta_1^o[a,b,c]) via nu_{kk,ll,mm}, one exponent per slot | none (index-wise statement) | no | CB |
| A6 | cor:special-klm | l.2784-2795 | spec* kappa_inf(omega;delta) = AJ_{klm}(Delta_1^o(omega;delta)) | none — printed for general (omega;delta) | no | FCT |
| A7 | crystalline point / trivial diamond action | l.2816-2818, 2879-2881 | crystalline iff eps_i omega^{-kk_i} = 1; then level-p diamonds trivial on eigencomponent, mu_*^3 iso | crystalline points of the CH branches are kk = 0, ll = mm = -1 mod (p-1) [weights (2,p,p),...]: dense (BSV-type density) | no | FCT |
| A8 | kappakappa (delta := 1, omega_i := eps_i omega^{-kk_i}) | l.2855-2857 | tautology at crystalline points | replaced by: the class hitting the branches is the (omega;delta) eigencomponent; at its crystalline points the geometric-diamond action is trivial | statement changes, content formal | P1 -> FCT |
| A9 | lemma-klm (mu_*^3 of index cycles, two orientation classes) | l.2891-2928 | mu_*^3 Delta_1[a,b,c] = Delta_01^{(abc/p)}; Delta_01 over Q | none for cycles; for the weighted cycle the naive cycle-level pushforward VANISHES (sum of a nontrivial character), the pushforward WITH Clebsch-Gordan coefficients does not | yes, with coefficients | NR |
| A10 | Prop cycleDR01 (kappa_01 = p^3 pi AJ(eps Delta_01^{klm})) | l.3239-3257 | proof says "delta = 1 is the trivial character", degree (p-1)^3 onto Delta_01 | W-CRIS (00_STATUS): same conclusion, same constant, proof must carry the section weights a^{kk}b^{ll}c^{mm} | yes | **P1 — FIRST NON-FORMAL NODE** |
| A11 | lemma:from-wiles, ordinary-proj, any-cycle | l.3012-3105 | pi_1 U_p = T_p pi_1 - pi_2, pi_2 = beta pi_1 on ordinary part; xi_f = chi_f(p)p^{k-1} | chi_xi(p) = 1 for CH (chi_f = 1, eta_K(p) = 1) | no | CB |
| A12 | projecting-diagonal, prop:main-crystalline | l.3144-3317 | (varpi_1)^3_* kappa_1 = E^bal/(E(f_a)E(g_a)E(h_a)) kappa_GKS | Euler factors in alpha,beta of the crystalline forms at weights (2,p,p),... | no | CB |

## B. The L-function and regulator (DR22 sec 3.1, 4.2; BSV 6, 7)

| # | node | source | original | weighted | changes? | class |
|---|---|---|---|---|---|---|
| B1 | L_p^f / L_p^g(test vectors), Hsieh interpolation | dr22 l.3354-3449; bsv l.2896-2964; CH Thm 4.1 l.976-1006 | defined for families with chi_f chi_g chi_h = 1 (DR22) / omega^{2a} (CH, general components) | CH's Theorem 4.1 is stated for exactly the branch characters (1, omega^{-1}eta_K, omega^{-1}eta_K) | no | FCT |
| B2 | 4-step filtration, characters eta | dr22 l.3513-3575 | characters from Psi (unramified), chi_f,chi_g,chi_h (tame level, unramified at p), eps_cyc, eps_underline; no Teichmuller | at the CH point: V_g|G_{Q_p} = unr(alpha)(+)unr(beta), all lines unramified; delta enters only through the global (1/2)-twist bookkeeping | no | FCT |
| B3 | Lambda-adic de Rham vectors (klz-prop), E_0, E_1, pseudo-eigenvalue lambda(phi) | dr22 l.1868-1903 | KLZ Prop 10.1.1/10.1.2 + Ohta; lambda(phi) interpolated | KLZ 10.1.x are for families of arbitrary component (KLZ17 sec 7.2.3 twist paragraph); pseudo-eigenvalue at level N_g vs N: BCPV's live seam R2 (l.1562 vs 1546) unchanged | no | FCT |
| B4 | Perrin-Riou regulator (prop pr) | dr22 l.3724-3740; bsv Prop 7.3 l.3305-3401 | interpolation (-1)^t/t! E^PR log_BK on balanced points; BSV: (p-1)alpha_k(1-beta_k alpha_l alpha_m/p^{c_w})... | the line V(f,g,h)^g for centres (2,1,1) is an unramified twist of a cyclotomic character (Xi_fgh tame part = 1); Prop 7.3's proof (l.3321-3401) uses only Psi_o, Gamma_o, Ramanujan; centre-blind | no | FCT |
| B5 | cor:crystalline-lambda (class is balanced) | dr22 l.3743-3770; bsv Cor 8.2 l.3590-3644 | density of balanced crystalline points + Saito purity + H^0 vanishing | density holds for the CH components (weights = t_i + 2 mod (p-1)) | no | CB |
| B6 | Theorem L=L / BSV Theorem A | dr22 l.3781-3856; bsv l.4387-4513 | checked on crystalline balanced points; Euler identity E^f = E^bal E^PR | verbatim on Sigma^o_bal of the CH components; BSV proves it for arbitrary centres | no | CB (given A10/W-CRIS) |
| B7 | BSV big class construction Det with centre-determined Teichmuller exponents | bsv l.3446-3463, (155) l.3489 | kappa*_f = omega^{(l_o+m_o-k_o-2)/2}<u>^{(l+m-k-2)/2}; kappa = (1/a_p(k)) AJ(Det) | at (2,1,1): (omega^{-1},1,1), total omega^{-1} = the weighted datum | no (printed) | FCT (PRINTED) |
| B8 | BSV Thm 8.1, Prop 8.3, Lemma 8.4 (crystalline specialization of kappa_BSV) | bsv l.3581-3587, 3965-3976, 4298-4385 | (p-1)alpha_f rho_w kappa = (1 - alpha_f beta_g beta_h/p^{r+2}) kappa^dag; Pi^alpha_* kappa^dag = (p-1)alpha_f (three factors) kappa_GKS | centre-blind (only alpha, beta, r) | no | CB |
| B9 | BSV Prop 3.6 (classical explicit reciprocity, BSV20b) and Prop 3.7 (GKS comparison, sign) | bsv l.1304-1319, 1393-1395 | log_p kappa(f,g,h)(eta_f (x) omega_g (x) omega_h) = E(f,g,h) L_p^f(f_a,g_a,h_a); kappa_tilde = +-AJ(eps Delta) | classical forms at weights >= 3 of level N, p not dividing conductors: centre-blind | no | CB (sign NR) |

## C. Transcription into BCPV (bcpv.tex) — the CH-specific nodes

| # | node | source | original | on the CH triple | class |
|---|---|---|---|---|---|
| C1 | k_o = 0 choice, eps_g = eps_g^{(t)} | l.423-425, 459, 710 | families over the k_o = 0 component | t_g = t_{g^c} = -1; the choice is BCPV's, not BSV's (BSV centres free, l.121-133) | FCT |
| C2 | conjugate family g^c := g (x) eps_g^{-1} | l.489, 557, 636 | tame twist; T_{g^c} = T_g^dual (x) chi_g chi_cyc | eps_g^{(t)} = eta_K, g CM by K => g^c = g | **BR for the target** (03_GATE_B) |
| C3 | diagonal iota_{2,3}(kappa,lambda) = (kappa,lambda,lambda) | l.339 | third slot = g^c at the same point | (g_alpha, g_alpha) at the weight-one point = CH's kappa_{alpha,beta^{-1}} = 0 | **BR for the target** |
| C4 | trace line T_g^- (x) T_{g^c}^+ (chi_g^{-1}chi_cyc^{-1}) trivial; id (x) tr | l.635-673, 1091-1120 | Log^{(g),dag} = Log_{omega_f}^dag((id (x) tr) res_p) | on (g_alpha,g_alpha): trivial line, class zero; on CH's (g_alpha,g_beta): line unr(alpha^2), tr = 0 on it | **BR for the target** |
| C5 | thm_reciprocity_big_diag | l.1106-1113 | attributed to BSV, DR; not proved in BCPV | printed source = BSV Theorem A at centres (2,1,1), for the triple (f,g,g); transcription unprinted; W-CRIS + 02 supply it | P1 -> reconstructed |
| C6 | finite-level specialization eqn_2023_11_15_1243 and lemma_2023_11_14_1442 | l.1474, 1490 | repaired by H9R18-P2 (all three slots) | unchanged from H9R18-P2; not reopened | NR (done) |
| C7 | root-number hypotheses (RN) | l.481-486 | global/local signs | not used by BSV Theorem A; NOT_ESTABLISHED carried, not needed here | CB |

## D. Summary counts
CB: A1,A2,A5,A7(partly),A11,A12,B5,B6,B8,B9,C7 — 11.  FCT: A3,A4,A6,A7,A8,B1,B2,B3,B4,B7,C1 — 11.  NR: A9,A10(W-CRIS),B9(sign),C6 — 4.
P1: A8 (harmless), A10 (the first non-formal node), C5 (transcription).  BR: none for the reciprocity law itself; C2-C4 break the
APPLICATION of the law to the Castella-Hsieh class, which is gate B.
