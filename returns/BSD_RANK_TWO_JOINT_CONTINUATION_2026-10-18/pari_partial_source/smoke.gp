install("bsd_partial_collect","G","bsdpartial","/Users/bsm/BSD_RANK_TWO_JOINT_CONTINUATION_2026-10-18_PARI_BUILD/libbsdpartial.dylib");
default(debug,1); alarm(10); B=bsdpartial(nfinit(x^3-x-1)); print("SMOKE_DONE ",B.clgp);
quit;
