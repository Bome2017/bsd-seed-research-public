{
S=read("/Users/bsm/BSD_SEED_COMPLETE_BOUND_SCALING_2026-10-20/seed_five/field.gp");
NF=read("/Users/bsm/BSD_SEED_COMPLETE_BOUND_SCALING_2026-10-20/seed_five/nf.gp");
print("SIG_TYPE=",type(S[7]),";VAR=",variable(S[4]),";DEG=",poldegree(lift(S[7])),";DEN=",factor(denominator(lift(S[7]))));
print("INDEX_FACTORS=",factor(NF.index));
print("NF_CERTIFY=",nfcertify(NF));quit;
}
