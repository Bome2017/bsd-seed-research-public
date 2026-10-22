E=ellinit([0,-1,0,-66020924,-65074271436]);
P1=[-3031,327384];P2=[-2394,281520];
if(!ellisoncurve(E,P1)||!ellisoncurve(E,P2),error("basis input not on curve"));
print("SCAN_BOUND=30000; COEFFICIENT_PRIME=5");
found=0;
forprime(q=2,30000,if(q==5||E.disc%q==0,next);Eq=ellinit([0,-1,0,-66020924,-65074271436],q);n=ellcard(Eq);if(valuation(n,5)!=1,next);h=n/5;A=ellmul(Eq,P1,h);B=ellmul(Eq,P2,h);print([q,n,h,lift(A),lift(B)]);if(A==[0]&&B==[0],found=q;break));
print("FIRST_HIT=",found);
print("DONE");
