\\ R25 checks of D1/D2 (p = 3). Part A: exact cyclotomic identities. Part B: Dwork integrality.
\\ Run: gp -q -D parisizemax=2000000000 -f coleman_family.gp < /dev/null
\\ ---- Part A: L_n^(alpha) in Q(zeta_N), N = 3^(n+1); zeta_{3^m} = x^(3^(n+1-m)).
Lfam(n, al) = { my(N = 3^(n+1), P = polcyclo(N), z = Mod(x, P), C = 3*2/(3 - al), s);
  s = al^(-(n+1))*C;
  for (m = 1, n+1, my(zm = z^(3^(n+1-m))); s += al^(-m) * 3^(-(n+1-m)) * (zm + zm^(-1) - 2));
  s; }
\\ apply sigma_a (x -> x^a) to an element of Q(zeta_N)
sig(e, a) = { my(P = e.mod); Mod(subst(lift(e), x, x^a), P); }
\\ embed an element of Q(zeta_{3^n}) (as poly in x mod polcyclo(3^n)) into Q(zeta_{3^(n+1)})
up(e, n) = Mod(subst(lift(e), x, x^3), polcyclo(3^(n+1)));
{ for (al = -1, 1, if (al == 0, next);
  print("alpha = ", al, ":  L_0 = ", lift(Lfam(0, al)));
  for (n = 1, 3,
    my(N = 3^(n+1), e = Lfam(n, al), tr = 0);
    for (j = 0, 2, tr += sig(e, 1 + 3^n*j));                 \\ Tr_{k_n/k_{n-1}} (1 + 3^n j, j = 0..2)
    print("  n=", n, "  Tr L_n - L_{n-1} == 0 : ", tr - up(Lfam(n-1, al), n) == 0));
  for (n = 1, 2,
    my(N = 3^(n+1), P = polcyclo(N), z = Mod(x, P), e = Lfam(n, al), g = Mod(4, N), lhs = 0, tau = 0);
    \\ chi(4^i) = zeta_{3^n}^i = z^(3 i), trivial on -1; conductor 3^(n+1)
    for (i = 0, 3^n - 1, lhs += sig(e, lift(g^i)) * z^(3*i));
    for (i = 0, 3^n - 1, for (s = 0, 1, my(a = lift((-1)^s * g^i)); tau += z^(3*i) * z^a));
    print("  n=", n, "  sum L_n^sigma chi(sigma) == alpha^-(n+1) tau(chi) : ", lhs == al^(-(n+1))*tau,
          "   tau != 0: ", tau != 0));
  ); }
\\ ---- Part B: Dwork integrality of exp(c*h), h = h0 + sum_k s^k 3^-k [(1+X)^{3^k} + (1+X)^{-3^k} - 2]
D = 40; K = 90; PR = 120;
hser(h0, sgn) = { my(v = vector(D+1)); v[1] = h0;
  for (j = 1, D, my(t = 0);
    for (k = 0, K, t += sgn^k * 3^(-k) * (binomial(3^k, j) + (-1)^j * binomial(3^k + j - 1, j)));
    v[j+1] = t); v; }
padicv(q) = if (q == 0, oo, valuation(q, 3));
\\ E = exp(c*h): real-coefficient case c = 1 -> single series; case c = i -> A + iB with A' = -h'B, B' = h'A
expre(hv) = { my(e = vector(D+1), h0 = hv[1] + O(3^PR)); e[1] = exp(h0);
  for (j = 0, D-1, my(t = 0); for (m = 0, j, t += (m+1)*hv[m+2]*e[j-m+1]); e[j+2] = t/(j+1)); e; }
expim(hv) = { my(A = vector(D+1), B = vector(D+1), h0 = hv[1] + O(3^PR), c = 0, s = 0);
  for (n = 0, 60, c += (-1)^n*h0^(2*n)/(2*n)!; s += (-1)^n*h0^(2*n+1)/(2*n+1)!);
  A[1] = c; B[1] = s;
  for (j = 0, D-1, my(ta = 0, tb = 0);
    for (m = 0, j, ta += -(m+1)*hv[m+2]*B[j-m+1]; tb += (m+1)*hv[m+2]*A[j-m+1]);
    A[j+2] = ta/(j+1); B[j+2] = tb/(j+1)); [A, B]; }
minv(w) = vecmin(vector(#w, j, padicv(w[j])));
{ my(h = hser(3/2, -1), h1 = hser(3, 1));
  print("B1 nonsplit  exp(i*h):  min v_3 of cos/sin coeffs to X^", D, " = ", minv(expim(h)[1]), " / ", minv(expim(h)[2]));
  print("B2 split     exp(h_1):  min v_3 = ", minv(expre(h1)), "   (Kobayashi family; expect >= 0)");
  print("B3 control   exp(h)  (b = 1, no twist): min v_3 = ", minv(expre(h)), "   (expect < 0)");
  my(w = expim(h1));
  print("B4 control   exp(i*h_1) (twist on split family): min v_3 = ", minv(w[1]), " / ", minv(w[2]), "  (expect < 0)");
  print("B5 h(zeta_3 - 1) check: h0 + S_1 = ", 3/2 + (-3), "  -> log y_0 = b*3/2"); }
