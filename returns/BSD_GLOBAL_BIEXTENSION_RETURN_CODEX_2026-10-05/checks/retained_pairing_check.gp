\\ Independent implementation for a bounded normalization diagnostic.
\\ No original GP script, Pro Python code, modular symbols or BSD value is read.
E = ellinit([0,-1,0,-66020924,-65074271436]);
P = [[-3031,327384],[-2394,281520]];
for(i=1,2, if(!ellisoncurve(E,P[i]),error("input off curve")));

denx(Q) = {
  my(dx=denominator(Q[1]),d=sqrtint(dx));
  if(d*d!=dx,error("non-square x denominator"));
  d;
};
logp(u,l,p,g) = {
  if(lift(Mod(u,l))==0,error("non-unit in tame logarithm"));
  Mod(znlog(Mod(u,l),Mod(g,l)),p);
};
hformal(Q,l,p,g) = {
  my(d=denx(Q),a=Q[1]*d^2,b=Q[2]*d^3);
  if(d%l,error("not formal"));
  if(denominator(a)!=1 || denominator(b)!=1,error("nonintegral coordinates"));
  logp(-a/b,l,p,g);
};
divpair(A,B,R,l,p,g) = {
  my(AR=elladd(E,A,R), RB=ellsub(E,R,B), ARB=ellsub(E,AR,B));
  logp(denx(ARB)*denx(R)/(denx(AR)*denx(RB)),l,p,g);
};
onecase(p,l) = {
  my(El=ellinit([0,-1,0,-66020924,-65074271436],l),g=lift(znprimroot(l)));
  my(count=ellcard(El),m=2*lcm(ellorder(El,P[1]),ellorder(El,P[2])));
  if((l-1)%p || count%p==0 || m%p==0,error("inadmissible local test"));
  my(U=vector(2,i,ellmul(E,P[i],m)),H=matrix(2,2),B=matrix(2,2));
  H[1,1]=hformal(U[1],l,p,g); H[2,2]=hformal(U[2],l,p,g);
  H[1,2]=(hformal(elladd(E,U[1],U[2]),l,p,g)-H[1,1]-H[2,2])/2;
  H[2,1]=H[1,2];
  my(repeats=0);
  for(k=1,3,
    my(R=if(k<=2,P[k],elladd(E,P[1],P[2])));
    for(i=1,2,for(j=1,2,B[i,j]=divpair(U[i],U[j],R,l,p,g)));
    if(B!=2*H,error("factor two comparison failed"));
    repeats++;
  );
  for(i=1,2,
    if(hformal(ellmul(E,U[i],2),l,p,g)!=4*H[i,i],error("scaling failed"));
  );
  if(B==H,error("wrong factor not detected in this chosen test"));
  print("CASE ",[p,l,count,m,lift(H[1,1]),lift(H[1,2]),lift(H[2,2]),lift(matdet(H)),repeats]);
};
onecase(7,29);
onecase(11,23);
onecase(17,103);
print("PAIRING_CHECK_PASS cases=3 translation_choices=9 wrong_factor_rejected=3");
quit;
