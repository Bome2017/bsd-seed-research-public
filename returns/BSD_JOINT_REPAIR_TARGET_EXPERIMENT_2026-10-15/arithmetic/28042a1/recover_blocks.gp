alarm(30);read("lib/selmer.gp");B=read("bnf.bin");nf=B.nf;D=read("data.gp");E=D[1];T=D[5];G=D[6];ps=D[4];
{recover(E,nf,T,G,np,avoid)=my(fL=nf.pol,rows=List(),blocks=List(),p=7,got=0,fl=vector(#G,j,flat(nf,G[j])));
 while(got<np,p=nextprime(p+1);if(p%3!=1||setsearch(avoid,p)||poldisc(fL)%p==0,next);
  my(rs=polrootsmod(fL,p));if(#rs!=8,next);
  my(Ep=ellinit(E,p),pts,chi,om=znprimroot(p)^((p-1)/3),ok=1,triples=List(),rblock=List());
  iferr(pts=vector(8,i,[subst(lift(lift(T[1])),w,rs[i]),subst(lift(lift(T[2])),w,rs[i])]),er,ok=0);if(!ok,next);
  chi=vector(8,i,vector(#G,j,my(sm=0);for(k=1,#fl[j],my(e=fl[j][k][1],v,u);v=iferr(subst(lift(e),w,rs[i]),er,ok=0;0);if(!ok||v==0,ok=0;break);u=v^((p-1)/3);if(u!=1&&u!=om&&u!=om^2,error("not cubic root"));sm+=fl[j][k][2]*if(u==1,0,u==om,1,2));sm%3));
  if(!ok,next);
  for(i=1,8,if(!ellisoncurve(Ep,pts[i])||ellmul(Ep,pts[i],3)!=[0],error("not torsion point"))); 
  for(i=1,8,for(j=i,8,my(Q=elladd(Ep,pts[i],pts[j]));if(Q==[0],next);my(kq=0);for(k=1,8,if(pts[k]==Q,kq=k));if(!kq,error("sum not found"));my(row=(chi[i]+chi[j]-chi[kq])%3);listput(rows,row);listput(rblock,row);listput(triples,[i-1,j-1,kq-1])));
  listput(blocks,[p,lift(rs),lift(pts),lift(om),chi,Vec(triples),Vec(rblock)]);got++);
 [Mod(matconcat(Vec(rows)~),3),Vec(blocks)];}
RR=recover(E,nf,T,G,6,ps);if(RR[1]!=D[13],error("additivity replay differs"));write("blocks.gpdata",RR[2]);print("PRIMES=",vector(#RR[2],i,RR[2][i][1]));print("EXACT_BLOCK_REPLAY_PASS");quit;
