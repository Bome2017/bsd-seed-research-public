{
alarm(55);gettime();
NF=read("/Users/bsm/BSD_SEED_COMPLETE_BOUND_SCALING_2026-10-20/seed_five/nf.gp");SG=read("/Users/bsm/BSD_RELATIVE_UNIT_CLASS_ALTERNATIVE_2026-10-20/relative_source/fields.gp")[3];TA=subst(lift(SG),variable(NF.pol),SG);
BR=readvec("../arithmetic/batch_rows.gp");D=read("../arithmetic/support_matrices.gp");PM=D[2];EV=D[8];KD=read("../arithmetic/integer_kernel_data.gp");H=KD[1];K=KD[2];
if(matsize(H)!=[392,743] || matsize(K)!=[392,80],error("kernel dimensions"));
for(i=1,196,my(v=Vec(EV[i,]),a=vector(743),b=vector(743));for(j=1,743,a[j]+=v[j];a[PM[PM[j]]]-=v[j]);for(j=1,743,b[PM[j]]=a[j]);if(a!=Vec(H[2*i-1,]) || b!=Vec(H[2*i,]),error("anti divisor map")));
if(H~*K!=matrix(743,80) || matrank(Mod(H,5))!=312 || matrank(Mod(K,5))!=80,error("full rational kernel certificate"));
V=vector(392);DONE=vector(392);POS=0;NEG=0;
for(j=1,80,my(u=Mod(1,NF.pol));for(i=1,392,if(K[i,j],if(!DONE[i],my(a=BR[(i+1)\2][5]);if(i%2==0,a=subst(lift(a),variable(NF.pol),SG));V[i]=a/subst(lift(a),variable(NF.pol),TA);DONE[i]=1);u*=V[i]^K[i,j]));if(u==1,POS++,if(u==-1,NEG++,error("nontrivial unit unexpectedly found"))));
if(POS!=78 || NEG!=2,error("unit sign count"));
write("replay_unit_kernel_result.gp",[392,743,312,80,POS,NEG]);print("INDEPENDENT_UNIT_KERNEL_REPLAY_COMPLETE;RANK=312;KERNEL=80;PLUS_ONE=",POS,";MINUS_ONE=",NEG,";MS=",gettime());quit;
}
