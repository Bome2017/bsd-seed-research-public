alarm(30);setrand(20261020);read("../../lib/cubinv.gp");read("../../lib/classimg.gp");read("../../lib/selmer.gp");
E=ellinit([1,-1,1,-39,102]);P=[[4/1,-3/1],[2/1,4/1]];FD=field3(E);B=bnfinit(FD[1],1);nf=B.nf;T=torsT(E,nf);tau=tauL(nf,E,T);ix=select(i->B.cyc[i]%3==0,[1..#B.cyc]);CA=matrix(#ix,#ix);
{for(j=1,#ix,my(J=idealpow(nf,B.gen[ix[j]],B.cyc[ix[j]]/3),v=bnfisprincipal(B,nfgaloisapply(nf,tau,J),0));for(i=1,#ix,if(v[ix[i]]%(B.cyc[ix[i]]/3),error("class action"));CA[i,j]=v[ix[i]]/(B.cyc[ix[i]]/3)));}
CF=matker(Mod(CA+matid(#ix),3));PC=vector(#P,j,ftan(E,T,P[j]));PF=vector(#P,j,idealfactor(nf,PC[j]));PL=List();
{for(j=1,#P,for(i=1,matsize(PF[j])[1],my(pr=PF[j][i,1],known=0);for(k=1,#PL,if(pr==PL[k],known=1));if(!known,listput(PL,pr))));}
PL=Vec(PL);V=matrix(#PL,#P,i,j,nfeltval(nf,PC[j],PL[i]));K=matker(Mod(V,3));CP=matrix(#ix,#K);
{for(j=1,#K,my(v=V*lift(K[,j]),J=matid(8),lc);for(i=1,#PL,if(v[i]%3,error("point ideal val"));J=idealmul(nf,J,idealpow(nf,PL[i],v[i]/3)));lc=bnfisprincipal(B,J,0);for(i=1,#ix,if(lc[ix[i]]%(B.cyc[ix[i]]/3),error("point class denominator"));CP[i,j]=lc[ix[i]]/(B.cyc[ix[i]]/3)));}
CP=Mod(CP,3);if(Mod(CA+matid(#ix),3)*CP!=0*CP,error("point class notfaithful"));
print("CLASS=",B.cyc,";FAITHFUL_DIM=",#CF,";POINT_ORDINARY_DIM=",#K,";POINT_CLASS_RANK=",matrank(CP),";CLASS_ACTION=",CA,";POINT_CLASSES=",lift(CP));
write("arithmetic.gp",[E,P,FD,T,tau,ix,CA,CF,PC,PL,V,K,CP]);writebin("provisional_bnf.bin",B);
if(#CF>matrank(CP),print("UNOCCUPIED_CLASS_SELECTED"),print("POINT_OCCUPIED_ONLY"));quit;
