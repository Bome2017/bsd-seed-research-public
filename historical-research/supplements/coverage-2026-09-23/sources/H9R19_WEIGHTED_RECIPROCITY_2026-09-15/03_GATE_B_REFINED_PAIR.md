# 03 — Gate B: the refined pair (g, g^c) versus the actual Castella-Hsieh pair

Verdict: Pro 6's mismatch is CONFIRMED from primary sources, and in the ring-class setting it is maximal.

## 1. Sources
- bcpv.tex l.489: "h^c := h (x) eps_h^{-1} the conjugate family. eps_h = eps_h^{(t)} by assumption ... primitive of level N_h.
  We identify the weight space W_{h^c} with W_h."  l.557: ad(T_g) ~ T_g (x) (T_{g^c} (x) chi_g^{-1}chi_cyc^{-1}), i.e.
  T_{g^c} ~ T_g^dual (x) chi_g chi_cyc = T_g (x) eps_g^{-1}.  l.339: iota_{2,3}(kappa,lambda) = (kappa,lambda,lambda).
  l.570-571: gbar_lambda := g_lambda^c (x) psi_lambda^{-1} "coincides with the complex conjugate of g_lambda" (weight-2 points only).
  l.660: the G_{Q_p}-action on T_g^- (x) T_{g^c}^+ (chi_g^{-1}chi_cyc^{-1}) is trivial (the trace line).
- ch extract l.1041: chi a ring class character of K, conductor c O_K, (pN_f, c D_K) = 1; l.1035: p splits, p = p pbar.
  l.1078: g = theta_chi(S_2), h = theta_{chi^{-1}}(S_3) in S^o(C, omega^{-1} eta_{K/Q}, O[[S]]); l.1338-1340: alpha = chi(p), (g_alpha, h_{alpha^{-1}})
  the weight-one specializations at S = v-1 with U_p-eigenvalues alpha, alpha^{-1}; l.1345-1348: beta = chi(pbar), four classes
  kappa(f,g_alpha,h_{alpha^{-1}}), kappa(f,g_alpha,h_{beta^{-1}}), kappa(f,g_beta,h_{alpha^{-1}}), kappa(f,g_beta,h_{beta^{-1}}); l.1350: alpha != +-1.
  l.1355-1383 Cor 4.8: (1) kappa_{alpha,alpha^{-1}}, kappa_{beta,beta^{-1}} in Sel(K, V_pE); (2) kappa_{alpha,beta^{-1}} = kappa_{beta,alpha^{-1}} = 0,
  proved via the 3-variable class of (f(S_1), theta_chi(S_2), theta_chi(S_3)) [l.1362-1364: third family = theta_chi again],
  restricted to (v(1+T)-1, v(1+T)^{-1}-1), F^+ analysis l.1372-1379, Cornut-Vatsal universal-norm vanishing l.1380-1382.

## 2. Derivation
(a) chi ring class => chi trivial on (p) O_c => alpha beta = chi(p) = 1, and chi^{-1} = chi^c => theta_{chi^{-1}} = theta_{chi^c} = theta_chi.
    So CH's g and h are the SAME weight-one form; h_{alpha^{-1}} = g_beta and h_{beta^{-1}} = g_alpha (beta^{-1} = alpha).
(b) BCPV's conjugate of CH's g: eps_g^{(t)} = eta_K (l.1078), so g^c = g (x) eta_K. A CM-by-K family is fixed by the eta_K-twist
    (a_l = 0 for l inert, eta_K(l) = 1 for l split, newform completion at l | D_K), and a_p(g^c) = eta_K(p)^{-1}a_p(g) = a_p(g).
    Hence g^c = g as primitive families, W_{g^c} = W_g is the identity, and the diagonal point (lambda,lambda) is the SAME
    stabilization twice.
(c) At the CH weight-one point: (g_{lambda_0}, g^c_{lambda_0}) = (g_alpha, g_alpha) = (g_alpha, h_{beta^{-1}}) in CH's labelling.
    CH Cor 4.8(2): kappa(f, g_alpha, h_{beta^{-1}}) = 0. The class is the specialization of the (f, theta_chi(S_2), theta_chi(S_3))
    three-variable class at (x_1, v-1, v-1) — exactly BCPV's ad(T_g)-diagonal at that point (up to the nonzero constants).
(d) CH's nonvanishing class kappa_{alpha,alpha^{-1}} = kappa(f, g_alpha, g_beta) is the diagonal specialization of (f, g, h) with
    h = theta_{chi^{-1}}(S) = theta_{chi Psi_S^c}: the CM branch in the CONJUGATE Psi-direction, a_p(h)|_{S=v-1} = alpha^{-1} != alpha =
    a_p(g^c)|_{S=v-1}. So h != g^c as Hida branches: two distinct branches through theta_chi, and BCPV's ad(T_g) uses the wrong one.
(e) Pro 6's general form. If chi|_Q = phi != 1 then g^c = g (x) phi^{-1} = theta_{chi^{-1}Psi^c}-family with a_p(g^c) = phi(p)^{-1}alpha =
    beta^{-1} (alpha beta = phi(p)): BCPV's pair is (g_alpha, h_{beta^{-1}}), "root alpha/eps(p) = beta^{-1}", as Pro 6 states.
    In the ring-class case phi = 1 and this reads (g_alpha, g_alpha).

## 3. Local lines at the weight-one point (V_g|G_{Q_p} = unr(alpha) (+) unr(beta), unramified: weight 1, eps_p = 1)
- BCPV pair (g_alpha, g_alpha): F^-V_g (x) F^+V_{g^c} = unr(alpha) (x) unr(beta) = unr(alpha beta) = trivial. Matches bcpv l.660.
- CH pair (g_alpha, g_beta): F^-V_{g_alpha} (x) F^+V_{g_beta} = unr(alpha) (x) unr(alpha) = unr(alpha^2) = L(alpha/beta). Pro 6's line, confirmed.
- Under V_h ~ V_g^dual, unr(alpha) in V_h is (F^+V_g)^dual, so the CH g-dominant line is F^-V_g (x) (F^+V_g)^dual, on which the
  trace V_g (x) V_g^dual -> L vanishes. BCPV's Delta^{(tr)} := (id (x) tr) res_p Delta^et (l.1118-1120) is identically zero on it.
  Since alpha^2 != 1 (l.1350) the line is not trivial, so no re-normalization rescues the trace projection.

## 4. Consequences
- BCPV's g-dominant trace square, on the CH data, evaluates the class of (f,g,g), which is 0 at the target point: the arrow
  "weighted big Kummer trace -> L-value" is closed for kappa_{alpha,alpha^{-1}} regardless of gate A.  L_VALUE_PRODUCED = NO.
- The printed projections compatible with the CH class:
  (i) CH Theorem 4.6 (Darmon-Rotger; l.1192-1201): L_p^f(test) = (alpha_p/2)(1 - alpha_p^{-1}a_p(g)a_p(h)^{-1}) Col^eta(loc_p kappa), on the
      line (x_1, S, S) of (f, g, h), proved at weight-2 points with wild eps_x of conductor p^s using DR17a Prop 2.10/Cor 2.11
      and the Gauss sum g(eps_x) (l.1265-1321) — i.e. the "tame omega^{-1} + wild" specialization is handled in print there;
      CH Theorem 4.7 then gives Col^eta(loc_p kappa) = +- Psi_T^{c-1}(sigma_{N+}) Theta_{f/K}(T) . (algebraic, nonzero). Analytic object: Theta_{f/K}.
  (ii) BSV Theorem A with xi = f or xi = g on the triple (f, g, h) (centres (2,1,1); Assumptions 1.1, 1.2 hold): a Perrin-Riou
      big logarithm on the unr(alpha^2)-line, not a trace to R_g.
- The sealed tower, MPC, H_pi and the weighted big trace are untouched by this; what changes is the analytic projection
  applied after them, which must be re-chosen for the triple (f,g,h).
