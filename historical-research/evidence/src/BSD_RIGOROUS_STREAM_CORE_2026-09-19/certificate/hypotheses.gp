\\ Exact (algebraic) inputs of the analytic-rank certificate; PARI 2.17.x.  One statement per line.
default(realprecision, 40);
E = ellinit([0,-22735,0,106272484,0]);
G = ellglobalred(E); print("CONDUCTOR ", G[1], " = ", factor(G[1]));
print("ROOT_NUMBER ", ellrootno(E));
print("DISC ", E.disc, " sign ", sign(E.disc), " factored ", factor(E.disc));
print("MINIMAL_MODEL_CHANGE ", ellminimalmodel(E, &ch), " via [u,r,s,t] = ", ch);
print("TORSION ", elltors(E));
P1 = [4547, 327384]; P2 = [5184, 281520];
print("ON_CURVE ", ellisoncurve(E, P1), " ", ellisoncurve(E, P2));
print("HEIGHTS ", ellheight(E, P1), " ", ellheight(E, P2));
print("REGULATOR(P1,P2) ", matdet(ellheightmatrix(E, [P1, P2])));
print("ORDER_P1_IS_INFINITE ", ellorder(E, P1) == 0);
P = G[4][,1]; print("a_3 = ", ellap(E, 3), "  local root numbers at ", P~, ": ", vector(#P, i, ellrootno(E, P[i])));
