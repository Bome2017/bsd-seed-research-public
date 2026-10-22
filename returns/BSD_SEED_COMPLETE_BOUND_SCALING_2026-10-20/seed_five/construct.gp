{
alarm(117); gettime();
E=ellinit([0,-22735,0,106272484,0]);
DP=elldivpol(E,5);
FY=polresultant(DP,w^2-x^3+22735*x^2-106272484*x,x);
FY=FY/content(FY);
if(poldegree(FY)!=24 || !polisirreducible(FY),error("point polynomial"));
write("raw_field.gp",[E,DP,FY]);
print("RAW_DEGREE24_IRREDUCIBLE_MS=",gettime());
RF=polredbest(FY,1); F=RF[1]; YT=RF[2];
if(subst(FY,w,YT)!=0,error("reduction binding"));
Q=gcd(DP,YT^2-x^3+22735*x^2-106272484*x);
if(poldegree(Q)!=1,error("recover x"));
XT=-polcoef(Q,0)/polcoef(Q,1); T=[XT,YT];
if(!ellisoncurve(E,T)||ellmul(E,T,5)!=[0],error("actual torsion point"));
BT=matrix(24,24,i,j,polcoef(lift(YT^(j-1)),i-1,w));
ww=matsolve(BT,vector(24,i,polcoef(lift(Mod(w,F)),i-1,w))~);
T2=ellmul(E,T,2); Y2=T2[2];
SIG=sum(i=1,24,ww[i]*Y2^(i-1));
if(subst(F,w,SIG)!=0,error("scalar field"));
if([subst(lift(XT),w,SIG),subst(lift(YT),w,SIG)]!=T2,error("scalar point"));
S2=subst(lift(SIG),w,SIG); S4=subst(lift(S2),w,S2);
if(S4!=Mod(w,F)||S2==Mod(w,F),error("scalar order4"));
write("field.gp",[E,DP,FY,F,YT,T,SIG]);
print("FIELD_POLYNOMIAL=",F,";REDUCTION_AND_SCALAR_MS=",gettime());
NF=nfinit(F); write("nf.gp",NF);
print("DEGREE=",poldegree(F),";SIGNATURE=",NF.sign,";DISC=",NF.disc,";A5=",ellap(E,5),";NF_MS=",gettime());
print("ACTUAL_SEED_P5_FIELD_AND_SCALAR_PASS");quit;
}
