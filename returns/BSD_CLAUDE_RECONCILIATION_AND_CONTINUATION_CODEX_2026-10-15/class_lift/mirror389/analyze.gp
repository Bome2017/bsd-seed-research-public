default(parisizemax,1000000000);
alarm(90);setrand(20261013);gettime();
read("lib/cubinv.gp");read("lib/classimg.gp");read("lib/selmer.gp");
B=read("/Users/bsm/BSD_CLASS_LIFT_COUPLING_EXPERIMENT_2026-10-13/search/mirror389/bnf.bin");CTX=read("/Users/bsm/BSD_CLASS_LIFT_COUPLING_EXPERIMENT_2026-10-13/search/mirror389/context.gp");E=CTX[1];Pts=CTX[2];fL=CTX[3];ps=CTX[4];T=CTX[5];tau=CTX[6];SL=CTX[7];nf=B.nf;
G=lsgens2(B,SL,"");G=vector(#G,j,redcube(nf,G[j]));ng=#G;print("SOURCE_DIM=",ng,";CLASS_GROUP=",B.cyc);
V=Mod(matrix(#SL,ng,i,j,nfeltval(nf,G[j],SL[i])),3);H0=matker(V);GT=vector(ng,j,tauapply(nf,tau,G[j]));PC=vector(#Pts,j,ftan(E,T,Pts[j]));
AP=auxprimes(fL,150,ps);PH=phimat(nf,concat(concat(G,GT),PC),AP);NR=matsize(PH)[1];PG=matrix(NR,ng,i,j,PH[i,j]);PT=matrix(NR,ng,i,j,PH[i,j+ng]);PP=matrix(NR,#Pts,i,j,PH[i,j+2*ng]);
if(matrank(PG)!=ng,error("source residue evaluation not injective"));TAU=matsolve(PG,PT);AC=matsolve(PG,PP);if(PG*TAU!=PT||PG*AC!=PP,error("coordinates inconsistent"));if(TAU^2!=matid(ng),error("tau inconsistent"));print("POINT_CLASS_RANK=",matrank(AC),";AUXROWS=",NR);
TR=vector(ng,j,0);AR=vector(#Pts,j,0);
{for(j=1,ng,my(rr=nfroots(nf,X^3-GT[j]/prod(i=1,ng,G[i]^lift(TAU[i,j]))));if(#rr<1,error("tau quotient not cube"));TR[j]=rr[1]);for(j=1,#Pts,my(rr=nfroots(nf,X^3-PC[j]/prod(i=1,ng,G[i]^lift(AC[i,j]))));if(#rr<1,error("point quotient not cube"));AR[j]=rr[1]);}
print("EXACT_TAU_AND_POINT_IDENTITIES=",ng+#Pts);SCALAR=TAU+matid(ng);LR=linrows(E,nf,T,G,6,ps);
UG=bnfunits(B)[1];UG=vector(#UG-1,j,UG[j]);UPH=phimat(nf,concat(G,UG),AP);PGU=matrix(matsize(UPH)[1],ng,i,j,UPH[i,j]);PU=matrix(matsize(UPH)[1],#UG,i,j,UPH[i,j+ng]);UB=matsolve(PGU,PU);if(PGU*UB!=PU,error("unit coordinates inconsistent"));
if(matrank(UB)!=sum(i=1,2,nf.sign[i])-1,error("unit rank mismatch"));if(V*UB!=0*(V*UB),error("unit valuations nonzero"));
AF=vector(ng,j,idealfactor(nf,G[j]));ALLP=List();
{for(j=1,ng,for(i=1,#AF[j]~,my(pr=AF[j][i,1],found=0);for(k=1,#ALLP,if(ALLP[k]==pr,found=1));if(!found,listput(ALLP,pr))))}
ALLP=Vec(ALLP);VV=matrix(#ALLP,ng,i,j,nfeltval(nf,G[j],ALLP[i]));if(Mod(VV,3)*H0!=0*(Mod(VV,3)*H0),error("outside S valuation defect"));CR=matrix(#B.cyc,#H0);II=List();
{for(j=1,#H0,my(ev=lift(H0[,j]),vv=VV*ev,I=matid(8));for(i=1,#ALLP,I=idealmul(nf,I,idealpow(nf,ALLP[i],vv[i]/3)));listput(II,I);CR[,j]=bnfisprincipal(B,I,0));}
ix=select(i->B.cyc[i]%3==0,[1..#B.cyc]);CC=Mod(matrix(#ix,#H0,i,j,CR[ix[i],j]/(B.cyc[ix[i]]/3)),3);
if(matrank(CC)!=#ix,error("full ordinary class3 source missing"));if(matrank(matconcat([H0*matker(CC),UB]))!=#UB || #matker(CC)!=#UB,error("class kernel differs from units"));
CPIV=matindexrank(CC)[2];CL=matrix(ng,#CPIV,i,j,H0[i,CPIV[j]]);print("ORDINARY_CLASS3_DIM=",#ix,";VALUATION_ZERO_DIM=",#H0,";UNITS=",#UB);
Rows=[;];LI=List();
{for(i=1,#ps,my(l=ps[i],Dl=[locdata(nf,pr)|pr<-idealprimedec(nf,l)],Bl=lockummer(E,nf,T,l,Dl,35),Ml=matconcat(vector(ng,j,Mod(concat(vector(#Dl,q,locvec(nf,G[j],Dl[q]))),3)~)),Rr=if(Bl[2]==0,Ml,matker(Bl[1]~)~*Ml));listput(LI,[l,Dl,Bl,Ml,Rr]);Rows=if(#Rows,matconcat([Rows;Rr]),Rr);print("LOCAL=",l,";IMAGE_DIM=",Bl[2],";ROW_RANK=",matrank(Rr),";MS=",gettime());)}
SCREEN=matconcat([SCALAR;LR;Rows]);if(SCREEN*AC!=0*(SCREEN*AC),error("point rejected"));
print("PROFILE=[full,H0,unit,scalarfull,addfull,localfull,jointfull,jointunit,jointH0]");print("PROFILE=",[ng,#H0,#UB,#matker(SCALAR),#matker(LR),#matker(Rows),#matker(SCREEN),#matker(SCREEN*UB),#matker(SCREEN*H0)]);
BKS=[SCALAR,matconcat([SCALAR;LR]),Rows,SCREEN];COUP=List();
{for(j=1,#BKS,my(DD=BKS[j],DU=DD*UB,Ann=matker(DU~)~,DC=Ann*DD*CL,Kc=matker(DC),ui=matindexrank(DU)[2],UP=matrix(ng,#ui,a,b,UB[a,ui[b]]),REPAIR);if(#ui,REPAIR=matsolve(DD*UP,-DD*CL*Kc),REPAIR=matrix(0,#Kc));if(DD*(CL*Kc+UP*REPAIR)!=0*(DD*CL*Kc),error("unit repair identity"));listput(COUP,[Ann,DC,Kc,UP,REPAIR]);print("BLOCK=",j,";UNIT_ADMITTED=",#matker(DU),";CLASS_DEFECT_RANK=",matrank(DC),";CLASS_ADMITTED=",#Kc));}
print("POINT_VALUATIONS=",lift(V*AC));print("UNIT_POINT_INTERSECTION=",matrank(AC)+#matker(SCREEN*UB)-matrank(matconcat([AC,UB*matker(SCREEN*UB)])));
write("data.gp",[E,Pts,fL,ps,T,G,V,H0,TAU,AC,TR,AR,LR,UB,Rows,Vec(LI),SCREEN,AP,PG,PT,PP,UG,CC,CL,Vec(COUP),ALLP,VV,Vec(II),CR]);
jm(A)=vector(matsize(A)[1],i,vector(matsize(A)[2],j,lift(A[i,j])));
write("matrices.json","{");write("matrices.json","\"source_dimension\":",ng,",");write("matrices.json","\"valuation\":",jm(V),",");write("matrices.json","\"valuation_zero_basis\":",jm(H0),",");write("matrices.json","\"units\":",jm(UB),",");write("matrices.json","\"scalar\":",jm(SCALAR),",");write("matrices.json","\"additivity\":",jm(LR),",");write("matrices.json","\"local\":",jm(Rows),",");write("matrices.json","\"points\":",jm(AC),",");write("matrices.json","\"class_boundary_H0\":",jm(CC),",");write("matrices.json","\"class_lifts\":",jm(CL),",");write("matrices.json","\"local_blocks\":[");
{for(i=1,#LI,write("matrices.json","{\"prime\":",LI[i][1],",\"image_dimension\":",LI[i][3][2],",\"rows\":",jm(LI[i][5]),"}",if(i<#LI,",","")));}
write("matrices.json", "],\"coupling_blocks\":[");
{for(i=1,#COUP,write("matrices.json","{\"block\":",i,",\"annihilator\":",jm(COUP[i][1]),",\"class_defect\":",jm(COUP[i][2]),",\"admitted_class_coefficients\":",jm(COUP[i][3]),",\"unit_repair_basis\":",jm(COUP[i][4]),",\"unit_repair_coefficients\":",jm(COUP[i][5]),"}",if(i<#COUP,",","")));}
write("matrices.json","]}");print("COUPLING_COMPLETE");quit;
