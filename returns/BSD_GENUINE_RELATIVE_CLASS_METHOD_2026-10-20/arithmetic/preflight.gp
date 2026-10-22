read("relative_setup.gp");
{
alarm(110);gettime();relative_setup();
if(#ORB==0,error("no faithful split prime orbit"));
for(i=1,min(2,#ORB),
  ID=idealpow(NF,ORB[i][2],96);C=contentideal(ID);J=idealdiv(NF,ID,C);
  print("REDUCTION_BEGIN;ORBIT=",i,";NORM_DIGITS=",#Str(idealnorm(NF,J)));
  R=shortstep(J,vector(14));
  write("preflight_rows.gp",[i,ID,C,J,R]);
  print("REDUCTION_EXACT;ORBIT=",i,";OLD_NORM_DIGITS=",#Str(idealnorm(NF,J)),";NEW_NORM_DIGITS=",#Str(idealnorm(NF,R[1])),";DECREASE=",idealnorm(NF,R[1])<idealnorm(NF,J),";MULTIPLIER_SIGN=",R[4])
);
print("RELATIVE_PREFLIGHT_COMPLETE;MS=",gettime());quit;
}
