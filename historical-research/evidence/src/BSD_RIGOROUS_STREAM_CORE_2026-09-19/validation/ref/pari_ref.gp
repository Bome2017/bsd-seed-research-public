\\ PARI reference values (numerical, not proofs): L''(E,1)/2 for the l2 validation, periods for all validation curves.
default(realprecision, 45);
C = [["37a1",[0,0,1,-1,0]],["389a1",[0,1,1,-2,0]],["446d1",[1,-1,0,-4,4]],["234446a1",[1,-1,0,-79,289]],["15a1",[1,1,1,-10,-10]],["24a1",[0,-1,0,-4,4]],["57b1",[1,0,1,-7,5]],["141a1",[0,1,1,-12,2]],["141d1",[0,-1,1,-1,0]]];
for(i = 1, #C, my(E = ellinit(C[i][2])); print("PER ", C[i][1], " N ", ellglobalred(E)[1], " w ", ellrootno(E), " a3 ", ellap(E, 3), " disc_sign ", sign(E.disc), " omega1 ", E.omega[1], " omega2_im ", imag(E.omega[2]), " omega2_re ", real(E.omega[2])));
L = [["389a1",[0,1,1,-2,0]],["446d1",[1,-1,0,-4,4]],["234446a1",[1,-1,0,-79,289]]];
for(i = 1, #L, my(E = ellinit(L[i][2])); print("L2HALF ", L[i][1], " ", lfun(E, 1, 2)/2, "  L(E,1) ", lfun(E, 1), "  analytic_rank ", ellanalyticrank(E)[1]));
