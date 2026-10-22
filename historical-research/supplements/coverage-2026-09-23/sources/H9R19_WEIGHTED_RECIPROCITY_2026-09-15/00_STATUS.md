# H9R19 — Weighted reciprocity source reconstruction — STATUS (2026-09-15)

Continues H9R18-P2 (frozen obstruction G_WEIGHTED_RECIPROCITY, "NOT_PRINTED for delta != 1"). Source-first, read-only on
the packet; all line numbers index the files in 05_FILES_CONSULTED.sha256 (same hashes as the H9R19 anchor packet; the BSV
pdftotext extract reproduced at 5682 lines). Nothing in H9R16-C, MPC, H_pi or the geometric point tower was reopened.

```
OMEGA_WEIGHTED_RECIPROCITY = PROVED_BY_RECONSTRUCTION
    (conditional: (TF) torsion-freeness of H^1(Q, V^dag_{fgh}(M)); the one unprinted node W-CRIS below, a formal
     Clebsch-Gordan/diamond bookkeeping; residual scalar pinned to {+-1} x {1, 2^{+-1}} by two named convention seams)

FIRST_NONFORMAL_NODE = dr22.tex l.3239-3257, Proposition (cycleDR01): kappa_01 = p^3 pi AJ_et((eps)Delta_01^{klm}).
    Its printed proof reads "in which delta = 1 is the trivial character" and counts the mu^3-degree on ONE tame orbit.
    Everything upstream (cor:special-klm l.2784-2795) is printed for general (omega;delta); everything downstream
    (prop:main-crystalline l.3261-3317, sec 3.1, sec 4.2, Theorem L=L l.3781-3856) is CHARACTER_BLIND or FORMAL.

EXACT_MISSING_LEMMA = (W-CRIS) Let (f,g,h) have tame diamond types (t_1,t_2,t_3) [weight-2 p-nebentypes omega^{t_i}] and let
    (kk,ll,mm) be a balanced triple that is crystalline for all three, i.e. kk_i = t_i mod (p-1), eps_i wild-trivial.
    Let Delta_1^o(omega;delta) be DR22's weighted cycle (l.2788) with diamond eigencharacter (omega^{t_1},omega^{t_2},omega^{t_3})
    and delta a square root of omega^{t_1+t_2+t_3}. Then
        mu_*^3  pi_{f_a g_a h_a} AJ_{kk,ll,mm}( Delta_1^o(omega;delta) ) = c_p . pi_{f_a g_a h_a} AJ_et( (eps_kk,eps_ll,eps_mm) Delta_01^{kk,ll,mm} ),
    with c_p = p^3 (DR22's constant) or p^3/2 (see 04, D-DR22-ORBIT), the SAME constant as at (1,1,1;1).
    Mechanism: at such a point the level-p geometric diamonds act trivially on the eigencomponent (dr22 l.2879) because the
    Clebsch-Gordan section (l.2692-2695) transforms by the moment weights (a_1^{kk} a_2^{ll} a_3^{mm}) which cancel the tame
    weights exactly when kk_i = t_i; the tame sum then collapses to (p-1)^3 as in the delta = 1 case.
    Once W-CRIS holds, the comparison (C_g) of the amendment follows with an explicit scalar — see 02_GATE_A.

ANALYTIC_OBJECT = BSV's square-root Garrett-Rankin p-adic L-function L_p^xi(f,g,h) in O_fgh (bsv extract l.2896-2909), xi = g,
    for Hida families with CENTRES (k_o,l_o,m_o) = (2,1,1); the reciprocity law is bsv Theorem A (l.217-219), proved in
    sec 8.5 (l.4387-4513) on Sigma^o_bal, which is dense for centres (2,1,1). BSV's construction (l.3446-3463) carries the
    tame weights through the centres: kappa*_f = omega^{(l_o+m_o-k_o-2)/2}<u>^{...} etc., i.e. (omega^{-1},1,1), total omega^{-1}
    at (2,1,1) — this IS the weighted datum. The BCPV transcription (thm_reciprocity_big_diag) remains NOT_PRINTED for
    delta != 1, but its source is printed.

NORMALIZATION = weighted datum (omega_1,omega_2,omega_3;delta) = (1, omega^{-1}, omega^{-1}; omega^{-1}) [or delta.(./p)],
    diamond eigencharacter = weight-2 p-nebentypes (CH l.1078: branch character omega^{-1}eta_K for g AND h), agreeing with
    Pro 6; H9R18-P2's (omega^2,omega,omega;omega^2) is the same eigenspace in the [bc,ac,ab] coefficient labelling.
    Scalars tracked: p^3/(p-1)^3 (DR22 l.2536/2788), 1/C_q (DR22 l.2866, 3494), 1/a_p(k) (BSV (155) l.3489),
    (p-1)alpha_{f_k} (BSV Thm 8.1 l.3586 and Prop 8.3 l.3975 — they CANCEL), E^bal (both papers, identical), 1/(E(f_a)E(g_a)E(h_a))
    (DR22 l.3267-3280) vs Pi^alpha_* = (x)(pr_{1*} - beta/p^{k-1} pr_{p*}) (BSV (169) l.3937-3942); on the CH triple chi_xi(p) = 1
    for all xi, so the pr_p-vs-pi_2 diamond seam is invisible and the two Euler-factor normalizations coincide.
    Residual: sign of BSV Prop 3.7 (l.1393-1395, "up to sign") and DR22's one-orbit degree count (04 D-DR22-ORBIT, factor 2).

ROOT_NUMBER_INPUT_USED = NONE for the reciprocity identity (BSV Remark 1.8(1) l.338-340: Theorem A holds regardless of
    Assumption 1.7). Used: Assumption 1.2 (chi_f chi_g chi_h = 1: 1.eta_K.eta_K = 1) and Assumption 1.1 (weight-one
    regularity: alpha != beta, i.e. chi(p) != chi(pbar), CH's alpha != +-1 l.1350; theta_chi has CM by imaginary K, no RM).
    BCPV's (RN) l.481-486 stays NOT_ESTABLISHED and is NOT needed for this step.

L_VALUE_PRODUCED = NO   (for the Castella-Hsieh target).  Reason: gate B (03). BCPV's conjugate family is g^c = g (x) eps_g^{-1}
    (bcpv l.489); for CH's g, eps_g^{(t)} = eta_K and g is CM by K, so g^c = g and BCPV's diagonal (kappa,lambda,lambda)
    specializes at the CH weight-one point to the SAME-ROOT pair (g_alpha, g_alpha) = (g_alpha, h_{beta^{-1}}), whose class is
    ZERO by CH Cor 4.8(2) (Cornut-Vatsal). The CH class kappa_{alpha,alpha^{-1}} = kappa(f,g_alpha,g_beta) lives on the triple
    (f,g,h) with h the conjugate-direction CM branch (a_p(h)|_{S=v-1} = alpha^{-1}), h != g^c, and BCPV's trace projection
    (id (x) tr, l.1118-1120) vanishes identically on that triple's g-dominant line F^-V_g (x) F^+V_h = unr(alpha^2).
    The weighted reciprocity law therefore produces L_p^g(f,g,g)|_{W_2}, the L-value of a class that is zero at the target
    point — not an L-value for kappa_{alpha,alpha^{-1}}.

NEXT_HANDOFF =
  (1) W-CRIS + the two scalar seams: a bounded computation (Clebsch-Gordan diamond weights at crystalline points; BSV
      Prop 3.7 sign; DR22 orbit/degree factor 2). Deliverable: (C_g) with scalar in {+-1, +-2^{+-1}} made exact.
  (2) RETARGET the analytic arrow. The sealed tower + weighted big trace feed BCPV's (f,g,g^c)-diagonal, which is the
      vanishing class at the CH point. The printed projections compatible with the CH class are: CH Thm 4.6 (Darmon-Rotger,
      f-dominant, Coleman map Col^eta on the line (x_1,S,S), proved at weight-2 wild points with Gauss sums g(eps_x), CH
      l.1265-1321) feeding CH Thm 4.7 (Theta_{f/K}); and BSV Theorem A with xi = f or g on the triple (f,g,h) — NOT the
      ad(T_g)-trace. Decide whether the big Kummer trace has any role on (f,g,h); prima facie it does not (the trace kills
      the relevant line), so the "big trace -> L-value" arrow is closed for the CH refinement, independently of gate A.
```

## Addendum 2026-09-16 (see 08, terminal block): under Castella Thm A (file 22) and kappa != 0, the live endpoint q_Sha(kappa) = 0 is
## EQUIVALENT to rank E(Q) = 2, i.e. to Sha(E/Q)[p^inf] finite. Seven audited routes (files 10-14, 19, 20) all failed at the step
## "p-adic object -> second rational point", which is this equivalence. No route with printed inputs remains. Lane closed at that boundary.
