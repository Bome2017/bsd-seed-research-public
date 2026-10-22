read("relative_setup.gp");
{
alarm(115);gettime();relative_setup();SS=read("support_matrices.gp");B=SS[1];PM=SS[2];EV=SS[8];nr=matsize(EV)[1];nc=#B;
H=matrix(2*nr,nc);for(i=1,nr,for(j=1,nc,H[2*i-1,j]+=EV[i,j];H[2*i-1,PM[PM[j]]]-=EV[i,j]));
for(i=1,nr,for(j=1,nc,H[2*i,PM[j]]=H[2*i-1,j]));
PF=List();for(j=1,#B,if(ispower(idealnorm(NF,B[j]),5),listput(PF,j)));
print("INTEGER_KERNEL_START;ROWS=",2*nr,";COLS=",nc,";PERFECT_FIFTH_NORMS=",Vec(PF));
KK=matker(mattranspose(H));
for(j=1,matsize(KK)[2],KK[,j]*=denominator(KK[,j]));
if(H~*KK!=matrix(nc,matsize(KK)[2]),error("integer kernel"));
KS=vector(matsize(KK)[2],j,[sum(i=1,2*nr,abs(KK[i,j])),vecmax(abs(KK[,j])),j]);KS=vecsort(KS,1);
write("integer_kernel_data.gp",[H,KK,KS,Vec(PF)]);
print("INTEGER_KERNEL_COMPLETE;RATIONAL_RANK=",2*nr-matsize(KK)[2],";KERNEL_COLS=",matsize(KK)[2],";SMALL_KERNELS=",select(v->v[1]<=100&&v[2]<=30,KS),";MS=",gettime());quit;
}
