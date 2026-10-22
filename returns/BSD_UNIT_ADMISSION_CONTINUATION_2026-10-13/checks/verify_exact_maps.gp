alarm(40);
D=read("../data/stage1_data.gp");G=D[1];TM=D[4];AM=D[6];
R=read("../inputs/previous/seed3/actual_representatives.gp");f=R[5];tau=Mod(-w,f);
TR=read("../data/tau_cube_roots.gp");AR=read("../data/actual_cube_roots.gp");
{for(j=1,15,if(subst(lift(G[j]),w,tau)!=TR[j]^3*prod(i=1,15,G[i]^lift(TM[i,j])),error("tau identity")));for(j=1,4,if(R[8][j]!=AR[j]^3*prod(i=1,15,G[i]^lift(AM[i,j])),error("actual coordinate identity")));}
AP=D[10];RR=List();
{for(k=1,#AP,my(q=AP[k][1],rt=AP[k][2],zz=znprimroot(q)^((q-1)/3),row=vector(15),ok=1);if(subst(f,w,Mod(rt,q))!=0,error("bad reduction root"));for(j=1,15,if(denominator(content(lift(G[j])))%q==0,ok=0;break);my(t=subst(lift(G[j]),w,Mod(rt,q)));if(t==0,ok=0;break);t=t^((q-1)/3);if(t==1,row[j]=0,if(t==zz,row[j]=1,if(t==zz^2,row[j]=2,error("cubic character")))));if(ok,listput(RR,row)));}
RR=Mod(matrix(#RR,15,i,j,RR[i][j]),3);if(matrank(RR)!=15,error("source independence"));
UB=matconcat([vector(15,i,i==12)~,vector(15,i,i==14)~,AM[,1],AM[,3]-AM[,4]]);
if(matrank(RR*UB)!=4,error("four units independent"));
if(matrank(RR*AM)!=4,error("actual classes independent"));
print("LITERAL_CUBE_IDENTITIES=19");print("INDEPENDENT_RESIDUE_ROWS=",matsize(RR)[1],";SOURCE_RANK=15;UNIT_BASIS_RANK=4");
C=read("../data/affine_norm_certificate.gp");
NFb=nfinit(C[1]);MM=matrix(3,3,i,j,polcoef(lift(Mod(x,C[4])*Mod(x,C[4])^(j-1)),i-1,x));
Mof(a)=sum(i=0,2,polcoef(lift(a),i,x)*MM^i);
Wmatrix=Mof(C[5]);
{for(j=1,4,my(aa=lift(R[8][j]),M=sum(i=0,poldegree(aa,w),polcoef(aa,i,w)*Wmatrix^i));if(matdet(M)!=C[6][j] || C[7][j]^3!=C[6][j],error("matrix norm or cube disagreement")));}
print("AFFINE_NORM_MULTIPLICATION_MATRIX_REPLAY=4");print("EXACT_MAP_REPLAY_PASS");quit;
