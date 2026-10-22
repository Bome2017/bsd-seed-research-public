\\ N5 robustness: does ord_5 of PARI's 5-adic regulator of <P1,P2> depend on the Weierstrass model (translations x -> x + r)?
m=2243; n=12; A=m+16*n^2; B=m+25*n^2; E=ellinit([0,-5*A,0,4*A*B,0]); P1=[A,6*n*A]; P2=[36*n^2,12*n*(m-2*n^2)];
print("seed model b2 = ", E.b2, "  truncate(b2/12) = ", truncate(E.b2/12));
R0=ellpadicregulator(E,5,12,[P1,P2]); print("r=0: Reg5 = ", R0, "  ord5 = ", valuation(R0,5));
for(r=-3,3, if(r!=0, v=[1,r,0,0]; Er=ellchangecurve(E,v); Q=ellchangepoint([P1,P2],v); Rr=ellpadicregulator(Er,5,12,Q); print("r=",r,": b2=",Er.b2,"  ord5 Reg5 = ", valuation(Rr,5), "  (Rr-R0) ord5 = ", valuation(Rr-R0,5))));
rr=-truncate(E.b2/12); v=[1,rr,0,0]; Er=ellchangecurve(E,v); Q=ellchangepoint([P1,P2],v); Rr=ellpadicregulator(Er,5,12,Q); print("r=",rr," (b2 ~ 0 model): b2=",Er.b2,"  ord5 Reg5 = ", valuation(Rr,5), "  (Rr-R0) ord5 = ", valuation(Rr-R0,5));
Em=ellminimalmodel(E,&vm); Qm=ellchangepoint([P1,P2],vm); Rm=ellpadicregulator(Em,5,12,Qm); print("minimal model (u=",vm[1],"): ord5 Reg5 = ", valuation(Rm,5), "  (Rm-R0) ord5 = ", valuation(Rm-R0,5));
L1=ellpadiclog(E,5,12,ellmul(E,P1,8))/8; L2=ellpadiclog(E,5,12,ellmul(E,P2,8))/8; print("ord5 log P1, log P2 = ", [valuation(L1,5), valuation(L2,5)]);
H=matrix(2,2,i,j,0); print("done");
