\\ DEAD ROUTE (AUDIT_B note #3, 2026-09-18): never completed, cited by no claim; 7d is proved via the Kummer map instead.
\\ out/s07b_Eprime_enum.out comes from an EARLIER version of this file (the killed 11:06 launch) and its "equal: 0" line is not
\\ reproducible from this file; see scripts/s07b_validation_diag.gp / out/s07b_validation_diag.out. The box truncation shared with
\\ s04b_enum_lib.gp was corrected below for hygiene only; this file has not been rerun.
\\ Step 7b: E' = [0,45470,0,91790289,0]. Route (b): Silverman bound (max of both published forms) + complete enumeration via the
\\ 16 quartics W^2 = s X^4 + a X^2 + b/s (s | b squarefree, signed) + Hermite => index of the eclib-saturated basis.
\\ Append-only checkpoint: one line per completed (H, s) block in out/s07b_enum_ckpt.gp (gp-readable); a restart skips those blocks.
m0=2243; n0=12; A=m0+16*n0^2; B=m0+25*n0^2;
aa=10*A; bb=9*m0*A; SH=-15157;          \\ x_E' = x_r + SH  (ellminimalmodel change [1,-15157,0,0])
E0=ellinit([0,aa,0,bb,0]);
M=ellminimalmodel(E0,&ch); print("minimal model change = ",ch,"  reduced model = ",M[1..5]);
if(ch!=[1,SH,0,0], error("unexpected change of variables"));
Er=ellinit(M[1..5]);
toR(P)=[P[1]-SH,P[2]];
naiveh(P)=log(max(abs(numerator(P[1])),denominator(P[1])));
CKF="out/s07b_enum_ckpt.gp";
ck_done=[];
iferr(read(CKF),err,print("no checkpoint file yet"));
print("checkpoint blocks already done: ",#ck_done);
sqfd=[1,3,m0,3*m0,A,3*A,m0*A,3*m0*A];
ckchk(pts)=lift(Mod(sum(i=1,#pts,i*(numerator(pts[i][1])+7*denominator(pts[i][1])+13*numerator(pts[i][2]))),2^61-1));
sgn_s=concat(sqfd,-sqfd);
enumpts(Hl)={
  my(eH=exp(Hl), res=List(), cnt=0);
  foreach(sgn_s, s,
    my(k=select(v->v[1]==Hl && v[2]==s, ck_done), pts);
    if(#k, pts=k[1][3],
      my(t0=getabstime(), Mmax=floor(sqrt((abs(SH)+1)*eH/abs(s)))+1, Dmax=floor(sqrt(eH))+1, Q=s*'X^4+aa*'X^2+bb/s, raw, L=List());
      raw=hyperellratpoints(Q,[Mmax,Dmax]);   \\ AUDIT_B #1/#3: was [Mmax,min(Dmax,Mmax)] (truncated denominators)
      foreach(raw, pt, my(X=pt[1], x=s*X^2, r2, P);
        if(x==0, next);
        r2=x^3+aa*x^2+bb*x; if(!issquare(r2), error("not a square"));
        P=[x, sqrtint(numerator(r2))/sqrtint(denominator(r2))];
        if(!ellisoncurve(E0,P), error("bad point"));
        P=toR(P); if(naiveh(P)<=Hl, listput(L,[P[1],abs(P[2])])));
      pts=Set(Vec(L));
      write(CKF, Str("ck_done=concat(ck_done,[[",Hl,",",s,",",pts,"]]); \\\\ raw=",#raw," cpu_ms=",getabstime()-t0," chk=",ckchk(pts)));
      ck_done=concat(ck_done,[[Hl,s,pts]]));
    foreach(pts,P,listput(res,P)));
  listput(res,[-SH,0]);   \\ the 2-torsion point x=0
  Set(Vec(res))
};
default(realprecision,50);
hQ(q)=log(max(abs(numerator(q)),abs(denominator(q))));
hinf(q)=log(max(1,abs(q)));
j=Er.j; D=Er.disc; b2=Er.b2;
mu=hQ(D)/12+hinf(j)/12+hinf(b2/12)/2+log(if(b2,2,1))/2;
Bs=[2*(hQ(j)/8+hQ(D)/12+0.973), 2*(hQ(j)/12+hQ(D)/12+1.07), 2*(hQ(j)/24+mu+0.973), 2*(mu+1.07)];
Bmax=vecmax(Bs); print("Silverman constants (BSD normalisation) [crude-,crude+,refined-,refined+] = ",Bs,"  B' = ",Bmax);
\\ validation of the enumerator against brute force at small height (x_r = mm/e^2, |mm|,e^2 <= exp(Hv))
Hv=10.5; ev=enumpts(Hv);
bf=List(); eHv=floor(exp(Hv));
{for(e=1,sqrtint(eHv), for(mm=-eHv,eHv, if(gcd(mm,e)!=1,next); my(x=mm/e^2, r=x^3+Er.a2*x^2+Er.a4*x+Er.a6);
   if(r>=0 && issquare(r), listput(bf,[x,sqrtint(numerator(r))/sqrtint(denominator(r))]))));}
bf=Set(Vec(bf)); print("validation H=10.5:",": enumerator ",#ev," points, brute force ",#bf," points, equal: ",bf==ev);
lam0=2.5; Hl=lam0+Bmax; print("lambda0 = ",lam0,"  search height H = ",Hl,"  exp(H) = ",exp(Hl));
t=getabstime(); r=enumpts(Hl); print("enumeration: ",#r," points up to sign (incl. T'), ",getabstime()-t," ms");
L=List(); foreach(r,P, if(P[2]==0,next); listput(L,[ellheight(Er,P),naiveh(P),P])); L=vecsort(Vec(L),1);
for(i=1,#L,print("  hhat=",L[i][1],"  h=",L[i][2],"  P=",L[i][3]));
lam=min(lam0,L[1][1]); print("PROVED lambda' >= ",lam);
S1=toR([5184,1355400]); S2=toR([-20187,-2906928]);
Rg=matdet(ellheightmatrix(Er,[S1,S2])); print("Reg of eclib-saturated basis {psi(P1), (-20187,-2906928)} = ",Rg);
print("Hermite index bound (2/sqrt3) sqrt(Reg)/lambda = ",(2/sqrt(3))*sqrt(Rg)/lam);
print("ellrank(Er') = ",ellrank(Er));
W=ellsaturation(Er,[toR([5184,1355400]),toR([3822025/1296,38806079435/46656])],100); print("ellsaturation(psi P1, psi P2; 100) -> Reg ratio ",matdet(ellheightmatrix(Er,W))/matdet(ellheightmatrix(Er,[toR([5184,1355400]),toR([3822025/1296,38806079435/46656])])));
print("elltors(E') = ",elltors(E0));
