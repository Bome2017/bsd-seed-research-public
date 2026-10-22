read("relative_setup.gp");
addideal(ID) = {
  my(nn=idealnorm(NF,ID),jj=1,G,gn,old);
  if(nn==1,return());
  while(jj<=#BB,
    if(gcd(nn,BN[jj])==1,jj++;next);
    G=idealadd(NF,ID,BB[jj]);gn=idealnorm(NF,G);GC++;
    if(gn==1,jj++;next);
    if(G==BB[jj],ID=idealdiv(NF,ID,G);nn=nn/gn;if(nn==1,return());jj=1;next);
    old=idealdiv(NF,BB[jj],G);BB[jj]=G;BN[jj]=gn;
    addideal(old);addideal(idealdiv(NF,ID,G));return()
  );
  listput(BB,ID);listput(BN,nn)
};
{
alarm(295);gettime();relative_setup();BR=readvec("batch_rows.gp");UM=Map();UL=List();ULN=List();BB=List();BN=List();GC=0;
for(i=1,#ORB,for(k=1,4,ID=ORB[i][4][k];addideal(ID)));
for(i=1,#BR,ID=BR[i][7];for(k=0,3,key=Str(ID);if(!mapisdefined(UM,key),mapput(UM,key,1);listput(UL,ID);listput(ULN,idealnorm(NF,ID)));ID=ai(ID)));
VV=Vec(UL);VN=Vec(ULN);ord=vecsort(vector(#VV,i,[VN[i],i]),1);
print("GCD_START;RESIDUALS=",#VV,";INITIAL_BASIS=",#BB);
for(i=1,#VV,
  addideal(VV[ord[i][2]]);
  if(i%25==0,print("GCD_PROGRESS;DONE=",i,";ATOMS=",#BB,";GCDS=",GC);write("gcd_checkpoint.gp",[i,Vec(BB),Vec(BN),GC]))
);
B=Vec(BB);BN=Vec(BN);
for(i=1,#B,for(j=i+1,#B,if(gcd(BN[i],BN[j])>1&&idealadd(NF,B[i],B[j])!=matid(24),error("support not pairwise coprime"))));
MM=Map();for(i=1,#B,mapput(MM,Str(B[i]),i));PM=vector(#B);
for(i=1,#B,if(!mapisdefined(MM,Str(ai(B[i])),&jj),error("scalar action not a permutation of gcd basis"));PM[i]=jj);
write("gcd_basis.gp",[B,BN,PM]);
write("gcd_result.gp",[#VV,#B,GC]);
print("GCD_REFINEMENT_COMPLETE;RESIDUALS=",#VV,";ATOMS=",#B,";GCDS=",GC,";MS=",gettime());quit;
}
