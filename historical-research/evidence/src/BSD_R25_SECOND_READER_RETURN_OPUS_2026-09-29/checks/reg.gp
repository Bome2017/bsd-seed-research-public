E=ellinit([0,-1,0,-66020924,-65074271436]); P1=[-3031,327384]; P2=[-2394,281520];
print("on curve: ", ellisoncurve(E,P1), ellisoncurve(E,P2), "  a3=", ellap(E,3), "  kodaira3=", elllocalred(E,3));
iferr(print("h_3(P1) = ", ellpadicheight(E,3,8,P1)), err, print("ellpadicheight error: ", err));
iferr(R=ellpadicregulator(E,3,8,[P1,P2]); print("Reg_3 = ", R, "  v3 = ", valuation(R,3)), err, print("ellpadicregulator error: ", err));
print("v3(log_3 4)^2 -> ", 2*valuation(log(4+O(3^10)),3));
