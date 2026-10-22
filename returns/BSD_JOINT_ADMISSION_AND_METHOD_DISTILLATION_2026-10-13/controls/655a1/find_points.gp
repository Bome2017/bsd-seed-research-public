alarm(90);read("../lib/cubinv.gp");read("../lib/classimg.gp");read("../lib/selmer.gp");D=read("data.gp");E=D[1];nf=read("nf.gp");T=D[5];G=D[6];AP=D[18];PV=List();
{for(k=-40,40,my(a=rhs2(E,k),r);if(a>=0&&issquare(a,&r),listput(PV,[k,(r-E.a1*k-E.a3)/2])));}
PV=Vec(PV);print("CANDIDATE_POINTS=",PV);PC=vector(#PV,j,ftan(E,T,PV[j]));PH=phimat(nf,concat(G,PC),AP);NR=matsize(PH)[1];PG=matrix(NR,#G,i,j,PH[i,j]);PP=matrix(NR,#PC,i,j,PH[i,j+#G]);CC=matsolve(PG,PP);print("POINT_MATRIX=",lift(CC));print("POINT_RANK=",matrank(CC));print("INDEPENDENT_INDICES=",matindexrank(CC)[2]);quit;
