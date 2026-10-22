# T5 — D1.1(a),(b) trace relation and D2 (Dwork) by hand.   VERDICT: PASS

## D1.1(a) Tr_{k_n/k_{n-1}} L_n = L_{n-1} (DERIVED by hand; exact PARI check n = 1, 2 in checks/ksr.log)
- Tr_{Q_p(zeta_{p^m})/Q_p(zeta_{p^{m-1}})} zeta_{p^m}^δ = 0 for m ≥ 2 (minimal polynomial X^p - zeta_{p^{m-1}}^δ), so the trace of
  zeta^δ - 1 is -p. Restriction identifies Gal(Q_p(zeta_{p^m})/Q_p(zeta_{p^{m-1}})) with Gal(k_{m-1}/k_{m-2}); summing over the
  p-1 values of δ: Tr S_m = -p(p-1). S_1 = (-1) - (p-1) = -p. Elements of k_{n-1} have trace p·(itself).
- L_n = alpha^{-(n+1)} C + sum_{m=1}^{n+1} alpha^{-m} p^{-(n+1-m)} S_m. Terms m ≤ n: factor p turns p^{-(n+1-m)} into p^{-(n-m)},
  the m-term of L_{n-1}. Term m = n+1 (n ≥ 1): alpha^{-(n+1)}(-p(p-1)). Constant: p alpha^{-(n+1)} C. Need
  p alpha^{-(n+1)}C - p(p-1) alpha^{-(n+1)} = alpha^{-n} C  ⟺  C(p - alpha) = p(p-1). R25's C_alpha = p(p-1)/(p-alpha). CONFIRMED.
## D1.1(b) L_0 = alpha^{-1}(C + S_1) = alpha^{-1}(C - p) = alpha^{-1} p(alpha-1)/(p-alpha) = (1 - alpha^{-1})(1 - alpha/p)^{-1}.
  alpha = -1, p = 3: 3/2. CONFIRMED (and K-SR1).
## D2.1 Dwork's lemma (DERIVED; R25's proof checked line by line)
F ∈ 1 + X K[[X]], F^φ(X^p) = F(X)^p H(X), H ∈ 1 + pO[[X]]. F(0) = 1 forces H(0) = 1 (R25 uses this silently; it holds).
Induction: mod X^{n+1}, F^φ(X^p) ≡ F_{<n}^φ(X^p) (np ≥ n+1) and F^p ≡ F_{<n}^p + p a_n X^n (F_{<n} ≡ 1 mod X, binomial terms of
order ≥ 2 in a_n X^n vanish); so p a_n = [F_{<n}^φ(X^p)]_n - [F_{<n}^p H]_n. Both are in O and congruent mod p since
G^φ(X^p) ≡ G(X)^p (mod p) for G ∈ O[[X]] and H ≡ 1 (mod p). Hence a_n ∈ O. QED.
Log form: exp(pX O[[X]]) ⊂ 1 + pX O[[X]] for p odd (v_p(p^n/n!) ≥ n - (n-1)/(p-1) ≥ 1). CONFIRMED.
## D2.2 (Frobenius-lift switch): (1/n) C(n,j) p^j = C(n-1,j-1) p^j/j, v_p ≥ j - v_p(j) ≥ 1. CONFIRMED.
## D2.3 (the Dwork condition for g = b h, p = 3)
- Reindexing k → j = k+1: h((1+X)^3 - 1) = 3/2 - 3[h(X) - 3/2 - X^2/(1+X)] = 6 - 3h + 3X^2/(1+X)
  (the k = 0 bracket of h is (1+X) + (1+X)^{-1} - 2 = X^2/(1+X)). PARI (checks/dwork.log): residual has v_3 ≥ 43 to X^30 with
  the k-sum cut at K = 45 (truncation error only).
- φ(b) = -b: (Φ - 3)(b h) = -b h((1+X)^3-1) - 3bh = -6b - 3b X^2/(1+X) ∈ 3O[[X]]. With g_0 = (3/2)b: φ(g_0) - 3g_0 = -6b, so
  (Φ - 3)(g - g_0) = -3b X^2/(1+X) ∈ 3X O[[X]]. h' = sum_k (-1)^k[(1+X)^{3^k-1} - (1+X)^{-3^k-1}] converges in Z_3[[X]]
  (v_3 C(3^k, i) = k - v_3(i) → ∞), so D2.2 moves Φ to X ↦ X^3 at the cost of 3O[[X]] (no constant term): D2.1 applies.
  G = exp(g_0)·exp(g - g_0) ∈ (1 + 3O)(1 + X O[[X]]). CONFIRMED.
- Independent numeric replay (checks/dwork.gp, b = i, Z_9 = Z_3[i], φ(i) = -i): exp(i(h - 3/2)) = cos + i sin has all
  coefficients 3-integral to X^30 (min v_3 = 0 / 0); control b = 1: min v_3 = -6 (not integral), as expected.
## D1.2 (v),(vi) (checked in T2(e)): y_n is Δ-fixed (h((1+X)^{-1}-1) = h(X)), φ̃ y_n = y_n^{-1}, log y_n = b L_n^(-1); log is
injective on U^1(K_n) because no non-trivial 3-power root of unity in Q_9(zeta_{3^{n+1}}) is Δ-fixed; so c_n = θ(y_n) is
norm-compatible in Ê(m_n) with log c_n = L_n^(-1).
