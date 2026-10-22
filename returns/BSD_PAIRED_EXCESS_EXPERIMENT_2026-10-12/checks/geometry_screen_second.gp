default(nbthreads,1);default(realprecision,70);
lg(E,Q,p,np,pr)=ellpadiclog(E,p,pr,ellmul(E,[Q[1]+O(p^(pr+4)),Q[2]+O(p^(pr+4))],np))/np;
{E0=ellinit([0,-1,1,-10,-20]);F0=ellinit([0,-1,1,-7820,-263580]);nc=0;nt=0;nr=0;found=0;start=getwalltime();lastd=97717;
for(dd=97718,2000000,
 if(nc>=200 || nt>=100000 || nr>=24 || found || getwalltime()-start>120000,break);
 lastd=dd;
 if(dd%4!=1 || !issquarefree(dd) || kronecker(dd,5)!=-1 || kronecker(dd,11)!=1,next);
 nt++;bn=bnfinit(quadpoly(dd,y));if(bn.no%5,next);pr=idealprimedec(bn,11)[1];co=bnfisprincipal(bn,pr,0);sm=matsnf(concat(matdiagonal(bn.cyc),co));if(!sum(i=1,#sm,sm[i]%5==0),next);
 nc++;E=ellminimalmodel(elltwist(E0,dd));rk=ellrank(E,2);print("CANDIDATE ",[dd,bn.no,bn.cyc,co,sm,rk]);
 if(rk[1]!=2 || rk[2]!=2 || #rk[4]!=2,next);
 nr++;P=ellsaturation(E,rk[4],7);F=ellminimalmodel(elltwist(F0,dd));iso=ellisomat(E,5);foundmap=0;
 for(j=1,#iso[1],Fs=ellinit(iso[1][j][1]);Fm=ellminimalmodel(Fs,&cv);if(Fm[1..5]==F[1..5],foundmap=j;break));
 if(!foundmap,error("target missing"));imgs=vector(2,i,ellchangepoint(ellisogenyapply(iso[1][foundmap][2],P[i]),cv));Q=ellsaturation(F,imgs,7);
 hc=ellheightmatrix(F,concat(Q,imgs));mat=round(hc[1..2,1..2]^-1*hc[1..2,3..4]);
 if(vector(2,i,elladd(F,ellmul(F,Q[1],mat[1,i]),ellmul(F,Q[2],mat[2,i]))==imgs[i])!=[1,1],error("map matrix fails"));
 hs=ellpadicheightmatrix(F,5,8,Q);hh=hs*[1,-ellpadics2(F,5,8)]~;lv=vector(2,i,lg(F,Q[i],5,7,8)/5);la=vector(2,i,lg(E,P[i],5,7,8)/5);hu=hh/log(6+O(5^10));rv=valuation(matdet(hu),5);
 print("GEOMETRY ",[dd,E[1..5],F[1..5],P,Q,mat,matdet(mat),ellglobalred(E)[3],ellglobalred(F)[3],rv,lift(Mod(hh/5,5)),lift(Mod(lv,5)),lift(Mod(la,5)),matdet(hu)]);
 if(rv>0 && rv<6 && valuation(matdet(mat),5)==1,found=dd);
);
print("DONE ",[nt,nc,nr,found,lastd,getwalltime()-start]);}
quit;
