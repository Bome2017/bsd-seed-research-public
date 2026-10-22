{
alarm(25); R=read("/Users/bsm/BSD_RELATIVE_UNIT_CLASS_ALTERNATIVE_2026-10-20/relative_source/fields.gp");A=read("/Users/bsm/BSD_SEED_COMPLETE_BOUND_SCALING_2026-10-20/seed_five/nf.gp");B=read("/Users/bsm/BSD_RELATIVE_UNIT_CLASS_ALTERNATIVE_2026-10-20/relative_source/nf12.gp");Z=R[7];SIG=R[3];IOT=subst(lift(SIG),variable(A.pol),SIG);OUT=List();
if(A.disc/B.disc^2!=2^4*5*4547^6,error("relative discriminant"));
for(ii=1,3,my(q=[2,5,4547][ii],PA=idealprimedec(A,q),PB=idealprimedec(B,q),HB=vector(#PB,j,idealhnf(A,subst(lift(nfbasistoalg(B,PB[j][2])),variable(B.pol),Z))),per=List());
 for(j=1,#PA,my(k=0);for(t=1,#PB,if(idealval(A,HB[t],PA[j])>0,if(k,error("multiple contraction"));k=t));if(!k,error("contraction absent"));my(e=PA[j][3]/PB[k][3],f=PA[j][4]/PB[k][4],h=idealhnf(A,PA[j]),fixed=(nfgaloisapply(A,IOT,h)==h));if(!setsearch([1,2],e)||!setsearch([1,2],f)||e*f>2,error("relative degree"));listput(per,[j,k,PA[j][3],PA[j][4],e,f,fixed]));listput(OUT,[q,Vec(per)]));
write("ramification_result.gp",Vec(OUT));print("RAMIFICATION_COMPLETE=",Vec(OUT));quit;
}
