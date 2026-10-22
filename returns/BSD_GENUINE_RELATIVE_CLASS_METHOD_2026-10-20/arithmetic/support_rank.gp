read("relative_setup.gp");
decomp(ID) = {
  my(v=vector(#B),nn=idealnorm(NF,ID),G);
  if(denominator(ID)!=1,error("decompose nonintegral"));
  for(j=1,#B,
    if(gcd(nn,BN[j])==1,next);
    while(gcd(nn,BN[j])>1,
      G=idealadd(NF,ID,B[j]);if(G==matid(24),break);
      if(G!=B[j],error("gcd atom does not reconstruct input"));
      ID=idealdiv(NF,ID,B[j]);nn=nn/BN[j];v[j]++
    )
  );
  if(ID!=matid(24)||nn!=1,error("unretained divisor support"));v
};
project(v,chi) = {
  my(r=vector(NC));for(j=1,#B,if(CI[j],r[CI[j]]+=chi^CP[j]*v[j]));lift(Mod(r,5))
};
{
alarm(295);gettime();relative_setup();BR=readvec("batch_rows.gp");GB=read("gcd_basis.gp");B=GB[1];BN=GB[2];PM=GB[3];seen=vector(#B);CI=vector(#B);CP=vector(#B);CYC=List();NC=0;
for(i=1,#B,
 if(seen[i],next);cyc=List();j=i;while(!seen[j],seen[j]=1;listput(cyc,j);j=PM[j]);if(j!=i,error("scalar orbit closure"));
 if(#cyc==4,NC++;for(k=1,4,CI[cyc[k]]=NC;CP[cyc[k]]=k-1));listput(CYC,Vec(cyc))
);
EV=matrix(#BR,#B);R2=matrix(#BR,NC);R3=matrix(#BR,NC);OV=matrix(#ORB,#B);
for(i=1,#ORB,OV[i,]=decomp(idealhnf(NF,ORB[i][2])));
for(i=1,#BR,
 v=BR[i][3]*OV-decomp(BR[i][7]);EV[i,]=v;
 R2[i,]=project(v,2);R3[i,]=project(v,3);
 if(i%25==0,print("SUPPORT_RANK_PROGRESS;ROW=",i))
);
OI=List();for(i=1,#ORB,v=project(OV[i,],2);nz=select(j->v[j]!=0,vector(NC,j,j));if(#nz!=1,error("original column not unique"));listput(OI,nz[1]));OI=Set(Vec(OI));if(#OI!=#ORB,error("original orbits not distinct"));PI=setminus(vector(NC,j,j),OI);
RK2=matrank(Mod(R2,5));RK3=matrank(Mod(R3,5));PR2=if(#PI,matrank(Mod(vecextract(R2,vector(#BR,j,j),PI),5)),0);PR3=if(#PI,matrank(Mod(vecextract(R3,vector(#BR,j,j),PI),5)),0);
write("support_matrices.gp",[B,PM,Vec(CYC),CI,CP,OI,PI,EV,R2,R3,OV]);
write("support_result.gp",[#BR,#B,NC,#OI,#PI,RK2,RK3,PR2,PR3,RK2-PR2,RK3-PR3]);
print("SUPPORT_RANK_COMPLETE;ROWS=",#BR,";ATOMS=",#B,";FAITHFUL_COLUMNS=",NC,";ORIGINAL=",#OI,";PRIVATE=",#PI,";RANK2=",RK2,";RANK3=",RK3,";ELIMINATED_PRIVATE_RANK2=",RK2-PR2,";ELIMINATED_PRIVATE_RANK3=",RK3-PR3,";MS=",gettime());quit;
}
