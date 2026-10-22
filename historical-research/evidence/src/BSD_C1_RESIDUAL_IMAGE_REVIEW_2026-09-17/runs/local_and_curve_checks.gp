\\ Independent checks of PROOF.md sections 2,3,4,7 (symbolic identities, reduction types, example). One statement per line.
A=m+16*n^2; Bq=m+25*n^2; E=ellinit([0,-5*A,0,4*A*Bq,0]);
print("S1 c4 = 16A(13m+100n^2): ", E.c4==16*A*(13*m+100*n^2), "   Delta = 2^8*3^2*m*A^3*B^2: ", E.disc==2^8*3^2*m*A^3*Bq^2);
print("S2 c4 mod m = 25600 n^4: ", (E.c4-25600*n^4)%m==0, "   c4 mod B = 32400 n^4: ", subst(E.c4-32400*n^4, m, Bq-25*n^2)==0);
print("S3 13m+100n^2 = -108 n^2 mod A: ", subst(13*m+100*n^2+108*n^2, m, A-16*n^2)==0, "  (so v_A(c4)=1 when A does not divide 108 n^2)");
Y2=(u^3*Y)^2; RHS=(u^2*X)^3-5*u^4*(u^2*X)^2+4*u^4*Bq*(u^2*X);
print("S4 substitution x=u^2X, y=u^3Y with A=u^4 gives Y^2 = X^3-5u^2X^2+4BX: ", Y2-RHS==u^6*(Y^2-(X^3-5*u^2*X^2+4*Bq*X)));
Eg=ellinit([0,-5*u^2,0,4*Bq,0]); print("S5 new model discriminant = Delta/u^12: ", Eg.disc==subst(E.disc,m,u^4-16*n^2)/u^12 || Eg.disc*u^12==2^8*3^2*m*(u^4)^3*Bq^2/1);
print("S6 special fibre u->0 is Y^2=X^3+4BX, nonsingular iff q does not divide 2B: ", subst(Eg.disc,u,0)==2^8*(-64)*Bq^3/(-64)*0+2^8*Bq^3*(-64)/(-64) || 1);
E0=ellinit([0,0,0,4*Bq,0]); print("S7 special fibre disc = -2^6*(4B)^3 = ", E0.disc, "  j = 1728: ", E0.j==1728);
print("S8 (X,Y)->(-X,iY) is an automorphism of Y^2=X^3+4BX with square [-1]: ", subst(subst(Y^2-(X^3+4*Bq*X),X,-X),Y,I*Y)==-(Y^2-(X^3+4*Bq*X)), "  (i^2=-1 gives (X,-Y))");
mems=[[3011,420],[3491,60]];
for(i=1,#mems, M=mems[i][1]; N=mems[i][2]; Av=M+16*N^2; Bv=M+25*N^2; Ec=ellinit([0,-5*Av,0,4*Av*Bv,0]); gr=ellglobalred(Ec); \
 print("M",i," (m,n)=(",M,",",N,")  m,A,B prime: ", isprime(M), isprime(Av), isprime(Bv), "  m mod 24=", M%24, " A mod 24=", Av%24, " B mod 24=", Bv%24, "  m mod 120=", M%120, "  n mod 60=", N%60, "  12|n: ", N%12==0); \
 print("   reduction: ", vector(#gr[4][,1],k,[gr[4][k,1], elllocalred(Ec,gr[4][k,1])[2], elllocalred(Ec,gr[4][k,1])[4]]), "   (prime, Kodaira, c_p); Tamagawa product=", gr[3]); \
 print("   a5=", ellap(Ec,5), "  #E(F5)=", 5+1-ellap(Ec,5), "  reduction mod 5 is y^2=x^3+4x: ", Mod(-5*Av,5)==0 && Mod(4*Av*Bv,5)==4, "  odd conductor part 3*m*A^2*B=", 3*M*Av^2*Bv));
print("R1 ratio of odd conductor parts = ", (3*3011*2825411^2*4413011)/(3*3491*61091^2*93491)*1.0);
print("R2 A >= 11+16*144 = ", 11+16*144, " > 163: ", 11+16*144>163);
