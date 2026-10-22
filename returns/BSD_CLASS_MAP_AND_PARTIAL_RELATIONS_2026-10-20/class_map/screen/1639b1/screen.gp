alarm(12);setrand(20261020);read("../../lib/cubinv.gp");read("../../lib/classimg.gp");read("../../lib/selmer.gp");
E=ellinit([1,-1,1,-6,6]);P=[[2/1,-1/1],[1/1,0/1]];for(i=1,#P,if(!ellisoncurve(E,P[i]),error("point")));
FD=field3(E);B=bnfinit(FD[1],1);ix=select(i->B.cyc[i]%3==0,[1..#B.cyc]);print("CLASS=",B.cyc,";DIM=",#ix);
if(#ix<2,print("SCREEN_COMPLETE_NO_MULTIPLE_CLASS");quit);
nf=B.nf;T=torsT(E,nf);tau=tauL(nf,E,T);CA=matrix(#ix,#ix);
{for(j=1,#ix,my(J=idealpow(nf,B.gen[ix[j]],B.cyc[ix[j]]/3),v=bnfisprincipal(B,nfgaloisapply(nf,tau,J),0));for(i=1,#ix,if(v[ix[i]]%(B.cyc[ix[i]]/3),error("class action nonintegral"));CA[i,j]=v[ix[i]]/(B.cyc[ix[i]]/3)));}
F=matker(Mod(CA+matid(#ix),3));print("FAITHFUL_DIM=",#F,";ACTION=",CA);
if(#F>=2,writebin("provisional_bnf.bin",B);write("context.gp",[E,P,FD,T,tau,ix,CA,F]);print("SCREEN_SELECTED_PROVISIONAL"),print("SCREEN_COMPLETE_NO_MULTIPLE_FAITHFUL_CLASS"));quit;
