alarm(90);read("lib/cubinv.gp");read("lib/classimg.gp");read("lib/selmer.gp");
E=ellinit([1,-1,0,-1367381,615777525]);Pts=[[653,675]];
B=read("bnf.bin");nf=B.nf;fL=nf.pol;ps=[2,3,7,2003];T=torsT(E,nf);tau=tauL(nf,E,T);SL=[];for(i=1,#ps,SL=concat(SL,idealprimedec(nf,ps[i])));
if(!ellisoncurve(E,Pts[1]),error("point binding"));
write("context.gp",[E,Pts,fL,ps,T,tau,SL]);print("CONTEXT_WITH_UNCERTIFIED_BNF_READY");quit;
