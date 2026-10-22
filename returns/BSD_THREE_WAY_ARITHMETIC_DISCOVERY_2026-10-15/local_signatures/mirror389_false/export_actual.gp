alarm(30);
B=read("bnf.bin");nf=B.nf;D=read("data.gp");E=D[1];T=D[5];G=D[6];W=D[10];ps=D[4];KN=Mod(Mat([0,0,0,0,0,0,2,2,2,2,1]~),3);AE=[prod(i=1,#G,G[i]^lift(KN[i,1]))];
coeffs(a)=vector(8,i,Str(polcoef(lift(a),i-1,w)));
write("actual_polynomials.json","{\"field\":",vector(9,i,Str(polcoef(nf.pol,i-1))),",\"T\":",[coeffs(T[1]),coeffs(T[2])],",\"classes\":",vector(#AE,j,coeffs(AE[j])),"}");print("ACTUAL_POLYNOMIALS_EXPORTED");quit;
