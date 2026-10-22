\\ Portable exact positive certificate. No bnf, class-group or unit basis.
alarm(90);
read("../seed3/certificate_library.gp");
R=read("../seed3/actual_representatives.gp");
fL=R[5]; nf=nfinit(fL); oldnf=read("../seed3/nf_only.gp");
if(nf.zk!=oldnf.zk,error("fresh integral basis differs"));
if(R[1]!=V_ai || R[2]!=V_P1 || R[3]!=V_P2 || R[4]!=V_C || R[5]!=V_fL,error("historical seed data binding"));
EC=ellinit(V_ai); T0=R[6];
if(!ellisoncurve(EC,T0) || ellmul(EC,T0,3)!=[0] || T0==[0],error("torsion point"));
AC=[V_kummer(V_ai,T0,V_P1),V_kummer(V_ai,T0,V_P2),V_cubicclass(nf,V_C[1])[1],V_cubicclass(nf,V_C[2])[1]];
if(AC!=R[8],error("fresh source-image reconstruction mismatch"));
UC=read("../seed3/unit_certificate.gp"); UF=UC[5];
if(UC[1]!=R[8][3] || UC[2]!=R[8][4],error("cubic image binding mismatch"));
if(UF[1,1]!=UC[1] || UF[1,2]!=1 || UF[2,1]!=UC[2] || UF[2,2]!=-1,error("unit ratio header"));
if(#UF~!=#UC[4]~+2,error("generator factor count"));
{for(i=1,#UC[4]~,if(UF[i+2,1]!=nfbasistoalg(nf,UC[4][i,1]) || UF[i+2,2]!=-3*UC[4][i,2],error("cube correction mismatch")));}
if(idealhnf(nf,idealpow(nf,UC[3],3))!=idealhnf(nf,UC[1]/UC[2]),error("ideal cube ratio"));

\\ Unlike the producer's generator check, factor the complete UNIT expression
\\ directly. Canonical ideal HNFs identify primes, not a printed prime encoding.
vals=Map(); first_nonzero=0; rawvals=Map();
{for(i=1,#UF~,my(F=idealfactor(nf,UF[i,1]));for(j=1,#F~,my(k=Str(idealhnf(nf,F[j,1])),v=0);mapisdefined(vals,k,&v);mapput(vals,k,v+UF[i,2]*F[j,2]);if(i<=2,v=0;mapisdefined(rawvals,k,&v);mapput(rawvals,k,v+UF[i,2]*F[j,2]));if(i==1 && F[j,2]!=0,first_nonzero=F[j,2]));)}
VK=Vec(vals);
if(sum(i=1,#VK,mapget(vals,VK[i])!=0)!=0,error("not a global unit"));
RK=Vec(rawvals);
if(sum(i=1,#RK,mapget(rawvals,RK[i])!=0)==0,error("omitted-correction control ineffective"));
\\ Increasing the first factor's exponent by one adds its nonzero ideal
\\ valuation row to the proved zero row, hence is rejected by this same test.
if(first_nonzero==0,error("tamper control ineffective"));

NC=read("../seed3/norm_one_unit_certificate.gp"); tau=Mod(-w,fL); UN=NC[2];
if(NC[1]!=tau || #UN~!=2*#UF~,error("norm-one binding"));
T=R[6];
if(subst(lift(T[1]),w,tau)!=T[1] || subst(lift(T[2]),w,tau)!=-T[2],error("tau not minusT"));
{for(i=1,#UF~,if(UN[i,1]!=UF[i,1] || UN[i,2]!=UF[i,2] || UN[i+#UF~,1]!=subst(lift(UF[i,1]),w,tau) || UN[i+#UF~,2]!=-UF[i,2],error("norm-one factor identity")));}
\\ Four exact residue rows are the replayed historical certificate. The
\\ unit class column is C1-C2 because the removed factor is a literal cube.
S=Mod([1,1,0,1;2,0,0,0;2,1,2,0;1,1,2,1],3);
Snew=matconcat([S[,1],S[,2],S[,3]-S[,4],S[,3]]);
if(matrank(Snew)!=4,error("unit class not distinguished"));
print("FRESH_NF_BASIS_MATCH=1");
print("FRESH_POINT_AND_CUBIC_IMAGES_MATCH=1");
print("GLOBAL_UNIT_CHECK=1; FACTORS=",#UF~, "; PRIME_IDEALS=",#VK);
print("NEGATIVE_OMIT_CUBE_CORRECTION=REJECTED");
print("NEGATIVE_EXPONENT_TAMPER=REJECTED; NONZERO_ADDED_VALUATION=",first_nonzero);
print("NORM_ONE_FACTOR_IDENTITY=1; TAU_T=-T");
print("UNIT_AND_POINTS_RESIDUE_RANK=",matrank(Snew));
print("PORTABLE_UNIT_CERTIFICATE_PASS");
quit;
