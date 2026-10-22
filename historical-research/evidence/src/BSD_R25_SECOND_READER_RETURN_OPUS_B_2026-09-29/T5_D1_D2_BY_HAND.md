# T5 (optional) — D1 trace relation and D2 Dwork integrality, by hand.  VERDICT: PASS (two cosmetic slips)

## D1.1(a) trace relation — DERIVED: CORRECT
Gal(k_n/k_{n-1}) = Gal(Q_p(zeta_{p^{n+1}})/Q_p(zeta_{p^n})) by restriction (both of order p). For n >= 1:
- m <= n: S_m lies in k_{m-1} c k_{n-1}, trace p S_m; alpha^{-m} p^{-(n+1-m)} . p = the coefficient of S_m in L_{n-1}.
- m = n+1: zeta_{p^{n+1}}^delta has minimal polynomial x^p - zeta_{p^n}^delta over Q_p(zeta_{p^n}) (n+1 >= 2), trace 0; so
  Tr S_{n+1} = sum_delta (0 - p) = -p(p-1).
- constant: p alpha^{-(n+1)} C - p(p-1) alpha^{-(n+1)} = alpha^{-n} C  <=>  C(p - alpha) = p(p-1). This is the definition of C.
Exact check (checks/ksr12.log): Tr L_1 = L_0, Tr L_2 = L_1 for alpha = -1, +1, 2. (b), (c), (d) re-derived in T1/K-SR1;
(d): at alpha = 1, C = p and L_n^(1) = p + sum_k p^{-k} S_{n+1-k} = Kob l.115 "log_p(d_n) = p + sum_k sum_delta (zeta^delta_{p^{n+1-k}} - 1)/p^k".

## D2.1 Dwork's lemma — DERIVED: CORRECT, one cosmetic slip
Mod X^{n+1} (n >= 1): F^phi(X^p) = F^phi_{<n}(X^p) and F^p = F^p_{<n} + p a_n X^n (F(0) = 1). Comparing X^n-coefficients of
F^phi(X^p) = F^p H gives p a_n H(0) = [F^phi_{<n}(X^p)]_n - [F^p_{<n} H]_n. R25 omits the factor H(0); it lies in 1 + pO,
a unit, so the conclusion a_n in O is unaffected. Both brackets are integral and congruent mod p since
F^phi_{<n}(X^p) = F_{<n}(X)^p = F^p_{<n} H (mod p). Log form: exp(p X O[[X]]) c 1 + p X O[[X]] because
v_3(3^n/n!) = n - v_3(n!) >= (n+1)/2 >= 1. Correct.
## D2.2 change of Frobenius lift — DERIVED: CORRECT ((1/n) C(n,j) p^j = C(n-1,j-1) p^j/j, v >= j - v(j) >= 1).
## D2.3 the Dwork condition for g = b h — DERIVED + COMPUTED: CORRECT
- Closed form (DERIVED, new): with L = log(1+X), (1+X)^n + (1+X)^{-n} - 2 = sum_{m>=1} 2 n^{2m} L^{2m}/(2m)!, and
  sum_k (-1)^k 3^{k(2m-1)} = 1/(1 + 3^{2m-1}), so
      h(X) = 3/2 + sum_{m>=1} 2 L^{2m} / ((2m)! (1 + 3^{2m-1})),    h_1(X) = 3 + sum_{m>=1} 2 L^{2m}/((2m)! (1 - 3^{2m-1})).
  So h does have rational coefficients (D1.2(iii) "in Q[[X]]" is right). Agrees with the defining k-sum to v_3 >= 39 (deg < 8).
- Identity h((1+X)^3 - 1) + 3 h(X) = 6 + 3X^2/(1+X): exact to O(X^32). Hence (Phi - 3)(b h) = -b(6 + 3X^2/(1+X)) in 3O[[X]].
- h' = sum_k (-1)^k (1+X)^{-1}[(1+X)^{3^k} - (1+X)^{-3^k}] converges in Z_3[[X]] (the bracket -> 0), so D2.2 applies.
- Constant term: phi(g_0) - 3 g_0 = -(3/2)b - (9/2)b = -6b; subtracting it gives zero constant term, so g - g_0 meets D2.1's
  log form; exp(g_0) = exp((3/2)b) in 1 + 3O. So G = exp(b h) in (1 + 3O)(1 + X O[[X]]). Correct.
- COMPUTED (checks/dwork_t5.log, exact rationals, degree <= 30): b = i u in Z_9 = Z_3[i] (phi(b) = -b; Frobenius = complex
  conjugation): cos(u(h - 3/2)), sin(u(h - 3/2)) have all coefficients 3-integral for u = 1, 2, 3.
  Controls: split h_1 with b = 1 (Kobayashi's G/(1+X)) integral; NEGATIVE controls h_1 with b = i (cos: v = -6, sin: v = -6)
  and h with b = 1 (exp: v = -6) are NOT integral. The twist (-1)^k and phi(b) = -b are both needed, as D2 claims.
## D1.2(v)-(vi) — DERIVED: CORRECT
Terms k >= n+1 vanish at X = zeta_{3^{n+1}} - 1; with m = n+1-k, (-1)^{n+1} h(zeta - 1) = (-1)^{n+1}(3/2) + sum_m (-1)^m 3^{-(n+1-m)} S_m
= L_n^(-1), so log y_n = b L_n^(-1). phi~(y_n) = y_n^{-1} since phi^j(b) = (-1)^j b; y_n is Delta-fixed since h is symmetric
under (1+X) -> (1+X)^{-1}. The Tate-curve twist theta (D1.2(i)) is SECONDARY (textbook); Steps 1-3 need only log c_n = L_n
and c_n in E^(m_n), and T2(e) shows log c_0 = 3/2 generates independently of theta.
## Slips (cosmetic): (1) D2.1 drops the unit H(0); (2) none else found in D1-D2.
