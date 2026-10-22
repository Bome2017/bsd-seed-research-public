\\ Step 4 route (b): PARI ellrank + ellsaturation + own proved index bound (Silverman 1990 height-difference bound + complete enumeration)
read("scripts/s04b_enum_lib.gp");
default(realprecision,60);
P1=[A,6*n0*A]; P2=[36*n0^2,12*n0*(m0-2*n0^2)]; T=[0,0];
Q1=toR(P1); Q2=toR(P2);
print("P1 on E0: ",ellisoncurve(E0,P1),"  P2 on E0: ",ellisoncurve(E0,P2),"  Q1,Q2 on Er: ",ellisoncurve(Er,Q1)," ",ellisoncurve(Er,Q2));
\\ ---- (i) ellrank ----
t=getabstime(); R0=ellrank(Er); print("ellrank(Er) = [r1,r2,s,L]: ",R0,"   (",getabstime()-t," ms)");
Tr=1; print("2-Selmer rank C = r2 + T + s = ",R0[2]+Tr+R0[3],"   (PARI doc: r2 = C - T - s; T = dim E(Q)[2] = 1)");
R1=ellrank(E0); print("ellrank(E0) = ",R1);
C2=ell2cover(Er); print("#ell2cover(Er) (basis of ELS 2-covers) = ",#C2);
\\ ---- (ii) Silverman 1990 Thm 1.1 bound, BSD normalisation, conservative constant 0.973 ----
hQ(q)=log(max(abs(numerator(q)),abs(denominator(q))));
hinf(q)=log(max(1,abs(q)));
j=Er.j; D=Er.disc; b2=Er.b2;
mu=hQ(D)/12+hinf(j)/12+hinf(b2/12)/2+log(if(b2,2,1))/2;
BS973=2*(hQ(j)/24+mu+0.973); BSup=2*(mu+1.07); BS961=2*(hQ(j)/24+mu+0.961);
print("Silverman: mu(E)=",mu,"  h(j)=",hQ(j),"  h(Delta)=",hQ(D));
print("  h - hhat <= 2(h(j)/24+mu+0.973) = ",BS973,"   [0.961 variant: ",BS961,"];  hhat - h <= 2(mu+1.07) = ",BSup);
\\ ---- (iii) regulator of <P1,P2> ----
M=ellheightmatrix(Er,[Q1,Q2]); Rg=matdet(M);
print("height matrix (Cremona/BSD normalisation) = ",M); print("Reg(P1,P2) = ",Rg);
\\ index n satisfies n^2 = Rg/Reg(E) and Hermite (gamma_2^2 = 4/3): lambda^2 <= (4/3) Reg(E) => n <= (2/sqrt(3)) sqrt(Rg)/lambda
lam0=2.5; Hl=lam0+BS973;
print("lambda0 = ",lam0,"  search naive height (reduced model) <= ",Hl,"  i.e. max(|num x'|,den x') <= ",exp(Hl));
t=getabstime(); r=enumpts(Hl); print("enumeration: ",#r[1]," points up to sign (incl. T), raw quartic points ",r[2],"  (",getabstime()-t," ms)");
hmin=10^9; 
foreach(r[1],P, if(P[2]==0, print("  torsion ",P); next); my(h=ellheight(Er,P)); print("  ",P,"  naive h'=",naiveh(P),"  hhat=",h); hmin=min(hmin,h));
print("min hhat among non-torsion points found = ",hmin);
lam=min(lam0,hmin);
print("PROVED lower bound lambda >= ",lam," (every non-torsion P with hhat(P) < lam0 has naive h' < lam0+B and was enumerated)");
nb=(2/sqrt(3))*sqrt(Rg)/lam; print("index bound n <= (2/sqrt3) sqrt(Reg)/lambda = ",nb);
\\ ---- (iv) PARI ellsaturation as a further check ----
W=ellsaturation(Er,[Q1,Q2],100); print("ellsaturation(Er,[Q1,Q2],100) = ",W,"  Reg(W)/Reg(V) = ",matdet(ellheightmatrix(Er,W))/Rg);
print("ellrank points L expressed: Reg(L) = ",if(#R0[4]==2,matdet(ellheightmatrix(Er,R0[4])),"n/a"));
