default(nbthreads,1);
{E=ellinit([0,-1,1,-10,-20]); k=0; for(d=2,10000,if(k>=60,break); if(d%4!=1 || !issquarefree(d) || gcd(d,55)!=1 || kronecker(d,5)!=-1,next); k++; F=ellminimalmodel(elltwist(E,d)); r=ellrank(F,1); print([k,d,ellglobalred(F)[1],F[1..5],ellap(F,5),r]); ); print("DONE ",k);}
quit;
