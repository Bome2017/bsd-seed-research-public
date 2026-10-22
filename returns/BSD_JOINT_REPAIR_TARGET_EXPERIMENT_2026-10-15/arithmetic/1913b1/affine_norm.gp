default(parisizemax,1000000000);
alarm(120);gettime();
read("lib/cubinv.gp");read("lib/classimg.gp");read("lib/selmer.gp");
DD=read("data.gp");B=read("bnf.bin");nf=B.nf;E=DD[1];fA=DD[3];T=DD[5];G=DD[6];UB=DD[14];SCREEN=DD[17];UG=DD[22];
eltof(a)=my(f=flat(nf,a));prod(i=1,#f,f[i][1]^f[i][2]);
UE=vector(#UG,j,eltof(UG[j]));UROOT=vector(#UG);
{for(j=1,#UG,my(target=UE[j]/prod(i=1,#G,G[i]^lift(UB[i,j])),rt=nfroots(nf,X^3-target));if(#rt==0,error("unit coordinate cube missing"));UROOT[j]=rt[1];if(UROOT[j]^3!=target,error("unit cube identity")));}
K=matker(SCREEN*UB);AE=vector(#K,j,prod(i=1,#UE,UE[i]^lift(K[i,j])));print("ACTUAL_UNIT_KERNEL_DIM=",#K);
SA=-E.c4/48;SB=-E.c6/864;XT=T[1]+E.b2/12;YT=T[2]+(E.a1*T[1]+E.a3)/2;
coeffcol(v)=vector(8,i,polcoef(lift(v),i-1,w))~;
BT=matrix(8,8,i,j,polcoef(lift(YT^(j-1)),i-1,w));ww=matsolve(BT,coeffcol(Mod(w,fA)));
fB=z^8-54*E.c4*z^4+216*E.c6*z^2-243*E.c4^2;
if(!polisirreducible(fB),error("dual line field not irreducible"));NF=nfinit(fB);mm=Mod(z,fB)/6;
GG=x^3-mm^2*x^2+(mm^4+2*SA)*x-(mm^6+2*SA*mm^2-4*SB);
YY=Mod(mm*x-(mm^4+SA)/(2*mm),GG);
WW=sum(i=1,8,ww[i]*YY^(i-1));
if(subst(fA,w,WW)!=0,error("source generator relation"));
if(subst(lift(XT),w,WW)!=Mod(x,GG),error("short X mismatch"));
if(subst(lift(YT),w,WW)!=YY,error("short Y mismatch"));
if(Mod(3*x^4+6*SA*x^2+12*SB*x-SA^2,GG)!=0,error("division polynomial mismatch"));
u(a)=norm(subst(lift(a),w,WW));
NV=vector(#AE,j,u(AE[j]));ROOT=vector(#AE);
{for(j=1,#AE,my(rt=nfroots(NF,x^3-NV[j]));if(#rt==0,error("norm is not a cube"));ROOT[j]=rt[1];if(ROOT[j]^3!=NV[j],error("norm cube identity"));print("EXACT_AFFINE_NORM_CUBE_",j,"=1"));}
write("affine_norm_certificate.gp",[fB,mm,GG,WW,UE,UROOT,K,AE,NV,ROOT]);print("AFFINE_NORM_MS=",gettime());print("AFFINE_NORM_COMPLETE");quit;
