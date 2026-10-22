install("bsd_partial_collect","G","bsdpartial","/Users/bsm/BSD_RANK_TWO_JOINT_CONTINUATION_2026-10-18_PARI_BUILD/libbsdpartial.dylib");
NF=read("/Users/bsm/BSD_RANK_TWO_JOINT_CONTINUATION_2026-10-18/twist_source/nf.gp");
print("HARVEST_FIELD=",NF.pol);default(debug,2);alarm(117);
B=bsdpartial(NF);
print("BNF_COMPLETE=",B.clgp);quit;
