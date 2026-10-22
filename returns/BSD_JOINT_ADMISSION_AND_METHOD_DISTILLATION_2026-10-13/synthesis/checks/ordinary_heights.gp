\\ Fresh canonical ordinary regulator; numerator never passed to this script.
E=ellinit([0,-1,0,-66020924,-65074271436]);G=[[-3031,327384],[-2394,281520]];
for(i=1,4,p=[5,7,11,13][i]; R=ellpadicregulator(E,p,8,G); LG=log(1+p+O(p^10)); RU=R/LG^2; ap=ellap(E,p); print("ROW p=",p," ap=",ap," valuation=",valuation(RU,p)," residue=",lift(Mod(lift(RU),p))," R_U=",RU));
print("DONE");
