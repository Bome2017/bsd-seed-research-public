\\ Search side (GRH allowed): Schaefer-Stoll 3-Selmer group of E inside L^x/L^x3, L = Q(T).
\\ Needs cubinv.gp, classimg.gp. Variable order x>y>z>..>t>s>X>w.
rhs2(E, xx) = 4*xx^3 + E.b2*xx^2 + 2*E.b4*xx + E.b6;   \\ (2y+a1x+a3)^2
{field3(E) = my(N = ellglobalred(E)[1], ps = Set(concat(factor(3*N)[,1]~, [])), g, fl);
  g = polresultant(elldivpol(E, 3), X^2 - rhs2(E, x), x);
  g = g / content(g); if (!polisirreducible(g) || poldegree(g) != 8, error("field3: rho-bar_3 not transitive on E[3]-{0}"));
  fl = polredbest([g, ps]); [subst(fl, X, w), ps];}
\\ T = [xT, yT] in L (polmods); unique root of psi_3 in L is asserted
{torsT(E, nf) = my(xs = nfroots(nf, subst(elldivpol(E,3), x, X)), xT, us, uT);
  if (#xs != 1, error("torsT: psi3 has ", #xs, " roots in L"));
  xT = xs[1]; us = nfroots(nf, X^2 - rhs2(E, xT)); uT = us[1];
  [xT, (uT - E.a1*xT - E.a3)/2];}
\\ local data at a prime ideal: [pr, n, bid, pi]
{locdata(nf, pr) = my(p = pr.p, e = pr.e, n = if (p == 3, floor(3*e/2) + 1, 1), bid, pi);
  bid = idealstar(nf, idealpow(nf, pr, n), 1);
  pi = if (e == 1, p, nfbasistoalg(nf, pr.gen[2]));
  if (nfeltval(nf, pi, pr) != 1, pi = nfbasistoalg(nf, pr.gen[2]) + p; if (nfeltval(nf, pi, pr) != 1, error("locdata: no uniformizer")));
  [pr, n, bid, pi];}
{locvec1(nf, a, D) = my(v = nfeltval(nf, a, D[1]), u = a / D[4]^v, lg = ideallog(nf, u, D[3]), cyc = D[3].cyc, out = [v % 3]);
  for (i = 1, #cyc, if (cyc[i] % 3 == 0, out = concat(out, [lg[i] % 3]))); out;}
\\ a may be a famat [elts, exps] (matrix) or an element
{locvec(nf, a, D) = if (type(a) == "t_MAT", my(r = 0); for (i = 1, #a~, r += a[i,2] * locvec1(nf, nfbasistoalg(nf, a[i,1]), D)); r % 3, locvec1(nf, a, D));}
\\ y-roots of E over Q_l at x (x in Q), precision k: returns list of [x, y] with y a t_PADIC
{ptsatx(E, l, x0, k) = my(m = max(0, -valuation(x0, l)), mm, X0, pol, rts);
  if (m % 2, return([])); mm = m/2; X0 = x0 * l^(2*mm);
  pol = X^2 + E.a1*X0*X*l^mm + E.a3*X*l^(3*mm) - (X0^3 + E.a2*X0^2*l^(2*mm) + E.a4*X0*l^(4*mm) + E.a6*l^(6*mm));
  rts = polrootspadic(pol, l, k); vector(#rts, i, [x0, rts[i] / l^(3*mm)]);}
\\ rational approximation of a p-adic number
padtoq(u) = my(v = valuation(u, u.p)); if (u == 0, 0, lift(u * u.p^(-v) ) * u.p^v);
\\ local Kummer image at the rational prime l: returns [B (F3 matrix, columns = images), expected dim]
{lockummer(E, nf, T, l, Dl, k) = my(d = 1 + sum(i = 1, #Dl, Dl[i][1].e == 1 && Dl[i][1].f == 1), dimexp, B = [;], xs, P, img, sing = [], tries = 0);
  dimexp = round(log(d)/log(3)) + (l == 3); if (3^(dimexp - (l==3)) != d, error("lockummer: #E(Q_l)[3] not a power of 3"));
  \\ singular x mod l (for odd l: double roots of rhs2 mod l)
  if (l > 2, my(r2 = Mod(1,l)*rhs2(E, X)); sing = [lift(r) | r <- polrootsmod(gcd(r2, deriv(r2)), l)], sing = [0, 1]);
  while (matrank(B) < dimexp && tries < 4000, tries++;
    my(c = random(6), x0);
    x0 = if (c == 0, random(l^6), c == 1, if (#sing, sing[random(#sing)+1], 0) + l^(1+random(5))*random(l^4),
          c == 2, (random(l^6)+1) / l^(2*(1+random(3))), c == 3, random(l), c == 4, (1+random(l^2)) / l^2, if (#sing, sing[1+random(#sing)], 0) + l*random(l^3));
    xs = ptsatx(E, l, x0, k);
    for (j = 1, #xs, P = [xs[j][1], padtoq(xs[j][2])];
      my(fv = ftan(E, T, P)); if (fv == 0, next);
      my(Ny=padicprec(xs[j][2],l), margin=vector(#Dl,q,Dl[q][1].e*Ny-nfeltval(nf,fv,Dl[q][1])-Dl[q][2]));
      if(vecmin(margin)<0,next);
      img = concat(vector(#Dl, i, locvec(nf, fv, Dl[i])));
      if(type(LPRECLOG)=="t_LIST",listput(LPRECLOG,[l,xs[j][1],P[2],Ny,vector(#Dl,q,[Dl[q][1].e,nfeltval(nf,fv,Dl[q][1]),Dl[q][2],margin[q]]),img]));
      B = if (#B == 0, Mat(Mod(img, 3)~), concat(B, Mod(img, 3)~))));
  if (matrank(B) != dimexp, error("lockummer: rank ", matrank(B), " != expected ", dimexp, " at l=", l));
  [matimage(B), dimexp];}
\\ generators of L(S,3): S-units + fundamental units (bnfunits) + Cl_S[3] lifts. Returns list (elements or famats)
{lsgens(bnf, SL) = my(nf = bnf.nf, BU = bnfunits(bnf, SL)[1], G, ClS, cyc, lp, c, c3, lc, e, a, beta);
  G = vector(#BU - 1, i, BU[i]);
  ClS = bnfsunit(bnf, SL)[5];
  lp = matconcat(vector(#SL, j, bnfisprincipal(bnf, SL[j], 0)));
  for (i = 1, #ClS[2], if (ClS[2][i] % 3 == 0,
     c = idealpow(nf, ClS[3][i], ClS[2][i]/3); c3 = idealpow(nf, c, 3);
     lc = bnfisprincipal(bnf, c3, 0);
     e = if (#bnf.cyc, matsolvemod(lp, bnf.cyc~, lc), vector(#SL,j,0)~);
     if (e == 0, error("lsgens: class of c^3 not in <S>"));
     a = c3; for (j = 1, #SL, a = idealmul(nf, a, idealpow(nf, SL[j], -e[j])));
     beta = bnfisprincipal(bnf, a, 1);
     if (beta[1] != 0*beta[1], error("lsgens: not principal"));
     G = concat(G, [nfbasistoalg(nf, beta[2])])));
  G;}
\\ auxiliary cubic residue symbol map at degree-1 primes (search-side injectivity heuristic)
{auxprimes(fL, m, avoid) = my(res = List(), p = 7);
  while (#res < m, p = nextprime(p+1); if (p % 3 != 1 || setsearch(avoid, p) || poldisc(fL) % p == 0, next);
    my(rs = polrootsmod(fL, p)); for (i = 1, #rs, if (#res < m, listput(res, [p, lift(rs[i]), znprimroot(p)^((p-1)/3)]))));
  Vec(res);}
{cr3(a, pr) = my(p = pr[1], v = Mod(subst(lift(a), w, pr[2]), p), u, om = pr[3]);
  if (v == 0, error("cr3: not a unit")); u = v^((p-1)/3); if (u == 1, 0, u == om, 1, u == om^2, 2, error("cr3"));}
crvec(nf, a, AP) = if (type(a) == "t_MAT", sum(i=1,#a~, a[i,2]*crvec(nf, nfbasistoalg(nf, a[i,1]),AP)) % 3, vector(#AP, i, cr3(a, AP[i])));
\\ main: returns [Sel basis as F3 exponent vectors, gens, dims]
{selmer3(E, bnf, T, ps, k, relax = []) = my(nf = bnf.nf, SL = [], G, rows = [;], info = []);
  for (i = 1, #ps, SL = concat(SL, idealprimedec(nf, ps[i])));
  G = lsgens2(bnf, SL, if (type(LG) == "t_STR", LG, ""));
  G = vector(#G, j, redcube(nf, G[j])); if (type(LG) == "t_STR", write(LG, ["generators reduced mod cubes; max log10 numerator", vecmax(vector(#G, j, round(log(1+vecmax(abs(Vec(lift(G[j])))))/log(10))))]));
  for (i = 1, #ps, my(l = ps[i], Dl, Bl, Ml, Kl);
    Dl = [locdata(nf, pr) | pr <- idealprimedec(nf, l)];
    if (setsearch(Set(relax), l), info = concat(info, [[l, #Dl, "relaxed", 0, 0]]); next);
    Bl = lockummer(E, nf, T, l, Dl, k); if (type(LG) == "t_STR", write(LG, ["local Kummer image done at l =", l, "dim", Bl[2]]));
    Ml = matconcat(vector(#G, j, Mod(concat(vector(#Dl, q, locvec(nf, G[j], Dl[q]))), 3)~));
    Kl = if(Bl[2] == 0, matid(#Ml~), matker(Bl[1]~)~);
    info = concat(info, [[l, #Dl, Bl[2], #Ml~, if (#Kl, Kl*Ml, 0)]]);
    if (#Kl, rows = if (#rows, matconcat([rows; Kl*Ml]), Kl*Ml)));
  [matker(rows), G, info];}
\\ flatten element/famat into list of [elt, exponent]
flat(nf, a) = if (type(a) == "t_MAT", vector(#a~, i, [nfbasistoalg(nf, a[i,1]), a[i,2]]), [[a, 1]]);
\\ Phi-matrix (F3) of a list of elements (or famats) at aux primes; primes where some element is a non-unit are dropped
{phimat(nf, elts, AP) = my(cols = List(), fl = vector(#elts, j, flat(nf, elts[j])));
  for (q = 1, #AP, my(ok = 1, r = vector(#elts));
    for (j = 1, #elts, my(sj = 0);
      for (k = 1, #fl[j], my(e = fl[j][k][1], v); if (denominator(content(lift(e))) % AP[q][1] == 0, ok = 0; break(2));
        v = Mod(subst(lift(e), w, AP[q][2]), AP[q][1]); if (v == 0, ok = 0; break(2));
        sj += fl[j][k][2] * cr3(e, AP[q]));
      r[j] = sj % 3);
    if (ok, listput(cols, r)));
  Mod(matconcat(Vec(cols)~), 3);}
\\ the automorphism tau of L/L4 (T -> -T)
{tauL(nf, E, T) = my(G = nfgaloisconj(nf), mT = -T[2] - E.a1*T[1] - E.a3);
  for (i = 1, #G, my(g = G[i]); if (nfgaloisapply(nf, g, T[1]) == T[1] && nfgaloisapply(nf, g, T[2]) == mT, return(g)));
  error("tauL: not found");}
tauapply(nf, g, a) = if (type(a) == "t_MAT", matconcat([vector(#a~, i, nfgaloisapply(nf, g, nfbasistoalg(nf, a[i,1])))~, a[,2]]), nfgaloisapply(nf, g, a));
\\ additivity (linearity) rows at primes p splitting completely in L: S -> chi_p(alpha_S) must be a homomorphism E[3] -> F3
{linrows(E, nf, T, G, np, avoid) = my(fL = nf.pol, rows = List(), p = 7, got = 0, fl = vector(#G, j, flat(nf, G[j])));
  while (got < np, p = nextprime(p+1); if (p % 3 != 1 || setsearch(avoid, p) || poldisc(fL) % p == 0, next);
    my(rs = polrootsmod(fL, p)); if (#rs != 8, next);
    my(Ep = ellinit(E, p), pts, chi, om = znprimroot(p)^((p-1)/3), ok = 1);
    iferr(pts = vector(8, i, [subst(lift(lift(T[1])), w, rs[i]), subst(lift(lift(T[2])), w, rs[i])]), er, ok = 0); if (!ok, next);
    \\ chi[i][j] = cubic residue symbol of generator j at root i
    chi = vector(8, i, vector(#G, j, my(sm = 0); for (k = 1, #fl[j], my(e = fl[j][k][1], v, u);
        v = iferr(subst(lift(e), w, rs[i]), er, ok = 0; 0); if (!ok || v == 0, ok = 0; break);
        u = v^((p-1)/3); sm += fl[j][k][2] * if (u == 1, 0, u == om, 1, 2)); sm % 3));
    if (!ok, next);
    for (i = 1, 8, for (j = i, 8, my(Q = elladd(Ep, pts[i], pts[j])); if (Q == [0], next);
       my(kq = 0); for (k = 1, 8, if (pts[k] == Q, kq = k)); if (!kq, error("linrows: sum not found"));
       listput(rows, (chi[i] + chi[j] - chi[kq]) % 3)));
    got++);
  Mod(matconcat(Vec(rows)~), 3);}
\\ variant of lsgens without bnfsunit: Cl_S[3] from discrete logs of S-primes in Cl (cheap), lifts via bnfisprincipal
{lsgens2(bnf, SL, LGF) = my(nf = bnf.nf, BU, G, cyc = bnf.cyc, gen = bnf.gen, lp, H, M, S3, out);
  if (LGF != "", write(LGF, "lsgens2: bnfunits start"));
  BU = bnfunits(bnf, SL)[1]; G = vector(#BU - 1, i, BU[i]);
  if (LGF != "", write(LGF, ["lsgens2: bnfunits done, #S-units+units", #G]));
  if (#cyc == 0, return(G));
  lp = matconcat(vector(#SL, j, bnfisprincipal(bnf, SL[j], 0)));
  \\ Cl_S = Z^r / (diag(cyc) + lp); find elements c of Cl whose image in Cl_S has order 3, as exponent vectors
  M = matconcat([matdiagonal(cyc), lp]); H = mathnf(M);
  my(Sn = matsnf(H, 1), U = Sn[1], D = Sn[3]);   \\ U*H*V = D
  for (i = 1, #D, my(d = D[i,i]); if (d % 3 == 0,
      my(ev = (U^-1)[, i] * (d/3), c = idealfactorback(nf, gen, ev), c3 = idealpow(nf, c, 3), lc = bnfisprincipal(bnf, c3, 0), e, a, beta);
      e = matsolvemod(lp, cyc~, lc); if (type(e) == "t_INT" && e == 0, error("lsgens2: c^3 not in <S>"));
      a = c3; for (j = 1, #SL, a = idealmul(nf, a, idealpow(nf, SL[j], -e[j])));
      beta = bnfisprincipal(bnf, a, 5);
      if(beta[1] != 0*beta[1], error("lsgens2: alleged class lift ideal not principal"));
      my(flbeta=flat(nf,beta[2]), betaid=matid(#nf.zk));
      for(j=1,#flbeta,betaid=idealmul(nf,betaid,idealpow(nf,idealhnf(nf,flbeta[j][1]),flbeta[j][2])));
      if(idealhnf(nf,betaid)!=idealhnf(nf,a),error("lsgens2: exact class lift principal ideal mismatch"));
      G = concat(G, [beta[2]])));
  if (LGF != "", write(LGF, ["lsgens2: class lifts done, total gens", #G]));
  G;}
\\ small explicit representative of g modulo L^x3: exponents of the factored form mod 3, then idealredmodpower
{redcube(nf, g) = my(fl = flat(nf, g), a = 1, b);
  for (k = 1, #fl, my(r = fl[k][2] % 3); if (r == 2, r = -1); if (r, a = nfeltmul(nf, a, nfeltpow(nf, fl[k][1], r))));
  a = nfbasistoalg(nf, a); b = idealredmodpower(nf, a, 3);
  Mod(nfbasistoalg(nf, nfeltmul(nf, a, nfeltpow(nf, b, 3))), nf.pol);}
