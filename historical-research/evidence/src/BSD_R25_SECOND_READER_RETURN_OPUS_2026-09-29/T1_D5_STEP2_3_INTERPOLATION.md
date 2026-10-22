# T1 — D5 Steps 2–3: Col(loc_3 z_gamma) = L_3 exactly.   VERDICT: PASS (one provenance correction, C1)

## THEOREM inputs (read on the rendered Kato pages / source texts)
- Ka 12.5(1) (printed p.221): the image of z_gamma^(p) in H^1(Q_p(zeta_{p^n}), V(f)(k-r)) under exp* lies in
  S(f)⊗Q(zeta_{p^n}), and "x ⊗ y ↦ sum_{sigma in G_n} chi(sigma) sigma(y) per_f(x)^±" (chi: G_n → C^x any character,
  ± = (-1)^{k-r-1} chi(-1)) "sends the image of z_gamma^(p) to (2 pi i)^{k-r-1} · L_{p}(f*, chi, r) · gamma^±."
- Ka 6.2 (printed pp.160–161): "L_S(f,chi,s) = sum_{(n,S)=1} a_n chi(n) n^{-s} = prod_{l not in S}(1 - a_l chi(l) l^{-s}
  + eps(l) chi^2(l) l^{k-1-2s})^{-1}", "(If l divides N, eps(l) means 0.)"  So L_{p} removes ONLY the Euler factor at p.
- Ka 16.2(i),(ii) (printed p.269): L_{p-adic,alpha}(f)(kappa^r chi^{-1}) = (r-1)!·p^{nr} alpha^{-n}·G(chi,zeta_{p^n})^{-1}
  ·(2 pi i)^{k-r-1}·(1/Omega_±)·L_{p}(f,chi,r), chi of conductor exactly p^n, "chi is regarded here as a character of
  (Z/p^n)^x via the cyclotomic character G_n ≅ (Z/p^n)^x", G(chi,zeta) = sum_b chi(b) zeta^b.  (ii): see KILL_TESTS.
- Ka Remark 16.3(1): values at almost all finite-order chi (for h distinct r) characterise elements of H_{h,L}.
- Kob §3 (txt l.243–298): Col_n(z) = sum_sigma (c_n^sigma, z)_{E,n} sigma; (x,z)_{E,n} = Tr_{k_n/Q_p}(log_E^(x) exp*_omega(z)).
- SW 2013 §3.2 (txt l.509–521, R24 task sources): "If chi is the character on G_inf sending gamma to a root of unity
  zeta of exact order p^n, then L_alpha(E, zeta - 1) = (1/alpha^{n+1}) · (p^{n+1}/G(chi^{-1})) · L(E, chi^{-1}, 1)/Omega_E."

## DERIVED
1. Rearrangement (any norm-compatible c, abelian Gamma_n; Galois-invariance of the cup product):
   Col_n(z) = (sum_rho log(c_n^rho) rho)·(sum_tau exp*(z^tau) tau^{-1}); Col is Lambda-linear (Col(tau z) = tau Col(z)).
   Hence chi(Col z) = [sum_sigma L_n^sigma chi(sigma)]·[sum_sigma chi(sigma)^{-1} sigma(exp* z_n)], and 1(Col z) = L_0 exp*(z_0).
2. First bracket = alpha^{-(n+1)} tau(chi), tau(chi) = sum_{a in (Z/p^{n+1})^x} chi(sigma_a) zeta^a, sigma_a(zeta) = zeta^a:
   proved by hand (S_m, m ≤ n, is fixed by Gal(k_n/k_{m-1}), on which a conductor-p^{n+1} chi is non-trivial) and
   checked exactly in PARI for n = 1, 2 (checks/ksr.log; the tau(chi^{-1}) alternative is FALSE for every chi).
   At alpha = -1 the factor is (-1)^{n+1}; it matches SW's 1/alpha^{n+1} and Kato's alpha^{-n} (conductor p^n).
3. Second bracket: Ka 12.5(1) at r = 1, k = 2, level n+1, applied to chi^{-1} (the sum over Gamma_n of the
   corestricted class equals the sum over G_{n+1} since chi is trivial on Delta):
   sum_sigma chi(sigma)^{-1} sigma(exp*_{omega_E} z) = L_{p}(E, chi^{-1}, 1)/Omega_+ = L(E, chi^{-1}, 1)/Omega_+ (chi ramified).
4. So Col(loc z_gamma)(chi) = alpha^{-(n+1)} tau(chi) L(E,chi^{-1},1)/Omega_+. Birch's lemma (derived: f_chi =
   tau(chi-bar)^{-1} sum_a chi-bar(a) f(tau + a/m)) gives sum_a chi(a) lambda^+(a/m) = tau(chi) L(E,chi-bar,1) for even chi, i.e.
   SW's integral = alpha^{-(n+1)} tau(chi) L(E,chi^{-1},1)/Omega_E, equal to SW's printed p^{n+1}/G(chi^{-1}) form since chi(-1) = 1.
   And Ka 16.2(i) at kappa·chi gives the same (G(chi)G(chi^{-1}) = chi(-1)p^{n+1}).
5. Trivial chi: L_0 · (1 - a_3/3) L(E,1)/Omega_+ = (3/2)(4/3) = 2 = (1 - alpha^{-1}) = SW eps_p. Exact, sign included
   (log c_0 = +3/2: D1.2(v) at n = 0 gives log y_0 = -b·h(zeta_3 - 1) = -b(3/2 - 3) = +(3/2)b).

## The chi ↔ chi^{-1} question (answered)
- Col side: mu ∈ Lambda ↦ (chi ↦ chi(mu)), sigma ↦ chi(sigma); Galois characters are Dirichlet characters via sigma_a ↔ a.
- SW side: Lambda ≅ Z_p[[T]], gamma ↦ 1+T, value at chi is L(zeta - 1) with zeta = chi(gamma); the measure is on Z_p^x via
  kappa. SAME identification. No involution T ↦ (1+T)^{-1} - 1 is needed. [Even if one were, it would preserve ord_T and
  the T^2 coefficient when a_0 = a_1 = 0 (DERIVED: iota(T)^2 = T^2 + O(T^3)), so D8 would be unaffected.]
- Kato's L_{p-adic,alpha} is a function on X(G_inf) evaluated at kappa·chi where Col and SW are evaluated at chi (the
  kappa^1 shift comes from Kato's V(f*)(k) twist in 16.6). R25's "Col(loc z) = L_{3,-1,omega_E,gamma}" must be read
  with this dictionary; D7's comparison with SW is consistent with it.
- C1 (correction, no effect on the bound): R25 (RETURN INPUT 4, D7 item 1) inherits the convention "from Kobayashi's
  printed split identity". Kobayashi's text writes L(E,chi,1) both for the chi^{-1}-weighted exp* sum (l.301–305) and
  in the MTT interpolation (l.321–322). Against Ka 12.5(1) as printed and SW/MTT as printed, BOTH should read
  L(E,chi^{-1},1); the two slips cancel. The identity should be sourced to Ka 12.5(1) + SW §3.2 directly (as above).

## Zariski density
Col(loc z) ∈ Lambda (z integral, T2/T3) and SW's L_alpha ∈ Lambda⊗Q (alpha a unit; bounded denominators, SW Lemma 3.6).
A non-zero element of Lambda⊗Q is p^mu·P·U (Weierstrass), U a unit (no zeros in |T| < 1), so it has finitely many
zeros in the open disc, while {zeta - 1 : zeta ∈ mu_{3^inf}, zeta ≠ 1} is infinite there. "Finitely many zeros" suffices;
the trivial character is not even needed. (Growth-type arguments, Ka 16.3(1), are needed only for unbounded H_h.)
