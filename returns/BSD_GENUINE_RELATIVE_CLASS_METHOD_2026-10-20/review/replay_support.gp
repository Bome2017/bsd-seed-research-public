{
alarm(55);gettime();
NF=read("/Users/bsm/BSD_SEED_COMPLETE_BOUND_SCALING_2026-10-20/seed_five/nf.gp");SG=read("/Users/bsm/BSD_RELATIVE_UNIT_CLASS_ALTERNATIVE_2026-10-20/relative_source/fields.gp")[3];
BR=readvec("../arithmetic/batch_rows.gp");D=read("../arithmetic/support_matrices.gp");B=D[1];PM=D[2];CYC=D[3];CI=D[4];CP=D[5];OI=D[6];PI=D[7];EV=D[8];R2=D[9];R3=D[10];OV=D[11];
if(#B!=743 || matsize(EV)!=[196,743] || matsize(R2)!=[196,185] || matsize(R3)!=[196,185],error("matrix sizes"));
for(j=1,#B,if(idealhnf(NF,nfgaloisapply(NF,SG,B[j]))!=B[PM[j]],error("scalar atom action")));
for(k=1,#CYC,my(c=CYC[k]);for(j=1,#c,if(PM[c[j]]!=c[j%#c+1],error("cycle order")));if(#c==4,for(j=1,4,if(CI[c[j]]!=CI[c[1]] || CP[c[j]]!=j-1,error("faithful cycle coordinate"))),for(j=1,#c,if(CI[c[j]],error("nonfaithful coordinate retained")))));
for(i=1,#BR,my(J=matid(24),v2=vector(185),v3=vector(185));for(j=1,#B,if(EV[i,j],J=idealmul(NF,J,idealpow(NF,B[j],EV[i,j])));if(CI[j],v2[CI[j]]+=2^CP[j]*EV[i,j];v3[CI[j]]+=3^CP[j]*EV[i,j]));if(J!=idealdiv(NF,BR[i][4],BR[i][7]),error("full divisor-support reconstruction"));if(lift(Mod(v2,5))!=Vec(R2[i,]) || lift(Mod(v3,5))!=Vec(R3[i,]),error("character projection mismatch")));
if(setunion(OI,PI)!=vector(185,j,j) || #setintersect(OI,PI) || #OI!=8,error("private partition"));
write("matrix_audit_input.gp",[OI,PI,vector(#BR,i,Vec(R2[i,])),vector(#BR,i,Vec(R3[i,]))]);
print("INDEPENDENT_SUPPORT_REPLAY_COMPLETE;ROWS=",#BR,";ATOMS=",#B,";FAITHFUL_COLUMNS=185;MS=",gettime());quit;
}
