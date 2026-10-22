{
alarm(18);gettime();
NF=read("/Users/bsm/BSD_SEED_COMPLETE_BOUND_SCALING_2026-10-20/seed_five/nf.gp");
F=read("/Users/bsm/BSD_SEED_COMPLETE_BOUND_SCALING_2026-10-20/seed_five/field.gp")[4];
if(NF.pol!=F,error("seed field binding"));
Bound=419775; Limits=[4813,12034,24068,48136,419775];
KC=vector(#Limits);KCZ=vector(#Limits);Num=0;IndexCases=0;
forprime(q=2,Bound,
  Num++;
  if(NF.index%q,
    ds=factormod(F,q,1)[,1],
    IndexCases++; L=idealprimedec(NF,q); ds=vector(#L,j,L[j][4])
  );
  k=0;for(j=1,#ds,if(q^ds[j]<=Bound,k++));
  if(k,for(j=1,#Limits,if(q<=Limits[j],KC[j]+=k;KCZ[j]++)))
);
if(KC[1]!=721 || KCZ[1]!=175,error("small-base cross-check disagrees with actual FBgen"));
R=[Bound,Limits,Num,IndexCases,KC,KCZ,vector(#Limits,j,8*KC[j]^2)];
write("default_kc_count_result.gp",R);
print("DEFAULT_KC_COUNT_COMPLETE;RESULT=",R,";MS=",gettime());quit;
}
