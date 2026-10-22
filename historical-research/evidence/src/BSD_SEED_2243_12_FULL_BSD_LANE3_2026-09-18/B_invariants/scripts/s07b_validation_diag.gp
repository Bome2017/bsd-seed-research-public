\\ AUDIT_B note #3 diagnostic (dead route, cited by no claim): why did out/s07b_Eprime_enum.out print "equal: 0" at H = 10.5?
\\ Recompute the E' enumeration at H = 10.5 with the truncated box [Mmax,min(Dmax,Mmax)] (as in scripts/s07b_Eprime_enum.gp),
\\ with the full box [Mmax,Dmax], and by brute force on the reduced model; print all three sets and their differences.
m0=2243; n0=12; A=m0+16*n0^2; B=m0+25*n0^2;
aa=10*A; bb=9*m0*A; SH=-15157;
E0=ellinit([0,aa,0,bb,0]);
Er=ellinit([0,-1,0,-597383344,5572681004764]);
print("reduced model check: ",ellinit(ellminimalmodel(E0)[1..5])[1..5]==Er[1..5]);
toR(P)=[P[1]-SH,P[2]];
naiveh(P)=log(max(abs(numerator(P[1])),denominator(P[1])));
sqfd=[1,3,m0,3*m0,A,3*A,m0*A,3*m0*A]; sgn_s=concat(sqfd,-sqfd);
en(Hl,full)={my(eH=exp(Hl), L=List()); foreach(sgn_s, s, my(Mmax=floor(sqrt((abs(SH)+1)*eH/abs(s)))+1, Dmax=floor(sqrt(eH))+1, Q=s*'X^4+aa*'X^2+bb/s, raw); raw=hyperellratpoints(Q,[Mmax,if(full,Dmax,min(Dmax,Mmax))]); foreach(raw, pt, my(X=pt[1], x=s*X^2, r2, P); if(x==0,next); r2=x^3+aa*x^2+bb*x; P=[x, sqrtint(numerator(r2))/sqrtint(denominator(r2))]; if(!ellisoncurve(E0,P),error("bad")); P=toR(P); if(naiveh(P)<=Hl, listput(L,[P[1],abs(P[2])])))); listput(L,[-SH,0]); Set(Vec(L))};
Hv=10.5;
et=en(Hv,0); ef=en(Hv,1);
print("truncated box: ",et); print("full box:      ",ef);
print("T' = ",[-SH,0]," on Er: ",ellisoncurve(Er,[-SH,0]));
bf=List(); eHv=floor(exp(Hv));
{for(e=1,sqrtint(eHv), for(mm=-eHv,eHv, if(gcd(mm,e)!=1,next); my(x=mm/e^2, r=x^3+Er.a2*x^2+Er.a4*x+Er.a6); if(r>=0 && issquare(r), listput(bf,[x,sqrtint(numerator(r))/sqrtint(denominator(r))]))));}
bf=Set(Vec(bf));
print("brute force:   ",bf);
print("brute - truncated = ",setminus(bf,et),"   truncated - brute = ",setminus(et,bf));
print("brute - full      = ",setminus(bf,ef),"   full - brute      = ",setminus(ef,bf));
print("equal(brute, full box): ",bf==ef);
