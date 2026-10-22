default(parisizemax,1000000000);alarm(30);
read("lib/cubinv.gp");read("lib/classimg.gp");read("lib/selmer.gp");
B=read("search/1246c1_retry600/bnf.bin");D=read("arithmetic/1246c1_retry600/data.gp");W=read("arithmetic/1246c1_retry600/witness_data.gp");nf=B.nf;E=D[1];T=D[5];G=D[6];tau=tauL(nf,E,T);AC=D[10];Pts=D[2];
KEEP=select(j->AC[,j]!=0*AC[,j],vector(#Pts,j,j));if(#KEEP!=2,error("not two nonzero point columns"));Pts=vecextract(Pts,KEEP);
{for(j=1,#W[1],if(idealhnf(nf,W[1][j])!=matid(8),error("not globalunit",j)));}
if(W[3]*nfgaloisapply(nf,tau,W[3])!=1,error("scalar normone"));
if(W[6]!=prod(j=1,#W[1],W[1][j]^W[5][j]),error("good unit identity"));
PV=prod(j=1,2,ftan(E,T,Pts[j])^lift(W[7][j]));if(W[6]!=W[8]^3*PV,error("good unit-point cube"));
if(W[9]!=prod(j=1,#G,G[j]^lift(D[24][j,1])),error("chosen class lift"));
if(W[10]!=prod(j=1,#W[1],W[1][j]^lift(W[11][j,1])),error("repair unit identity"));
PV2=prod(j=1,2,ftan(E,T,Pts[j])^lift(W[12][j,1]));if(W[9]*W[10]!=W[13]^3*PV2,error("class repair point cube"));
Q=W[4];q=Q[1];rs=Mod(Q[2],q);Ep=ellinit(E,q);PP=Mod(Q[3],q);VV=Mod(Q[4],q);ix=Q[5];
if(!isprime(q)||q%3!=1,error("bad residue prime"));
if(#rs!=8||#Set(lift(rs))!=8,error("not eight distinct roots"));
{for(j=1,8,if(subst(nf.pol,w,rs[j])!=0,error("not fieldroot"));if(PP[j]!=[subst(lift(T[1]),w,rs[j]),subst(lift(T[2]),w,rs[j])],error("torsion specialization"));if(!ellisoncurve(Ep,PP[j])||ellmul(Ep,PP[j],3)!=[0],error("not3torsion"));if(VV[j]!=subst(lift(W[3]),w,rs[j]),error("unit specialization")));}
if(elladd(Ep,elladd(Ep,PP[ix[1]],PP[ix[2]]),PP[ix[3]])!=[0],error("notaffinetriple"));
prd=prod(i=1,3,VV[ix[i]]);if(lift(prd)!=Q[8]||lift(prd^((q-1)/3))!=Q[9]||prd^((q-1)/3)==1,error("noncubeproduct"));
print("WITNESS_REPLAY_PASS;1246c1_retry600=1246c1_retry600;Q=",q,";PRODUCT=",lift(prd),";CUBIC_RESIDUE=",lift(prd^((q-1)/3)),";POINT_COORDS=",W[12]);quit;
