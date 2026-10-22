# 09 — Branch-involution audit: the g/h sheets, the graph lambda -> (lambda, iota_CM(lambda)), and the H9R16 modified pairing

Labels: [V] verified verbatim in a source (line/page given); [D] derived here from [V] facts by a computation anyone can redo;
[O] open, for H9R20. CH page numbers are the rendered PDF (pages 20-25 were read as images; the text extract conflates
p and the prime p_frak, so extract line numbers are given only where unambiguous).

## 1. The two CM sheets through theta_chi, and the involution

[V] CH l.1088-1092: Psi_T is the universal character of Gamma_{p_frak^infty} = Gal(K_{p_frak^infty}/K), the p_frak-RAMIFIED Z_p-extension
    (Psi_T(sigma) = (1+T)^{l(sigma)}); Psi_T^{1-c} factors through the anticyclotomic Gamma_infty.
[V] CH p.22 (proof of Thm 4.6): at a weight-2 point x with psi_x := Psi_T|_{T = zeta v - 1}, (g_x, h_x) are the theta series of
    (chi psi_x^{-1}, chi^{-1} psi_x^{-1}) with a_p(g_x) = chi psi_x^{-1}(sigma_{pbar}) and a_p(h_x) = chi^{-1} psi_x^{-1}(sigma_{pbar}).
[V] CH p.23 sec 4.6: alpha = chi(pbar), beta = chi(p_frak); g_alpha, h_{alpha^{-1}} are the S = v-1 specializations of (g,h); the four
    classes arise by "alternatively changing the roles of p_frak and pbar in the construction of g and h".
[V] CH l.1078: g = theta_chi(S_2), h = theta_{chi^{-1}}(S_3), both primitive CM Hida families in S^o(C, omega^{-1}eta_{K/Q}, O[[S]]).
[D] Since chi is a ring class character, chi^{-1} = chi^c and theta_{Phi^c} = theta_Phi for every Hecke character Phi (same
    q-expansion). Hence h = theta_{chi^{-1} Psi_S^{-1}} = theta_{chi Psi_S^{-c}}: the SAME construction as g with the Psi-direction
    conjugated (p_frak-ramified -> pbar-ramified). The two sheets are exchanged by the automorphism c of K applied to the CM
    datum with the weight coordinate fixed:  iota_CM = id on Spf O[[S]], g <-> h on branches.  Equivalently, chi -> chi^{-1}
    with Psi fixed. At S = v-1 (Psi = 1) it swaps the two p-stabilizations: g_alpha <-> g_beta (= h_{alpha^{-1}}).
[D] The sheets are Poincare-orthogonal as Hecke eigensystems: a_l(h) - a_l(g) = (chi(lbar) - chi(l))(Psi(l) - Psi(lbar)) != 0
    generically, while BCPV's tame conjugate g^c = g (x) eta_K has a_l(g^c) = a_l(g). So h is NOT g^c and NOT a Galois conjugate
    of g under coefficient conjugation (that would also invert Psi).
[D] Galois representations: T_g = Ind_K^Q(chi Psi^{-1}), T_h = Ind_K^Q(chi^{-1}Psi^{-1}) = Ind(chi Psi^{-c}). At a weight-2 point
    V_{gbar_x} (complex conjugate form) = V_{g_x} (x) (nebentype)^{-1} = Ind(chi psi_x^{-1} . psi_x psi_x^c) = Ind(chi psi_x^c) = V_h at the
    point x' with psi_{x'} = psi_x^{-1}. So "h at the ANTI-diagonal point" is the complex conjugate of g_x, and Lambda-adically
    T_h o iota_anti ~ T_g (x) psi^cyc (iota_anti: (1+T) -> (1+T)^{-1}, CH's line (v(1+T)-1, v(1+T)^{-1}-1)). The ordinary
    filtrations are EXCHANGED under this isomorphism: T_g^+ (x) psi^cyc = (chi psi^{-1} psi psi^c)|_{K_p} = (chi psi^c)|_{K_p} is unramified,
    i.e. it is T_{h o iota}^- not T_{h o iota}^+. At S = v-1: F^+V_{g_alpha} = unr(beta), F^+V_{g_beta} = unr(alpha).

## 2. Does the H9R16 modified pairing survive on the graph?

[V] BCPV l.489-493: the Lambda-adic pairing is T_h (x)_{R_h} T_{h^c} -> chi_h chi_cyc with W_{h^c} = W_h; l.505-529: it interpolates
    <x, W_{N p^r}^{-1}(U_p')^r y> on T_ord(N p^r,k) (x) T_ord(N p^r,k), i.e. a pairing of the branch WITH ITSELF, values in
    Z_p[Delta_{p^r}] (x) eps_h chi_cyc^{k+1}, rewritten as T_h (x) T_{h^c} by moving eps_h^{-1} to the second factor (l.527).
    l.570-574: specialized at lambda it reads V_{g_lambda} (x) V_{gbar_lambda} -> chi_cyc with gbar_lambda = g_lambda^c (x) psi_lambda^{-1}
    "the complex conjugate of g_lambda". l.635-636: T_g^+ and T_{g^c}^+ are orthogonal complements; l.699-706: this orthogonality
    is what sends the balanced local condition into H^1_f(Q, T_f^dag) (x) R_g.
[D] Hecke bookkeeping of l.516: Poincare duality pairs a T_l-eigenvector with eigenvalue a against T_l^*-eigenvalue a; since
    T_l^* = <l>^{-1}T_l and W^{-1} carries the g_psi-eigenspace to the (eps psi)^{-1}-nebentype eigenspace with T_l-eigenvalue
    (eps psi)^{-1}(l) a, the composite <x, W^{-1} y> is non-zero only for x, y BOTH in the g_psi-eigenspace. The wild character
    is absorbed by the group ring, the tame part by eps_h^{-1}. Therefore the modified pairing is intrinsically a self-pairing
    of each branch at each point: it is g <-> g^c (= g for CM), never g <-> h.
[D] Consequently, on the cross-sheet graph lambda -> (lambda, iota_CM(lambda)) at the SAME weight-space point, the modified pairing
    restricted to (g-part) (x) (h-part) is identically zero (different eigensystems, sec 1). The contraction/trace step of
    H9R16 (MPC, ad(T_g) -> R_g) has no analogue there.  VERDICT: the H9R16 modified pairing does NOT survive along the graph.
[D] What does exist across sheets is the UNMODIFIED Poincare duality between g_lambda and its complex conjugate gbar_lambda = h at
    the anti-diagonal point (l.570-574), Lambda-adically T_g (x) (T_h o iota_anti) -> chi_cyc-twist. But because the ordinary
    filtrations are exchanged (sec 1), F^+T_g and F^+(T_h o iota_anti) are NOT orthogonal, so the l.699-706 mechanism fails:
    the trace of a balanced class along the anti-diagonal is not Selmer for f a priori (see sec 3, line IV).

## 3. The four lines through the target point (v-1, v-1) and their Galois/local structure

Representation types (after the critical twist X^{-1}; [V] CH (4.4) l.1119-1121 for line III, CH Cor 4.8 proof p.23 for line II;
[D] for lines I and IV by the same computation, using Ind(Phi)(x)Ind(Phi') = Ind(Phi Phi') (+) Ind(Phi Phi'^c) and the fact that the
wild part of X is psi^cyc on the diagonals and trivial on the anti-diagonals since Phi|_Q Phi'|_Q = 1 there):

| line | third slot | pair at a weight-2 point | V^dag_{f,..} = V_f(1) (x) | F^+ cap (V_f(x) first summand) | class | at T=0 |
|---|---|---|---|---|---|---|
| I  BCPV diagonal (g, g^c=g), (lambda,lambda) | same sheet | (theta_{chi psi^{-1}}, theta_{chi psi^{-1}}) | Ind(1) (+) Ind(chi^2 Psi^{c-1}) | F^0V_f (x) Ind(1): Selmer at p_frak AND pbar [V l.706] | Delta^et(f (x) ad g): Selmer over Q, H9R16 point tower | (g_alpha, g_alpha) = kappa_{alpha,beta^{-1}} = 0 [V Cor 4.8(2)] |
| II (g, g'=theta_chi(S_3)) anti-diagonal | same sheet | (theta_{chi psi^{-1}}, theta_{chi psi}) | Ind(chi^2) (+) Ind(Psi^{1-c}) | F^0V_f (x) Ind(Psi^{1-c}): crystalline | universal norm over K_infty => 0 identically [V Cor 4.8(2) proof] | 0 |
| III CH diagonal (g, h), S_2 = S_3 | other sheet | (theta_{chi psi^{-1}}, theta_{chi^{-1} psi^{-1}}) | Ind(Psi^{1-c}) (+) Ind(chi^2) | V_f (x) (Psi^{1-c})_{p_frak} + 0 at pbar [V Lemma 4.5 proof] | loc_{pbar} = 0 [V Lemma 4.5(2)]; Col^eta(loc_{p_frak}) = Theta_{f/K} != 0 [V Thm 4.7]: p_frak-relaxed, NOT Selmer Lambda-adically | kappa_{alpha,alpha^{-1}} in Sel(K,V_pE) [V Cor 4.8(1)], point-valued in E(Q)(x)L [V Cor 5.1] |
| IV (g, h) anti-diagonal, (v(1+T)-1, v(1+T)^{-1}-1) | other sheet | classical points are WEIGHT-ONE wild twists (theta_{chi phi}, theta_{chi^{-1}phi^{-1}}) at 1+T = zeta, phi = psi_zeta; the weight-2 point of slot 2 is paired with a weight-0 point of slot 3 | Ind(1) (+) Ind(chi^2 Psi^{1-c}) [D, exact at T = zeta-1] | V_f (x) 1_{p_frak} only (1_{pbar} = V_g^- (x) V_h^- has no plus): RELAXED at p_frak, ZERO at pbar | [D] a T-family in the FIXED group H^1(K, V_pE); with z = z^+ + z^-: z^+_p = z^-_p (one condition), sing_{p_frak} = 2 sing(z^+_p) — see 10 | (g_alpha, h_{alpha^{-1}}) = (g_alpha, g_beta): kappa_{alpha,alpha^{-1}} again |

Reading: lines I and IV are "trace type" (trivial constituent, f-extraction over Q/K possible); lines II and III are
"Shapiro type" (anticyclotomic constituent, f-extraction to Hhat^1(K_infty, V_f(1))). The live class sits on III and IV.
The H9 point tower lives on I (Selmer at both primes because g^c's F^+ is the orthogonal line). On III the f-extracted class
is a Kato-type Euler-system class (p_frak-relaxed, Coleman map = Theta_{f/K}); Col^eta at the twist used is a dual-exponential
map (CH sec 3.2, Thm 3.4 with j = -1), which kills H^1_f, so Theta_{f/K} != 0 proves the class is NOT the Kummer image of a
norm-compatible family of points at generic T. Point-valuedness on III holds only at T = 0 (Cor 5.1), and there the point is
an OUTPUT of the analytic route: kappa_{alpha,alpha^{-1}} = C (1-p^{-1}alpha_p)/(1-alpha_p^{-1}) . theta-bar_{f/K}/h^{(rho)}(P,Q) . (P (x) log_p Q - Q (x) log_p P).

## 4. Verdict for H9R20 (retargeting the sealed construction)

1. [D] The cycle tower itself is branch-agnostic: CH p.21 recalls DR17a's kappa_infty = lim (1,U_p,1)^{-s} kappa~_s in H^1(Q, V^ord_infty)
   built on X_0(Np) x X_s x X_s^dag with D_s = {(<a;b>, <a;b^{-1}>)}, and "the triple (f,g,h) defines a natural projection
   varpi_{f,g,h}: V^ord_infty -> V^dag_{f,gh}(N)". Retargeting at the CYCLE level is only a change of Hecke projection
   (varpi_{f,g,g} -> varpi_{f,g,h}); nothing geometric must be rebuilt. This is DR22's tower with the (omega;delta) datum of 00_STATUS.
2. [D] The POINT tower (the H9R16 realization of BCPV's trace class by points) cannot be moved to line III: the class there is
   provably not point-valued Lambda-adically (sec 3). Along III the printed replacement is CH Thm 4.6/4.7: Coleman map -> Theta_{f/K}.
3. [D] Line IV is the only cross-sheet line with a trivial constituent through the live class; it is the exact analogue of BCPV's
   line I with the third slot on the other sheet (honest complex-conjugate pairing, unmodified Poincare duality). Its
   f-extracted class is a T-family in the fixed group H^1(K, V_pE), p_frak-relaxed and pbar-strict.
   OPERATOR CORRECTION (2026-09-15): vanishing of the p_frak-singular component gives the missing LOCAL Bloch-Kato condition
   only; it does NOT identify a Selmer class with a Mordell-Weil Kummer class. The gate is therefore split:
   [O] H9R20-Q1: sing_{p_frak}(kappa_IV(T)) = 0 identically?   [O] H9R20-Q2: which printed regulator/reciprocity law computes it?
   [O] H9R20-Q3: if Q1 = YES, is the resulting Selmer family Kummer-valued (needs Sha(E/Q)[p^infty] finite or equivalent)?
   Fable's source answer to Q1/Q2 (local graded line, printed law, forced zero) is in 10_LINE_IV_PRINTED_LAW.md.
4. [D] The H9R16 modified pairing, MPC, and the trace ad(T_g) -> R_g do not survive on any cross-sheet line (sec 2). On line IV
   the substitute is the projection V_g (x) (V_h o iota_anti) -> Ind(1) -> 1 (a Lambda-adic map of representations, not a Hecke
   self-pairing), whose compatibility with the balanced condition is exactly the one-condition defect above. H_pi and the norm
   element are operator identities on the g-sheet alone and are unaffected, but they feed the same-sheet contraction.

## 5. Discrepancy note (internal)
The pdftotext extract writes K_p for both K_{p_frak} and K_{pbar} and alpha = chi(p) for alpha = chi(pbar) (CH sec 4.6). The
rendered pages fix: alpha = chi(pbar), beta = chi(p_frak), Lemma 4.5(2) is loc_{pbar} = 0, Thm 4.6/4.7 apply Col^eta to loc_{p_frak}.
Nothing in 03_GATE_B changes (it used only alpha beta = 1 and h_{beta^{-1}} = g_alpha).

## Correction (2026-09-16, see 12 sec 0)
"h at the anti-diagonal point is the complex conjugate of g_x" is wrong as a statement about FORMS: gbar_x is anti-ordinary
(a_p = p/a_p(g_x)) and lies on no Hida family; h at iota(x) is the non-classical weight-(2-k) specialization of h. The correct
statement is Lambda-adic and representation-theoretic: V_h o iota_anti = Ind(chi^{-1}Psi_T) = V_g^dual = V_{g^c}(chi_g^{-1}chi_cyc^{-1}),
with the ordinary lines exchanged. Everything in sec 2 (self-pairing, zero across sheets, filtrations exchanged) and the line table
in sec 3 (classical points of line IV are weight-one wild pairs and T = 0) stands.
