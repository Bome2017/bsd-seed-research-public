{
alarm(117);setdebug("bnf",1);gettime();
NF=read("/Users/bsm/BSD_SEED_COMPLETE_BOUND_SCALING_2026-10-20/seed_five/nf.gp");
F=read("/Users/bsm/BSD_SEED_COMPLETE_BOUND_SCALING_2026-10-20/seed_five/field.gp")[4];
if(NF.pol!=F,error("seed field binding"));
print("UNMODIFIED_SEED_BEGIN;TECH=[0.02,0,4];EXACT_FLAG=1");
B=bnfinit(NF,1,[0.02,0,4]);
writebin("unmodified_small_base_bnf.bin",B);
write("unmodified_small_base_class.gp",[B.cyc,B.no,B.reg]);
print("UNMODIFIED_SMALL_BASE_COMPLETE;CLASS=",B.cyc,";MS=",gettime());quit;
}
