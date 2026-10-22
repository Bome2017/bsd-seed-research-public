read("scripts/s04b_enum_lib.gp");
default(realprecision,50);
H=11.0;
t=getabstime(); r=enumpts(H); print("enumpts(",H,"): ",#r[1]," points (up to sign) ; raw quartic points ",r[2],"  ms=",getabstime()-t);
print(r[1]);
t=getabstime(); b=brute(H); print("brute(",H,"): ",#b," points (with signs) ms=",getabstime()-t);
b2=Set(apply(P->[P[1],abs(P[2])],b)); print(b2);
print("agree: ",b2==r[1]);
