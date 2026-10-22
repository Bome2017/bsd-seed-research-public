install("bsd_lowmem_init","G","bsd_lowmem_init","./libbsd_profile.dylib");
{
alarm(42);setdebug("bnf",1);gettime();
NF=read("/Users/bsm/BSD_SEED_COMPLETE_BOUND_SCALING_2026-10-20/seed_five/nf.gp");
F=read("/Users/bsm/BSD_SEED_COMPLETE_BOUND_SCALING_2026-10-20/seed_five/field.gp")[4];
if(NF.pol!=F,error("seed field binding"));
print("CHANGED_SEED_BEGIN;TECH=[0.02,0,4];EXACT_FLAG=1");
B=bsd_lowmem_init(NF);
writebin("profile_seed_bnf.bin",B);
write("profile_seed_class.gp",[B.cyc,B.no,B.reg]);
print("PROFILE_SEED_BNF_COMPLETE;CLASS=",B.cyc,";MS=",gettime());
quit;
}
