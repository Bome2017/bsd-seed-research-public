# D2 — Integrality of G = exp(b h) (DERIVED, unaudited). Part 2 of the MS-R24 derivation.

## D2.1 Dwork's lemma (the direction used; proof included so no citation is needed)
O = W(k), K = Frac O, phi = Frobenius (phi(a) = a^p mod p). Let F in 1 + X K[[X]] with
F^phi(X^p) = F(X)^p H(X), H in 1 + p O[[X]]. Then F in 1 + X O[[X]].
Proof. Induction on n: suppose a_0..a_{n-1} in O, F_{<n} := sum_{i<n} a_i X^i. Mod X^{n+1}:
F^phi(X^p) == F_{<n}^phi(X^p) (n >= 1) and F^p == F_{<n}^p + p a_n X^n. Comparing X^n-coefficients,
p a_n = [F_{<n}^phi(X^p)]_n - [F_{<n}^p H]_n. Both brackets are integral and congruent mod p, because
F_{<n}^phi(X^p) == F_{<n}(X)^p == F_{<n}^p H (mod p). So a_n in O.  QED.
Log form: g in X K[[X]] with g^phi(X^p) - p g(X) in p X O[[X]]  ==>  exp(g) in 1 + X O[[X]]
(since exp(p X O[[X]]) is in 1 + p X O[[X]] for p odd: v_p(p^n/n!) >= 1 for n >= 1).

## D2.2 Switching the Frobenius lift
Lemma. If f in X K[[X]] has f' in O[[X]], and Y, Z in X O[[X]] with Y == Z (mod p), then f(Y) - f(Z) in p O[[X]].
Proof. f = sum (c_{n-1}/n) X^n, c in O; Y^n - Z^n = sum_{j>=1} C(n,j) p^j W^j Z^{n-j} (Y = Z + pW) and
(1/n) C(n,j) p^j = C(n-1,j-1) p^j / j has v_p >= j - v_p(j) >= 1.  QED.
Apply with Y = (1+X)^p - 1, Z = X^p.

## D2.3 The Dwork condition for g := b h (p = 3; general p identical with sum over Delta)
Write Phi(f)(X) := f^phi((1+X)^3 - 1). Since h has rational coefficients and phi(b) = -b:
  Phi(b h) = -b h((1+X)^3 - 1),
  h((1+X)^3 - 1) = 3/2 + sum_{k>=0} (-1)^k 3^{-k}[(1+X)^{3^{k+1}} + (1+X)^{-3^{k+1}} - 2]
                 = 3/2 - 3 [h(X) - 3/2 - X^2/(1+X)]          (reindex j = k+1; k = 0 term of h is X^2/(1+X)).
  So (Phi - 3)(b h) = -b [h((1+X)^3-1) + 3 h(X)] = -b [6 + 3 X^2/(1+X)]  in 3 O[[X]].
h' = sum_k (-1)^k [(1+X)^{3^k-1} - (1+X)^{-3^k-1}] converges in Z_3[[X]] (the bracket -> 0 as k -> oo), so
h' is integral and D2.2 turns this into (b h)^phi(X^3) - 3 b h(X) in 3 O[[X]].
Constant term: g_0 = (3/2) b in 3 O. So g - g_0 satisfies D2.1 (constant parts: phi(g_0) - 3 g_0 = -6b in 3O),
exp(g - g_0) in 1 + X O[[X]], exp(g_0) in 1 + 3 O. Hence G = exp(b h) in (1 + 3O)(1 + X O[[X]]).  QED (D1.2(iv)).
Split sanity: b = 1 and h_1 := 3 + sum_k 3^{-k}[(1+X)^{3^k} + (1+X)^{-3^k} - 2] give (Phi - 3) h_1 =
-3 X^2/(1+X) - 6, so exp(h_1) in Z_3[[X]]: this is Kobayashi's G up to the factor (1+X) (NOTES §3).

## D2.4 Evaluation (the step Kobayashi also takes, l.115)
For |x| < 1: G(x) converges (integral coefficients). log G = g as power series and the partial sums of
log(1 + (G-1)) converge uniformly on {|X| <= r} (|G - 1| <= max(|3|, r) < 1 there), so log G(x) = g(x).
Termwise evaluation of the k-sum of h on {|X| <= r}: for k >= k_0(r), (1+X)^{3^k} = exp(3^k log(1+X)) and the
k-th term is 3^{-k} sum_{i>=2 even} 2 (3^k L)^i / i!, L = log(1+X) bounded there; this -> 0 uniformly.

## D2.5 Consequences (with D1)
- y_n in U^1(K_n) exist with log y_n = b L_n^(-1); c_n = theta(y_n) in E^(m_n); log_E^(c_n) = L_n^(-1).
- c = (c_n) in lim_n E^(m_n), log_E^(c_0) = 3/2.
Numerical cross-check of D2.3 (coefficients of cos(h), sin(h) 3-integral to degree 40): checks/coleman_family.gp.
