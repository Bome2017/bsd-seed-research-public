\\ AUDIT_B correction #2: lambda0 = 4.2 with the MAXIMUM of all four Silverman constants (B = 20.329), so H = 24.529,
\\ using the corrected full box (scripts/s04b_enum_lib.gp after AUDIT_B #1). Also the combination cross-check at this H.
read("scripts/s04b_enum_lib.gp");
default(realprecision,40);
hQ(q)=log(max(abs(numerator(q)),abs(denominator(q))));
hinf(q)=log(max(1,abs(q)));
j=Er.j; D=Er.disc; b2=Er.b2;
mu=hQ(D)/12+hinf(j)/12+hinf(b2/12)/2+log(if(b2,2,1))/2;
Bs1=2*(hQ(j)/8+hQ(D)/12+0.973); Bs2=2*(hQ(j)/12+hQ(D)/12+1.07); Bm1=2*(hQ(j)/24+mu+0.973); Bm2=2*(mu+1.07);
Bmax=vecmax([Bs1,Bs2,Bm1,Bm2]); print("crude form: ",Bs1," / ",Bs2,"   refined form: ",Bm1," / ",Bm2,"   max = ",Bmax);
lam0=4.2; Hl=lam0+Bmax; print("lambda0 = ",lam0,"  search height H = ",Hl,"  exp(H) = ",exp(Hl));
t=getabstime(); r=enumpts(Hl); print("enumeration: ",#r[1]," points up to sign (incl. T); raw ",r[2],"  (",getabstime()-t," ms)");
L=List(); foreach(r[1],P, if(P[2]==0,next); listput(L,[ellheight(Er,P),naiveh(P),P]));
L=vecsort(Vec(L),1); for(i=1,#L,print("  hhat=",L[i][1],"  h'=",L[i][2],"  P=",L[i][3]));
print("points with hhat < 4.2: ",#select(v->v[1]<4.2,L));
lam=L[1][1]; Rg=matdet(ellheightmatrix(Er,[toR([A,6*n0*A]),toR([36*n0^2,12*n0*(m0-2*n0^2)])]));
print("lambda = min hhat over non-torsion E(Q) = ",lam,"  (attained)");
print("index bound (2/sqrt3) sqrt(Reg)/lambda = ",(2/sqrt(3))*sqrt(Rg)/lam);
Q1=toR([A,6*n0*A]); Q2=toR([36*n0^2,12*n0*(m0-2*n0^2)]); TT=[-SH,0];
{
my(rr=r[1], miss=0, C=List());
for(a=-6,6, for(b=-6,6, for(e=0,1,
   my(P=elladd(Er, elladd(Er, ellmul(Er,Q1,a), ellmul(Er,Q2,b)), ellmul(Er,TT,e)), Pp);
   if(P==[0], next);
   Pp=[P[1],abs(P[2])];
   if(naiveh(Pp)<=Hl, listput(C,Pp); if(!setsearch(rr,Pp), miss++; print("MISSING: ",[a,b,e]," ",Pp))))));
C=Set(Vec(C));
print("crosscheck H=",Hl,": combos |a|,|b|<=6 with naive h'<=H (distinct up to sign): ",#C,"  enumerated: ",#rr,"  missing: ",miss,"  enumerated-but-not-a-small-combo: ",#setminus(rr,C));
}
