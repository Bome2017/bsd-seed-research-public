# 19 — CONGRUENCE-LINKING GATE (operator spec, 2026-09-16). Kill-first test; no Chow work.
Sources: CH l.1078-1098 (families g = theta_chi(S), h = theta_{chi^{-1}}(S), Psi_T(sigma) = (1+T)^{l(sigma)}, v), l.171 (chi ring class,
chi^c = chi^{-1}), rendered p.23 (alpha = chi(p-bar), beta = chi(p)); lane 13 sec 1 (approximants crystalline of level C prime to p
for n > b), 14 check 1 (Psi_{l_n} = Psi_0^{phi(p^n)}, so Psi_{l_n} = 1 mod p^n as a character of G_K), 13 sec 5 (slots, rho_n).
Notation: l_n = 1 + phi(p^n); g_n := g_{l_n} = theta_{chi Psi_{l_n}}, h_n := h_{l_n} = theta_{chi^{-1} Psi_{l_n}}, both newforms of weight
l_n, level C, nebentype eta_K (n > b). M_n := H^1_par(X_1(C)_Qbar, TSym^{l_n - 2}(O)) (or its Poincare dual with Sym; the argument
below uses only that M_n is an O-lattice with an integral action of the FULL level-C Hecke algebra T_n = O[T_q (all q), <d>]).
X_n := (M_n (x) L)[g_n], Y_n := (M_n (x) L)[h_n] (each 2-dimensional = V_{g_n}, V_{h_n}); L_X := M_n cap X_n, L_Y := M_n cap Y_n;
N_n := M_n cap (X_n (+) Y_n); C_n := N_n / (L_X (+) L_Y) (the operator's congruence module). d_0 := v_p(alpha - beta), a FIXED
integer (CH regularity alpha != beta gives d_0 < infinity; p-distinguished, alpha != beta mod m, gives d_0 = 0).

## Step 1 — prime-to-p Hecke eigensystems: congruent mod p^n, and not beyond a fixed shift
For q != p split in K, q = q_frak q_frak-bar, and chi^{-1} = chi^c:
  a_q(g_n) - a_q(h_n) = (chi(q_frak) - chi(q_frak-bar)) (Psi_{l_n}(q_frak) - Psi_{l_n}(q_frak-bar)).
Psi_{l_n} = 1 mod p^n as a character, so the difference is = 0 mod p^n. For q inert both a_q = 0; for q | C both a_q = 0 (ring class
conductor: q_frak and q_frak-bar both divide cond(chi)); nebentypes agree (eta_K). So the tame eigensystems are congruent mod p^n;
indeed both are congruent to the weight-one eigensystem of theta_chi (a_q(g_n) = a_q(h_n) = chi(q_frak) + chi(q_frak-bar) mod p^n).
Exactness: Psi_{l_n}^{1-c}(sigma) - 1 = v^{phi(p^n) u} - 1 with u = l(sigma) - l(c sigma c); for u a unit and v a topological
generator of 1 + pZ_p this has valuation exactly n; with the fixed shift b of 14 check 1 the order is p^{n + O(1)}. Chebotarev gives
split q with chi(q_frak) != chi(q_frak-bar) mod m when chi^2 != 1 mod m.
  TAME_HECKE_CONGRUENCE_ORDER = p^n (up to the fixed shift b); both eigensystems = theta_chi's tame eigensystem mod p^n.

## Step 2 — the congruence module of the (g_n, h_n) packet is killed by p^{d_0}, uniformly in n  [KILL]
(a) The operator at p. At level C the Hecke operator T_p acts INTEGRALLY on M_n (p does not divide the level). Under the p-frak-adic
    embedding, Psi_{l_n}(p-frak-bar) = Psi_{l_n}(Frob_{p-frak-bar}) = 1 mod p^n (unramified at p-frak-bar, character = 1 mod p^n) and
    Psi_{l_n}(p-frak) = 0 mod p^{l_n - 1} (Psi(p-frak) Psi(p-frak-bar) = Psi((p)) has valuation l_n - 1 = phi(p^n) >= n). Hence
      a_p(g_n) = chi(p-frak) Psi(p-frak) + chi(p-frak-bar) Psi(p-frak-bar) = alpha  (mod p^n),
      a_p(h_n) = chi^{-1}(p-frak) Psi(p-frak) + chi^{-1}(p-frak-bar) Psi(p-frak-bar) = chi(p-frak) = beta  (mod p^n).
    So v_p(a_p(g_n) - a_p(h_n)) = v_p(alpha - beta) = d_0 for every n > max(b, d_0): the T_p-eigenvalues of the two approximants are
    the two ROOTS alpha, beta of the weight-one form theta_chi at p. The tame congruence of step 1 is "g_n = h_n = theta_chi", and at p
    the two approximants are congruent to the two DIFFERENT stabilizations theta_{chi,alpha} and theta_{chi,beta} = CH's (g_alpha, h_{alpha^{-1}}).
(b) Depth bound. Let t := T_p - a_p(h_n) in T_n subset End_O(M_n). t acts on X_n by delta := a_p(g_n) - a_p(h_n), v_p(delta) = d_0, and
    on Y_n by 0. For m = x + y in N_n (x in X_n, y in Y_n): t m = delta x lies in M_n cap X_n = L_X, so p^{d_0} x in L_X, and then
    p^{d_0} y = p^{d_0} m - p^{d_0} x in M_n cap Y_n = L_Y. Hence
      p^{d_0} N_n subset L_X (+) L_Y,   i.e.   p^{d_0} C_n = 0   for all n > max(b, d_0).
    If alpha != beta mod m (p-distinguished): d_0 = 0 and the maximal ideals m_g = (m', T_p - alpha), m_h = (m', T_p - beta) of T_n are
    distinct, so the Hensel idempotents e_{m_g}, e_{m_h} in T_n split M_n integrally and N_n = L_X (+) L_Y: C_n = 0 exactly.
(c) "Discarding U_p / T_p" does not change (b). N_n and C_n are defined by the lattice M_n and the subspaces X_n, Y_n alone; the tame
    subalgebra T'_n is a choice of what to record, not a change of the lattice. t = T_p - a_p(h_n) is an element of End_O(M_n) whether or
    not it is named, and (b) is a statement about End_O(M_n). The same holds at level Cp^r on the ordinary part e M_n: e is integral,
    e is the identity on the class's coefficient lattice (the H9R23 approximant is built with e_ord, DR22 l.2972; BCPV l.498), and
    U_p - a_p(h_n^{ord}) acts on e X'_n by (alpha - beta) Psi(p-frak-bar), valuation d_0, and kills e Y'_n: p^{d_0} e N'_n subset e L_X' (+) e L_Y'.
(d) Where deep gluing WOULD exist, and why it is out of reach. At level Cp the CRITICAL stabilizations g_n^{crit}, h_n^{crit} have
    U_p-eigenvalues beta Psi(p-frak), alpha Psi(p-frak), both = 0 mod p^{l_n - 1}: with the tame congruence, their full eigensystems are
    congruent mod p^n and their lattices can glue to depth ~ n + d_0. But e kills them, the H9R23 class is an ordinary-projected class
    (its g- and h-components lie in e M_n), and a critical-slope analogue of the DR diagonal class is not printed (DR22 constructs with
    e_ord only). Using them changes the class, not the lattice; outside this gate.
  CONGRUENCE_MODULE = C_n killed by p^{d_0}, d_0 = v_p(alpha - beta) fixed; C_n = 0 under p-distinguishedness. Not of exponent p^n.

## Step 3 — gluing anti-isometry (recorded for completeness; step 2 already kills)
Poincare duality on M_n is Hecke-adjoint (T_q <-> T_q', BSV l.580; KLZ l.580), pairing the g_n-part with the g_n-bar = g_n-part, so
X_n perp Y_n rationally, as the operator states. The discriminant-form gluing lemma (a finite-index overlattice N of L_X (+) L_Y with
N unimodular gives an anti-isometry between the images of N in L_X^vee/L_X and L_Y^vee/L_Y) has two requirements here:
 (i) N_n must be unimodular. N_n = M_n cap (X_n (+) Y_n) is unimodular iff it is an orthogonal direct summand of M_n, i.e. iff the
     (g_n, h_n) packet is not glued to any other eigenpacket. In weight l_n >= p, TSym^{l_n - 2}(F) is reducible and the residual
     eigensystem of theta_chi occurs in many forms (all theta_{chi Psi'} with Psi' = Psi mod m, Hasse-invariant translates of theta_chi,
     non-CM forms); multiplicity-one/Gorenstein results are printed only for weights <= p + 1. Unimodularity of N_n is not available.
 (ii) Granting (i), the anti-isometry identifies the images of N_n, which by step 2 are p^{d_0}-torsion: gamma_n lives on the
     p^{d_0}-torsion of the discriminant groups, and is 0 under p-distinguishedness.
  GLUING_ANTI_ISOMETRY = defined at most on p^{d_0}-torsion (0 if alpha != beta mod m); unimodularity of the two-packet lattice not available.

## Step 4 — linking functional versus the live functional
The torsion linking contraction (*) factors through C_{g,n} (image of N_n in L_X^vee/L_X), which is killed by p^{d_0}. So the
functional it induces on the class's g-component has exponent <= p^{d_0} (it is identically 0 under p-distinguishedness). The required
reduced functional c-bar_n : (rho_n mod p^n) -> 1 is nonzero mod p^n on the moving constituent for every n > e (13 sec 5(iv)). For
n > d_0 + e no functional of exponent p^{d_0} equals c-bar_n mod p^n. The constituent obstruction of 13 sec 5 (which slots the linking
pairing would hit) is not even reached.
  LINKING_FUNCTIONAL = exponent <= p^{d_0}; identically zero under p-distinguishedness.
  LIVE_FUNCTIONAL_MATCH = NO.

## Return
```
TAME_HECKE_CONGRUENCE_ORDER = p^n (exact up to the fixed shift b of 14 check 1); both eigensystems = theta_chi's tame eigensystem mod p^n
CONGRUENCE_MODULE          = C_n killed by p^{d_0}, d_0 = v_p(alpha - beta) FIXED (0 under p-distinguishedness, then C_n = 0 exactly);
                             bound realized by the integral operator t = T_p - a_p(h_n) (level C) or U_p - a_p(h_n^ord) on e M_n (level Cp^r)
GLUING_ANTI_ISOMETRY       = at most on p^{d_0}-torsion; unimodularity of N_n (needed for the discriminant-form lemma) not available at weight l_n >= p
LINKING_FUNCTIONAL         = exponent <= p^{d_0}; identically 0 when alpha != beta mod m
LIVE_FUNCTIONAL_MATCH      = NO
FIRST_DEFECT               = Step 2(a): a_p(g_n) = alpha, a_p(h_n) = beta (mod p^n). The tame congruence is "both = theta_chi mod p^n";
                             at p the approximants converge to the two DIFFERENT p-stabilizations of theta_chi, whose eigenvalues alpha, beta
                             differ by the fixed d_0 = v_p(alpha - beta). The integral lattice cannot glue g_n to h_n more deeply than p^{d_0},
                             independently of n, and "discarding T_p/U_p" does not remove them from End_O(M_n).
ARCHITECTURE               = KILLED (operator rule: LIVE_FUNCTIONAL_MATCH = NO). No Chow work performed. No new H9R number.
RESIDUAL (outside gate)    = deep gluing exists only between the CRITICAL-slope stabilizations (U_p = 0 mod p^{l_n - 1} for both), which
                             e_ord kills; the printed DR class is e_ord-projected, so using them changes the class, not the lattice.
```
