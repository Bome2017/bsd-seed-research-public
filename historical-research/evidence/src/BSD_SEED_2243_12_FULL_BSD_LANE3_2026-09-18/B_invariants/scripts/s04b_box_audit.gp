\\ AUDIT_B correction #1: compare the pre-audit (truncated) box [Mmax, min(emax,Mmax)] with the full box [Mmax, emax]
\\ for every quartic where they differ (Mmax < emax, i.e. |s| > 7579), at every search height used in B.4.
\\ Every extra X found by the full box is turned into a point of E_r, its naive height is printed, and it is identified
\\ as a*P1 + b*P2 + e*T (|a|,|b| <= 6) when possible.
read("scripts/s04b_enum_lib.gp");
default(realprecision,40);
hQ(q)=log(max(abs(numerator(q)),abs(denominator(q))));
hinf(q)=log(max(1,abs(q)));
j=Er.j; D=Er.disc; b2=Er.b2;
mu=hQ(D)/12+hinf(j)/12+hinf(b2/12)/2+log(if(b2,2,1))/2;
Bs1=2*(hQ(j)/8+hQ(D)/12+0.973); Bs2=2*(hQ(j)/12+hQ(D)/12+1.07); Bm1=2*(hQ(j)/24+mu+0.973); Bm2=2*(mu+1.07);
Bmax=vecmax([Bs1,Bs2,Bm1,Bm2]);
Q1=toR([A,6*n0*A]); Q2=toR([36*n0^2,12*n0*(m0-2*n0^2)]); TT=[-SH,0];
ident(Pr)={my(Pp=[Pr[1],abs(Pr[2])]); for(a=-6,6, for(b=-6,6, for(e=0,1, my(P=elladd(Er, elladd(Er, ellmul(Er,Q1,a), ellmul(Er,Q2,b)), ellmul(Er,TT,e))); if(P!=[0] && [P[1],abs(P[2])]==Pp, return([a,b,e]))))); 0};
Hs=[11.0, 18.979, 20.679, 2.5+Bm1, 4.2+Bm1, 2.5+Bmax, 4.2+Bmax];
print("Bm1 (refined, 0.973) = ",Bm1,"   Bmax = ",Bmax);
{
foreach(Hs, H,
  my(eH=exp(H), emax=floor(sqrt(eH))+1, extras=0, extras_in=0, naff=0);
  foreach(sqfdivs(), s,
    my(Mmax=floor(sqrt((SH+1)*eH/abs(s)))+1, Q=s*'X^4+aa*'X^2+bb/s, po, pn, Xo, Xn, ex);
    if(Mmax>=emax, next);
    naff++;
    po=hyperellratpoints(Q,[Mmax,min(emax,Mmax)]);
    pn=hyperellratpoints(Q,[Mmax,emax]);
    Xo=Set(apply(p->p[1],po)); Xn=Set(apply(p->p[1],pn));
    if(#setminus(Xo,Xn)>0, error("old-box point missing from the full box"));
    ex=setminus(Xn,Xo);
    print("H=",H," s=",s," Mmax=",Mmax," emax=",emax," raw old=",#po," raw new=",#pn," distinct X old=",#Xo," new=",#Xn," extra X=",#ex);
    foreach(ex, X, my(x=s*X^2, r, P, Pr, h);
      if(x==0, next);
      r=x^3+aa*x^2+bb*x;
      if(!issquare(r), error("not on curve"));
      P=[x, sqrtint(numerator(r))/sqrtint(denominator(r))];
      if(!ellisoncurve(E0,P), error("bad point"));
      Pr=toR(P); h=naiveh(Pr);
      print("    extra X=",X,"  x_r=",Pr[1],"  h_r=",h,"  h_r<=H: ",h<=H,"  combo [a,b,e] (up to sign) = ",ident(Pr));
      extras++; if(h<=H, extras_in++)));
  print("SUMMARY H=",H,": quartics with a truncated denominator range = ",naff,"; extra X values found by the full box = ",extras,", of which with h_r <= H: ",extras_in);
);
}
