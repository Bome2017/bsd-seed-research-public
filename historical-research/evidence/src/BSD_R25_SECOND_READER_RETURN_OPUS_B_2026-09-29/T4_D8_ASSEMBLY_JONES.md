# T4 — D8 (assembly) against Jones 1989.  VERDICT: PASS for steps 4-6 and 8-9; step 7 stays an INPUT, with a sharpened warning
Jones author copy, pages reversed (printed p = 28 - pdf p); all quotes from the rendered pages.

## Step 4 (control) — DERIVED: CORRECT
(12.5.2) (SL_2(Z_3) in the image of G_{Q(mu_{3^inf})}, SECONDARY seed input) gives E(Q(mu_{3^inf}))[3] = 0, so
E(Q_inf)[3^inf] = 0 and Sel(E/Q) -> Sel(E/Q_inf)^Gamma is injective. So rank_{Z_3} X_Gamma >= corank Sel(E/Q) >= 2.
For finitely generated torsion X: rank X/TX = number of elementary summands Lambda/(T^e) <= ord_T char(X) (pseudo-isomorphisms
change coinvariants by finite groups). Hence ord_T f_E >= 2.
## Step 5 — DERIVED: CORRECT
T^2 | f_E | L_3 forces a_0 = a_1 = 0 (a_1 = 0 is forced, not assumed). Lambda is a UFD, so L_3 = T^2 h, f_E = T^2 g, g | h;
evaluating at T = 0 gives g(0) | h(0) = a_2 in Z_3. So v_3(g(0)) <= v_3(a_2) = 2, g(0) != 0 and ord_T f_E = 2.
Side check (THEOREM, Kato 18.4, txt l.8707-8720): "rank(E(Q)) <= ord_{s=1}(L_{p-adic,alpha}(f)) if E is not a Tate curve" (alpha != 1
here). With ord = 2 = rank this gives corank Sel(E/Q) = 2, so Sha[3^inf] is finite BEFORE any leading-term formula. This is
Jones's hypothesis 1 (below); no circularity. (Same conclusion from Step 4 + ord_T f_E = 2.)

## Step 6 against Jones — THEOREM quotes, then the check
- p.1: "Let p != 2 be a prime number and let K be a number field." p = 3, K = Q.
- p.3 hypotheses: "1. Sha_{p^inf}(K) is finite; 2. every prime of K for which A has bad reduction splits finitely in L; 3. the
  reduction of A is semi-stable at every place of K dividing p, and is an extension of an ordinary abelian variety by a torus
  for every t in T; 4. for every place t in T, the universal norms of A(L_t) are of finite index in A(K_t)." For 4: "known to
  hold ... A is an elliptic curve with non-split multiplicative reduction at v (see [11])". Seed: 1 by Step 5; 2 cyclotomic;
  3 multiplicative at 3; 4 by [11] (SECONDARY). p.4: e = sum of dimensions of maximal SPLIT subtori: e = 0 at nonsplit 3.
- p.6: "S_inf := Image H^1(O_L, A^0_{p^inf}) -> H^1(O_L - T, A^0_{p^inf}). They are quasi-isomorphic to the classical p-Selmer
  group of A over K and L respectively (see [6])." Quasi-isomorphic = finite kernel and cokernel (p.1), so char(S_inf^*) = f_E
  exactly (classical Selmer over Q_inf = R25's X on the Delta-trivial branch). [6] itself not re-read: SECONDARY.
- p.4: "the map which sends T to gamma - 1 induces an isomorphism from Z_p[[T]] to Lambda" (same variable as SW and R25);
  p.5: "F_M^{(m)}(0) := (1/m!) d^m/dT^m F_M(T)|_{T=0}" — i.e. g(0) for m = 2.
- p.8: "This definition depends on our choice of generator gamma of Gamma. To remedy this we set <,>_p := <,>_gamma log kappa(gamma)."
- p.16: "ker g / cok g = L(A)/(log_p kappa(gamma))^{r+e} . det<,>_p Sha_K /(A_{p^inf}(K) A~_{p^inf}(K)) . prod_{l not | inf} m_l."
- p.17, Theorem 3.1: "rho >= r + e. If <,>_p is non-degenerate, then rho = r + e and L_H^(rho)(1) ~ L(A) det<,>_p Sha_K /
  (A^fin_{p^inf}(K) A~^fin_{p^inf}(K)) prod m_l", with L_H(s) := f_H(kappa(gamma)^{1-s}); p.18 (proof): "L_H^(rho)(1) =
  (-log_p kappa(gamma))^rho f_S^(r)(1)"; nonsplit display: "rho = r and L_H^(rho)(1) ~ det<,>_p Sha_K/(A_{p^inf}(K) A~_{p^inf}(K)) prod m_l".
- DERIVED: the (log_p kappa(gamma))^{-r} factor IS there, in the T-variable. With e = 0, r = 2:
  g(0) = F_S^{(2)}(0) ~ det<,>_p /(log_3 kappa(gamma))^2 . #Sha[3^inf] . prod m_l / (#E(Q)[3^inf])^2 = Reg_gamma . #Sha[3^inf] . (units),
  Reg_gamma := det<,>_gamma = det<,>_p/(log_3 kappa(gamma))^2. In the s-variable the two log factors cancel. m_l: Tamagawa-type,
  all c_l in {1,2}; any factor at 3 such as #E~_ns(F_3) = 4 is a unit; E(Q)[3] = 0; A~ = A. The r! and (-1)^r are units.
  D8 step 6 ("g(0) = unit * #Sha[3^inf] * prod c_l^(3) * Reg_gamma / #E(Q)[3^inf]^2") matches, with Reg_gamma as just defined.
- Non-degeneracy of <,>_p is a hypothesis of the formula; it comes from the height certificate (step 7), not from Step 5.

## Step 7 — INPUT (O5). Sharpened warning (DERIVED)
v_3(log_3 kappa(gamma)) = 1 for every topological generator (log_3 4 = 3 + 2.3^2 + ..., checks/reg3.log). So
v_3(Reg_gamma) = v_3(det<,>_p) - 2 EXACTLY. The chain needs v_3(Reg_gamma) >= -1, i.e. v_3(det<,>_p) >= 1:
  v_3(Reg_gamma) = 0  -> #Sha[3^inf] <= 9;   = -1 -> <= 27 -> 9 (square, B2);   = -2 (i.e. v_3(det<,>_p) = 0) -> <= 81: NOT closed.
So the certificate must state which determinant it reports. "v_3 = 0" for det<,>_gamma (SW/MTT's Reg_gamma) closes the chain;
"v_3 = 0" for Jones's gamma-free det<,>_p would leave exactly the factor 9 open. The certificate is not in my bundle
(S3_GOVERNING_RECORD says only "an independent nonzero 3-adic height determinant supplies nondegeneracy"). I did not recompute
it: PARI's ellpadicheight returns the Dieudonne pair [f,g] (reg3.log); the canonical height at nonsplit 3 needs the Tate-curve
correction over Q_9, which is not a tiny check. R25's WARNING (156a1: normalized regulators can have v_3 < 0) stands.
## Steps 8-9 — DERIVED: CORRECT given step 7 (v_3(Reg_gamma) >= -1) and B2; the square fallback covers -1.
