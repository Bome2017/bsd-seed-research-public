ai(ID) = idealhnf(NF,SM*idealhnf(NF,ID));
ti(ID) = idealhnf(NF,TM*idealhnf(NF,ID));
ta(a) = subst(lift(a),w,TA);
contentideal(ID) = {
  my(C=idealadd(NF,ID,ti(ID)),v);
  for(j=1,#RAM,v=idealval(NF,C,RAM[j]);if(v%2,C=idealdiv(NF,C,RAM[j])));
  if(ti(C)!=C,error("base content not tau invariant"));
  if(!issquare(idealnorm(NF,C)),error("base content norm not square"));
  C;
};
relative_setup() = {
  default(realprecision,128);
  NF=nfnewprec(read("/Users/bsm/BSD_SEED_COMPLETE_BOUND_SCALING_2026-10-20/seed_five/nf.gp"));
  FS=read("/Users/bsm/BSD_RELATIVE_UNIT_CLASS_ALTERNATIVE_2026-10-20/relative_source/fields.gp");
  N12=read("/Users/bsm/BSD_RELATIVE_UNIT_CLASS_ALTERNATIVE_2026-10-20/relative_source/nf12.gp");
  if(NF.pol!=FS[1]||N12.pol!=FS[6],error("field binding"));
  SG=FS[3];TA=subst(lift(SG),w,SG);ZP=FS[7];
  SM=matrix(24,24);for(j=1,24,SM[,j]=nfalgtobasis(NF,subst(lift(NF.zk[j]),w,SG)));
  TM=SM^2;
  if(SM^4!=matid(24)||denominator(SM)!=1||abs(matdet(SM))!=1,error("scalar action"));
  RAM=List();RD=List();
  for(k=1,3,
    q=[2,5,4547][k];PA=idealprimedec(NF,q);PB=idealprimedec(N12,q);
    for(i=1,#PA,
      hit=0;er=0;
      for(j=1,#PB,
        aa=subst(lift(nfbasistoalg(N12,PB[j][2])),y,ZP);
        if(idealval(NF,aa,PA[i])>0,hit++;er=PA[i][3]/PB[j][3])
      );
      if(hit!=1||!(er==1||er==2),error("relative contraction or ramification"));
      if(er==2,listput(RAM,PA[i]));listput(RD,[q,i,PA[i][3],PA[i][4],er])
    )
  );
  RAM=Vec(RAM);RD=Vec(RD);
  ORB=List();
  forprime(q=7,101,
    if(NF.disc%q==0,next);
    PP=idealprimedec(NF,q);HH=vector(#PP,j,idealhnf(NF,PP[j]));PM=vector(#PP);seen=vector(#PP);
    for(j=1,#PP,JJ=ai(HH[j]);hit=0;for(k=1,#PP,if(JJ==HH[k],PM[j]=k;hit++));if(hit!=1,error("prime action")));
    for(j=1,#PP,
      if(seen[j],next);cyc=List();k=j;
      while(!seen[k],seen[k]=1;listput(cyc,k);k=PM[k]);
      if(k!=j,error("prime orbit closure"));
      if(#cyc==4&&q^PP[j][4]<=50000,listput(ORB,[q,PP[j],Vec(cyc),vector(4,h,HH[cyc[h]])]));
      if(#ORB>=8,break)
    );
    if(#ORB>=8,break)
  );
  ORB=Vec(ORB);
  write("setup_data.gp",[SM,RAM,RD,ORB]);
  print("RELATIVE_SETUP;RAMIFIED_PRIMES=",#RAM,";ORBITS=",#ORB,";ORBIT_NORMS=",vector(#ORB,j,idealnorm(NF,ORB[j][2])));
};

shortstep(J,v) = {
  my(R=idealred(NF,[J,1],v),a,P,C,K,sgn);
  a=nfbasistoalg(NF,R[2]);P=idealhnf(NF,a);
  if(idealmul(NF,R[1],P)==J,sgn=1,
    if(idealmul(NF,J,P)==R[1],a=1/a;P=idealhnf(NF,a);sgn=-1,error("idealred multiplier identity")));
  C=contentideal(R[1]);K=idealdiv(NF,R[1],C);
  if(denominator(K)!=1||idealmul(NF,idealmul(NF,P,C),K)!=J,error("relative reduced invariant"));
  [K,a,C,sgn];
};
