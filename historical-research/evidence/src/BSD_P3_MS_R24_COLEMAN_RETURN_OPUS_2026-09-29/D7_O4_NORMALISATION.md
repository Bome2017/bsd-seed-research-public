# D7 — O4: the certificate's L_3 versus L_{3-adic,alpha,omega_E,gamma+} (DERIVED; UNAUDITED)

Claim: L_3^cert = u * L_{3-adic, -1, omega_E, gamma}(E) with u in Z_3^x, up to the change of variable
T -> (1+T)^v - 1 (v in Z_3^x) coming from the choice of topological generator of Gamma.

## The certificate's convention (SW 2013, read at source, SW l.290-521)
- [r]^+ = lambda^+(r)/Omega_E with lambda^+ built from the newform f (SW l.290-297); Omega_E = the Neron real period
  (= 2 x integral over gamma^+ of omega_E when E(R) has two components, SW l.292-293).
- Multiplicative p: alpha = a_p, mu_alpha(a + p^k Z_p) = alpha^{-k} [a/p^k]^+ (SW l.309-319); L_alpha(E,T) as in (3.1)
  with T = kappa(gamma)^{s-1} - 1 (SW l.338-357); interpolation: L_alpha(E,0) = eps_p L(E,1)/Omega_E, eps_p = 1 - 1/alpha
  = 2 at nonsplit p (SW l.499-510); nontrivial chi: alpha^{-(n+1)} p^{n+1}/G(chi^{-1}) L(E,chi^{-1},1)/Omega_E (SW l.517-521).
- The S.3 certificate: a_{4,2} = 15480 in the omega_1 normalisation, 7740 in the Neron one (S3_GOVERNING_RECORD);
  the ratio 2 = Omega_E/omega_1 (Delta_seed > 0, two real components). v_3 = 2 either way.

## Comparison with Kato's L_{p-adic,alpha,omega,gamma} (Ka 16.2)
Both are characterised by their values at finite-order characters (Ka 16.3(1); Kob l.324). Term by term:
1. alpha^{-(conductor exponent)} and the Gauss sum: identical (Ka 16.2(i) vs SW l.517-521, with chi <-> chi^{-1} being
   the standard identification of Lambda with measures; Kobayashi's printed split-case identity Col(z) = L_{p,gamma}
   uses the same identification, and the twist by eta changes both sides by the same alpha^{-(n+1)}, D1.1(c)).
2. Trivial character: (1 - alpha^{-1}) in both (Ka 16.2(ii) with eps(p) = 0; SW eps_p = 2).
3. Periods: Kato divides by Omega_+(omega) := the gamma^+-coordinate of per(omega). For omega = omega_E and gamma^+ a
   generator of H_1(E,Z)^+ (x) Z_3 = T^+ ("good gamma", Ka 14.18), Omega_+ = integral of omega_E over gamma^+, which is
   Omega_E or Omega_E/2: ratio a 3-adic unit.
4. f versus omega_E: SW's symbols use f, and pi^*(omega_E) = c_pi f (Cesnavicius (2.11 proof)). So
   L_alpha^SW = c^{+-1} * (unit) * L_{alpha,omega_E,gamma}. Manin constant: Cesnavicius, arXiv:1703.02951, Thm 1.2 /
   Thm 2.11 (read at source, l.60-63, l.385-386): "ord_p(c_pi) = 0 for every prime p such that p^2 does not divide n"
   for a new elliptic optimal quotient. N_seed = 2^3 * 3 * 2243 * 4547^2 * 5843 has 3 || N, so 3 does not divide c for
   the optimal curve; the seed's class is {E, E'} (one 2-isogeny), so for either member c changes by a power of 2 only.
   Grade: THEOREM (preprint copy of Compositio 154 (2018)); sha256 recorded in sources/SOURCES.sha256.
5. Generator of Gamma: SW's T uses kappa(gamma) (any generator, e.g. 4); a change of generator is the Lambda-automorphism
   T -> (1+T)^v - 1, v in Z_3^x. It preserves divisibility in Lambda, ord_T, and multiplies the T^2 coefficient
   of a series with ord_T = 2 by v^2 (a unit).
6. The involution chi -> chi^{-1} (if a source uses the other identification): L(T) -> L((1+T)^{-1} - 1) keeps
   divisibility up to applying it to both sides, and keeps the leading T^2 coefficient when a_0 = a_1 = 0.

## Conclusion
O4 holds: v_3 of every coefficient comparison used downstream is unchanged; in particular v_3(a_2(L_3)) = 2 for
L_{3-adic,-1,omega_E,gamma} as for the certificate. Only unit factors (2, c^{+-1} with 3 not dividing c, v^2, signs) occur.
Grades: SW defs and Ka 16.2-16.3 THEOREM at source; Manin constant THEOREM at source (preprint of published paper);
the certificate value a_{4,2} is an INPUT (S.3, PROVED_COMPUTER_ASSISTED per its record), not re-derived here.
