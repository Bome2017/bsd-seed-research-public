# FG proxy (mock plectic scalar, k = 1) — predictions SEALED before any Gross-point sum was computed
Law tested (FG Conj. 2.16 shape + Lemma 3.12/Thm 3.16): D_{l,K} = u_l * c_K * det_l (mod p), u_l an unknown unit
(per l), c_K the mock plectic scalar, det_l = dlog_l(P) rho(Q) - dlog_l(Q) rho(P) from Cremona generators
(global_side.out; det is K-independent). Hypotheses: H_unit (c_K a p-unit; = "c proportional to K_E" here since
p !| K_E in every row) predicts D = 0 iff det = 0. H_zero (c_K = 0 mod p) predicts D = 0 always.
Every row: S0 = sum_sigma f(x_sigma) = 0 mod p (zero at the trivial character).

| curve | p | l | fields D | det_l | H_unit predicts | H_zero predicts |
|---|---|---|---|---|---|---|
| 655a1 | 5 | 2 | -67, -163 | 2 | D != 0 | D = 0 |
| 655a1 | 5 | 17 | -163 | 4 | D != 0 | D = 0 |
| 655a1 | 5 | 23 | -8, -163 | 0 | D = 0 | D = 0 |
| 655a1 | 5 | 47 | -8 | 2 | D != 0 | D = 0 |
| 655a1 | 5 | 53 | -8, -67 | 4 | D != 0 | D = 0 |
| 1001c1 | 7 | 3 | -43, -79 | 6 | D != 0 | D = 0 |
| 1001c1 | 7 | 47 | -51, -79, -95 | 1 | D != 0 | D = 0 |
| 1001c1 | 7 | 73 | -43 | 0 | D = 0 | D = 0 |
| 1001c1 | 13 | 17 | -24, -164, -167 | 0 | D = 0 | D = 0 |
| 1001c1 | 13 | 149 | -83, -164, -167 | 1 | D != 0 | D = 0 |

Two-prime check (1001c1): the same global P^Q must explain the pattern at p = 7 and at p = 13, and v_p(c) = 0 = v_p(K_E=48)
at both (rows with det != 0).

Exploratory (not a pass/fail law; u_l cancels across fields sharing l): (c_K1/c_K2)^2 = (D_1/D_2)^2 * (d_1/d_2) mod p
(canonical sqrt-coordinate normalization). Candidates fixed now: (a) 1; (b) r_1/r_2, r = L(E^D,1)/Omega(E^D);
(c) s_1/s_2, s = L(E^D,1) sqrt|D|/Omega^-(E); each also times (h_1/h_2)^(+-2). Values: twist_values.txt
(655a1: r(-8)=2, r(-67)=144, r(-163)=576; 1001c1: r(-43)=216, r(-24)=12, all others 24; s equal except s(-8)=4, s(-24)=24).
