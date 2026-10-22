{alarm(70);gettime();NF=read("../p7_arithmetic/nf.gp");N=poldegree(NF.pol);I=matid(N);seen=Map();units=List();logs=List();ct=0;
for(k=1,4,for(j=1,NF.r1+NF.r2,
 vv=vector(NF.r1+NF.r2,i,if(i==j,[16,32,64,96][k],0));
 RR=idealred(NF,[I,1],vv);J=RR[1];t=RR[2];
 if(idealhnf(NF,nfeltmul(NF,t,1))!=idealinv(NF,J),error("extended ideal convention"));
 key=Str(J);un=0;
 if(mapisdefined(seen,key,&old),u=nfeltdiv(NF,t,old);if(u!=1&&u!=-1,if(idealhnf(NF,u)!=I,error("unit identity"));listput(units,u);un=1),mapput(seen,key,t));
 ct++;listput(logs,[k,j,idealnorm(NF,J),un]);
 write("progress.gp",[ct,#units,idealnorm(NF,J)]);
 ));
write("units.gp",Vec(units));write("rows.gp",Vec(logs));print("REDUCED_IDEAL_UNIT_SEARCH_COMPLETE;REDUCTIONS=",ct,";UNITS=",#units,";MS=",gettime());quit;}
