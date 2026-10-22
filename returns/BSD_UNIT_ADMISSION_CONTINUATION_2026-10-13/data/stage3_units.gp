alarm(110);read("cubinv.gp");read("classimg.gp");read("selmer.gp");gettime();
B=read("/Users/bsm/BSD_P3_LOWER_HALF_3DESCENT_RETURN_OPUS_2026-09-29/work/kb2a_bnf.bin");B=subst(B,y,w);nf=B.nf;
D=read("stage1_data.gp");G=D[1];V=D[2];H0=D[3];TAU=D[4];LR=D[5];AC=D[6];Norm=TAU+matid(15);
AF=vector(15,j,idealfactor(nf,G[j]));PP=List();
{for(j=1,15,for(i=1,#AF[j]~,my(pr=AF[j][i,1],found=0);for(k=1,#PP,if(PP[k]==pr,found=1));if(!found,listput(PP,pr))))}
PP=Vec(PP);VV=matrix(#PP,15,i,j,nfeltval(nf,G[j],PP[i]));
if(Mod(VV,3)*H0!=0*(Mod(VV,3)*H0),error("outside-S valuation defect"));
CR=matrix(#B.cyc,#H0);II=List();
{for(j=1,#H0,my(ev=lift(H0[,j]),vv=VV*ev,I=matid(8));for(i=1,#PP,I=idealmul(nf,I,idealpow(nf,PP[i],vv[i]/3)));listput(II,I);CR[,j]=bnfisprincipal(B,I,0);print("H0_CLASS_COLUMN=",j,"; class=",CR[,j]);)}
ix=select(i->B.cyc[i]%3==0,[1..#B.cyc]); CC=Mod(matrix(#ix,#H0,i,j,CR[ix[i],j]/(B.cyc[ix[i]]/3)),3);
if(vector(#B.cyc,i,vector(#H0,j,(3*CR[i,j])%B.cyc[i]))!=vector(#B.cyc,i,vector(#H0)),error("class not3torsion"));
UK=matker(CC); UB=H0*UK; TU=matsolve(UB,TAU*UB);
if(UB*TU!=TAU*UB,error("unit tau stable"));
UN=UB*matker(TU+matid(#UB)); KU=matconcat([AC[,1],AC[,3]-AC[,4]]);
if(matrank(matconcat([UN,KU]))!=#UN,error("known units not entire norm plane"));
print("FULL_VALUATION_ZERO_DIM=",#H0,"; UNIT_DIM=",#UB,"; NORM_UNIT_DIM=",#UN,"; KNOWN_UNIT_RANK=",matrank(KU));
print("H0_BASIS=",lift(H0));print("H0_CLASS_RAW=",CR);print("H0_CLASS3=",lift(CC));print("UNIT_BASIS=",lift(UB));print("TAU_ON_UNITS=",lift(TU));print("NORM_UNIT_BASIS=",lift(UN));
Screen=matconcat([Norm;LR]); DU=Screen*UB; DH=Screen*H0;
print("COUPLING_RANK_NORM=",matrank(Norm*H0)-matrank(Norm*UB),"; COUPLING_RANK_NORM_ADDITIVITY=",matrank(DH)-matrank(DU));
jx=matindexrank(CC)[2];CL=matrix(15,#jx,i,j,H0[i,jx[j]]);ux=matindexrank(DU)[2];UP=matrix(15,#ux,i,j,UB[i,ux[j]]);REPAIR=matsolve(Screen*UP,-Screen*CL);
if(Screen*(CL+UP*REPAIR)!=0*(Screen*CL),error("coupling repair failed"));
print("CLASS_LIFTS=",lift(CL));print("UNIT_REPAIR_BASIS=",lift(UP));print("UNIT_REPAIR_COORDINATES=",lift(REPAIR));
write("stage3_data.gp",[H0,CR,CC,UB,TU,UN,KU,CL,UP,REPAIR,PP,VV,II]);
print("UNIT_CLASS_MAP_MS=",gettime());
RD=read("/Users/bsm/BSD_STRUCTURAL_DISCOVERY_2026-10-13/seed3/ideal_root_data.gp");I1=RD[4][1]; PG=bnfisprincipal(B,I1,5);if(PG[1]!=0*PG[1],error("point1 root ideal notprincipal")); GF=PG[2];PM=Map();
{for(i=1,#GF~,my(FF=idealfactor(nf,GF[i,1]));for(j=1,#FF~,my(key=Str(FF[j,1]),old=0);mapisdefined(PM,key,&old);mapput(PM,key,old+GF[i,2]*FF[j,2])));}
IF=idealfactor(nf,I1);
{for(i=1,#IF~,my(key=Str(IF[i,1]),old=0);mapisdefined(PM,key,&old);mapput(PM,key,old-IF[i,2]);)}
ZZ=Mat(PM);if(sum(i=1,matsize(ZZ)[1],abs(ZZ[i,2]))!=0,error("point compact generator mismatch"));
AA=read("/Users/bsm/BSD_STRUCTURAL_DISCOVERY_2026-10-13/seed3/actual_representatives.gp")[8];
UF=matconcat([[AA[1],1];matrix(#GF~,2,i,j,if(j==1,nfbasistoalg(nf,GF[i,1]),-3*GF[i,2]))]);
if(idealpow(nf,I1,3)!=idealhnf(nf,AA[1]),error("point root idealcube mismatch"));
write("point_unit_certificate.gp",[AA[1],I1,GF,UF]);print("POINT_UNIT_CERTIFIED=1; compact_factors=",#UF~);
print("POINT_UNIT_MS=",gettime());
BAD=0;
{for(j=1,15,if(Mod(VV[,j],3)==0*Mod(VV[,j],3) && #AF[j]~==0 && Norm[,j]!=0*Norm[,j],BAD=j;break));}
print("REJECTED_UNIT_SOURCE_INDEX=",BAD);
if(BAD,write("rejected_unit.gp",[G[BAD],BAD,Norm[,BAD],nfeltnorm(nf,G[BAD])]);print("REJECTED_UNIT_NORM=",nfeltnorm(nf,G[BAD]),"; defect=",lift(Norm[,BAD])));
print("STAGE3_COMPLETE");quit;
