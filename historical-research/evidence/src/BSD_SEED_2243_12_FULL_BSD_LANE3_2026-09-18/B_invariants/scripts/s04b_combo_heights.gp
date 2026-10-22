\\ naive heights (reduced model) of all a*P1+b*P2+e*T, |a|,|b|<=6, sorted: shows the gap above 17.05
read("scripts/s04b_enum_lib.gp");
default(realprecision,20);
Q1=toR([A,6*n0*A]); Q2=toR([36*n0^2,12*n0*(m0-2*n0^2)]); TT=[-SH,0];
L=List();
{for(a=-6,6, for(b=-6,6, for(e=0,1, P=elladd(Er, elladd(Er, ellmul(Er,Q1,a), ellmul(Er,Q2,b)), ellmul(Er,TT,e)); if(P==[0],next); listput(L,[naiveh(P),a,b,e]))));}
L=vecsort(Vec(L),1); for(i=1,min(40,#L),print(L[i]));
