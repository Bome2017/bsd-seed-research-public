# D3 — Kill tests K-R25a and K-R25b (DERIVED; numerics in checks/)

## The Coleman map (both cases). c = (c_n) in lim E^(m_n) with log_E^(c_n) = L_n^(alpha) (D1, D2).
  Col(z) := lim_n sum_{sigma in Gamma_n} (c_n^sigma, z_n)_{E,n} sigma,   z in lim_n H^1(k_n, T*(1))   (Kob l.243-255).
Kob l.266: (x, z)_{E,n} = Tr_{k_n/Q_p}(log_E^(x) exp*_omega(z)) for x in E^(m_n). With Kob's rearrangement
(l.276-284, valid verbatim for any norm-compatible c):
  chi(Col(z)) = [sum_sigma L_n^sigma chi(sigma)] * [sum_sigma exp*_omega(z^sigma) chi(sigma)^{-1}]   (chi of conductor p^{n+1}),
  1(Col(z))  = L_0 * exp*_omega(z_0).
By D1.1(c): chi(Col(z)) = alpha^{-(n+1)} tau(chi) sum_sigma exp*(z^sigma) chi(sigma)^{-1};  1(Col(z)) = L_0 exp*(z_0).

## K-R25a (split sanity, eta = 1, alpha = a_p = +1): PASS
- L_n^(1) = p + sum_{k=0}^n p^{-k} S_{n+1-k} is Kob's log_p(d_n) (l.115) term by term (D1.1(d)).
- Gauss sums: sum log_p(d_n^sigma) chi(sigma) = tau(chi) for chi != 1, and 0 for chi = 1 (Kob l.289-294) —
  reproduced (D1.1(c) with alpha = 1; exact check for n = 1, 2 in checks/coleman_family.log).
- L_0^(1) = 0, i.e. d_0 = 1 (Kob Prop 2.1(i)), hence 1(Col(z)) = 0 for EVERY z: Col(z)(0) = 0 (Kob l.327-329).
  In our language the trivial zero is forced: every norm-compatible system in lim U^1_n has trivial level-0
  component, since the universal norms of k_inf/Q_p inside 1 + pZ_p are trivial (local CFT: the norm group of
  k_n is <p> x mu_{p-1} x (1 + p^{n+1} Z_p)).
- Integral realisation: exp(h_1) in Z_3[[X]] (D2.3; numeric B2), = Kobayashi's G divided by (1+X).
- Then Col(z^Kato) = L_{p,gamma}(E,X) by Kob's argument (l.301-325), unchanged.
- Discrepancy found (NOTES §3, REMARK): Kob's literal d_n equals zeta_{p^{n+1}} d_n'. Harmless.

## K-R25b (trivial character, alpha = a_3 = -1): CONFIRMED, exactly (not only up to units)
Inputs read at source:
- Ka Thm 12.5(1) (rendered p.221): for chi: G_n -> C^x and r = 1, k = 2, the image of z_gamma under exp* and
  x (x) y -> sum_sigma chi(sigma) sigma(y) per_f(x)^+- is L_{p}(f*, chi, 1) gamma^+-, +- = chi(-1).
- Ka 6.2 (l.2409-2438): L_S(f, chi, s) = sum_{(n,S)=1} a_n chi(n) n^{-s} = prod_{l not in S}(...), and eps(l) = 0
  for l | N. So only the Euler factor at p is removed; for chi = 1, L_{p}(E,1) = (1 - a_p/p) L(E,1).
- Ka 16.1-16.2(ii) (rendered pp.268-269): 16.1 needs (1 - alpha u) | 1 - a_p u + eps(p) p u^2, ord_p(alpha) < 1;
  for p | N this is alpha = a_p = -1 (allowed). 16.2(ii) at k = 2, r = 1, eps(p) = 0:
  L_{p-adic,alpha}(kappa) = (1/Omega_+)(1 - alpha^{-1}) L(E,1) = 2 L(E,1)/Omega_+.
Computation: 1(Col(z_gamma)) = L_0 * exp*(z_0) = (2p/(p+1)) * (1 + 1/p) L(E,1)/Omega_+ = 2 L(E,1)/Omega_+.
At p = 3: (3/2)(4/3) = 2 = 1 - alpha^{-1}. Claude's pre-computation is right, and the "Coleman factor" is exactly
L_0 = log_E^(c_0) = 3/2: it is the level-0 value of the twisted family, with v_3 = 1 cancelling v_3(4/3) = -1.
Independent confirmation AT SOURCE: Ka Thm 16.4(ii) (Perrin-Riou; rendered p.270) gives, for eta = (1 - p^{-r}phi)eta',
L_eta(x)(kappa^r) = (r-1)! <exp*(x_{-r,0}), (1 - p^{r-1}phi^{-1}) eta'>. At r = 1 and phi(eta) = alpha eta this is
(1 - alpha^{-1})(1 - alpha/p)^{-1} <exp*(x_0), eta> = L_0 * <exp*(x_0), eta>: the same factor 3/2 as D1.1(b).
Ka 16.4(i) likewise carries alpha^{-n} at conductor p^n, matching D1.1(c). (Applied to the crystalline 1-dim quotient;
for the 2-dim semistable V see the KKT caveat in D5. Nothing in D1-D3 depends on 16.4.)
REMARK (good ordinary sanity, algebra only): with L_{p}(E,1) = (1 - alpha/p)(1 - alpha^{-1}) L(E,1) and the
factor L_0 = (1 - alpha^{-1})(1 - alpha/p)^{-1}, the product is (1 - alpha^{-1})^2 L(E,1) = Ka 16.2(ii), eps(p) = 1.
Numerics (Sage 3-adic L-series, modular symbols; checks/kr25c.log): constant term = 2 * L(E,1)/Omega_E on every
nonsplit test curve (Omega_E / Omega_+ in {1, 2}, a 3-adic unit); 0 on split curves (21a1, 51a1).
