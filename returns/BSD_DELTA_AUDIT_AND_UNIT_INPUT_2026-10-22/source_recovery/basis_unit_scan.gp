{
alarm(110);gettime();
NF=read("inputs/nf.gp");
C=read("inputs/field.gp");
SG=C[7];TA=subst(lift(SG),w,SG);
if(NF.pol!=C[4]||#NF.zk!=24,error("field binding"));
if(subst(lift(TA),w,TA)!=Mod(w,NF.pol),error("tau"));
VV=List();seen=Map();CHECKED=0;UNITS=List();REL=List();
for(i=1,24,listput(VV,[i,0,1,0]));
for(i=1,24,for(j=i+1,24,for(c=1,2,for(d=-2,2,if(d==0,next);listput(VV,[i,j,c,d])))));
print("SOURCE_CANDIDATES;COUNT=",#VV);
for(k=1,#VV,
 rr=VV[k];a=NF.zk[rr[1]]*rr[3];if(rr[2],a+=NF.zk[rr[2]]*rr[4]);
 av=nfalgtobasis(NF,a);key=Str(av);if(mapisdefined(seen,key),next);mapput(seen,key,1);
 nn=nfeltnorm(NF,a);CHECKED++;
 if(abs(nn)==1,
   if(denominator(av)!=1||denominator(nfalgtobasis(NF,1/a))!=1,error("unit integrality"));
   aa=Mod(a,NF.pol);b=aa/subst(lift(aa),w,TA);
   if(b*subst(lift(b),w,TA)!=1,error("relative norm"));
   if(denominator(nfalgtobasis(NF,b))!=1||denominator(nfalgtobasis(NF,1/b))!=1,error("relative unit integral"));
   listput(UNITS,[rr,aa,nn]);if(b!=1&&b!=-1,listput(REL,b));
   print("UNIT_FOUND;CANDIDATE=",rr,";NORM=",nn,";RELATIVE_NONTORSION=",b!=1&&b!=-1)
 );
 if(CHECKED%250==0,print("PROGRESS;CHECKED=",CHECKED))
);
write("BASIS_UNIT_RESULT.gp",[CHECKED,Vec(UNITS),Vec(REL)]);
print("BASIS_UNIT_COMPLETE;CHECKED=",CHECKED,";UNITS=",#UNITS,";RELATIVE_NONTORSION=",#REL);quit;
}
