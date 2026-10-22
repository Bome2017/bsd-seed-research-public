{
alarm(55);gettime();
NF=read("/Users/bsm/BSD_SEED_COMPLETE_BOUND_SCALING_2026-10-20/seed_five/nf.gp");GS=read("../arithmetic/geometric_support.gp");GD=read("../arithmetic/geometric_rank_data.gp");UK=read("../arithmetic/geometric_unit_kernel.gp");B=GS[8];PM=GS[10];AA=GS[4];EV=GD[4];NC=#GD[7]+#GD[8];SG=GS[2];SM=GS[3];
for(j=1,#B,if(idealnorm(NF,B[j])!=GS[9][j] || idealhnf(NF,SM*B[j])!=B[PM[j]],error("atom scalar identity"));for(k=j+1,#B,if(idealadd(NF,B[j],B[k])!=matid(24),error("not coprime atoms"))));
for(i=1,#AA,
 z=matid(24);for(j=1,#B,if(EV[i,j],z=idealmul(NF,z,idealpow(NF,B[j],EV[i,j]))));if(z!=idealhnf(NF,AA[i]) || z!=idealdiv(NF,GS[5][i],GS[6][i]),error("divisor reconstruction"));
 si=4*((i-1)\4)+((i-1+1)%4)+1;if(subst(lift(AA[i]),variable(NF.pol),SG)!=AA[si],error("element scalar orbit"));
 for(e=2,3,rr=vector(NC);for(j=1,#B,if(GD[2][j],rr[GD[2][j]]+=e^GD[3][j]*EV[i,j]));if(lift(Mod(rr,5))!=GD[e+3][i,],error("projection")))
);
HH=matrix(#AA,#B,i,j,EV[i,j]-EV[i,PM[PM[j]]]);if(HH!=UK[1] || HH~*UK[2]!=matrix(#B,matsize(UK[2])[2]),error("kernel"));
for(j=1,matsize(UK[2])[2],uu=Mod(1,NF.pol);for(i=1,#AA,if(UK[2][i,j],ti=4*((i-1)\4)+((i-1+2)%4)+1;uu*=(AA[i]/AA[ti])^UK[2][i,j]));if(uu!=1,error("nontrivial unit")));
SC=GD[9];for(i=1,#SC,r=SC[i];if(idealmul(NF,r[5],r[6])!=B[r[2]] || idealnorm(NF,r[6])!=r[7],error("support split"));ff=r[4];if(prod(j=1,matsize(ff)[1],ff[j,1]^ff[j,2])!=r[3],error("norm factorization")));
write("geometric_matrix_export.json",[vector(matsize(GD[5])[1],i,Vec(GD[5][i,])),vector(matsize(GD[6])[1],i,Vec(GD[6][i,])),GD[7],GD[8],vector(matsize(HH)[1],i,Vec(HH[i,])),vector(matsize(UK[2])[1],i,Vec(UK[2][i,])),vector(#SC,i,[SC[i][1],SC[i][2],SC[i][3],vector(matsize(SC[i][4])[1],j,Vec(SC[i][4][j,])),SC[i][7]])]);
print("INDEPENDENT_GEOMETRIC_REPLAY_PASS;ELEMENTS=",#AA,";ATOMS=",#B,";UNIT_PRODUCTS=",matsize(UK[2])[2],";MS=",gettime());quit;
}
