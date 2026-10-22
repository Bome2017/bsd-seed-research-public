{
alarm(10);gettime();E=read("field.gp")[1];
if(ellap(E,5)!=-2,error("good ordinary nonanomalous5"));
lr=elllocalred(E,2243);
if(valuation(E.disc,2243)!=1||lr[1]!=1||ellap(E,2243)!=1,error("split multiplicative I1"));
print("AT5_A=",ellap(E,5),";AT2243_DELTA_VAL=",valuation(E.disc,2243),";AT2243_AP=",ellap(E,2243),";LOCALRED=",lr);
print("SEED_LOCAL_BINDING_PASS");quit;
}
