default(parisizemax,1000000000);
alarm(90);read("../selmer.gp");
D=read("data.gp");nf=read("nf.gp");E=D[1];T=D[5];G=D[6];ps=D[4];
{scan(E,nf,T,G,avoid)=my(fL=nf.pol,p=3,fl=vector(#G,j,flat(nf,G[j])),blocks=List(),skips=List());
 while(#blocks<6 && p<100000,p=nextprime(p+1);if(p>100000,break);if(p%3!=1||setsearch(avoid,p)||poldisc(fL)%p==0,next);
  my(rs=polrootsmod(fL,p));if(#rs!=8,next);
  my(Ep=ellinit(E,p),pts,chi,om=znprimroot(p)^((p-1)/3),ok=1,triples=List());
  iferr(pts=vector(8,i,[subst(lift(lift(T[1])),w,rs[i]),subst(lift(lift(T[2])),w,rs[i])]),er,ok=0);if(!ok,next);
  chi=vector(8,i,vector(#G,j,my(sm=0);for(k=1,#fl[j],my(e=fl[j][k][1],v,u);v=iferr(subst(lift(e),w,rs[i]),er,ok=0;0);if(!ok||v==0,ok=0;break);u=v^((p-1)/3);if(u!=1&&u!=om&&u!=om^2,error("cubic root failed"));sm+=fl[j][k][2]*if(u==1,0,u==om,1,2));sm%3));
  if(!ok,listput(skips,[p,"source factor nonunit"]);next);
  for(i=1,8,if(!ellisoncurve(Ep,pts[i])||ellmul(Ep,pts[i],3)!=[0],error("not torsion")));
  for(i=1,8,for(j=i,8,my(Q=elladd(Ep,pts[i],pts[j]));if(Q==[0],next);my(kq=0);for(k=1,8,if(pts[k]==Q,kq=k));if(!kq,error("sum missing"));listput(triples,[i-1,j-1,kq-1])));
  listput(blocks,[p,lift(rs),lift(pts),lift(om),chi,Vec(triples)]));
 [Vec(blocks),Vec(skips)];}
OUT=scan(E,nf,T,G,ps);write("scan.gpdata",OUT);print("PRIMES=",vector(#OUT[1],i,OUT[1][i][1]));print("FULL_SOURCE_SCAN_COMPLETE");quit;
