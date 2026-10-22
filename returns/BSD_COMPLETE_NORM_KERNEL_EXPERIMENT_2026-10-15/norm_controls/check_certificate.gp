\\ Independent multiplication-matrix norm and exact certificate checker.
alarm(60);
C=read("norms.gp");J=read("norm_kernel.gp");
fA=C[1];fB=C[2];GG=C[3];WW=C[4];S=C[5];AE=C[6];NV=C[7];
RR=J[1];RC=J[2];K=J[3];SK=J[4];KV=J[5];KR=J[6];
if(J[7]!=1,error("producer did not certify complete kernel"));
ng=#D[6];SC=D[9]+matid(ng);
if(SC*S!=0*(SC*S)||#S!=#matker(SC)||matrank(S)!=#S,error("incomplete scalar basis"));
if(subst(fA,w,WW)!=0,error("source algebra embedding"));
if(!polisirreducible(fB),error("line field polynomial reducible"));
NN=vector(#AE);
{
for(j=1,#AE,
  if(AE[j]!=prod(i=1,ng,D[6][i]^lift(S[i,j])),error("actual source binding"));
  F=subst(lift(AE[j]),w,WW);
  MM=matrix(3,3,i,k,polcoef(lift(F*Mod(x,GG)^(k-1)),i-1,x));
  NN[j]=matdet(MM);
  if(NN[j]!=NV[j],error("independent determinant norm"))
)
}
{
for(i=1,#RC,
  q=RC[i][1];Rt=RC[i][2];gg=RC[i][3];Row=RC[i][4];
  if(!isprime(q)||q%3!=1,error("residue prime"));
  if(subst(fB,z,Mod(Rt,q))!=0||subst(deriv(fB),z,Mod(Rt,q))==0,error("simple residue place"));
  if(znorder(Mod(gg,q))!=q-1,error("primitive residue generator"));
  rho=Mod(gg,q)^((q-1)/3);
  for(j=1,#NN,
    if(denominator(content(lift(NN[j])))%q==0,error("nonintegral evaluation"));
    Val=subst(lift(NN[j]),z,Mod(Rt,q));
    if(Val==0||Val^((q-1)/3)!=rho^Row[j],error("noncube residue row"));
    if(lift(RR[i,j])!=Row[j],error("stored row binding"))
  )
)
}
if(RR*K!=0*(RR*K)||matrank(K)!=#K||#K+matrank(RR)!=#S,error("complete residue kernel"));
if(SK!=S*K,error("kernel coordinates"));
{
for(j=1,#K,
  NNprod=prod(i=1,#NN,NN[i]^lift(K[i,j]));
  if(KV[j]!=NNprod||KR[j]^3!=NNprod,error("literal kernel cube root"))
)
}
if(D[17]*SK!=0*(D[17]*SK),error("complete norm kernel not retained admissible"));
print("SCALAR_SOURCE_DIM=",#S,";NORM_IMAGE_RANK=",matrank(RR),";COMPLETE_NORM_KERNEL=",#K);
print("INDEPENDENT_DETERMINANT_NORMS=",#AE,";SIMPLE_PLACE_CERTIFICATES=",#RC,";LITERAL_CUBE_ROOTS=",#KR);
print("VALZERO_ON_KERNEL=",D[7]*SK==0*(D[7]*SK));
print("UNIT_CONTAINED=",matrank(matconcat([D[14],SK]))==matrank(D[14]));
print("RETAINED_JOINT_KERNEL_DIM=",#matker(D[17]));
if(#D[2],print("POINT_PLANE_EQUALS=",matrank(matconcat([D[10],SK]))==#K&&matrank(D[10])==#K),print("NO_POINT_DIRECTIONS"));
print("COMPLETE_NORM_CERTIFICATE_PASS");quit;
