\\ local4547.gp -- local data at p = 4547 for BOTH curves of the isogeny class of the seed (2243,12).
\\ Needed for Edixhoven [Edi91, Thm 3] as summarized in CNS 1911.09446v3 Sec. 1: p >= 11 and NOT (additive AND potentially ordinary AND Kodaira type II/III/IV)  ==>  p does not divide c.
\\ PARI Kodaira codes: II=2, III=3, IV=4, I0*=-1, II*=-2, III*=-3, IV*=-4, I_n = 4+n.
p = 4547; E = ellinit([0,-22735,0,106272484,0]);
\\ ellisomat entries are [[a4,a6], isogeny, dual]
M = ellisomat(E); L = M[1]; print("isogeny class size = ", #L, " ; isogeny degree matrix = ", M[2]);
kname(k) = if(k==2,"II",k==3,"III",k==4,"IV",k==-1,"I0*",k==-2,"II*",k==-3,"III*",k==-4,"IV*",k==1,"I0",k>4,Str("I",k-4),Str("I",-k-4,"*"));
for(i = 1, #L, my(Ei = ellinit(L[i][1]), Em = ellminimalmodel(Ei), lr = elllocalred(Em, p), jm = Mod(numerator(Em.j), p)/Mod(denominator(Em.j), p)); print("curve ", i, ": [a1,a2,a3,a4,a6]_min = ", [Em.a1,Em.a2,Em.a3,Em.a4,Em.a6], " ; conductor exponent f_p = ", lr[1], " ; Kodaira = ", kname(lr[2]), " ; v_p(Delta_min) = ", valuation(Em.disc, p), " ; v_p(j) = ", valuation(Em.j, p), " (>= 0: potentially good) ; j mod p = ", lift(jm), " ; conductor = ", ellglobalred(Em)[1]));
print("p mod 4 = ", p % 4, " ; a_p(y^2 = x^3 + x) = ", ellap(ellinit([0,0,0,1,0]), p), " ; a_p(y^2 = x^3 - x) = ", ellap(ellinit([0,0,0,-1,0]), p), "  (a_p = 0 <=> supersingular for p >= 5)");
print("ellcard over F_p of the two j=1728 forms: ", [ellcard(ellinit([0,0,0,1,0], p)), ellcard(ellinit([0,0,0,-1,0], p))], " (p + 1 = ", p + 1, ")");
\\ supersingularity is geometric: check also a j=1728 curve over F_{p^2}: #E(F_{p^2}) = p^2 + 1 + 2p for a supersingular curve with a_p = 0
print("a_{p^2} check: #E(F_{p^2}) for y^2 = x^3 + x = ", ellcard(ellinit([0,0,0,1,0], ffgen(p^2))), " vs (p+1)^2 = ", (p+1)^2);
