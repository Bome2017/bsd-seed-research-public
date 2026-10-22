alarm(20);z;w;C=read("ROOT_CERTIFICATES.gp");
{for(i=2,#C,my(r=C[i],alpha=r[4],B=r[5],fb=B[1],g=B[2],ww=B[3],nn=r[6],s=r[7][1],nfB=nfinit(fb),an=alpha/8,sn=s/8,an_emb=subst(lift(an),w,ww),MM=matrix(3,3,j,k,polcoef(lift(an_emb*Mod(x,g)^(k-1)),j-1,x)),Nnew=matdet(MM));
if(an/alpha!=(1/2)^3||Nnew!=nn/512||sn^3!=Nnew,error("cube scaling identity"));
my(ic=nfalgtobasis(nfB,sn));if(denominator(ic)==1,error("unexpected integral root"));
print("SCALING=",r[1],":",r[2],";SAME_CLASS=1;NEW_ROOT_NONINTEGRAL=1;INTEGRAL_BASIS_DENOM=",denominator(ic)););}
print("SCALING_CONTROL_PASS;ROWS=5");quit;
