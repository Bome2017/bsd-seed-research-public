alarm(30);read("../selmer.gp");D=read("data.gp");nf=read("nf.gp");E=D[1];T=D[5];G=D[6];
eltof(a)=my(f=flat(nf,a));prod(i=1,#f,f[i][1]^f[i][2]);
coeffs(a)=vector(8,i,Str(polcoef(lift(a),i-1,w)));
write("source_elements.json","{\"field\":",vector(9,i,Str(polcoef(nf.pol,i-1))),",\"T\":",[coeffs(T[1]),coeffs(T[2])],",\"ainvariants\":",vector(5,i,E[i]),",\"source\":",vector(#G,j,coeffs(eltof(G[j]))),"}");print("SOURCE_ELEMENTS_EXPORTED");quit;
