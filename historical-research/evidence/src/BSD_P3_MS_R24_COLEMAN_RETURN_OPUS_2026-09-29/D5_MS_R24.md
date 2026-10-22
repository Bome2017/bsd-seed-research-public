# D5 — MS-R24: statement and proof (DERIVED from printed inputs; UNAUDITED)

## Statement proved
T = T_3E, T^0 = T_3E^ = Z_3(1)(x)eta, T/T^0 = Z_3(eta), eta unramified quadratic. Lambda = Z_3[[Gamma]] (the
Delta-trivial branch; Kobayashi's k_n tower). There is a Lambda-linear Col : H^1_Iw(Q_3,T)/H^1_Iw(Q_3,T^0) -> Lambda
which is an ISOMORPHISM (injective, cokernel 0), and Col(loc_3 z_gamma) = L_{3-adic,alpha,omega_E,gamma}(E) EXACTLY,
alpha = a_3 = -1, gamma in T with gamma^+ a Z_3-basis of T^+ (Kato's "good" gamma), omega_E the Neron differential.

## Step 1. Local structure (DERIVED; standard inputs SECONDARY: Tate local duality and Euler characteristic)
(a) H^2_Iw(Q_3,T^0) = H^0(Q_3(mu_3^inf), Q_3/Z_3(eta))^v (Ka l.5650-5655 duality) = 0: eta is non-trivial on
    G_{Q_3(mu_3^inf)} (totally ramified tower), so eta(g) x = x forces 2x = 0. Same for T/T^0 and for every k_n.
(b) Hence H^1_Iw(T)/H^1_Iw(T^0) = H^1_Iw(Q_3, Z_3(eta)).  For every n: H^0(k_n,T^0) = H^2(k_n,T^0) = 0, H^1(k_n,T^0)
    is Z_3-free of rank 3^n (torsion = H^0(k_n, mu_3^inf (x) eta) = 0); likewise for Z_3(eta); so the Tate pairing
    H^1(k_n,T^0) x H^1(k_n,T/T^0) -> Z_3 is perfect.
(c) Kummer: E^(m_n) = H^1(k_n,T^0) (injective; ranks equal; cokernel = a Tate module of rank 0, hence 0).
(d) Norms E^(m_n) -> E^(m_{n'}) are onto (the obstruction lies in H^2(k_{n'}, T^0 (x) I) = 0 by (a)); so E^(m_n) is
    cohomologically trivial over every subgroup of Gamma_n and Z_3-free, hence Z_3[Gamma_n]-free of rank 1
    (Nakayama-Rim; SECONDARY, Serre Local Fields IX.5), and c_n generates it iff its norm c_0 generates E^(3Z_3).
(e) D1/D2: log_E^(c_0) = L_0 = 3/2, so c_0 generates E^(3Z_3) = 3Z_3 (log is an isomorphism, p odd). So every c_n
    generates, {c_n^sigma} is a Z_3-basis of H^1(k_n,T^0), and by (b) Col_n : H^1(k_n,T/T^0) -> Z_3[Gamma_n] is an
    isomorphism; in the limit Col is an isomorphism onto Lambda.
Cross-check at source: Ka Lemma 17.12 (rendered p.277; a purely local statement: T invertible, unramified,
H^0(Q_p,T) = 0) gives an injection with FINITE cokernel for the Perrin-Riou map of such T. Ours is sharper (cokernel 0).

## Step 2. Interpolation (THEOREM inputs + D1)
Kob l.266 and l.276-298 (rearrangement, valid for any norm-compatible c): chi(Col z) = [sum L_n^sigma chi(sigma)] *
[sum exp*_{omega_E}(z^sigma) chi(sigma)^{-1}]. D1.1(c): the first bracket is alpha^{-(n+1)} tau(chi); at chi = 1 the
value is L_0 exp*(z_0), L_0 = (1-alpha^{-1})(1-alpha/p)^{-1} = 3/2.
These are exactly Perrin-Riou's factors in Ka Thm 16.4(i)(ii) (alpha^{-n} at conductor p^n; (1-p^{r-1}phi^{-1})
(1-p^{-r}phi)^{-1} at r = 1). So Col = L_eta of Ka 16.4 for the eta with phi(eta) = alpha eta, <omega_E, eta> = 1,
restricted to the quotient (for multiplicative p, D_cris(V*) is the line of the dual of the unramified quotient).

## Step 3. Col(loc z_gamma) = L_3 exactly
- Ka Thm 16.6 (rendered p.271-272): for alpha, omega, gamma as in 16.2 — 16.1 only asks (1 - alpha u) | 1 - a_p u
  + eps(p)p u^2 and ord_p alpha < 1, which HOLDS at p | N with alpha = a_p = -1 — L_{p-adic,alpha,omega,gamma}(f) =
  L_eta(z_gamma^(p)(f*)(k)). Read at source; no p-not-dividing-N hypothesis in 16.1-16.6. CAVEAT: Ka Remark 16.5(2)
  says Perrin-Riou's 16.4 for NON-crystalline V (our semistable V) was "checked" in [KKT], an unpublished preprint.
  So this route is a CROSS-CHECK only (grade: printed, with internal provenance through unpublished KKT).
- PRIMARY proof (Kobayashi's route; uses only Ka 12.5(1) [proved in Ka §13.12], 16.2-16.3 and the exp* adjunction,
  never 16.4/16.6): Col(loc z_gamma) and L_3 (Ka 16.2(i),(ii); SW l.312-521) agree at every
  finite-order character: nontrivial chi by D1.1(c) + Ka 12.5(1); chi = 1 by D3 (both 2 L(E,1)/Omega_+).
  "An element of Lambda has only finitely many zeros" (Kob l.324) / Ka Remark 16.3(1) => equality.
- Normalisation is homogeneous of degree 0 in omega (exp*_{a omega} = a^{-1} exp*_omega, Omega(a omega) = a Omega(omega)),
  so no Manin constant enters HERE: Col uses omega_E on both sides. (It enters in O4.)
- Integrality: loc z_gamma in H^1_Iw(Q_3,T) because Z(f,T) is in H^1(T) (Ka 12.5(4), O1: p != 2, (12.5.2) holds).
  Hence L_3 = Col(loc z_gamma) lies in Lambda.

## Grades
THEOREM (read at source): Ka 12.5(1),(4), 6.2, 16.1-16.3, 17.12; Kob l.243-329. Ka 16.4, 16.6: cross-check only (KKT caveat).
DERIVED here: D1 (family), D2 (integrality, Dwork proved inline), Step 1 assembly, Step 3 assembly.
SECONDARY (textbook, not re-read): Tate local duality/Euler characteristic; Nakayama-Rim; Tate curve over Q_9.
Open named gap in MS-R24: NONE found. Status of MS-R24: DERIVED, UNAUDITED.
