{
alarm(120);default(realprecision,64);
NF=read("seed_nf.gp");FS=read("relative_fields.gp");NK=read("nf12.gp");
if(NF.pol!=FS[1]||NK.pol!=FS[6],error("field binding"));
SG=FS[3];SM=matrix(24,24);for(j=1,24,SM[,j]=nfalgtobasis(NF,subst(lift(NF.zk[j]),w,SG)));TM=SM^2;
if(SM^4!=matid(24)||denominator(SM)!=1,error("scalar integrity"));
DR=abs(NF.disc/NK.disc^2);cut=0;while((cut+1)^10<DR,cut++);
if(cut!=242,error("unexpected bound"));
rows=List();pairs=List();skipped=List();
forprime(q=2,cut,
 PP=idealprimedec(NF,q);HH=vector(#PP,j,idealhnf(NF,PP[j]));TP=vector(#PP);SP=vector(#PP);
 for(j=1,#PP,
  J=idealhnf(NF,TM*HH[j]);Z=idealhnf(NF,SM*HH[j]);hit=0;shi=0;
  for(k=1,#PP,if(J==HH[k],TP[j]=k;hit++);if(Z==HH[k],SP[j]=k;shi++));
  if(hit!=1||shi!=1,error("prime action"))
 );
 for(j=1,#PP,
  nn=q^PP[j][4];if(nn>cut,next);
  listput(rows,[q,j,PP[j][3],PP[j][4],nn,TP[j],SP[j]]);
  if(TP[j]!=j&&j<TP[j],
    if(PP[j][3]!=1,listput(skipped,[q,j,TP[j],"absolute ramification"]),
      listput(pairs,[q,j,TP[j],PP[j][4],nn,HH[j],HH[TP[j]]]))
  )
 )
);
write("split_prime_data.gp",[DR,cut,Vec(rows),Vec(pairs),Vec(skipped)]);
print("SMALL_SPLIT_COMPLETE;cut=",cut,";primeideals=",#rows,";unramifiedpairs=",#pairs,";skippedpairs=",#skipped);
print("PAIR_SUMMARY=",vector(#pairs,j,pairs[j][1..5]));
quit;
}
