{
alarm(20);S=read("/Users/bsm/BSD_SEED_COMPLETE_BOUND_SCALING_2026-10-20/seed_five/field.gp");NF=read("/Users/bsm/BSD_SEED_COMPLETE_BOUND_SCALING_2026-10-20/seed_five/nf.gp");F=S[4];B=419775;OUT=List();TOTAL=0;NP=0;
forprime(q=2,B,NP++;my(ds);if(NF.index%q,ds=factormod(F,q,1)[,1],my(ps=idealprimedec(NF,q));ds=vector(#ps,j,ps[j][4]));my(ss=Set(ds));for(i=1,#ss,my(f=ss[i],m=sum(j=1,#ds,ds[j]==f));if(q^f<=B,listput(OUT,[q,f,m]);TOTAL+=m)));
if(TOTAL!=35749||NP!=35373,error("inventory mismatch"));write("norm_inventory_result.gp",[B,TOTAL,NP,Vec(OUT)]);print("NORM_INVENTORY_COMPLETE;PRIME_IDEALS=",TOTAL,";ROWS=",#OUT);quit;
}
