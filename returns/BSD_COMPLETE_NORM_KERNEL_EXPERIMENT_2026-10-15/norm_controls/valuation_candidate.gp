alarm(30);C=read("norms.gp");J=read("norm_kernel.gp");S=C[5];K=J[3];RR=J[1];VK=matker(D[7]*S);
print("SCALAR_VALUATION_ZERO_DIM=",#VK,";EXACT_NORM_KERNEL_DIM=",#K);
print("NORM_EQUALS_VALUATION_ZERO=",#K==#VK&&RR*VK==0*(RR*VK));
print("SCALAR_VALUATION_ROWS=",lift(D[7]*S));
print("VALZERO_NORM_RESIDUES=",lift(RR*VK));
write("valuation_candidate.gpout",[VK,D[7]*S,RR*VK,#K==#VK&&RR*VK==0*(RR*VK)]);
print("VALUATION_CANDIDATE_COMPLETE");quit;
