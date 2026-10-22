# H9R19 checkpoint 01 (findings so far, verified in source this session)

## Packet checks
- All 6 SHA-256 match. BSV pdftotext extract reproduces at 5682 lines (packet line numbers valid).
- G3 resolved: DR22 self-duality `\chi_{f} \chi_{g} \chi_{h} = 1` is at dr22.tex l.2812 and l.3324 (braces, so the
  packet's pattern search missed it). H9R18-P2 cited l.2806 (blank) and l.3325 (off by one).

## DR22 conventions (source)
- l.990-991: W = Spf Z_p[[1+pZ_p]] (WILD weight space only). l.1001-1006: arithmetic points nu_{k,eps}(n)=eps(n)n^k with
  eps a character of (1+pZ/p^r) [wild]. l.1023: nu_{k,eps} o eps_cyc_underline = eps.<eps_cyc>^k = eps.eps_cyc^k.omega^{-k}.
- l.1028-1045 def-Hida-fam: specialization at nu_{k,eps} lies in S_k(Mp^r, chi.eps.omega^{-k}) (k = weight-2 here, "kk").
  => with eps wild, the tame p-part of the nebentype is omega^{-kk} ALWAYS  == BCPV's omega^{k_o - wt} with k_o = 0.
  => DR22's printed Hida families are k_o = 0 families (unless eps is silently allowed a tame part).
- l.1049-1057 tame-cris: "tame if eps factors through (Z/pZ)^x" (vacuous if eps wild); "crystalline iff eps.omega^{-kk}=1
  i.e. trivial nebentypus at p".
- l.1097-1102 Wiles-ord: V^+ = Lambda(psi^{-1} chi eps_cyc^{-1} eps_underline), V^- = Lambda(psi).
- l.2524-2540 eqn:cycles-tame: kappa_inf(omega;delta) = p^3/(p-1)^3 Sum delta^{-1}(abc) omega_1(a)omega_2(b)omega_3(c) kappa_inf[bc,ac,ab],
  omega_1omega_2omega_3 = delta^2, two deltas differ by the quadratic character (l.2530).
- l.2542-2554 lemma:iwasawa-cycles: sigma_m acts by delta(m); diamonds <a1,a2,a3> by omega_123. Proof: "direct calculation".
- l.2784-2795 cor:special-klm: general omega; l.2808-2818 sec:cris: chi_f chi_g chi_h = 1 assumed (l.2812); crystalline point
  defined by eps_i omega^{-kk_i} = 1 (l.2818); l.2855-2857 kappakappa is a TAUTOLOGY at crystalline points.
- l.2879: "crystalline => diamonds in Gal(X_1/X_01) act trivially on the eigencomponents => mu_*^3 iso".  <- THIS is the
  place a nontrivial tame p-nebentype would kill the class under mu_*^3 (projection to Gamma_0(p)-level).
- l.2891-2928 lemma-klm: mu_*^3 Delta_1[a,b,c] depends only on (abc/p); Delta_01 = Delta_01^+ + Delta_01^- over Q.
- l.3239-3257: kappa_01 = p^3 pi AJ(eps Delta_01^{klm}) via cor:special-klm at (1,1,1;1) with "delta = 1 trivial".
- l.3261-3281 prop:main-crystalline: (varpi_1)^3_* kappa_1 = E^bal/(E(f_a)E(g_a)E(h_a)) kappa(f,g,h) [DR14 cycle].
- l.3321-3449 sec 3.1: L_p^f(test vectors) in Q_f (x) Lambda_g (x) Lambda_h; Hsieh interpolation (padicL-Garrett) on W^f.
- l.3452-3550: V^dag_fgh = V_f(x)V_g(x)V_h(-1)(1/2), (1/2) = (eps_f eps_g eps_h)^{-1/2} WILD half-twist; 4-step filtration
  with characters built from Psi (unramified), chi_f,chi_g,chi_h (TAME LEVEL chars, unramified at p), eps_cyc, eps_underline.
  NO Teichmuller character appears anywhere in the filtration characters.
- l.3480-3497 def-family: kappa(f,g,h) := (1/C_q) varpi_*(kappa_inf(1,1,1;1)).
- l.3629-3650: eta_f^{gh} = Psi_f^{gh} x Theta_f^{gh}, Theta = Lambda-adic cyclotomic char specializing to eps_cyc^t, t=(-k+l+m)/2.
- l.3680-3701 var-per: Lambda-adic de Rham pairing via Prop klz-prop (Ohta/KLZ), factors 1/(E_0 E_1).
- l.3724-3740 prop pr: 3-variable Perrin-Riou regulator, interpolation (i) balanced: (-1)^t/t! E^PR log_BK; proof "standard
  methods as in KLZ Thm 8.2.8, LZ14 App B, DR2 5.1".
- l.3743-3770 cor:crystalline-lambda: kappa_p in image of H^1(Q_p,V^+) by density of balanced crystalline points + Saito purity.
- l.3781-3856 Theorem L=L and proof: checked on balanced CRYSTALLINE points with f_x,g_y,h_z stabilizations of level-M forms;
  ingredients: var-per, klz-prop, pr, prop:main-crystalline, DR14 main theorem, Euler factor identity E^f = E^bal E^PR.

## BSV conventions (extract)
- l.121-133: families have CENTRES k_o,l_o,m_o; U_f disc centred at k_o in W; U_f^cl = {k in U_f cap Z>=2 : k = k_o mod 2(p-1)};
  f_k^sharp in S_k(N_f p, chi_f), level Gamma_1(N_f) cap Gamma_0(p), character chi_f. => ALL classical points have trivial
  p-nebentype (crystalline, or weight-2 p-new). BSV never specialize at tame non-crystalline points.
- l.134-140 Assumption 1.1 (u_o = 1 case: weight-one specialization is p-stabilisation of classical cuspidal p-regular newform,
  no RM by real quadratic field with p split). l.165 Assumption 1.2 chi_f chi_g chi_h = 1.
- l.3124-3130: Xi_fgh(g) = omega_cyc(g)^{(4-k_o-l_o-m_o)/2} . kappa_cyc(g)^{(4-k-l-m)/2}; V(f,g,h) = V(f)(x)V(g)(x)V(h)(x)Xi_fgh.
  => the TAME part of the self-dual twist is omega^{(4-k_o-l_o-m_o)/2}: = omega^{-1} for centres (2,2,2) [BCPV], = 1 for (2,1,1) [CH].
- l.3188-3203: H^1_bal = H^1(Q_p, F^2 V); p_f, p_g, p_h projections. l.3305-3320 Prop 7.3: L_f = Log(f,g,h) with interpolation
  (p-1)alpha_k (1 - beta_k alpha_l alpha_m/p^{c_w}) (-1)^{c_w-k}/(c_w-k)! log_p(Z_w)_f on Sigma_bal; factors through p_f*.
- l.4387-4513 §8.5: Theorem A proved on Sigma^o_bal = balanced (k,l,m), k,l,m >= 3, p not dividing conductors; dense; uses
  Thm 8.1, Prop 8.3 (specialization = explicit multiple of the classical diagonal class), Lemma 8.4, Prop 7.3, Prop 3.6 (explicit
  reciprocity law at a fixed classical balanced triple, from BSV20b). Nothing in 8.5 uses the centres.
- l.2829-2909 §6: L_p^f(f,g,h) in O_fgh by Hida's method interpolating at Sigma^gen_f; Remark 6.2: BSV's L_p^f = DR14's
  L_p^f(w_N(f^*),g,h). l.2911-2964 Hsieh interpolation under Assumption 6.3.

## CH conventions (extract)
- l.908-919: S^o(N,chi,I), chi mod Np "branch character"; f_x in S_{k_x}(Np^{r_x+1}, chi omega^{2-k_x} eps_x).
- l.1075-1079: f in S^o(N_f, I) with branch character chi_f = 1; g = theta_chi(S_2), h = theta_{chi^{-1}}(S_3) BOTH in
  S^o(C, omega^{-1} eta_{K/Q}, O[[S]]), C = D_K l^{2m}.  => tame diamond eigenvalue (p-nebentype at weight 2) = omega^{-1} for BOTH
  g and h = g^c.  Types (t_f,t_g,t_{g^c}) = (0,-1,-1): CONFIRMS H9R18-P2, REFUTES H9R17A's (0,-1,+1).
- l.1009-1017: chi_f chi_g chi_h = omega^{2a}, here omega^{-2}, a = -1; det V_fgh = X^2 eps_cyc with X p-ramified,
  X(c) = (-1)^a; V^dag := V_fgh (x) X^{-1}.   <- THIS is the packet's Xi (CH's script X). Tame part of X: a square root of
  omega^{-2}.(1) i.e. omega^{-1} or omega^{-1}.quadratic. Two choices = DR22's two deltas.
- l.1142-1143, 1338-1340: g = theta_chi, h = theta_{chi^{-1}} weight 1, p-stabilizations with U_p eigenvalues alpha=chi(p_frak),
  alpha^{-1}; specialization at S = v-1.
- l.1192-1201 Thm 4.6 (Darmon-Rotger): L_p^f(test) = alpha_p/2 (1 - alpha_p^{-1}a_p(g)a_p(h)^{-1}) Col^eta(loc_p kappa) — an
  f-dominant reciprocity law along the line S_2=S_3 at weight-2 f, proved by checking at weight-2 points x with wild eps_x of
  conductor p^s (l.1265-1321), using DR17a Prop 2.10 / Cor 2.11 (AJ_p of the twisted diagonal cycle Delta_s at Gamma_1(Np^s)
  level with wild nebentype) and a Gauss sum g(eps_x).
