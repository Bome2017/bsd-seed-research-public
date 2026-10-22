actideal(ID,k)={my(R=ID);for(j=1,k,R=idealhnf(NF,nfgaloisapply(NF,SG,R)));R};
actelt(a,k)={my(R=a);for(j=1,k,R=subst(lift(R),variable(NF.pol),SG));R};
isbase(ID)={if(actideal(ID,2)!=ID,error("non-invariant discarded ideal"));for(j=1,#RAM,if(idealval(NF,ID,RAM[j])%2,error("odd ramified exponent")));1};
{
alarm(55);gettime();
NF=read("/Users/bsm/BSD_SEED_COMPLETE_BOUND_SCALING_2026-10-20/seed_five/nf.gp");
FS=read("/Users/bsm/BSD_RELATIVE_UNIT_CLASS_ALTERNATIVE_2026-10-20/relative_source/fields.gp");
B=read("/Users/bsm/BSD_RELATIVE_UNIT_CLASS_ALTERNATIVE_2026-10-20/relative_source/nf12.gp");SG=FS[3];Z=FS[7];
if(NF.pol!=FS[1] || B.pol!=FS[6] || NF.disc/B.disc^2!=2^4*5*4547^6,error("field binding"));
RAM=List();for(ii=1,3,my(q=[2,5,4547][ii],PA=idealprimedec(NF,q),PB=idealprimedec(B,q));for(j=1,#PA,my(hit=0,e=0);for(k=1,#PB,my(a=subst(lift(nfbasistoalg(B,PB[k][2])),variable(B.pol),Z));if(idealval(NF,a,PA[j])>0,hit++;e=PA[j][3]/PB[k][3]));if(hit!=1,error("contraction"));if(e==2,listput(RAM,PA[j]))));RAM=Vec(RAM);if(#RAM!=4,error("ramification count"));
SETUP=read("../arithmetic/setup_data.gp");ORB=SETUP[4];BR=readvec("../arithmetic/batch_rows.gp");CY=readvec("../arithmetic/closed_cycles.gp");R2=List();R3=List();
for(i=1,#ORB,my(P=idealhnf(NF,ORB[i][2]));if(P!=ORB[i][4][1],error("orbit prime"));for(k=0,3,if(actideal(P,k)!=ORB[i][4][k+1],error("orbit action"))));
for(i=1,#BR,my(r=BR[i],P=matid(24));if(r[1]!=i || #r[3]!=#ORB,error("row identity"));for(j=1,#ORB,if(r[3][j],P=idealmul(NF,P,idealpow(NF,ORB[j][2],r[3][j]))));if(P!=r[4],error("input divisor"));isbase(r[6]);if(idealmul(NF,idealmul(NF,idealhnf(NF,r[5]),r[6]),r[7])!=P,error("principal pseudo-relation")));
for(c=1,#CY,my(r=CY[c],a=BR[r[1]],b=BR[r[2]],k=r[3]);if(a[7]!=actideal(b[7],k),error("cycle residual support"));my(L=idealdiv(NF,a[4],actideal(b[4],k)),R=idealmul(NF,idealhnf(NF,r[4]),r[5]));if(L!=R || r[4]!=a[5]/actelt(b[5],k),error("cycle witness"));isbase(r[5]);my(v2=lift(Mod(a[3]-2^k*b[3],5)),v3=lift(Mod(a[3]-3^k*b[3],5)));if(v2!=r[6] || v3!=r[7],error("character projection"));listput(R2,v2);listput(R3,v3));
M2=matrix(#R2,#ORB,i,j,R2[i][j]);M3=matrix(#R3,#ORB,i,j,R3[i][j]);RK2=matrank(Mod(M2,5));RK3=matrank(Mod(M3,5));
write("replay_relative_result.gp",[#BR,#CY,#ORB,#RAM,RK2,RK3]);print("INDEPENDENT_RELATIVE_REPLAY_COMPLETE;ROWS=",#BR,";CYCLES=",#CY,";RANKS=",[RK2,RK3],";MS=",gettime());quit;
}
