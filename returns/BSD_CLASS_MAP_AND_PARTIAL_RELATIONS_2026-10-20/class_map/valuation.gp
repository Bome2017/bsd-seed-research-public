read("../../lib/cubinv.gp");read("../../lib/classimg.gp");read("../../lib/selmer.gp");
uval(a)=norm(subst(lift(a),variable(nf.pol),WW));
jm(A)=vector(matsize(A)[1],i,vector(matsize(A)[2],j,lift(A[i,j])));
{main()=
alarm(30);gettime();C=read("ideal_map_certificate.gp");D=read("data.gp");B=read("bnf.bin");nf=B.nf;NB=nfinit(C[2]);WW=C[4];E=D[1];
if(subst(nf.pol,variable(nf.pol),w)!=D[3],error("source polynomial"));T=vector(2,i,subst(lift(D[5][i]),w,Mod(variable(nf.pol),nf.pol)));tau=tauL(nf,E,T);
ps=[2,3,13];PA=[];PB=[];for(i=1,#ps,PA=concat(PA,idealprimedec(nf,ps[i]));PB=concat(PB,idealprimedec(NB,ps[i])));
NA=#PA;NN=#PB;TA=matrix(NA,NA);TB=matrix(NN,NN);UD=matrix(NN,NA);WIT=List();hh=B.no;
for(j=1,NA,my(Q=idealhnf(nf,nfgaloisapply(nf,tau,PA[j])),count=0);for(i=1,NA,if(Q==idealhnf(nf,PA[i]),TA[i,j]=1;count++));if(count!=1,error("source action")));
for(j=1,NN,my(Q=idealhnf(NB,nfgaloisapply(NB,Mod(-z,C[2]),PB[j])),count=0);for(i=1,NN,if(Q==idealhnf(NB,PB[i]),TB[i,j]=1;count++));if(count!=1,error("target action")));
for(j=1,NA,my(PP=idealpow(nf,PA[j],hh),t=bnfisprincipal(B,PP,1),be,nu,F,J=matid(8));if(t[1]!=0*t[1],error("supportprincipal"));be=nfbasistoalg(nf,t[2]);if(idealhnf(nf,be)!=PP,error("support source identity"));nu=uval(be);F=idealfactor(NB,nu);for(i=1,NN,my(v=nfeltval(NB,nu,PB[i]));if(v%hh,error("weighted nonintegral"));UD[i,j]=v/hh;J=idealmul(NB,J,idealpow(NB,PB[i],v)));if(J!=idealhnf(NB,nu),error("support outsideS"));listput(WIT,[PA[j],be,nu,F]));
if(UD*TA!=TB*UD,error("equivariance"));K=matker(Mod(TA+matid(NA),3));RR=matrank(Mod(UD,3)*K);QDIM=#K-RR;
write("valuation_certificate.gp",[ps,PA,PB,TA,TB,UD,K,Vec(WIT)]);
write("VALUATION.json",Str("{\"S\":",ps,",\"source_primes_p_e_f\":",vector(NA,i,[PA[i].p,PA[i].e,PA[i].f]),",\"target_primes_p_e_f\":",vector(NN,i,[PB[i].p,PB[i].e,PB[i].f]),",\"source_scalar_permutation\":",jm(TA),",\"target_scalar_permutation\":",jm(TB),",\"primitive_divisor_map\":",jm(UD),",\"faithful_source_dimension\":",#K,",\"faithful_map_rank\":",RR,",\"valuation_allowance_upper\":",QDIM,"}"));
print("PRIMITIVE_SUPPORT_MAP_COMPLETE;FAITHFUL_DIM=",#K,";RANK=",RR,";ALLOWANCE=",QDIM,";MS=",gettime());
}
main();quit;
