alarm(90);
R=read("/Users/bsm/BSD_STRUCTURAL_DISCOVERY_2026-10-13/seed3/actual_representatives.gp");nf=nfinit(R[5]);
if(nf.zk!=read("/Users/bsm/BSD_STRUCTURAL_DISCOVERY_2026-10-13/seed3/nf_only.gp").zk,error("integral basis mismatch"));
SD=read("../data/stage1_data.gp");
{for(k=1,3,my(file=if(k==1,"../data/point_unit_certificate.gp",Str("../data/rejected_unit_",if(k==2,12,14),"_certificate.gp")),C=read(file),raw=if(k==1,R[8][1],SD[1][if(k==2,12,14)]),UF=C[4],GF=C[3],VV=Map(),QQ,FC=0);if(C[1]!=raw || UF[1,1]!=raw || UF[1,2]!=1,error("source binding"));if(#UF~!=#GF~+1,error("factor count"));for(i=1,#GF~,if(UF[i+1,1]!=nfbasistoalg(nf,GF[i,1]) || UF[i+1,2]!=-3*GF[i,2],error("literal cube correction")));if(idealhnf(nf,idealpow(nf,C[2],3))!=idealhnf(nf,raw),error("ideal cube"));for(i=1,#UF~,my(F=idealfactor(nf,UF[i,1]));for(j=1,#F~,my(key=Str(idealhnf(nf,F[j,1])),v=0);mapisdefined(VV,key,&v);mapput(VV,key,v+UF[i,2]*F[j,2])));QQ=Mat(VV);for(i=1,matsize(QQ)[1],if(QQ[i,2]!=0,error("not a global unit")));print("INDEPENDENT_UNIT_",k,"_PASS; FACTORS=",#UF~, ";PRIME_IDEALS=",matsize(QQ)[1]);)}
if(nf.sign!=[2,3],error("source signature"));
fPlus=subst(R[5],w,sqrt(x));
if(poldegree(fPlus,x)!=4 || nfinit(fPlus).sign!=[2,1],error("fixed field signature"));
print("RELATIVE_UNIT_RANK=2");
print("NEW_UNITS_PORTABLE_PASS");quit;
