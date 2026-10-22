{alarm(57);gettime();NF=read("../p7_arithmetic/nf.gp");n=poldegree(NF.pol);ID=matid(n);seen=Map();units=List();logs=List();ct=0;
for(ai=2,9,aa=vector(n,j,j==ai)~;II=idealhnf(NF,aa);
for(k=1,2,for(j=1,NF.r1+NF.r2,
 vv=vector(NF.r1+NF.r2,i,if(i==j,[32,96][k],0));RR=idealred(NF,[II,1],vv);JJ=RR[1];tt=RR[2];
 if(idealmul(NF,JJ,idealhnf(NF,tt))!=II,error("principal relation"));
 gg=nfeltdiv(NF,aa,tt);if(idealhnf(NF,gg)!=JJ,error("ideal generator"));
 key=Str(JJ);un=0;if(mapisdefined(seen,key,&old),uu=nfeltdiv(NF,gg,old);ua=nfbasistoalg(NF,uu);if(ua!=1&&ua!=-1,if(idealhnf(NF,uu)!=ID,error("unit auth"));listput(units,uu);un=1),mapput(seen,key,gg));
 ct++;listput(logs,[ai,k,j,idealnorm(NF,JJ),un]);
 if(un,write("walk_units_checkpoint.gp",Vec(units)));write("walk_progress.gp",[ct,#units,idealnorm(NF,JJ)]);
 )));
write("walk_units.gp",Vec(units));write("walk_rows.gp",Vec(logs));print("PRINCIPAL_IDEAL_WALK_COMPLETE;REDUCTIONS=",ct,";UNITS=",#units,";MS=",gettime());quit;}
