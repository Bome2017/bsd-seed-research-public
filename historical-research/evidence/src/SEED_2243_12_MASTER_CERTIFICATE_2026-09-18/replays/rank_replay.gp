m=2243; n=12; A=m+16*n^2; B=m+25*n^2;
E=ellinit([0,-5*A,0,4*A*B,0]);
r=ellrank(E); print("ELLRANK [r,R,s,L] r,R,s = ", r[1..3], "  points found: ", #r[4]);
P1=[A,6*n*A]; P2=[36*n^2,12*n*(m-2*n^2)];
H=ellheightmatrix(E,[P1,P2]); print("NT height matrix det (regulator of <P1,P2>) = ", matdet(H));
print("torsion = ", elltors(E)[1..2]);
S=ellsaturation(E,[P1,P2],50); print("saturation at primes <= 50 returns (same as input up to sign?): ", S, "  reg ratio = ", matdet(ellheightmatrix(E,S))/matdet(H));
