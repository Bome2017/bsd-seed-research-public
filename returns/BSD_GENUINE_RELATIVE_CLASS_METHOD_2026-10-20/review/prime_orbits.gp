clens(pm)={my(seen=vector(#pm),ls=List());for(j=1,#pm,if(!seen[j],my(k=j,n=0);while(!seen[k],seen[k]=1;n++;k=pm[k]);if(k!=j,error("nonpermutation cycle"));listput(ls,n)));Vec(ls)};
polyperm(F,sp,q,B)={my(ff=factormod(F,q)[,1],ind=select(j->q^poldegree(ff[j])<=B,vector(#ff,j,j)),fs=vector(#ind,j,ff[ind[j]]),pm=vector(#fs),x=variable(F));for(j=1,#fs,my(t=Mod(Mod(1,q)*sp,fs[j]),k=0);for(h=1,#fs,if(poldegree(fs[j])==poldegree(fs[h]) && subst(fs[h],x,t)==0,k=h));if(!k,error("poly scalar unmatched"));pm[j]=k);clens(pm)};
idealperm(NF,SIG,q,B)={my(ps=idealprimedec(NF,q),ind=select(j->q^ps[j][4]<=B,vector(#ps,j,j)),hs=vector(#ind,j,idealhnf(NF,ps[ind[j]])),pm=vector(#hs));for(j=1,#hs,my(h=nfgaloisapply(NF,SIG,hs[j]),k=0);for(t=1,#hs,if(h==hs[t],k=t));if(!k,error("ideal scalar unmatched"));pm[j]=k);clens(pm)};
{
alarm(55);gettime(); S=read("/Users/bsm/BSD_SEED_COMPLETE_BOUND_SCALING_2026-10-20/seed_five/field.gp"); NF=read("/Users/bsm/BSD_SEED_COMPLETE_BOUND_SCALING_2026-10-20/seed_five/nf.gp"); F=S[4];SIG=S[7];sp=lift(SIG);B=419775;
if(NF.pol!=F || denominator(sp)!=1,error("source binding"));
PRE=List();forprime(q=2,97,if(NF.index%q,my(a=vecsort(polyperm(F,sp,q,B)),b=vecsort(idealperm(NF,SIG,q,B)));if(a!=b,error("poly/ideal mismatch"));listput(PRE,[q,a,b])));
print("POLY_IDEAL_PREFLIGHT=",#PRE);write("prime_orbits_preflight.gp",Vec(PRE));
ROWS=List();TOTAL=0;IDEALS=0;NQ=0;IDX=0;forprime(q=2,B,
 NQ++;my(ls=if(NF.index%q,polyperm(F,sp,q,B),IDX++;idealperm(NF,SIG,q,B)),c=sum(j=1,#ls,ls[j]==4));
 if(vecsum(ls)<0,error("count"));IDEALS+=vecsum(ls);TOTAL+=c;if(c || !(NF.index%q),listput(ROWS,[q,c,ls,NF.index%q==0]));
);
if(IDEALS!=35749 ||NQ!=35373 || IDX!=10,error("complete inventory mismatch"));
write("prime_orbits_result.gp",[B,TOTAL,IDEALS,NQ,IDX,Vec(ROWS)]); print("PRIME_ORBITS_COMPLETE;CHI_COLUMNS=",TOTAL,";IDEALS=",IDEALS,";ROWS=",#ROWS,";MS=",gettime());quit;
}
