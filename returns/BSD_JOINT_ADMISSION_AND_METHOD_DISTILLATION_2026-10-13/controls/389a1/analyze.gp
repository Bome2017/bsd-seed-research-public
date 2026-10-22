alarm(90); read("../lib/cubinv.gp");read("../lib/classimg.gp");read("../lib/selmer.gp");
D=read("data.gp");E=D[1];Pts=D[2];fL=D[3];ps=D[4];T=D[5];G=D[6];V=D[7];H0=D[8];TAU=D[9];AC=D[10];LR=D[13];UB=D[14];Rows=D[15];LI=D[16];SCREEN=D[17];ng=#G;SCALAR=TAU+matid(ng);GS=matconcat([SCALAR;LR]);KG=matker(GS);EX=[;];BASE=AC;
{for(j=1,#KG,if(matrank(matconcat([BASE,KG[,j]]))>#BASE,EX=if(#EX,matconcat([EX,KG[,j]]),Mat(KG[,j]));BASE=matconcat([BASE,KG[,j]])));}
print("GLOBAL_NECESSARY_KERNEL_DIM=",#KG,";EXTRA_DIRECTIONS=",#EX);print("EXTRA_EXPONENTS=",lift(EX));print("EXTRA_VALUATION_ROWS=",lift(V*EX));
print("LOCAL_EXTRA_RANK=",matrank(Rows*EX));
{for(j=1,#EX,print("EXTRA_ELEMENT_",j,"=",prod(i=1,ng,G[i]^lift(EX[i,j])));for(l=1,#LI,print("EXTRA_LOCAL=",LI[l][1],";column=",j,";defect=",lift(LI[l][5]*EX[,j]))));}
nf=read("nf.gp");setrand(20261014);Rows45=[;];
{for(i=1,#ps,my(l=ps[i],Dl=[locdata(nf,pr)|pr<-idealprimedec(nf,l)],Bl=lockummer(E,nf,T,l,Dl,45),Ml=matconcat(vector(ng,j,Mod(concat(vector(#Dl,q,locvec(nf,G[j],Dl[q]))),3)~)),Rr=if(Bl[2]==0,Ml,matker(Bl[1]~)~*Ml));if(matrank(matconcat([Rr;LI[i][5]]))!=matrank(Rr)||matrank(Rr)!=matrank(LI[i][5]),error("local rowspace changed"));Rows45=if(#Rows45,matconcat([Rows45;Rr]),Rr);print("LOCAL_PRECISION_45_AGREES=",l));}
if(matrank(matconcat([Rows;Rows45]))!=matrank(Rows),error("aggregate local changed"));
jm(A)=vector(matsize(A)[1],i,vector(matsize(A)[2],j,lift(A[i,j])));
write("matrices.json","{");write("matrices.json","\"source_dimension\":",ng,",");
write("matrices.json","\"valuation\":",jm(V),",");write("matrices.json","\"units\":",jm(UB),",");write("matrices.json","\"scalar\":",jm(SCALAR),",");write("matrices.json","\"additivity\":",jm(LR),",");write("matrices.json","\"local\":",jm(Rows),",");write("matrices.json","\"points\":",jm(AC),",");write("matrices.json","\"extra\":",jm(EX),",");write("matrices.json","\"local_blocks\":[");
{for(i=1,#LI,write("matrices.json","{\"prime\":",LI[i][1],",\"image_dimension\":",LI[i][3][2],",\"rows\":",jm(LI[i][5]),"}",if(i<#LI,",","")));}
write("matrices.json","]}");print("ANALYSIS_COMPLETE");quit;
