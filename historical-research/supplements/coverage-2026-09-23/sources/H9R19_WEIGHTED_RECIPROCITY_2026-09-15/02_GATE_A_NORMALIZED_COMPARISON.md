# 02 — Gate A: normalized DR -> BSV comparison (C_g)

Claim to verify (amendment): pr_g res_p( J_CH z^wt_{DR,CH} - kappa_BSV ) = 0 in H^1(Q_p, L_g), scalars exact.

## 1. What BSV's class is, in the weighted language
bsv extract l.3446-3463: Det(x,y,z) = det(x,y)^{kappa*_h} det(x,z)^{kappa*_g} det(y,z)^{kappa*_f},
kappa*_f(u) = omega(u)^{(l_o+m_o-k_o-2)/2} <u>^{(l+m-k-2)/2}, kappa*_fgh = omega^{(k_o+l_o+m_o-6)/2}<u>^{(k+l+m-6)/2}; class
kappa(f,g,h) = (1/a_p(k)) AJ(Det) (l.3489-3497), with Atkin-Lehner w_p on the f-slot (l.3512-3534) and prf_gh.
At centres (2,1,1): Teichmuller exponents (omega^{-1}, 1, 1), total omega^{-1}. These are DR22's Clebsch-Gordan exponents
(kk',ll',mm') of l.2690 read mod (p-1) at the centre — the tame weights of the weighted class. So BSV's kappa(f,g,g) IS a
weighted class with datum equivalent to (1,omega^{-1},omega^{-1};omega^{-1}), and BSV Theorem A is its reciprocity law.
(At centres (2,2,2) the exponents are (1,1,1), total 1 — DR22's kappa_inf(1,1,1;1).)

## 2. Both classes at a crystalline balanced point w = (k,l,m) of the CH components
Let kappa_GKS = pi_{fgh} AJ_et((eps_r) Delta_{N,r}) be the level-N (prime-to-p) Gross-Kudla-Schoen class of the newforms
f_k, g_l, h_m (weights k = 2 mod (p-1), l = m = 1 mod (p-1), all >= 3 in Sigma^o_bal).
- BSV: Thm 8.1 (l.3581-3587) x Prop 8.3 (l.3965-3976), the (p-1)alpha_{f_k} cancelling, and Prop 3.7 (l.1393-1395, sign +-):
      Pi^alpha_* rho_w kappa_BSV = E^bal(w) . (+-) kappa_GKS,
      E^bal = (1-alpha_f beta_g beta_h/p^c)(1-beta_f alpha_g beta_h/p^c)(1-beta_f beta_g alpha_h/p^c)(1-beta_f beta_g beta_h/p^c), c = r+2.
- DR22 (weighted, given W-CRIS): cor:special-klm (l.2784-2795, general omega) -> W-CRIS (= cycleDR01 with weights) ->
      prop:main-crystalline (l.3261-3281, character-blind):
      (varpi_1)^3_* rho_w kappa_DR^wt = E^bal(w) / (E(f_a)E(g_a)E(h_a)) . kappa_GKS,   E(xi_a) = 1 - chi_xi^{-1}(p) beta_xi^2 p^{1-k_xi} = 1 - beta_xi/alpha_xi.
- Relating the projections. BSV (169): Pi^alpha_* = (x)_xi (pr_{1*} - beta_xi p^{1-k_xi} pr_{p*}). On the ordinary (xi_alpha)-isotypic
  part pr_{p*} = beta_xi . pr_{1*} (DR22 l.3047-3048: pi_2 o e = beta pi_1 o e, from pi_2 U_p = p[p]pi_1, [p] = chi(p)p^{k-2}; BSV's
  pr_1, pr_p are the same degeneracy maps, l.463-471, with the same Hecke relations (22) l.682 and l.4214), hence
      Pi^alpha_* |_{ord} = prod_xi (1 - beta_xi^2 p^{1-k_xi}) . pr_{1*} = prod_xi (1 - chi_xi(p) beta_xi/alpha_xi) . pr_{1*}.
  On the CH triple chi_f(p) = 1 and chi_g(p) = chi_h(p) = eta_K(p) = +1 (p split), so this equals prod_xi E(xi_a) . pr_{1*}, and
  varpi_1 = pr_1 (dr22 l.1147-1151: (A,P) -> (A,pP), tau -> tau; bsv l.467-469: identity on H).
- Therefore, at every w in Sigma^o_bal of the CH components:
      pr_{1*} rho_w kappa_BSV = (+-) E^bal/prod E(xi_a) . kappa_GKS = (+-) c . pr_{1*} rho_w kappa_DR^wt,   c in {1, 2^{+-1}} (D-DR22-ORBIT),
  and pr_{1*} is injective on the ordinary isotypic part (dr22 l.2880-2881 with l.3003-3007; bsv l.3951), so
      rho_w kappa_BSV = (+-) c . rho_w kappa_DR^wt   for all w in Sigma^o_bal.

## 3. From points to the Lambda-adic identity
(TF): H^1(Q, V^dag_{fgh}(M)) is O_fgh-torsion-free. Sufficient: H^0(Q, V^dag (x) O_wp) = 0 for every height-one prime wp, which holds
when rho-bar_f is absolutely irreducible and not a constituent of rho-bar_g (x) rho-bar_h (CH's (CR) plus the CM shape
Ind(chi-bar^2) (+) Ind(1) of V_g (x) V_h); BSV use the same device for the local module in Cor 8.2 (l.3612-3644).
Under (TF), two classes agreeing at the dense set Sigma^o_bal are equal:  kappa_DR^wt = (+-) c^{-1} . kappa_BSV in H^1(Q, V^dag_{fgh}(M)),
hence pr_g res_p(kappa_DR^wt - (+-)c^{-1} kappa_BSV) = 0. This is (C_g) with the scalar J_CH = (+-)c^{-1} (the two DR-side
constants p^3/(p-1)^3 and 1/C_q and BSV's 1/a_p(k) are already inside the two specialization formulas, so they are accounted for).

## 4. What is NOT settled (each localized to a line)
- (S-A1) sign: bsv Prop 3.7 l.1393-1395 "equal (up to sign)". Fixing it needs BSV's Equation (59) Leray isomorphism against DR14's.
- (S-A2) factor 2: DR22 l.3248-3250 asserts a degree-(p-1)^3 map from |Delta_1(1,1,1;delta)| onto Delta_01 while the printed weighted
  sum (l.2538, [bc,ac,ab]) covers one orientation orbit only; with the all-triples reading (l.2788) the count gives p^3 . deg where
  deg in {1,2} depends on whether <-1,-1,-1> is counted (dr22 l.1171-1172 says X_1 -> X_{0,1} has degree p-1, not (p-1)/2). See 04.
- (S-A3) level: DR22's classical class lives over X = level M prime to p (l.2957-2959), BSV's over Y_1(N); equal when M = N = lcm.
- (S-A4) W-CRIS itself (the first non-formal node), a bounded computation.
- (S-A5) the CH-specific simplification chi_xi(p) = 1 removes the pr_p diamond seam; for a general triple the ratio would be
  prod (1-beta/alpha)/(1-chi(p)beta/alpha), a Lambda-adic unit but not 1.
Nothing here is a new global theorem; (C_g) is PROVED_BY_RECONSTRUCTION modulo (TF), W-CRIS and the sign/factor-2 seams.

## 5. What gate A does NOT give
Even with (C_g) exact, the object compared is the class of the triple (f, g, g^c) = (f, g, g). By gate B this class specializes to
zero at the CH weight-one point, so (C_g) transports BSV's reciprocity law to a class that is irrelevant to kappa_{alpha,alpha^{-1}}.
