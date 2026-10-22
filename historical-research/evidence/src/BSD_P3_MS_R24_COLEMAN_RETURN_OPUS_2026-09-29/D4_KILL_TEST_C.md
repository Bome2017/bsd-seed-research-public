# D4 — Kill test K-R25c (numerical bookkeeping): PASS  (checks/kr25c.sage, kr25c.log, cands.txt)

## Data
Cremona curvedata (fields 1, 29, 36, 39, 45, a-invariants field 11), optimal curves ("...1"), 3 || N, a_3 = -1
(nonsplit at 3), rank 0: all 264 with N < 1200, plus the first 25 with 9 | sha_an (N < 10000). Rank 1: 12 curves.
Sage 10.x (run040 env), 1 process, 48 s CPU in total.

## What is compared (rank 0)
- A = v_3(constant term of Sage's 3-adic L-series, series(4)): modular symbols, MTT measure with alpha = a_3 = -1.
- B = v_3(2 L(E,1)/Omega_E) from the exact L_ratio.   [Omega_E/Omega_+ in {1,2}: a unit at 3.]
- C = v_3(sha_an) + sum_l v_3(c_l) - 2 v_3(#E(Q)_tors): v_3 of char(Sel^vee(E/Q_inf))(0) predicted by the
  Euler-characteristic formula for the CLASSICAL (primitive) Selmer group at nonsplit p (no p-local factor:
  c_3 in {1,2}, E(Q_3)[3] = 0 because E~_ns(F_3) has order 4).
- Route K (O2 as derived in D6): char(Sel^vee) | L_3  ==>  C <= A.
- NC1 (negative control): an extra Euler factor on the Selmer side, C + sum_{l mult, l != 3} v_3(1 - a_l/l).
- NC2 (negative control): the wrong local term #E(Q_l)[3^inf] at nonsplit l, C + sum v_3(l+1).

## Results
| set | curves | C <= A | C = A | A = B | of which ns2 | NC1 caught (ns2) | NC2 caught (ns2) |
|---|---|---|---|---|---|---|---|
| all rank 0 (264 with N < 1200 + 25 sha-set) | 289 | 289 | 289 | 289 | 126 | 126/126 | 126/126 |
| subset 9 \| sha_an (25 sha-set + 681b1) | 26 | 26 | 26 | 26 | 14 | 14/14 | 14/14 |
- ns2 = a nonsplit prime l = 2 (mod 3), l || N (3 | l+1, like 5843). Also sp1 = split l = 1 (mod 3): 73 curves,
  NC1 caught on 73/73. 52 curves have A >= 1; 5073d1, 5655d1, 5862h1, 7359b1 have A = C = 3.
- No off-by-one on the ns2 curves: the local term that enters is the Tamagawa 3-part (here 1), not 1 + l^{-1}
  and not #E(Q_l)[3^inf] (= 3 at such l).

## What this test can and cannot see (stated plainly)
- For rank 0, C = A is FORCED by the definition of sha_an (L(E,1)/Omega = sha_an prod c / tors^2). So the test
  checks the SHAPE of the bookkeeping, not BSD: (i) A = B confirms independently that MTT's L_3(0) = 2 L/Omega at
  nonsplit 3 (K-R25b numerically); (ii) the Euler-characteristic local terms are the Tamagawa 3-parts;
  (iii) a stray factor on the SELMER side (NC1, NC2) violates C <= A on every flagged curve, so it is caught.
- A stray factor on the L SIDE (char | L_3 (1 + l^{-1})) would still satisfy C <= A. No numerical test of this
  kind can catch it. It is excluded only by the derivation (D6: Kato's L_{p} keeps the Euler factors at l | N,
  Ka 6.2; Kato's H^2 uses j_*, Ka 8.2).

## Rank 1: NOT RUN (not cheap)
Sage: "the p-adic regulator is not implemented for non-split multiplicative" reduction. Raw data only (no test
claim): L_3(0) = 0 and v_3(L_3'(0)) = 0 on all 12 curves; 156a1 has C = 1, so route K + Jones would force
v_3(Reg_gamma) <= -1 there. This is a WARNING for O5: normalized 3-adic regulators can have negative valuation.
