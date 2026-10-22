# H9R19 checkpoint 02 — gate B (refined pair) and the (omega;delta) dictionary

## Gate B sources
- BCPV l.489: "h^c := h (x) eps_h^{-1} the conjugate family. eps_h = eps_h^{(t)} by assumption. [LoefflerCMB Lemma 3.4]
  h^c primitive of level N_h. We identify W_{h^c} with W_h."  => g^c = g (x) eps_g^{-1} (TAME twist), same weight space.
- BCPV l.557: ad(T_g) ~ T_g (x) (T_{g^c} (x) chi_g^{-1} chi_cyc^{-1}); l.636: T_g^{+-} (x) T_{g^c}^{-+} ~ chi_g chi_cyc;
  l.570-571: gbar_lambda := g_lambda^c (x) psi_lambda^{-1} "coincides with the complex conjugate of g_lambda" (weight-2 wild pts).
- BCPV l.339: W_3 = W_f x W_g x W_g, iota_{2,3}(kappa,lambda) = (kappa,lambda,lambda): SAME point lambda in slots 2,3.
- BCPV l.660: "the G_{Q_p}-action on T_g^- (x) T_{g^c}^+ (chi_g^{-1}chi_cyc^{-1}) is trivial" — the trace line.
- CH l.1041: chi a RING CLASS character of K (=> chi^c = chi^{-1}, chi|_Q = 1, nebentype of theta_chi = eta_{K/Q}).
- CH l.1078: g = theta_chi(S_2), h = theta_{chi^{-1}}(S_3), BOTH in S^o(C, omega^{-1} eta_{K/Q}, O[[S]]) => eps_g^{(t)} = eta_K.
- CH l.1035: p O_K = p pbar split => eta_K(p) = +1.
- CH l.1338-1348: alpha = chi(p), beta = chi(pbar); g_alpha, h_{alpha^{-1}} weight-1 stabilizations at S = v-1; four classes
  kappa(f,g_alpha,h_{alpha^{-1}}), kappa(f,g_alpha,h_{beta^{-1}}), kappa(f,g_beta,h_{alpha^{-1}}), kappa(f,g_beta,h_{beta^{-1}}); alpha != +-1 (l.1350).
- CH l.1355-1383 Cor 4.8: (1) kappa_{alpha,alpha^{-1}}, kappa_{beta,beta^{-1}} in Sel(K,V_pE); (2) kappa_{alpha,beta^{-1}} = kappa_{beta,alpha^{-1}} = 0,
  proof via the 3-variable class of the triple (f, theta_chi(S_2), theta_chi(S_3)) [l.1362-1364: h' = theta_chi(S_3) — SAME family as g],
  specialized on the line (v(1+T)-1, v(1+T)^{-1}-1), F^+ analysis, Cornut-Vatsal (sign +1).

## Gate B derivation (source-exact)
1. chi ring class => chi^{-1} = chi^c => theta_{chi^{-1}} = theta_{chi^c} = theta_chi: CH's g and h are the SAME weight-one form,
   distinguished only by the U_p root: h_{alpha^{-1}} = g_beta (root alpha^{-1} = chi^{-1}(p) = chi(pbar) = beta), h_{beta^{-1}} = g_alpha.
2. BCPV's g^c = g (x) eta_K. For a CM family by K, twisting by eta_K is the identity on a_l (l inert: a_l = 0; l split: eta=1;
   l | D_K: newform completion gives a_l back) => g^c = g as primitive families, the identification W_{g^c} = W_g is the identity,
   a_p(g^c) = eta_K(p)^{-1} a_p(g) = a_p(g).
3. Hence BCPV's diagonal iota_{2,3} at the CH weight-one point lambda_0 is (g_{lambda_0}, g^c_{lambda_0}) = (g_alpha, g_alpha)
   = (g_alpha, h_{beta^{-1}}) in CH's labelling: the SAME-ROOT pair.
4. CH Cor 4.8(2): kappa(f, g_alpha, h_{beta^{-1}}) = 0.  And CH's class of interest is kappa_{alpha,alpha^{-1}} = kappa(f,g_alpha,g_beta),
   the DIFFERENT-ROOT pair, which is the diagonal specialization of the triple (f, g, h) with h = theta_chi(S) in the CONJUGATE
   Psi-direction (a_p(h)|_{S=v-1} = alpha^{-1}), a different Hida branch through theta_chi; h != g^c.
5. Local lines at weight one (V_g|G_{Q_p} = unr(alpha) (+) unr(beta), unramified since weight 1, eps_p = 1):
   BCPV (g_alpha, g_alpha): F^-V_g (x) F^+V_{g^c} = unr(alpha) (x) unr(beta) = unr(alpha beta) = trivial  [BCPV l.660 "trivial", consistent];
   CH (g_alpha, g_beta):    F^-V_{g_alpha} (x) F^+V_{g_beta} = unr(alpha) (x) unr(alpha) = unr(alpha^2) = L(alpha/beta) (beta = alpha^{-1}).
   Under V_h ~ V_g^dual, unr(alpha) in V_h is (F^+V_g)^dual, so the CH g-dominant line is F^-V_g (x) (F^+V_g)^dual, on which
   tr: V_g (x) V_g^dual -> L vanishes. So BCPV's (id (x) tr) [l.1118-1120] is ZERO on the CH class's g-dominant line.
   => Pro 6's refinement mismatch CONFIRMED and sharpened: in the ring-class case g^c = g and the BCPV diagonal is the
      Cornut-Vatsal-vanishing class.
6. General ring-class-free case (chi|_Q = phi != 1): g^c = g (x) phi^{-1} = theta_{chi^{-1} Psi^c}-family, a_p(g^c) = phi(p)^{-1} alpha
   = beta^{-1} (alpha beta = phi(p) at weight 1): BCPV's pair is (g_alpha, h_{beta^{-1}}) exactly as Pro 6 states.

## (omega;delta) dictionary — DR22 source
- DR22 l.2053: <a1,a2,a3> Delta_r[d] = Delta_r[a2a3 d1, a1a3 d2, a1a2 d3]; l.2058: sigma_m Delta_r[d] = Delta_r[m d1, m d2, m d3];
  l.2345: sigma_m kappa_r[a,b,c] = kappa_r[ma,mb,mc]; l.2379: j(<d>) = cl(Delta_r^o[a d2d3, b d1d3, c d1d2]).
- The tame diamond orbits on index triples I_1 are the two ORIENTATION classes (abc square / non-square) [l.2910-2911, 2929-2952];
  sigma_m with m a non-square swaps them [l.2917-2919]. The map (a,b,c) -> [bc,ac,ab] is 2-to-1 onto the square orbit only.
- Printed l.2536-2538 sums kappa_inf[bc,ac,ab]; printed l.2788 (cor:special-klm) sums Delta_1^o[a,b,c] over ALL [a,b,c] in I_1.
  With the ALL-triples reading (l.2788), both claims of lemma:iwasawa-cycles verify exactly:
     sigma_m -> (delta^{-3} omega_1omega_2omega_3)^{-1}(m) = delta(m)   [uses delta^2 = omega_1omega_2omega_3]
     <d>     -> (delta^2/omega_2omega_3, delta^2/omega_1omega_3, delta^2/omega_1omega_2) = omega_123.
  With the printed [bc,ac,ab] reading, kappa(omega;delta) = p^3 e_{(delta omega_i^{-1})} kappa[1,1,1] is supported on ONE orientation
  orbit, has diamond eigencharacter (delta omega_i^{-1}) (not omega_123), and is moved off itself by non-square sigma_m, so it
  cannot descend to Q (contradicts l.2545, l.2860). => INTERNAL DISCREPANCY D-DR22-2538: "[bc,ac,ab]" at l.2538 should read
  "[a,b,c]" (as at l.2788). Same one-orbit slip underlies BCPV's e_0^{(x)3} symmetrization (= H9R17's Q-rationality defect D2)
  and the p^3 vs p^3/2 constant in DR22 l.3248-3250 (degree (p-1)^3 "onto Delta_01" counts both orbits).
- Physical content, convention-free: the weighted class is the projection of the two-orbit base class onto the tame-diamond
  eigenspace whose character equals the branches' Lambda-adic (weight-2-normalized) tame diamond eigenvalues, i.e. their
  weight-2 p-nebentypes: (1, omega^{-1}, omega^{-1}) for (f, g, g^c=g) [CH l.1078], twisted by delta with delta^2 = product.
  In DR22's all-triples labelling this is Pro 6's (omega_1,omega_2,omega_3;delta) = (1,omega^{-1},omega^{-1}; omega^{-1}) (or
  delta.lambda); H9R18-P2's (omega^2,omega,omega;omega^2) is the same eigenspace written with coefficient characters
  delta^{-1}omega_i in the [bc,ac,ab] pattern — a labelling difference, not a different class, once the Hom-dual sign is fixed.
- BSV's Xi_fgh tame part omega^{(4-k_o-l_o-m_o)/2} = 1 at centres (2,1,1) (extract l.3127): consistent with Pro 6's
  "Xi = eps_cyc^{-1} at (2,1,1)" up to DR22's explicit (-1) twist (dr22 l.3461).
