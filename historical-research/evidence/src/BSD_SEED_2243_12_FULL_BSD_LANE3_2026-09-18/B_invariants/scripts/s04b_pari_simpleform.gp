\\ Robustness: use the cruder (abstract) form of Silverman 1990 Thm 1.1:
\\   -(1/8)h(j) - (1/12)h(Delta) - 0.973 <= hhat_S(P) - (1/2)h(x(P)) <= (1/12)h(j) + (1/12)h(Delta) + 1.07
\\ and the max of all variants, then redo the lambda0 = 2.5 enumeration.
read("scripts/s04b_enum_lib.gp");
default(realprecision,40);
hQ(q)=log(max(abs(numerator(q)),abs(denominator(q))));
hinf(q)=log(max(1,abs(q)));
j=Er.j; D=Er.disc; b2=Er.b2;
mu=hQ(D)/12+hinf(j)/12+hinf(b2/12)/2+log(if(b2,2,1))/2;
Bs1=2*(hQ(j)/8+hQ(D)/12+0.973); Bs2=2*(hQ(j)/12+hQ(D)/12+1.07); Bm1=2*(hQ(j)/24+mu+0.973); Bm2=2*(mu+1.07);
Bmax=vecmax([Bs1,Bs2,Bm1,Bm2]); print("crude form: ",Bs1," / ",Bs2,"   refined form: ",Bm1," / ",Bm2,"   max = ",Bmax);
lam0=2.5; Hl=lam0+Bmax; print("search height H = ",Hl,"  exp(H) = ",exp(Hl));
t=getabstime(); r=enumpts(Hl); print("enumeration: ",#r[1]," points up to sign (incl. T); raw ",r[2],"  (",getabstime()-t," ms)");
L=List(); foreach(r[1],P, if(P[2]==0,next); listput(L,[ellheight(Er,P),naiveh(P),P]));
L=vecsort(Vec(L),1); for(i=1,#L,print("  hhat=",L[i][1],"  h'=",L[i][2],"  P=",L[i][3]));
print("min hhat over enumerated non-torsion = ",L[1][1]," ; lambda >= ",min(lam0,L[1][1]));
Rg=matdet(ellheightmatrix(Er,[toR([A,6*n0*A]),toR([36*n0^2,12*n0*(m0-2*n0^2)])]));
print("index bound with lambda0=2.5: ",(2/sqrt(3))*sqrt(Rg)/lam0);
