alarm(30);
SETUP
coeffs(a)=vector(8,i,Str(polcoef(lift(a),i-1,w)));
write("actual_polynomials.json","{\"field\":",vector(9,i,Str(polcoef(nf.pol,i-1,w))),",\"T\":",[coeffs(T[1]),coeffs(T[2])],",\"classes\":",vector(#AE,j,coeffs(AE[j])),"}");print("ACTUAL_POLYNOMIALS_EXPORTED");quit;
