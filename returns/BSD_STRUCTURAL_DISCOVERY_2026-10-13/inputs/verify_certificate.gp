\\ verify_certificate.gp -- standalone exact verifier for Lane B2 (#Sha(E/Q)[3] >= 9 for the seed curve).
\\ Run: gp -q -D parisizemax=4000000000 -f verify_certificate.gp < /dev/null
\\ Uses only exact arithmetic (integers, rationals, polmods over L); no bnfinit, no GRH, no search-side data
\\ except the two cubics, the two points and the defining polynomial of L (all re-verified here).
\\ ===== standalone verifier library (exact arithmetic only; no GRH, no bnfinit) =====
\\ variable order: x > y > z > b1..b6 > t > s > X > w
z; b1; b2; b3; b4; b6; t; s; X; w;
V_hm(U) = my(v = [x,y,z]); matrix(3, 3, i, j, deriv(deriv(U, v[i]), v[j]));
V_h(U) = matdet(V_hm(U));
V_mon = [x^3,y^3,z^3,x^2*y,x^2*z,y^2*x,y^2*z,z^2*x,z^2*y,x*y*z];
V_cv(U) = vector(10, i, my(m = V_mon[i]); polcoef(polcoef(polcoef(U, poldegree(m,x), x), poldegree(m,y), y), poldegree(m,z), z));
\\ raw covariant scalars: q4 with d/de H(U + e H(U)) = q4*U ; [A,B] with H(H(U)) = A*U + B*H(U)
{V_raw(U) = my(HU = V_h(U), D1 = trace(matadjoint(V_hm(U)) * V_hm(HU)), q4 = D1 / U, HH, cU, cH, cHH, i1, i2, d, A, B);
  if (type(q4) == "t_RFRAC" || poldegree(q4, x) || poldegree(q4, y) || poldegree(q4, z), error("q4 not scalar"));
  HH = V_h(HU); cU = V_cv(U); cH = V_cv(HU); cHH = V_cv(HH);
  for (i = 1, 10, for (j = i+1, 10, d = cU[i]*cH[j] - cU[j]*cH[i]; if (d != 0, i1 = i; i2 = j; break(2))));
  A = (cHH[i1]*cH[i2] - cHH[i2]*cH[i1])/d; B = (cU[i1]*cHH[i2] - cU[i2]*cHH[i1])/d;
  if (cHH != A*cU + B*cH, error("H(H(U)) not in span(U, H(U))")); simplify([q4, A, B]);}
\\ calibration on the generic Weierstrass cubic (computed here, not imported)
is_rat(u) = type(u) == "t_INT" || type(u) == "t_FRAC";
{V_calib() = my(Wg = y^2*z + b1*x*y*z + b3*y*z^2 - x^3 - b2*x^2*z - b4*x*z^2 - b6*z^3, B2 = b1^2 + 4*b2, B4 = 2*b4 + b1*b3, B6 = b3^2 + 4*b6,
     C4 = B2^2 - 24*B4, C6 = -B2^3 + 36*B2*B4 - 216*B6, r = V_raw(Wg), k4 = simplify(r[1]/C4), k6 = simplify(r[3]/C6), kA = simplify(r[2]/C4^2));
  if (!is_rat(k4) || !is_rat(k6) || !is_rat(kA), error("calibration not constant: ", [k4, k6, kA]));
  [k4, k6, kA];}
V_K = V_calib();
{V_c46(U) = my(r = V_raw(U), c4 = r[1]/V_K[1], c6 = r[3]/V_K[2]); if (r[2] != V_K[3]*c4^2, error("A != kA c4^2")); [c4, c6];}
V_sub(U, g) = my(v = g*[x,y,z]~); substvec(U, [x,y,z], [v[1], v[2], v[3]]);
\\ ---- local solubility: Hensel points ----
V_ev(F, P) = substvec(F, [x,y,z], [P[1], P[2], P[3]]);
\\ Hensel criterion (multivariate Newton): v_l(U(P)) > 2 * min_i v_l(dU/dx_i (P)), P primitive integral
{V_hcrit(U, l, P) = my(G = [deriv(U,x), deriv(U,y), deriv(U,z)], u = V_ev(U, P), vg = vecmin(vector(3, i, my(g = V_ev(G[i], P)); if (g == 0, oo, valuation(g, l)))));
  if (vg == oo, return(0)); if (u == 0, return(1)); valuation(u, l) > 2*vg;}
\\ small l: exhaustive tree search over primitive points mod l^k, k <= kmax
{V_hsmall(U, l, kmax) = my(cur = List());
  for (a = 0, l-1, for (b = 0, l-1, listput(cur, [a, b, 1]))); for (a = 0, l-1, listput(cur, [a, 1, 0])); listput(cur, [1, 0, 0]);
  for (k = 1, kmax, my(nxt = List());
    for (i = 1, #cur, my(P = cur[i]); if (V_ev(U, P) % l^k != 0, next);
      if (V_hcrit(U, l, P), return(P));
      if (k < kmax, forvec(d = vector(3, j, [0, l-1]), my(Q = P + l^k * d); listput(nxt, Q))));
    cur = nxt; if (#cur == 0, break));
  0;}
\\ large l: a smooth F_l-point (z = 1 chart, then z = 0 line)
{V_hlarge(U, l) = my(G = [deriv(U,x), deriv(U,y), deriv(U,z)]);
  for (a = 0, l-1, my(f = Mod(1, l) * substvec(U, [x, z], [a, 1]));
    if (f == 0, next);
    my(rt = polrootsmod(f, l)); for (i = 1, #rt, my(P = [a, lift(rt[i]), 1]); if (V_hcrit(U, l, P), return(P))));
  my(f = Mod(1,l) * substvec(U, [y, z], [1, 0])); if (f != 0, my(rt = polrootsmod(subst(f, x, X), l)); for (i = 1, #rt, my(P = [lift(rt[i]), 1, 0]); if (V_hcrit(U, l, P), return(P))));
  if (V_ev(U, [1,0,0]) % l == 0 && V_hcrit(U, l, [1,0,0]), return([1,0,0]));
  0;}
V_hensel(U, l) = if (l <= 13, V_hsmall(U, l, 6), V_hlarge(U, l));
\\ real point: restriction to the line z = 0 is a real binary cubic (or (1:0:0) lies on U)
V_realpt(U) = my(f = substvec(U, [y, z], [1, 0])); if (V_ev(U, [1,0,0]) == 0, [1,0,0], poldegree(f, x) == 3, "odd-degree binary cubic on z=0 has a real root", 0);
\\ ---- class images in L^x / L^x3, L = Q[w]/(fL) ----
\\ Kummer image of a point: tangent line at T (flex) evaluated at P
{V_kummer(ai, T, P) = my(lam = (3*T[1]^2 + 2*ai[2]*T[1] + ai[4] - ai[1]*T[2]) / (2*T[2] + ai[1]*T[1] + ai[3]), nu = T[2] - lam*T[1], v = P[2] - lam*P[1] - nu);
  if (v == 0, error("kummer value 0")); v;}
\\ Hesse pencil quartic: Delta(U + t H(U)) = kappa * Q(t)^3
{V_hquartic(U) = my(HU = V_h(U), iv = V_c46(U + t*HU), D = (iv[1]^3 - iv[2]^2)/1728, fa = factor(D), Q, k);
  Q = prod(i = 1, #fa~, fa[i,1]); k = simplify(D / Q^3); if (type(k) == "t_POL" || type(k) == "t_RFRAC" || k == 0, error("pencil discriminant is not kappa*Q^3"));
  [Q, HU];}
\\ class of a cubic: L-root t0 of Q (verified by substitution), triangle F = U + t0 H, line restriction, Cardano.
{V_cubicclass(fL, U) = my(QH = V_hquartic(U), Q = QH[1], HU = QH[2], rt, F, g, A = [1,0,0], B = [0,1,0], a, b, c1, d, p, q, D, e, cc, tries = 0);
  if (poldegree(Q, t) == 4, rt = nfroots(fL, Q); if (#rt < 1, error("no L-root of Hesse quartic")); if (subst(Q, t, rt[1]) != 0, error("root check")); F = U + rt[1]*HU,
     F = HU);   \\ degree < 4: the member t = oo, i.e. H(U) itself, is the L-rational triangle candidate
  while (1, g = substvec(F, [x,y,z], [s*A[1]+B[1], s*A[2]+B[2], s*A[3]+B[3]]);
    if (poldegree(g, s) == 3 && poldisc(g) != 0, break); tries++; if (tries > 200, error("no good line"));
    A = vector(3, i, random(11)-5); B = vector(3, i, random(11)-5));
  a = polcoef(g,3,s); b = polcoef(g,2,s)/a; c1 = polcoef(g,1,s)/a; d = polcoef(g,0,s)/a;
  p = c1 - b^2/3; q = 2*b^3/27 - b*c1/3 + d; D = -4*p^3 - 27*q^2;
  e = nfroots(fL, X^2 + D/3); if (#e < 1, error("-disc/3 not a square in L: not a mu_3-torsor")); e = e[1];
  if (e^2 != -D/3, error("sqrt check"));
  cc = -q/2 + e/6; if (cc == 0, cc = -q/2 - e/6);
  [cc, if (poldegree(Q, t) == 4, rt[1], "oo"), [A, B]];}
\\ cubic residue symbol at the degree-1 prime (p, w - r); returns 0,1,2 w.r.t. fixed omega
{V_cr3(c, p, r, om) = my(pl = lift(c), v, u); if (denominator(content(pl)) % p == 0, error("non-integral at p"));
  v = Mod(subst(pl, w, r), p); if (v == 0, error("not a unit at p")); u = v^((p-1)/3);
  if (u == 1, 0, u == om, 1, u == om^2, 2, error("cr3"));}
\\ degree-1 primes p = 1 mod 3, p not dividing disc(fL) and not in the avoid list; m of them
{V_deg1(fL, m, avoid) = my(res = List(), p = 7, dF = poldisc(fL));
  while (#res < m, p = nextprime(p + 1); if (p % 3 != 1 || dF % p == 0 || setsearch(avoid, p), next);
    my(rs = polrootsmod(fL, p)); for (i = 1, #rs, if (#res < m, listput(res, [p, lift(rs[i]), lift(znprimroot(p)^((p-1)/3))]))));
  Vec(res);}
\\ ================= main verification routine =================
\\ ai: a-invariants; pts: list of rational points (Kummer classes used); cubs: list of integral ternary cubics;
\\ fL: polynomial in w defining L; nsym: number of degree-1 primes for residue symbols. Returns 1 iff all checks pass.
{V_verify(ai, pts, cubs, fL, nsym) = my(E = ellinit(ai), gr = ellglobalred(E), N = gr[1], ok = 1, xs, xT, us, T, q3, cls = [], lab = [], Dl, Mt, rk);
  print("E = ", ai, "   N = ", N, " = ", factor(N), "   torsion = ", elltors(E)[2]);
  if (!polisirreducible(fL) || poldegree(fL) != 8, print("FAIL: fL"); return(0));
  \\ T in E(L)[3] - {0}
  xs = nfroots(fL, subst(elldivpol(E, 3), x, X)); if (#xs != 1, print("FAIL: psi3 roots in L = ", #xs); return(0)); xT = xs[1];
  us = nfroots(fL, X^2 + (ai[1]*xT + ai[3])*X - (xT^3 + ai[2]*xT^2 + ai[4]*xT + ai[5])); if (#us < 1, print("FAIL: no yT"); return(0));
  T = [xT, us[1]];
  if (T[2]^2 + ai[1]*T[1]*T[2] + ai[3]*T[2] != T[1]^3 + ai[2]*T[1]^2 + ai[4]*T[1] + ai[5] || subst(elldivpol(E,3), x, T[1]) != 0, print("FAIL: T"); return(0));
  \\ uniqueness of the L-rational subgroup <T>: psi3/(X - xT) has no root mod some degree-1 prime
  q3 = subst(elldivpol(E,3), x, X) / (X - xT);
  my(found = 0, p = 7, dF = poldisc(fL));
  while (!found && p < 10^5, p = nextprime(p+1); if (dF % p == 0 || (3*N) % p == 0, next);
    my(rs = polrootsmod(fL, p)); for (i = 1, #rs, my(r = lift(rs[i]), qb, cz = [denominator(content(lift(polcoef(q3, j, X)))) | j <- [0..3]]);
      if (vecmax(apply(u -> u % p == 0, cz)), next);
      qb = Mod(1, p) * sum(j = 0, 3, subst(lift(polcoef(q3, j, X)), w, r) * X^j);
      if (poldegree(qb) == 3 && #polrootsmod(qb, p) == 0, found = [p, r]; break)));
  if (!found, print("FAIL: uniqueness of L-rational subgroup not certified"); return(0));
  print("L-rational subgroup <T> unique: psi3/(X-xT) has no root mod (p, w - r) = ", found);
  \\ Kummer images of points
  for (i = 1, #pts, my(P = pts[i]);
    if (!ellisoncurve(E, P), print("FAIL: point not on E"); return(0));
    cls = concat(cls, [V_kummer(ai, T, P)]); lab = concat(lab, [Str("kappa", P)]));
  \\ cubics
  for (i = 1, #cubs, my(U = cubs[i], iv, s2, Dc, bad, cc);
    print("--- cubic ", i, ": ", U);
    iv = V_c46(U); s2 = iv[2]*E.c4 / (iv[1]*E.c6);
    if (!issquare(s2) || iv[1] != s2^2*E.c4 || iv[2] != s2^3*E.c6, print("FAIL: Jacobian: c4,c6 = ", iv, " not (s^4 c4(E), s^6 c6(E))"); ok = 0; next);
    print("  Jacobian: c4(C) = s^4 c4(E), c6(C) = s^6 c6(E) with s^2 = ", s2);
    Dc = (iv[1]^3 - iv[2]^2)/1728; bad = Set(concat([2, 3], concat(factor(N)[,1]~, factor(abs(Dc))[,1]~)));
    print("  disc(C) = ", factor(Dc), "   primes to check: ", bad, "   (all other l: good reduction, soluble by Hasse-Weil + Hensel)");
    my(rp = V_realpt(U)); if (rp == 0, print("  FAIL real"); ok = 0; next); print("  R: ", rp);
    for (j = 1, #bad, my(l = bad[j], P = V_hensel(U, l));
      if (P == 0, print("  FAIL: no Hensel point found at l = ", l); ok = 0; break);
      print("  Q_", l, ": Hensel point ", P, "  v(U(P)) = ", if (V_ev(U,P)==0, "oo", valuation(V_ev(U,P), l)), "  min v(grad) = ", vecmin(vector(3, k, my(g = V_ev([deriv(U,x),deriv(U,y),deriv(U,z)][k], P)); if (g == 0, oo, valuation(g, l))))));
    if (!ok, next);
    cc = V_cubicclass(fL, U); print("  class image in L^x/L^x3: t0 = ", cc[2], "   line = ", cc[3]);
    cls = concat(cls, [cc[1]]); lab = concat(lab, [Str("C", i)]));
  if (!ok, return(0));
  \\ residue symbols
  my(avoid = Set(concat(factor(3*N)[,1]~, [])), AP = V_deg1(fL, nsym, avoid), rows = List());
  for (q = 1, #AP, my(r = iferr(vector(#cls, j, V_cr3(cls[j], AP[q][1], AP[q][2], AP[q][3])), er, 0)); if (r != 0, listput(rows, r)));
  Mt = Mod(matconcat(Vec(rows)~), 3); rk = matrank(Mt);
  print("cubic residue symbol matrix: ", #rows, " degree-1 primes x ", #cls, " classes; F3-rank = ", rk);
  if (rk != #cls, print("FAIL: classes dependent in L^x/L^x3"); return(0));
  my(sub = matimage(Mt~)); \\ exhibit a certifying square minor
  my(sel = List(), cur = [;]); for (q = 1, #rows, my(tst = if (#cur, matconcat([cur; Mat(Mt[q,])]), Mat(Mt[q,]))); if (matrank(tst) > matrank(cur), cur = tst; listput(sel, [AP[q][1], AP[q][2], lift(Mt[q,])])));
  print("certifying primes (p, w mod p, symbols): ", Vec(sel));
  1;}

\\ ================= DATA (seed) =================
V_ai = [0,-1,0,-66020924,-65074271436];            \\ minimal model of the seed curve E
V_P1 = [-3031, 327384]; V_P2 = [-2394, 281520];    \\ E(Q)/3E(Q) generators (rank 2 imported; torsion checked below)
V_fL = w^8 - 1188376638*w^4 - 7030398068360*w^2 - 117686586145348587;   \\ L = Q(T), T in E[3]-{0}
V_C = [61*x^3 + (31*y + 15*z)*x^2 + (-7*y^2 - 56*z*y - 139*z^2)*x + (20*y^3 + 75*z*y^2 - 23*z^2*y + 27*z^3), 92*x^3 + (49*y + 73*z)*x^2 + (-61*y^2 + 50*z*y + 31*z^2)*x + (-35*y^3 + 58*z*y^2 - 58*z^2*y - 31*z^3)];               \\ [C1, C2] (also printed below)
\\ ================= MAIN CERTIFICATE =================
print("==================== CERTIFICATE CHECK: seed curve ====================");
print("calibration constants [k4, k6, kA] (computed from the generic Weierstrass cubic) = ", V_K);
V_res = V_verify(V_ai, [V_P1, V_P2], V_C, V_fL, 80);
print("CERTIFICATE RESULT: ", if (V_res == 1, "PASS", "FAIL"));
if (V_res == 1, print("=> kappa(P1), kappa(P2), [C1], [C2] are F3-independent in Sel_3(E/Q): dim Sel_3 >= 4."); print("   With rank E(Q) = 2 (imported) and E(Q)[3] = 0 (torsion Z/2, checked): dim Sha(E/Q)[3] >= 2, #Sha(E/Q)[3] >= 9."));
\\ ================= NEGATIVE CONTROLS (each must be rejected) =================
{V_kummercubic(ai, Q) = my(y0 = -Q[2] - ai[1]*Q[1] - ai[3], Wp, G2);
  Wp = y^2 + ai[1]*x*y + ai[3]*y - x^3 - ai[2]*x^2 - ai[4]*x - ai[5];
  G2 = subst(Wp, y, y0 + y*(x - Q[1])) / (x - Q[1]); G2 = substvec(G2, [x,y], [x/z, y/z]) * z^3; G2 / content(G2);}
V_Et = ellinit(elltwist(ellinit(V_ai), -4));
V_Wt = y^2*z + V_Et.a1*x*y*z + V_Et.a3*y*z^2 - x^3 - V_Et.a2*x^2*z - V_Et.a4*x*z^2 - V_Et.a6*z^3;
print("==================== NEGATIVE CONTROLS ====================");
print("NEG(b) C2 replaced by the Kummer cubic of P1 (class kappa(P1)):"); V_n = V_verify(V_ai, [V_P1, V_P2], [V_C[1], V_kummercubic(V_ai, V_P1)], V_fL, 80); print("NEG(b) RESULT (must be 0): ", V_n);
print("NEG(b') C2 replaced by the Kummer cubic of P1+P2:"); V_n = V_verify(V_ai, [V_P1, V_P2], [V_C[1], V_kummercubic(V_ai, elladd(ellinit(V_ai), V_P1, V_P2))], V_fL, 80); print("NEG(b') RESULT (must be 0): ", V_n);
print("NEG(c2) C2 replaced by the Weierstrass cubic of the Q(i)-twist (c6 sign):"); V_n = V_verify(V_ai, [V_P1, V_P2], [V_C[1], V_Wt], V_fL, 80); print("NEG(c2) RESULT (must be 0): ", V_n);
print("NEG(c3) C2 with one coefficient perturbed by 1:"); V_n = V_verify(V_ai, [V_P1, V_P2], [V_C[1], V_C[2] + x^3], V_fL, 80); print("NEG(c3) RESULT (must be 0): ", V_n);
\\ ================= SELF-TEST (positive control): the two class-image methods agree =================
\\ Kummer cubic of P (E embedded by |2O + P|, has the rational point O) has class kappa(+-P); its triangle/Cardano
\\ image must equal the tangent-line image f_T(P) up to inversion: all residue symbols of c*f or c/f vanish.
{V_selftest(ai, fL, Ps, m) = my(E = ellinit(ai), xs = nfroots(fL, subst(elldivpol(E,3), x, X)), xT = xs[1], T, AP = V_deg1(fL, m, Set(factor(3*ellglobalred(E)[1])[,1]~)), ok = 1);
  T = [xT, nfroots(fL, X^2 + (ai[1]*xT + ai[3])*X - (xT^3 + ai[2]*xT^2 + ai[4]*xT + ai[5]))[1]];
  for (i = 1, #Ps, my(k = V_kummer(ai, T, Ps[i]), c = V_cubicclass(fL, V_kummercubic(ai, Ps[i]))[1], same = 1, inv = 1, used = 0);
    for (q = 1, #AP, my(a = iferr(V_cr3(c, AP[q][1], AP[q][2], AP[q][3]), er, -1), b = iferr(V_cr3(k, AP[q][1], AP[q][2], AP[q][3]), er, -1));
      if (a < 0 || b < 0, next); used++; if (a != b, same = 0); if ((a + b) % 3 != 0, inv = 0));
    print("self-test P = ", Ps[i], ": class(Kummer cubic) == kappa(P)^(+1): ", same, "  ^(-1): ", inv, "   (", used, " primes)");
    if (!(same || inv) || used < 20, ok = 0));
  ok;}
print("==================== SELF-TEST ====================");
V_st = V_selftest(V_ai, V_fL, [V_P1, V_P2, elladd(ellinit(V_ai), V_P1, V_P2)], 80); print("SELF-TEST RESULT (must be 1): ", V_st);
quit;
