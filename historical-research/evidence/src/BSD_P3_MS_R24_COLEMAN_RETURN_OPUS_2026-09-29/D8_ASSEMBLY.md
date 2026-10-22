# D8 — Assembly: T-INT ==> #Sha(E/Q)[3^inf] <= 9 ==> Sha[3^inf] = (Z/3)^2  (UNAUDITED)

Notation: f_E := char_Lambda(Sel_{3^inf}(E/Q_inf)^v) (classical Selmer, Delta-trivial branch), L_3 := L_{3,-1,omega_E,gamma+}.

| # | step | source | grade |
|---|---|---|---|
| 1 | T-INT: f_E divides L_3 in Lambda | D6 (Ka 17.13 template) + D5 (MS-R24) + O1 (Ka 12.5(4)) | DERIVED from THEOREMs |
| 2 | L_3 and the certificate's series agree up to Z_3^x and T -> (1+T)^v - 1 | D7 (O4) | DERIVED; Manin const. THEOREM |
| 3 | a_2(L_3) != 0, v_3(a_2) = 2; a_0 = 2L(E,1)/Omega_+ = 0 | S.3 certificate (a_{4,2} = 15480) | INPUT (PROVED_COMPUTER_ASSISTED per S.3) |
| 4 | ord_T f_E >= 2 | below | DERIVED (elementary) |
| 5 | L_3 = T^2 h, f_E = T^2 g, g divides h, v_3(g(0)) <= 2, ord_T f_E = 2 | below | DERIVED |
| 6 | g(0) = unit * #Sha[3^inf] * prod c_l^(3) * Reg_gamma / #E(Q)[3^inf]^2 | Jones 1989 Thm 3.1 (forward), S.3 import | INPUT (not re-read here) |
| 7 | v_3(Reg_gamma) = 0 (the independent height certificate) | B1/S.3 | INPUT — see WARNING |
| 8 | #Sha[3^inf] <= 9 | 5 + 6 + 7; prod c_l = 16, E(Q)_tors = Z/2 (no 3) | DERIVED |
| 9 | Sha[3^inf] = (Z/3)^2 | 8 + B2 (Sha[3] contains (Z/3)^2, CERTIFIED) | DERIVED |

Step 4: control. Sel(E/Q) -> Sel(E/Q_inf)^Gamma has finite kernel (kernel in H^1(Gamma, E(Q_inf)[3^inf]) = 0, since
E(Q(mu_3^inf))[3] = 0 by (12.5.2)). So corank Sel(E/Q_inf)^Gamma >= rank E(Q) = 2, i.e. rank_{Z_3}(X/TX) >= 2, and for a
torsion Lambda-module rank_{Z_3}(X/TX) <= ord_T char(X). (Finiteness of Sha[3^inf] would also follow from ord_T f_E = 2.)
Step 5: T^2 | f_E | L_3 forces a_1 = 0 as well; h(0) = a_2; g | h gives g(0) | h(0) in Z_3; h(0) != 0 gives g(0) != 0.
Step 9: B2 gives #Sha[3] >= 9; with #Sha[3^inf] <= 9 this forces Sha[3^inf] = Sha[3] = (Z/3)^2. Cassels-Tate is
then not even needed; it is the fallback if step 7 only gives v_3(Reg_gamma) = -1 (then #Sha[3^inf] <= 27, and an
order that is a square (finite Sha, Cassels-Tate) and >= 9 is 9).

WARNING on step 7 (from K-R25c rank-1 data): normalized 3-adic regulators can have NEGATIVE valuation (156a1 needs
v_3(Reg_gamma) <= -1 under route K). The chain needs v_3(Reg_gamma) >= -1 in the normalisation of Jones Thm 3.1 that
matches L_3's variable T. S.3's own deduction (#Sha = 9 from v_3(a_2) = 2 under equality) implies v_3(Reg_gamma) = 0;
the checker should confirm this from the height certificate itself. Not computed here (no seed runs).

What route K does NOT use: Skinner 2016, Skinner-Urban, any Hida family, GRH, the B3 pairing computation.
What it uses: Kato 2004 (12.4, 12.5, 14.9, 16.2-16.6, 17.10, 17.12, 17.13 template), Kobayashi 2006 (mechanics),
SW 2013 (definitions), Cesnavicius 2018 (Manin constant), Jones 1989 Thm 3.1 (forward), the S.3 certificate a_{4,2},
the height certificate, B2, and textbook local duality.
