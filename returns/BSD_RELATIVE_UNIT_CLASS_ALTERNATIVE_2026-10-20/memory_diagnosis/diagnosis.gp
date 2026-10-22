{
alarm(57);setdebug("bnf",2);gettime();
F=read("/Users/bsm/BSD_SEED_COMPLETE_BOUND_SCALING_2026-10-20/seed_five/field.gp")[4];
print("DIAGNOSIS_BEGIN_ORIGINAL_BNF");
B=bnfinit(F,1);
writebin("diagnosis_bnf.bin",B);
print("DIAGNOSIS_BNF_COMPLETE;MS=",gettime());quit;
}
