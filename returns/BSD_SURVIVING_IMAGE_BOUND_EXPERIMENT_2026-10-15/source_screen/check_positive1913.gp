alarm(45);
D=read("../mirror_bound/positive1913/inputs/data.gp");C=read("../mirror_bound/positive1913/inputs/affine_norm_certificate.gp");R=read("../mirror_bound/positive1913/reverse_certificate.gp");
E=D[1];fA=D[3];T=D[5];fB=C[1];NA=nfinit(fA);NB=nfinit(fB);TW=R[1];AA=R[2];BB=R[3];Q=R[4];
XT=T[1]+E.b2/12;YT=T[2]+(E.a1*T[1]+E.a3)/2;SA=-E.c4/48;
Q0=gcd(x^4-2*XT*x^2+2*YT*x+SA,subst(fB,z,6*x));Q0=Q0/pollead(Q0);
if(Q0!=Q||poldegree(Q)!=3,error("incidence cubic mismatch"));
for(j=1,2,if(idealhnf(NA,AA[j])!=matid(8)||idealhnf(NB,BB[j])!=matid(8),error("not global units"));if(AA[j]*subst(lift(AA[j]),w,TW)!=1||BB[j]*subst(lift(BB[j]),z,-Mod(z,fB))!=1,error("not strictly anti"));U=Mod(subst(lift(BB[j]),z,6*x),Q);MM=matrix(3,3,a,b,polcoef(lift(U*Mod(x^(b-1),Q)),a-1,x));if(matdet(MM)!=AA[j],error("determinant reverse norm mismatch")));
if(matrank(Mod(R[6],3))!=2,error("independence"));
print("INDEPENDENT_TRANSPOSE_INCIDENCE_DETERMINANT_IDENTITIES=2;GLOBAL_UNITS=YES;STRICT_ANTI=YES;SOURCE_CLASS_RANK=2;PASS");quit;
