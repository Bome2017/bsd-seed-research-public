{
alarm(115);gettime();NF=read("/Users/bsm/BSD_SEED_COMPLETE_BOUND_SCALING_2026-10-20/seed_five/nf.gp");GS=read("geometric_support.gp");GD=read("geometric_rank_data.gp");EV=GD[4];PM=GS[10];nr=matsize(EV)[1];nc=matsize(EV)[2];H=EV;
for(i=1,nr,for(j=1,nc,H[i,PM[PM[j]]]-=EV[i,j]));
KK=matker(H~);for(j=1,matsize(KK)[2],KK[,j]*=denominator(KK[,j]));if(H~*KK!=matrix(nc,matsize(KK)[2]),error("kernel"));
write("geometric_unit_kernel.gp",[H,KK]);print("GEOMETRIC_UNIT_KERNEL;RANK=",nr-matsize(KK)[2],";DIM=",matsize(KK)[2]);
KS=vecsort(vector(matsize(KK)[2],j,[sum(i=1,nr,abs(KK[i,j])),vecmax(abs(KK[,j])),j]),1);UU=vector(nr);done=vector(nr);result=List();nontriv=0;
for(h=1,#KS,
 j=KS[h][3];u=Mod(1,NF.pol);
 for(i=1,nr,if(KK[i,j],if(!done[i],ti=4*((i-1)\4)+((i-1+2)%4)+1;UU[i]=GS[4][i]/GS[4][ti];done[i]=1);u*=UU[i]^KK[i,j]));
 if(idealhnf(NF,u)!=matid(24),error("not actual unit"));sgn=if(u==1,1,if(u==-1,-1,0));if(sgn==0,nontriv++;write("geometric_actual_units.gp",[j,KK[,j],u]));listput(result,[j,KS[h][1],KS[h][2],sgn]);
 if(h%10==0,print("GEOMETRIC_UNIT_PROGRESS;CHECKED=",h,";NONTORSION=",nontriv))
);
write("geometric_units_result.gp",[Vec(result),nontriv]);print("GEOMETRIC_UNITS_COMPLETE;KERNEL_DIM=",#KS,";NONTORSION=",nontriv,";PLUS_ONE=",#select(r->r[4]==1,Vec(result)),";MINUS_ONE=",#select(r->r[4]==-1,Vec(result)),";MS=",gettime());quit;
}
