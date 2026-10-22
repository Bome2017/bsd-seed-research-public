{
alarm(25);gettime();
NF=read("/Users/bsm/BSD_SEED_COMPLETE_BOUND_SCALING_2026-10-20/seed_five/nf.gp");D=read("../arithmetic/support_matrices.gp");PS=read("../arithmetic/private_support_result.gp");B=D[1];CI=D[4];PI=D[7];OUT=List();IP=0;
if(#PS[1]!=177 || PS[2]!=21 || PS[3]!=156,error("private classification count"));
for(i=1,#PS[1],my(r=PS[1][i],col=r[1],j=r[2],nn=idealnorm(NF,B[j]),fac=List());if(CI[j]!=col || !setsearch(PI,col) || nn!=r[3],error("norm binding"));if(!r[6],my(F=idealfactor(NF,B[j]),P=matid(24));for(k=1,matsize(F)[1],my(pr=F[k,1],ex=F[k,2],norm=idealnorm(NF,pr));if(norm>419775,error("inside claim has outside prime support"));P=idealmul(NF,P,idealpow(NF,pr,ex));listput(fac,[pr[1],pr[4],ex,norm]));if(P!=B[j],error("inside ideal factorization"));IP++);listput(OUT,[col,j,nn,r[6],Vec(fac)]));
if(IP!=21,error("inside count"));write("private_support_audit_input.gp",Vec(OUT));print("INDEPENDENT_PRIVATE_INSIDE_SUPPORT_COMPLETE;INSIDE=",IP,";PRIVATE=177;MS=",gettime());quit;
}
