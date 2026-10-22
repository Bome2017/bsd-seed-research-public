\\ Independent unconditional 2-descent (PARI ellrank) for the seed and its 2-isogenous curve; exact lower-bound images.
E = ellinit([0,-22735,0,106272484,0]);
print("conductor ", ellglobalred(E)[1]);
print("torsion ", elltors(E)[1..2]);
P1 = [4547,327384]; P2 = [5184,281520];
print("P1,P2 on E: ", ellisoncurve(E,P1), " ", ellisoncurve(E,P2));
r = ellrank(E, 0, [P1,P2]);
print("ellrank(E) [r1,r2,s] = ", r[1..3]);
Ep = ellinit([0,45470,0,91790289,0]);
print("E' torsion ", elltors(Ep)[1..2]);
rp = ellrank(Ep);
print("ellrank(E') [r1,r2,s] = ", rp[1..3]);
\\ 2-isogeny images: alpha(x,y) = x mod squares (x != 0), alpha(T) = b mod squares
sqf(n) = core(numerator(n)) * core(denominator(n));
print("alpha(T)  = ", core(106272484), "   alpha(P1) = ", sqf(P1[1]), "   alpha(P2) = ", sqf(P2[1]));
print("alpha'(T') = ", core(91790289));
L = rp[4]; for(i=1,#L, print("alpha'(E' point ", i, ") = ", sqf(L[i][1])));
