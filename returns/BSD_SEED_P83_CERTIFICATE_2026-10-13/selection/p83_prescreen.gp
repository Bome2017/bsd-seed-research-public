read("/Users/bsm/BSD_P17_PREREQUISITES_2026-09-25/singleton_probe/mt_prescreen/tame_reg.gp");
E=ellinit([0,-1,0,-66020924,-65074271436]);
P=[[-3031,327384],[-2394,281520]];
r=tamereg(E,P,167,83,compexp(E));
print(r);
print("R_E=",lift(Mod(r[9],83)/Mod(r[5],83)^4));
quit;
