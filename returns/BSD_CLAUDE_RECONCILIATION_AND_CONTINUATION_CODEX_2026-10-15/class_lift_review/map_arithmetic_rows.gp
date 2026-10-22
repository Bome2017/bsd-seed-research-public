alarm(60);
read("lib/cubinv.gp");read("lib/classimg.gp");read("lib/selmer.gp");
B=read("/Users/bsm/BSD_CLASS_LIFT_COUPLING_EXPERIMENT_2026-10-13/search/mirror389/bnf.bin");nf=B.nf;
D=read("data.gp");E=D[1];T=D[5];G=D[6];H0=D[8];TAU=D[9];LR=D[13];LI=D[16];
CTX=read("/Users/bsm/BSD_CLASS_LIFT_COUPLING_EXPERIMENT_2026-10-13/search/mirror389/context.gp");tau=CTX[6];
if(nfgaloisapply(nf,tau,T[1])!=T[1]||nfgaloisapply(nf,tau,T[2])!=-T[2]-E.a1*T[1]-E.a3,error("tau does not negate torsion point"));
print("SCALAR_TARGET_GENERATOR_1BASED=8");print("SCALAR_TARGET_GENERATOR=",lift(G[8]));
print("SCALAR_FULL_ROW=",lift((TAU+matid(#G))[8,]));print("SCALAR_H0_ROW=",lift((TAU+matid(#G))[8,]*H0));
{for(j=1,#G,if(tauapply(nf,tau,G[j])!=D[11][j]^3*prod(i=1,#G,G[i]^lift(TAU[i,j])),error("literal tau cube identity mismatch")));}
print("ALL_LITERAL_TAU_CUBE_IDENTITIES_PASS");
{maplin()=my(fL=nf.pol,rows=List(),p=7,got=0,fl=vector(#G,j,flat(nf,G[j])));
while(got<2,
 p=nextprime(p+1);if(p%3!=1||setsearch(D[4],p)||poldisc(fL)%p==0,next);
 my(rs=polrootsmod(fL,p));if(#rs!=8,next);
 my(Ep=ellinit(E,p),pts,chi,om=znprimroot(p)^((p-1)/3),ok=1);
 iferr(pts=vector(8,i,[subst(lift(lift(T[1])),w,rs[i]),subst(lift(lift(T[2])),w,rs[i])]),er,ok=0);if(!ok,next);
 chi=vector(8,i,vector(#G,j,my(sm=0);for(k=1,#fl[j],my(e=fl[j][k][1],v,u);v=iferr(subst(lift(e),w,rs[i]),er,ok=0;0);if(!ok||v==0,ok=0;break);u=v^((p-1)/3);sm+=fl[j][k][2]*if(u==1,0,u==om,1,2));sm%3));if(!ok,next);
 print("SPLIT_PRIME=",p,";ROOTS=",lift(rs),";CUBIC_ROOT=",lift(om));
 for(i=1,8,for(j=i,8,my(Q=elladd(Ep,pts[i],pts[j]));if(Q==[0],next);my(kq=0);for(k=1,8,if(pts[k]==Q,kq=k));if(!kq,error("sum not found"));my(row=(chi[i]+chi[j]-chi[kq])%3,ix=#rows);listput(rows,row);if(Mod(row,3)!=LR[ix+1,],error("additivity row differs from saved data"));
 if(ix==1||ix==33,print("SELECTED_ROW_ZEROBASED=",ix,";PRIME=",p,";TORSION_INDICES_1BASED=",[i,j,kq]);print("ROOT_TRIPLE=",lift([rs[i],rs[j],rs[kq]]));print("POINT_TRIPLE=",lift([pts[i],pts[j],pts[kq]]));print("SYMBOL_TRIPLE=",[chi[i],chi[j],chi[kq]]);print("ADDITIVITY_FULL_ROW=",row);print("ADDITIVITY_H0_ROW=",lift(Mod(row,3)*H0)))));
 got++);
print("ADDITIVITY_PREFIX_ROWS_MATCH=",#rows);}
maplin();
L3=LI[1];if(L3[1]!=3,error("wrong first local block"));Dl=L3[2];LB=L3[3][1];ML=L3[4];ANN=matker(LB~)~;ar=ANN[2,];
if(ar*LB!=0*(ar*LB),error("not a Kummer annihilator"));if(ar*ML!=L3[5][2,]||L3[5][2,]!=D[15][2,],error("local row mismatch"));
print("LOCAL_KUMMER_IMAGE=",lift(LB));print("LOCAL_ANNIHILATOR_ROW=",lift(ar));print("LOCAL_FULL_ROW=",lift(ar*ML));print("LOCAL_H0_ROW=",lift(ar*ML*H0));
print("SELECTED_LOCAL_PRIME_HNF=",idealhnf(nf,Dl[1][1]));print("SELECTED_LOCAL_UNIT_LOG_2=",ideallog(nf,2,Dl[1][3]));
print("SELECTED_LOCAL_W_MOD_27=",select(a->nfeltval(nf,Mod(w,nf.pol)-a,Dl[1][1])>=3,[0..26]));
print("SELECTED_LOCAL_UNIT_LOG_5=",ideallog(nf,5,Dl[1][3]));
LC=vector(#G,j,locvec(nf,G[j],Dl[1]));FRESHLOCAL=Mod(vector(#G,j,LC[j][2]),3);if(FRESHLOCAL!=ar*ML,error("fresh local unit coordinate differs from saved row"));print("FRESH_LOCAL_SOURCE_COORDINATES=",LC);print("FRESH_LOCAL_SOURCE_ROW_MATCH");
{my(cursor=1);for(j=1,#Dl,my(pr=Dl[j][1],cyc=Dl[j][3].cyc);print("LOCAL_PRIME_INDEX_1BASED=",j,";EF=",[pr.e,pr.f],";CUBE_DEPTH=",Dl[j][2],";PRIME_GENERATOR=",nfbasistoalg(nf,pr.gen[2]),";UNIFORMIZER=",Dl[j][4],";CYCLIC_ORDERS=",cyc);print("COORDINATE=",cursor,";PRIME_INDEX=",j,";KIND=VALUATION;WEIGHT=",lift(ar[cursor]));cursor++;for(k=1,#cyc,if(cyc[k]%3==0,print("COORDINATE=",cursor,";PRIME_INDEX=",j,";KIND=UNIT_LOG;CYCLIC_INDEX=",k,";CYCLIC_ORDER=",cyc[k],";WEIGHT=",lift(ar[cursor]));cursor++)));if(cursor!=#ar+1,error("local coordinate enumeration mismatch"));}
CC=(TAU+matid(#G))[8,]+LR[2,]+LR[34,]+2*ar*ML;
if(CC*H0!=Mod([0,0,0,0,1],3),error("four-row certificate mismatch"));
print("FOUR_ROW_FULL=",lift(CC));print("FOUR_ROW_H0=",lift(CC*H0));print("ARITHMETIC_ROW_MAP_PASS");quit;
