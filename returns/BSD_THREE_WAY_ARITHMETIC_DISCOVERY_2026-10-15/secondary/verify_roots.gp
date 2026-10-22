alarm(45);z;w;gettime();
C=read("ROOT_CERTIFICATES.gp");
{if(#C!=6,error("six records required"));for(i=1,#C,my(r=C[i],fa=r[3],alpha=r[4],B=r[5],fb=B[1],g=B[2],ww=B[3],nn=r[6],rr=r[7],nfA=nfinit(fa),nfB=nfinit(fb));
 if(poldegree(fa,w)!=8||poldegree(fb,z)!=8||poldegree(g,x)!=3,error("wrong degrees"));
 if(subst(fa,w,ww)!=0,error("incidence embedding"));
 my(aa=subst(lift(alpha),w,ww),MM=matrix(3,3,j,k,polcoef(lift(aa*Mod(x,g)^(k-1)),j-1,x)));
 if(matdet(MM)!=nn,error("independent determinant norm"));
 if(idealhnf(nfA,alpha)!=matid(8)||#nfroots(nfA,x^3-alpha)!=0,error("unit/noncube"));
 if(i==1,if(#rr!=0||#nfroots(nfB,x^3-nn)!=0,error("false norm")),if(#rr!=1||rr[1]^3!=nn||idealhnf(nfB,rr[1])!=matid(8),error("root or unit")));
 print("VERIFIED=",r[1],":",r[2]););}
print("INDEPENDENT_DETERMINANT_NORM_PASS;ROWS=6");quit;
