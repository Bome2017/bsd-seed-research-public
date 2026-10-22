ai(ID)=idealhnf(NF,SM*idealhnf(NF,ID));
addideal(ID)={my(nn=idealnorm(NF,ID),j=1,G,gn,old);if(nn==1,return());while(j<=#BB,if(gcd(nn,BN[j])==1,j++;next);G=idealadd(NF,ID,BB[j]);gn=idealnorm(NF,G);GC++;if(gn==1,j++;next);if(G==BB[j],ID=idealdiv(NF,ID,G);nn/=gn;if(nn==1,return());j=1;next);old=idealdiv(NF,BB[j],G);BB[j]=G;BN[j]=gn;addideal(old);addideal(idealdiv(NF,ID,G));return());listput(BB,ID);listput(BN,nn);};
{
alarm(115);gettime();C=read("/Users/bsm/BSD_SEED_COMPLETE_BOUND_SCALING_2026-10-20/seed_five/field.gp");NF=read("/Users/bsm/BSD_SEED_COMPLETE_BOUND_SCALING_2026-10-20/seed_five/nf.gp");SG=C[7];SM=matrix(24,24,i,j,nfalgtobasis(NF,subst(lift(NF.zk[j]),w,SG))[i]);if(SM^4!=matid(24)||denominator(SM)!=1,error("scalar action"));NR=readvec("norm_rows.gp");AA=List();II=List();DD=List();DN=List();BB=List();BN=List();GC=0;
for(i=1,#NR,a=NR[i][3];for(k=0,3,d=denominator(nfalgtobasis(NF,a));ID=idealhnf(NF,d*a);DI=idealhnf(NF,d);if(denominator(ID)!=1||idealdiv(NF,ID,DI)!=idealhnf(NF,a),error("denominator binding"));listput(AA,a);listput(II,ID);listput(DD,DI);listput(DN,d);addideal(DI);addideal(ID);a=subst(lift(a),w,SG));print("GEOMETRIC_GCD_PROGRESS;FUNCTION=",i,";ATOMS=",#BB));
B=Vec(BB);BN=Vec(BN);for(i=1,#B,for(j=i+1,#B,if(gcd(BN[i],BN[j])>1&&idealadd(NF,B[i],B[j])!=matid(24),error("not coprime support"))));MM=Map();for(i=1,#B,mapput(MM,Str(B[i]),i));PM=vector(#B);for(i=1,#B,if(!mapisdefined(MM,Str(ai(B[i])),&j),error("scalar support not permutation"));PM[i]=j);
write("geometric_support.gp",[C[4],SG,SM,Vec(AA),Vec(II),Vec(DD),Vec(DN),B,BN,PM]);
print("GEOMETRIC_GCD_COMPLETE;ELEMENTS=",#AA,";ATOMS=",#B,";GCDS=",GC,";MS=",gettime());quit;
}
