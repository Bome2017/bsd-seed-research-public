alarm(110); read("cubinv.gp");read("classimg.gp");read("selmer.gp");gettime();
nf=read("/Users/bsm/BSD_STRUCTURAL_DISCOVERY_2026-10-13/seed3/nf_only.gp");
D=read("stage1_data.gp");G=D[1];TAU=D[4];AC=D[6];tau=Mod(-w,nf.pol);
B0=read("/Users/bsm/BSD_STRUCTURAL_DISCOVERY_2026-10-13/seed3/actual_representatives.gp");AA=B0[8];
roots=List();
{for(j=1,15,my(a=tauapply(nf,tau,G[j])/prod(i=1,15,G[i]^lift(TAU[i,j])),rr=nfroots(nf,X^3-a));if(#rr<1,error("tau quotient not cube"));if(rr[1]^3!=a,error("tau cube identity"));listput(roots,rr[1]);write("tau_cube_checkpoints.gp",[j,rr[1]]);print("TAU_EXACT_COLUMN=",j,"; elapsed_ms=",gettime()));}
write("tau_cube_roots.gp",Vec(roots));aroots=List();
{for(j=1,4,my(a=AA[j]/prod(i=1,15,G[i]^lift(AC[i,j])),rr=nfroots(nf,X^3-a));if(#rr<1,error("actual coordinate quotient not cube"));if(rr[1]^3!=a,error("actual cube identity"));listput(aroots,rr[1]);write("actual_cube_checkpoints.gp",[j,rr[1]]);print("ACTUAL_EXACT_COLUMN=",j,"; elapsed_ms=",gettime()));}
write("actual_cube_roots.gp",Vec(aroots));print("EXACT_MAPS_COMPLETE");quit;
