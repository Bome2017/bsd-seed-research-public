install("bsd_mixed_collect","GG","bsdmixed","/Users/bsm/BSD_RANK_TWO_JOINT_CONTINUATION_2026-10-18_PARI_BUILD/libbsdmixed.dylib");
NF=read("../twist_source/nf.gp");AM=read("../twist_source/direct_units/basis_scalar_matrix.gp");
print("HARVEST_FIELD=",NF.pol);default(debug,1);alarm(117);
B=bsdmixed(NF,AM^3);print("BNF_COMPLETE=",B.clgp);quit;
