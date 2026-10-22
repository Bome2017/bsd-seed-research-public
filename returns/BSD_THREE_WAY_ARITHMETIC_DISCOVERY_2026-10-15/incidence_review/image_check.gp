alarm(60);
E=ellinit([0,0,1,-21,-27]);f=x^8-4*x^7-17*x^6+12*x^5+270*x^4+33*x^3-1101*x^2-1218*x+3945;
print("DISCRIMINANT=",E.disc," FACTOR=",factor(E.disc));print("GALOIS=",polgalois(f));print("IRREDUCIBLE=",polisirreducible(f));
forprime(q=5,37,if(E.disc%q,print("FROB ",q," ",ellap(E,q)," DISCR_MOD3 ",lift(Mod(ellap(E,q)^2-4*q,3)))));
print("IMAGE_CHECK_COMPLETE");quit;
