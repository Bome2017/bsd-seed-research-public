\\ Independent numerical check of G2(x) = int_1^oo exp(-x y) log(y) dy/y by PARI quadrature (not a proof; cross-check of arbcore g2t).
default(realprecision, 50);
G2(x) = intnum(y = 1, [oo, x], exp(-x*y)*log(y)/y);
v = [1/1000, 1/10, 1, 7/2, 10, 35/3];
for(i = 1, #v, print("PARI G2(", v[i], ") = ", G2(v[i])));
