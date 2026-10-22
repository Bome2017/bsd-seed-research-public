\\ Independent verifier: no producer libraries; source residues, local maps, resultant norms.
alarm(60);gettime();
D=read("../../arithmetic/28042a1/data.gp");C=read("../../arithmetic/28042a1/affine_norm_certificate.gp");B=read("../../arithmetic/28042a1/bnf.bin");LP=read("../../arithmetic/28042a1/local_precision.gp");E=D[1];fa=D[3];nf=nfinit(fa);T=D[5];G=D[6];ng=#G;AP=D[18];UE=C[5];AE=C[8];Rt=C[10];fb=C[1];
if(E[1..5]!=[1,-1,0,-1367381,615777525],error("identity"));
if(Vec(B.pol)!=Vec(fa)||!polisirreducible(fb),error("field certificate identity"));
if(!polisirreducible(fa)||!ellisoncurve(E,T)||ellmul(E,T,3)!=[0],error("torsion field"));
if(B.tu[1]!=2,error("torsion unit data"));
S=D[4];npS=sum(i=1,#S,#idealprimedec(nf,S[i]));rd=nf.sign[1]+nf.sign[2]-1+npS;
\\ No complete class-group/S-unit assertion is used for this lower bound.
{for(j=1,ng,my(ff=idealfactor(nf,G[j]));for(k=1,#ff~,if(!setsearch(S,ff[k,1].p)&&ff[k,2]%3,error("outside S valuation"))));}
myres(a,rr)={my(q=rr[1],v=Mod(subst(lift(a),w,rr[2]),q),uu=v^((q-1)/3),om=rr[3]);if(v==0,error("zero residue"));if(uu==1,0,uu==om,1,uu==om^2,2,error("cubic character"))};
RR=List();
{for(i=1,#AP,my(ok=1,rr);iferr(rr=vector(ng,j,myres(G[j],AP[i])),err,ok=0);if(ok,listput(RR,rr)));}
RM=Mod(matconcat(Vec(RR)~),3);if(matrank(RM)!=ng,error("source dependence"));
RU=Mod(matrix(#AP,#UE,i,j,myres(UE[j],AP[i])),3);RA=Mod(matrix(#AP,#AE,i,j,myres(AE[j],AP[i])),3);if(matrank(RU)!=4||matrank(RA)!=3,error("unit/survivor independence"));
{for(j=1,#UE,if(idealhnf(nf,UE[j])!=matid(8),error("not actual unit")));}
{for(j=1,2,if(idealhnf(nf,AE[j])!=matid(8),error("admitted element is not unit")));}
tau=Mod(1-w,fa);if(subst(lift(T[1]),w,tau)!=T[1]||subst(lift(T[2]),w,tau)!=-T[2]-E.a1*T[1]-E.a3,error("tau"));
SCROOT=vector(#AE);
{for(j=1,#AE,my(a=AE[j]*subst(lift(AE[j]),w,tau),rr=nfroots(nf,x^3-a));if(#rr==0,error("scalar norm not cube"));SCROOT[j]=rr[1];if(SCROOT[j]^3!=a,error("scalar root identity")));}
\\ Derive incidence from slopes; use a resultant, not producer's norm/matrix.
mm=Mod(z,fb)/6;aa=-E.c4/48;bb=-E.c6/864;phi=x^4+2*aa*x^2+4*bb*x-aa^2/3;
gg=x^3-mm^2*x^2+(mm^4+2*aa)*x-(mm^6+2*aa*mm^2-4*bb);
if(phi!=(x+mm^2)*gg,error("affine line divisor"));
yy=Mod(mm*x-(mm^4+aa)/(2*mm),gg);if(yy^2-Mod(x,gg)^3-aa*Mod(x,gg)-bb!=0,error("incidence curve"));
ww=C[4];if(subst(fa,w,ww)!=0,error("embedding"));
if(subst(lift(T[1]+E.b2/12),w,ww)!=Mod(x,gg)||subst(lift(T[2]+(E.a1*T[1]+E.a3)/2),w,ww)!=yy,error("coordinate binding"));
{for(j=1,#AE,my(a=lift(subst(lift(AE[j]),w,ww)),nm=polresultant(gg,a,x));if(nm!=Rt[j]^3,error("independent resultant norm cube")));}
locdatum(pr)={my(dep=if(pr.p==3,floor(3*pr.e/2)+1,1),bid=idealstar(nf,idealpow(nf,pr,dep),1),pi=if(pr.e==1,pr.p,nfbasistoalg(nf,pr.gen[2])));if(nfeltval(nf,pi,pr)!=1,pi=nfbasistoalg(nf,pr.gen[2])+pr.p);if(nfeltval(nf,pi,pr)!=1,error("uniformizer"));[pr,dep,bid,pi]};
localvector(a,dd)={my(v=nfeltval(nf,a,dd[1]),lg=ideallog(nf,a/dd[4]^v,dd[3]),cyc=dd[3].cyc,ix=select(i->cyc[i]%3==0,[1..#cyc]));concat([v%3],vector(#ix,j,lg[ix[j]]%3))};
tangent(P)={my(slope=(3*T[1]^2+2*E.a2*T[1]+E.a4-E.a1*T[2])/(2*T[2]+E.a1*T[1]+E.a3));P[2]-T[2]-slope*(P[1]-T[1])};
LOCAL=List();ALLROW=[;];MINM=10^9;
{for(ii=1,#S,my(q=S[ii],prs=idealprimedec(nf,q),dd=vector(#prs,j,locdatum(prs[j])),nt=1+sum(j=1,#prs,prs[j].e==1&&prs[j].f==1),dim=0,cols=List(),loca,locg,LL);
 while(3^dim<nt,dim++);if(3^dim!=nt,error("local torsion count"));dim+=(q==3);
 for(j=1,#LP[2],my(c=LP[2][j]);if(c[1]!=q,next);my(xx=c[2],yy0=c[3],ff=yy0^2+E.a1*xx*yy0+E.a3*yy0-xx^3-E.a2*xx^2-E.a4*xx-E.a6,fp=2*yy0+E.a1*xx+E.a3,Nc);
 if(ff!=0,if(valuation(ff,q)<=2*valuation(fp,q),error("Hensel"));Nc=valuation(ff,q)-valuation(fp,q),Nc=c[6]);
 my(ev=tangent([xx,yy0]));for(k=1,#dd,my(margin=prs[k].e*Nc-nfeltval(nf,ev,prs[k])-dd[k][2]);if(margin<0,error("cube precision"));MINM=min(MINM,margin));
 listput(cols,Mod(concat(vector(#dd,k,localvector(ev,dd[k]))),3)~));
 my(lb=if(#cols,matconcat(Vec(cols)),matrix(sum(j=1,#dd,1+sum(k=1,#dd[j][3].cyc,dd[j][3].cyc[k]%3==0)),0)));
 if(matrank(lb)!=dim,error("local basis not complete"));
 loca=Mod(matconcat(vector(#AE,j,concat(vector(#dd,k,localvector(AE[j],dd[k])))~)),3);
 if(matrank(matconcat([lb,loca]))!=dim,error("local admission"));
 locg=Mod(matconcat(vector(ng,j,concat(vector(#dd,k,localvector(G[j],dd[k])))~)),3);
 LL=if(dim==0,locg,matker(lb~)~*locg);ALLROW=if(#ALLROW,matconcat([ALLROW;LL]),LL);
 listput(LOCAL,[q,vector(#prs,j,[prs[j].e,prs[j].f]),nt,dim,matsize(loca)[1]]));}
SCL=Mod(matrix(matsize(RM)[1],ng,i,j,0),3);
SCG=vector(ng,j,G[j]*subst(lift(G[j]),w,tau)); SR=List();
{for(i=1,#AP,my(ok=1,rr);iferr(rr=vector(ng,j,myres(SCG[j],AP[i])),err,ok=0);if(ok,listput(SR,rr)));}
SCL=Mod(matconcat(Vec(SR)~),3);
print("SCALAR_PLUS_LOCAL_DIM=",#matker(matconcat([SCL;ALLROW])));
UPPER=matconcat([SCL;ALLROW]);
print("SOURCE_DIM=",ng,";SIGNATURE=",nf.sign,";S_PRIMES=",npS,";RESIDUE_RANK=",matrank(RM));
print("ACTUAL_UNIT_RANK=",matrank(RU),";SURVIVOR_RANK=",matrank(RA),";SCALAR_CUBES=",#SCROOT,";RESULTANT_NORM_CUBES=",#AE);
print("LOCAL_FULL_IMAGES=",Vec(LOCAL),";MINIMUM_MARGIN=",MINM);
print("NECESSARY_UPPER_DIM=",#matker(UPPER),";TRUE_SEL3_DIM_AT_LEAST=3");
if(AE[3]!=tangent([653,675]),error("point binding"));
write("independent_28042_scalar_roots.gp",SCROOT);print("INDEPENDENT_COMPLETE;MS=",gettime());quit;
