\\ Same as s04b_pari.gp but lambda0 = 4.2 (> the smallest height found, 4.1285): determines lambda exactly.
read("scripts/s04b_enum_lib.gp");
default(realprecision,40);
hQ(q)=log(max(abs(numerator(q)),abs(denominator(q))));
hinf(q)=log(max(1,abs(q)));
j=Er.j; D=Er.disc; b2=Er.b2; mu=hQ(D)/12+hinf(j)/12+hinf(b2/12)/2+log(if(b2,2,1))/2; BS973=2*(hQ(j)/24+mu+0.973);
lam0=4.2; Hl=lam0+BS973; print("B_S=",BS973," lambda0=",lam0," H=",Hl);
t=getabstime(); r=enumpts(Hl); print("enumeration: ",#r[1]," points up to sign (incl. T); raw ",r[2],"  (",getabstime()-t," ms)");
L=List(); foreach(r[1],P, if(P[2]==0,next); listput(L,[ellheight(Er,P),P]));
L=vecsort(Vec(L),1); for(i=1,min(6,#L),print("  hhat=",L[i][1],"  P=",L[i][2]));
print("points with hhat < 4.2: ",#select(v->v[1]<4.2,L));
lam=L[1][1]; Rg=matdet(ellheightmatrix(Er,[[A-7578,6*n0*A],[36*n0^2-7578,12*n0*(m0-2*n0^2)]]));
print("lambda = min hhat over non-torsion E(Q) = ",lam,"  (attained; = hhat(P1+P2))");
print("index bound (2/sqrt3) sqrt(Reg)/lambda = ",(2/sqrt(3))*sqrt(Rg)/lam);
