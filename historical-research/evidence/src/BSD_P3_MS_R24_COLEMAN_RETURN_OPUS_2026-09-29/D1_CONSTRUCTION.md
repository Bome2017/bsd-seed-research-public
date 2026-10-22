# D1 — The twisted Kobayashi family (DERIVED, unaudited). Part 1 of the MS-R24 derivation.

Notation (Kobayashi §2): p odd; k_n = n-th layer of the cyclotomic Z_p-ext. of Q_p, k_n = Q_p(zeta_{p^{n+1}})^Delta,
Gamma_n = Gal(k_n/Q_p), Lambda = Z_p[[Gamma]]; Delta = mu_{p-1} acting on zeta by zeta -> zeta^delta.
S_m := sum_{delta in Delta} (zeta_{p^m}^delta - 1) in k_{m-1}   (m >= 1).   For p = 3: S_m = zeta+zeta^{-1}-2.

## D1.1 The family (alpha a p-adic unit; the seed uses alpha = a_3 = -1, Kobayashi alpha = a_p = +1)
  C_alpha := p(p-1)/(p-alpha),
  L_n^(alpha) := alpha^{-(n+1)} C_alpha + sum_{m=1}^{n+1} alpha^{-m} p^{-(n+1-m)} S_m   in k_n.
Facts used: Tr_{Q_p(zeta_{p^m})/Q_p(zeta_{p^{m-1}})}(zeta_{p^m}^delta - 1) = -p for m >= 2, so
Tr_{k_{m-1}/k_{m-2}} S_m = -p(p-1); S_1 = -1-(p-1) = -p; Tr of an element of k_{n-1} from k_n is p times it.
(a) Tr_{k_n/k_{n-1}} L_n = L_{n-1}  (n >= 1).  Proof: terms m <= n gain a factor p, which matches the
    exponent of L_{n-1}; the m = n+1 term gives -p(p-1)alpha^{-(n+1)}; constants: p*alpha^{-(n+1)}C - p(p-1)
    alpha^{-(n+1)} = alpha^{-n} C  <=>  C(p - alpha) = p(p-1).  QED.
(b) L_0 = alpha^{-1}(C + S_1) = alpha^{-1} p (alpha-1)/(p-alpha) = (1 - alpha^{-1})(1 - alpha/p)^{-1}.
    alpha = +1: L_0 = 0.   alpha = -1: L_0 = 2p/(p+1);  p = 3: L_0 = 3/2, v_3(L_0) = 1.
    [= Claude's factor (1-phi)(1-p^{-1}phi^{-1})^{-1} at phi = alpha^{-1}.]
(c) Gauss sums. chi a character of Gamma_n of conductor p^{n+1} (n >= 1), extended trivially on Delta,
    tau(chi) = sum_{g in G_{n+1}} chi(g) zeta_{p^{n+1}}^g:
      sum_{sigma in Gamma_n} L_n^sigma chi(sigma) = alpha^{-(n+1)} tau(chi).
    Proof: constants and S_m (m <= n, fixed by Gal(k_n/k_{m-1}) on which chi is non-trivial) die;
    sum_sigma S_{n+1}^sigma chi(sigma) = tau(chi) - (p-1) sum chi = tau(chi).  QED.
    Trivial character: sum_sigma L_n^sigma = Tr L_n = L_0.
(d) alpha = +1: L_n^(1) = p + sum_{k=0}^{n} p^{-k} S_{n+1-k} = Kobayashi's log_p(d_n) (Kob l.115) verbatim.

## D1.2 Integral realisation for alpha = -1 (the nonsplit case)
K = Q_{p^2}, O = W(F_{p^2}), phi = Frobenius (phi^2 = 1). K_n = K k_n, phi~ generating Gal(K_n/k_n).
(i) Over K, E is a Tate curve; the Tate isomorphism for E_q (Kob l.211-233) composed with the O-isomorphism
    of minimal models E_q ~ E (quadratic unramified twist, unit u) gives theta: G^_m -> E^ over O with
    theta^phi = theta o [-1] and log_E^ o theta = lambda log(1+X), lambda in O^x, phi(lambda) = -lambda.
    [log normalised by omega_E; the twist cocycle is [-1] because T_pE^ = Z_p(1) (x) eta.]
(ii) Hence E^(m_n) = theta(U^-(K_n)),  U^-(K_n) := {y in U^1(K_n): phi~(y) = y^{-1}},  and
     log_E^(theta(y)) = lambda log y.
(iii) Put b := lambda^{-1} (phi(b) = -b) and, for p = 3 (Delta = {+-1}),
      h(X) := 3/2 + sum_{k>=0} (-1)^k 3^{-k} [(1+X)^{3^k} + (1+X)^{-3^k} - 2]   in Q[[X]],
      G(X) := exp(b h(X)).
    [General p: h = C_{-1} + sum_k (-1)^k p^{-k} sum_delta((1+X)^{p^k delta} - 1).]
    Convergence: the X^j-coefficient of the k-th term is 2 sum_{m even>=2} s(j,m) 3^{k(m-1)}/j!  -> 0.
(iv) CLAIM: G in 1 + (3, X) O[[X]].  Proof in D2 (Dwork's lemma, proved there).
(v) y_n := (phi^{-(n+1)} G)(zeta_{3^{n+1}} - 1) = exp((-1)^{n+1} b h(zeta_{3^{n+1}} - 1)).
    Terms k >= n+1 vanish at zeta_{3^{n+1}}, so h(zeta_{3^{n+1}} - 1) = 3/2 + sum_{k=0}^{n} (-1)^k 3^{-k} S_{n+1-k},
    and log y_n = b L_n^(-1)  (index m = n+1-k).  y_n is Delta-fixed because h((1+X)^{-1}-1) = h(X).
(vi) c_n := theta(y_n) lies in E^(m_n) (phi~ y_n = y_n^{-1} since log is injective on U^1(K_n)) and
     log_E^(c_n) = L_n^(-1).  By (a) and torsion-freeness, (c_n) is norm-compatible: c in lim E^(m_n).
