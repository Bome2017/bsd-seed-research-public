{
alarm(60);K=read("nf12.gp");FS=read("relative_fields.gp");rad=Mod(-polcoef(FS[9],0,x),K.pol);R=List();all=List();
forprime(q=2,242,
 if(K.disc%q==0||q==5,next);
 P=idealprimedec(K,q);
 for(j=1,#P,
  nn=q^P[j][4];if(nn>242,next);
  mp=nfmodprinit(K,P[j]);a=nfmodpr(K,rad,mp);
  if(a==0,error("unexpected quadratic ramification"));
  sq=issquare(a);listput(all,[q,j,P[j][4],nn,sq]);
  if(sq,listput(R,[q,j,P[j][4],nn]))
 )
);
print([Vec(R),Vec(all)]);quit;
}
