alarm(30);read("lib/cubinv.gp");read("lib/classimg.gp");read("lib/selmer.gp");
B=read("/Users/bsm/BSD_CLASS_LIFT_COUPLING_EXPERIMENT_2026-10-13/search/mirror389/bnf.bin");D=read("data.gp");nf=B.nf;G=D[6];H=D[8];CL=D[24];COUP=D[25];UG=D[22];UB=D[14];E=D[1];T=D[5];
if(poldegree(nf.pol)!=8||!polisirreducible(nf.pol)||!ellisoncurve(E,T)||ellmul(E,T,3)!=[0],error("field torsion binding"));
SL=concat(vector(#D[4],i,idealprimedec(nf,D[4][i])));LP=matconcat(vector(#SL,j,bnfisprincipal(B,SL[j],0)));CS=matsnf(mathnf(matconcat([matdiagonal(B.cyc),LP])));
expected=nf.sign[1]+nf.sign[2]-1+#SL+sum(i=1,#CS,CS[i]%3==0);if(#G!=expected,error("source count"));if(B.tu[1]%3==0,error("unhandled rootsunity"));
PH=phimat(nf,G,D[18]);if(matrank(PH)!=#G,error("source residual dependence"));
{for(i=1,#G,my(fa=idealfactor(nf,G[i]));for(j=1,#fa~,if(!setsearch(Set(D[4]),fa[j,1].p)&&fa[j,2]%3,error("source bad support"))));}
idx=0;for(j=1,#H,if(H[,j]==CL[,1],idx=j));if(!idx,error("classlift notbasiscolumn"));CID=D[28][idx];beta=prod(j=1,#G,G[j]^lift(CL[j,1]));if(idealpow(nf,CID,3)!=idealhnf(nf,beta),error("literal idealcube"));if(bnfisprincipal(B,CID,0)==0,error("trivial ordinaryclass"));
UE=vector(#UG,j,nfbasistoalg(nf,nffactorback(nf,UG[j])));if(vector(#UE,j,idealhnf(nf,UE[j]))!=vector(#UE,j,matid(8)),error("not units"));
rg=COUP[2][4]*COUP[2][5];rl=COUP[3][4]*COUP[3][5];eg=matsolve(UB,rg);el=matsolve(UB,rl);ug=prod(j=1,#UE,UE[j]^lift(eg[j,1]));ul=prod(j=1,#UE,UE[j]^lift(el[j,1]));
Dg=matconcat([D[9]+matid(#G);D[13]]);Dl=D[15];if(Dg*(CL+rg)!=0*(Dg*CL)||Dl*(CL+rl)!=0*(Dl*CL),error("repair mismatch"));
ANN=COUP[4][1];DD=matconcat([Dg;Dl]);vals=ANN*DD*CL;k=0;for(i=1,#vals~,if(vals[i,1],k=i;break));if(!k,error("no rejection"));lam=ANN[k,]/vals[k,1];if(lam*DD*UB!=0*(lam*DD*UB)||lift(lam*DD*CL)[1]!=1,error("annihilator certificate"));
write("class_witness.gp",[nf,CID,beta,UE,eg,el,ug,ul,Dg,Dl,UB,CL,lam,D,SL]);
print("CERTIFIED_SAVED_CLASS=",B.cyc,";S_CLASS=",CS,";EXPECTED_SOURCE=",expected,";SOURCE_RESIDUE_RANK=",matrank(PH));
print("CLASS_IDEAL_COORD=",bnfisprincipal(B,CID,0),";EXACT_IDEAL_CUBE_PASS");print("GLOBAL_REPAIR_UNIT_EXPONENTS=",lift(eg),";LOCAL_REPAIR_UNIT_EXPONENTS=",lift(el));print("ANNIHILATOR_ON_UNITS=",lift(lam*DD*UB),";ANNIHILATOR_ON_CLASS=",lift(lam*DD*CL));
print("LITERAL_CLASS_REPAIR_MISMATCH_WITNESS_PASS");quit;
