\\ Torsion certificate independent of elltors: E(Q)_tors injects into E(F_p) for good p >= 3 (Silverman AEC VII.3.1(b) with e=1 < p-1).
E=ellinit([0,-22735,0,106272484,0]);
L=List(); g=0;
forprime(p=5,60, if(E.disc%p, my(np=ellcard(E,p)); listput(L,[p,np]); g=gcd(g,np)));
print("[p, #E(F_p)] for good p in [5,60]: ",L);
print("gcd = ",g);
print("elltors(E) = ",elltors(E));
