alarm(30);
read("lib/cubinv.gp");read("lib/classimg.gp");read("lib/selmer.gp");
D=read("data.gp");C=read("affine_norm_certificate.gp");E=D[1];fA=D[3];G=D[6];T=D[5];UB=D[14];SC=D[17];fB=C[1];mm=C[2];GG=C[3];WW=C[4];UE=C[5];UR=C[6];K=C[7];AE=C[8];NV=C[9];RT=C[10];
if(SC*UB*K!=0*(SC*UB*K),error("accepted exponent source mismatch"));
{for(j=1,#UE,if(UR[j]^3!=UE[j]/prod(i=1,#G,G[i]^lift(UB[i,j])),error("unit binding")));}
SA=-E.c4/48;SB=-E.c6/864;
if(subst(fA,w,WW)!=0,error("field embedding"));
if(subst(lift(T[1]+E.b2/12),w,WW)!=Mod(x,GG),error("X embedding"));
if(subst(lift(T[2]+(E.a1*T[1]+E.a3)/2),w,WW)!=Mod(mm*x-(mm^4+SA)/(2*mm),GG),error("Y embedding"));
{for(j=1,#AE,my(F=subst(lift(AE[j]),w,WW),MM=matrix(3,3,i,k,polcoef(lift(F*Mod(x,GG)^(k-1)),i-1,x)),NN=matdet(MM));if(NN!=NV[j]||RT[j]^3!=NN,error("independent determinant cube")));}
print("UNIT_BINDINGS=",#UE,";EXACT_NORM_CUBES=",#AE);print("MULTIPLICATION_MATRIX_NORM_CHECK_PASS");quit;
