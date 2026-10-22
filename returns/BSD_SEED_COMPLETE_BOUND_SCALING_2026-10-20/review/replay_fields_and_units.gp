{
alarm(50); gettime();
for(lane=1,2,
  my(path=if(lane==1,"../seed_five/","../same_curve_scaling/"));
  my(C=read(Str(path,"field.gp")),NF=read(Str(path,"nf.gp")));
  my(E=C[1],F=C[4],T=C[6],sig=C[7],n=poldegree(F),v=variable(F));
  if(n!=24 || !polisirreducible(F),error("field degree/irreducibility"));
  if(NF.pol!=F,error("integral basis field mismatch"));
  if(!ellisoncurve(E,T)||ellmul(E,T,5)!=[0],error("torsion point"));
  if([subst(lift(T[1]),v,sig),subst(lift(T[2]),v,sig)]!=ellmul(E,T,2),error("scalar action"));
  if(subst(F,v,sig)!=0,error("automorphism equation"));
  my(sig2=subst(lift(sig),v,sig),sig4=subst(lift(sig2),v,sig2));
  if(sig4!=Mod(v,F)||sig2==Mod(v,F),error("scalar order"));
  my(S=if(lane==1,[2,3,5,2243,4547,5843],[2,5,13]),dims=vector(#S));
  for(i=1,#S,
    my(PR=idealprimedec(NF,S[i]),H=vector(#PR,j,idealhnf(NF,PR[j])),P=matrix(#PR,#PR));
    for(j=1,#PR,
      my(a=nfgaloisapply(NF,sig,H[j]),matches=0);
      for(k=1,#PR,if(a==H[k],P[k,j]=1;matches++));
      if(matches!=1,error("unmatched prime ideal"))
    );
    if(P^4!=matid(#PR),error("ideal scalar order"));
    dims[i]=#matker(Mod(P-2*matid(#PR),5));
  );
  if(lane==1 && dims!=[0,0,0,1,0,0],error("seed divisor dimensions"));
  if(lane==2 && dims!=[0,0,0],error("fixed curve divisor dimensions"));
  print("FIELD_AND_DIVISOR_REPLAY=",lane,";DIMS=",dims,";DISC=",NF.disc);
);
NF=read("../same_curve_scaling/nf.gp");
FU=read("../same_curve_scaling/units_compact.gp")[1];
Q=read("../same_curve_scaling/AUTHENTICATION_DATA.gp");
FF=Q[1]; PP=Q[2]; DV=Q[3]; EX=Q[4];
if(#FU!=14 || matsize(EX)!=[#FF,13],error("unit dimensions"));
EE=matrix(#FF,13);
for(j=1,13,
  for(k=1,matsize(FU[j])[1],
    my(a=nfalgtobasis(NF,FU[j][k,1]),h=setsearch(FF,a));
    if(h==0,error("unit factor not bound"));
    EE[h,j]+=FU[j][k,2]
  )
);
if(EE!=EX,error("unit exponent binding"));
for(i=1,#FF,
  my(J=idealhnf(NF,1));
  for(k=1,#PP,if(DV[k,i],J=idealmul(NF,J,idealpow(NF,PP[k],DV[k,i]))));
  if(J!=idealhnf(NF,FF[i]),error("literal ideal factorization"))
);
if(DV*EX!=matrix(#PP,13),error("not actual ordinary units"));
print("THIRTEEN_ACTUAL_UNITS_REPLAYED;FACTORS=",#FF,";IDEALS=",#PP);
print("INDEPENDENT_FIELD_UNIT_REPLAY_PASS;MS=",gettime());quit;
}
