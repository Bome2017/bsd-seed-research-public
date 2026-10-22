\\ Library: complete enumeration of points of naive height <= Hlog on the REDUCED minimal model Er,
\\ via the 2-isogeny parametrisation on the original model E0: y^2 = x(x^2 + a x + b), x = x' + 7578.
\\ Every P=(m/e^2, n/e^3) (lowest terms, x!=0) has m = s*M^2 with s a squarefree divisor of b (sign incl.),
\\ and (X,W) = (M/e, N/e^2) on W^2 = s X^4 + a X^2 + b/s.  h'(P) <= Hlog  ==>  e^2 <= exp(Hlog), |m| <= (1+7578)*exp(Hlog).
m0=2243; n0=12; A=m0+16*n0^2; B=m0+25*n0^2;
aa=-5*A; bb=4*A*B; SH=7578;
E0=ellinit([0,aa,0,bb,0]);
Er=ellinit([0,-1,0,-66020924,-65074271436]);
naiveh(Pr)=my(x=Pr[1]); log(max(abs(numerator(x)),denominator(x)));
toR(P)=[P[1]-SH,P[2]];
sqfdivs()={my(L=List()); foreach([1,2,A,2*A,B,2*B,A*B,2*A*B],d, listput(L,d); listput(L,-d)); Vec(L)};
enumpts(Hlog)={
  my(eH=exp(Hlog), emax=floor(sqrt(eH))+1, res=List(), cnt=0);
  foreach(sqfdivs(), s,
    my(Mmax=floor(sqrt((SH+1)*eH/abs(s)))+1, Q=s*'X^4+aa*'X^2+bb/s, pts);
    pts=hyperellratpoints(Q,[Mmax,min(emax,Mmax)]);
    foreach(pts, pt, my(X=pt[1], x=s*X^2, P, Pr);
      if(x==0, next);
      if(!issquare(x^3+aa*x^2+bb*x), error("not on curve"));
      P=[x, sqrtint(numerator(x^3+aa*x^2+bb*x))/sqrtint(denominator(x^3+aa*x^2+bb*x))];
      if(!ellisoncurve(E0,P), error("bad point"));
      Pr=toR(P);
      if(naiveh(Pr)<=Hlog, listput(res,Pr)));
    cnt+=#pts);
  \\ add the 2-torsion point x=0 (x'=-7578) explicitly
  listput(res,[-SH,0]);
  res=Set(apply(P->[P[1],abs(P[2])],Vec(res)));
  [res,cnt]
};
brute(Hlog)={ \\ naive brute force directly on Er for validation (small Hlog only)
  my(eH=floor(exp(Hlog)), res=List());
  for(e=1,sqrtint(eH), for(mm=-eH,eH, if(gcd(mm,e)!=1,next); my(x=mm/e^2, r=x^3-x^2-66020924*x-65074271436);
     if(r>=0 && issquare(r), listput(res,[x,sqrtint(numerator(r))/sqrtint(denominator(r))]))));
  Set(Vec(res))
};
