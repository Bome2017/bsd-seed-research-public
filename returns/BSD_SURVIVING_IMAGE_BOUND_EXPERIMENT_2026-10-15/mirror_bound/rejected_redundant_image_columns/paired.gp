alarm(60);gettime();read("inputs/lib/cubinv.gp");read("inputs/lib/classimg.gp");read("inputs/lib/selmer.gp");A=read("inputs/A_data.gp");B=read("inputs/B_data.gp");NA=read("inputs/A_norms.gp");NB=read("inputs/B_norms.gp");NFA=read("inputs/A_nf.gp");NFB=read("inputs/B_nf.gp");SA=NA[5];SB=NB[1];VA=NA[7];VB=NB[3];
IAB=nfisincl(NA[2],B[3]);IBA=nfisincl(NB[4],A[3]);if(#IAB!=2||#IBA!=2,error("mirror field iso count"));iab=Mod(IAB[1],B[3]);iba=Mod(IBA[1],A[3]);if(subst(NA[2],z,iab)!=0||subst(NB[4],z,iba)!=0,error("field isomorphism"));
FAB=vector(#VA,j,subst(lift(VA[j]),z,iab));FBA=vector(#VB,j,subst(lift(VB[j]),z,iba));
PB=phimat(NFB,concat(B[6],FAB),B[18]);PA=phimat(NFA,concat(A[6],FBA),A[18]);
GB=matrix(matsize(PB)[1],#B[6],i,j,PB[i,j]);GA=matrix(matsize(PA)[1],#A[6],i,j,PA[i,j]);NBV=matrix(matsize(PB)[1],#FAB,i,j,PB[i,j+#B[6]]);NAV=matrix(matsize(PA)[1],#FBA,i,j,PA[i,j+#A[6]]);
if(matrank(GA)!=#A[6]||matrank(GB)!=#B[6],error("source rank"));MAB=matsolve(GB,NBV);MBA=matsolve(GA,NAV);if(GB*MAB!=NBV||GA*MBA!=NAV,error("source coordinate existence"));
RTAB=vector(#FAB);RTBA=vector(#FBA);
{for(j=1,#FAB,my(r=nfroots(NFB,X^3-FAB[j]/prod(i=1,#B[6],B[6][i]^lift(MAB[i,j]))));if(#r!=1,error("A to B literal coordinate"));RTAB[j]=r[1]);for(j=1,#FBA,my(r=nfroots(NFA,X^3-FBA[j]/prod(i=1,#A[6],A[6][i]^lift(MBA[i,j]))));if(#r!=1,error("B to A literal coordinate"));RTBA[j]=r[1]);}
CAB=matsolve(SB,MAB);CBA=matsolve(SA,MBA);if(CBA*CAB!=0*(CBA*CAB)||CAB*CBA!=0*(CAB*CBA),error("norm composite nonzero"));
KA=SA*matker(CAB);KB=SB*matker(CBA);IA=MBA;IB=MAB;KH=KB*matker(B[7]*KB);IH=IB*matker(B[7]*IB);UC=if(#IH,B[23]*matsolve(B[8],IH),matrix(1,0));
print("RANKS=",[matrank(CAB),matrank(CBA)],";HOMOLOGY=",[#KA-matrank(IA),#KB-matrank(IB)],";MIRROR_IMAGE_VALUATION=",matrank(B[7]*IB),";IMAGE_H0=",#IH,";IMAGE_CLASS=",matrank(UC));
write("paired_certificate.gp",[iab,iba,FAB,FBA,MAB,MBA,RTAB,RTBA,CAB,CBA,KA,KB,IA,IB,KH,IH,UC]);
jm(A)=vector(matsize(A)[1],i,vector(matsize(A)[2],j,lift(A[i,j])));
write("paired.json",Str("{\"A_scalar_basis\":",jm(SA),",\"B_scalar_basis\":",jm(SB),",\"A_to_B_full\":",jm(MAB),",\"B_to_A_full\":",jm(MBA),",\"A_to_B_scalar\":",jm(CAB),",\"B_to_A_scalar\":",jm(CBA),",\"A_norm_kernel\":",jm(KA),",\"B_norm_kernel\":",jm(KB),",\"B_image_valuations\":",jm(B[7]*IB),",\"B_image_H0\":",jm(IH),",\"B_image_class\":",jm(UC),",\"B_class_line\":",jm(KH),"}"));print("PAIRED_NORM_CERTIFICATE_COMPLETE;MS=",gettime());quit;
