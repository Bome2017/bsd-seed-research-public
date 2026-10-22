alarm(90);gettime();D=read("inputs/data.gp");E=D[1];fA=D[3];T=D[5];G=D[6];ng=#G;SC=D[9]+matid(ng);S=matker(SC);if(#S!=5,error("scalar source dimension"));
GC=matker(matconcat([SC;D[13]]));if(#GC!=3,error("retained full candidate kernel dimension"));
SA=-E.c4/48;SB=-E.c6/864;XT=T[1]+E.b2/12;YT=T[2]+(E.a1*T[1]+E.a3)/2;
coeffcol(v)=vector(8,i,polcoef(lift(v),i-1,w))~;
BT=matrix(8,8,i,j,polcoef(lift(YT^(j-1)),i-1,w));ww=matsolve(BT,coeffcol(Mod(w,fA)));
fB=z^8-54*E.c4*z^4+216*E.c6*z^2-243*E.c4^2;if(!polisirreducible(fB),error("dual field reducible"));NF=nfinit(fB);m=Mod(z,fB)/6;
GG=x^3-m^2*x^2+(m^4+2*SA)*x-(m^6+2*SA*m^2-4*SB);YY=Mod(m*x-(m^4+SA)/(2*m),GG);WW=sum(i=1,8,ww[i]*YY^(i-1));
if(subst(fA,w,WW)!=0,error("source field map"));if(subst(lift(XT),w,WW)!=Mod(x,GG)||subst(lift(YT),w,WW)!=YY,error("torsion map"));if(Mod(3*x^4+6*SA*x^2+12*SB*x-SA^2,GG)!=0,error("division polynomial"));
eltof(v)=prod(i=1,ng,G[i]^lift(v[i]));
u(a)=norm(subst(lift(a),w,WW));
AE=vector(#S,j,eltof(S[,j]));NV=vector(#S,j,u(AE[j]));CE=vector(#GC,j,eltof(GC[,j]));CN=vector(#GC,j,u(CE[j]));RT=vector(#GC,j,[]);
write("norm_data.gp",[S,AE,NV,fB,GG,WW,GC,CE,CN]);write("dual_nf.gp",NF);print("ALL_FIVE_NORMS_CONSTRUCTED;MS=",gettime());
{for(j=1,#GC,RT[j]=nfroots(NF,x^3-CN[j]);if(#RT[j]>1,error("line field unexpected cube roots"));if(#RT[j]&&RT[j][1]^3!=CN[j],error("cube witness wrong"));write("cube_checkpoint.gp",[j,RT[j]]);print("CANDIDATE_",j,"_CUBE_ROOT_COUNT=",#RT[j],";MS=",gettime()));}
write("candidate_cube_roots.gp",RT);print("COMPLETE_NORM_FIRST_TEST_FINISHED");quit;
