{
alarm(177);setdebug("bnf",1);gettime();
NF=read("/Users/bsm/BSD_SEED_COMPLETE_BOUND_SCALING_2026-10-20/seed_five/nf.gp");
F=read("/Users/bsm/BSD_SEED_COMPLETE_BOUND_SCALING_2026-10-20/seed_five/field.gp")[4];
if(NF.pol!=F,error("seed field binding"));
print("RANDOM_RELATION_BEGIN;TECH=[0.02,0,-1];EXACT_FLAG=1");
B=bnfinit(NF,1,[0.02,0,-1]);
writebin("random_relations_bnf.bin",B);
write("random_relations_class.gp",[B.cyc,B.no,B.reg]);
print("RANDOM_RELATION_BNF_COMPLETE;CLASS=",B.cyc,";MS=",gettime());quit;
}
