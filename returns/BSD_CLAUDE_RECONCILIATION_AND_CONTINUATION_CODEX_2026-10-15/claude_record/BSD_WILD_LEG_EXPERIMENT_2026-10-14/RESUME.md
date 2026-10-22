# Wild-leg experiment — RESUME (Claude Opus 5.5, 2026-10-14)

## Question
The two-leg experiment showed tame legs at two primes form ONE quadratic form. Does the p-adic (wild) direction join
the same form? Wild direction = W = (1+pZ)/(1+p^2 Z) = Z/p inside (Z/p^2)^x, generator 1+p,
phi(u) = -((u^(p-1) - 1)/p) mod p (so phi(1+p) = 1).
Wild height (same recipe as the tame one, mapped to W): w(Q) = phi(-a/b mod p^2), Q = (a/d^2, b/d^3), Q = O mod p.
Valid mod p^2 only when sigma(t)/t = 1 mod p^2 for t in pZ_p: needs a1 = 0 (the sigma t^2-term is a1/2).
Curves: 389a1 (K 8), 664a1 (K 16), 655a1 (K 8). Primes p in {5,7,11,13}, p !| N, ordinary, non-anomalous.

## Tests (candidates fixed before any symbol; the data choose, a candidate counts only if it fits EVERY clean row)
A. pure wild, level p^2: c2w = sum_a C(phi(a),2)[a/p^2]^+ == F*K*det(Hw)/(cexp^2 idx_p)^2 (mod p),
   F in {a_p-1 (= -#E(F_p) mod p, the tame-leg analogue), a_p-2, 1, 1-a_p, a_p}.
B. wild x tame, level l*p^2 (p | l-1, l <= 400): c11 = sum ind_l(a) phi(a) [a/(l p^2)]^+ ==
   s*F*(a_l-2)*K*(h_l(Q1)w(Q2) + w(Q1)h_l(Q2) - 2 b_l b_w)/(cexp^2 idx)^2 (mod p), s in {+1,-1}.
   Consistency (forced): wild-squared coefficient at level l*p^2 == (a_l-2)*c2w(p^2) (mod p).
Outcomes: one F (and one s) fits all rows => the p-adic class at p is the same form as the tame classes; none fits =>
the wild direction carries a different local structure (then report the observed ratios, no fitting beyond the list).
Endpoint: none (control curves; shape only).

## Row-rule amendment (before any symbol; first step-1 pass gave only 10 pure-wild rows)
p in {5,...,31} (primes), same filters; l <= 400 with l = 1 mod p. Step 1 re-run; earlier output overwritten.
