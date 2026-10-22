decomp(ID)={my(v=vector(#B),nn=idealnorm(NF,ID),G);for(j=1,#B,if(gcd(nn,BN[j])==1,next);while(gcd(nn,BN[j])>1,G=idealadd(NF,ID,B[j]);if(G==matid(24),break);if(G!=B[j],error("atom does not reconstruct"));ID=idealdiv(NF,ID,B[j]);nn/=BN[j];v[j]++));if(ID!=matid(24)||nn!=1,error("lost support"));v;};
proj(v,c)={my(r=vector(NC));for(j=1,#B,if(CI[j],r[CI[j]]+=c^CP[j]*v[j]));lift(Mod(r,5));};
{
alarm(115);gettime();NF=read("/Users/bsm/BSD_SEED_COMPLETE_BOUND_SCALING_2026-10-20/seed_five/nf.gp");GS=read("geometric_support.gp");B=GS[8];BN=GS[9];PM=GS[10];CI=vector(#B);CP=vector(#B);seen=vector(#B);CYC=List();NC=0;
for(i=1,#B,if(seen[i],next);cy=List();j=i;while(!seen[j],seen[j]=1;listput(cy,j);j=PM[j]);if(j!=i,error("scalar cycle"));if(#cy==4,NC++;for(k=1,4,CI[cy[k]]=NC;CP[cy[k]]=k-1));listput(CYC,Vec(cy)));
EV=matrix(#GS[4],#B);R2=matrix(#GS[4],NC);R3=matrix(#GS[4],NC);for(i=1,#GS[4],EV[i,]=decomp(GS[5][i])-decomp(GS[6][i]);R2[i,]=proj(EV[i,],2);R3[i,]=proj(EV[i,],3));
OUT=List();IN=List();SC=List();PPM=Map();amb=List();
for(h=1,NC,
 j=0;for(k=1,#B,if(CI[k]==h,j=k;break));FF=factor(BN[j],419776);BI=matid(24);cert=0;
 for(i=1,matsize(FF)[1],q=FF[i,1];if(q>419775,next);if(!mapisdefined(PPM,q,&PP),PP=idealprimedec(NF,q);mapput(PPM,q,PP));for(k=1,#PP,v=idealval(NF,B[j],PP[k]);if(v&&q^PP[k][4]<=419775,BI=idealmul(NF,BI,idealpow(NF,PP[k],v))));
 );
 OI=idealdiv(NF,B[j],BI);on=idealnorm(NF,OI);if(on==1,listput(IN,h),listput(OUT,h));
 if(on!=1&&ispower(on,5),
  for(i=1,matsize(FF)[1],q=FF[i,1];if(q>419775,next);PP=mapget(PPM,q);for(k=1,#PP,if(q^PP[k][4]>419775&&idealval(NF,OI,PP[k])%5,cert=1)));
  if(!cert,listput(amb,h))
 );
 listput(SC,[h,j,BN[j],FF,BI,OI,on]);
);
IN=Vec(IN);OUT=Vec(OUT);rk2=matrank(Mod(R2,5));rk3=matrank(Mod(R3,5));ok2=if(#OUT,matrank(Mod(vecextract(R2,vector(#GS[4],j,j),OUT),5)),0);ok3=if(#OUT,matrank(Mod(vecextract(R3,vector(#GS[4],j,j),OUT),5)),0);
write("geometric_rank_data.gp",[Vec(CYC),CI,CP,EV,R2,R3,IN,OUT,Vec(SC),Vec(amb)]);
write("geometric_rank_result.gp",[#GS[4],#B,NC,#IN,#OUT,rk2,rk3,ok2,ok3,rk2-ok2,rk3-ok3,Vec(amb)]);
print("GEOMETRIC_RANK_COMPLETE;ELEMENTS=",#GS[4],";ATOMS=",#B,";FAITHFUL_COLUMNS=",NC,";INSIDE=",#IN,";OUTSIDE=",#OUT,";FULL_RANK=",[rk2,rk3],";OUTSIDE_RANK=",[ok2,ok3],";NET_CLOSED_RANK=",[rk2-ok2,rk3-ok3],";AMBIGUOUS_OUTSIDE_FIFTHS=",Vec(amb),";MS=",gettime());quit;
}
