alarm(30);
D=read("data.gp");T=D[5];nf=read("nf.gp");G=D[6];AC=D[10];AE=vector(#AC,j,prod(i=1,#G,G[i]^lift(AC[i,j])));
coeffs(a)=vector(8,i,Str(polcoef(lift(a),i-1,w)));
write("actual_polynomials.json","{\"field\":",vector(9,i,Str(polcoef(nf.pol,i-1,w))),",\"T\":",[coeffs(T[1]),coeffs(T[2])],",\"classes\":",vector(#AE,j,coeffs(AE[j])),"}");print("ACTUAL_POLYNOMIALS_EXPORTED");quit;
