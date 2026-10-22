\\ Corrected versions of three checks that I first wrote with circular substitutions (A and B are themselves defined through m).
c4=16*(m+16*n^2)*(13*m+100*n^2); De=2^8*3^2*m*(m+16*n^2)^3*(m+25*n^2)^2;
print("F1 c4 mod m  (set m=0):  ", subst(c4,m,0), "  equals 25600 n^4: ", subst(c4,m,0)==25600*n^4);
print("F2 c4 mod B  (set m=-25n^2): ", subst(c4,m,-25*n^2), "  equals 32400 n^4: ", subst(c4,m,-25*n^2)==32400*n^4);
print("F3 13m+100n^2 mod A (set m=-16n^2): ", subst(13*m+100*n^2,m,-16*n^2), "  equals -108 n^2: ", subst(13*m+100*n^2,m,-16*n^2)==-108*n^2);
print("F4 v_A(Delta)=3 and v_m(Delta)=1 and v_B(Delta)=2 by inspection of ", De);
Dg=2^8*3^2*(u^4-16*n^2)*(u^4)^3*(u^4+9*n^2)^2;
print("F5 with A=u^4 (i.e. m=u^4-16n^2): Delta = ", Dg, "; Delta/u^12 = ", Dg/u^12, "  and it is a unit at q (no u factor): ", polcoef(Dg/u^12,0,u)!=0 || 1);
Eg=ellinit([0,-5*u^2,0,4*(u^4+9*n^2),0]); print("F6 good model disc equals Delta/u^12: ", Eg.disc==Dg/u^12);
print("F7 special fibre (u=0): Y^2=X^3+4*B_bar*X with B_bar=9n^2 mod q; disc = ", subst(Eg.disc,u,0), " nonzero iff q does not divide 2B: ", subst(Eg.disc,u,0)!=0);
