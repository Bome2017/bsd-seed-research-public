\\ Consistency check of the enumeration: every combination a*P1+b*P2+e*T (|a|,|b|<=6) of naive height <= H must be in enumpts(H).
read("scripts/s04b_enum_lib.gp");
default(realprecision,40);
Q1=toR([A,6*n0*A]); Q2=toR([36*n0^2,12*n0*(m0-2*n0^2)]); TT=[-SH,0];
{
foreach([18.979,20.679], H,
  r=enumpts(H)[1]; miss=0; inside=0; L=List();
  for(a=-6,6, for(b=-6,6, for(e=0,1,
     P=elladd(Er, elladd(Er, ellmul(Er,Q1,a), ellmul(Er,Q2,b)), ellmul(Er,TT,e));
     if(P==[0], next);
     Pp=[P[1],abs(P[2])];
     if(naiveh(Pp)<=H, inside++; listput(L,Pp); if(!setsearch(r,Pp), miss++; print("MISSING: ",[a,b,e]," ",Pp))))));
  L=Set(Vec(L));
  print("H=",H,": combos with naive h'<=H (distinct up to sign): ",#L,"  enumerated: ",#r,"  missing: ",miss,"  enumerated-but-not-a-small-combo: ",#setminus(r,L));
  foreach(setminus(L,[]),P, print("   ",P,"  h'=",naiveh(P)))
);
}
