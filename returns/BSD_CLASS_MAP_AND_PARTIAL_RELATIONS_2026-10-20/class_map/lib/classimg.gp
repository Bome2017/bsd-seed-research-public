\\ Class images in L^x/L^x3 (L = Q(T), T in E[3]\{0}) for points (tangent line at T) and for plane cubics
\\ (L-rational triangle of the Hesse pencil + Cardano). Needs cubinv.gp. Variable order x>y>z>..>t>s>w.
t; s; X; w;
\\ tangent-line value f_T(P) = y - lam x - nu; E given by ellinit over Q, T = [xT, yT] with entries in L (polmods)
{ftan(E, T, P) = my(xT = T[1], yT = T[2], lam, nu);
  lam = (3*xT^2 + 2*E.a2*xT + E.a4 - E.a1*yT) / (2*yT + E.a1*xT + E.a3);
  nu = yT - lam*xT; P[2] - lam*P[1] - nu;}
\\ Weierstrass cubic of E (homogeneous)
wcub(E) = y^2*z + E.a1*x*y*z + E.a3*y*z^2 - x^3 - E.a2*x^2*z - E.a4*x*z^2 - E.a6*z^3;
\\ plane cubic for the class kappa(+-Q): E embedded by L(2O + Q) = <1, x, h>, h = (y - y(-Q))/(x - xQ)
{kummercubic(E, Q) = my(y0 = -Q[2] - E.a1*Q[1] - E.a3, Wp, G, G2);
  Wp = y^2 + E.a1*x*y + E.a3*y - x^3 - E.a2*x^2 - E.a4*x - E.a6;
  G = subst(Wp, y, y0 + y*(x - Q[1])); G2 = G / (x - Q[1]);
  if (type(G2) == "t_RFRAC", error("kummercubic: not divisible"));
  G2 = substvec(G2, [x,y], [x/z, y/z]) * z^3; G2 = G2 / content(G2); G2;}
\\ pencil discriminant quartic: Delta(U + t H) = kappa * Q(t)^3 ; returns [Q, kappa, HU]
{hessequartic(U) = my(HU = hess(U), iv = c46(U + t*HU), D = (iv[1]^3 - iv[2]^2)/1728, fa, Q, k);
  fa = factor(D); Q = prod(i=1, #fa~, fa[i,1]); k = D / Q^3;
  if (poldegree(k, t) != 0 || type(k) == "t_RFRAC", error("pencil discriminant not kappa*Q^3: ", fa));
  [Q, k, HU];}
\\ Cardano class of a squarefree binary cubic g(s) over L: returns c with L[s]/g = L[z]/(z^3 - c)
{cardano(nf, g) = my(a = polcoef(g,3,s), b = polcoef(g,2,s), c1 = polcoef(g,1,s), d = polcoef(g,0,s), p, q, D, r, cc);
  b /= a; c1 /= a; d /= a;
  p = c1 - b^2/3; q = 2*b^3/27 - b*c1/3 + d;
  D = -4*p^3 - 27*q^2; if (D == 0, error("cardano: repeated root"));
  r = nfroots(nf, X^2 + D/3); if (#r == 0, error("cardano: -disc/3 not a square in L"));
  cc = -q/2 + r[1]/6; if (cc == 0, cc = -q/2 - r[1]/6); cc;}
\\ class image of a plane cubic U (over Q). Returns [c, t0, line] ; t0 = oo encoded as "oo"
{classimg_cubic(nf, U) = my(QkH = hessequartic(U), Q = QkH[1], HU = QkH[3], rt, F, g, A, B, tries = 0);
  rt = nfroots(nf, Q);
  if (poldegree(Q, t) == 4,
     if (#rt != 1, error("expected exactly one L-root of the Hesse quartic, got ", #rt)); F = U + rt[1]*HU,
     if (#rt != 0, error("Q has degree < 4 and an L-root")); F = HU; rt = ["oo"]);
  A = [1,0,0]; B = [0,1,0];
  while (1, g = substvec(F, [x,y,z], [s*A[1]+B[1], s*A[2]+B[2], s*A[3]+B[3]]);
    if (poldegree(g, s) == 3 && poldisc(g) != 0, break);
    tries++; A = vector(3,i,random(11)-5); B = vector(3,i,random(11)-5));
  [cardano(nf, g), rt[1], [A, B]];}
\\ cube test in L and comparison up to inversion
iscubeL(nf, c) = #nfroots(nf, X^3 - c) > 0;
samecls(nf, c1, c2) = iscubeL(nf, c1/c2) || iscubeL(nf, c1*c2);
