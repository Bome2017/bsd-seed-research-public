\\ K288 custody audit, part 2 (Claude, 2026-10-06). Fresh code: does not read mt_prescreen/tame_reg.gp.
\\ Tame height on Q = O mod l, Q in E0 at every bad prime, x = a/d^2, y = b/d^3 in lowest terms:
\\   h(Q) = ind_g(-a/b mod l) mod p.  Gram = [[h1, b12],[b12, h2]], b12 = (h(Q1+Q2) - h1 - h2)/2.
\\   R(p,l) = det Gram(M.P1, M.P2) / M^4 mod p.
\\ M here = cexp * exponent(E(F_l)), a different multiplier from tame_reg.gp (cexp * lcm of generator orders),
\\ so agreement with the frozen prescreen values also checks the M^4 scaling.
\\ Extra rows at p = 5 and p = 3 (sealed predictions; c2 not yet computed when this ran).

E = ellinit([0,-1,0,-66020924,-65074271436]);
G = [[-3031,327384],[-2394,281520]];
gr = ellglobalred(E);
cexp = lcm(vector(#gr[4][,1], i, elllocalred(E, gr[4][i,1])[4]));
print("CURVE conductor=", gr[1], " tamagawa_product=", gr[3], " cexp=", cexp, " torsion=", elltors(E)[1..2]);
print("GENS on curve: ", [ellisoncurve(E, G[1]), ellisoncurve(E, G[2])]);
print("REG (real, PARI ellheightmatrix) = ", matdet(ellheightmatrix(E, G)));
S50 = ellsaturation(E, G, 50);
print("SATURATION B=50 index^2 = ", round(matdet(ellheightmatrix(E, G)) / matdet(ellheightmatrix(E, S50))));

lpr(l) = my(f = factor(l - 1)[,1]); for(g = 2, l - 1, if(vecmin(vector(#f, i, Mod(g, l)^((l-1)/f[i]) != 1)), return(g)));
lpr2(l) = my(f = factor(l - 1)[,1], k = 0); for(g = 2, l - 1, if(vecmin(vector(#f, i, Mod(g, l)^((l-1)/f[i]) != 1)), k++; if(k == 2, return(g))));

th(Q, l, p, g) =
{
  my(x = Q[1], y = Q[2], D = denominator(x), d = sqrtint(D), a, b);
  if (d^2 != D, error("x denominator not a square"));
  if (d % l, error("point not in the kernel of reduction at l"));
  if (denominator(y) != d^3, error("y denominator is not d^3"));
  a = numerator(x); b = numerator(y);
  lift(znlog(Mod(-a, l) / Mod(b, l), Mod(g, l))) % p;
}

row(p, l, gexp) =
{
  my(El = ellinit(E, l), Nl = ellcard(El), al = ellap(E, l), ex = ellgroup(El)[1], M, Q1, Q2, S, D2, g, g2, out = []);
  if (lpr(l) != gexp, error("least primitive root differs from the c2 run"));
  M = cexp * ex;
  if (M % p == 0 || Nl % p == 0, error("p divides M or #E(F_l)"));
  Q1 = ellmul(E, G[1], M); Q2 = ellmul(E, G[2], M); S = elladd(E, Q1, Q2); D2 = ellsub(E, Q1, Q2);
  foreach([lpr(l), lpr2(l)], gg,
    my(h1 = th(Q1, l, p, gg), h2 = th(Q2, l, p, gg), hs = th(S, l, p, gg), hdf = th(D2, l, p, gg), b12, b12alt, dM, dE);
    b12 = Mod(hs - h1 - h2, p) / 2; b12alt = Mod(hs - hdf, p) / 4;
    if (b12 != b12alt, error("polarization identities disagree"));
    dM = Mod(h1, p) * h2 - b12^2; dE = dM / Mod(M, p)^4;
    out = concat(out, [[gg, h1, h2, lift(b12), lift(dM), lift(dE)]]));
  print("ROW p=", p, " l=", l, " #E(F_l)=", Nl, " a_l=", al, " M=", M, " data=", out);
}

row(5, 191, 19);
row(5, 311, 17);
row(3, 103, 5);
print("DONE");
