default(parisizemax,1000000000);alarm(150);read("../lib/selmer.gp");C=read("certificate.gp");CW=read("../class_witness.gp");nf=C[1];LI=CW[14][16];RAY=read("ray.bin");RR=read("ray_coordinates.gp");RC=RR[2];
PRS=concat(vector(#LI,j,vector(#LI[j][2],i,LI[j][2][i][1])));DEP=concat(vector(#LI,j,vector(#LI[j][2],i,LI[j][2][i][2])));OLDBID=concat(vector(#LI,j,vector(#LI[j][2],i,LI[j][2][i][3])));
FACT=matrix(#PRS,2,i,j,if(j==1,PRS[i],DEP[i]));KG=List();ELTS=List();SELECT3=List();BASISCHECKS=List();
{for(i=1,#PRS,my(BID=idealstar(nf,idealpow(nf,PRS[i],DEP[i]),2));if(BID.cyc!=OLDBID[i].cyc,error("local basis invariant mismatch"));for(j=1,#BID.cyc,my(gen=BID.gen[j],LG=ideallog(nf,gen,OLDBID[i]),target=vector(#BID.cyc,k,k==j)~);if(LG!=target,error("local generator basis changed"));my(gg=nfbasistoalg(nf,idealchinese(nf,FACT,vector(#PRS,k,if(k==i,gen,1)))),hh=idealhnf(nf,gg),cc=bnrisprincipal(RAY,hh,0));listput(ELTS,gg);listput(KG,cc);if(BID.cyc[j]%3==0,listput(SELECT3,#KG));));}
KG=matconcat(Vec(KG));SEL=Vec(SELECT3);KS=matrix(#RAY.cyc,#SEL,i,j,KG[i,SEL[j]]);CY=matdiagonal(RAY.cyc);
KINDEX=matsnf(mathnf(matconcat([CY,KG])));if(select(a->a>1,KINDEX)!=[3],error("residue kernel image index not3"));
RAWREL=mathnf(matconcat([CY,3*KG]));RAWSN=matsnf(RAWREL);ALLOW=KS*lift(C[11]);FINALREL=mathnf(matconcat([CY,3*KG,ALLOW]));FINALSN=matsnf(FINALREL);
if(select(a->a>1,FINALSN)!=[3,3,3,3],error("actual ray quotient differs from pushout"));
if(matsolvemod(matconcat([CY,3*KG,ALLOW]),vector(#RAY.cyc),3*RC)==0,error("3J not killed in final quotient"));
print("RESIDUE_KERNEL_INDEX=",KINDEX,";RAW_CUBE_KERNEL_QUOTIENT=",RAWSN,";LOCAL_ALLOWANCE_QUOTIENT=",FINALSN);
BC=lift(C[10]);BR=KS*BC;RB=RR[3];if(matsolvemod(matconcat([CY,3*KG]),vector(#RAY.cyc),RB-BR)==0,error("beta ray/residue match fails"));
write("quotient_certificate.gp",[FACT,Vec(ELTS),KG,SEL,KS,CY,RAWREL,RAWSN,ALLOW,FINALREL,FINALSN,KINDEX,BR]);
print("ACTUAL_CRT_TO_RAY_QUOTIENT_PASS");quit;
