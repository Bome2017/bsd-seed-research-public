# Two-leg tame experiment — RESUME (Claude Opus 5.5, 2026-10-14)

## Question (shape probe, not a certificate)
At one auxiliary prime the record's tame law holds: c2(l) = K_E*(a_l-2)*R_l (mod odd part of l-1).
Does the derivative structure assemble into ONE quadratic form when two auxiliary primes act together?
At level M = l1*l2 the Mazur-Tate element lives in Z[G1 x G2]. Its I^2/I^3 image has three parts:
  x1^2, x2^2 (FORCED by the distribution relation + the one-prime law: used only to validate code)
  x1*x2      (NEW: not determined by one-prime data) = c11 = sum_a ind1(a)*ind2(a)*[a/M]^+
Prediction (single global form, Mazur-Tate refined shape):
  c11 == K_E*(a_l1-2)*(a_l2-2)*Dmix / (cexp^2*idx_M)^2   (mod q^min(e1,e2))
  Dmix = h1(Q1)h2(Q2) + h2(Q1)h1(Q2) - 2*b1*b2, b_j = (h_j(Q1+Q2)-h_j(Q1)-h_j(Q2))/2,
  Q1,Q2 = LLL basis of L_M = ker(Z^2 -> E(F_l1) x E(F_l2)) on P' = cexp*P, idx_M = [Z^2:L_M].
Analogy: Yun-Zhang's r-th derivative = sum over r-tuples of places ("legs"); here two legs sit at l1, l2.

## Outcomes and what each means (fixed before computing)
- Mixed term matches at every clean row: the tame leading terms at all auxiliary primes and their couplings are values
  of one form K*det(universal tame height). One constant, one class P1^P2, across primes. Tame shadow of reopener 3.
- Mixed term fails while pure terms pass: per-prime laws do NOT assemble; the missing object must carry cross-prime
  data beyond P1^P2. Pre-registered follow-up: tabulate lambda = c11/Dmix (Dmix a unit) against (a1-2),(a2-2),K,
  ind_g1(l2), ind_g2(l1) (arithmetic linking numbers).
- Pure terms fail: code/convention bug (they are forced). Stop and debug; no mixed-term conclusion.

## Endpoint check (written before any computation)
No FIN / ORDER9 / Q36 effect. Control curves only. It decides the SHAPE (single cross-prime form or not).

## Row rule (fixed before any symbol)
Curves: 389a1, 433a1, 664a1, 655a1, 1615a1 (10-07 data; 194040co6 excluded: composite-level symbols too costly).
Pairs l1 < l2 primes, l_i !| N, l2 <= 200; odd q | gcd(l1-1, l2-1) with q <= 13; e = min(v_q(l1-1), v_q(l2-1)).
Row is clean iff q !| cexp*idx_M. Conventions: 10-07 lib_tl.gp (g = least primitive root, full index lift,
[a/M]^+ = kap*mseval(xp,[oo,a/M]), kap from the Birch ratio).

## Steps
1. s1_reg2.gp -> outputs/reg2.txt (heights only, NO symbols)   2. seal.py -> predictions.json + sha256
3. s2_sym2.gp -> outputs/sym2.txt (symbols, c_jk)              4. evaluate.py -> RESULTS.json/md, REPORT.md
