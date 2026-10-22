# D6 — O2: the Poitou-Tate passage (Kato 17.13 template, nonsplit inputs DERIVED; UNAUDITED)

Kato's H^q(T) = lim_n H^q(Z[zeta_{p^n}, 1/p], j_* T) (Ka 12.2, and 8.2: "H^q(R, j_*A) is denoted H^q(R, A)").
X := Pontryagin dual of lim_n Sel(Q(zeta_{3^n}), E[3^inf]) = the CLASSICAL Selmer group over Q(mu_3^inf) (Ka 14.1:
Bloch-Kato Sel = usual Sel for abelian varieties).  All statements below are on the relevant Delta-branch.

## (a) The exact sequence
Ka (14.9.3) (rendered p.240; Poitou-Tate with j_* coefficients over O_K[1/p]; local terms ONLY at p) for
K = Q(zeta_{3^n}), in the inverse limit, together with Ka (17.10.1) (below), gives Ka (17.13.1):
 0 -> H^1(T)/lim H^1_f(Z[.,1/p],T) -> H^1_loc(T)/lim H^1_f(Q_3(zeta),T) -> X -> H^2(T) -> H^2_loc(T).
Nonsplit inputs replacing Kato's good-ordinary Lemma 17.9 (DERIVED):
- (a1) H^2_loc(T) = 0 (addendum 5; D5 Step 1(a) for T itself: H^0(Q_3(mu_3^inf), E[3^inf]) = 0).
- (a2) = O2(b): H^1_f(K_n,T) = image of H^1(K_n,T^0) for every n (K_n in Q_3(mu_3^inf)): rationally both have dimension
  [K_n:Q_3] (dim H^1_f(K_n,V) = dim D_dR/Fil^0 + dim H^0 = [K_n:Q_3]; H^1(K_n,V^0) = H^1_f and injects since
  H^0(K_n,V/V^0) = 0); integrally the quotient embeds in H^1(K_n,T/T^0)_tors = H^0(K_n, Q_3/Z_3(eta)) = 0.
  Dually (BK Prop 3.8, as in Ka 17.10) the classical condition at 3 is Greenberg's: ker(H^1 -> H^1(., Q_3/Z_3(eta))).
  So lim H^1_f(Q_3(zeta),T) = H^1_loc(T^0) and H^1_loc(T)/lim H^1_f = H^1_Iw(T)/H^1_Iw(T^0) (Kato's 17.13.3, exact).
- (a3) lim H^1_f(Z[.,1/p],T) = 0 and H^1(T) -> H^1_loc(T)/H^1_loc(T^0) is injective: H^1(T) is torsion-free of
  rank 1 (Ka 12.4(2)) and the image of Z(f) has rank 1 because Col(loc z) = L_3 != 0 (Ka 17.13.2 argument).
Result:  0 -> H^1(T)/Z(f,T) -> Lambda/(L_3) -> X -> H^2(T) -> 0   (using MS-R24: Col iso, Col(loc Z(f,T)) = (L_3)).
Delta-branch / O2(d): Ka 12.5(1) gives z_{iota(gamma)} = -sigma_{-1} z_gamma; on the branch used, Z(f,T) is generated
by z_gamma with gamma^+ a basis of T^+ (the gamma^- part dies there), so Col(loc Z(f,T)) = Lambda L_3.

## (b) T-INT
X is torsion and, for every height-one P of Lambda (P = (3) included):
 length(X_P) - ord_P(L_3) = length(H^2(T)_P) - length((H^1(T)/Z(f,T))_P) <= 0      (Ka 12.5(4); O1).
Hence char_Lambda(X) | L_3 in Lambda.  [char multiplicative on the 4-term sequence of torsion modules.]

## (c) Local terms at l in {2, 2243, 4547, 5843} — including l = 5843 (3 | 5843+1)
- Ka 17.10 (rendered p.276-277), the l != p step, uses NO hypothesis on reduction at p or at l: with
  C_l^n = H^1(Z_l (x) Z[zeta_{p^n}], T(r)(x)Q/Z) (the j_* condition) and B_l^n the Bloch-Kato image,
  "lim_n C_l^n = 0 since H^1(Z_l (x) Z[zeta_{p^n}], ) = H^1(F_l (x) Z[zeta_{p^n}], ) and the p-cohomological dimension of
  U_n F_l(zeta_{p^n}) is zero. Hence lim_n B_l^n = 0", giving (17.10.1): lim Sel = lim S = the j_*-Selmer group.
- So in the limit the j_* condition, the Bloch-Kato condition and the classical condition all equal 0 at every
  l != 3, whatever the reduction type. Seed check: 5843 is inert in Q_inf (residue field = the Z_3-extension of
  F_5843, whose absolute Galois group is pro-prime-to-3): H^1_ur(Q_inf,5843, E[3^inf]) = 0 although
  E(Q_inf,5843)[3^inf] is infinite. The group E(Q_l)[3] = Z/3 never enters.
- Where a factor (1 + 5843^{-1}) WOULD come from: a Sigma-imprimitive Selmer group (no condition at 5843, i.e.
  G_{Q,Sigma}-cohomology instead of j_*) has char = char(X) * P_5843(5843^{-1} gamma_5843), P = 1 - a_l u, value
  1 + 1/5843 at the trivial character (v_3 = 1). Route K never uses it: Kato's z_gamma interpolate L_{p} with
  ONLY p removed (Ka 12.5(1) + 6.2: eps(l) = 0 for l | N keeps (1 - a_l l^{-s})^{-1}), and Kato's H^1, H^2 use j_*.
  Both sides are primitive at 5843. No stray factor. (K-R25c NC1: the mixed version contradicts data 126/126.)

## (d) Conclusion of O2
T-INT: char(Sel_{3^inf}(E/Q_inf)^v) divides L_3 in Lambda (classical Selmer; Delta-trivial branch after the usual
twist identification; Sel(E/Q_inf) = Sel(E/Q(mu_3^inf))^Delta since |Delta| = 2).
Grades: THEOREM at source: Ka 8.2, 12.4, 12.5, 14.1, 14.9.3, 17.10 (l != p step), 17.13 (template).
DERIVED: (a1)-(a3) at nonsplit p; the assembly. No stray factor named.
