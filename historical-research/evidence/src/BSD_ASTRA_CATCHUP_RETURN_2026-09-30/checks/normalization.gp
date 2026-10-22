E=ellinit([0,-1,0,-66020924,-65074271436]);
P1=[-3031,327384]; P2=[-2394,281520];
print("ON_CURVE ",ellisoncurve(E,P1)," ",ellisoncurve(E,P2));
print("A3 ",ellap(E,3));
forstep(n=8,14,3,R=ellpadicregulator(E,3,n,[P1,P2]); print("PREC ",n," REG ",R," VREG ",valuation(R,3)," VLOG ",valuation(log(4+O(3^(n+4))),3)," VNORMALIZED ",valuation(R/log(4+O(3^(n+4)))^2,3)));
print("V5843 ",valuation(1+1/5843,3));
print("VA2 ",valuation(15480,3)," ",valuation(7740,3));
quit;
