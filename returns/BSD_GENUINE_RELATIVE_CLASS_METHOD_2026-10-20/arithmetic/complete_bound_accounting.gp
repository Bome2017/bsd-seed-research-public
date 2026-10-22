{
alarm(15);SS=read("support_matrices.gp");PS=read("private_support_result.gp");R2=SS[9];R3=SS[10];OUT=Vec(select(a->a[6]==1,PS[1]));IN=Vec(select(a->a[6]==0,PS[1]));OC=vector(#OUT,j,OUT[j][1]);IC=vector(#IN,j,IN[j][1]);nr=matsize(R2)[1];rk2=matrank(Mod(vecextract(R2,vector(nr,j,j),OC),5));rk3=matrank(Mod(vecextract(R3,vector(nr,j,j),OC),5));
write("complete_bound_accounting_result.gp",[IC,OC,rk2,rk3,8918+#OC-matrank(Mod(R2,5)),8918+#OC-matrank(Mod(R3,5))]);
print("COMPLETE_BOUND_ACCOUNTING_COMPLETE;INSIDE=",#IC,";OUTSIDE=",#OC,";OUTSIDE_RANK2=",rk2,";OUTSIDE_RANK3=",rk3,";RESULTING_GRH_PRESENTATION_BOUNDS=",[8918+#OC-matrank(Mod(R2,5)),8918+#OC-matrank(Mod(R3,5))]);quit;
}
